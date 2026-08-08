import sys
import random 
import mysql.connector as sql

con=sql.connect(host="Your_host_name",user="your_user_name",password="your_password")


try:
    if con.is_connected()==True:
        print("CONNECTED SUCCESSFULLY\n\n")

except:
    print(" Connection Error/n")
    
    
def create():  
    cursor=con.cursor()
    
    cursor.execute("create database if not exists CDS")
    
    cursor.execute("use CDS")
    
    cursor.execute("create table if not exists ACD(CID varchar(50) primary key,Car_Model varchar(50),\
Mileage varchar(25),Price varchar(11),Engine varchar(50),Seater int,Type varchar(25))")
    
    cursor.execute("select * from ACD")
    r=cursor.fetchall()
    c=0
    for a in r:
        c+=1
    if c==0:
        cursor.execute(
            "insert into ACD values "
            "('C01', 'Hyundai Creta', '17.4', '1199000', '1497', 5, 'SUV'),"
            "('C02', 'Toyota Fortuner', '14.4', '3564000', '2755', 7, 'SUV'),"
            "('C03', 'Honda City', '18.4', '1199900', '1498', 5, 'Sedan'),"
            "('C04', 'Skoda Slavia', '19.1', '1299000', '999', 5, 'Sedan'),"
            "('C05', 'Maruti Suzuki Swift', '22.4', '649000', '1197', 5, 'Hatchback'),"
            "('C06', 'Tata Altroz', '20.3', '699000', '1199', 5, 'Hatchback'),"
            "('C07', 'Maruti Suzuki Ertiga', '20.6', '899000', '1462', 7, 'MUV/MPV'),"
            "('C08', 'Kia Carens', '19.5', '1099000', '1497', 6, 'MUV/MPV'),"
            "('C09', 'BMW Z4', '11.0', '6890000', '1998', 2, 'Luxury/Convertible'),"
            "('C10', 'Mercedes-Benz E-Class', '12.5', '7850000', '1991', 5, 'Luxury/Convertible')"
        )
        
                   
    cursor.execute("create table if not exists Customer(customer_id varchar(10) primary key,\
Name varchar(50),Mobile_no BIGINT ,address varchar(50),Email_id  varchar(50))")
                   
    cursor.execute("create table if not exists CP(customer_id varchar(10),foreign key(customer_id)\
references Customer(customer_id),CID varchar(50),foreign key(CID) references ACD(CID),MOP varchar(10))")
                                                 
    
    con.commit()
                   

def registration():
    
    cursor=con.cursor()
    
    print()
    print(" "*49,'*'*14,'\n', " "*49 , 'REGISTRATION' ,'\n'," "*48,'*'*14,'\n')
    
    s=input("enter whether you are old or new customer:")
    if s=="new":   
        x0=random.randint(1,100)
        x7=str(x0)
        xcid="c"+x7+"ID"
        x1=input("enter customer name: ")
        x2=int(input("enter customer mobile no. : "))
        x3=input("enter customer address: ")
        x4=input("enter customer email_id: ")
        x5=input("enter car ID: ")
        x6=input("enter mode of payment(cash/loan/EMI): ")
        
        cursor.execute("insert into Customer values('{}','{}',{},'{}','{}')".format(xcid,x1,x2,x3,x4))
        cursor.execute("select car_model from ACD where CID='{}'".format(x5))
        rec=cursor.fetchall()
        if not rec:
            print("Invalid car ID.")
            return
        cursor.execute("insert into CP values('{}','{}','{}')".format(xcid,x5,x6))
        con.commit()
        print("Your payment is successful,THANKS FOR PURCHASING FROM OUR STORE ")
        print()
        print("Your customer id is:",xcid,"{This id will also act as your 'PASS' for accessing your details}")
    elif s=="old":      
        cid=input("customer id:")
        nc=input("enter the car ID of the new car you want to purchase:")
        mp=input("enter the mode of payement(cash/loan/EMI):")
        cursor.execute("select car_model from ACD where CID='{}'".format(nc))
        rec=cursor.fetchall()
        if not rec:
            print("Invalid car ID.")
            return
        cursor.execute("insert into CP values('{}','{}','{}')".format(cid,nc,mp))
        con.commit()
           
        
    print('*'*117)
    print("Pick your choice: \n 1.Available car details \n 2.customer details \n 3.HOME \n 4.exit ")
    c=int(input("enter your choice: "))
    if c==1:
        Avail_car_details()
    elif c==2:
        customer_details()
    elif c==3:
        mainmenu()
    elif c==4:
        sys.exit()
    
        

