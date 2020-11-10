import re

def multi_re_find(patterns, phrase):
    for i in patterns:
        print('searching for patter {}'.format(i))
        print(re.findall(i,phrase))
        print('\n')

test_phrase = 'This is a string with numbers 1243514 and a symbol #'

test_patter = [r'\W+']

multi_re_find(test_patter,test_phrase)