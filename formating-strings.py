# format() method python
"""
The format() method formats the specified value(s) and insert them inside the string's placeholder.
The placeholder is defined using curly brackets: {}.
"""
txt = "Hello {word}"
print(txt.format(word = 'World!'))
#output : Hello World!

data1 = 'Hi, My name is {} and I am {} years old.'
print(data1.format('Ferisa', 20))
#output : Hi, My name is Ferisa and I am 20 years old.

data2 = 'Hi, My name is {name} and I am {number} years old.'
print(data2.format(name ='Ferisa', number = 20))
#output : Hi, My name is Ferisa and I am 20 years old.

data3 = 'Hi, My name is {0} and I am {1} years old.'
print(data3.format('Ferisa', 20))
#output : Hi, My name is Ferisa and I am 20 years old.
