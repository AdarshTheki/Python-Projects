# A Bike Rental System
class BikeShop:
    def __init__(self,stock):
        self.stock = stock
    def DisplayBike(self):
        print("Total Bikes: ",self.stock)
    def RentalBike(self,q):
        if q<=0:
            print("Enter the positive value or greater than Zero ")
        elif q>self.stock:
            print("Enter the value (less than stock)")
        else:
            self.stock = self.stock-q
            print("Total Price: ",q*100)
            print("Total Bikes: ",self.stock)

while True:
    obj = BikeShop(100)
    uc = int(input('''
1 Display stocks
2 Rent a Bike
3 Exit
    '''))
    if uc==1:
        obj.DisplayBike()
    elif uc==2:
        n = int(input("Enter The Qrt: "))
        obj.RentalBike(n)
    else:
        break