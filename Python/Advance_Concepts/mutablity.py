a=[]
b=a



print(id(a))
print(id(b))
# same address

a.append(35)
print(a)
print(b)
# same value

b=[]# mutability

print(a)
print(b)

# Immutable
a=8597
b=8597
print(id(a))
print(id(b))
# same address

a=8590
print(id(a))

b=a
print(a)
print(b)
print(id(a))
print(id(b))


# mutable default parameter -> bad idea , other object when created will get previous value if not specified
# better make it equal to None

