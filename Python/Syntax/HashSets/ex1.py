#define a set
student_ids = set()

#add elements to the set
student_ids.add(103)
student_ids.add(100)
student_ids.add(101)
student_ids.add(102)
student_ids.add(100)

print(student_ids) #this will print everything in the set once
print(101 in student_ids) #this will print True


#Hash sets in python are unordered, 
# so the order of the elements may not be the same as the order they were added. 
#check in example

