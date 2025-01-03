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

It handles all the instructions present in `instructions.py` file, and according to the type of instruction, it generates the machine code. More details about the implementation can be found in the `second_pass` function.

### `main`

The `main` function coordinates the assembly process:

1. Reads the input assembly file.
2. Calls `first_pass` to generate the symbol table.
3. Calls `second_pass` to produce the machine code.
4. Writes the machine code to the output files in two diffrent formates, binary and hex (for readability).

## Usage

To assemble an assembly file, 

1. Place the assembly code in the file `IO/in.txt`.
2. Run the following command:
```sh
python main.py
```

This will generate the binary files `out_bin.txt` and `out_hex.txt` from the assembly file `in.txt`.

## License

This project is licensed under the MIT License.