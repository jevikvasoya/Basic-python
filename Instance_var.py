class mobile():
    def __init__(self):
        self.model = "realme" # instance variable

    def show_model(self):
        print(self.model) # Accesing instance variable

realeme = mobile()
redmi = mobile()

print(redmi.model)
print(realeme.model) # Accessing instance variable outside the class

redmi.model = 'note 10s' # Changing instance variable value
print(redmi.model) 