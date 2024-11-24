import csv
import struct
import sys


class Assembler:
    def __init__(self):
        self.instructions = []
    
    def parse_file(self, input_file):
        with open(input_file, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    self.instructions.append(self.parse_instruction(line))
    
    def parse_instruction(self, line):
        parts = line.split(',')
        return [int(part.strip(), 16) for part in parts]

    def write_binary_file(self, output_file):
        with open(output_file, 'wb') as file:
            for instruction in self.instructions:
                file.write(struct.pack('B' * len(instruction), *instruction))
    
    def write_log_file(self, log_file):
        with open(log_file, 'w', newline='') as file:
            writer = csv.writer(file)
            for instr in self.instructions:
                writer.writerow([f"byte{i}={byte}" for i, byte in enumerate(instr)])


class Interpreter:
    def __init__(self):
        self.memory = [0] * 1024  # Example size

    def execute(self, binary_file, result_file, start_addr, end_addr):
        with open(binary_file, 'rb') as file:
            program = file.read()
        
        self.process_instructions(program)

        with open(result_file, 'w', newline='') as file:
            writer = csv.writer(file)
            for addr in range(start_addr, end_addr):
                writer.writerow([f"address={addr}", f"value={self.memory[addr]}"])

    def process_instructions(self, program):
        pc = 0
        while pc < len(program):
            opcode = program[pc]
            if opcode == 0x2A:  # Example opcode
                const = program[pc + 1]
                self.load_constant(const)
                pc += 2
            elif opcode == 0x6E:  # Example opcode for reading
                addr = program[pc + 1:pc + 5]
                addr = struct.unpack('>I', bytes(addr))[0]
                self.read_memory(addr)
                pc += 5
            elif opcode == 0xF5:  # Example opcode for writing
                addr = program[pc + 1:pc + 5]
                addr = struct.unpack('>I', bytes(addr))[0]
                self.write_memory(addr)
                pc += 5
            elif opcode == 0x85:  # Example opcode for shift
                addr = program[pc + 1:pc + 5]
                addr = struct.unpack('>I', bytes(addr))[0]
                self.shift(addr)
                pc += 5
            else:
                raise ValueError(f"Unknown opcode: {opcode}")

    def load_constant(self, const):
        self.accumulator = const

    def read_memory(self, addr):
        self.accumulator = self.memory[addr]

    def write_memory(self, addr):
        self.memory[addr] = self.accumulator

    def shift(self, addr):
        self.accumulator <<= 1
        self.memory[addr] = self.accumulator


def main():
    if len(sys.argv) != 5:
        print("Usage: python uvw.py <input_file> <output_file> <log_file> <result_file>")
        sys.exit(1)

    input_file, output_file, log_file, result_file = sys.argv[1:5]

    assembler = Assembler()
    assembler.parse_file(input_file)
    assembler.write_binary_file(output_file)
    assembler.write_log_file(log_file)

    interpreter = Interpreter()
    interpreter.execute(output_file, result_file, start_addr=0, end_addr=1024)


if __name__ == '__main__':
    main()