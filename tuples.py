topping =['pepper','tomato','onion','spinach','cheese','butter']
reqTop=['tomato','butter','cheese']

for top in sorted(topping,reverse=True):
    print(top)
dicts ={'color':'white','shade':'light','bright':'high'}
print(dicts['color'])
dicts['color']='black'
print(dicts['color'])
dicts['opposite']='white'
print(dicts['color'])
print(dicts['opposite'])
print(dicts)

for name in sorted(dicts.keys(), reverse=True):
    print(name)



message=input('this is my input\n')
print ('this is message '+message)