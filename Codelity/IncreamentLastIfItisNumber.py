'''
Created on 12-May-2019

@author: Sumedh.Tambe
'''
#     
#  # Write a function which increments a string, to create a new string. 
# If the string already ends with a number, the number should be incremented by 1. 
# If the string does not end with a number, the number 1 should be appended to the new string.
#     Examples:
#     foo -> foo1
#     foobar23 -> foobar24
#     foo23bar -> foo23bar1
#     foo0042 -> foo0043
#     foo9 -> foo10
#     foo099 -> foo100
# 
# Attention: If the number has leading zeros the number of digits should be considered.

# def stringIncrement(word):
#     l = len(word)
#     move = 0
#     numbers = '0123456789'
#     found = False
#     
#     while not found and move > -l:
#         c = word[l+move-1]
#         if c in numbers:
#             move -= 1
#             continue
#         else:
#             found = True
#     part1,part2 = word[:move], int(word[move:])
#     
#     
#     return part1+part2+'1'
# 
# if __name__ == '__main__':
#     word='foo'
#     Result=stringIncrement(word)

#foo23bar

inString="fooba1r23"
numbers='0123456789'
keepmoving=0
finalstring=''
for i in range(len(inString)-1,0,-1):
    if(inString[i] in numbers):
        keepmoving=i
    if(inString[i].isalpha()):
        break
#     else:
#         keepmoving=0
if(keepmoving==0):
    finalstring=inString.join('1')
else:
    justString=inString[0:keepmoving]
    splitedString=inString[keepmoving:len(inString)]
    number=int(splitedString)
    finalnumber=number+1
    finalstring=justString+str(finalnumber)
print(finalstring)