import customtkinter
from customtkinter import *
from API import * 
from cnn_train import *
from runCNN import * 

# make everything run in  a function so I dont ruun 50 things when I run ts file
def Stock_Graph():
    period = period_var.get()
    interval = interval_var.get()
    drawgraph(frame1,period,interval) 
    number = 3
    number2 = 0
    for i in About:
        text2 = About[i]
        if number>=6:
            number2 = 1
            number = 3
        label2 = customtkinter.CTkLabel(master=frame2, text=f'{i}:{text2}' , fg_color="#14295c",text_color="#cbd5e1",corner_radius=8,font=("Segoe UI", 14, "bold"),anchor="center",padx=20,pady=6)
        label2.grid(row=number , column=number2, pady=10, columnspan=1,sticky="ew")
        number += 1 
    
    #take the grpah made by user
    # download it and allow it to be read by cnn stuff
    #display it in here
    Pred_Label = customtkinter.CTkLabel(master=frame2, text='Test' , fg_color="red", text_color="White")
    Pred_Label.grid(row=6 , column=0, pady=10, columnspan=2, sticky="ew")
    



app = CTk()
app.geometry("1400x800")
app.title("Stock-Project")
set_appearance_mode("dark")
set_default_color_theme("dark-blue")



tabview = CTkTabview(master=app)
tabview.grid(row=0, padx=20, pady=5, sticky="nsew")
tabview.add("Graph")
tabview.add("tab 2")
tabview.set("Graph")
 
#--------------------------------------------------------------------------#

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

tab1 = tabview.tab("Graph")
tab1.grid_rowconfigure(0, weight=1)

tab1.grid_columnconfigure(0, weight=1)
tab1.grid_columnconfigure(1, weight=1)



#--------------------------------------------------------------------------#

frame1 = CTkScrollableFrame(master=tab1,fg_color="transparent", width=500)
frame1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
frame2 = CTkFrame(master=tab1, fg_color="transparent", width=200)
frame2.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")

for i in range(2):
    frame1.grid_rowconfigure(i, weight=0)
frame1.grid_columnconfigure(0, weight=0)
frame1.grid_columnconfigure(1, weight=0)



frame2.grid_columnconfigure(0, weight=1)
frame2.grid_columnconfigure(1, weight=1)
for i in range(7):
    frame1.grid_rowconfigure(i, weight=0)

# master of frames is tab1 they go into that row and column configure of that
#--------------------------------------------------------------------------#

button = CTkButton(master=frame2, text="Graph", command=Stock_Graph)
button.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

Predict = CTkButton(master=frame2, text="Predict", command= CNN_predict) # its predicts the pre determied file for now
Predict.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="ew")



# --- Period OptionMenu --- #

period_options = [
    "1d", "5d", "1mo", "3mo", "6mo",
    "1y", "2y", "5y", "10y", "ytd", "max"
]
period_var = customtkinter.StringVar(value="1mo")
period_menu = customtkinter.CTkOptionMenu(
    master=frame2,
    values=period_options,
    variable=period_var
)
period_menu.grid(row=1, column=0, padx=5, pady=4, columnspan=2, sticky="ew")
# --- Interval OptionMenu --- #

interval_options = [
    "1m", "2m", "5m", "15m", "30m", "60m", "90m",
    "1h", "1d", "5d", "1wk", "1mo", "3mo"
]
interval_var = customtkinter.StringVar(value="1d")
interval_menu = customtkinter.CTkOptionMenu(
    master=frame2,
    values=interval_options,
    variable=interval_var
)
interval_menu.grid(row=2, column=0, padx=5, pady=4, columnspan=2, sticky="ew")
#--------------------------------------------------------------------------#

app.mainloop()
