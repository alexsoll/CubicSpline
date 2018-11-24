from tkinter import *
from tkinter import messagebox
import splain

class cub_spl:
    def __init__(self,master):
        self.b = Button(master, text = "Ok", command= lambda: self.set_num_of_points(master))
        self.update = Button(master, text = "Add one points", command= lambda: self.update_data(master))
        self.e = Entry(master)
        self.l = Label(master, text = "Enter the number of points")
        self.update.place(x = 200, y = 15)
        self.b.place(x = 150, y = 15)
        self.l.grid(row = 1, column = 0)
        self.e.grid(row = 2, column = 0)
    def set_num_of_points(self, master):
            self.x = []
            self.y = []
            self.num = int(self.e.get())
            if (self.num > 8):
                messagebox.showinfo("Warning", "You have entered too much value.")
                return
            self.lbl = Label(master, text = "Enter the point")
            self.lbl.grid(row = 3, column = 0)
            for i in range(self.num):
                ex = Entry(master)
                ex.grid(row = i + 4, column = 0)
                self.x.append(ex)

                ey = Entry(master)
                ey.grid(row = i + 4 , column = 1)
                self.y.append(ey)
            self.b1 = Button(master, text = "Get Splaine", command= lambda: self.get_splain(master))
            self.b1.grid(row = self.num+4+1, column = 1)
    def get_splain(self,master):
        file = open("point1.txt", "w")
        for i in range(len(self.x)):
            X = self.x[i].get()
            Y = self.y[i].get()
            file.write(str(X) + ' ' + str(Y) + '\n')
        file.close()
        splain.main()

    def update_data(self,master):
        if (self.num == 7):
            messagebox.showinfo("Warning", "After entry new point, their number will too much")
            return

        ex = Entry(master)
        ex.grid(row = self.num + 5, column = 0)
        self.x.append(ex)

        ey = Entry(master)
        ey.grid(row = self.num + 5 , column = 1)
        self.y.append(ey)

        self.b1.grid(row = self.num+4+2, column = 1)

        self.num += 1

    
root = Tk()
fb = cub_spl(root)
root.title("Cubic Splaine")
root.geometry("300x300")
root.mainloop()