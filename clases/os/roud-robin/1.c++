#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

struct Process {
    int id;
    int burstTime;
    int remainingTime;
    int waitingTime;
    int turnaroundTime;
};
void roundRobin(vector<Process>& processes, int timeQuantum) {
    int n = processes.size();
    int time = 0;
    bool done = false;
    while(!done){
    	done=true;
    	for (int i = 0; i < n; ++i) {
    		if(processes[i].remainingTime>0){
    			done=false;
    			if(processes[i].remainingTime>timeQuantum){
    				time+=timeQuantum;
    				processes[i].remainingTime-=timeQuantum;
    			}
    			else{
    				time+=processes[i].remainingTime;
    				processes[i].waitingTime=time-processes[i].burstTime;
    				processes[i].remainingTime=0;
    			}
    		}
        }
    }
    for (int i = 0; i < n; ++i) {
        processes[i].turnaroundTime = processes[i].waitingTime + processes[i].burstTime;
    }
}


void printResults(const vector<Process>& processes) {
    cout << setw(10) << "Process ID" << setw(15) << "Burst Time" << setw(15) << "Waiting Time" << setw(20) << "Turnaround Time" << endl;
    for (const auto& p : processes) {
        cout << setw(10) << p.id << setw(15) << p.burstTime << setw(15) << p.waitingTime << setw(20) << p.turnaroundTime << endl;
    }
}

int main() {
    vector<Process> processes = {{1, 10, 10, 0, 0}, {2, 5, 5, 0, 0}, {3, 8, 8, 0, 0}, {4, 7, 7, 0, 0},{5, 15, 2, 0, 0},{6, 17, 9, 0, 0}};
    int timeQuantum = 3;
    
    roundRobin(processes, timeQuantum);
    printResults(processes);

    return 0;
}