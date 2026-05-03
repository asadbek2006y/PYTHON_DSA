# # Control structures determine the orgder in which code executes. They allow us to control the flow of our program and make decisions based on certain conditions. In this lesson, we will cover the following control structures:
# # 1. Conditional statements (if, elif, else)
# # 2. Loops (for, while)
# # 3. Control Flow Statements (break, continue, pass)

# temprature =  25 
# if temprature > 30: 
#     print("It's a hot day")
# elif temprature > 20: 
#     print("It's warm outside")
# else: 
#     print("It's a cold day")


# # Chaining Comparisons
# age = 18 
# if 18 <= age < 65: 
#     print("working age")

# # Compounding Conditions
# temprature = 25 
# good_oxygen_level = True
# if temprature > 20 and good_oxygen_level:
#     print("It's a good day to go outside")



# ## Loops
# fruits = [ "apple", "banana", "cherry" ]
# for fruit in fruits:
#     print(fruit)
#     # Output:
#     # apple
#     # banana
#     # cherry

# for letter in "Sampletext":
#     print(letter)
#     # Output:
#     # S
#     # a
#     # m
#     # p
#     # l
#     # e
#     # t
#     # e
#     # x
#     # t

# fruits = [ "apple", "banana", "cherry" ]
# for index, fruit in enumerate(fruits):
#     print(index, fruit)

# # Range with Step 
# for i in range(0, 10, 2):
#     print(i)
#     # Output:
#     # 0
#     # 2
#     # 4
#     # 6
#     # 8

# #b. While Loop
# count = 5 
# while count > 0: 
#     print(count)
#     count -= 1
# print("Blast off!")

# # While loop with else 
# # count = 0 
# while count < 5: 
#     print(count)
#     count += 1
# else: 
#     print("Loop completed successfully")

# Control Flow Keywords
# a. Break
for i in range(10):
    if i == 5:
        break
    print(i)

# b. Continue
for i in range(10):
    if i == 5: 
        continue
    print(i)

# c. Pass
for i in range(10):
    if i == 5: 
        pass
    print(i)