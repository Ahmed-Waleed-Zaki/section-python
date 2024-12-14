import tkinter as tk
from tkinter import messagebox

# Function to play the text as speech
def play_text():
    text = entry.get()
    if text.strip():  # Check if the entry has text
        messagebox.showinfo("Playing", f"Text to Speech: {text}")
    else:
        messagebox.showwarning("Error", "Please enter some text!")

# Function to exit the program
def exit_program():
    root.destroy()

# Function to clear the entry
def clear_text():
    entry.delete(0, tk.END)

# Create the main GUI window
root = tk.Tk()
root.title("Text to Speech")

# Create an Entry widget
entry_label = tk.Label(root, text="Enter your text:")
entry_label.pack(pady=5)  # Padding for better spacing

entry = tk.Entry(root, width=50, justify='left')
entry.pack(pady=5)

# Create buttons
play_button = tk.Button(root, text="Play", command=play_text)
play_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", fg="red", command=exit_program)
exit_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear", command=clear_text)
clear_button.pack(pady=5)

# Run the GUI loop
root.mainloop()
