#for i in range (1,11):
   # print (i)
#print ("hello wrold")

#movie1=input("the first movie is=")
#movie2=input("the second movie is=")
#print(movie1+movie2)

#num1=int(input("first number is="))
#num2=int(input("second number is="))
#sum=(num1+num2)
#print("the sum is=",sum)

"""numbers=[3,2,8,4,9,0,1,5,7,6]
numbers.sort(reverse=True)
print("numbers are arranges in descending order:",numbers)
numbers.sort()
print("numbers are arranged in ascending order:",numbers)

print(len(numbers))"""

"""for i in range(1,100):
 if i%5==0:
   print(i,"multiple of 5")
    
 elif i%3==0:
      print(i,"multiple of 3")"""
   
#movie1=input("first movie is:") 
#movie2=input("second movie is:")
#longest_movie=max(movie1,movie2,key=len)
#print("the lonest movie is:",longest_movie)
#print(len(longest_movie))
"""if movie1<movie2:
   print("movie1 is the longest")
elif movie1>movie2:
   print("movie2 is the longest")
else:
   print("both movies have same length")"""

#logical operators

"""a=30
b=12
c=27
if a>b and a>c: print("both statments are true")"""

"""a=30
b=33
c=23
if a>b or b<c: print("one of them is coreect")         #else statement is correct as none of the if value correct
else: print("nothing correct")"""
"""
a=20
b=30
if not a>b: print("a is not greater than b")"""
""" nested if
a=80
if a>20: 
   print("above 20")
   if a>40:
      print("greater than40")                    # only runs if the outer condition(a>20) is true
   if a>70:
      print("above 70")
   else:
      print("not above")"""

"""for i in range(1,101):
    if i%5==0:
        print(i,"multiple of 5")             #nested if
    if i%10==0:
         print(i,"multiple of 10")"""

"""a=10
b=20                       # variable swap
a,b=b,a
print(f"a:{a},b:{b}")"""

list=["apple","banana","papaya","lychee"]
#list.append("strawberry","guava")
#list.pop(0)
#del list[2]  #del specified index
list.remove("lychee") #remove specified item
print(list)
