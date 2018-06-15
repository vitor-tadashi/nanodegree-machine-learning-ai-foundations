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
