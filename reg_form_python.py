import tkinter as tk
from tkinter import messagebox

def register():
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
    else:
        messagebox.showinfo("Success", f"Registration successful for {username}")
        # Here you can add code to save the registration details to a database or file




        
    
def clear_entries():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    confirm_password_entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Create labels
username_label = tk.Label(root, text="Username:", bg="#f0f0f0", font=("Helvetica", 12))
password_label = tk.Label(root, text="Password:", bg="#f0f0f0", font=("Helvetica", 12))
confirm_password_label = tk.Label(root, text="Confirm Password:", bg="#f0f0f0", font=("Helvetica", 12))

# Create entry fields
username_entry = tk.Entry(root, font=("Helvetica", 12))
password_entry = tk.Entry(root, show="*", font=("Helvetica", 12))
confirm_password_entry = tk.Entry(root, show="*", font=("Helvetica", 12))

# Create buttons
register_button = tk.Button(root, text="Register", command=register, bg="#4CAF50", fg="white", font=("Helvetica", 12))
clear_button = tk.Button(root, text="Clear", command=clear_entries, bg="#f44336", fg="white", font=("Helvetica", 12))

# Grid layout
username_label.grid(row=0, column=0, pady=(20, 5), padx=10, sticky="w")
username_entry.grid(row=0, column=1, pady=(20, 5), padx=10)
password_label.grid(row=1, column=0, pady=5, padx=10, sticky="w")
password_entry.grid(row=1, column=1, pady=5, padx=10)
confirm_password_label.grid(row=2, column=0, pady=5, padx=10, sticky="w")
confirm_password_entry.grid(row=2, column=1, pady=5, padx=10)
register_button.grid(row=3, column=0, columnspan=2, pady=20)
clear_button.grid(row=4, column=0, columnspan=2)

# Start the application
root.mainloop()

