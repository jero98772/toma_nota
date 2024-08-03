#include <iostream>       // Para operaciones de entrada y salida
#include <vector>         // Para usar el contenedor vector
#include <string>         // Para manejar cadenas de caracteres
#include <filesystem>     // Para operaciones del sistema de archivos
#include <fstream>        // Para operaciones de archivos
#include <sstream>        // Para manejar flujos de entrada/salida de cadenas
#include <unistd.h>       // Para operaciones del sistema Unix
#include <thread>         // Para manejar hilos
#include <chrono>         // Para manejar tiempos de espera
#include <set>            // Para manejar conjuntos (sets)
#include <algorithm>      // Para std::all_of
#include <pwd.h>          // Para obtener información de usuarios
#include <sys/sysinfo.h>  // Para obtener información del sistema
#include <sys/types.h>    // Para tipos de datos del sistema Unix
#include <sys/stat.h>     // Para obtener información sobre archivos
#include <new>


namespace fs = std::filesystem;

// Clase que representa un proceso
class Process {
public:
    int pid;            // Identificador del proceso
    std::string user;   // Usuario propietario del proceso
    std::string name;   // Nombre del proceso
    std::string status; // Estado del proceso
    long memory;        // Uso de memoria del proceso en KB
    double cpu_usage;   // Uso de CPU del proceso en porcentaje

    // Constructor de la clase
    Process(int pid, std::string user, std::string name, std::string status, long memory, double cpu_usage)
        : pid(pid), user(user), name(name), status(status), memory(memory), cpu_usage(cpu_usage) {}
};

bool compareByCpuUsage(const Process& a, const Process& b) {
    return a.cpu_usage > b.cpu_usage;
}

bool compareByMemory(const Process& a, const Process& b) {
    return a.cpu_usage > b.cpu_usage;
}


// Clase que monitorea los procesos del sistema
class ProcessMonitor {
public:
    // Método para obtener la lista de procesos actuales
    std::vector<Process> getProcesses() {
        std::vector<Process> processes;

        // Iterar a través del directorio /proc para obtener información de los procesos
        for (const auto& entry : fs::directory_iterator("/proc")) {
            if (entry.is_directory()) {
                const std::string pid_str = entry.path().filename().string();
                if (is_number(pid_str)) {
                    int pid = std::stoi(pid_str);
                    std::string user = getProcessUser(pid);
                    std::string name = getProcessName(pid);
                    std::string status = getProcessStatus(pid);
                    long memory = getProcessMemory(pid);
                    double cpu_usage = getProcessCpuUsage(pid);
                    processes.emplace_back(pid, user, name, status, memory, cpu_usage);
                }
            }
        }
        return processes;
    }

    // Método para monitorear los procesos en intervalos regulares
    void monitorProcesses(int interval_seconds) {
        std::set<int> previous_pids; // Conjunto de PIDs en la ejecución anterior
        while (true) {
            std::cout << "Medicion..." << std::endl;
            auto processes = getProcesses();
            std::sort(processes.begin(), processes.end(), compareByMemory);

            std::set<int> current_pids; // Conjunto de PIDs en la ejecución actual

            // Detectar nuevos procesos
            for (const auto& process : processes) {
                current_pids.insert(process.pid);
                if (previous_pids.find(process.pid) == previous_pids.end()) {
                    std::cout << "Nuevo proceso detectado: | (ID) " << process.pid << " | (nombre) " << process.name << " | (Estado) " << process.status << std::endl;
                }
            }

            // Detectar procesos terminados
            for (const auto& pid : previous_pids) {
                if (current_pids.find(pid) == current_pids.end()) {
                    std::cout << "<<Proceso terminado: " << pid << ">>"<<std::endl;
                }
            }

            previous_pids = current_pids; // Actualizar el conjunto de PIDs anteriores
            std::this_thread::sleep_for(std::chrono::seconds(interval_seconds)); // Esperar el intervalo especificado
        }
    }

private:
    // Método para verificar si una cadena es un número
    bool is_number(const std::string& s) {
        return !s.empty() && std::all_of(s.begin(), s.end(), ::isdigit);
    }

    // Método para obtener el usuario propietario de un proceso dado su PID
    std::string getProcessUser(int pid) {
        struct stat info; // Estructura para obtener información del archivo
        std::string path = "/proc/" + std::to_string(pid);
        if (stat(path.c_str(), &info) != 0) {
            return "Unknown";
        }
        struct passwd* pw = getpwuid(info.st_uid); // Obtener información del usuario
        return pw ? pw->pw_name : "Unknown";
    }

    // Método para obtener el nombre de un proceso dado su PID
    std::string getProcessName(int pid) {
        std::ifstream comm_file("/proc/" + std::to_string(pid) + "/comm");
        std::string name;
        std::getline(comm_file, name);
        return name;
    }

