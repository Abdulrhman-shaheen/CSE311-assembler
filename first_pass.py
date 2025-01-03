from instructions import mem_instructions, reg_instructions, pseudo_instructions
def first_pass(lines):
    """
    This function takes a list of lines of assembly code and returns a symbol table. It works by 
    iterating over each line individually and checking if there's a 3 charachter at most label at
    the beggining that's not one of the instructions in the instruction set. It then return a
    dictionary with the labels as keys and their respective memory addresses as values. The format 
    function is used to format the memory addresses as hexadecimal value with "03X" meaning it will
    add leading zeros if the value is less than three digits) .  
    
    Args:
        lines (list): List of strings with the assembly code.
    
    Returns:
        symbol_table (dict): Dictionary with the labels and their respective memory addresses.
    """
    
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

