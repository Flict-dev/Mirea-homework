import struct
import csv
import sys
from dataclasses import dataclass

COMMANDS = {
    "LOAD": 10,
    "READ": 14,
    "WRITE": 21,
    "SHIFT": 16,
}


class TempBuffer:
    def __init__(self) -> None:
        self.binary_data = bytearray()
        self.bit_size = 0
    
    def write(self, x, bit_width):
        for i in range(bit_width):
            if (self.bit_size + 1) * 8 > len(self.binary_data):
                self.binary_data.append(0)
            self.binary_data[self.bit_size // 8] ^= (((x >> i) & 1) << (self.bit_size % 8))
            self.bit_size += 1

def parse_line(line):
    if line.strip().startswith("#") or not line.strip():
        return None
    parts = line.strip().split()
    command = parts[0].upper()
    if len(parts) < 2:
        raise ValueError(f"Insufficient arguments for command: {line.strip()}")
    operand = int(parts[1])
    return command, operand

def process_command(command, operand, buffer):
    opcode = COMMANDS.get(command)
    if opcode is None:
        raise ValueError(f"Unknown command: {command}")
    
    buffer.write(opcode, 5)
    if command == "LOAD":
        buffer.write(operand, 9)
        buffer.write(0, 2)
    else:
        buffer.write(operand, 31)
        buffer.write(0, 4)
def assemble(input_path, binary_path, log_path):
    buffer = TempBuffer()

    with open(input_path, "r") as f:
        lines = f.readlines()

    for line in lines:
        parsed = parse_line(line)
        if parsed is not None:
            command, operand = parsed
            process_command(command, operand, buffer)
    print(len(buffer.binary_data))
    with open(binary_path, "wb") as f:
        f.write(buffer.binary_data)
    print(buffer.bit_size)

    log_assembly(input_path, log_path)

def log_assembly(input_file, log_file):
    with open(log_file, 'w', newline='') as csvfile:
        log_writer = csv.writer(csvfile)
        log_writer.writerow(["Command", "Operand"])
        with open(input_file, 'r') as infile:
            for line in infile:
                parsed = parse_line(line)
                if parsed is not None:
                    command, operand = parsed
                    log_writer.writerow([command, operand])

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python assemble.py <input_file> <binary_file> <log_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    binary_file = sys.argv[2]
    log_file = sys.argv[3]
    assemble(input_file, binary_file, log_file)