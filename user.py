class User:

    def __init__(self, emailAddress="", firstName="", lastName="", registrationDate=""):
        self.emailAddress = emailAddress
        self.firstName = firstName
        self.lastName = lastName
        self.registrationDate = registrationDate

    def save_user(self):
        print("You've been added to our list")