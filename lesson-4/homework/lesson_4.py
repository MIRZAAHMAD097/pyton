#lesson 4
#1
mydict={"apple":2, "orange":5, "banana":13, "strawberry": 1}

asc_sorted=dict(sorted(mydict.items(), key=lambda item: item[1]))

desc_sorted= dict(sorted(mydict.items(), key=lambda item: item[1], reverse = True))

print("ascending: ", asc_sorted)
print("desending: ", desc_sorted)


#2
my_dict={0:10, 1:20}
my_dict[2]=30
print(my_dict)

#3
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}

dic4= {**dic1, **dic2, **dic3}
print(dic4)

#4
n = int(input("enter a number: "))

square = {x : x*x for x in range(1, n+1)}

print(square)

#5
square = {x: x*x for x in range(1, 16)}

print(square)

#6
set1= {"apple", "orange", "banana"}

print(set1)

#7
set2={"apple", "orange", "banana"}

for item in set2:
    print(item)


#8
set3={"banana", "apple", "orange"}

set3.add("strawberry")

set3.update(["pineapple", "cherry"])
print(set3)

#9
set3={"banana", "apple", "orange"}
set3.remove("apple")

print(set3)

#10
set3={"banana", "apple", "orange"}

item="orange"

if item in set3:
    set3.remove(item)

print(set3)




