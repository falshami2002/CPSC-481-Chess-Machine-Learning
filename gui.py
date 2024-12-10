import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.webp")])
    if file_path:
        img = Image.open(file_path)
        img = img.resize((800, 800))  # Resize the image to fit the canvas
        img_tk = ImageTk.PhotoImage(img)
        canvas.image = img_tk  # Keep a reference to avoid garbage collection
        canvas.create_image(400, 400, image=img_tk, anchor="center")  # Center the image

# Create the main window
root = tk.Tk()
root.title("Organized Window")
root.geometry("600x400")  # Set the window size

# Frames for left and right halves
left_frame = tk.Frame(root, width=300, height=400, bg="lightgray")
left_frame.pack(side="left", fill="both", expand=True)

right_frame = tk.Frame(root, width=300, height=400, bg="white")
right_frame.pack(side="right", fill="both", expand=True)

# Inner Frame for Canvas and Button
left_inner_frame = tk.Frame(left_frame, bg="lightgray")
left_inner_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center inner frame

# Fixed-size Canvas for Image
canvas = tk.Canvas(left_inner_frame, width=800, height=800, bg="lightgray", relief="groove")
canvas.pack(pady=10)

# Upload Button
upload_button = tk.Button(left_inner_frame, text="Upload Image", command=upload_image)
upload_button.pack(pady=10)

# Right Frame: Switches
switch_frame = tk.Frame(right_frame, bg="white")
switch_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame

switches = []
options = ["Option 1", "Option 2"]

for i in range(3):
    var = tk.StringVar(value=options[0])  # Default to Option 1
    tk.Label(switch_frame, text=f"Switch {i+1}", bg="white").grid(row=i, column=0, padx=10, pady=5)
    for j, option in enumerate(options):
        tk.Radiobutton(
            switch_frame,
            text=option,
            variable=var,
            value=option,
            bg="white"
        ).grid(row=i, column=j+1, padx=10)
    switches.append(var)

# Run the application
root.mainloop()
