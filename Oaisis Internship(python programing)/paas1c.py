import random
import string
import customtkinter as ctk
from PIL import Image
import pyperclip

# Initialize the main window
root = ctk.CTk()
root.config(bg="#0a0525")
root.geometry("700x500")
root.title("Advanced Password Generator")


img1=ctk.CTkImage(Image.open("C:\\Users\\dilip\\OneDrive\\Desktop\\assistant\\pickey.jpg"),size=(700,500))
l2=ctk.CTkLabel(root,image=img1,height=700,width=500,text=" ")
l2.pack()

# headFrm = ctk.CTkFrame(l2, height=500,width=700 ,fg_color="white", bg_color="white")
# headFrm.pack()



def weak_password():
    # Get the length of the desired password from the user input
    lenn = length.get()
    # Define the set of characters to use in the password (lowercase letters)
    characters = string.ascii_lowercase
    password = ''.join(random.choice(characters) for i in range(lenn))
    # Display the generated password in the Tkinter window
    l1.configure(text=password)

def strong_password():
    # Get the length of the desired password from the user input
    lenn = length.get()
    # Define the set of characters to use in the password (letters, numbers, and special symbols)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(lenn))
    # Display the generated password in the Tkinter window
    l1.configure(text=password)
    
def copy_password():
    password = l1.cget("text")
    pyperclip.copy(password)


# Create and place widgets
ctk.CTkLabel(l2, text="PASSWORD GENERATOR", font=("Nothing Font (5x7)", 35, "bold"),fg_color="#FFFFFF").place(x=160, y=20)
ctk.CTkLabel(l2, text="Enter the length", font=("Nothing Font (5x7)", 20, "bold"), bg_color="white",text_color="black",corner_radius=5).place(x=250, y=80)

length = ctk.IntVar()
ctk.CTkEntry(l2, textvariable=length, font=("Lucida", 20, "bold"),height=30,width=120).place(x=280,y=120)

ctk.CTkButton(l2, text="Generate Weak Password", command=weak_password,text_color="white", font=("Lucida", 10, "bold"),fg_color="black",height=35).place(x=150, y=170)
ctk.CTkButton(l2, text="Generate Strong Password", command=strong_password, fg_color="black",text_color="white", font=("Lucida", 10, "bold"),height=35).place(x=350, y=170)

ctk.CTkButton(l2, text="Copy Password", command=copy_password, fg_color="black", text_color="white", font=("Lucida", 10, "bold")).place(x=250, y=270)

l1 = ctk.CTkLabel(l2, text=" ", font=("Nothing Font (5x7)", 13, "bold"), bg_color="black",text_color="white",height=40,width=300)
l1.place(x=170, y=220)

# Run the application
root.mainloop()
