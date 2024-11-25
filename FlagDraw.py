import tkinter as tk

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Rectangle with tkinter")

    # Create the canvas
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas.pack()

    # Create a red rectangle
    rect = canvas.create_rectangle(
        0,              # x1
        CANVAS_HEIGHT / 2,  # y1
        CANVAS_WIDTH,   # x2
        0,              # y2
        fill="red"
    )

    # Run the Tkinter main loop
    root.mainloop()

if __name__ == '__main__':
    main()
