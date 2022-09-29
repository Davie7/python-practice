L1 = [1,2,3,4,5]

L2 = [1,2,3,4,5]


if L1 is L2:
    print(True)
else:
    print(False)

    
if L1 == L2:
    print(True)
else:
    print(False)

L3 = [8,9,1,2,3]

L4 = L3

L4[0] = 6

print(L4)
print(L3)

if L3 is L4:
    print(True)
else:
    print(False)

    
if L3 == L4:
    print(True)
else:
    print(False)
