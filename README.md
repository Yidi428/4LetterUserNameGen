# Username Generator

This is a simple username generator application built using the `customtkinter` library in Python. The application allows users to generate random, pronounceable usernames with optional length, capital letters, and numbers.

## Features

- **Customizable Username Length**: Users can specify the desired length of the generated username.
- **Include Capitals**: Users can choose to include capital letters in the generated username.
- **Include Numbers**: Users can choose to include numbers in the generated username.
- **Pronounceable Usernames**: The generated usernames are designed to be pronounceable, with alternating consonants and vowels.
- **Copy to Clipboard**: The generated username can be easily copied to the clipboard with a single click.

## Usage

1. Clone the repository:
   ```
   git clone https://github.com/Yidi428/4LetterUserNameGen.git
   ```
2. Navigate to the project directory:
   ```
   cd 4LetterUserNameGen
   ```
3. Install the required dependencies:
   ```
   pip install customtkinter pyperclip
   ```
4. Run the Python script to launch the application:
   ```
   python username_generator.py
   ```
5. Adjust the desired settings in the customization frame:
   - **Username Length**: Enter the desired length of the generated username.
   - **Include Capitals**: Check the box to include capital letters in the generated username.
   - **Include Numbers**: Check the box to include numbers in the generated username.
6. Click the "Generate" button to generate a new username.
7. The generated username will be displayed in the entry field and automatically copied to the clipboard.

## Code Explanation

The main components of the code are:

1. **`generate_username()`**: This function generates a random, pronounceable username based on the user's preferences for length, capital letters, and numbers.
2. **`generate_and_copy()`**: This function is called when the "Generate" button is clicked. It generates a new username, displays it in the entry field, and copies it to the clipboard.
3. **`center_window()`**: This function centers the application window on the screen and prevents the user from resizing it.
4. **`set_default_username_length()`**: This function sets the default username length in the entry field.

The application uses the `customtkinter` library to create the graphical user interface, including the entry field, buttons, and checkboxes. The `pyperclip` library is used to copy the generated username to the clipboard.

## Dependencies

- Python 3.x
- `customtkinter` library
- `pyperclip` library

You can install the required dependencies using pip:

```
pip install customtkinter pyperclip
```

## Contribution

If you have any suggestions or find any issues, feel free to create a new issue or submit a pull request on the [project's GitHub repository](https://github.com/Yidi428/4LetterUserNameGen).
