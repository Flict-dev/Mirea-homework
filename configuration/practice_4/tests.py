from dataclasses import dataclass
import pytest
import pathlib
import subprocess

project_dir = pathlib.Path(__file__).parent

@dataclass
class Case:
    name: str
    input: str
    expected_output: bytes


@pytest.mark.parametrize("op", [
    Case("load",
                 "LOAD 161\n",
                 bytes([0x2a, 0x14])
    ),
    Case("read",
                 "READ 411\n",
                 bytes([0x6e, 0x33, 0x00, 0x00, 0x00])
    ),
    Case("write",
                 "WRITE 311\n",
                 bytes([0xf5, 0x26, 0x00, 0x00, 0x00])
    ),
    Case("shift",
                 "SHIFT 194\n",
                 bytes([0x50, 0x18, 0x00, 0x00, 0x00])
    )
])
def test_load(tmp_path, op):
    input_file = tmp_path / f"input_{op.name}"
    log_file = tmp_path / f"log_{op.name}.yaml"
    output_file = tmp_path / f"output_{op.name}"
    with open(input_file, "w") as f:
        f.write(op.input)

    res = subprocess.run(["python3", "assembler.py",\
                    str(input_file), str(output_file),
                    str(log_file)])
    assert res.returncode == 0
    with open(output_file, "rb") as f:
        got = f.read(len(op.expected_output))
        assert got == op.expected_output


def test_program(tmp_path):
    input_file = tmp_path / "program.txt"
    log_file = tmp_path / "program_log.csv"
    assembler_file = tmp_path / "program.bin"
    interpreter_file = tmp_path / "result.csv"

    with open(input_file, "w") as f:
        f.write(
        """
            LOAD 161
            WRITE 20
            LOAD 260
            WRITE 30
            READ 20
            SHIFT 30
            WRITE 31
        """)
    assembler_res = subprocess.run(["python3", "assembler.py",\
                    str(input_file), str(assembler_file),
                    str(log_file)])
    assert assembler_res.returncode == 0

    interpreter_res = subprocess.run(["python3", "interpreter.py",\
                    str(assembler_file), str(interpreter_file),\
                        "20", "32"], capture_output=True)
    assert interpreter_res.returncode == 0

    with open(interpreter_file, "r") as f:
        got = f.read()
        print(got)
        excepted = \
"""Addresults,Value
20,161
21,0
22,0
23,0
24,0
25,0
26,0
27,0
28,0
29,0
30,260
31,298280421875326519411118857382380050630023480498690092965642736404384221952475136
"""
        assert got == excepted