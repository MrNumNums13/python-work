message = "Hello Python World!"
print(message)

message = "Hello Python Crash Course World!"
print(message)

string1 = "This is a string"
string2 = 'This is also a string'

story = '   This is a story about my friend "Lary", Lary was a prick     '

# .title on a string changes every first character of each word and capitalizes it.
print(story.title())

print(story.upper())
print(story.lower())

# same kind of string concatenation in Java
# \n gives you a new line
# \t inserts a tab into the string
print(message + "\n\t" + story)

# rstrip() removes whitespace from the right side
# lstrip() removes whitespace from the left side
print(story.lstrip())

######## Numbers ########

# Same as most languages
# pemdas applies, floats work normally, no funny business

# parsing int to string
age = 23
#  message = "Happy " + age + "rd Birthday"
# This won't work because age is an Int not a string
# Do this instead
message = "Happy " + str(age) + "rd Birthday"
print(message)
