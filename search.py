from package import price
import time
class Search:
    @classmethod
    def place (self):
        time.sleep(5)
        print("\n","_"*50,"Welcome to Vacation","_"*50)
        value1=int(input("\n\t1.Hill Station \n\t2.Beach Areas\n\t3.Historical places \n\t Select the places--->"))
        if value1==1:
            click1 =int(input("\n\t1.Ooty\n\t2.Darjeeling\n\t3.Munnar\n\tselect your favourite location--->"))
            if click1==1:              
               hotel_choice = int(input("\n\t1.Gem park\n\t2.Sherlock Hotel\n\t3.Destiny-Farm Report\n\tEnter Your Choice--->"))  
               if hotel_choice == 1:
                    price().members(7000)
               if hotel_choice == 2:
                    price().members(9000)
               if hotel_choice == 3:
                    price().members(5000)
            elif click1==2:
                hotel_choice = int(input("\n\t1.Hotel MerryGold\n\t2.Maruti Luxury Homestay\n\t3.Mayfair Darjeeling\n\tEnter Your Choice--->"))  
                if hotel_choice == 1:
                    price().members(17000)
                if hotel_choice == 2:
                    price().members(13000)
                if hotel_choice == 3:
                    price().members(15000)
            elif click1==3:
                hotel_choice = int(input("\n\t1.Chandys Windy Woods\n\t2.Sprise Munnar Resort\n\t3.Fragrant Nature Munnar\n\tEnter Your Choice--->"))  
                if hotel_choice == 1:
                    price().members(2300)
                if hotel_choice == 2:
                    price().members(8000)
                if hotel_choice == 3:
                    price().members(25000)
        if value1==2:
            click2 =int(input(("\n\t1.Andaman and Nicobar\n\t2.Kochi\n\t3.Mahabalipuram\n\tselect your favourite location---> ")))
            if click2==1:
               hotel_choice = int(input("\n\t1.Taj Exotica Resort\n\t2.Tilar Siro Andamans\n\t3.Barefoot At Havelock\n\tEnter Your Choice--->"))  
               if hotel_choice == 1:
                    price().members(7600)
               if hotel_choice == 2:
                    price().members(9500)
               if hotel_choice == 3:
                    price().members(15000)
            elif click2==2:
                hotel_choice = int(input("\n\t1.Radisson Blu\n\t2.ibis Kochi City Centre\n\t3.Trident Cochin\n\tEnter Your Choice--->"))  
                if hotel_choice == 1:
                    price().members(7560)
                if hotel_choice == 2:
                    price().members(4300)
                if hotel_choice == 3:
                    price().members(5800)
            elif click2==3:
                hotel_choice = int(input("\n\t1.Hotel Mahabs\n\t2.Alice Paradise\n\t3.Srinivasa Residency\n\tEnter Your Choice--->"))  
                if hotel_choice == 1:
                    price().members(1870)
                if hotel_choice == 2:
                    price().members(5400)
                if hotel_choice == 3:
                    price().members(8600)
        if value1==3:
            click3 =int(input("\n\t1.Brahadeshwara Temple\n\t2.Vijayanagar Fort\n\t3.Taj Mahal\n\tselect your favourite location--->"))
            if click3==1:
               hotel_choice = int(input("\n\t1.Savatma\n\t2.Sangam\n\t3.Lotus Hotel\n\tEnter Your Choice--->"))  
               if hotel_choice == 1:
                    price().members(7560)
               if hotel_choice == 2:
                    price().members(5420)
               if hotel_choice == 3:
                    price().members(2690)
            elif click3==2:
               hotel_choice = int(input("\n\t1.Farifield\n\t2.Myspace Dhruva Inn\n\t3.West Fort Hotel\n\tEnter Your Choice--->"))  
               if hotel_choice == 1:
                    price().members(7540)
               if hotel_choice == 2:
                    price().members(9890)
               if hotel_choice == 3:
                    price().members(5640)
            elif click3==3:
                hotel_choice = int(input("\n\t1.Novotel \n\t2.The Park New Delhi\n\t3.Taj Palace\n\tEnter Your Choice--->"))  
                if hotel_choice == 1:
                    price().members(7080)
                if hotel_choice == 2:
                    price().members(9580)
                if hotel_choice == 3:
                    price().members(5790)


            