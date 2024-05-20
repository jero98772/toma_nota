import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Vector;
import java.util.List;
import java.util.ArrayList;


public class Main {
    public static void main(String[] args) {
        // Initialize ROM and RAM
        
        ROM rom = new ROM(16, 120);
        RAM ram = new RAM(16);


        rom.loadRomFromFile("rom.txt");

        // Create CPU with ROM and RAM
        CPU cpu = new CPU(rom, ram);

        // Execute instructions
        cpu.executeInstructions();
    }
}



// CPU class
class CPU {
    private ROM rom;
    private RAM ram;
    private short registerD;
    private short registerA;

    public CPU(ROM rom, RAM ram) {
        this.rom = rom;
        this.ram = ram;
    }

    // Method to execute a single instruction from ROM
    public void executeInstructions() {
        for (int instructionAddress = 0; instructionAddress < 16; instructionAddress++) {
    
        
            int[] instruction = rom.getValuesAt(instructionAddress);

            
            int typeInstruccion = instruction[0];
            if (typeInstruccion==1){// is C intricion
                int d1 =instruction[10];
                int d2 =instruction[11];
                int d3 =instruction[12];
            	int j1 =instruction[13];
                int j2 =instruction[14];
                int j3 =instruction[15];
            
            }else{
    		//else is a instruccion
                short mask = 0x7FFF; //mask to take 15 frist values beacause is a instruccion
                registerA = (short) (value & mask);

            }
        }
        
    }

    public int jump(int j1, int j2, int j3, int out ,int romPosition) {
        if (j1 == 1 && j2 == 0 && j3 == 0 && out > 0) { // JGT
            romPosition = registerA;
        } else if (j1 == 1 && j2 == 0 && j3 == 1 && out == 0) { // JEQ
            romPosition = registerA;
        } else if (j1 == 1 && j2 == 0 && j3 == 1 && out >= 0) { // JGE
            romPosition = registerA;
        } else if (j1 == 0 && j2 == 1 && j3 == 0 && out < 0) { // JLT
            romPosition = registerA;
        } else if (j1 == 0 && j2 == 1 && j3 == 1 && out != 0) { // JNE
            romPosition = registerA;
        } else if (j1 == 0 && j2 == 1 && j3 == 1 && out <= 0) { // JLE
            romPosition = registerA;
        } else if (j1 == 1 && j2 == 1 && j3 == 1) { // JMP
            romPosition = registerA;
        } else {
            romPosition++;
        }
        return romPosition;
    }

    public void handleRegisters(int d1, int d2, int d3, short value) {
        if (d1 == 1) {
            registerA = value; // Store in A register
        }
        if (d2 == 1) {
            registerD = value; // Store in D register
        }
        if (d3 == 1) {
            ram.setValueAt(value,registerA); // Store in RAM at address A
        }
    }
}


public class ALU {
    // Inputs
    short x;
    short y;

    // Control bits
    short zx;
    short nx;
    short zy;
    short ny;
    short f;
    short no;

    // Outputs
    short out;
    short zr;
    short ng;


    public ALU(short x, short y, short zx, short nx, short zy, short ny, short f, short no) {
        this.x = x;
        this.y = y;
        this.zx = zx;
        this.nx = nx;
        this.zy = zy;
        this.ny = ny;
        this.f = f;
        this.no = no;
    }
    public void compute() {
        short x1 = (short) (zx == 1 ? 0 : x);           // Zero the x input
        short x2 = (short) (nx == 1 ? ~x1 : x1);        // Negate the x input
        short y1 = (short) (zy == 1 ? 0 : y);           // Zero the y input
        short y2 = (short) (ny == 1 ? ~y1 : y1);        // Negate the y input

        short out1 = (short) (f == 1 ? x2 + y2 : x2 & y2);  // Perform the operation
        out = (short) (no == 1 ? ~out1 : out1);             // Negate the output

        zr = (short) (out == 0 ? 1 : 0);                        // Set the zero flag
        ng = (short) ((short) ((out >> 15) & 1) == 1 ? 1 : 0);     // Set the negative flag
    }
    public short getOut() {
        return out;
    }

    public short getZr() {
        return zr;
    }

    public short getNg() {
        return ng;
    }
}
// convert romvector of shorts  
public class ROM {
    private Vector<Vector<Integer>> rom;

    public ROM(int rows, int columns) {
        rom = new Vector<>(rows);
        for (int i = 0; i < rows; i++) {
            rom.add(new Vector<>(columns));
            for (int j = 0; j < columns; j++) {
                rom.get(i).add(0); // Initialize with zeros
            }
        }
    }

    // Method to load ROM from a text file
    public void loadRomFromFile(String fileName) {
        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line;
            int rowIndex = 0;

            while ((line = br.readLine()) != null && rowIndex < rom.size()) {
                String[] parts = line.split("\\s+");
                for (int colIndex = 0; colIndex < parts.length && colIndex < rom.get(rowIndex).size(); colIndex++) {
                    rom.get(rowIndex).set(colIndex, Integer.parseInt(parts[colIndex]));
                }
                rowIndex++;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // Method to get the values at a specific position
    public Vector<Integer> getValuesAt(int position) {
        if (position >= 0 && position < rom.size()) {
            return rom.get(position);
        } else {
            throw new IndexOutOfBoundsException("Invalid ROM position: " + position);
        }
    }

    // Method to get the number of rows
    public int getNumRows() {
        return rom.size();
    }


}

class RAM {
    private int[] ram;

    public RAM(int size) {
        ram = new int[size];
    }

    // Method to set a value at a specific position
    public void setValueAt(int value, int position) {
        if (position >= 0 && position < ram.length) {
            ram[position] = value;
        } else {
            throw new IndexOutOfBoundsException("Invalid RAM position: " + position);
        }
    }

    // Method to get a value at a specific position
    public int getValueAt(int position) {
        if (position >= 0 && position < ram.length) {
            return ram[position];
        } else {
            throw new IndexOutOfBoundsException("Invalid RAM position: " + position);
        }
    }
}
