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
        LOAD 1
        WRITE 1
        LOAD 2
        WRITE 2
        LOAD 3
        WRITE 3
        LOAD 4
        WRITE 4
        LOAD 5
        WRITE 5
        LOAD 6
        WRITE 6

        LOAD 1
        WRITE 7
        LOAD 2
        WRITE 8
        LOAD 3
        WRITE 9
        LOAD 4
        WRITE 10
        LOAD 5
        WRITE 11
        LOAD 6
        WRITE 12

        READ 1
        SHIFT 7
        WRITE 13

        READ 2
        SHIFT 8
        WRITE 14

        READ 3
        SHIFT 9
        WRITE 15

        READ 4
        SHIFT 10
        WRITE 16

        READ 5
        SHIFT 11
        WRITE 17

        READ 6
        SHIFT 12
        WRITE 18

        """)
    assembler_res = subprocess.run(["python3", "assembler.py",\
                    str(input_file), str(assembler_file),
                    str(log_file)])
    assert assembler_res.returncode == 0

    interpreter_res = subprocess.run(["python3", "interpreter.py",\
                    str(assembler_file), str(interpreter_file),\
                        "1", "19"], capture_output=True)
    assert interpreter_res.returncode == 0

    with open(interpreter_file, "r") as f:
        got = f.read()
        print(got)
        excepted = \
"""Addresults,Value
1,1
2,2
3,3
4,4
5,5
6,6
7,1
8,2
9,3
10,4
11,5
12,6
13,2
14,8
15,24
16,64
17,160
18,384
"""
        assert got == excepted