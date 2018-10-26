from tkinter import *
import splain

class cub_spl:
    def __init__(self,master):
        self.b = Button(master, text = "Ok", command= lambda: self.set_num_of_points(master))
        self.e = Entry(master)
        self.b.grid(row = 0, column = 0)
        self.e.grid(row = 0, column = 1) 
    def set_num_of_points(self, master):
            self.x = []
            self.y = []
            num = int(self.e.get())
            for i in range(num):
                ex = Entry(master)
                ex.grid(row = i + 1, column = 1)
                self.x.append(ex)

                ey = Entry(master)
                ey.grid(row = i + 1, column = 2)
                self.y.append(ey)
            self.b1 = Button(master, text = "Get Splain", command= lambda: self.get_splain(master))
            self.b1.grid(row = 8, column = 1)
    def get_splain(self,master):
        file = open("point1.txt", "w")
        for i in range(len(self.x)):
            X = self.x[i].get()
            Y = self.y[i].get()
            file.write(str(X) + ' ' + str(Y) + '\n')
        file.close()
        splain.main()

    
root = Tk()
fb = cub_spl(root)
root.title("Cubic Splain")
root.geometry("300x300")
root.mainloop()