from tkinter import Frame,Label

class Block(Frame):

    def __init__(self,master,num : int = None,w:int = 100,h:int = 100) -> None:

        color = "blue"

        self.dimentionLetter = int((h*25)/100)

        super().__init__(master,background=color,width=w,height=h,borderwidth=1, relief="solid",highlightcolor="black")
        self.pack_propagate(False)
        
        if num != None:
            LabelText = Label(self,text=num,background=color,fg='#fff',font=("Arial", self.dimentionLetter))
            LabelText.pack(expand=1)
        