import tkinter as tk
from tkinter import messagebox

def remove_common_chars(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    name1_list = list(name1)
    name2_list = list(name2)

    for ch in name1[:]:
        if ch in name2_list:
            name1_list.remove(ch)
            name2_list.remove(ch)

    total = len(name1_list) + len(name2_list)
    return total

def flames_result(count):
    flames = ['F', 'L', 'A', 'M', 'E', 'S']
    while len(flames) > 1:
        index = (count % len(flames)) - 1
        if index >= 0:
            flames = flames[index + 1:] + flames[:index]
        else:
            flames = flames[:-1]
    return flames[0]

def meaning(letter):
    return {
        'F': "Friends 👬",
        'L': "Love ❤️",
        'A': "Affection 😊",
        'M': "Marriage 💍",
        'E': "Enemies 😈",
        'S': "Siblings 👧👦"
    }[letter]

def check_flames():
    name1 = entry1.get()
    name2 = entry2.get()
    if not name1 or not name2:
        messagebox.showwarning("Missing Input", "Please enter both names!")
        return
    count = remove_common_chars(name1, name2)
    result = flames_result(count)
    result_text = f"{name1} and {name2} are... {meaning(result)}!"
    messagebox.showinfo("💘 FLAMES Result", result_text)

# GUI Setup
root = tk.Tk()
root.title("🔥 FLAMES Game")
root.geometry("400x250")
root.configure(bg="#fff0f5")

label_title = tk.Label(root, text="FLAMES Relationship Checker", font=("Arial", 16, "bold"), bg="#fff0f5")
label_title.pack(pady=10)

label1 = tk.Label(root, text="Your Name:", bg="#fff0f5")
label1.pack()
entry1 = tk.Entry(root, width=30)
entry1.pack()

label2 = tk.Label(root, text="Crush's Name 😏:", bg="#fff0f5")
label2.pack()
entry2 = tk.Entry(root, width=30)
entry2.pack()

btn = tk.Button(root, text="Check Relationship 🔍", command=check_flames, bg="#ff69b4", fg="white", padx=10, pady=5)
btn.pack(pady=20)

root.mainloop()
