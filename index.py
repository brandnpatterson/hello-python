#lists
list1 = [1, 2, 3]
list2 = [
    # dictionaries
    {
        "message": "Hello world"
    },
    {
        "message": "Testing 123465"
    },
    {
        "message": "Hello sunshine"
    }
]

# tuples
tuple1 = (
    (0,'zero',),
    (1,'one',)
)

# for in loop
for index, list_item in enumerate(list2):
    list_item["message"] = list_item["message"] + " " + (str(index * index + 10))

# functions
def print_list(mylist):
    print(mylist)

def print_tuple(mytuple):
    print(mytuple)

# call functions
print_list(list2)
print_tuple(tuple1)

# classes
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Hank", 22)

print(f"{p1.name} is a cool name")
