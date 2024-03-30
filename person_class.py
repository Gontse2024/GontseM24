class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

def main():
    person1 = Person("John", 30, "male")
    person1.introduce()

if __name__ == "__main__":
    main()


