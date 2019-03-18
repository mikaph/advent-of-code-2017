with open('input7', 'r') as input_file:
    input7 = input_file.read().splitlines()


parsed_input = [x.split() for x in input7]

for i in parsed_input:
    i.pop(1)

program_list = set()
children = set()

for i in parsed_input:
    if '->' in i:
        program_list.add(i[0])
        for j in range(2, len(i)):
            child_to_add = i[j].strip(',')
            children.add(child_to_add)
            program_list.add(child_to_add)
    else:
        for j in i:
            program_list.add(j)

print("answer1:" + str(program_list - children))

# part 2

parsed_input2 = [x.split() for x in input7]


def bracketnumber_to_int(bnum):
    return int(bnum.strip('(').strip(')'))


def get_disc_weight(name):
    for i in parsed_input2:
        if i[0] == name:
            return bracketnumber_to_int(i[1])
    print("error, name not found")


def get_tower_weight(name):
    for item in parsed_input2:
        if item[0] == name:
            if '->' in item:
                child_weights = 0
                for child in item[3:]:
                    child_weights += get_tower_weight(child.strip(','))

                return child_weights + bracketnumber_to_int(item[1])
            else:
                return bracketnumber_to_int(item[1])


# start from the root
tree_root = "vtzay"


def find_wrong_weight(name):
    # check which child tree is not balanced
    child_tree_weights = {}

    for item in parsed_input2:
        if item[0] == name:
            if '->' in item:
                for child in item[3:]:
                    child_tree_weights.update({child.strip(','): get_tower_weight(child.strip(','))})

    average_weight = 0
    biggest_difference = 0
    wrong_weight = ""

    for key, value in child_tree_weights.items():
        average_weight += value

    if len(child_tree_weights) > 0:
        average_weight = average_weight/len(child_tree_weights)

    # find biggest difference from average weight
    for key, value in child_tree_weights.items():
        if abs(average_weight - value) > biggest_difference:
            wrong_weight = key
            biggest_difference = abs(average_weight - value)

    if biggest_difference == 0:
        return name
    else:
        return find_wrong_weight(wrong_weight)


def find_required_weight(name):
    own_weight = 0
    sibling_weight = 0

    for item in parsed_input2:
        if name in str(item[3:]):
            own_weight = get_tower_weight(name)
            for child in item[3:]:
                if child.strip(',') != name:
                    sibling_weight = get_tower_weight(child.strip(','))

    return get_disc_weight(name) + (sibling_weight - own_weight)


wrong = find_wrong_weight(tree_root)
print("answer2:" + str(find_required_weight(wrong)))