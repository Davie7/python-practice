string = "    geeks for geeks    "

# prints the string without stripping.
print(string)

# prints the string by removing leading and trailing whitespaces.
print(string.strip())

# prints the string by removing geeks
print(string.strip(' geeks'))

str1=' ekgs'
# prints the string by removing geeks also.
print(string.strip(str1))

state = " the King has the largest army in the entire world the "

# prints the string after removing the from beginning and end
print(state.strip(" the"))
