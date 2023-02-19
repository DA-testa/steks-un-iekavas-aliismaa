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
            if len(opening_brackets_stack) == 0:
                return i+1
            opening_brackets_stack.pop()
            for j in range(len(opening_brackets_stack) - 1, -1, -1):
                if opening_brackets_stack[j][1] in "([{":
                    if are_matching(opening_brackets_stack[j][1], next):
                        opening_brackets_stack.pop(j)
                        break
                    else:
                        return i + 1

    if len(opening_brackets_stack) == 1:
      return opening_brackets_stack[0][0] + 1
    # success
    return 0

def main():
    text = ""
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if (mismatch == 0):
        print("Success")
    else:
        print(mismatch)

if __name__ == "__main__":
    main()
