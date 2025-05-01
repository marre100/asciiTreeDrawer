import tkinter as tk

def mouse_position(canvas):
    mouse_positions = []
    tracking_active = [True]

    def update_mouse_position():
        if tracking_active[0]:
            pointer_x, pointer_y = canvas.winfo_pointerxy()
            x = pointer_x - canvas.winfo_rootx()
            y = pointer_y - canvas.winfo_rootx()
            mouse_positions.append((x, y))
            print("Mouse positions:", mouse_positions)
        canvas.after(50, update_mouse_position)

    def on_mouse_enter(event):
        tracking_active[0] = True

    def on_mouse_leave(event):
        tracking_active[0] = False
        print("Mouse outside window, tracking = False")

    canvas.bind("<Enter>", on_mouse_enter)
    canvas.bind("<Leave>", on_mouse_leave)


    update_mouse_position()
    return mouse_positions



def bind_mouse_events(canvas):



    canvas.bind("<Button-1>", )
    canvas.bind("<B1-Motion>", )
    canvas.bind("<ButtonRelease-1>", )
