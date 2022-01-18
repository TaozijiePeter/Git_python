from operator import add,sub
def a_plus_abs_b(a,b):
    if b>=0:
        h=a+b
    else:
        h=a-b
    return h
a=int(input("请输入a的值： "))
b=int(input("请输入b的值： "))
print(a_plus_abs_b(a,b))
