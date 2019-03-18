input_file = open('input11', 'r').read()

parsed_input = list((input_file.split(',')))

x_coord = 0
y_coord = 0

last_distance = 0
distances = []

for item in parsed_input:
    print("item " + item)
    if item == 'ne':
        x_coord += 1
        y_coord -= 1
    elif item == 'se':
        x_coord += 1
    elif item == 's':
        y_coord += 1
    elif item == 'sw':
        x_coord -= 1
        y_coord += 1
    elif item == 'nw':
        x_coord -= 1
    elif item == 'n':
        y_coord -= 1

    z_coord = -x_coord - y_coord
    distances.append((abs(x_coord) + abs(y_coord) + abs(z_coord))/2)


print("x:" + str(x_coord) + " y:" + str(y_coord) + " z:" + str(z_coord))
print("max distance:" + str(max(distances)))
print("distance form start:" + str(distances.pop()))

