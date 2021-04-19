'''
BNF Grammar
<expression> ::= <variable>|<unary>(<expression>)|(<expression>)|<expression><operator><expression>
<variable> ::= x|y|z
<unary> ::= ~
<operator> ::= +|-
'''

variables = ["x","y","z"]
operator = ['+', '-']

def IsValid(string):
  list = []
  curr_index = open_par = close_par = 0
  l_index = len(string)-1

  for s in string:
    list.append(s)
  
  if not list:
    return "INAVLID"

  for s in list:
    if s == '(':
      open_par += 1
    elif s == ')':
      close_par += 1

    if curr_index < l_index:
      next_elem = list[curr_index+1]
      if s == '~':
        if next_elem not in variables and next_elem != '(':
          return "INVALID"
      elif s in variables:
        if next_elem not in operator and next_elem != ')':
          return "INVALID"
      elif s == '(':
        if next_elem in operator or next_elem == ')':
          return "INVALID"
      elif s == ')':
        if next_elem not in operator and next_elem != ")":
          return "INVALID"
      elif s in operator:
        if next_elem not in variables and next_elem not in "~(":
          return "INVALID"
    elif s not in variables and s != ")":
      return "INVALID"
    else:
      return "VALID" if open_par == close_par else "INVALID"

    curr_index += 1

def main():
  again = 1
  while (again == 1):
    string = input("Enter string to check: ")
    print(IsValid(string))
    again = int(input("Enter 0 to quit or 1 to check again: "))

if __name__ == "__main__":
    main()
