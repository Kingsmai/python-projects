# Open a file in read mode by default
helloFile = open("data/hello.txt")

content = helloFile.read()

# Close the file
helloFile.close()

helloFile = open("data/hello.txt")

# readlines return a list of strings
print(helloFile.readlines())

helloFile.close()

# Open a file in write mode, it will truncate the file
helloFile = open("data/hello2.txt", "w")
# Use write method to write in the file and it will return the how many bytes or how many characters they wrote to it
# Write will not add a \n to each string
helloByte = helloFile.write("Hello!!!!!!!")
print(helloByte)
helloByte = helloFile.write("Hello!!!!!!!\n")
helloByte = helloFile.write("Hello!!!!!!!")
helloFile.close()

# Open a file in append mode, it will continue writing the file
helloFile = open("data/bacon.txt", "w")
helloFile.write("Bacon is not a vegetable.")
helloFile.close()

helloFile = open("data/bacon.txt", "a")
helloFile.write("\n\nBacon is delicious")
helloFile.close()

# To store complex data into a binary file,
import shelve
shelfFile = shelve.open("data/mydata")
shelfFile["Cats"] = ["Zophie", "Pooka", "Simon", "Fat-tail", "Cleo"]
shelfFile.close()

# Grab back the value
shelfFile = shelve.open("data/mydata")
print(shelfFile["Cats"])
shelfFile.close()

# We use file to save list, dict, and other non text file

# Shelf object is very similar to dictionary
shelfFile = shelve.open("data/mydata")
key = shelfFile.keys()
print(key)
print(list(key))
value = shelfFile.values()
print(value)
print(list(value))