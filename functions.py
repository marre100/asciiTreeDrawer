def draw_grid(canvas, canvas_width, canvas_height, grid_size):
    for x in range(0, canvas_width * grid_size + 1, grid_size):
        canvas.create_line(x, 0, x, canvas_height * grid_size, fill="gray")

    for y in range(0, canvas_height * grid_size + 1, grid_size):
        canvas.create_line(0, y, canvas_width * grid_size, y, fill="gray")

def clear_canvas(canvas, canvas_width, canvas_height, grid_size):
    canvas.delete("all")
    draw_grid(canvas, canvas_width, canvas_height, grid_size)