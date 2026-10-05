# import tkinter as tk

# root = tk.Tk()
# root.title("My First Canvas")

# canvas = tk.Canvas(root, width=500,
#                    height=350, bg="white")

# canvas.pack()
# canvas.create_rectangle(40, 40, 220, 150, fill="coral")
# canvas.create_oval(200, 50, 440, 190, fill="lightblue")
# canvas.create_line(50,250, 500, 250, width=4)
# canvas.create_text(275, 310, text="Hello Canvas", font=
# ("Arial",20))

# root.mainloop()

import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=450, bg="skyblue")
canvas.pack()

# ---------------- SUN ----------------
canvas.create_oval(40, 40, 100, 100, fill="yellow", outline="orange")

# Sun rays
for x1, y1, x2, y2 in [
    (70, 30, 70, 15),
    (70, 110, 70, 125),
    (30, 70, 15, 70),
    (110, 70, 125, 70)
]:
    canvas.create_line(x1, y1, x2, y2, fill="orange", width=3)


# ---------------- GRASS ----------------
canvas.create_rectangle(0, 350, 600, 450, fill="lightgreen")


# ---------------- MAIN HOUSE ----------------

# House body
canvas.create_rectangle(180, 190, 420, 350, fill="lightyellow")

# Roof
canvas.create_polygon(
    150, 190,
    300, 90,
    450, 190,
    fill="firebrick"
)

# Roof shading
for x in range(175, 426, 25):
    canvas.create_line(x, 190, 300, 90, fill="darkred")

# Chimney
canvas.create_rectangle(360, 120, 390, 175, fill="brown")

# Door
canvas.create_rectangle(275, 270, 325, 350, fill="saddlebrown")

# Door knob
canvas.create_oval(312, 305, 318, 311, fill="yellow")

# Left window
canvas.create_rectangle(200, 220, 250, 270, fill="lightblue")
canvas.create_line(225, 220, 225, 270, fill="white", width=3)
canvas.create_line(200, 245, 250, 245, fill="white", width=3)

# Right window
canvas.create_rectangle(350, 220, 400, 270, fill="lightblue")
canvas.create_line(375, 220, 375, 270, fill="white", width=3)
canvas.create_line(350, 245, 400, 245, fill="white", width=3)


# ---------------- PATH ----------------
canvas.create_polygon(
    275, 350,
    325, 350,
    370, 450,
    230, 450,
    fill="burlywood"
)


# ---------------- DOG HOUSE ----------------

# Dog house body
canvas.create_rectangle(40, 320, 140, 380, fill="peru")

# Dog house roof
canvas.create_polygon(
    25, 320,
    90, 275,
    155, 320,
    fill="brown"
)

# Dog house entrance
canvas.create_oval(65, 335, 115, 380, fill="black")


# ---------------- PUPPY ----------------

# Body
canvas.create_oval(470, 335, 550, 385, fill="brown")

# Head
canvas.create_oval(490, 295, 555, 350, fill="brown")

# Ears
canvas.create_oval(485, 295, 505, 330, fill="saddlebrown")
canvas.create_oval(540, 295, 560, 330, fill="saddlebrown")

# Eyes
canvas.create_oval(505, 312, 512, 319, fill="black")
canvas.create_oval(535, 312, 542, 319, fill="black")

# Nose
canvas.create_oval(520, 325, 530, 333, fill="black")

# Legs
canvas.create_rectangle(485, 365, 500, 400, fill="brown")
canvas.create_rectangle(525, 365, 540, 400, fill="brown")

# Tail
canvas.create_line(545, 345, 570, 325, fill="brown", width=6)


# ---------------- FLOWERS ----------------

# Flower 1
canvas.create_oval(120, 400, 130, 410, fill="red")
canvas.create_oval(130, 400, 140, 410, fill="red")
canvas.create_oval(125, 395, 135, 405, fill="red")
canvas.create_oval(125, 405, 135, 415, fill="red")
canvas.create_oval(128, 402, 133, 407, fill="yellow")

# Flower 2
canvas.create_oval(440, 400, 450, 410, fill="purple")
canvas.create_oval(450, 400, 460, 410, fill="purple")
canvas.create_oval(445, 395, 455, 405, fill="purple")
canvas.create_oval(445, 405, 455, 415, fill="purple")
canvas.create_oval(448, 402, 453, 407, fill="yellow")


root.mainloop()