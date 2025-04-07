import sqlite3
import tkinter as tk
from tkinter import messagebox

def submit():
    # Get data from fields
    first = first_name.get()
    last = last_name.get()
    bday = birthday.get()
    mail = email.get()
    phone_num = phone.get()
    street = street_address.get()
    city_val = city.get()
    state_val = state_province.get()
    zip_code = zip_postal.get()
    contact = contact_method.get()

    # Insert into database
    conn = sqlite3.connect('customers.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO customers 
            (first_name, last_name, birthday, email, phone, 
            street_address, city, state_province, zip_postal, preferred_contact) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (first, last, bday, mail, phone_num, street, city_val, state_val, zip_code, contact))
        conn.commit()
        messagebox.showinfo("Success", "Customer info added!")

        # ✅ Clear fields after successful insert
        first_name.delete(0, tk.END)
        last_name.delete(0, tk.END)
        birthday.delete(0, tk.END)
        email.delete(0, tk.END)
        phone.delete(0, tk.END)
        street_address.delete(0, tk.END)
        city.delete(0, tk.END)
        state_province.delete(0, tk.END)
        zip_postal.delete(0, tk.END)
        contact_method.set("")  # Clears the dropdown


    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Email already exists.")
    finally:
        conn.close()

# GUI setup
root = tk.Tk()
root.title("Customer Entry Form")
root.geometry("400x450")

# Input fields
tk.Label(root, text="First Name").pack()
first_name = tk.Entry(root)
first_name.pack()

tk.Label(root, text="Last Name").pack()
last_name = tk.Entry(root)
last_name.pack()

tk.Label(root, text="Birthday (YYYY-MM-DD)").pack()
birthday = tk.Entry(root)
birthday.pack()

tk.Label(root, text="Email").pack()
email = tk.Entry(root)
email.pack()

tk.Label(root, text="Phone").pack()
phone = tk.Entry(root)
phone.pack()

tk.Label(root, text="Street Address").pack()
street_address = tk.Entry(root)
street_address.pack()

tk.Label(root, text="City").pack()
city = tk.Entry(root)
city.pack()

tk.Label(root, text="State/Province").pack()
state_province = tk.Entry(root)
state_province.pack()

tk.Label(root, text="ZIP/Postal Code").pack()
zip_postal = tk.Entry(root)
zip_postal.pack()

tk.Label(root, text="Preferred Contact Method").pack()
contact_method = tk.StringVar()
tk.OptionMenu(root, contact_method, "Email", "Phone", "Mail").pack()

tk.Button(root, text="Submit", command=submit).pack(pady=10)

root.mainloop()