from first_pass import first_pass
from second_pass import second_pass

with open(r"IO/in.txt", "r") as f:

    lines = f.readlines()
    lines = [line.strip() for line in lines]
    removed_comments = [line.split("/")[0].rstrip() for line in lines]
    removed_comments = [line for line in removed_comments if line != ""]
    symbol_table = first_pass(removed_comments)
    machine_code = second_pass(removed_comments, symbol_table)

    with open(r"IO/out_hex.txt", "w") as f_hex, open(r"IO/out_bin.txt", "w") as f_bin:
        for line_hex, code_hex in machine_code:

            f_hex.write(f"{line_hex} {code_hex}\n")
            line_bin = format(int(line_hex, 16), "012b")
            code_bin = format(int(code_hex, 16), "016b")
            f_bin.write(f"{line_bin} {code_bin}\n")


# TESTING
with open(r"IO/expected.txt", "r") as expected, open(r"IO/out_bin.txt", "r") as out:
    expected_lines = expected.readlines()
    out_lines = out.readlines()
    for i, (expected_line, out_line) in enumerate(zip(expected_lines, out_lines)):
        assert (
            expected_line.strip().split() == out_line.strip().split()
        ), f"Line {i + 1} does not match"
    print("All Lines Matche!")
