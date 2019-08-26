import re


my_string = 'Hello,everyone my name is Maria Mariova. I am 22 years old. was born on 22-06-1994. fabcde'

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://wwww.nasa.gov
'''

setence = 'Start a sentence and then bring it to an end'

#pattern = re.compile(r'\d\d\d.\d{3}[-.]\d{4}')
#pattern = re.compile(r'[^a-zA-Z]')
#pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
#pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

subbed_urls = pattern.sub(r'\2\3', urls)

print(subbed_urls)

matches = pattern.finditer(urls)

for match in matches:
    print(match.group(0))

'''
with open('data.txt', 'r') as f:
    contents = f.read()

    matches = pattern.finditer(contents)

    for match in matches:
        print(match)
'''