with open('input5', 'r') as input_file:
    puzzle_input = input_file.read().splitlines()

parsed_puzzle_input = []

for i in puzzle_input:
    parsed_puzzle_input.append(int(i))

last_pc = 0
pc = 0
steps = 0

while pc < len(parsed_puzzle_input):
    last_pc = pc
    pc = pc + parsed_puzzle_input[pc]
    steps = steps + 1
    parsed_puzzle_input[last_pc] = parsed_puzzle_input[last_pc] + 1

print("answer1:" + str(steps))

# part 2

parsed_puzzle_input = []

for i in puzzle_input:
    parsed_puzzle_input.append(int(i))

last_pc = 0
pc = 0
steps = 0

while pc < len(parsed_puzzle_input):
    last_pc = pc
    pc = pc + parsed_puzzle_input[pc]
    steps = steps + 1
    if parsed_puzzle_input[last_pc] >= 3:
        parsed_puzzle_input[last_pc] -= 1
    else:
        parsed_puzzle_input[last_pc] += 1

print("answer2:" + str(steps))