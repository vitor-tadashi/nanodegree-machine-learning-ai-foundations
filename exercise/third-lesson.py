# Practice: Which Prize
# Write an if statement that lets a competitor know which of these prizes they won based on the number of
# points they scored, which is stored in the integer variable points.
# Points	Prize
# 1     - 50	wooden rabbit
# 51    - 150	no prize
# 151   - 180	wafer-thin mint
# 181   - 200	penguin
# All of the lower and upper bounds here are inclusive, and points can only take on positive integer values up to 200.
# In your if statement, assign the result variable to a string holding the appropriate message
# based on the value of points. If they've won a prize, the message should state "Congratulations!
# You won a [prize name]!" with the prize name.
# If there's no prize, the message should state "Oh dear, no prize this time."
# Note: Feel free to test run your code with other inputs,
# but when you submit your answer, only use the original
# input of points = 174. You can hide your other inputs by commenting them out.
points = 174  # use this input to make your submission

# write your if statement here
result = "Congratulations! You won a {}!"
if points <= 50:
    result = result.format("wooden rabbit")
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = result.format("wafer-thin mint")
elif points <= 200:
    result = result.format("penguin")

print(result)

# Quiz: Using Truth Values of Objects
# The code below is the solution to the Which Prize quiz you've seen previously.
# You're going to rewrite this based on what you've learned about truth values.
# You will use a new variable prize to store a prize name if one was won, and then
# use the truth value of this variable to compose the result message. This will involve two if statements.
#
# 1st conditional statement: update prize to the correct prize name based on points.
# 2nd conditional statement: set result to the correct phrase based on whether prize is evaluated as True or False.
#
# If prize is None, result should be set to "Oh dear, no prize this time."
# If prize contains a prize name, result should be set to "Congratulations! You won a {}!".format(prize).
# This will avoid having the multiple result assignments for different prizes.
# At the beginning of your code, set prize to None, as the default value.
points = 174  # use this as input for your submission

# establish the default prize value to None
prize = None

# use the points value to assign prizes to the correct prize names
if points <= 50:
    prize = "wooden rabbit"
elif points <= 180:
    prize = "wafer-thin mint"
elif points <= 200:
    prize = "penguin"

# use the truth value of prize to assign result to the correct prize
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."

print(result)


# Quiz: Create Usernames
# Write a for loop that iterates over the names list to create a usernames list.
# To create a username for each name, make everything lowercase and replace spaces with underscores.
# Running your for loop over the list:
#
# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
#
# should create the list:
#
# usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]
#
# HINT: Use the .replace() method to replace the spaces with underscores.
# Check out how to use this method in this Stack Overflow answer.
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    usernames.append(name.replace(' ', '_').lower())

print(usernames)


# Quiz: Modify Usernames with Range
# Write a for loop that uses range() to iterate over the positions in usernames to modify the list.
# Like you did in the previous quiz, change each name to be lowercase and replace spaces with underscores.
# After running your loop, this list
#
# usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
#
# should change to this:
#
# usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for index in range(4):
    usernames[index] = usernames[index].lower().replace(' ', '_')

print(usernames)


# Quiz: Tag Counter
# Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags.
# XML is a data language similar to HTML. You can tell if a string is an XML tag if it
# begins with a left angle bracket "<" and ends with a right angle bracket ">".
# Keep track of the number of tags using the variable count.
#
# You can assume that the list of strings will not contain empty strings.
tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    if token[0] == "<" and token[-1] == ">":
        count += 1

print(count)

# Quiz: Create an HTML List
# Write some code, including a for loop, that iterates over a list of strings and creates a single string,
# html_str, which is an HTML list. For example, if the list is items = ['first string', 'second string'],
# printing html_str should output:
#
# <ul>
# <li>first string</li>
# <li>second string</li>
# </ul>
# That is, the string's first line should be the opening tag <ul>.
# Following that is one line per element in the source list, surrounded by <li> and </li> tags.
# The final line of the string should be the closing tag </ul>.
items = ['first string', 'second string']
html_str = "<ul>\n"
# "\ n" is the character that marks the end of the line, it does
# the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    html_str += "<li>{}</li>\n".format(item)

