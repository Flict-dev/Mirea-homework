import csv
import sys

MEMORY_SIZE = 1024

class TempBuffer:
    def __init__(self, binary_data: bytes):
        self.binary_data = binary_data
        self.bit_it = 0

    def read(self, bit_width: int) -> int:
        result = 0
        for i in range(bit_width):
            result ^= (((self.binary_data[self.bit_it // 8] >> (self.bit_it % 8)) & 1) << i)
            self.bit_it += 1
        return result

def interpret(binary_path: str, resultult_path: str, memory_range: tuple):
    memory = [0] * MEMORY_SIZE
    register_accumulator = 0

    with open(binary_path, "rb") as f:
        binary_data = f.read()

    buffer = TempBuffer(binary_data)
    i = 0
    while i * 8 < len(binary_data):
        opcode = buffer.read(5)
        if opcode == 10:  # LOAD
            value = buffer.read(9)
            if buffer.read(2) != 0:
                raise ValueError("Unexpected padding bits.")
            register_accumulator = value
            i += 2
        elif opcode == 14:  # READ
            addresults = buffer.read(31)
            if buffer.read(4) != 0:
                raise ValueError("Unexpected padding bits.")
            register_accumulator = memory[addresults]
            i += 5
        elif opcode == 21:  # WRITE
            addresults = buffer.read(31)
            if buffer.read(4) != 0:
                raise ValueError("Unexpected padding bits.")
            memory[addresults] = register_accumulator
            i += 5

        elif opcode == 16:  # SHIFT
            addresults = buffer.read(31)
            if buffer.read(4) != 0:
                raise ValueError("Unexpected padding bits.")
            register_accumulator <<= memory[addresults]
            i += 5

        else:
            raise ValueError(f"Unknown opcode: {opcode}")


    with open(resultult_path, 'w', newline='') as csvfile:
        fieldnames = ['Addresults', 'Value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for addr in range(*memory_range):
            writer.writerow({'Addresults': addr, 'Value': memory[addr]})

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <binary_file> <resultult_file> <memory_start> <memory_end>")
        sys.exit(1)

    binary_file = sys.argv[1]
    resultult_file = sys.argv[2]
    try:
        memory_start, memory_end = int(sys.argv[3]), int(sys.argv[4])
    except ValueError:
        print("Memory range must be two integers.")
        sys.exit(1)

    if not (0 <= memory_start < MEMORY_SIZE and 0 <= memory_end <= MEMORY_SIZE and memory_start < memory_end):
        print("Invalid memory range.")
        sys.exit(1)

    interpret(binary_file, resultult_file, (memory_start, memory_end))