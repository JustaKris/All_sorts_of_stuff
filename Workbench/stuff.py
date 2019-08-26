import re

#user_input = input()

test_string = 'Hello,everyone my name is Maria Mariova. I am 22 years old. was born on 22-06-1994.'

# Name
name_pattern = re.findall(r'(?<=name is )([A-Z][a-z]+\s[A-Z][a-z]+)', test_string)
name_actual = name_pattern[0]
print(name_actual)


'''
name_pattern = re.compile(r'(?<=name is )([A-Z][a-z]+\s[A-Z][a-z]+)')
name_matches = name_pattern.finditer(test_string)
for name in name_matches:
    name_actual = name.group(1)
    print(name_actual)
'''

# Age
age_pattern = re.findall(r'(\s)([1-9]\d{1})(\s)(?=years)', test_string)
retrieved_list = age_pattern[0]
age_actual = retrieved_list[1]
print(age_actual)



'''
age_pattern = re.compile(r'(\s)([1-9]\d{1})(\s)(?=years)')
age_match = age_pattern.finditer(test_string)
for age in age_match:
    age_actual = age.group(2)
    print(age_actual)
'''

# Birth day
bdate_pattern = re.findall(r'(?<= on )(\d{2}-\d{2}-\d{4}\.)', test_string)
bdate_actual = bdate_pattern
print(bdate_actual[0])

'''
bdate_pattern = re.compile(r'(?<= on )(\d{2}-\d{2}-\d{4}\.)')
bdate_match = bdate_pattern.finditer(test_string)
for date in bdate_match:
    bdate_actual = date.group(1)
    print(bdate_actual)
    pls_work = []

    pls_work.append(bdate_actual)
    print(pls_work)
    if bdate_actual:
        print('No match')
        bdate_actual = 'Fuck'
        print(bdate_actual)
    else:
        print('Good')
        print(bdate_actual)
'''
