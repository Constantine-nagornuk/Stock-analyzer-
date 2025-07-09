import customtkinter
from customtkinter import *
from API import * 

def Stock_Graph():
    drawgraph(frame1)
    Text1 = About["Industry"]
    label1 = customtkinter.CTkLabel(master=frame1, text= Text1 , fg_color="Black", text_color="White")
    label1.grid(row=1 , column=0, pady=10)
    # make this a loop so I dont have to type out like million things :)
app = CTk()
app.geometry("1200x800")
app.title("Stock-Project")
set_appearance_mode("dark")
set_default_color_theme("dark-blue")



tabview = CTkTabview(master=app)
tabview.grid(row=0, padx=20, pady=5, sticky="nsew")
tabview.add("tab 1")
tabview.add("tab 2")
tabview.set("tab 1")
 
#--------------------------------------------------------------------------#

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

tab1 = tabview.tab("tab 1")
tab1.grid_rowconfigure(0, weight=1)

tab1.grid_columnconfigure(0, weight=1)
tab1.grid_columnconfigure(1, weight=1)



#--------------------------------------------------------------------------#

frame1 = CTkFrame(master=tab1,fg_color="Green")
frame1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
frame2 = CTkFrame(master=tab1, fg_color="Red")
frame2.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")

frame1.grid_rowconfigure(0, weight=0)
frame1.grid_rowconfigure(1, weight=0)
frame2.grid_columnconfigure(0, weight=1)

frame2.grid_rowconfigure(0, weight=0)
frame2.grid_rowconfigure(1, weight=0)
frame2.grid_rowconfigure(2, weight=0)
frame2.grid_columnconfigure(0, weight=1)
# master of frames is tab1 they go into that row and column configure of that
#--------------------------------------------------------------------------#

button = CTkButton(master=frame2, text="Graph", command=Stock_Graph)
button.grid(padx=2, pady=4, row=0,column=0)

def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)
optionmenu_var = customtkinter.StringVar(value="option 2")
optionmenu = customtkinter.CTkOptionMenu(values=["option 1", "option 2"],command=optionmenu_callback,variable=optionmenu_var, master= frame2)
optionmenu.grid(row=1,padx=2, pady=4, column=0)



app.mainloop()
