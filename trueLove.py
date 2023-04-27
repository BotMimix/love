import tkinter as tk
from tkinter import PhotoImage
import datetime

class TimerWidget(tk.Label):
    def __init__(self, master=None, **kwargs):
        tk.Label.__init__(self, master, **kwargs)
        self.start_time = datetime.datetime(2023, 4, 27, 18, 10, 0)

    def update(self):
        time_passed = datetime.datetime.now() - self.start_time
        hours, remainder = divmod(time_passed.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.config(text=f"{time_passed.days} days, {hours:02d}:{minutes:02d}:{seconds:02d}")
        self.after(1000, self.update)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("<3 MP <3")

    # Create a frame to hold the image and timer
    frame = tk.Frame(root)
    frame.pack()

    # Load the image
    img = PhotoImage(file="iLoveYou.png")
    img = img.subsample(2)

    # Create a label to display the image
    img_label = tk.Label(frame, image=img)
    img_label.pack()

    # Create the timer widget
    timer = TimerWidget(frame, font=("Mono Sans", 36), fg="purple")
    timer.pack(padx=20, pady=20)
    timer.update()

    root.mainloop()
