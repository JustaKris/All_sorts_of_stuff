'''
https://judge.softuni.bg/Contests/Practice/Index/1140#1
'''



user_input = input('')

while user_input != 'stop playing':

    # Reworking the given input into a useable format
    sifted_input = user_input.split()
    sifted_input_int = []
    for x in sifted_input:
        sifted_input_int.append(int(x))
    sifted_input = sifted_input_int

    # Used to determine if list is unique
    other_list = []
    for x in sifted_input:
        if x in sifted_input and x not in other_list:
            other_list.append(x)

    # Logic for Unique list
    another_list = []
    if sifted_input == other_list:
        for x in sifted_input:
            if x % 2 == 0:
                another_list.append(int(x) + 2)
            elif x % 2 != 0:
                another_list.append(x)
        another_list.sort()
        print_list = ','.join(map(str, another_list))
        print('Unique list: ' + str(print_list))

        total = 0
        for x in another_list:
            total = x + total
        calculation = (total) / (len(another_list))
        testing_string = "{:.2f}".format(calculation)
        print(f'Output: {testing_string}')

    # Logic for Non-Unique list
    elif sifted_input != other_list:
        for x in sifted_input:
            if x % 2 != 0:
                another_list.append(int(x) + 3)
            elif x % 2 == 0:
                another_list.append(x)
        another_list.sort()
        print_list = ':'.join(map(str, another_list))
        print('Non-unique list: ' + str(print_list))

        total = 0
        for x in another_list:
            total = x + total
        calculation = (total) / (len(another_list))
        testing_string = "{:.2f}".format(calculation)
        print(f'Output: {testing_string}')

    # Re-runs it all (should probably try to clean it up, maybe make repeating code into functions and so on)
    user_input = input('')

