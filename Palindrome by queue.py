from collections import deque

s = input("enter a string: ")
q = deque(s)
is_pal = True


while len(q) > 1:
    if q.popleft() != q.pop():
        is_pal = False
        break

if is_pal:
    print(s,"is palindrome")
else:
    print(s,"is not palindrome")
