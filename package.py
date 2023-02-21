from payment1 import Payment
import time
class price():
    @classmethod
    def members (self,price):
        print("_"*50,"_"*50)
        time.sleep(2)
        value2=int(input("\n\tEnter the package--->"))
        
        #print(value2)
        if value2:          
            Total_price =value2*price
            print("\tTotal Amount=",Total_price)
            print("_"*50,"_"*50)
            print("\n")
            Payment().paymentmethod()      

    

