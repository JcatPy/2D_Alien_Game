import os
import csv

def newCustomer():
    print("Add a new Customer Record")
    print("=========================")
    f = open('hotel.csv', 'a', newline='\r\n')
    s = csv.writer(f)
    Customerid = input('Enter Customer id: ')
    Customername = input('Enter Customer name: ')
    roomno = input('Enter Room No: ')
    price = float(input('Enter price: '))
    persons = float(input('Enter number of persons: '))
    print("----------------------------------------------------")
    rec = [Customerid, Customername, roomno, price, persons]
    s.writerow(rec)
    f.close()
    print("Customer Record Saved")
    input("Press any key to continue..")

def editCustomer():
    print("Modify a Customer Record")
    print("=========================")
    f = open('hotel.csv', 'r', newline='\r\n')
    f1 = open('temp.csv', 'w', newline='\r\n')
    s = csv.reader(f)
    s1 = csv.writer(f1)
    r = input('Enter Customerid whose record you want to modify: ')
    for rec in s:
        if rec[0] == r:
            print("-------------------------------")
            print("Customer id= ", rec[0])
            print("Customer Name= ", rec[1])
            print("Room No= ", rec[2])
            print("Price= ", rec[3])
            print("Number of persons= ", rec[4])
            print("-------------------------------")

            choice = input("Do you want to modify this Customer Record (y/n): ")
            if choice.lower() == 'y':
                print("----------------------------------------------------")
                Customerid = input('Enter new Customer id (if required): ')
                Customername = input('Enter new Customer name (if required): ')
                roomno = input('Enter new Room No: ')
                price = float(input('Enter price: '))
                persons = float(input('Enter number of persons: '))
                print("----------------------------------------------------")
                rec = [Customerid, Customername, roomno, price, persons]
                s1.writerow(rec)
                print("Customer Record Modified")
            else:
                s1.writerow(rec)
        else:
            s1.writerow(rec)
    f.close()
    f1.close()
    os.remove("hotel.csv")
    os.rename("temp.csv", "hotel.csv")
    input("Press any key to continue..")

def delCustomer():
    f = open('hotel.csv', 'r', newline='\r\n')
    f1 = open('temp.csv', 'w', newline='\r\n')
    s = csv.reader(f)
    s1 = csv.writer(f1)
    r = input('Enter Customerid whose record you want to delete: ')
    for rec in s:
        if rec[0] == r:
            print("-------------------------------")
            print("Customer id= ", rec[0])
            print("Customer Name= ", rec[1])
            print("Room No= ", rec[2])
            print("Price= ", rec[3])
            print("Number of persons= ", rec[4])
            print("-------------------------------")
            choice = input("Do you want to delete this Customer Record (y/n): ")
            if choice.lower() == 'y':
                pass
                print("Customer Record Deleted....")
            else:
                s1.writerow(rec)
        else:
            s1.writerow(rec)
    f.close()
    f1.close()
    os.remove("hotel.csv")
    os.rename("temp.csv", "hotel.csv")
    input("Press any key to continue..")

def searchCustomer():
    print("Search a Customer Record")
    print("=====================")
    f = open('hotel.csv', 'r', newline='\r\n')  # Remove new line character from output
    r = input('Enter Customerid you want to search: ')
    s = csv.reader(f)
    customer_found = False
    for rec in s:
        if rec[0] == r:
            print("-------------------------------")
            print("Customer id=", rec[0])
            print("Customer Name=", rec[1])
            print("Room No=", rec[2])
            print("Price=", rec[3])
            print("Number of persons=", rec[4])
            print("-------------------------------")
            customer_found = True

    if not customer_found:
        print("Customer not found.")
        
    f.close()
    input("Press any key to continue..")

def listofcustomers():
    print("=====================================================================")
    print("                 List of All Customers")
    print("=====================================================================")
    f = open('hotel.csv', 'r', newline='\r\n')
    s = csv.reader(f)
    for rec in s:
        print(rec[0], end="\t\t")
        print(rec[1], end="\t\t")
        print(rec[2], end="\t\t")
        print(rec[3], end="\t\t")
        print(rec[4])
    f.close()
    input("Press any key to continue..")

def menu():
    choice = 0
    while choice != 6:
        print("\n")
        print("| Hotel Management System |")
        print('\n')
        print("          Menu")
        print("1. Add a new Customer Record")
        print("2. Modify Existing Customer ")
        print("3. Delete Existing Customer ")
        print("4. Search a Customer")
        print("5. List all Customers")
        print("6. Exit")

        choice = int(input('Enter your choice: '))
        if choice == 1:
            newCustomer()
        elif choice == 2:
            editCustomer()
        elif choice == 3:
            delCustomer()
        elif choice == 4:
            searchCustomer()
        elif choice == 5:
            listofcustomers()
        elif choice == 6:
            print("Software Exited..")
            break

menu()
