from tkinter import *
import random

class maingui:
    def __init__(self, root, title, geometry):

        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)
        self.pageshow = Login_Page(self, self.root)
      
    def changepage(self, page):
        self.page = page
        
        if self.page == 0:
            #del self.pageshow
            self.pageshow = Login_Page(self, self.root)

        if self.page == 1:
            #del self.pageshow
            self.pageshow = Sign_Page(self, self.root)


class Login_Page:
    def __init__(self, parent, window):
        
        self.parent = parent
        
        self.frame = Frame(window)
        self.frame.pack()

        self.welcm_lbl = Label(self.frame, text='welcome')
        self.welcm_lbl.grid(row=0, column=1)

        self.name_lbl = Label(self.frame, text='name:')
        self.name_lbl.grid(row=1, column=0)

        self.name_entry = Entry(self.frame)
        self.name_entry.grid(row=1, column=1)

        self.sbt = Button(self.frame, text='login', command=self.clicked)
        self.sbt.grid(row=2, column=1)

    def clicked(self):
        self.frame.destroy()
        self.parent.changepage(1)
        

class Sign_Page():
    def __init__(self, parent, window):

        self.parent = parent
        
        self.frame = Frame(window)
        self.frame.pack()

        self.welcm_lbl = Label(self.frame, text='welcome sign-up')
        self.welcm_lbl.grid(row=0, column=1)

        self.name_lbl = Label(self.frame, text='name:')
        self.name_lbl.grid(row=1, column=0)

        self.name_entry = Entry(self.frame)
        self.name_entry.grid(row=1, column=1)

        self.sbt = Button(self.frame, text='sign-up', command=self.clicked)
        self.sbt.grid(row=2, column=1)      

    def clicked(self):
        self.frame.destroy()
        self.parent.changepage(0)
        
    
def main():
    root = Tk()
    maingui(root, "Rpg", "400x400")
    root.mainloop()
    
if __name__ =='__main__':
    main()