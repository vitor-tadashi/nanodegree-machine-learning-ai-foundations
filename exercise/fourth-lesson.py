# Quiz: Population Density Function
# Write a function named population_density that takes two arguments, population and land_area,
# and returns a population density calculated from those values. I've included two test cases that you
# can use to verify that your function works correctly. Once you've written your function, use the
# Test Run button to test your code.
# write your function here


def population_density(population, land_area):
    return population / land_area


# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))


# Quiz: readable_timedelta
# Write a function named readable_timedelta. The function should take one argument, an integer
# days, and return a string that says how many weeks and days that is. For example, calling the
# function and printing the result like this:
#
# print(readable_timedelta(10))
# should output the following:
#
# 1 week(s) and 3 day(s).
# Include a docstring that explains what the function does.
#
#
# # write your function here
#
#
# # test your function
# print(readable_timedelta(10))
# write your function here
def readable_timedelta(days):
    """
    Return a string of the number of weeks and days included in days.

    Parameters:
    days -- number of days to convert (int)

    Returns:
    string of the number of weeks and days included in days
    """
    week = int(days / 7)
    day = days - (week * 7)
    return "{} week(s) and {} day(s).".format(week, day)


# test your function
print(readable_timedelta(1))

# Quiz: Lambda with Map
# map() is a higher-order built-in function that takes a function and iterable as inputs,
# and returns an iterator that applies the function to each element of the iterable.
# The code below uses map() to find the mean of each list in numbers to create the list averages.
# Test run it to see what happens.
#
# Rewrite this code to be more concise by replacing the mean function with a
# lambda expression defined within the call to map().
numbers = [
    [34, 63, 88, 71, 29],
    [90, 78, 51, 27, 45],
    [63, 37, 85, 46, 22],
    [51, 22, 34, 11, 18]
]

mean = lambda num_list: sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)


# Quiz: Lambda with Filter
# filter() is a higher-order built-in function that takes a function and iterable as
# inputs and returns an iterator with the elements from the iterable for which the function returns True.
# The code below uses filter() to get the names in cities that are fewer than 10 characters long
# to create the list short_cities. Give it a test run to see what happens.
#
# Rewrite this code to be more concise by replacing the is_short function with a lambda expression
# defined within the call to filter().
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

is_short = lambda name: len(name) < 10

short_cities = list(filter(is_short, cities))
print(short_cities)


# Quiz: Implement my_enumerate
# Write your own generator function that works like the built-in function enumerate.
#
# Calling the function like this:
#
# lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]
#
# for i, lesson in my_enumerate(lessons, 1):
#     print("Lesson {}: {}".format(i, lesson))
# should output:
#
# Lesson 1: Why Python Programming
# Lesson 2: Data Types and Operators
# Lesson 3: Control Flow
# Lesson 4: Functions
# Lesson 5: Scripting
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]


def my_enumerate(iterable, start=0):
    for item in iterable:
        yield start, item
        start += 1


for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))


# Quiz: Chunker
# If you have an iterable that is too large to fit in memory in full (e.g.,
# when dealing with large files), being able to take and use chunks of it at a time can be very valuable.
#
# Implement a generator function, chunker, that takes in an iterable and yields a chunk of a specified size at a time.
#
# Calling the function like this:
#
# for chunk in chunker(range(25), 4):
#     print(list(chunk))
# should output:
#
# [0, 1, 2, 3]
# [4, 5, 6, 7]
# [8, 9, 10, 11]
# [12, 13, 14, 15]
# [16, 17, 18, 19]
# [20, 21, 22, 23]
# [24]
def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]


for chunk in chunker(range(25), 4):
    print(list(chunk))# Implement function here

