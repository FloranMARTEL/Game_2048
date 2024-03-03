from tkinter import Frame,Label

class Block(Frame):

    def __init__(self,master,num : int = None) -> None:

        color = "blue"

        super().__init__(master,background=color,width=100,height=100,borderwidth=1, relief="solid",highlightcolor="black")
        self.pack_propagate(False)
        
        if num != None:
            LabelText = Label(self,text=num,background=color,fg='#fff',font=("Arial", 25))
            LabelText.pack(expand=1)
        