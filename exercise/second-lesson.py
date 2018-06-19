# Quiz: Average Electricity Bill
# My electricity bills for the last three months have been $23, $32 and $64.
# What is the average monthly electricity bill over the three month period?
# Write an expression to calculate the mean, and use print() to view the result.
# Write an expression that calculates the average of 23, 32 and 64.
# Place the expression in this print statement.
bills = [23, 32, 64]
average_monthly_bill = sum(bills)/len(bills)
print(average_monthly_bill)


# Quiz: Calculate
# In this quiz you're going to do some calculations for a tiler.
# Two parts of a floor need tiling. One part is 9 tiles wide by 7 tiles long,
# the other is 5 tiles wide by 7 tiles long. Tiles come in packages of 6.
# 1. How many tiles are needed?
# 2. You buy 17 packages of tiles containing 6 tiles each. How many tiles will be left over?

floor_one = 9*7
floor_two = 5*7
total_tiles = floor_one+floor_two
tiles_seventeen_packages = 17*6
remnant_tiles = tiles_seventeen_packages - total_tiles

# Fill this in with an expression that calculates how many tiles are needed.
print(total_tiles)

# Fill this in with an expression that calculates how many tiles will be left over.
print(remnant_tiles)


# Quiz: Assign and Modify Variables
# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall = rainfall*0.9

# add the rainfall variable to the reservoir_volume variable
reservoir_volume = reservoir_volume+rainfall

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume = reservoir_volume*1.05

# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume = reservoir_volume*0.95

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume = reservoir_volume-2.5e5

# print the new value of the reservoir_volume variable
print(reservoir_volume)


# Quiz: Which is denser, Rio or San Francisco?
# Try comparison operators in this quiz!
# This code calculates the population densities of Rio de Janeiro and San Francisco.
# Write code to compare these densities.
# Is the population of San Francisco more dense than that of Rio de Janeiro?
# Print True if it is and False if not.
sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise
print(san_francisco_pop_density > rio_de_janeiro_pop_density)


# Quiz: Fix the Quote
# The line of code in the following quiz will cause a SyntaxError,
# thanks to the misuse of quotation marks. First run it with Test Run to view the error message.
# Then resolve the problem so that the quote (from Henry Ford)
# is correctly assigned to the variable ford_quote.
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'


# Quiz: Write a Server Log Message
# In this programming quiz, you’re going to use what you’ve
# learned about strings to write a logging message for a server.
# You’ll be provided with example data for a user,
# the time of their visit and the site they accessed.
# You should use the variables provided and the techniques
# you’ve learned to print a log message like this one
# (with the username, url, and timestamp replaced with values from the appropriate variables):
# Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20.
# Use the Test Run button to see your results as you work on coding this piece by piece.
username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."
print(username + " accessed the site " + url + " at " + timestamp + ".")


# Quiz: len()
# Use string concatenation and the len() function to find the
# length of a certain movie star's actual full name. Store that
# length in the name_length variable. Don't forget that there are
# spaces in between the different parts of a name!
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length = len(given_name + " " + middle_names + " " + family_name)

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)


# Quiz: Total Sales
# In this quiz, you’ll need to change the types of the input and output data in order to get the result you want.

# Calculate and print the total sales for the week from the data provided.
# Print out a string of the form "This week's total sales: xxx",
# where xxx will be the actual total of all the numbers.
# You’ll need to change the type of the input data in order to calculate that total.
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.
monday_sales = int(mon_sales)
tuesday_sales = int(tues_sales)
wednesday_sales = int(wed_sales)
thursday_sales = int(thurs_sales)
friday_sales = int(fri_sales)
total_sales = monday_sales+tuesday_sales+wednesday_sales+thursday_sales+friday_sales
print("This week's total sales: " + str(total_sales))


# Quiz: List Indexing
# Use list indexing to determine how many days are in a particular month
# based on the integer variable month, and store that value in the integer
# variable num_days. For example, if month is 8, num_days should be set to 31,
# since the eighth month, August, has 31 days.

# Remember to account for zero-based indexing!
month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month
num_days = days_in_month[month-1]

print(num_days)


# Quiz: Slicing Lists
# Select the three most recent dates from this list using list slicing notation. Hint: negative indexes work in slices!


eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']


# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])


# Quiz: Define a Dictionary
# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5
population = {"Shanghai": 17.8, "Istanbul": 13.3, "Karachi": 13.0, "Mumbai": 12.5}
print(population)


# Quiz: Adding Values to Nested Dictionaries
# Try your hand at working with nested dictionaries.
# Add another entry, 'is_noble_gas,' to each dictionary in the elements dictionary.
# After inserting the new entries you should be able to perform these lookups:
# >>> print(elements['hydrogen']['is_noble_gas'])
# False
# >>> print(elements['helium']['is_noble_gas'])
# True
elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't
elements["hydrogen"]["is_noble_gas"] = False
elements["helium"]["is_noble_gas"] = True

print(elements['hydrogen']['is_noble_gas'])
print(elements['helium']['is_noble_gas'])
