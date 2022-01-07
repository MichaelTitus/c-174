from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import random
root = Tk()
root.title("Joe Mama 69 foods")
root.geometry("1000x700")

burger=ImageTk.PhotoImage(Image.open('burger1.png'))
burger_img_lbl=Label(root,image=burger)
burger_img_lbl.place(relx=0.7,rely=0.5,anchor=CENTER)

Label_heading=Label(root,text="Joe Mama__69 foods",font=("times",25,"bold"),fg="Blue")
Label_heading.place(relx=0.12,rely=0.1,anchor=CENTER)

label_dish=Label(root,text="Select Dish",font=("times",15))
label_dish.place(relx=0.06,rely=0.2,anchor=CENTER)

dish=["burger","ice cream"]
dishdd=ttk.Combobox(root,state="readonly",values=dish)
dishdd.place(relx=0.25,rely=0.2,anchor=CENTER)

label_addons=Label(root,text="Select toppins",font=("times",15))
label_addons.place(relx=0.06,rely=0.5,anchor=CENTER)

topping=[]
toppingsdd=ttk.Combobox(root,state="readonly",values=topping)
toppingsdd.place(relx=0.25,rely=0.5,anchor=CENTER)

dishamnt=Label(root,font=("times",15,"bold"))
dishamnt.place(relx=0.2,rely=0.75,anchor=CENTER)

class parent():
    
    def __init__(self):
        print("This is parent class")
        
    def menu(dish):
        #using if, add a conditon for "burger", print a message with toppings cheese and jalapeno
        if dish=="Burger":
            print("You can add following toppins")
            print("Cheese or Jalepeno")
            topping=["Cheese", "Jalepeno"]
            toppingsdd["values"]=topping
            
        #using elif, add a conditon for "ice-cream", print a message with flavors chocolate and caramel
        elif dish=="Ice cream":
            print("You can add following toppins")
            print("Vanilla and Chocolate")
            topping=["Vanilla", "Chocolate"]
            toppingsdd["values"]=topping
        else:
            print("please enter a valid dish")
            
    #pass the variable dish, add_ons for the function        
    def final_amount(dish,add_ons):
        #add condition for dish=="burger" and add_ons=="cheese", then print 250 USD
        if dish=="Burger" and add_ons=="Cheese":
            dishamnt["text"]="You ned to pay $13.99"
        #add elif condition for dish=="burger" and add_ons=="jalepeeno", then print 350 USD
        elif dish=="Burger" and add_ons=="Jalepeno":
            dishamnt["text"]="You need to pay $14.99"
        #add elif condition for dish=="iced_americano" and add_ons=="chocolate", then print 250 USD
        elif dish=="Ice cream" and add_ons=="Vannila":
            dishamnt["text"]="You need to pay $4.99"
         #add elif condition for dish=="iced_americano" and add_ons=="caramel", then print 450 USD
        elif dish=="Ice cream" and add_ons=="Chocolate":
            dishamnt["text"]="You need to pay $3.99"


#make the child class inherit parent class 
class child1(parent):
    #create init function, pass self, dish into it
    def __init__(self,dish):
        #assign the value dish to self.new_dish
        self.new_dish = dish
        
    def  get_menu(self):
        newdish=dishdd.get()
        parent.menu(newdish)
    #call the function menu from the parent, pass new_dish into it
        
        
class child2(parent):
    #create init function, pass self, dish, addons into it
    def __init__(self,dish,add_ons):
        self.new_dish=dish
        self.new_toppings=add_ons
        #assign the value dish to self.new_dish and addons to self.addons
        
   
        
    def get_final_amount(self):
        newdish=dishdd.get()
        topping=toppingsdd.get()
        #call the function final_amount from parent class, and pass self.new_dish and self.addons
        parent.final_amount(newdish,topping)
#create an object for the class child1, pass any food as value in it. ex "burger" or "iced_americano"       
Child1=child1(dishdd.get())
#call the function get_menu() of the child1 object
Child1.get_menu()


#create an object for the class child2, pass any food as value in it. ex "burger" or "iced_americano"  
Child2=child2(dishdd.get(),toppingsdd.get())
# and also the toppings of the respective food
Child2.get_final_amount()

#call the function get_final_amount for the object child2

button_addon=Button(root,text="Check toppings",command=Child1.get_menu,bg="Blue",fg="White")
button_addon.place(relx=0.06,rely=0.3,anchor=CENTER)
  
button_amount=Button(root,text="Get Amount",command=Child2.get_final_amount(),bg="Blue",fg="White")
button_amount.place(relx=0.06,rely=0.6,anchor=CENTER)      
        
#create object for child2 and 3        
root.mainloop()