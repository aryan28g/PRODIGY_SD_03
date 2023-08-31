import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")
        
        self.contacts = []
        
        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        
        self.create_gui()
        
    def create_gui(self):
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root, textvariable=self.name_var)
        self.name_entry.pack()
        
        self.phone_label = tk.Label(self.root, text="Phone:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(self.root, textvariable=self.phone_var)
        self.phone_entry.pack()
        
        self.email_label = tk.Label(self.root, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self.root, textvariable=self.email_var)
        self.email_entry.pack()
        
        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.pack()
        
        self.view_button = tk.Button(self.root, text="View Contacts", command=self.view_contacts)
        self.view_button.pack()
        
    def add_contact(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        
        if name and phone and email:
            contact = Contact(name, phone, email)
            self.contacts.append(contact)
            self.clear_entries()
            messagebox.showinfo("Success", "Contact added successfully.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")
        
    def view_contacts(self):
        if self.contacts:
            contact_list = "\n".join(f"Name: {c.name}, Phone: {c.phone}, Email: {c.email}" for c in self.contacts)
            messagebox.showinfo("Contacts", contact_list)
        else:
            messagebox.showinfo("Contacts", "No contacts found.")
        
    def clear_entries(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.email_var.set()

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagementApp(root)
    root.mainloop()
