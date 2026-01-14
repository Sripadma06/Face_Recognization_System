from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

conn=mysql.connector.connect(host="localhost",username="root",password="Rani@2668",database="mini")

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #variables
        self.var_dep=StringVar()
        self.var_cousre=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_StudentID=StringVar()
        self.var_StudentName=StringVar()
        self.var_Class_div=StringVar()
        self.var_Roll_Number=StringVar()
        self.var_Gender=StringVar()
        self.var_DOB=StringVar()
        self.var_Phone_No=StringVar()
        self.var_Address=StringVar()
        self.var_radio1=StringVar()
        

        #first img
        img1=Image.open("C:/Users/ADMIN/Desktop/Mini/image/face.jpeg")
        img1=img1.resize((400,100),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=400,height=100)

        #second img
        img2=Image.open("C:/Users/ADMIN/Desktop/Mini/image/face2.png")
        img2=img2.resize((200,100),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=400,y=0,width=200,height=100)

        #third img
        img3=Image.open("C:/Users/ADMIN/Desktop/Mini/image/face3.png")
        img3=img3.resize((200,100),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=600,y=0,width=200,height=100)
        
        #FOUR img
        img99=Image.open("C:/Users/ADMIN/Desktop/Mini/image/face3.png")
        img99=img99.resize((200,100),Image.Resampling.LANCZOS)
        self.photoimg99=ImageTk.PhotoImage(img99)

        f_lbl=Label(self.root,image=self.photoimg99)
        f_lbl.place(x=800,y=0,width=200,height=100)

        #FIVE img
        img98=Image.open("C:/Users/ADMIN/Desktop/Mini/image/face3.png")
        img98=img98.resize((200,100),Image.Resampling.LANCZOS)
        self.photoimg98=ImageTk.PhotoImage(img98)

        f_lbl=Label(self.root,image=self.photoimg98)
        f_lbl.place(x=800,y=0,width=200,height=100)

        #background_img
        img4=Image.open("C:/Users/ADMIN/Desktop/Mini/image/inside.jpg")
        img4=img4.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=30)

        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=40,width=1500,height=600)
        
        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        Left_frame.place(x=4,y=9,width=660,height=600)
        
        img_left = Image.open("C:/Users/ADMIN/Desktop/Mini/image/photos.png")
        img_left = img_left.resize((600, 130),Image.Resampling.LANCZOS)  # Resizing to 600x150
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=600, height=130)

        #current course
        Current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        Current_course_frame.place(x=5,y=135,width=720,height=150)

        #Department
        dep_label=Label(Current_course_frame,text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10)
        
        dep_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=17)
        dep_combo["values"]=("Select Department","CS","ISE","CIVIL","MECH")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #course
        course_label=Label(Current_course_frame,text="Course",font=("times new roman",12,"bold"))
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_cousre,font=("times new roman",12,"bold"),state="readonly",width=17)
        course_combo["values"]=("Select Course","OS","DBMS","EEE","BIO")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #YEAR
        year_label=Label(Current_course_frame,text="Year",font=("times new roman",12,"bold"))
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=17)
        year_combo["values"]=("Select Year","2020-24","2021-25","2022-26","2023-27")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #semester
        semester_label=Label(Current_course_frame,text="Semester",font=("times new roman",12,"bold"))
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        semester_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=17)
        semester_combo["values"]=("Select semester","1sem","2sem","3sem","4sem","5sem","6sem","7sem","finally graduating")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #Class Student information
        Class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
        Class_Student_frame.place(x=5,y=250,width=720,height=300)
        
        #student ID
        StudentID_label=Label(Class_Student_frame,text="StudentID",font=("times new roman",12,"bold"))
        StudentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        StudentID_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_StudentID,width=20,font=("times new roman",12,"bold"))
        StudentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #student NAME
        StudentName_label=Label(Class_Student_frame,text="StudentName",font=("times new roman",12,"bold"))
        StudentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        StudentName_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_StudentName,width=20,font=("times new roman",12,"bold"))
        StudentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #CLASS DIV
        Class_div_label=Label(Class_Student_frame,text="Class Division",font=("times new roman",12,"bold"),bg="white")
        Class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        # Class_div_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_Class_div,width=20,font=("times new roman",12,"bold"))
        # Class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        Class_div_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_Class_div,font=("times new roman",12,"bold"),state="readonly",width=17)
        Class_div_combo["values"]=("A","B","C")
        Class_div_combo.current(0)
        Class_div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll Number
        Roll_Number_label=Label(Class_Student_frame,text="Roll No",font=("times new roman",12,"bold"))
        Roll_Number_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        Roll_Number_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_Roll_Number,width=20,font=("times new roman",12,"bold"))
        Roll_Number_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #GENDER
        Gender_label=Label(Class_Student_frame,text="GENDER",font=("times new roman",12,"bold"))
        Gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        # Gender_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_Gender,width=20,font=("times new roman",12,"bold"))
        # Gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        Gender_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_Gender,font=("times new roman",12,"bold"),state="read only",width=17)
        Gender_combo["values"]=("Male","Female","Other")
        Gender_combo.current(0)
        Gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        #DOB
        DOB_label=Label(Class_Student_frame,text="DOB",font=("times new roman",12,"bold"))
        DOB_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        DOB_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_DOB,width=20,font=("times new roman",12,"bold"))
        DOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #Phone No
        Phone_No_label=Label(Class_Student_frame,text="Phone No",font=("times new roman",12,"bold"))
        Phone_No_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        Phone_No_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_Phone_No,width=20,font=("times new roman",12,"bold"))
        Phone_No_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        #Address
        Address_label=Label(Class_Student_frame,text="Address",font=("times new roman",12,"bold"))
        Address_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        Address_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_Address,width=20,font=("times new roman",12,"bold"))
        Address_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        #radio button
        self.var_radio1=StringVar()
        Radio_Button1=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="Take Photo",value="YES")
        Radio_Button1.grid(row=6,column=0)
        
        Radio_Button2=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="NO Photo",value="NO")
        Radio_Button2.grid(row=6,column=1)
        
        #button frame
        btn_frame=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=160,width=715,height=35)
        
        save_button=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="green",fg="white")
        save_button.grid(row=0,column=0)
        
        update_button=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="green",fg="white")
        update_button.grid(row=0,column=1)
        
        delete_button=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="green",fg="white")
        delete_button.grid(row=0,column=2)
        
        reset_button=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="green",fg="white")
        reset_button.grid(row=0,column=3)

        btn_frame1=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=200,width=715,height=35)
        
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take photo sample",width=35,font=("times new roman",13,"bold"),bg="green",fg="white")
        take_photo_btn.grid(row=0,column=0)
        
        update_photo_btn=Button(btn_frame1,text="Update photo sample",width=35,font=("times new roman",13,"bold"),bg="green",fg="white")
        update_photo_btn.grid(row=0,column=1)
        

        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

        img_right = Image.open("C:/Users/ADMIN/Desktop/Mini/image/GROUP2.jpg")
        img_right = img_right.resize((720, 130),Image.Resampling.LANCZOS)  # Resizing to 600x150
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        
        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=720, height=130)
        
        #search 
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=130,width=620,height=70)
        
        search_label=Label(Search_frame,text="Search By",font=("times new roman",12,"bold"),bg="orange")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select ","StudentID","Student Name","Phone_No","Class Division","Roll No","Gender","Address",)
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        search_entry=ttk.Entry(Search_frame,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        search_button=Button(Search_frame,text="Search",width=8,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_button.grid(row=0,column=3,padx=3)
        
        showAll_button=Button(Search_frame,text="Show All",width=8,font=("times new roman",13,"bold"),bg="aqua",fg="blue")
        showAll_button.grid(row=0,column=4,padx=3)

        #table frame
        table_frame=Frame(Right_frame,bd=4,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("Dep","Course","Year","Sem","ID","Name","Div","Roll","Gender","Dob","Phone_No","Address","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("ID",text="ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Div",text="Division")
        self.student_table.heading("Roll",text="Roll")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Dob",text="DOB")
        self.student_table.heading("Phone_No",text="Phone_No")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Photo",text="PhotoSample")
        self.student_table["show"]="headings"

        self.student_table.column("Dep",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Div",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Dob",width=100)
        self.student_table.column("Phone_No",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Photo",width=150)
        
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #function declaration
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_StudentName.get()=="" or self.var_StudentID.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Rani@2668",database="mini")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                        self.var_dep.get(),
                                                                                                        self.var_cousre.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_StudentID.get(),
                                                                                                        self.var_StudentName.get(),
                                                                                                        self.var_Class_div.get(),
                                                                                                        self.var_Roll_Number.get(),
                                                                                                        self.var_Gender.get(),
                                                                                                        self.var_DOB.get(),
                                                                                                        self.var_Phone_No.get(),
                                                                                                        self.var_Address.get(),
                                                                                                        self.var_radio1.get()

                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Rani@2668",database="mini")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()    

    #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_cousre.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_StudentID.set(data[4]),
        self.var_StudentName.set(data[5]),
        self.var_Class_div.set(data[6]),
        self.var_Roll_Number.set(data[7]),
        self.var_Gender.set(data[8]),
        self.var_DOB.set(data[9]),     
        self.var_Phone_No.set(data[10]),
        self.var_Address.set(data[11]),
        self.var_radio1.set(data[12])
        

    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Deparment" or self.var_StudentName.get()=="" or self.var_StudentID.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Rani@2668",database="mini")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Class_div=%s,Roll=%s,Gender=%s,DOB=%s,Phone_No=%s,Address=%s,Photo=%s where StudentId=%s",(
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_cousre.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_StudentName.get(),
                                                                                                        self.var_Class_div.get(),
                                                                                                        self.var_Roll_Number.get(),
                                                                                                        self.var_Gender.get(),
                                                                                                        self.var_DOB.get(),
                                                                                                        self.var_Phone_No.get(),
                                                                                                        self.var_Address.get(),
                                                                                                        self.var_radio1.get(),
                                                                                                        self.var_StudentID.get()
        
                    ))

                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)        

    #delete function
    def delete_data(self):
        if self.var_StudentID.get()=="":
            messagebox.showerror("Error","Student Id required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete page","Do you want to delete this student details?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Rani@2668",database="mini")
                    my_cursor=conn.cursor()
                    sql="delete from student where StudentID=%s"
                    val=(self.var_StudentID.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted this student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)            


    #reset function
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_cousre.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_StudentID.set(""),
        self.var_StudentName.set(""),
        self.var_Class_div.set("Select Divison"),
        self.var_Roll_Number.set(""),
        self.var_Gender.set("Male"),
        self.var_DOB.set(""),     
        self.var_Phone_No.set(""),
        self.var_Address.set(""),
        self.var_radio1.set("")

    #Generate data set or Take photo samples
    def generate_dataset(self):
        if self.var_dep.get()=="Select Deparment" or self.var_StudentName.get()=="" or self.var_StudentID.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Rani@2668",database="mini")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("Update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Class_div=%s,Roll=%s,Gender=%s,DOB=%s,Phone_No=%s,Address=%s,Photo=%s where StudentId=%s",(
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_cousre.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_StudentName.get(),
                                                                                                        self.var_Class_div.get(),
                                                                                                        self.var_Roll_Number.get(),
                                                                                                        self.var_Gender.get(),
                                                                                                        self.var_DOB.get(),
                                                                                                        self.var_Phone_No.get(),
                                                                                                        self.var_Address.get(),
                                                                                                        self.var_radio1.get(),
                                                                                                        self.var_StudentID.get()==id+1
                ))    
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #load predefined data on face frontals from opencv

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #min neighbor=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)        



if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()