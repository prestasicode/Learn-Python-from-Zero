data = "Hello World!'
print(data)

# Slicing on the variable 'message' with only index 0 to index 5
data[0:5]
#'Hello'

# Slicing on the variable 'message' with only index 6 to index 12
data[6:12]
#'World!'

# to select every second element in the variable 'message'
data[::2]
#'HloWrd'

# corporation of slicing and striding
# get every second element in range from index 0 to index 6
data[0:6:2]
#'Hlo'
