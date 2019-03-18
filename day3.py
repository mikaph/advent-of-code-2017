puzzle_input = 368078

d_x = 0
d_y = 0

x_dir = 1
y_dir = 1

row_len = 1
puzzle_input = puzzle_input - 1

while puzzle_input > 0:
    for i in range(0, row_len):
        puzzle_input = puzzle_input - 1
        d_x += x_dir

        if puzzle_input == 0:
            break

    x_dir = x_dir*-1

    if puzzle_input == 0:
        break

    for i in range(0, row_len):
        puzzle_input = puzzle_input - 1
        d_y += y_dir

        if puzzle_input == 0:
            break

    y_dir = y_dir*-1

    row_len = row_len + 1

print("answer1:" + str(abs(d_x) + abs(d_y)))

# part2

puzzle_input = 368078

d_x = 0
d_y = 0

x_dir = 1
y_dir = 1

row_len = 1
puzzle_input = puzzle_input - 1

numbers = {}
bigger_found = False


def sum_neighbours(delta_x, delta_y, dict_numbers):
    result = 0

    if (delta_x - 1, delta_y) in dict_numbers:
        result += dict_numbers[delta_x - 1, delta_y]
    if (delta_x - 1, delta_y - 1) in dict_numbers:
        result += dict_numbers[delta_x - 1, delta_y - 1]
    if (delta_x, delta_y - 1) in dict_numbers:
        result += dict_numbers[delta_x, delta_y - 1]
    if (delta_x + 1, delta_y) in dict_numbers:
        result += dict_numbers[delta_x + 1, delta_y]
    if (delta_x + 1, delta_y + 1) in dict_numbers:
        result += dict_numbers[delta_x + 1, delta_y + 1]
    if (delta_x, delta_y + 1) in dict_numbers:
        result += dict_numbers[delta_x, delta_y + 1]
    if (delta_x - 1, delta_y + 1) in dict_numbers:
        result += dict_numbers[delta_x - 1, delta_y + 1]
    if (delta_x + 1, delta_y - 1) in dict_numbers:
        result += dict_numbers[delta_x + 1, delta_y - 1]

    return result


numbers.update({(0, 0): 1})

while not bigger_found:
    for i in range(0, row_len):
        new_number = sum_neighbours(d_x, d_y, numbers)
        if d_x == 0 and d_y == 0:
            new_number = 1
        if new_number > puzzle_input:
            print("answer2:" + str(new_number))
            bigger_found = True
            break
        numbers.update({(d_x, d_y): new_number})
        d_x += x_dir

    x_dir = x_dir*-1

    for i in range(0, row_len):
        new_number = sum_neighbours(d_x, d_y, numbers)
        if new_number > puzzle_input:
            print("answer2:" + str(new_number))
            bigger_found = True
            break
        numbers.update({(d_x, d_y): new_number})
        d_y += y_dir

    y_dir = y_dir*-1

    row_len = row_len + 1
