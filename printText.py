message = "Hello Python world!      "
print(message.upper())
message1 = "hello python crash course world!"
print(message1.title() + " " + message.upper().rstrip())

message2 = 1234
print(message + " " + message1 + " " + str(message2))

print(3 / 2)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[3].title())

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(2, 'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)
