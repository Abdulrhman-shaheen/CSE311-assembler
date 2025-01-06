# CSE311 Assembler

This project is an assembler for the basic computer assembly language. The assembler translates the instructions into machine code in two versions, binary and hex that can be found in `IO/out_bin.txt` and `IO/out_hex.txt` respectively.

## Project Structure

- `first_pass`: This function processes the assembly code to identify labels and store their addresses to be used in the second pass.
- `second_pass`: This function converts the assembly instructions into machine code.
- `main`: The main function calls the `first_pass` and the `second_pass` functions, then asserts that the output is the same as the `IO/expected.txt`.

## Functions

### `first_pass`

The `first_pass` function scans the assembly code to:

1. Identify the addresses of all labels in the program.
2. Store these addresses in `symbol_table` to be used in the second pass.

### `second_pass`

The `second_pass` function translates the assembly instructions into machine code by:

1. Using the symbol table generated in the first pass.
2. Converting each instruction into its corresponding machine code representation.
3. If the instruction was an indirect addressing, it ORs the instruction code with 0x8000 to flip the 15th bit (0-indexed) to 1.

It handles all the instructions present in `instructions.py` file, and according to the type of instruction, it generates the machine code. More details about the implementation can be found in the `second_pass` function.

It also handles invalid instructions and arguments, and raises an error if an invalid instruction or argument is found.

The "ORG" instruction argument should be written in HEX, and if not included in the code it will start at 0.

The "END" instruction can or cannot be included in the code, and if included it should be the last instruction in the code.

### `main`

The `main` function coordinates the assembly process:

1. Reads the input assembly file.
2. Calls `first_pass` to generate the symbol table.
3. Calls `second_pass` to produce the machine code.
4. Writes the machine code to the output files in two diffrent formates, binary and hex (for readability).


## Error Handling

The assembler handles the following errors:
1. Invalid instruction: If an instruction is not found in the instruction set, the assembler raises an error.
2. Invalid or repeated label: If a label length is more than 3 charachters or it's the letter "I", the assembler raises an error.

To avoid any errors, the input file should be written in the format mentioned in the next section.
## Usage

First, the input file should be written in the following format:
    

### Labels
1. The label maximum length is 3 characters. Otherwise the assembler crashes with an error message.
1. The label should be followed by a comma and a space.
1. The label can't be the capital letter "I" as it's reserved for Indirect addressing. Otherwise the assembler crashes with an error message
1. The label should be unique, otherwise the assembler crashes with an error message.

### Instructions
1. The instruction can be in lower or upper case.
1. The instruction should be followed and preceded  by a space.
1. The instruction should exist in the instruction set (in instuctions.py). Otherwise the assembler crashes with an error message


### Arguments
1. The arguments should come after the instruction.
1. Valid arguments are addresses, labels, numbers, the letter 

### Comments
1. Any comment should be preceded by a backslash and a space ( /Comment here).
1. The comment should be at the end of the line.


To assemble an assembly file, 

1. Place the assembly code in the file `IO/in.txt`.
2. Run the following command:
```sh
python main.py
```

This will generate the binary files `out_bin.txt` and `out_hex.txt` from the assembly file `in.txt`.

## License

This project is licensed under the MIT License.