class Parent1:
    a = 8

class Parent2:
    b = 9

class Children(Parent1,Parent2):
    c = 10

ch = Children()
print(ch.a)
print(ch.b)
print(ch.c)