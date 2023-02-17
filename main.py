# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        
        if next in "([{":
            Br=Bracket(next,i)
            opening_brackets_stack.append(Br)
        if next in ")]}":
            if len(opening_brackets_stack)!=0 and are_matching(opening_brackets_stack[len(opening_brackets_stack) - 1][0],next) == True:
                del opening_brackets_stack[len(opening_brackets_stack) - 1]
            else:
                return i+1
    if len(opening_brackets_stack)!=0:
        return opening_brackets_stack[0][1]+1

def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == None:
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
