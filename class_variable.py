class ExampleClass:
    varia = ""

    def __init__(self, val):
        ExampleClass.varia += "CLASS VARIABLE"  # CLASS VARIABLE
        self.varia = "INSTANCE VARIABLE"  # INSTANCE VARIABLE
        varia = "LOCAL METHOD VARIABLE"  # LOCAL METHOD VARIABLE
        print(varia)


print("Before the very first object of the class is instantiated")
print(ExampleClass.__dict__)

print("Instantiating an instance of ExampleClass class")
example_object = ExampleClass(2)

print("After the very first object of the class has been instantiated")
print(ExampleClass.__dict__)
print(example_object.__dict__)
