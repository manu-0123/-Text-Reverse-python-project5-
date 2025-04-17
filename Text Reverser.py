import tkinter as tk
from tkinter import messagebox, filedialog

def reverse_characters(text):
    return text[::-1]

def reverse_words(text):
    return ' '.join(text.split()[::-1])

def save_to_file(content):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(content)
        messagebox.showinfo("Success", f"Text saved to {file_path}")

def process_text():
    input_text = entry.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Input Error", "Please enter some text.")
        return

    if mode.get() == "characters":
        result = reverse_characters(input_text)
    else:
        result = reverse_words(input_text)

    output.delete("1.0", tk.END)
    output.insert(tk.END, result)

def create_gui():
    global entry, output, mode

    root = tk.Tk()
    root.title("Text Reverser")
    root.geometry("500x400")

    tk.Label(root, text="Enter Text:").pack(pady=5)
    entry = tk.Text(root, height=5, width=50)
    entry.pack(pady=5)

    mode = tk.StringVar(value="characters")
    tk.Radiobutton(root, text="Reverse Characters", variable=mode, value="characters").pack()
    tk.Radiobutton(root, text="Reverse Words", variable=mode, value="words").pack()

    tk.Button(root, text="Reverse", command=process_text).pack(pady=10)

    tk.Label(root, text="Output:").pack(pady=5)
    output = tk.Text(root, height=5, width=50)
    output.pack(pady=5)

    tk.Button(root, text="Save to File", command=lambda: save_to_file(output.get("1.0", tk.END))).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
