import customtkinter as ctk
import pyperclip
import random

# Define consonant and vowel lists
consonants = "bcdfghjklmnpqrstvwxyz"
vowels = "aeiou"

def generate_username(replace_letters=True):
    """Generates a random 4-letter pronounceable username with optional number replacement."""
    username = ""

    # Generate first two letters (consonant-vowel)
    username += random.choice(consonants)
    username += random.choice(vowels)

    # Generate last two letters (can be consonant-consonant or vowel-consonant)
    if random.choice([True, False]):
        username += random.choice(consonants)
        username += random.choice(consonants)
    else:
        username += random.choice(vowels)
        username += random.choice(consonants)

    # Replace certain letters with numbers (optional)
    if replace_letters:
        for i in range(len(username)):
            if username[i] in ["a", "e", "i", "o", "b"]:
                if random.choice([True, False]):
                    username = username[:i] + str(random.randint(4, 9)) + username[i + 1:]

    return username

def generate_and_copy():
    new_username = generate_username()
    username_entry.delete(0, ctk.END)
    username_entry.insert(0, new_username)
    pyperclip.copy(new_username)
    notice_label.configure(text="Username copied to clipboard!")

# Create the main window
root = ctk.CTk()
root.title("Username Generator")

# Center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 500
window_height = 150
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a frame to hold the username entry and copy button
username_frame = ctk.CTkFrame(root)
username_frame.pack(pady=10)

# Create a text field to display the username
username_entry = ctk.CTkEntry(username_frame, width=200)
username_entry.pack(side=ctk.LEFT, padx=10)

# Create a copy button
copy_button = ctk.CTkButton(username_frame, text="Copy", command=lambda: pyperclip.copy(username_entry.get()))
copy_button.pack(side=ctk.LEFT, padx=10)

# Create a generate button
generate_button = ctk.CTkButton(root, text="Generate", command=generate_and_copy)
generate_button.pack(pady=10)

# Create a label to display notices
notice_label = ctk.CTkLabel(root, text="")
notice_label.pack(pady=10)

# Run the app
root.mainloop()