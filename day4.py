with open('input4', 'r') as input_file:
    puzzle_input = input_file.read().splitlines()

parsed_puzzle_input = [x.split("\t") for x in puzzle_input]

for i in range(0, len(parsed_puzzle_input)):
    parsed_puzzle_input[i] = parsed_puzzle_input[i][0].split()

answer = 0

for i in parsed_puzzle_input:
    if len(set(i)) == len(i):
        answer = answer + 1

print("answer1:" + str(answer))

# part 2


def letter_counts(word):
    result = {}
    for letter in word:
        if letter in result:
            result[letter] += 1
        else:
            result.update({letter: 1})
    return result


def anagrams(string1, string2):
    counts1 = letter_counts(string1)
    counts2 = letter_counts(string2)

    if counts1 == counts2:
        return True
    else:
        return False


valid_passwords = 0

for line in parsed_puzzle_input:
    line_valid = True
    for i in range(0, len(line)):
        for j in range(i+1, len(line)):
            if anagrams(line[i], line[j]):
                line_valid = False

    if line_valid:
        valid_passwords += 1


print("answer2:" + str(valid_passwords))