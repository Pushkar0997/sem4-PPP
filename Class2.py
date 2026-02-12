class University:

    def __init__(self):

        self.name = "krish" # Public

        self._branch = "Maeers" # Protected
        self.__bal= 98769876 # Private

    def show(self):
        print("University Name:", self.name)
        print("Branch:", self._branch)
        print("Balance:", self.__bal)

class Branch2(University):

    def __init__(self):
        super().__init__()

    def display(self):
        print("Branch Name:", self._branch)  # Accessing protected member
        print("Balance:", self.__bal)  # This will raise an AttributeError

# Create an instance of Branch2
branch = Branch2()
branch.show()  # Accessing public and protected members through the parent class method