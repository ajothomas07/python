import threading
import time
import tkinter


class CountdownTimer:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("400x300")
        self.root.config(bg="grey35")
        self.root.title("Countdown Timer")

        self.hrs = 0
        self.min = 0
        self.sec = 0

        self.label1 = tkinter.Label(self.root, font=15, text="Enter the time :", bg="grey45", fg="white")
        self.label1.grid(row=0, column=0, columnspan=2, padx=115, pady=5)
        self.text = tkinter.Entry(self.root, font=0)
        self.text.grid(row=1, column=0, columnspan=2, padx=75, pady=7)
        self.start = tkinter.Button(self.root, font=45, text="Start",command=self.start_thread, bg="green", fg="white")
        self.start.place(x=100, y=105)
        self.stop = tkinter.Button(self.root, font=45, text="Reset",command=self.reset, bg="red", fg="white")
        self.stop.place(x=180, y=105)
        self.pause = tkinter.Button(self.root, font=35, text="pause",command=self.time_pause, bg="grey", fg="white")
        self.pause.place(x=100, y=155)
        self.resume = tkinter.Button(self.root, font=35, text="Resume",command=self.time_resume, bg="green", fg="white")
        self.resume.place(x=180, y=155)
        self.timelabel1=tkinter.Label(self.root, font=('Arial',15),text="Time =00:00:00")
        self.timelabel1.place(x=100, y=74)


        self.root.mainloop()


    def start_thread(self) :
            t = threading.Thread(target=self.start_timer)
            t.start()

    def start_timer(self):
        self.stop_loop=False
        time_split =self.text.get().split(":")
        if len(time_split)==3:
            self.hrs=int(time_split[0])
            self.min=int(time_split[1])
            self.sec=int(time_split[2])
        elif len(time_split)==2:
            self.min = int(time_split[0])
            self.sec = int(time_split[1])

        elif len(time_split)==1:
            self.sec = int(time_split[0])
        else:
            print("Invalid time format")
            return
        self.full_sec = self.hrs*3600+self.min*60+self.sec
        while self.full_sec>0 and not self.stop_loop:
            self.full_sec=self.full_sec-1
            self.min,self.sec=divmod(self.full_sec,60)
            self.hrs, self.min = divmod(self.min, 60)
            self.timelabel1.config(text=f"Time:{self.hrs:02d}:{self.min:02d}:{self.sec:02d}")
            self.root.update()
            time.sleep(1)

        self.root.update()



    def time_pause(self):
            self.pause =True
            self.stop_loop = True
            self.hrs =self.hrs
            self.min = self.min
            self.sec =self.sec
            self.timelabel1.config(text=f"Time:{self.hrs:02d}:{self.min:02d}:{self.sec:02d}")
            self.timelabel1.update()


    def time_resume(self):
            self.pause = False
            self.stop_loop = False
            while self.full_sec >0 and not self.stop_loop:
                self.full_sec = self.full_sec-1
                self.min ,self.sec =divmod(self.full_sec,60)
                self.hrs, self.min = divmod(self.min, 60)
                self.timelabel1.config(text=f"Time:{self.hrs:02d}:{self.min:02d}:{self.sec:02d}")
                self.root.update()
                time.sleep(1)

    def reset(self):
            self.stop_loop =True
            self.timelabel1.config(text="Time =00:00:00")
            self.root.update()

CountdownTimer()
