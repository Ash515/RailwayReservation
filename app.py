def main():
    lots={'A':['A1','A2','A3'],'B':['B1','B2','B3']}
    adhaar=[]
    print("Welcome to Railways Reservation System")
    name=input("Enter your name:")
    age=int(input("Enter the age:"))
    adhaar_card=int(input("Enter the Adhaar Card Number:"))
    adhaar.append(adhaar_card)
    members=int(input("How many members?:"))
    amt=members*150        #150 is ticket amount
    slot=input("Enter the class you want:")
    if slot in lots:
        for i in range(len(lots)):
            try:
                reserve=lots[slot][0]
                print("******************************")
                print("Successfully class is booked at",reserve)
                print("Adhaar Number:",adhaar_card)
                print("Total members:",members)
                print("Amount:",amt)
                print("***Happy Journey !!***")
                del lots[slot][0]
            except:
                print("Sorry this class is full try other class")

main()





    


        
