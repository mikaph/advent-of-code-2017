import random
input_file = open('input12', 'r').read().splitlines()

parsed_input = [list(x[x.find('>') + 1:].split(',')) for x in input_file]

the_group = set([0])
searched_lines = set([])
not_searched = set([])
not_searched.update(range(len(parsed_input)))

def add_connections(value):
    searched_lines.add(int(value))
    for item in parsed_input[int(value)]:
        the_group.add(int(item))
        if int(item) not in searched_lines:
            add_connections(int(item))
    return

add_connections(0)

#part1 answer
print(len(the_group))

#part2
not_searched = not_searched.difference(the_group)
groups = 1
while len(not_searched) > 0:
    the_group.clear()
    starting_number = random.sample(not_searched, 1)[0]
    add_connections(int(starting_number))
    not_searched = not_searched.difference(the_group)
    groups += 1

print(groups)

