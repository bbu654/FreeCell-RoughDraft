import tkinter as tk, time
class StopWatch(tk.Frame):

    @classmethod
    def main(cls):
        tk.NoDefaultRoot()
        root = tk.Tk()
        root.title('Stop Watch')
        root.resizable(True, False)
        root.grid_columnconfigure(0, weight=1)
        padding = dict(padx = 5, pady = 5)
        widget = StopWatch(root, **padding)
        widget.grid(sticky=tk.NSEW, **padding)
        
        root.mainloop()

    def __tick(self, time1=''):
        """Get current time from OS"""
        time2 = time.strftime('%H:%M:%S')
        if time2 != time1:
            time1 = time2
            self.__clock.config(text = time2)
        self.__clock.after(200, self.__tick)

    def __init__(self, master=None, cnf={},**kw):
        padding = dict(padx=kw.pop('padx', 5),pady=kw.pop('pady', 5))
        super().__init__(master, cnf, **kw)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.__total = 0
        self.__label  = tk.Label(self,text='Total Time:', font=('arial', 12, 'bold'), bg='yellow')
        self.__time   = tk.StringVar(self, '0.000000')
        self.__display= tk.Label(self, textvariable = self.__time, font=('arial', 12, 'bold'), bg='yellow')
        self.__clock  = tk.Label(self, font=('arial', 20, 'bold'), bg='yellow')        
        #self.__clock.pack(fill='both',expand=1) Apparently U cant pack and **padding
        self.__button = tk.Button(self, text='Start', command=self.__click, font=('arial', 12, 'bold'), bg='yellow')
        self.__label.grid(row=0,column=0,sticky=tk.E,**padding)
        self.__display.grid(row=0,column=1,sticky=tk.EW,**padding)
        self.__button.grid(row=1,column=0,columnspan=2,sticky=tk.NSEW,**padding)
        self.__clock.grid(row=2,column=0,columnspan=2,sticky=tk.NSEW,**padding)
        self.__tick()

    def __click(self):
        if self.__button['text'] == 'Start':
            self.__button['text'] = 'Stop'
            self.__start = time.time()
            self.__counter = self.after_idle(self.__update)
        else:
            self.__button['text'] = 'Start'
            self.after_cancel(self.__counter)


    def __update(self):
        now = time.time()
        diff = now - self.__start
        self.__start = now
        self.__total += diff
        self.__time.set('{:.6f}'.format(self.__total))
        self.__counter = self.after_idle(self.__update)


if __name__ == '__main__':
    print(f'before StopWatch.main()')
    StopWatch.main()
    print(f' after StopWatch.main()')