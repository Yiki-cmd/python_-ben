"""
x=3
y=4
sum=x+y
z="thomas"
y="tobi"
print(sum)
print(x,y)
print(z+y)

my_first_list=[1,2,3,4,5,6,7,8,9]
my_second_list=["apple" "banana" "orange" "kiwi" "cherry" "mango"]
my_first_list.append(22)
my_first_list.append("true")
print(my_first_list)
print("---------------------------------------")
my_first_list.insert(3,10)
# in 3.index adds 10
print(my_first_list)
my_first_list.extend(my_second_list)
print(my_first_list)
my_second_list.extend(my_first_list)
print(my_second_list)
print("----------------------------------")
my_first_list=(*my_first_list,*my_second_list)
print(my_first_list)
"""
my_first_list=[1,2,3,4,5,6,7,8,9]
my_first_list.remove(7)
print(my_first_list)
my_first_list.pop()
print(my_first_list)
my_first_list.pop(2)
print(my_first_list)

print("------------------------------------")
"""
i=0
while i<10:
    print(i)
    i+=1
    
print("---------------------")

i=10
while i>1:
  print(i)
  i=i-1
"""
myList=["apple","banana", "orange", "kiwi"]
print(myList[2])
print(myList)

print("------------------------------")
i=0
while i<=4:
    print(myList[i])
    i=i+1