class Book:
    def __init__(self , title , author , price):
        self.title = title
        self.author = author
        self.price = price
    def apply_discount(self ,discount):
        if discount >100 or discount<0 :
            return print("discount number have to been between 0-100 ")
        discountMount = self.price * (discount/100)
        self.price -= discountMount
        
    def display_details(self):
        print(f"\n--- book Information before ---")
        print(f' book {self.title} was written by {self.author} and the price before off is ${self.price}')

createBook1 = Book("شازده کوچولو" , "آنتوان دو سنت اگزوپری" , 250)
createBook2 = Book("1984" , "جورج اورول" , 550)

print(" our content before add discount")
createBook1.display_details()
createBook2.display_details()
print(" Book1 content after add discount")
createBook1.apply_discount(10)
print(" Book2 content after add discount")
createBook2.apply_discount(50)


print(" show books after discount")
createBook1.display_details()
createBook2.display_details()