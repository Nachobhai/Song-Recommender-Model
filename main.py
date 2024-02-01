import tkinter as tk
from PIL import Image, ImageTk

def transliterate_word(word, transliteration_dict):
    return transliteration_dict.get(word, word)

def transliterate_input(event):
    input_text = input_entry.get()
    words = input_text.split()
    transliterated_words = [transliterate_word(word, transliteration_dict) for word in words]
    output_text.set(" ".join(transliterated_words))

# Transliteration dictionary
transliteration_dict = {
    "hello": "नमस्ते",
    "world": "दुनिया",
    # Add more words as needed
}

# Create Tkinter window
window = tk.Tk()
window.title("Dynamic Transliteration")

# Load and set the background image
background_image = Image.open("C:/Users/nachi/Desktop/family_pic.jpg")  # Replace "background_image.png" with your image file
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(window, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# Input entry widget
input_text = tk.StringVar()
input_entry = tk.Entry(window, textvariable=input_text, font=("Helvetica", 14), width= 50, )
input_entry.bind("<space>", transliterate_input)
input_entry.pack(pady=10)

# Output label widget
output_text = tk.StringVar()
output_label = tk.Label(window, textvariable=output_text, font=("Helvetica", 14))
output_label.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()