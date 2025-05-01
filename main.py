import tkinter as tk
from functions import draw_grid, clear_canvas
from mouse_interactions import mouse_position

#const
window_width = 800
window_height = 800

grid_size = 16
grid_width = canvas_width = window_width // grid_size
grid_height = canvas_height = window_height // grid_size

#main window
window = tk.Tk()
window.title("ASCII Tree Painter")
window.geometry(f"{window_width}x{window_height}")
window.resizable(False, False)

#canvas
canvas = tk.Canvas(window, width=canvas_width * grid_size, height=canvas_height * grid_size, bg="white")
canvas.pack()

#clear button
clear_button = tk.Button(
    window,
    text="Clear",
    command=lambda: clear_canvas(canvas, canvas_width, canvas_height, grid_size)
)
clear_button.place(x=10, y=10)


draw_grid(canvas, canvas_width, canvas_height, grid_size)

mouse_position(canvas)

window.mainloop()