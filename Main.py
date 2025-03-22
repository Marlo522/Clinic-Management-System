import tkinter as tk
from tkinter import messagebox, simpledialog
import database as db

window = tk.Tk()
db.connect_db()

class ClinicManagementSystem:
    def __init__(self, window):
        self.window = window
        self.window.title("CLINIC MANAGEMENT SYSTEM")
        self.window.geometry("1000x600")
        
        tk.Label(window, text="Clinic Management System", font=("Arial", 20)).pack()
        self.frame = tk.Frame(self.window)
        self.frame.pack()
        
        tk.Button(self.frame, text="Patient", command=self.Patient).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(self.frame, text="Doctor", command=self.Doctor).grid(row=0, column=1, padx=5, pady=5)
        
    def clear_frame(self):
        """Clear all widgets from the frame."""
        for widget in self.frame.winfo_children():
            widget.destroy()

    def Patient(self):
        self.clear_frame()
        tk.Label(self.frame, text="Patient").grid(row=0, column=0, padx=5, pady=5, columnspan=3)
        tk.Button(self.frame, text="Login", command=self.PatientLogIn).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(self.frame, text="Register", command=self.PatientRegister).grid(row=1, column=2, padx=5, pady=5)

    def Doctor(self):
        self.clear_frame()
        tk.Label(self.frame, text="Doctor").grid(row=0, column=0, padx=5, pady=5)
        tk.Button(self.frame, text="Login", command=self.DoctorLogIn).grid(row=1, column=0, padx=5, pady=5)

    def PatientLogIn(self):
        self.clear_frame()
        PatientID = simpledialog.askinteger("Input", "Enter Patient ID", parent=self.window)
        username = simpledialog.askstring("Input", "Enter username", parent=self.window)
        
        if PatientID and username:
            messagebox.showinfo("Login Info", f"Patient ID: {PatientID}, Username: {username}")
        else:
            messagebox.showwarning("Input Error", "Please provide both Patient ID and Username.")

    def PatientRegister(self):
        self.clear_frame()
        
       
        tk.Label(self.frame, text="Patient ID").grid(row=0, column=0, padx=5, pady=5)
        patient_id_entry = tk.Entry(self.frame)
        patient_id_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(self.frame, text="Username").grid(row=1, column=0, padx=5, pady=5)
        username_entry = tk.Entry(self.frame)
        username_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(self.frame, text="Password").grid(row=2, column=0, padx=5, pady=5)
        password_entry = tk.Entry(self.frame, show="*")
        password_entry.grid(row=2, column=1, padx=5, pady=5)
        
        
        tk.Button(
            self.frame, 
            text="Register", 
            command=lambda: self.Register(username_entry.get(), password_entry.get())
        ).grid(row=3, column=0, padx=5, pady=5)

    def Register(self, username, password):
        if username and password:
            try:
                user_id = db.insert_user(username, password)
                messagebox.showinfo("Success", f"User registered successfully! Your ID is: {user_id}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")


    def DoctorLogIn(self):
        print("Doctor Login functionality goes here.")
        
    
        
self = ClinicManagementSystem(window)  
window.mainloop()