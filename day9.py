input_file = open('input9', 'r').read()

trash = False
ignore_next = False
open_braces = 0
score = 0
trash_count = 0

for i in input_file:
    if ignore_next:
        ignore_next = False
        continue

    if i == '{' and not trash:
        open_braces += 1
    elif i == '}' and not trash:
        score += open_braces
        open_braces -= 1
    elif i == '!':
        ignore_next = True
    elif i == '<':
        if trash:
            trash_count += 1
        else:
            trash = True
    elif i == '>':
        trash = False
    elif trash:
        trash_count += 1

print("answer1:" + str(score))
print("answer2:" + str(trash_count))