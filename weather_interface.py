from customtkinter import *
from PIL import Image,ImageTk
import weather as wt
from datetime import datetime

######## current time

time=datetime.now().strftime("%I:%M %p")

######## setting theme of the program
set_appearance_mode("light")
set_default_color_theme("blue")
root=CTk()
root.title("Weather App ;)")
root.geometry("800x550")
root.resizable(False,False)

##### weather report icon on top
weatherreprticon=Image.open("weather_forecast_env\\weather_icon.webp")
weatherreprticon=CTkImage(weatherreprticon,size=(230,170))
img10=CTkLabel(master=root,image=weatherreprticon,text="").place(x=550,y=20)



### title box
image2=Image.open("weather_forecast_env\\neumorphic-rectangle-button-free-png.webp")
img2=CTkImage(image2,size=(450,140))
label2=CTkLabel(master=root,image=img2,text="Weather Dude ;)",
                font=("Comic Sans MS",35,"bold"),
                text_color="white").place(x=100,y=5)

######## weather icon

img5=Image.open("weather_forecast_env\\4571485.png")
img5=CTkImage(img5,size=(150,150))
image5=CTkLabel(master=root,image=img5,text="").place(x=150,y=270)



####### weather report temp, time, main
label=CTkLabel(master=root,text="None",
               font=('San Francisco',50,"bold"),
               text_color="#e36a62")
label.place(x=350,y=300)
label7=CTkLabel(master=root,text="None",font=('San Francisco',20,"bold"),
                text_color="black")
label7.place(x=350,y=360)


###### location entry
###### location displaying label
label2=CTkLabel(master=root,text="",font=("Comic Sans MS",20,"bold"),
                height=150,
                width=400,
                fg_color=("#b5e1f5",""),
                corner_radius=150)
label2.place(x=320,y=140) 

######entry box
def get_entry():
    wt.city=entry.get()
    wt.weather_details()
    if(wt.output=="city not found"):
        label2.configure(text=wt.output)
        label3.configure(text="NONE          NONE                  NONE             NONE             NONE")
    else:
        label2.configure(text=f"The location you've entered is :\n{wt.city} of {wt.country}\n lat:{wt.lat}\n lon:{wt.lon} ")
        label3.configure(text=f"{wt.windspeed}km/h       {wt.description}         {wt.visibility}m         {wt.humidity}%             {wt.feelslike}°")
        label.configure(text=f"{wt.temp}°")
    
    label7.configure(text=f"{wt.main}\n Current time:{time}")
    
##### clearing the search box function def
def clear():
    entry.delete(0,END)

####### entry box
entry=CTkEntry(master=root,
               width=200,height=50,corner_radius=30,
               placeholder_text="Enter City",
               font=("Comic Sans MS",24,"bold"),
               text_color="white",
               fg_color=("#3383c4","black"),
               placeholder_text_color="white")
entry.place(x=30,y=150)
##### locate icon
img6=Image.open("weather_forecast_env\\pin-icon-sign-symbol-design-free-png.webp")
img6=CTkImage(img6,size=(35,55))
label6=CTkLabel(master=root,image=img6,text="")
label6.place(x=250,y=215)

#####submit and clear buttons
submit=CTkButton(master=root,command=get_entry,
                 text="OK",
                 font=("Comic Sans MS",13,"bold"),
                 width=55,
                 height=25,
                 corner_radius=10).place(x=240,y=150)

clear_button=CTkButton(master=root,command=clear,
                       text="Clear",
                       font=("Comic Sans MS",13,"bold"),
                       width=30,
                       height=25,
                       corner_radius=10).place(x=240,y=175)


####locate me button
def locate():
    info=wt.locateme()  
    label2.configure(text=info)
    wt.locateme()
    wt.weather_details()
    if(wt.output!="city not found"):
        label3.configure(text=f"{wt.windspeed}km/h         {wt.description}           {wt.visibility}m             {wt.humidity}%            {wt.feelslike}°")
        label.configure(text=f"{wt.temp}°")
    label7.configure(text=f"{wt.main}\nCurrent time:{time}")
    
button1=CTkButton(master=root,command=locate,text="Locate Me",
                  font=("Comic Sans MS",24,"bold")
                  ,width=200,height=50,corner_radius=30).place(x=30,y=220)



####### weather report box
image4=Image.open("weather_forecast_env\\rectangular_box.jpeg")
image4=CTkImage(image4,size=(850,95))
label3=CTkLabel(master=root,image=image4,text=f"NONE          NONE                  NONE             NONE             NONE",
                corner_radius=90,
                height=90,
                font=("Comic Sans MS",20,"bold"))
label3.place(x=-80,y=460)

##### titles for weather report
templabel=CTkLabel(master=root,text="Wind            Description             Visibility          Humidity       feels like",
                   font=("Comic Sans MS",20,"bold"),
                   fg_color=("#8fc9f7","#8fc9f7"),
                   height=50,
                   width=570,
                   corner_radius=40).place(x=-15,y=417)


root.mainloop()

