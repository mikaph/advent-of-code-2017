puzzle_input = [10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6]
testinput = [0, 2, 7, 0]

log = []
no_same = True
steps = 0
index_redistribution = 0
redistributed = 0

while no_same:
    steps = steps + 1
    log.append(list(puzzle_input))
    redistributed = max(puzzle_input)
    index_redistribution = puzzle_input.index(redistributed)
    puzzle_input[index_redistribution] = 0

    while redistributed > 0:
        index_redistribution = index_redistribution + 1
        if index_redistribution == len(puzzle_input):
            index_redistribution = 0

        puzzle_input[index_redistribution] = puzzle_input[index_redistribution] + 1
        redistributed = redistributed - 1

    if puzzle_input in log:
        no_same = False

# part1
print("answer1:" + str(steps))
# part2
print("answer2:" + str(steps - log.index(list(puzzle_input))))