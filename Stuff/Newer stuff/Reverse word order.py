'''
Reverse word order
https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
'''

user_input = input("Insert a phrase: ")

def reversal(phrase):
    split_phrase = phrase.split()
    word = ''
    for i in split_phrase:
        word = i + ' ' + word
    return word

print(reversal(user_input))