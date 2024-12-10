# Create a list of 5 random numbers and print the list.
Rand_Numbers=[1,5,7,9,11]
print(Rand_Numbers)
# new  3 random numbers
Rand_New_Numbers=[13,15,17]
print(Rand_New_Numbers)
# add the elements of the Rand_New_Number to Rand_Numbers
Rand_Numbers.extend(Rand_New_Numbers)
print("updated List:",Rand_Numbers)
# insert the new element to the sp,ific position based on the index
Rand_Numbers.insert(1,3)
print("updated List:",Rand_Numbers)


# Generate a list of 5 random numbers using for loop
import random
random_numbers = [random.randint(1, 100) for _ in range(5)]
print(random_numbers)
# Insert 3 new values using the for loop to the list and print the updated list.
new_values = [random.randint(1, 100) for _ in range(3)]
print(new_values)
# add element from the new_values to the random_numbers
random_numbers.extend(new_values)
print("Updated List with extend:",random_numbers)
# insert new_values elements to the specific postion of the random_numbers
random_numbers.insert(1, new_values)
print("Updated List with insert:",random_numbers)
print ( type(random_numbers))



# Create a dictionary with keys 'name', 'age', and 'address'
# and values 'John', 25, and 'New York' respectively.
student={"name":"John","age":"25","address":"New York"}
print(student)
student.update({"Phone NO":"1234567890"})
print(student)

# # Creating a set with values 1, 2, 3, 4, and 5
new_set = {1, 2, 3, 4, 5}
print("Set:", new_set)

# Add the value 6 to the set created "new_set"
new_set.add(6)
print("New  Set:",new_set)

# Remove the value 3 from the set created "mew_set"
new_set.remove(3)
print("updated set",new_set)

# Create a tuple  with values 1, 2, 3, and 4
tuple = (1, 2, 3, 4)
print("tuple",tuple)

# print the length of the tuple created
print(len(tuple))
