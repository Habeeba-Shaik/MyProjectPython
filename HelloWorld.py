print("HI")
print("{} {}".format("1st string value", 1))
a=("a",1,"b",2)
print("Tuple ",a)

#a[1]="c"
#print(a)
#a.append("ab")
print(a)
dict={"Name":"Habeeba","place":"Hyd"}
print(dict)
#insert
dict["Age"]=24
print("After intserting the new value: ",dict)
#update
dict["Age"]="25"
print("After updation: ",dict)
del dict["Age"]
print("After deletion: ",dict)

#for loop

obj=[1,2,3,4,5]
for i in obj:
    print(i)

#range-example-sum of 5 nautral numbers
#range(i,j) then j will be j-1
summed=0
for j in range(1,6):
    summed=summed+j
print("Sum of 5 natural numbers are: ",summed)
###
print("**********")
for k in range(1, 10, 2):
    print(k)
print("*****")
for x in range(8):
    print(x)