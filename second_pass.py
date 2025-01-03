from instructions import mem_instructions, reg_instructions, pseudo_instructions
def second_pass(lines, symbol_table):
    """     
    This function takes the assembly lines and the symbol table and returns a list of tuples with the memory address
    and the machine code in hex.
    
    It works by iterating over each line and checking which type of instruction it is after splitting the line on the space between
    the parts of the line. If there's a label in the firs part of the line, it means that the instrucion will be the second part of 
    the line not the first. Same with arguments which are the third part of the line if there's a label and the second part if there's
    no label.


    It handles each type of instruction differently. For pseudo instructions it's straightforward.
    
    For memory instructions:
    It checks if there's a label and if there is it replaces it with the memory address from the
    symbol table. It then checks if the instruction is indirect and sets the 4th bit in the opcode
    by ORing it with 0x8000 which have a 1 in  the 15th bit. It then ORs the opcode (which have 
    bits 0-11 set to zero) with the memory address to get the final hex value of the instruction.

    For register instructions:
    It just gets the opcode from the dictionary in `instruction.py` and formats it as a hexadecimal
    value.

    Format function is also used here to format the hex value with leading zeros if it's less than 
    4 digits.

    Args:
        lines (list): List of strings with the assembly code.
        symbol_table (dict): Dictionary with the labels and their respective memory addresses.
    
    Returns:
        machine_code (list): List of tuples with the memory address and the machine code in hex.
        
    """
    lc = format(0, "03X")
    machine_code = []
    for line in lines:
        parts = line.split()

        label = parts[0] if "," in parts[0] else None
        instruction = parts[1] if label else parts[0]
        args = parts[2:] if label else parts[1:]

        if instruction == "ORG":
            lc = format(int(args[0], 16), "04X")
            continue

        if instruction == "END":
            break

        if (
            instruction not in mem_instructions
            and instruction not in reg_instructions
            and instruction not in pseudo_instructions
        ):
            print(f"Invalid instruction: {instruction}")
            continue

        if instruction in mem_instructions:

            if args[0] in symbol_table:
                args[0] = symbol_table[args[0]]

            if "I" in args:
                opcode = mem_instructions[instruction] | 0x8000
            else:
                opcode = mem_instructions[instruction]

            hex_value = format(opcode | int(args[0], 16), "04X")

        if instruction in reg_instructions:
            hex_value = format(reg_instructions[instruction], "04X")

        if instruction == "DEC":
            hex_value = format(int(args[0]) & 0xFFFF, "04X")

        if instruction == "HEX":
            hex_value = format(int(args[0], 16) & 0xFFFF, "04X")

        machine_code.append((lc, hex_value))
        lc = format(int(lc, 16) + 1, "03X")

    return machine_code

