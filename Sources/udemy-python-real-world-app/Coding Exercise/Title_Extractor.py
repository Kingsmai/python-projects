import pyperclip

while True:
    userinput = input("Please enter your string: ")
    if userinput == '\end':
        print("Program Ends!")
        break
    words = userinput.split(" ")
    pyperclip.copy("_{}.py".format("_".join(words[1:-1])))
print("Thank for use!\n")
