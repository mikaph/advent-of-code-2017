from functools import reduce

input14 = "jzgqcdpd"

class Cyclic_iterator:
    def __init__(self, list_size):
        self.list_size = list_size
        self.i = 0
    def increment(self, amount):
        for i in range(0,amount):
            if self.i == self.list_size - 1:
                self.i = 0
            else:
                self.i += 1
    def get_i(self):
        return self.i

    def set_i(self, i):
        self.i = i

rows = []
for i in range(0,128):
    rows.append(input14 + "-" + str(i))


magic_numbers = [17, 31, 73, 47, 23]

bin_hashes = []

for row in rows:
    rows_int = []
    hash = row
    print(hash)

    for i in hash:
        rows_int.append(ord(i))

    rows_int.extend(magic_numbers)

    sublist = []
    skip_size = 0
    rope = list(range(0,256))
    i_rope = Cyclic_iterator(len(rope))

    for j in range(0,64):
        for i in rows_int:
            sublist_start = i_rope.get_i()
            for k in range(0, i):
                sublist.append(rope[i_rope.get_i()])
                i_rope.increment(1)

            sublist.reverse()
            i_rope.set_i(sublist_start)

            for item in sublist:
                rope[i_rope.get_i()] = item
                i_rope.increment(1)

            sublist = []

            i_rope.increment(skip_size)
            skip_size += 1

    hash = []

    for i in range(0,16):
        hash.append(reduce((lambda x, y: x ^ y), rope[i*16:(i+1)*16]))

    hex_hash = []
    for i in hash:
        hex_hash.append(hex(i))

    bin_hash = []
    for i in hash:
        bin_hash.append(bin(i))

    bin_hashes.append(bin_hash)

print(bin_hash)
print("answer1: " +str(sum(x == "1" for x in str(bin_hashes))))

#2

areas = []
zeros = '00000000'

for i in bin_hashes:
    line = ""
    for j in i:
        line += (zeros[len(j)-2:] + j[2:])
    areas.append(list(line))

for i in areas:
    print(i)

def flood_fill(line, index):
    if areas[line][index] == '1':
        areas[line][index] = '2'
        if line < 127:
            flood_fill(line+1,index)

        if index < 127:
            flood_fill(line,index+1)

        if line > 0:
            flood_fill(line-1,index)

        if index > 0:
            flood_fill(line,index-1)

num_areas = 0

for i in range(0,128):
    for j in range(0,128):
        if areas[i][j] == '1':
            flood_fill(i,j)
            num_areas += 1

print("answer2: " + str(num_areas))


