#data in variable
data = 'hello python!'
print('Before uppercase: ', data )
#output : Before uppercase: hello python!

# convert uppercase the elements in a string
data_upper = data.upper()
print('After uppercase: ', data_upper)
#output : After uppercase: HELLO PYTHON!

# convert lowercase the elements in a string
data_lower = data.lower()
print('Again lowercase: ', data_lower)
#output : Again lowercase: hello python!

# convert first letter of string to uppercase
data_title = data.title()
print('The first element of the string is uppercase: ', data_title)
#output : The first element of the string is uppercase: Hello Python!

#find and replace string
data = 'Hello Python!'
data2 = data.replace('Hello', 'Hi')
data3 = data.replace('Python', 'World')
print(data2)
print(data3)
#output : Hi Python!
#output : Hello World!
#find
data = 'Hello World!'
print(data.find('Wo'))
# the output is the index number of the first element of the substring
#6
