# # Read the whole text
# handle = open("test.txt","r")

# data = handle.read()
# print(data)

# handle.close()

# # Read a single line

# handle = open("test.txt","r")

# data = handle.readline()
# print(data)

# handle.close()

# # Read multiple lines
# handle = open("test.txt","r")

# data = handle.readlines()
# print(data) 

# handle.close()

# # Looping through a file
# handle = open("test.txt","r")
# data = handle.read()
# counter = 0
# for word in data.split():
#     if word == "Python":
#         counter += 1
# print(counter)

# Write a file
handle = open("text-write.txt", "w")

handle.write("Hello Moringa")
handle.close()