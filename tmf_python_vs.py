import datetime
from user import User
from helperFx import HelperFx


def main(self=None):
    # emailAddress = input("Please enter your email address: ")
    admin = User()

    emailAddress = HelperFx.get_email_address(self)
    domain = "@fool.com"

    while domain not in emailAddress:
        print("Sorry, that's not a domain we fools recognize.")
        emailAddress = HelperFx.get_email_address(self)

    firstName = input("Please enter your first name: ")
    lastName = input("Please enter your last name: ")
    registrationDate = datetime.date.today().strftime("%m/%d/%Y")
    print(f"Welcome {firstName} {lastName}! You are a new admin as of {registrationDate}!")
    # admin = User(emailAddress, firstName, lastName, registrationDate)

    User.__init__(admin, emailAddress, firstName, lastName, registrationDate)
    admin.save_user()


if __name__ == '__main__':
       main()