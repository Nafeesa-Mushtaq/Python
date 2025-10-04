class Person:
    address = "abc "
    name = "xyz"

    # if there is no need to use the class attribute in the function than we can mark the function as static method so that wedont have to pass it self arguemnt
    @staticmethod  # this method is static
    def greet():
        print("Good Morning")

    # in this function we are utilizing the attributes so we have to pass self otherwise it will thorw an error
    def info(self):
        print(f"The address is {self.address} and name is {self.name}")



Name = Person()
Name.greet()
Name.info()