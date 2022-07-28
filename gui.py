from tkinter import END, Tk, Button, Label, Radiobutton, Text, StringVar, Entry, filedialog, IntVar, E, W, N, S, Menu
from PIL.Image import open as pil_open
from PIL import ImageTk
from weather_chart import *
import time
import datetime

def click_double_esc_btn(self):
    window.destroy()

def click_esc_btn(self):
    window.attributes('-fullscreen', False)

def click_f11_btn(self):
    window.attributes('-fullscreen', True)

def click_1_btn(self):
    global data_type
    data_type = "rain"
    text.insert("1.0","AWS 자료를 '강수량'으로 변경합니다.\n")
    window.update()

def click_2_btn(self):
    global data_type
    data_type = "temp"
    text.insert("1.0","AWS 자료를 '기온'으로 변경합니다.\n")
    window.update()

def update_start(self):
    global data_type
    while True:
        try:
            text.delete("1.0","2.0")
            text.insert("1.0","업데이트를 시작합니다.\n")

            window.update()
            print("update start")
            rader()
            window.update()
            print("rader")
            p1, p2 = warn()
            window.update()
            print("warn")
            satellite()
            window.update()
            print("satelite")
            sfc()
            window.update()
            print("sfc")
            aws(data_type=data_type)
            print(f"aws {data_type}")

            image = pil_open("./image/true.png")
            img = image.resize((int(width*rate), int(width*rate)))
            my_img = ImageTk.PhotoImage(img, master=window)
            label_img1.configure(image=my_img)
            window.update()

            image2 = pil_open("./image/day_night.png")
            img2 = image2.resize((int(width * rate), int(width * rate)))
            my_img2 = ImageTk.PhotoImage(img2, master=window)
            label_img2.configure(image=my_img2)
            window.update()

            image3 = pil_open("./image/rader.png")
            img3 = image3.resize((int(width * rate), int(width * rate)))
            my_img3 = ImageTk.PhotoImage(img3, master=window)
            label_img3.configure(image=my_img3)
            window.update()

            image4 = pil_open("./image/sfc3.png")
            img4 = image4.resize((int(width * rate), int(width * (rate))))
            my_img4 = ImageTk.PhotoImage(img4, master=window)
            label_img4.configure(image=my_img4)
            window.update()

            image5 = pil_open("./image/warn.png")
            img5 = image5.resize((int(width * rate), int(width * rate)))
            my_img5 = ImageTk.PhotoImage(img5, master=window)
            label_img5.configure(image=my_img5)
            window.update()

            image6 = pil_open(f"./image/aws_{data_type}.png")
            img6 = image6.resize((int(width * rate), int(width * rate)))
            my_img6 = ImageTk.PhotoImage(img6, master=window)
            label_img6.configure(image=my_img6)
            window.update()

            now = datetime.datetime.now()
            now = f"업데이트 : {now.year}년 {now.month}월 {now.hour}시 {now.minute}분\n\n"

            text.delete("1.0", "end")
            text.insert("1.0",p2)
            text.insert("1.0",p1+"\n\n\n")
            text.insert("1.0",now)
            window.update()
            print(now)
            for i in range(60):
                time.sleep(3)
                window.update()
        except:
            print("Error!")
            #time.sleep(60)

rate = 0.27

window = Tk()
window.title("Weather Chart")
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry(f'{width}x{height}+0+0')
window.bind_all('<F11>', click_f11_btn)
window.bind_all('<Escape>', click_esc_btn)
window.bind_all('<Double-Escape>', click_double_esc_btn)
window.bind_all('<space>', update_start)
window.bind_all('1', click_1_btn)
window.bind_all('2', click_2_btn)
window.configure(bg="black")


# 위성 : 천연색
image = pil_open("./image/true.png")
img = image.resize((int(width*rate), int(width*rate)))
my_img = ImageTk.PhotoImage(img, master=window)
label_img1 = Label(window, image=my_img)
label_img1.grid(column=0, row=0, ipadx=2, ipady=2)
label_img1.configure(bg="black")

# 위성 : 주야간
image2 = pil_open("./image/day_night.png")
img2 = image2.resize((int(width*rate), int(width*rate)))
my_img2 = ImageTk.PhotoImage(img2, master=window)
label_img2 = Label(window, image=my_img2)
label_img2.grid(column=0, row=1, ipadx=2, ipady=2)
label_img2.configure(bg="black")


# 레이더 : 강수
image3 = pil_open("./image/rader.png")
img3 = image3.resize((int(width*rate), int(width*rate)))
my_img3 = ImageTk.PhotoImage(img3, master=window)
label_img3 = Label(window, image=my_img3)
label_img3.grid(column=1, row=0, ipadx=2, ipady=2)
label_img3.configure(bg="black")

# 일기도 : 지상3
image4 = pil_open("./image/sfc3.png")
img4 = image4.resize((int(width*rate), int(width*(rate))))
my_img4 = ImageTk.PhotoImage(img4, master=window)
label_img4 = Label(window, image=my_img4)
label_img4.grid(column=1, row=1, ipadx=2, ipady=2)
label_img4.configure(bg="black")


# 특보 : 현재
image5 = pil_open("./image/warn.png")
img5 = image5.resize((int(width*rate), int(width*rate)))
my_img5 = ImageTk.PhotoImage(img5, master=window)
label_img5 = Label(window, image=my_img5)
label_img5.grid(column=2, row=0, ipadx=2, ipady=2)
label_img5.configure(bg="black")

# aws
global data_type
data_type = "rain"
image6 = pil_open(f"./image/aws_{data_type}.png")
img6 = image6.resize((int(width*rate), int(width*rate)))
my_img6 = ImageTk.PhotoImage(img6, master=window)
label_img6 = Label(window, image=my_img6)
label_img6.grid(column=2, row=1, ipadx=2, ipady=2)
label_img6.configure(bg="black")

text = Text(window, font=('Courier',13),
            relief="raised",  borderwidth=0,width=29)
text.grid(column=3, row=0,rowspan=2, sticky=N+S,ipadx=20)
text.configure(bg="black", foreground="white",
               highlightthickness=0, insertbackground="#FFC400", selectbackground="black", selectforeground="#FFC400")

text.insert("1.0", "Spacebar를 눌러 업데이트를 시작해주세요 :)")

window.attributes('-fullscreen', True)
window.mainloop()