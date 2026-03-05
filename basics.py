
# num = input("Enter a number: ")
# print("User entered: ",num,type(num))

# Data conversion

# y = "10000001"
# print("y: ",type(y))

# convert y to int
# x = int(y)
# print("x: ",type(x))



# user_input = int(input("Enter a number: "))

# 12 / 2 == 0

# if user_input even print("it is a even number") else ("it is a odd number")


# if user_input % 2 == 0:
#     print("even")
# else:
#     print("odd")


# user_input = input("Enter a day: ")

# if user_input == "sunday":
#     print("First day")
# elif user_input == "monday":
#     print("second day")
# elif user_input == "tuesday":
#     print("third day")
# elif user_input == "wednesday":
#     print("fourth day")
# elif user_input == "thursday":
#     print("fifth day")
# elif user_input == "friday":
#     print("sixth day")
# elif user_input == "saturday":
#     print("seventh day")
# else:
#     print("invalid day")


day = "sunday"
month = "february"

# and not or

# sunday and january => True


# if (day == "sunday" or month == "january") or (day == "sunday" and month == "february"):
#     print("ok")
# else:
#     print("not ok")


# Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

username = "udhaya nagaraj"

# print(username[::-1])

# range() => 0 ...... 10
# 0...9

# for i in range(0,10):
#     print(i)


u_len = len(username) - 1
# print(u_len)

#start_index,stop_index,step
# jar

# for i in range(u_len,-1,-5):
#     print(i)
#     print(username[i],end="")
# print()


nums = [1,2,3,4,5,6,7,8,9,10]

# 1. using for loop find the total sum
# 2. print in reverse order
# 3. find the number of even and odd numbers count

# import time

# start_time = time.time()

# x = sum(nums)
# end_time = time.time()

# print("Execution time for sum: ",end_time - start_time)
# print(x)

# count = 0
# start_time = time.time()
# for i in range(0,len(nums)):
#     count += nums[i]
#     # count = count + nums[i]
# end_time = time.time()

# print("Execution time for for loop sum: ",end_time - start_time)

# 4.29e-06 = 0.00000429 seconds

# 1.40e-05 = 0.00001406 seconds


# for i in nums:
#     print(i)

# pass
# break

# x = 10

# if x > 5:
#     pass
# elif x > 15:
#     print("greater than 15")


# for i in nums:
#     if i == 5:
#         break

#     print(i)
# else:
#     print("Looped nums")

# Number guessing game

# 1. get input from user
# 2. default value 0 to 100
# 3. user value == default Value
# 4. if equals: print("found the answer") break
# 5. user input 
# 6. total tries 10 times.

# while True:
    
default_value = 99
total_tries = 10
available_tries = total_tries

# while True:
#     user_input = int(input("Enter a number between 0 to 100: "))
#     if user_input == default_value:
#         print("Found the answer!")
#         break
    
#     available_tries -= 1
#     print(f"You have remaining {available_tries} lifes.")
#     if available_tries == 0:
#         print("Better luck next time!")
#         break


# while available_tries >= 1:
#     user_input = int(input("Enter a number between 0 to 100: "))
#     if user_input == default_value:
#         print("Found the answer!")
#         break
#     elif user_input > default_value: #99 55 > 99
#         available_tries -= 1
#         print("user input greater than default value")
#     elif user_input < 0: #55 < 0
#         pass
#     else:
#         available_tries -= 1

#     print(f"You have remaining {available_tries} lifes.")

# default_value 99 > 100 eg 1000
# print invalid number

# negative number:
# print("it negative number")
# pass


# factorial

u_num = input("Enter a number")

u_num = 2


print(u_num*u_num*u_num)


# u_num.