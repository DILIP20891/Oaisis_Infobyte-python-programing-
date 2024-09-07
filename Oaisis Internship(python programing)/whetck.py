import customtkinter as ctk
from PIL import Image
import requests,json


root=ctk.CTk()
#root.configure("Blue")
root.geometry("700x500")
root.title("Weather App")

def gen_kab():
    apikey="e9f37490e2373810a7c933f9ce3d9f11"
    baseURL="https://api.openweathermap.org/data/2.5/weather?q="
    city=tx.get()
    completeurl=baseURL+city+"&appid="+apikey
    response=requests.get(completeurl)
    data=response.json()
    print(data)
    t1="Current Temperature:=",data["main"]["temp"]
    t2="Humidity:=",data["main"]["humidity"]
    t3="Weather Description:=", data["weather"][0]["main"]
    t4="Description:=",data["weather"][0]["description"]
    l1.configure(text=t1)
    l2.configure(text=t2)
    l3.configure(text=t3)
    l4.configure(text=t4)

    


img1=ctk.CTkImage(Image.open("C:\\Users\\dilip\\OneDrive\\Desktop\\assistant\\skyblue1.jpg"),size=(700,500))
l=ctk.CTkLabel(root,image=img1,height=700,width=500,text=" ")
l.pack()

ctk.CTkLabel(l,text="Weather App☁️",font=("Paytone One", 35, "bold"),fg_color="#ade3ff").place(x=220, y=20)
ctk.CTkLabel(l, text="Enter the City", font=("Nothing Font (5x7)", 20, "bold"), bg_color="#ade3ff",fg_color="#ade3ff",text_color="black").place(x=270, y=80)

ctk.CTkButton(l,text="Generate Weak Password", command=gen_kab,text_color="white", font=("Lucida", 10, "bold"),fg_color="black",height=35).place(x=270, y=170)

tx = ctk.StringVar()
ctk.CTkEntry(l,textvariable=tx,font=("Lucida", 20, "bold"),height=30,width=120,bg_color="#ade3ff").place(x=280,y=120)

l1 = ctk.CTkLabel(l, text="Current Temperature:=", font=("Consolas", 18, "bold"), bg_color="#54a6d1",text_color="black",height=40,width=300)
l1.place(x=170, y=220)
l2 = ctk.CTkLabel(l, text="Humidity:=", font=("Consolas", 18, "bold"), bg_color="#54a6d1",text_color="black",height=40,width=300)
l2.place(x=170, y=260)
l3 = ctk.CTkLabel(l, text="Weather Description:=", font=("Consolas", 18, "bold"), bg_color="#54a6d1",text_color="black",height=40,width=300)
l3.place(x=170, y=300)
l4 = ctk.CTkLabel(l, text="Description:= ", font=("Consolas", 18, "bold"), bg_color="#54a6d1",text_color="black",height=40,width=300)
l4.place(x=170, y=340)


root.mainloop()
