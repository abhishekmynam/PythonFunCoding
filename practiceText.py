'''guestList =['john', 'james', 'david'] #, 'robert','chris','bob','frank']
print('you are invited, '+guestList[0])
print('you are invited, '+guestList[1])
print('you are invited, '+guestList[2])

print('james is not able to attend')

guestList.remove('james')'''

guestList =['john', 'james', 'david', 'robert','chris','bob','frank']
print (guestList)
guestList2=guestList[2:]
guestList.insert(2,'abhi')
print (guestList2)
print (guestList)
guestList2.append('abhishek')
print (guestList2)
print (guestList)
guestList2.remove('frank')
print (guestList)
guestList.pop()
print (guestList)
guestList.pop(4)
print (guestList)
print (guestList[:3])
lengths = len(guestList)
print (lengths)
userList=[1,4,45,56,87,99]
user=55
if user <=45:
    print(user)
elif user<78:
    print(user-6)
else:
    print(user-3)


'''
print (guestList[:-2])
for name in guestList[2:-2]:
    print (name)'''
'''


listVal= list(range(5,25,2));
print (listVal)

print(min(listVal))
print(max(listVal))
print(sum(listVal))

squares=[value+3 for value in range(1,10,2)]
print(squares)

print(sum(list(range(1,1000000))))
'''