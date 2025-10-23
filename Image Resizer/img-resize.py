import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def upload_image():
    global img, img_path
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.webp")]
    )
    if not file_path:
        return
    img_path = file_path
    img = Image.open(file_path)
    preview = img.copy()
    preview.thumbnail((200, 200))
    img_tk = ImageTk.PhotoImage(preview)
    img_label.config(image=img_tk)
    img_label.image = img_tk
    messagebox.showinfo("Image Loaded", "Image uploaded successfully!")

def resize_image():
    if not img_path:
        messagebox.showerror("Error", "Please upload an image first.")
        return
    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers for width and height.")
        return

    output_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("All files", "*.*")]
    )

    if not output_path:
        return

    with Image.open(img_path) as im:
        resized = im.resize((width, height), Image.Resampling.LANCZOS)
        resized.save(output_path)

    messagebox.showinfo("Success", f"Image resized and saved to:\n{output_path}")

# --- GUI Setup ---
root = tk.Tk()
root.title("Image Resizer")
root.geometry("400x400")
root.resizable(False, False)

tk.Label(root, text="🖼️ Simple Image Resizer", font=("Arial", 14, "bold")).pack(pady=10)

upload_btn = tk.Button(root, text="Upload Image", command=upload_image, width=20, bg="#4CAF50", fg="white")
upload_btn.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Width:").grid(row=0, column=0, padx=5)
width_entry = tk.Entry(frame, width=8)
width_entry.insert(0, "128")
width_entry.grid(row=0, column=1)

tk.Label(frame, text="Height:").grid(row=0, column=2, padx=5)
height_entry = tk.Entry(frame, width=8)
height_entry.insert(0, "128")
height_entry.grid(row=0, column=3)

resize_btn = tk.Button(root, text="Resize & Save", command=resize_image, width=20, bg="#2196F3", fg="white")
resize_btn.pack(pady=10)

img_label = tk.Label(root)
img_label.pack(pady=10)

img_path = None
root.mainloop()
