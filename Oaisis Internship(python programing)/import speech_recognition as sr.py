import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Set the speech rate (lower value for slower speed)

output_label=None
def speak(text):
    print(text)
    global output_label # Print the text to the console
    #output_label.configure(text=f"Assistant: {text}")  # Update the label with the assistant's response
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            user_dis.configure(text=f"User: {query}")  # Display the user's query
            return query.lower()
        except Exception as e:
            print("Say that again please...")
            return "None"

def respond_to_greeting():
    speak("Hello! How can I assist you today?")
    output_label.configure(text="Assistant:Hello! How can I assist you today?")

def respond_meme():
    speak("patar se patar marey tho chigari nikalti")

def tell_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    output_label.configure(text=f"Assistant: {current_time}")
    speak(f"The current time is {current_time}")
    

def tell_date():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    output_label.configure(text=f"Assistant: {current_date}")
    speak(f"Today's date is {current_date}")

def search_web(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")
    

def start_assistant():
    while True:
        query = take_command()

        if 'hello' in query:
            respond_to_greeting()
            break
        elif 'rock' in query:
            respond_meme()
        elif 'time' in query:
            tell_time()
            break
        elif 'date' in query:
            tell_date()
            break
        elif 'search' in query:
            speak("What do you want to search for?")
            search_query = take_command()
            search_web(search_query)
            break
        elif 'exit' in query:
            speak("Goodbye!")
            break

def on_start():
    messagebox.showinfo("Voice Assistant", "Voice Assistant is starting...")
    start_assistant()

def on_exit():
    messagebox.showinfo("Voice Assistant", "Voice Assistant is stopping...")
    root.destroy()

# Create the main window
root = ctk.CTk()
root.config(bg="#0a0525")
root.geometry("500x500")

root.title("Voice Assistant")

img1 = ctk.CTkImage(Image.open("C:\\Users\\dilip\\OneDrive\\Desktop\\assistant\\michai11.png"), size=(120,100))

user_dis=ctk.CTkLabel(root,text=" " ,fg_color="#0a0525", bg_color="#0a0525",text_color="white")
user_dis.place(x=100,y=270)
# Create a label to display the assistant's voice output
output_label = ctk.CTkLabel(root, text="User:", fg_color="#0a0525", bg_color="#0a0525",text_color="white",font=("Nothing Font (5x7)", 15, "bold"))
output_label.place(x=100,y=290)

ctk.CTkLabel(root, text="AI VOICE GENERATOR", font=("Nothing Font (5x7)", 15, "bold"),fg_color="#0a0525",bg_color="#0a0525",text_color="white").place(x=160, y=110)

# Create buttons
start_button = ctk.CTkButton(root, text=" ", image=img1, command=on_start, fg_color="#0a0525", bg_color="#0a0525", hover_color="#0a0525")
start_button.place(x=170, y=170)

exit_button = ctk.CTkButton(root, text="Exit", command=on_exit, fg_color="#0a0525", bg_color="#0a0525",font=("Nothing Font (5x7)", 10, "bold"))
exit_button.pack(pady=10)

# Run the GUI loop
root.mainloop()