def Avail_car_details():
    
    cursor=con.cursor()
    
    print(" "*45,'*'*22,'\n', " "*48, 'AVAILABLE CARS' ,'\n'," "*44,'*'*22,'\n')
    
    print("Types of Car Avaiable: \n1.SUV \n2.Sedan \n3.Hatchback \n4.MUV/MPV \n5.Luxury/Convertible \n6.All\n\n") 
    ch=int(input("enter the Type of Car you are looking for(enter the numeric value):"))
    print()
    print("CAR_ID  |  MODEL  |  MILEAGE(KM/L)  |  PRICE  |  ENGINE  |  SEATER  |  TYPE  ")
    print()
    cursor.execute("select * from ACD")
    rec1=cursor.fetchall()
    for a in rec1:
        if ch==1 and a[-1]=="SUV":
            print(a)
        elif ch==2 and a[-1]=="Sedan":
            print(a)
        elif ch==3 and a[-1]=="Hatchback":
            print(a)
        elif ch==4 and a[-1]=="MUV/MPV":
            print(a)
        elif ch==5 and a[-1]=="Luxury/Convertible":
            print(a)
        elif ch==6:
            print(a)
    


        
    print("*"*117)
    print()
    print("Pick your choice: \n 1.Registration \n 2.customer details \n 3.HOME \n 4.exit ")
    c=int(input("enter your choice: "))
    if c==1:
        registration()
    elif c==2:
        customer_details()
    elif c==3:
        mainmenu()
    elif c==4:
        sys.exit()
    print()


        

def customer_details():         
    create()
    cursor=con.cursor()
    flag=0
    print()
    print(" "*46,'*'*24,'\n', " "*49 , 'CUSTOMER DETAILS' ,'\n'," "*45,'*'*24,'\n')
    x=input("customer id[PASS]:")
    
    cursor.execute("select * from customer")
    rec3=cursor.fetchall()
    for b in rec3:
        if x==b[0]:
            flag+=1
    if flag==0:
        print("Your ID is wrong or your Data does not exits in our database ")
    elif flag==1:
        cursor.execute("select * from CP where customer_id='{}'".format(x))
        rec2=cursor.fetchall()
        for a in rec2:
            print(a)
        z=input("do you want to see your other details/personal details also Y/N:")
        if z.lower() == "y":
            cursor.execute("select * from Customer where customer_id='{}'".format(x))
            rec3=cursor.fetchall()
            for b in rec3:
                print(b)
                    
       
            
   
            
        
    print("*"*117)
    print("Pick your choice: \n 1.Available car details \n 2.registration \n 3.HOME \n 4.exit ")
    c=int(input("enter your choice: "))
    if c==1:
        Avail_car_details()
    elif c==2:
        registration()
    elif c==3:
        mainmenu()
    elif c==4:
        sys.exit()
    print()

    

def mainmenu():    
    create()
    print('*'*117,'\n\n', " "*52 , 'TEMPEST CAR DEALERSHIP' ,'\n\n', '*'*116,'\n')
    ans="y"
    while(ans=="y"):
        print("Pick your choice: \n 1.Available car details \n 2.customer details \n 3.Registration \n 4.exit")
        c=int(input("enter your choice: "))
        if c==1:
            Avail_car_details()
        elif c==2:
            customer_details()
        elif c==3:
            registration()
        elif c==4:
            sys.exit()
            
mainmenu()  
con.close()    