html_str += "</ul>"

print(html_str)


# Quiz: Count By
# Suppose you want to count from some number start_num by another number count_by until
# you hit a final number end_num. Use break_num as the variable that you'll change each time through the loop.
#
# Before the loop, what do you want to set break_num equal to? How do you want to change
# break_num each time through the loop? What condition will you use to see when it's time to stop looping?
#
# After the loop is done, print out break_num, showing the value that indicated it was time to stop looping.
start_num = 5
end_num = 100
count_by = 2

break_num = start_num
# write a while loop that uses break_num as the ongoing number to
#   check against end_num
while break_num < end_num:
    break_num += count_by

print(break_num)


# Quiz: Count By Check
# Suppose you want to count from some number start_num by another number count_by until
# you hit a final number end_num, and calculate break_num the way you did in the last quiz.
#
# Now in addition, address what would happen if someone gives a start_num that is greater than end_num.
# If this is the case, set result to "Oops! Looks like your start value is greater than the end value.
# Please try again." Otherwise, set result to the value of break_num.
start_num = 5
end_num = 100
count_by = 2

# write a condition to check that end_num is larger than start_num before looping
# write a while loop that uses break_num as the ongoing number to
#   check against end_num
if start_num > end_num:
    result = "Oops!  Looks like your start value is greater than the end value.  Please try again."

else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by

    result = break_num

print(result)

# Quiz: Nearest Square
# Write a while loop that finds the largest square number less than an integerlimit
# and stores it in a variable nearest_square. A square number is the product of an integer
# multiplied by itself, for example 36 is a square number because it equals 6*6.
#
# For example, if limit is 40, your code should set the nearest_square to 36.
limit = 40

# write your while loop here
num = 0
while (num+1)**2 < limit:
    num += 1
nearest_square = num**2

print(nearest_square)


# Quiz: Break the String
# Write a loop with a break statement to create a string, news_ticker, that is exactly 140 characters long.
# You should create the news ticker by adding headlines from the headlines list, inserting a space in between each
# headline. If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 characters long.
#
# Remember that break works in both for and while loops. Use whichever loop seems most appropriate.
# Consider adding print statements to your code to help you resolve bugs.
# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here
for headline in headlines:
    news_ticker += headline + " "
    news_ticker = (news_ticker[:140]) if len(news_ticker) > 140 else news_ticker


print(news_ticker)


# Quiz: Zip Coordinates
# Use zip to write a for loop that creates a string specifying the label and coordinates of each
# point and appends it to the list points. Each string should be formatted as label: x, y, z.
# For example, the string for the first coordinate should be F: 23, 677, 4.
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for label, x, y, z in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(label, x, y, z))


for point in points:
    print(point)


# Quiz: Zip Lists to a Dictionary
# Use zip to create a dictionary cast that uses names as keys and heights as values.
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print(cast)


# Quiz: Unzip Tuples
# Unzip the cast tuple into two names and heights tuples.
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here
names, heights = zip(*cast)

print(names)
print(heights)


# Quiz: Transpose with Zip
# Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix.
# There's actually a cool trick for this! Feel free to look at the solutions if you can't figure it out.
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)

# Quiz: Enumerate
# Use enumerate to modify the cast list so that each element contains the name followed by the
# character's corresponding height. For example, the first element of cast should change from "Barney Stinson" to
# "Barney Stinson 72".
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# write your for loop here
for i, name in enumerate(cast):
    cast[i] = "{} {}".format(name, heights[i])

print(cast)


# Quiz: Extract First Names
# Use a list comprehension to create a new list first_names containing just the first names in names in lowercase.
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.lower().split()[0] for name in names]
print(first_names)


# Quiz: Multiples of Three
# Use a list comprehension to create a list multiples_3 containing the first 20 multiples of 3.
multiples_3 = [x*3 for x in range(1, 21)]
print(multiples_3)


# Quiz: Filter Names by Scores
# Use a list comprehension to create a list of names passed that only include those that scored at least 65.
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for (name, score) in scores.items() if score >= 65]
print(passed)