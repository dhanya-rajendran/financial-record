import tkinter
from tkinter import ttk

def enter_data():
    publisher =  title_combobox.get()
    subject = subject_name_entry.get()
    body = body_name_entry.get()
    print("Publisher:", publisher)
    print("Subject:", subject)
    print("Body:", body)
    print("*-----------------------------------*")


window = tkinter.Tk()
window.title("Finance Teqfire")
frame = tkinter.Frame(window)
frame.pack()

user_info_frame = tkinter.LabelFrame(frame, text="Finance Teqfire")
user_info_frame.grid(row= 0,column= 0 , padx=150, pady=150)

title_label =tkinter.Label(user_info_frame,text="Publisher")
title_label.grid(row=0, column=0)
title_combobox = ttk.Combobox(user_info_frame, values=["2X2Network", "Aderbid", "AdExpertsMedia", "Adzesto", "AxeiteMediaLLC", "BrowserTech", "Coinis", "DigitalFuture", "Doxaclick", "Exmarketplace", "FaceBase", "InternetTraffic", "LokiDigital", "MetaSearch1", "MetroDealsLLC",
                              "MobileCloud", "Mobco", "MobiFun", "MonadSearch", "Netstar", "NavigateLLC", "O2Rintelligence", "PrimeRollSearch", "Pragmati", "Phonder", "Qovolta", "QuexlePty", "RichAds", "Skyter", "TrafficGuru", "Typcom", "Upperate", "Winkleads", "ZephyrOne", "ZikMedia"])

subject_name_label = tkinter.Label(user_info_frame,text="Subject")
subject_name_label.grid(row=1,column=0)

body_name_label = tkinter.Label(user_info_frame, text="Body")
body_name_label.grid(row=2,column=0)

title_combobox.grid(row=0,column=1)
subject_name_entry =tkinter.Entry(user_info_frame)
subject_name_entry.grid(row=1,column=1)
body_name_entry = tkinter.Entry(user_info_frame)
body_name_entry.grid(row=2,column=1)

#button
button = tkinter.Button(user_info_frame, text="submit", command=enter_data)
button.grid(row= 3, column=1 , sticky="news", padx=20, pady=20)
window.mainloop()


