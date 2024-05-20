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
        short sizeram = 64;
        RAM ram = new RAM(sizeram );


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
    ALU alu = new ALU();

    public CPU(ROM rom, RAM ram) {
        this.rom = rom;
        this.ram = ram;
    }

    // Method to execute a single instruction from ROM
    public void executeInstructions() {
        for (short instructionAddress = 0; instructionAddress < rom.getNumRows(); instructionAddress++) {
    
        
            Vector<Integer> instruction = rom.getValuesAt(instructionAddress);
            //Vector<Integer> instruction = rom.convertShortToBitVector(rom.getValuesAt(instructionAddress));

            
            short typeInstruccion = instruction.get(0).shortValue(); 
            if (typeInstruccion==1){// is C intricion
                short a = instruction.get(3).shortValue();   // a
                short zx = instruction.get(4).shortValue();  // c1
                short nx = instruction.get(5).shortValue();  // c2
                short zy = instruction.get(6).shortValue();  // c3
                short ny = instruction.get(7).shortValue();  // c4
                short f = instruction.get(8).shortValue();   // c5
                short no = instruction.get(9).shortValue();  // c6
                short d1 = instruction.get(10).shortValue();
                short d2 = instruction.get(11).shortValue();
                short d3 = instruction.get(12).shortValue();
                short j1 = instruction.get(13).shortValue();
                short j2 = instruction.get(14).shortValue();
                short j3 = instruction.get(15).shortValue();

                if(a==1){//register A
                    this.alu.setInputs(registerD,registerA);
                }else{// memory
                    this.alu.setInputs(registerD,this.ram.getValueAt(registerA));
                }
                this.alu.setControlBits(zx, nx, zy, ny, f, no);
                this.alu.compute();
                this.handleRegisters(d1, d2, d3, this.alu.getOut());
                instructionAddress=this.jump(j1, j2, j3, this.alu.getOut() ,instructionAddress);
            
            }else{
    		//else is a instruccion
                short result = 0;
                int shiftAmount = 0;
        
                // Iterate over each Integer in the vector
                for (int i = 0; i < instruction.size(); i++) {
                    // Extract the current integer value
                    int intValue = instruction.get(i);

                    // Use bitwise OR to combine the bits of intValue into result
                    result |= (intValue & 0x7FFF) << shiftAmount;

                    // Update the shift amount for the next integer
                    shiftAmount += 16;
                }
        
                //short mask = 0x7FFF; //mask to take 15 frist values beacause is a instruccion
                registerA = result;

            }
        }
        
    }

    public short jump(short j1, short j2, short j3, short out ,short romPosition) {
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
            
        }
        return romPosition;
    }

    public void handleRegisters(short d1, short d2, short d3, short value) {
        if (d1 == 1) {
            this.registerA = value; // Store in A register
        }
        if (d2 == 1) {
            this.registerD = value; // Store in D register
        }
        if (d3 == 1) {
            this.ram.setValueAt(value,this.registerA); // Store in RAM at address A
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

    public void setInputs(short x, short y) {
        this.x = x;
        this.y = y;
    }

    public void setControlBits(short zx, short nx, short zy, short ny, short f, short no) {
        this.zx = zx;
        this.nx = nx;
        this.zy = zy;
        this.ny = ny;
        this.f = f;
        this.no = no;
    }
    public ALU() {
        /*
          x=outDReg,
          y=outAorM,
          zx=instruction[11],   // c1
          nx=instruction[10],   // c2
          zy=instruction[9],    // c3
          ny=instruction[8],    // c4
          f =instruction[7],    // c5
          no=instruction[6],    // c6
          out=outALU,
          out=outM,
          zr=isZeroOut,
          ng=isNegOut
        */
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
    public static List<Short> convertShortToBitVector(short value) {
        List<Short> bitVector = new ArrayList<>(16);
        
        for (int i = 0; i < 16; i++) {
            // Shift right and mask with 1 to get the bit at position i
            bitVector.add(0, (short)((value >> i) & 1));
        }
        
        return bitVector;
    }    // Method to get the number of rows
    public int getNumRows() {
        return rom.size();
    }


}

class RAM {
    private short[] ram;

    public RAM(short size) {
        ram = new short[size];
    }

    // Method to set a value at a specific position
    public void setValueAt(short value, short position) {
        if (position >= 0 && position < ram.length) {
            ram[position] = value;
        } else {
            throw new IndexOutOfBoundsException("Invalid RAM position: " + position);
        }
    }

    // Method to get a value at a specific position
    public short getValueAt(short position) {
        if (position >= 0 && position < ram.length) {
            return ram[position];
        } else {
            throw new IndexOutOfBoundsException("Invalid RAM position: " + position);
        }
    }
}
