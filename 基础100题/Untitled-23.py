"""

        *
       ***
      *****
     *******
      *****
       ***
        *

"""
str = '*'
for i in range(4):
    str = "*"*(2*i+1)
    print(str.center(7,' '))
for i in range(3):
    str = "*"*(2*(3-i)-1)
    print(str.center(7,' ')) 