    // Método para obtener el estado de un proceso dado su PID
    std::string getProcessStatus(int pid) {
        std::ifstream status_file("/proc/" + std::to_string(pid) + "/status");
        std::string line;
        while (std::getline(status_file, line)) {
            if (line.find("State:") == 0) {
                std::istringstream iss(line);
                std::string key, status;
                iss >> key >> status;
                return status;
            }
        }
        return "Unknown";
    }

    // Método para obtener el uso de memoria de un proceso dado su PID
    long getProcessMemory(int pid) {
        std::ifstream status_file("/proc/" + std::to_string(pid) + "/status");
        std::string line;
        while (std::getline(status_file, line)) {
            if (line.find("VmRSS:") == 0) {
                std::istringstream iss(line);
                std::string key;
                long memory;
                iss >> key >> memory;
                return memory;
            }
        }
        return 0;
    }

    // Método para obtener el uso de CPU de un proceso dado su PID
    double getProcessCpuUsage(int pid) {
        struct sysinfo sys_info; // Estructura para obtener información del sistema
        if (sysinfo(&sys_info) != 0) {
            return 0;
        }

        std::ifstream stat_file("/proc/" + std::to_string(pid) + "/stat");
        std::string line;
        std::getline(stat_file, line);
        std::istringstream iss(line);
        std::vector<std::string> stats;
        std::string stat;
        while (iss >> stat) {
            stats.push_back(stat);
        }

        if (stats.size() < 17) {
            return 0;
        }

        long total_time = std::stol(stats[13]) + std::stol(stats[14]); // Tiempo total de CPU usado por el proceso
        double seconds = sys_info.uptime - (std::stol(stats[21]) / sys_info.loads[0]);

        return (total_time / sysconf(_SC_CLK_TCK)) / seconds * 100;
    }
};

// Función para formatear el texto de una celda
std::string formatCell(const std::string& text, int width) {
    if (text.length() >= width) {
        return text.substr(0, width - 1) + " "; // Truncar y añadir espacio si el texto es muy largo
    }
    return text + std::string(width - text.length(), ' '); // Añadir espacios si el texto es más corto
}

// Función para aplicar color al estado según su valor
/*
    Significado de los Estados Comunes de los Procesos:
     R (Running): Ejecutando o en la cola de ejecución.
     S (Sleeping): Dormido, esperando algún evento.
     D (Disk Sleep): Esperando en el disco (no se puede interrumpir).
     Z (Zombie): Proceso terminado, pero aún no recogido por su proceso padre.
     T (Stopped): Detenido, ya sea por una señal de control de trabajo o por depuración.
     I (Idle): Inactivo, esperando a ser utilizado.
*/
std::string textStatus(const std::string& status) {
    if (status == "R") { // Running
        return  status + " - Running"; 
    } else if (status == "S") { // Sleeping
        return  status + " - Sleeping"; 
    } else if (status == "D") { // Disk Sleep
        return  status + " - Disk Sleep"; 
    } else if (status == "Z") { // Zombie
        return  status + " - Zombie";
    } else if (status == "T") { // Stopped
        return  status + " - Stopped";
    } else if (status == "I") { // Stopped
        return  status + " - Inactivo";    
    } else { // Desconocido o cualquier otro estado
        return status + " - (Desconocido)";
    }
}

// Función para imprimir una fila formateada
void printRow(const std::vector<std::string>& columns, const std::vector<int>& widths) {
    for (size_t i = 0; i < columns.size(); ++i) {
        std::cout << formatCell(columns[i], widths[i]);
    }
    std::cout << std::endl;
}

// Función principal
int main() {
    ProcessMonitor monitor; // Crear una instancia de ProcessMonitor
    std::cout << "Listando procesos actuales:" << std::endl;

    // Obtener y listar los procesos actuales
    auto processes = monitor.getProcesses();
    //std::sort(processes.begin(), processes.end(), compareByCpuUsage);
    std::sort(processes.begin(), processes.end(), compareByMemory);

    // Definir anchos de columnas
    std::vector<int> widths = {8, 12, 25, 10, 10, 10};

    // Imprimir encabezados de la tabla
    printRow({"PID", "Usuario", "Nombre", "Estado", "Memoria", "CPU %"}, widths);
    printRow({"--------", "----------", "-------------------------", "----------", "----------", "----------"}, widths);

    // Imprimir datos de los procesos
    for (const auto& process : processes) {
        printRow({
            std::to_string(process.pid),
            process.user,
            process.name,
            textStatus(process.status),
            std::to_string(process.memory) + " KB",
            std::to_string(process.cpu_usage)
        }, widths);
    }

    // Sort the vector in ascending order by cpu_usage

    // Print the sorted vector

    std::cout << "Monitoreando cambios en los procesos..." << std::endl;
    monitor.monitorProcesses(5); // Monitorea cambios en los procesos cada 5 segundos

    return 0;
}
