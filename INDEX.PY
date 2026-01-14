from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.messagebox
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from time import strftime
from datetime import datetime

class Face_Recognition_System:
    def __init__(self, root):  # Corrected __init__ method
        self.root = root
        self.root.geometry("1530x710+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")

        # FIRST IMAGE
        img = Image.open("C:/Users/ADMIN/Desktop/Mini/image/images.jpeg")
        img = img.resize((400, 150))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=400, height=150)

        # SECOND IMAGE
        img1 = Image.open("C:/Users/ADMIN/Desktop/Mini/image/face.jpeg")
        img1 = img1.resize((200, 150))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=400, y=0, width=200, height=150)

        # THIRD IMAGE
        img31 = Image.open("C:/Users/ADMIN/Desktop/Mini/image/face3.png")
        img31 = img31.resize((200, 150))
        self.photoimg31 = ImageTk.PhotoImage(img31)

        f_lbl = Label(self.root, image=self.photoimg31)
        f_lbl.place(x=600, y=0, width=200, height=150)

        # FOURTH IMAGE
        img2 = Image.open("C:/Users/ADMIN/Desktop/Mini/image/face2.png")
        img2 = img2.resize((200, 150))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=800, y=0, width=200, height=150)

        # FIFTH IMAGE
        img41 = Image.open("C:/Users/ADMIN/Desktop/Mini/image/photo.png")
        img41 = img41.resize((400, 150))
        self.photoimg41 = ImageTk.PhotoImage(img41)

        f_lbl = Label(self.root, image=self.photoimg41)
        f_lbl.place(x=1000, y=0, width=400, height=150)

        # BACKGROUND IMAGE
        img3 = Image.open("C:/Users/ADMIN/Desktop/Mini/image/background.jpg")
        img3 = img3.resize((1530, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=150, width=1530, height=560)

        # Title Label
        title_label = Label(bg_img, text="FACE RECOGNITION SYSTEM IN REAL TIME",
                            font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_label.place(x=0, y=0, width=1530, height=50)

        # STUDENT BUTTON
        img4 = Image.open("C:/Users/ADMIN/Desktop/Mini/image/student.jpeg")
        img4 = img4.resize((170, 170))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=170, height=170)

        b1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2",
                    font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1.place(x=200, y=250, width=170, height=40)

        # DETECT FACE BUTTON
        img5 = Image.open("C:/Users/ADMIN/Desktop/Mini/image/face2.png")
        img5 = img5.resize((170, 170))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.face_data)
        b2.place(x=450, y=100, width=170, height=170)

        b2 = Button(bg_img, text="Face Detector", cursor="hand2",
                    font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b2.place(x=450, y=250, width=170, height=40)

        # ATTENDANCE BUTTON
        img6 = Image.open("C:/Users/ADMIN/Desktop/Mini/image/attendance.webp")
        img6 = img6.resize((170, 170))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.attendance_data)
        b3.place(x=700, y=100, width=170, height=170)

        b3 = Button(bg_img, text="Attendance", cursor="hand2",
                    font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b3.place(x=700, y=250, width=170, height=40)

        # HELP DESK BUTTON
        img7 = Image.open("C:/Users/ADMIN/Desktop/Mini/image/help.webp")
        img7 = img7.resize((170, 170))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b4 = Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.help_data)
        b4.place(x=950, y=100, width=170, height=170)

        b4 = Button(bg_img, text="Help Desk", cursor="hand2",
                    font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b4.place(x=950, y=250, width=170, height=40)

        # TRAIN BUTTON
        img8 = Image.open("C:/Users/ADMIN/Desktop/Mini/image/train.webp")
        img8 = img8.resize((170, 170))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.train_data)
        b5.place(x=200, y=340, width=170, height=170)

        b5 = Button(bg_img, text="Train", cursor="hand2",
                    font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b5.place(x=200, y=470, width=170, height=40)

        # PHOTOS BUTTON
        img9 = Image.open("C:/Users/ADMIN/Desktop/Mini/image/photos.png")
        img9 = img9.resize((170, 170))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.open_photos)
        b6.place(x=450, y=340, width=170, height=170)

        b6 = Button(bg_img, text="Photos", cursor="hand2",
                    font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b6.place(x=450, y=470, width=170, height=40)

        # DEVELOPER BUTTON
        img10 = Image.open("C:/Users/ADMIN/Desktop/Mini/image/developer.jpeg")
        img10 = img10.resize((170, 170))
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b7 = Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.developer_info)
        b7.place(x=700, y=340, width=170, height=170)

        b7 = Button(bg_img, text="Developer", cursor="hand2",
        font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b7.place(x=700, y=470, width=170, height=40)

        # EXIT BUTTON
        img11 = Image.open("C:/Users/ADMIN/Desktop/Mini/image/exit.jpg")
        img11 = img11.resize((170, 170))
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b8 = Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.exit_system)
        b8.place(x=950, y=340, width=170, height=170)

        b8 = Button(bg_img, text="Exit", cursor="hand2",
        font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b8.place(x=950, y=470, width=170, height=40)

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)  

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window) 

    
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

if __name__ == "__main__":
    root = Tk()
    app = Face_Recognition_System(root)
    root.mainloop()
