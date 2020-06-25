import tkinter as tk
from pages.start_page import StartPage
from pages.page_one import PageOne

class FileSortingApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Container defenition 
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {

        }

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    """
        Render the right page in the screen. 
    """
    def show_frame(self, cont): 
        frame = self.frames[cont]
        frame.tkraise()