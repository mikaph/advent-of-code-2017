programs = "abcdefghijklmnop"

input_file = open('input16', 'r').read()

input16 = input_file

parsed_input = input16.split(',')

for i in parsed_input:
    print(i)

def spin(string, amount):
    for i in range(0, amount):
        string = string[-1] + string[:-1]
    return string

def exchange(string, x, y):
    result = list(string)
    result[x], result[y] = result[y], result[x]
    return ''.join(result)

def partner(string, x, y):
    return exchange(string, string.find(x), string.find(y))

def execute(string, command):
    if command[0] == 's':
        return spin(programs, int(command[1:]))
    if command[0] == 'x':
        return exchange(programs, int(command[1:].split('/')[0]), int(command[1:].split('/')[1]))
    if command[0] == 'p':
        return partner(programs, command[1], command[3])
    else:
        print("invalid command:" + command)
        return ""

for command in parsed_input:
    programs = execute(programs, command)

print("answer1: " + programs)

#2
programs =  "abcdefghijklmnop"

seen = []
cycle_len = 0

for i in range(0,1000):
    seen.append(programs)

    for command in parsed_input:
        programs = execute(programs,command)
    if programs in seen:
        cycle_len = i+1
        break

print("answer2: " + seen[1000000000 % cycle_len])
