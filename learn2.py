'''
Sometimes you’ll want to use the value of an item after you remove it from a
list. For example, you might want to get the x and y position of an alien that
was just shot down, so you can draw an explosion at that position. In a web
application, you might want to remove a user from a list of active members
and then add that user to a list of inactive members.
The pop() method removes the last item in a list, but it lets you work
with that item after removing it. The term pop comes from thinking of a
list as a stack of items and popping one item off the top of the stack. In
this analogy, the top of a stack corresponds to the end of a list.
'''

motorcycles = ['honda', 'yamaha', 'suzuki','ducati','kawasaki','harley','dirt bike']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
first_owned = motorcycles.pop(3)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

motorcycles.remove('yamaha')
print(motorcycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']
'''
print(cars)

cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
'''
cars.reverse();

print(cars)
print(len(cars))
