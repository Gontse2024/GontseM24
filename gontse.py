name = input("Enter your name: ")
age = int(input("Enter your age: "))
location = input("Enter your location: ")

# first approach
print("hello ", name, "you are and live in", location)

#second approach %
print ("second approach")
print("Hello %s you are %d years old and live in %s"%(name, age, location))

#third approach format
print("third approach")
print("Hello {}  you are {} years old and live in {}".format(name, age, location))