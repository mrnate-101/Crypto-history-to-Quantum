import tkinter as tk

# --- Vigenère Cipher Functions ---
def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()
    key_length = len(key)
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % key_length]) - 65
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result


def vigenere_decrypt(text, key):
    result = ""
    key = key.upper()
    key_length = len(key)
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % key_length]) - 65
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result


# --- Button Functions ---
def encode():
    text = input_entry.get().strip()
    key = key_entry.get().strip()
    if text and key:
        encrypted = vigenere_encrypt(text, key)
        output_entry.delete("1.0", tk.END)
        output_entry.insert(tk.END, encrypted)
    else:
        output_entry.delete("1.0", tk.END)
        output_entry.insert(tk.END, "⚠️ Enter both text and key!")


def decode():
    text = input_entry.get().strip()
    key = key_entry.get().strip()
    if text and key:
        decrypted = vigenere_decrypt(text, key)
        output_entry.delete("1.0", tk.END)
        output_entry.insert(tk.END, decrypted)
    else:
        output_entry.delete("1.0", tk.END)
        output_entry.insert(tk.END, "⚠️ Enter both text and key!")


def clear_all():
    input_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)
    output_entry.delete("1.0", tk.END)


# --- GUI Setup ---
root = tk.Tk()
root.title("Vigenère Cipher")
root.geometry("550x400")

tk.Label(root, text="Enter your message:").pack(pady=5)
input_entry = tk.Entry(root, width=60)
input_entry.pack(pady=5)

tk.Label(root, text="Enter key:").pack(pady=5)
key_entry = tk.Entry(root, width=30)
key_entry.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

encode_button = tk.Button(button_frame, text="ENCODE", command=encode, width=12)
encode_button.grid(row=0, column=0, padx=5)

decode_button = tk.Button(button_frame, text="DECODE", command=decode, width=12)
decode_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(button_frame, text="CLEAR", command=clear_all, width=12)
clear_button.grid(row=0, column=2, padx=5)

tk.Label(root, text="Result:").pack(pady=5)
output_entry = tk.Text(root, height=6, width=60)
output_entry.pack(pady=5)

root.mainloop()
