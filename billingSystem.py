myorders = []
sum =0
#details of ferm
print("Welcome to our store")
print("Chitkara Fashion Arena")
print("Rajpura,Punjab")
print("GSTIN:22AAAAA0000A1Z5") 
print(" ")
print("") 

def shop(sum):
     dict={'jeans':5000,'hoodies':1000,'tie':400,'trouser':900,'tuxedo':10000,'bow':300,'blazer':6000,'windcheater':3000}
     print(list(dict.keys()))
     True

#       inventory
     while True:
         print("jeans(5000rs)")
         print("hoodies(1000)")
         print("tie(400)")
         print("trouser(900)")
         print("tuxedo(10000)")
         print("bow(300)")
         print("blazer(6000)")
         print("windcheater(3000)")
         order = input("type what you wanna buy: ")
         if order =="E":
            break
#          quantity
#          discount
         else:
             if order in dict.keys():
                 quantity = int(input("How much do you want: "))
                #  d=int(input("discount given :"))
                 oneItem = f"order: {order}, quantity: {quantity} "
                 myorders.append(oneItem)
                 sum=sum+quantity*(dict[order])

             else:
                 print("please enter right item.⚠️ ")
     return sum
sum = shop(sum)
print(myorders)
print("your total bill is ",sum)
print("Do you wanna add more item. press: yes otherwise no")
opinion = input()
