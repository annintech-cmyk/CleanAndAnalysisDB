class User:
    def __init__(self,name,email,password, age):
        self.email = email
        self.name = name
        self.password = password

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_password(self,password):
        return password == self.password

    def check_email(self,email):
        return email == self.email

    def authenticate(self):
        if self.password.lower() == self.name.lower():
            print("Login Successful!")
            return True
        else:
            print("Please try again!")
            return False

    def isMajor(self):
        if self.age >= 18:
            print("You are Major")
        else:
            print("You are not Major")

usee1 = User("Ann","aa@gg.com","Ann", 30)
usee1.authenticate()
user2 = User("Ann", 30)
usee1.isMajor()

