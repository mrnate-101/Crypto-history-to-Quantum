import tkinter as tk
import random

# --- RSA Helper Functions ---
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
    g, x, y = egcd(e, phi)
    return x % phi

def is_prime(n, k=10):
    if n <= 1 or n % 2 == 0:
        return False
    if n == 2:
        return True

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_large_prime(bits=8):  # small for demo
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

def generate_keys(bits=8):
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = mod_inverse(e, phi)
    return (e, n), (d, n)

def encrypt(public_key, plaintext):
    e, n = public_key
    return [pow(ord(char), e, n) for char in plaintext]

def decrypt(private_key, ciphertext):
    d, n = private_key
    try:
        return ''.join([chr(pow(char, d, n)) for char in ciphertext])
    except:
        return "⚠️ Invalid decryption"

# --- GUI ---
def generate_keypair():
    global public_key, private_key
    public_key, private_key = generate_keys(bits=8)
    key_display.delete("1.0", tk.END)
    key_display.insert(tk.END, f"Public Key: {public_key}\nPrivate Key: {private_key}")

def encrypt_message():
    msg = input_entry.get().strip()
    if msg and public_key:
        cipher = encrypt(public_key, msg)
        output_entry.delete("1.0", tk.END)
        output_entry.insert(tk.END, str(cipher))
    else:
        output_entry.delete("1.0", tk.END)
        output_entry.insert(tk.END, "⚠️ Generate keys & enter a message!")

def decrypt_message():
    cipher_text = output_entry.get("1.0", tk.END).strip()
    try:
        cipher_list = eval(cipher_text)  # convert string back to list
        plain = decrypt(private_key, cipher_list)
        result_entry.delete("1.0", tk.END)
        result_entry.insert(tk.END, plain)
    except:
        result_entry.delete("1.0", tk.END)
        result_entry.insert(tk.END, "⚠️ Invalid ciphertext!")

# --- GUI Setup ---
root = tk.Tk()
root.title("RSA Encryption / Decryption")
root.geometry("600x500")

tk.Label(root, text="Enter Message:").pack(pady=5)
input_entry = tk.Entry(root, width=50)
input_entry.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Generate Keys", command=generate_keypair, width=15).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Encrypt", command=encrypt_message, width=15).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Decrypt", command=decrypt_message, width=15).grid(row=0, column=2, padx=5)

tk.Label(root, text="Keys:").pack(pady=5)
key_display = tk.Text(root, height=4, width=70)
key_display.pack(pady=5)

tk.Label(root, text="Ciphertext:").pack(pady=5)
output_entry = tk.Text(root, height=5, width=70)
output_entry.pack(pady=5)

tk.Label(root, text="Decrypted Message:").pack(pady=5)
result_entry = tk.Text(root, height=3, width=70)
result_entry.pack(pady=5)

public_key, private_key = None, None

root.mainloop()
