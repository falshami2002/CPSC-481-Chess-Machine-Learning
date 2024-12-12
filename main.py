import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import divide
import predict
import translate
import evaluation

image = ""

def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.webp")])
    if file_path:
        img = Image.open(file_path)
        img = img.resize((800, 800))  # Resize the image to fit the canvas
        img_tk = ImageTk.PhotoImage(img)
        global image
        image = Image.open(file_path)
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
toPlayOptions = ['White', 'Black']
var = tk.StringVar(value=toPlayOptions[0])
tk.Label(switch_frame, text="To Play", bg="white").grid(row=0, column=0, padx=10, pady=5)
for j, option in enumerate(toPlayOptions):
    tk.Radiobutton(
        switch_frame,
        text=option,
        variable=var,
        value=option,
        bg="white"
    ).grid(row=0, column=j + 1, padx=10)
switches.append(var)

castleOptions = ["White King", "White Queen", "Black King", "Black Queen"]
tk.Label(switch_frame, text="Castle", bg="white").grid(row=1, column=0, padx=10, pady=5)
for i, option in enumerate(castleOptions):
    var = tk.BooleanVar(value=False)  # Default state is unchecked
    tk.Checkbutton(
        switch_frame,
        text=option,
        variable=var,
        bg="white"
    ).grid(row=1, column=i+1, padx=10, pady=5)
    switches.append(var)

tk.Label(switch_frame, text="En Passante", bg="white").grid(row=2, column=0, padx=10, pady=5)
enPassante = tk.Entry(switch_frame, width=30)
enPassante.grid(row=2, column=1, padx=10, pady=5)

tk.Label(switch_frame, text="Evaluation: ", bg="white").grid(row=3, column=0, padx=10, pady=5)
evaluationLabel = tk.Label(switch_frame, text="", bg="white")
evaluationLabel.grid(row=3, column=1, padx=10, pady=5)

def getSwitchValues():
    selected_values = [switch.get() for switch in switches]
    FEN2 = ""
    if(selected_values[0] == 'White'):
        FEN2 += "w "
    else:
        FEN2 += 'b '

    if (selected_values[1] == True):
        FEN2 += "K"
    if (selected_values[2] == True):
        FEN2 += "Q"
    if (selected_values[3] == True):
        FEN2 += "k"
    if (selected_values[4] == True):
        FEN2 += "q"
    if (selected_values[1] == False and selected_values[2] == False and selected_values[3] == False and selected_values[4] == False):
        FEN2 += "-"
    if (enPassante.get() == ""):
        FEN2 += " -"
    else:
        FEN2 += " " + enPassante.get()
    FEN2 += " 0 20"
    print(selected_values, FEN2)
    return FEN2

def getEvaluation():
    if image == "":
        evaluationLabel.config(text="No Image Selected")
    else:
        images = divide.divideBoard(image)
        labels = predict.prediction(images)
        FEN1 = translate.toFEN(labels)
        FEN = FEN1 + " " + getSwitchValues()
        eval = evaluation.getBestMove(FEN)
        print(FEN)
        evaluationLabel.config(text=eval)

evaluate = tk.Button(switch_frame, text="Evaluate", command=getEvaluation)
evaluate.grid(row=4, column=2, padx=10, pady=5)
# Run the application
root.mainloop()
