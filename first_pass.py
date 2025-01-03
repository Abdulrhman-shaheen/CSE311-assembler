from instructions import mem_instructions, reg_instructions, pseudo_instructions
def first_pass(lines):
    lc = format(0, "03X")
    symbol_table = {}

    for line in lines:
        label = line.split(",")[0]

        if "ORG" in label:
            lc = format(int(label.split(" ")[1], 16), "04X")    
            continue

        if len(label) <= 3:
            if not (label in reg_instructions) and not (label in pseudo_instructions) and not (label in mem_instructions):
                symbol_table[label] = lc

        lc = format(int(lc, 16) + 1, "03x")
    return symbol_table

