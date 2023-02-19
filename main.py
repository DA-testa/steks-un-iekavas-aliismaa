# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append((i, next))
          
        if next in ")]}":
            if (len(opening_brackets_stack) == 0 or are_matching(opening_brackets_stack[len(opening_brackets_stack)-1][1], next) != True):
                return i+1
            opening_brackets_stack.pop()
          
    if len(opening_brackets_stack) == 1:
      return opening_brackets_stack[0][0] + 1
    return 0

def main():
    text = ""
    choice = input()
  
    if choice == "F":
        text = open(str(input()),"r").read()
        mismatch = find_mismatch(text)
        if (mismatch == 0):
            print("Success")
        else:
            print(mismatch)
          
    elif choice == "I":
        text = input()
        mismatch = find_mismatch(text)
        if (mismatch == 0):
            print("Success")
        else:
            print(mismatch)
          
    else: 
        print("error")

if __name__ == "__main__":
    main()
