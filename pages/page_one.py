import tkinter as tk

LARGE_FONT = ("Verdona", 12)

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="First Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Back to start Page", command=lambda: controller.show_frame(StartPage))
        button.pack()



