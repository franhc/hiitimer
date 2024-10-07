from tkinter import Label, Scale, Tk

MAX_SECONDS_INTERVAL = 600 
MAX_SECONDS_PAUSE = 60
HORIZONTAL = 'horizontal'

def main():
    
    root = Tk()

    interval_scale = Scale(root, from_=5, to=MAX_SECONDS_INTERVAL, length=300, 
                            tickinterval=60, resolution=5, 
                            label="Interval", orient=HORIZONTAL)
    interval_scale.pack()
    
    pause_scale = Scale(root, from_=0, to=MAX_SECONDS_PAUSE, length=300, 
                            tickinterval=10, resolution=1, 
                            label="Pause", orient=HORIZONTAL)
    pause_scale.pack()
    
    root.mainloop()

if __name__ == "__main__":
    main()
