import os
import tkinter as tk


os.environ["TK_SILENCE_DEPRECATION"] = "1"


def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def encode():
    user_text = input_entry.get().strip()
    if user_text:
        result = caesar_cipher(user_text, 3)
        output_entry.delete("1.0", tk.END)
        output_entry.insert(tk.END, result)
    else:
        output_entry.delete("1.0", tk.END)
        output_entry.insert(tk.END, "⚠️ No input text!")

def decode():
    user_text = input_entry.get().strip()
    if user_text:
        result = caesar_cipher(user_text, -3)
        output_entry.delete("1.0", tk.END)
        output_entry.insert(tk.END, result)
    else:
        output_entry.delete("1.0", tk.END)
        output_entry.insert(tk.END, "⚠️ No input text!")

def clear_all():
    input_entry.delete(0, tk.END)
    output_entry.delete("1.0", tk.END)

# --- GUI Setup ---
root = tk.Tk()
root.title("Encoder / Decoder")
root.geometry("500x400") 

tk.Label(root, text="Enter your message:").pack(pady=5)
input_entry = tk.Entry(root, width=50)  # Single line input
input_entry.pack(pady=5)


button_frame = tk.Frame(root)
button_frame.pack(pady=10)

encode_button = tk.Button(button_frame, text="ENCODE", command=encode, width=10)
encode_button.grid(row=0, column=0, padx=5)

decode_button = tk.Button(button_frame, text="DECODE", command=decode, width=10)
decode_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(button_frame, text="CLEAR", command=clear_all, width=10)
clear_button.grid(row=0, column=2, padx=5)


tk.Label(root, text="Result:").pack(pady=5)
output_entry = tk.Text(root, height=6, width=50)
output_entry.pack(pady=5)


root.mainloop()
