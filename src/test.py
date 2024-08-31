# from Neat import DAOJson

# import json
# import os


# DATAFile = "src\\Neat\\data"
# PREFIX = "Generation_"

# if __name__ == "__main__":
#     print(DAOJson.Read(1))

#     json_dict = [{"a": 1, "b":2}]
#     json_str = json.dumps(json_dict,indent=1)

#     open(DATAFile+"\\"+PREFIX+str(2)+".json","w").write(json_str)

#     os.remove(DATAFile+"\\"+PREFIX+str(2)+".json")


from tkinter import * 

def onObjectClick(event):                  
    print('Got object click', event.x, event.y)
    print(event.widget.find_closest(event.x, event.y))

root = Tk()
canv = Canvas(root, width=100, height=100)
obj1Id = canv.create_line(0, 30, 100, 30, width=5, tags="obj1Tag")
obj2Id = canv.create_text(50, 70, text='Click', tags='obj2Tag')

canv.tag_bind(obj1Id, '<ButtonPress-1>', onObjectClick)       
canv.tag_bind('obj2Tag', '<ButtonPress-1>', onObjectClick)   
print('obj1Id: ', obj1Id)
print('obj2Id: ', obj2Id)
canv.pack()
root.mainloop()