'''
Issue: when user input is actually used as an input() only the first row is being read.
'''
'''
Link to SoftUni test:
https://judge.softuni.bg/Contests/Practice/Index/1140#2
'''

import re

user_input = '''
Hello,everyone my name is Test Io. I am 22 years old. was born on 22-06-1994.
Hello,everyone my name is Test Oooook. I am 22 years old. was born on 22-06-1994.
Hello,everyone my name is Asd Iooo. I am 64 years old. was born on 15-06-1994.
Hello,everyone my name is Asd Io. I am 9 years old. was born on 15-06-1994.
make migrations
'''

user_input = input('')

#print(user_input)

# Patterns
name_pattern = re.findall(r'(?<=name is )([A-Z][a-z]+\s[A-Z][a-z]+)', user_input)
age_pattern = re.findall(r'(\s)([1-9]\d{1})(\s)(?=years)', user_input)
bdate_pattern = re.findall(r'(?<= on )(\d{2}-\d{2}-\d{4}\.)', user_input)
make_migration_pattern = re.findall(r'(make migrations)', user_input)

'''
print(name_pattern)
print(len(name_pattern))

print(age_pattern)
print(len(age_pattern))

print(bdate_pattern)
print(len(bdate_pattern))
'''

if len(name_pattern) >= 1 and len(age_pattern) >= 1 and len(bdate_pattern) >= 1:
    person_1 = []

    person_1.append(name_pattern[0])

    retrieved_list = age_pattern[0]
    person_1.append(retrieved_list[1])

    person_1.append(bdate_pattern[0])

if len(name_pattern) >= 2 and len(age_pattern) >= 2 and len(bdate_pattern) >= 2:
    person_2 = []

    person_2.append(name_pattern[1])

    retrieved_list = age_pattern[1]
    person_2.append(retrieved_list[1])

    person_2.append(bdate_pattern[1])

if len(name_pattern) >= 3 and len(age_pattern) >= 3 and len(bdate_pattern) >= 3:
    person_3 = []

    person_3.append(name_pattern[2])

    retrieved_list = age_pattern[2]
    person_3.append(retrieved_list[1])

    person_3.append(bdate_pattern[2])

if len(name_pattern) >= 4 and len(age_pattern) >= 4 and len(bdate_pattern) >= 4:
    person_4 = []

    person_4.append(name_pattern[3])

    retrieved_list = age_pattern[3]
    person_4.append(retrieved_list[1])

    person_4.append(bdate_pattern[3])



try:
    person_1
except NameError:
    pass
else:
    people = []
    people.append(person_1)

try:
    person_2
except NameError:
    pass
else:
    people.append(person_2)

try:
    person_3
except NameError:
    pass
else:
    people.append(person_3)

try:
    person_4
except NameError:
    pass
else:
    people.append(person_4)

try:
    people
except NameError:
    print('DB is empty')
else:
    for person in people:
        print(f"Name of the person: {person[0]}.")
        print(f"Age of the person: {person[1]}.")
        print(f"Birthdate of the person: {person[2]}")