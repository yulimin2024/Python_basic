# IF usage- soccer game warning
yellow_card=1
foul=True
if foul:
    yellow_card+=1
    if yellow_card==2:
        print("kicked out")
    else:
        print("be careful")
else:
    print("warning")

# For usage
for x in range(10):
    print(f"{x+1}th jumping")

for x in range(1,20,3):
    print(f"{x}th increasing")

my_list=[1,2,3,5]
for x in my_list:
    print(x)
my_tuple=(1,4,7,8)
for x in my_tuple:
    print(x)
my_dic={'name':'Yuli', 'age':45, 'gender':'F'}
for x in my_dic.keys():
    print(x)
for x in my_dic.values():
    print(x)
for x in my_dic.items():
    print(x)
for x, y in my_dic.items():
    print(x, y)

fruit='apple'
for x in fruit:
    print(x)

# While usage
max=25
weight=0
item=3
while weight+item<=max:
    weight+=item
    print(weight)
    print("add more item")
print(f'total weight is {weight}')

#while+ break usage
drama=['season1', 'season2', 'season3', 'season4']
for x in drama:
    if x=='season3':
        print("boring, stop watching")
        break
    print(f'{x} watching')

# while+ continue usgae
drama=['season1', 'season2', 'season3', 'season4']
for x in drama:
    if x=='season3':
        print(f"{x} boring, stop watching")
        continue
    print(f'{x} watching')

for x in range(10):
    if x%2==1:
        continue
    print(x)