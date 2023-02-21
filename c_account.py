import re
from search import Search

class c_Account():
        _name=["Boomi","Abhi","Arivu","Sharmi","Mano"]
        _password=["Boomi@123","Abhi@123","Arivu@123","Sharmi@123","Mano@123"]
        _phone_number=[9442755071,9442755972,9442755073,9442755074,9443755075]
        _Email_id=["boomi1@gmail.com","abhi2@gmail.com","arivu3@gmail.com","sharmi4@gmail.com","mano5@gmail.com"]
        @classmethod
        def Register(self):
            name1=input("\n\tEnter your name: ")
            self._name.append(name1)
            while True:
                phone_number1=int(input("\tEnter your Phone_number:"))
                if 6000000000 < phone_number1 and 10000000000 > phone_number1:
                    self._phone_number.append(phone_number1)
                    break
                else:
                    print("\tInvalid phone number!\nPlease try  to enter a valid phone number")

            Email_id1=input("\tEnter Email ID:")
            self._Email_id.append(Email_id1)
            flag = True
            regex = ("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$")
            rule = re.compile(regex)
            while flag:
                password1 = input("\tEnter the password:")
                if re.search(rule, password1):
                    self._password.append(password1)
                    flag = False
                else:
                    print("\tInvalid password!\nPlease try  to enter a valid password")
            logincls().Login()
class logincls(c_Account):
        global valid
        valid = 0
        @classmethod
        def Login(self):
            print("_"*50,"Login","_"*50)
            name1=input("\n\tEnter your name:")
            password1=input("\tEnter your Password:")
            for i in range (len(self._name)):  
                if name1 == self._name[i]:
                    if password1 == self._password[i]:   
                        print("_"*50,"Login Successfully","_"*50)
                        Search().place()
                        valid = 1
            if valid == 0:
                print("\tInvalid password/User Name")
                



        


        



        
