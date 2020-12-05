first, second = input("Input two Number: (a,b) ").split(",")

def sum(first, second):
    s = int(first) + int(second)
    return s, first, second

print(sum(first, second))