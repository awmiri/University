import csv

class Contact :
    def __init__(self , name , phone):
        self.name = name
        if phone.isdigit() :
            self._phone=phone
        else:
            raise ValueError("value not defend")
    
class PhoneBook :
    def __init__(self):
        self.contacts = [] 

    def addContact(self , name , phone):
        newContact = Contact(name , phone)
        self.contacts.append(newContact)

    def save_to_csv(self , fileName):
        try:
            with open(fileName ,"w" , encoding="utf-8" , newline="") as file :
                writer = csv.writer(file)
                writer.writerow(["name" , "phone"])
                for c in self.contacts:
                    writer.writerow([c.name , c._phone])
                
            print("save successfully :))))))")
        except PermissionError :
            print("cant write on this file")
    
    def load_from_csv(self , fileName):
        try:
            with open(fileName , "r" , encoding="utf-8") as file :
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    try:
                        self.contacts.append(Contact(row[0] , row[1]))
                    except(ValueError , IndexError):
                        print(f"in row {row} for not valid option is ignore")
        except FileNotFoundError:
            print("create the new book")



my_book = PhoneBook()
my_book.load_from_csv("contacts.csv")


while True :
    print("--------- phone book ---------")
    print("1- add pearson")
    print("2- show all ")
    print("3- save and exit ")

    try :
        number = int(input("what do you want to do ??? "))

        if number == 1 :
            name = input("enter your name :")
            phone = input("enter your phone :")
            try:
                my_book.addContact(name , phone)
                print("contact is successfully add")
            except ValueError as e :
                print(f"try again {e}") 
        
        elif number == 2:
            print("your all contact :")
            
            for row in my_book.contacts :
                print(f"name: {row.name}  |||  phone: {row._phone}")
        
        elif number == 3 :
            my_book.save_to_csv("contacts.csv")
            print("goodbye")
            break

        else:
            print("please enter a number between the (1-3)")

    except Exception as e :
        print(f"have error {e}")