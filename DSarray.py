from array import*

array1=array('i',[1,2,3,4,5])
for i in array1:
    print(i)

print("accessing element at index 2")
print(array1[2])

print("inserting element into array")
array1.insert(1,60)
for i in array1:
    print(i)

print("deleting element 3")
array1.remove(3)
for i in array1:
    print(i)

print("searching an element")
print(array1.index(2))

print("updating elemet 60 to 20")
array1[1]=20
for i in array1:
    print(i)

