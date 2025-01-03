from instructions import mem_instructions, reg_instructions, pseudo_instructions
def second_pass(lines, symbol_table):
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

