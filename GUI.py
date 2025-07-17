import customtkinter
from customtkinter import *
from API import * 
from cnn_train import *
from runCNN import * 
from News import *
import tkinter.messagebox as mb
Last_Loaded_Stock = None
User_input = None
Pred_Label = None

def Stock_Graph():
    global Pred_Label
    period = period_var.get()
    interval = interval_var.get()
    drawgraph(frame1,period,interval,User_input) 
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
    if Pred_Label is None:
        Pred_Label = customtkinter.CTkLabel( master=frame2,text="Prediction will appear here",fg_color="red", text_color="white")
        Pred_Label.grid(row=6, column=0, pady=10, columnspan=2, sticky="ew")



def Load_News():
    global User_input, Last_Loaded_Stock
    if not User_input:
        return  
    if User_input == Last_Loaded_Stock:
        print("News already loaded for this stock.")
        mb.showwarning("Warning", "News is already loaded for this stock!")
        return
    try:
        stock = yf.Ticker(User_input)
        news_data = Display_News(stock)
        # Display news
        for item in news_data:
            frame = CTkFrame(master=news_scroll_frame, fg_color="#1e293b", corner_radius=10)
            frame.pack(padx=10, pady=5, fill="x")

            title = CTkLabel(frame, text=item["title"], font=("Segoe UI", 14, "bold"), text_color="#f1f5f9", wraplength=700, anchor="w", justify="left")
            title.pack(anchor="w", padx=10, pady=5)

            info = CTkLabel(frame, text=f'{item["pub_date"]} - {item["provider"]}', font=("Segoe UI", 11), text_color="#94a3b8")
            info.pack(anchor="w", padx=10)

            summary = CTkLabel(frame, text=item["summary"], font=("Segoe UI", 12), text_color="#cbd5e1", wraplength=700, justify="left")
            summary.pack(anchor="w", padx=10, pady=5)

            link = CTkLabel(frame, text=f"🔗 {item['url']}", font=("Segoe UI", 11), text_color="skyblue", cursor="hand2")
            link.pack(anchor="w", padx=10, pady=(0, 10))
            link.bind("<Button-1>", lambda e, url=item['url']: __import__('webbrowser').open_new(url))
        Last_Loaded_Stock = User_input
    except Exception as e:
        print(f"Error fetching news: {e}")

def clear_scrollable_frame(scroll_frame):
    for widget in scroll_frame.winfo_children():
        widget.destroy()
    global Last_Loaded_Stock
    Last_Loaded_Stock = None  

app = CTk()
app.geometry("1400x800")
app.title("Stock-Project")
set_appearance_mode("dark")
set_default_color_theme("dark-blue")

tabview = CTkTabview(master=app)
tabview.grid(row=0, padx=20, pady=5, sticky="nsew")
tabview.add("Graph")
tabview.add("News")
tabview.set("Graph")
 
#--------------------------------------------------------------------------#

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

tab1 = tabview.tab("Graph")
tab1.grid_rowconfigure(0, weight=1)
tab1.grid_columnconfigure(0, weight=1)
tab1.grid_columnconfigure(1, weight=1)

tab2 = tabview.tab("News")
tab2.grid_rowconfigure(0, weight=1)
tab2.grid_columnconfigure(0, weight=1)
news_scroll_frame = CTkScrollableFrame(master=tab2, fg_color="transparent")
news_scroll_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
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
for i in range(9):
    frame1.grid_rowconfigure(i, weight=0)


#--------------------------------------------------------------------------#

button = CTkButton(master=frame2, text="Graph", command=Stock_Graph)
button.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

News_Button = CTkButton(master=tab2, text="Load News", command=Load_News)
News_Button.grid(row=10, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

Clear_News_Button = CTkButton(master=tab2, text="Clear News", command=lambda: clear_scrollable_frame(news_scroll_frame))
Clear_News_Button.grid(row=11, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

def Pred():
    global Pred_Label
    result = CNN_predict()  
    if Pred_Label:
        Pred_Label.configure(text=result)

Predict = CTkButton(master=frame2, text="Predict", command= Pred) 
Predict.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

Stock_Code_Enter = customtkinter.CTkEntry(master=frame2, placeholder_text="Enter the stock code")
Stock_Code_Enter.grid(row=8,column=0, columnspan=2, padx=10, pady=10, sticky="ew")

def Get_Stock_Code():
    thing = Stock_Code_Enter.get() 
    print(thing) 
    global User_input
    User_input = thing
    Stock_Code_Enter.delete(0, 'end')
    return User_input

Stock_Code_Enter_Button = CTkButton(master=frame2, text="Enter Code", command= Get_Stock_Code) 
Stock_Code_Enter_Button.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

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
