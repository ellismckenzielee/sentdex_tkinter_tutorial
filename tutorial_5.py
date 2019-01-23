import tkinter as tk
from tkinter import ttk

LARGE_FONT =('Verdana', 12)

class SeapfBTCAPP(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #Add icon to the window instead of the feather - has to be ico format
        #tk.Tk.iconbitmap(self, default='')
        tk.Tk.wm_title(self, 'Sea of BTC Client')

        container = tk.Frame(self)
        #Fill fills in space that you have alloted the pack
        #Expand fills any potential space
        container.pack(side='top', fill='both', expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}


        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] =  frame
            #nsew stretches frame to the size of the window 
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

def qf(print_statement):
    print(print_statement)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text='Start Page', font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text='Visit Page 1', command=lambda: controller.show_frame(PageOne))
        button1.pack()
        button2 = ttk.Button(self, text='Page 2', command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text='Page 1', font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button1 = ttk.Button(self, text='Back to home', command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text='Page 2', command=lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageTwo(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text='Page 2', font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button1 = ttk.Button(self, text='Back to home', command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text='Page 1', command=lambda: controller.show_frame(PageOne))
        button2.pack()


app = SeapfBTCAPP()
app.mainloop()