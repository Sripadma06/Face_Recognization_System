import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Function to open the second page (another window)
def open_home_page():
    root.withdraw()  # Hide the login window
    home_page = tk.Toplevel(root)
    home_page.title("Home Page")
    home_page.geometry("1530x710")

    label_welcome = tk.Label(home_page, text="Welcome to the Home Page!", font=("Arial", 24))
    label_welcome.pack(pady=250)

    button_quit = tk.Button(home_page, text="Logout", font=("Arial", 14), command=lambda: close_home_page(home_page))
    button_quit.pack(pady=120)

def close_home_page(home_page):
    home_page.destroy()
    root.deiconify()  # Show login window again

# Function to validate login credentials
def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "password":
        messagebox.showinfo("Login Success", "Welcome!")
        open_home_page()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to dynamically resize the background image
def resize_bg(event):
    new_width = event.width
    new_height = event.height
    bg_image_resized = bg_image.resize((new_width, new_height))
    bg_photo_resized = ImageTk.PhotoImage(bg_image_resized)
    bg_label.config(image=bg_photo_resized)
    bg_label.image = bg_photo_resized

# Initialize the main window
root = tk.Tk()
root.title("Login Page")
root.geometry("1530x710")

# Load background image
bg_image = Image.open("C:/Users/ADMIN/Desktop/Mini/image/face2.png")
bg_image_resized = bg_image.resize((1530, 710))
bg_photo = ImageTk.PhotoImage(bg_image_resized)

# Create a label for the background image and place it
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Bind the resize event to dynamically resize the background
root.bind("<Configure>", resize_bg)

# Create a frame to hold the login widgets and place it in the center
center_frame = tk.Frame(root, bg='aqua', bd=5)
center_frame.place(relx=0.5, rely=0.5, anchor="center")

# Username Label and Entry
label_username = tk.Label(center_frame, text="Username:", bg='aqua', font=("Arial", 14))
label_username.pack(pady=10)
entry_username = tk.Entry(center_frame, font=("Arial", 14))
entry_username.pack(pady=5)

# Password Label and Entry
label_password = tk.Label(center_frame, text="Password:", bg='aqua', font=("Arial", 14))
label_password.pack(pady=10)
entry_password = tk.Entry(center_frame, show="*", font=("Arial", 14))
entry_password.pack(pady=5)

# Login Button
button_login = tk.Button(center_frame, text="Login", font=("Arial", 14), command=login)
button_login.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
