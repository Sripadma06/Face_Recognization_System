from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

conn = mysql.connector.connect(host="localhost", username="root", password="Rani@2668", database="mini")

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1300, height=45)

        # 1st image
        img_top = Image.open("C:/Users/ADMIN/Desktop/Mini/image/fa4.jpg")
        img_top = img_top.resize((650, 600), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=600)

        # 2nd image
        img_bottom = Image.open("C:/Users/ADMIN/Desktop/Mini/image/fa4.jpg")
        img_bottom = img_bottom.resize((650, 600), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=500, y=55, width=650, height=600)

        # button
        b1_1 = Button(f_lbl, text="Face Recognition", cursor="hand2", command=self.face_recog, font=("times new roman", 18, "bold"), bg="green", fg="white")
        b1_1.place(x=200, y=550, width=200, height=30)

    # attendance
    def mark_attendance(self, i, r, n, d):
        with open("Gouri.csv", "w+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])
            if i not in name_list and r not in name_list and n not in name_list and d not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    # face recognition
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Rani@2668", database="mini")
                my_cursor = conn.cursor()

                # Fetch Name
                my_cursor.execute("SELECT Name FROM student WHERE StudentId=" + str(id))
                n = my_cursor.fetchone()
                n = str(n[0]) if n is not None else "Unknown"  # Add check for None

                # Fetch Roll
                my_cursor.execute("SELECT Roll FROM student WHERE StudentId=" + str(id))
                r = my_cursor.fetchone()
                r = str(r[0]) if r is not None else "Unknown"  # Add check for None

                # Fetch Department
                my_cursor.execute("SELECT Dep FROM student WHERE StudentId=" + str(id))
                d = my_cursor.fetchone()
                d = str(d[0]) if d is not None else "Unknown"  # Add check for None

                # Fetch Student ID
                my_cursor.execute("SELECT StudentID FROM student WHERE StudentId=" + str(id))
                i = my_cursor.fetchone()
                i = str(i[0]) if i is not None else "Unknown"  # Add check for None

                if confidence > 77:
                    cv2.putText(img, f"ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255), 3)
                    cv2.putText(img, f"Dep:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255), 3)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("Classifier.xml")

        video_cap = cv2.VideoCapture(0)

        try:
            while True:
                ret, img = video_cap.read()
                if not ret:
                    print("Failed to grab frame")
                    break

                img = recognize(img, clf, faceCascade)
                cv2.imshow("Welcome to face recognition", img)

                if cv2.waitKey(1) == 27:  # Press 'Esc' key to exit
                    break
        finally:
            video_cap.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
