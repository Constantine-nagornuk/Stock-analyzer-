import customtkinter
from customtkinter import *
from API import *


app = customtkinter.CTk()
app.geometry("1200x800")
app.title("Stock-Project")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
tabview = customtkinter.CTkTabview(master=app)
tabview.grid(padx=20, pady=20, row=0, column=0)

tabview.add("tab 1")  
tabview.add("tab 2") 
tabview.set("tab 1")  

app.grid_rowconfigure(0, weight=1) # Make row 0 expand
app.grid_columnconfigure(0, weight=1) # Make column 0 expand


frame1 = customtkinter.CTkFrame(master=tabview.tab("tab 1"), width=150, height=150)
frame1.grid(column=0 , row= 9, sticky="sw" )

def Stock_Graph():
    where = frame1
    # istead make it so that it goes into a frame witing the tab not
    # the tab itself
    # if clicked more then once it makes a lot of copies

    drawgraph(where,app)



button = customtkinter.CTkButton(master=tabview.tab("tab 1"), text="CTkButton", command=Stock_Graph)
button.grid(padx=20, pady=20)
















app.mainloop()























app.mainloop()

