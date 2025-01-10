import tkinter as tk
import random
from tkinter import messagebox
import pygame  

def generate_key():
    key = f"{generate_block()}-{generate_block()}-{generate_block()}"
    key_var.set(key)

def generate_block():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    block = random.choices(chars, k=3) + random.choices(digits, k=2)
    random.shuffle(block)
    return ''.join(block)

root = tk.Tk()
root.title("clash")
root.geometry("700x400")

def play_music():
    pygame.mixer.init()  
    pygame.mixer.music.load("mu.mp3")
    pygame.mixer.music.play(-1)


root.after(100, play_music)


background_image = tk.PhotoImage(file="bg.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

key_var = tk.StringVar()
key_entry = tk.Entry(root, textvariable=key_var, font=("Arial", 14), justify="center", state="readonly")
key_entry.place(relx=0.5, rely=0.4, anchor="center", width=300)



generate_button = tk.Button(root, text="Generate Key", font=("Arial", 12), command=generate_key)
generate_button.place(relx=0.5, rely=0.6, anchor="center")

def save_key():
    key = key_var.get()
    with open("generated_key.txt", "w") as file:
        file.write(key)
    messagebox.showinfo("Saved", "Your key has been saved to 'generated_key.txt'.")

save_button = tk.Button(root, text="Save Key", font=("Arial", 12), command=save_key)
save_button.place(relx=0.5, rely=0.7, anchor="center")

def on_enter(event):
    generate_button.config(bg="lightgreen")

def on_leave(event):
    generate_button.config(bg="SystemButtonFace")

generate_button.bind("<Enter>", on_enter)
generate_button.bind("<Leave>", on_leave)


root.mainloop()