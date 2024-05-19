# Listing recall items, Important!!!
products=['JOA-2020', 'JOA-2021', 'SIRO-2021', 'SIRO-2022']
recall=[]
# among the products, if a product starts with 'SIRO', add to recall list
for p in products:
    if p.startswith('SIRO'):
        recall.append(p)
print(recall)

# list comprehension: list=[변수활용 for 변수 in 반복대상 if 조건]
my_list=[1,2,3,4,5]
new_list=[x for x in my_list if x>3]
print(new_list)

# for the above products list, put 'SE' at the end
prod_se=[p+'SE' for p in products]
print(prod_se)
# for the above products list, change into small letters
prod_lower=[p.lower() for p in products]
print(prod_lower)
# for '22 products, put 'newly' at the end
prod_new=[p+'(newly)' for p in products if p.endswith('22')]
print(prod_new)

#Quiz 36) 'a'를 포함하는 문자를 모두 대문자로 변경하라
my_list=['korea', 'English', 'france']
new_list=[x.upper() for x in my_list if 'a' in x]
print(new_list)

#Question: while문을 사용해 1부터 1000까지 자연수 중 3의 배수의 합을 구하라.

result=0
i=1
while i<=1000:
    if(i%3==0):
        result+=i
    i+=1
print(result)

# Qeustion: while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해보자.

i=0
while True:
    i+=1
    if i>5:
        break
    print('*'*i)

# Question:for문을 사용해서 1부터 100까지의 숫자를 출력해라. 

for i in range(1, 101, 1):
    print(i, end=',') # 옆으로 계속 출력 end=' '   

#Question: A 학급의 평균 점수 구하기
A=[70,60,55,75,95,90,80,80,85,100]
total=0
for score in A:
    #total+=float(score)
    total+=score # 리스트 내 변수는 보통 string 아님?? 숫자는 아님!
average=total/len(A)
print(total, average)

#Q 리스트 중에서 홀수에만 2 곱하여 저장하도록 한다.
numbers=[1, 2, 3, 4, 5]

result=[x*2 for x in numbers if x % 2==1]
print(result)

## by another way
result1=[]
for n in numbers:
    if n%2==1:
        result1.append(n*2)
print(result1)

# 함수 Function!!! - def func_name():
def show_price():
    print("price for cut:10000won")

show_price()    # 호출해야 함수의 결과값이 나옴!
 
 #함수- 전달값, def 함수명(전달값):
def show_price(customer):
    print(f"{customer} 고객님")
    print("커트가격은 15,000원입니다")

customer1='김파마'
show_price(customer1)

customer2='이커트'
show_price(customer2)

#함수 - 반환값 return: 함수 내에서 처리된 결과를 반환
def get_price():
    return 15000

price=get_price()
print(f"가격은 {price} 입니다")

# vip 고객 여부에 따라 가격 차등 함수
def get_price(is_vip):
    if is_vip==True:
        return 10000
    else:
        return 15000

price=get_price(True)
print(f"커트가격은 {price} 입니다")

# 함수- 기본값: 전달값의 기본으로 setting 해줌
def get_price(is_vip=False): #전달값=False 세팅
    if is_vip==True:
        return 10000
    else:
        return 15000
price=get_price()
print(f"cut price is {price}")

# 함수-키워드 값: 전달값이 많을 때, 기본세팅 변경하는 값만 전달해줌
def get_price(is_vip=False,
              is_birthday=False,
              is_membership=False,
              card=False,
              review=False,
              first_time=False): # 전달값이 다수!
    print()    
price=get_price(review=True, is_birthday=True) # 전달값중 review, birthday 키워드 값만 정해서 전달함.

# 파일입출력- open(파일명, 모드, encoding='인코딩')
f=open('list.txt', 'w', encoding='utf8') #쓰기모드로 파일 열기
f.write('민정임도 배우자\n')
f.write('오환희도 배운다 \n')
f.write('오은성도 배운다\n')
f.close()

f=open('list.txt', 'a', encoding='utf8')
f.write('우리 다같이 배우자') #append(x), write(o)
f.close()

f=open('list.txt', 'r', encoding='utf8')
content=f.read() #파일 기재된 내용을 content로 받음.
print(content)

f=open('list.txt', 'r', encoding='utf8')
for line in f: #한줄씩 읽는다
    print(line, end='--')
f.close()

# with open(...) as f: equals to f=open(...)
with open('list.txt','a',encoding='utf8') as f:
    f.write("파이선은 c보다 쉽다 \n")
    f.write('파이선은 AI에 많이 사용된다')

with open('list.txt','r',encoding='utf8') as f:
    content=f.read()
    print(content)

# lambda 함수 대신에 사용, 한줄로 간결하게 표현가능
add=lambda a, b: a+b
result=add(3,5)
print(result)