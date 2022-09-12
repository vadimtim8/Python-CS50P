def main():
    plate = input('Plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')

def is_valid(s):
    # rule1 = 0
    for i in s[0:2]:
        if i.isalpha() == False:
            return False
            """ rule1 += 1
    if rule1 != 2:
        return False """

    if (2 <= len(s) <= 6) == False:
        return False

    index = -1
    for letter1 in s:
        if letter1.isalpha():
            index += 1
    if len(s) > index + 1:
        if s[index + 1] == '0':
            return False
    for letter2 in s[index + 1:]:
        if letter2.isdigit() == False:
            return False

    for letter in s:
        if letter.isalpha() or letter.isdigit():
            return True

main()