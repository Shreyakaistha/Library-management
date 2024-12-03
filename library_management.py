import tkinter as tk
from tkinter import messagebox

# Function to handle "Update Book/Movie"
def update_item():
    item_type = var_item_type.get()
    name = entry_item_name.get()
    author_director = entry_author_director.get()
    year = entry_year.get()

    if not name or not author_director or not year:
        messagebox.showerror("Error", "All fields are mandatory for updating!")
        return

    # Placeholder for database interaction
    messagebox.showinfo("Success", f"{item_type} '{name}' updated successfully!")

# Function to handle "User Management"
def manage_user():
    user_type = var_user_type.get()
    name = entry_user_name.get()

    if not name:
        messagebox.showerror("Error", "Name is mandatory for user management!")
        return

    # Placeholder for database interaction
    messagebox.showinfo("Success", f"{user_type} user '{name}' processed successfully!")

# Tkinter Root Window
root = tk.Tk()
root.title("Library Management System")
root.geometry("400x400")

# Notebook Frame
notebook = tk.Frame(root)
notebook.pack(fill="both", expand=True)

# Update Book/Movie Section
frame_update = tk.LabelFrame(notebook, text="Update Book/Movie", padx=10, pady=10)
frame_update.pack(fill="both", padx=10, pady=5)

var_item_type = tk.StringVar(value="Book")
tk.Label(frame_update, text="Select Type:").grid(row=0, column=0, sticky="w", pady=5)
tk.Radiobutton(frame_update, text="Book", variable=var_item_type, value="Book").grid(row=0, column=1, pady=5)
tk.Radiobutton(frame_update, text="Movie", variable=var_item_type, value="Movie").grid(row=0, column=2, pady=5)

tk.Label(frame_update, text="Name:").grid(row=1, column=0, sticky="w", pady=5)
entry_item_name = tk.Entry(frame_update)
entry_item_name.grid(row=1, column=1, columnspan=2, pady=5, sticky="we")

tk.Label(frame_update, text="Author/Director:").grid(row=2, column=0, sticky="w", pady=5)
entry_author_director = tk.Entry(frame_update)
entry_author_director.grid(row=2, column=1, columnspan=2, pady=5, sticky="we")

tk.Label(frame_update, text="Year:").grid(row=3, column=0, sticky="w", pady=5)
entry_year = tk.Entry(frame_update)
entry_year.grid(row=3, column=1, columnspan=2, pady=5, sticky="we")

tk.Button(frame_update, text="Update", command=update_item).grid(row=4, column=0, columnspan=3, pady=10)

# User Management Section
frame_user = tk.LabelFrame(notebook, text="User Management", padx=10, pady=10)
frame_user.pack(fill="both", padx=10, pady=5)

var_user_type = tk.StringVar(value="New")
tk.Label(frame_user, text="Select User Type:").grid(row=0, column=0, sticky="w", pady=5)
tk.Radiobutton(frame_user, text="New", variable=var_user_type, value="New").grid(row=0, column=1, pady=5)
tk.Radiobutton(frame_user, text="Existing", variable=var_user_type, value="Existing").grid(row=0, column=2, pady=5)

tk.Label(frame_user, text="Name:").grid(row=1, column=0, sticky="w", pady=5)
entry_user_name = tk.Entry(frame_user)
entry_user_name.grid(row=1, column=1, columnspan=2, pady=5, sticky="we")

tk.Button(frame_user, text="Submit", command=manage_user).grid(row=2, column=0, columnspan=3, pady=10)

# Run the Tkinter Loop
root.mainloop()
