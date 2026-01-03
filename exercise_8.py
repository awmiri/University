import tkinter as tk
from tkinter import messagebox
def submit_form():
    try:
        totalBill = float(entryBill.get()) 
        cuntPeople = float(entryPerson.get()) 
        if totalBill == "" or cuntPeople == "":
            raise ValueError("لطفاً هر دو فیلد را پر کنید!")
        
        if cuntPeople ==0 :
            raise ValueError("people have to be more than  0")
        
        sharePerPerson = totalBill/cuntPeople
        messagebox.showinfo("نتیجه محاسبه",f"سهم هر نفر: {sharePerPerson:.2f} تومان")
    except ValueError as e : 
        messagebox.showerror(f"warn {e}")
root = tk.Tk()

root.title("calc dong")
root.geometry("400x150")

# price
labelBillTotal = tk.Label(root , text="enter the full price : ")
labelBillTotal.pack()
entryBill = tk.Entry(root)
entryBill.pack()

# person
labelCountPerson = tk.Label(root , text="enter how many are you? ")
labelCountPerson.pack()
entryPerson = tk.Entry(root)
entryPerson.pack()

# calc btn

calcBtn = tk.Button(root , text="calculate" , command=submit_form)
calcBtn.pack()


root.mainloop()
print("end pj")