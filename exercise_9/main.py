import tkinter as tk
import logic
from tkinter import messagebox

book = logic.PhoneBook()

def refreshList() :
    listOfContact.delete(0 ,tk.END)
    for contact in book.contacts :
        displayText = f"{contact.name} - {contact._phone} "
        listOfContact.insert(tk.END , displayText)

def addContactBtn():
    name =entryName.get()
    phone =entryPhone.get()
    if not name or not phone:
        messagebox.showinfo("please enter the number or name !!!")
        return
    try:
        book.addContact(name , phone)

        refreshList()

        entryName.delete(0 , tk.END)
        entryPhone.delete(0 , tk.END)
        messagebox.showinfo("Success","add successFully")
    except ValueError as e :
        messagebox.showwarning("Warning",f"warn {e}")

def saveContactBtn ():
    book.save_to_csv("contacts.csv")
    messagebox.showinfo("Saved","save successfully")

def readContactBtn ():
    book.load_from_csv("contacts.csv")
    refreshList()
    messagebox.showwarning("Loaded","read data from file")

def searchValue ():
    searchValue = searchEntry.get().lower()
    listSearch.delete(0 , tk.END)
    for contact in book.contacts :
        if searchValue in contact.name.lower():
            listSearch.insert(tk.END , f"{contact.name} - {contact._phone}")
    
def exitAndSave ():
    book.save_to_csv("contacts.csv")
    messagebox.showinfo("Saved","save successfully")
    if messagebox.askyesno("Confirm Delete" , "are you sure for exit ?"):
        root.destroy()
    
def deleteContact ():
    if messagebox.askyesno("confirm delete" , "are you sure for exit ?"):
        selectedIndex =listOfContact.curselection()
        selectedSearchIndex =listSearch.curselection()

        if not selectedIndex or not selectedSearchIndex :
            messagebox.showwarning("warning" , "please select one people")

        if selectedIndex :
            index = selectedIndex[0]
        else:
            index = selectedSearchIndex[0]
    

        del book.contacts[index]

        listOfContact.delete(index)
        messagebox.showinfo("Deleted", "Contact deleted successfully")

def sortByName():
    book.contacts.sort(key=lambda c: c.name.lower())
    refreshList()

def sortByPhone():
    book.contacts.sort(key=lambda c: c._phone)
    refreshList()


root = tk.Tk()

root.title("phone book")

root.geometry("500x700")
frame_top = tk.Frame(root)
frame_top.pack(pady=10)

tk.Label(frame_top , text="name : ").pack()
entryName = tk.Entry(frame_top)
entryName.pack()

tk.Label(frame_top , text="phone").pack()
entryPhone = tk.Entry(frame_top)
entryPhone.pack()

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

tk.Button(frame_buttons , text="add contact" , command=addContactBtn ,bg="#4181AF", fg="white").pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons , text="save contact" , command=saveContactBtn ,bg="#9CD81B", fg="white").pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons , text="read contact" , command=readContactBtn ,bg="#FF9800", fg="white").pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons , text="delete" , command=deleteContact ,bg="#FF4800", fg="white").pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons , text="sort by name" , command=sortByName ,bg="#857068", fg="white").pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons , text="sort by phone" , command=sortByPhone ,bg="#2E221E", fg="white").pack(side=tk.LEFT, padx=5)

tk.Label(root , text="list of contact").pack()
listOfContact = tk.Listbox(root , width=50 , height=10)
listOfContact.pack()

tk.Label(root, text="search").pack()

search_frame = tk.Frame(root)
search_frame.pack(pady=5)

searchEntry = tk.Entry(search_frame)
searchEntry.pack(side=tk.LEFT, padx=5)

tk.Button(
    search_frame,
    text="Search",
    command=searchValue,
    bg="#B42CDA",
    fg="white"
).pack(side=tk.LEFT)

tk.Label(root , text="list of search").pack()
listSearch = tk.Listbox(root , width=50 , height=5)
listSearch.pack()

tk.Button(root , text="exit" , command=exitAndSave ,bg="#F11212", fg="white").pack(side=tk.LEFT, padx=5)
root.mainloop()