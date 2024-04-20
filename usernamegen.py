import customtkinter as ctk
import pyperclip
import random
import string

DEFAULT_USERNAME_LENGTH = 4
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
VOWELS = "aeiou"
DIGITS = string.digits

def generate_username(length, include_capitals, include_numbers):
    """Generate a random pronounceable username with optional length, character inclusion."""
    available_chars = CONSONANTS + VOWELS + DIGITS
    if include_capitals:
        available_chars += CONSONANTS.upper() + VOWELS.upper()

    username = ""
    for _ in range(length):
        if len(username) % 2 == 0:
            username += random.choice(CONSONANTS)
        else:
            username += random.choice(VOWELS)
        if include_numbers and random.random() < 0.5:  # 50% chance of adding a digit
            username += random.choice(DIGITS)

    return username[:length]

def generate_and_copy():
    """Generate a new username, display it, and copy it to the clipboard."""
    try:
        new_username = generate_username(
            int(username_length_entry.get()),
            include_capitals_var.get(),
            include_numbers_var.get()
        )
        username_entry.delete(0, ctk.END)
        username_entry.insert(0, new_username)
        pyperclip.copy(new_username)
        notice_label.configure(text="Username copied to clipboard!")
    except ValueError:
        notice_label.configure(text="Please enter a valid integer for the username length.")

def center_window(window, width, height):
    """Center the given window on the screen and prevent full-screening."""
    screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
    window.geometry(f"{width}x{height}+{(screen_width - width) // 2}+{(screen_height - height) // 2}")
    window.resizable(False, False)

def set_default_username_length():
    """Set the default username length in the entry field."""
    username_length_entry.delete(0, ctk.END)
    username_length_entry.insert(0, str(DEFAULT_USERNAME_LENGTH))

root = ctk.CTk()
root.title("Username Generator")
center_window(root, 600, 220)

username_frame = ctk.CTkFrame(root)
username_frame.pack(pady=10)

username_entry = ctk.CTkEntry(username_frame, width=200)
username_entry.pack(side=ctk.LEFT, padx=10)

copy_button = ctk.CTkButton(username_frame, text="Copy", command=lambda: pyperclip.copy(username_entry.get()))
copy_button.pack(side=ctk.LEFT, padx=10)

generate_button = ctk.CTkButton(root, text="Generate", command=generate_and_copy)
generate_button.pack(pady=10)

notice_label = ctk.CTkLabel(root, text="")
notice_label.pack(pady=10)

customization_frame = ctk.CTkFrame(root)
customization_frame.pack(pady=10)

username_length_label = ctk.CTkLabel(customization_frame, text="Username Length:")
username_length_label.pack(side=ctk.LEFT, padx=10)
username_length_entry = ctk.CTkEntry(customization_frame, width=50)
username_length_entry.pack(side=ctk.LEFT, padx=10)
set_default_username_length()

include_capitals_var = ctk.BooleanVar(value=True)
include_capitals_checkbox = ctk.CTkCheckBox(customization_frame, text="Include Capitals", variable=include_capitals_var)
include_capitals_checkbox.pack(side=ctk.LEFT, padx=10)

include_numbers_var = ctk.BooleanVar(value=True)
include_numbers_checkbox = ctk.CTkCheckBox(customization_frame, text="Include Numbers", variable=include_numbers_var)
include_numbers_checkbox.pack(side=ctk.LEFT, padx=10)

root.mainloop()
