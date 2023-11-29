from pygame import mixer
from tkinter.ttk import *
from tkinter import *
from datetime import datetime
import time
from time import sleep
from PIL import ImageTk, Image
from threading import Thread

#The GUI tkinter
clock = Tk()

clock.title("Motunrayo's clock")
clock.geometry("350x180")
clock.configure(bg='white')

#frame
fram_lin = Frame(clock, width=450, height=5, bg='blue')
fram_lin.grid(row=0, column=0)

#frame body
fram_body = Frame(clock, width=450, height=290, bg='white')
fram_body.grid(row=1, column=0)

#image icon
img = Image.open('clock.png')
img.resize((10, 10))
img = ImageTk.PhotoImage(img)
enb_img = Label(fram_body, height=125, image=img, bg='white')
enb_img.place(x=5, y=0)

#Input of variables
time_format=Label(fram_body, text= "Time in 24hrs format!", fg="black",bg="white",font="Timeroman 15 bold", height=1).place(x=75,y=140)
setYourAlarm = Label(fram_body,text = "Wake up time!",fg="black",relief = "solid",font=("Timeroman 12 bold")).place(x=14.5, y=44)


#setting the width and height of the time:
hour= Label(fram_body,text = 'hour',bg = "white",width = 5, font=('timeroman 10 bold')).place(x=135,y=20)
c_hour = Combobox(fram_body, width=2, font=('timeroman 10 bold'))
c_hour['values'] = ('00','01','02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19','20','21','22','23','24')
c_hour.current(0)
c_hour.place(x=135, y=40)

min= Label(fram_body,text = 'min',bg = "white",width = 5, font=('timeroman 10 bold')).place(x=175,y=20)
c_min = Combobox(fram_body, width=2, font=('timeroman 10 bold'))
c_min['values'] = ('00','01','02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19','20','21','22','23','24', '25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59')
c_min.current(0)
c_min.place(x=180, y=40)

sec = Label(fram_body,text = 'sec',bg = "white",width = 5, font=('timeroman 10 bold')).place(x=220,y=20)
c_sec = Combobox(fram_body, width=2, font=('timeroman 10 bold'))
c_sec['values'] = ('00','01','02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19','20','21','22','23','24', '25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59')
c_sec.current(0)
c_sec.place(x=230, y=40)




#Function to activate alarm
def activate_alarm():
    t = Thread(target=Alarm)
    t.start()
    
#Activation button
selected = IntVar()
radio_bu = Radiobutton(fram_body, font=('timeroman', 10, 'bold'), value=1, text='Activate', bg='white', variable=selected, command=activate_alarm)
radio_bu.place(x=125, y=95)

#Function to deactivate alarm
def Deactivate_alarm():
    print('Deactived alarm: ', selected.get())
    mixer.music.stop()   
   
def Ring_alarm():
    mixer.music.load('Alarmtone.mp3')
    mixer.music.play()
    selected.set(0)
 #Deactivation button
    radio_bu_2 = Radiobutton(fram_body, font=('timeroman', 10, 'bold'), value=2, text='Deactivate', bg='white', variable=selected, command=Deactivate_alarm)
    radio_bu_2.place(x=180, y=95) 

    
  # Creating a function for time.
def Alarm(): 
    while True: 
        control = selected.get()
        print(control)
        alarm_hur = c_hour.get()
        alarm_min = c_min.get()
        alarm_sec = c_sec.get()
        current_time = datetime.now() 
        hour = current_time.strftime("%H")
        min = current_time.strftime("%M") 
        sec = current_time.strftime("%S")
    
        if control ==1:
            if alarm_hur == hour:
                if alarm_min == min:
                    if alarm_sec == sec:
                        print("The time is now!")
                        Ring_alarm() 
        sleep(1)
                        
        

mixer.init()


clock.mainloop()