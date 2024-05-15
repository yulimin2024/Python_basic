# Python_basic
First coding project in May 2024

# Method_string
letter='HOW ARE YOU'
print(letter.lower())
print(letter.split())
print(letter.count('H'))
print(letter.strip('U'))
print(letter.replace('YOU','WE'))

#Printout_string
python='python'
java='java'
print(python + ' ' + java)
print('{} and {} are commonly used coding languages'.format(python, java))
print('{1} and {0} are commonly used coding languages'.format(python, java))
print(f'{python} and {java} are commonly used coding langs')

#Change of line
snack='nacho is my favorate snack'
print(snack)
snack='nacho \n is my favorate \n snack'
print(snack)


# List
my_list=['a',1, 32, 'book', 120, 'cat']
print(my_list[2], my_list[5], my_list[:])
print('cat' in my_list)
print('dog' in my_list)
print(len(my_list))
my_list[3]='dog'
print(my_list)
my_list.append('pig') # add only one argument
print(my_list)
my_list.remove(32)
print(my_list)
your_list=['pizza', 10, 'sandwitch']
my_list.extend(your_list) # list +list
print(my_list)

#Tuple
my_tuple=('cat', 5, 'dog', 3) #packing
(t1, t2, t3, t4)=my_tuple  #unpacking
print(t1, t2, t3, t4, my_tuple)
numbers=(1,2,3,4,5,6,7)
(one, two, *others)=numbers  #others=list type
print(one, two, others[2])

#set
A={'a', 'b', 'c', 5}
B={'b','c', 'd', 3, 5}
print(A.intersection(B))
print(A.union(B))
print(A.difference(B))
A.add('g')
print(A)

#dictionary {key:value}
my_dic={'name':'Yuli', 'age':45, 'height':160, 'weight':55}
print(my_dic['name'], my_dic['height']) #dic-> key indexing
my_dic['gender']='female' #add key:value
print(my_dic)
my_dic['weight']=50
print(my_dic)
my_dic.update({'height':165, 'weight':52})
print(my_dic)
my_dic.pop('weight')
print(my_dic)
print(my_dic.keys())
print(my_dic.values())
print(my_dic.items())

# Change of type
my_tuple=('nacho', 'chips', 'nacho')
my_list=list(my_tuple)  #tuple -> list
my_list.append('scon')
print(my_tuple, my_list)
print(type(my_tuple), type(my_list))
my_tuple=tuple(my_list)
print(my_tuple)

my_set=set(my_list) #replicatd 'nacho' is removed
print(my_list)
my_list=list(my_set)  
print(my_list)
my_dic2=dict.fromkeys(my_list)
print(my_dic2)

#Question 1- Score:sum/average
Hong_dic={'kor':80, 'eng':75, 'math':55}
sum=(Hong_dic['kor']+Hong_dic['eng']+Hong_dic['math'])
avg=sum/3
print(f"sum={sum}, avg={avg} ")

#Question 2- even or odd number
number=12
if(number%2==0):
    print("the number is even")
else:
    print("the number is odd")

#Question 3- Dividing id numbers
Hong_id=[881120,'-', 1068234]
print(Hong_id[0], Hong_id[2])

Hong_id2=(881120, '-', 2058234)
(num_first, bar, num_last)=Hong_id
print(num_first, num_last)

#Question 4- M or F from id number
num_last=list(str(num_last)) #number ->string->list
print(type(num_last))
if (num_last[0])==1:
    print("Male")
else:
    print("Female")


#other way for Q 3,4 
pin="881120-1068264"
yyyymmdd=pin[:6]
num=pin[7:]
print(yyyymmdd, num)
if(pin[7]==1):
    print("Male")
else:
    print("Female")

#Question 5-replace function
string1='a:b:c:d:'
string2=string1.replace(':', '#')
print(string1,string2)

#Question 6- list.sort, list.reverse
list6=[1, 3, 5, 4, 2]
list6.sort()
list6.reverse()
print(list6)

#Question 7- list->str using join()
list7=['Life', 'is', 'too', 'short']
result=" ".join(list7) #join: list->string, " ":space
print(type(result), result)

#Question 8 - tuple -> list -> tuple
tuple8=(1,2,3)
list8=list(tuple8)
list8.append(4)
tuple8=tuple(list8)
print(tuple8, type(tuple8))

a=(1,2,3)
b=(4,) #type is tuple
print(a+b) #addition of tuples

#Question 9 dict
a=dict()
a['name']='python'
print(a)
a['a']='python'
print(a)
a[250]='python'
print(a)
print(a.keys())

#Question 10: dict -> extract key values
dict10={'A':90, 'B':80, 'c':70}
print(dict10['A'])
result=dict10.pop('B') #removing B and putting into result
print(dict10, result)


#Question 11: removing replicated values in list
list11=[1,1,1,2,2,3,3,3,4,4,5]
aSet=set(list11)
print(aSet)
blist=list(aSet)
print(blist)
