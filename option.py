from c_account import c_Account 
from c_account import logincls
class optioN():
    @classmethod
    def user (self):
        flag = True
        while flag:
            print("\n\tEnter 1 to Register")
            print("\tEnter 2 to Login")
            print("\tEnter 3 to Logout")
            try:
                value=int(input("\tEnter your chioce--->\t"))
            except:
                print("\tInvalid entry!\nPlease entry a valid choice")
            if value==1:
                c_Account.Register()
            elif value==2:
                logincls().Login()
            elif value==3:
                print("\t\t\t\t\tLogout successfully")
                quit()
                # print("_"*50,"Welcome to Vacation","_"*50)
