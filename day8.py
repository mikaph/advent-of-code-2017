with open('input8', 'r') as input_file:
    input8 = input_file.read().splitlines()


parsed_input = [x.split() for x in input8]

registers = {}
register_max_value = 0

for i in parsed_input:
    # pick information from array
    modified_register = i[0]

    if i[1] == 'inc':
        modifier_multiplier = 1
    elif i[1] == 'dec':
        modifier_multiplier = -1

    modifier_value = i[2]

    comparison_register = i[4]

    comparison_operator = i[5]

    comparison_value = i[6]

    # do something with it
    if modified_register not in registers:
        registers.update({modified_register: 0})

    if comparison_register not in registers:
        registers.update({comparison_register: 0})

    condition = str(registers.get(comparison_register)) + " " + comparison_operator
    condition = condition + " " + comparison_value

    if eval(condition):
        registers.update({modified_register: registers.get(modified_register) + int(modifier_value)*modifier_multiplier})
        if register_max_value < registers.get(modified_register):
            register_max_value = registers.get(modified_register)


print("answer1:" + str(max(registers.values())))
print("answer2:" + str(register_max_value))