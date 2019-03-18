with open('input2', 'r') as puzzle_input_file:
    puzzle_input = puzzle_input_file.read().splitlines()

parsed_puzzle_input = [x.split("\t") for x in puzzle_input]
parsed_puzzle_input = [list(map(int, x)) for x in parsed_puzzle_input]

result = 0
for i in parsed_puzzle_input:
    result += max(i) - min(i)

print("answer1:" + str(result))

# part2
result = 0
line_len = len(parsed_puzzle_input[0])

for line in parsed_puzzle_input:
    for i in range(0, line_len):
        for j in range(i+1, line_len):
            if line[i] % line[j] == 0:
                result += line[i]/line[j]
            elif line[j] % line[i] == 0:
                result += line[j]/line[i]

print("answer2:" + str(result))
