'''
BNF Grammar:
<palindrome> ::= <empty string>|<letter>|                              
                          a<palindrome>a
                          b<palindrome>b
                          c<palindrome>c
                          .
                          .
                          .
                          z<palindrome>z
                          A<palindrome>A
                          B<palindrome>B
                          C<palindrome>C
                          .
                          .
                          .
                          Z<palindrome>Z
<letter> ::= a|b|c|....|z|A|B|C|...|Z|
<empty string> = ' '
'''

def palindrome_checker(string):  
  list = []
  f_index = 0
  l_index = len(string)-1
  flag = True

  for s in string:
    list.append(s)
  if s.isalpha() or s == ' ':
    for s in list:
      while(f_index <= len(string)-1 and flag == True):
        first = list[f_index]
        last = list[l_index]

        if(first == last):
          f_index += 1
          l_index -= 1
        else:
          flag = False
  else:
    return 'INVALID'
  
  return 'A PALINDROME' if flag == True else 'NOT A PALINDROME'

again = 1
while (again == 1):
  string = input("Enter string to check: ")
  new_str = string.replace(" ", "") if string != ' ' else string
  print(palindrome_checker(new_str))
  again = int(input("Enter 0 to quit or 1 to check again: "))
