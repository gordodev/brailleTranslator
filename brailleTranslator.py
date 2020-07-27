#!/usr/bin/python3
#Begin


'''  NOTES:

    #print list elements from list called braille, as single string (Not: 1,2,3 or [1,2,3] but 123 (also not 1 2 3))
print (''.join(map(str, braille)))

----------------------------------------------------------I/O EXAMPLES

-- Python cases --
Input:
solution.solution("code")
Output:
    100100101010100110100010

Braille > 000001110000111010100000010100111000111000100010        #Initial is upper

UPPER code:
    _____?
    000001110000111010100000010100111000111000100010  Braile
    0000010111101100101000100000001111                The quick brown fox ....

letters:
    e > 11000100010 (is this e?)
    e > "e" : [[1,0],[0,1],[1,0]] or 100110(from github)
    a > "e" : [[1,0],[0,1],[1,0]]  ?


UAT Testing: ( expand comment section once done testing new elements)
'''

braille=[1,]
