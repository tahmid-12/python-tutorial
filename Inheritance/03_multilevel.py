class P1:
    a = 5

class P2(P1):
    b = 8

class Children(P2):
    c = 9

ch = Children()
print(ch.a)
print(ch.b)
print(ch.c)