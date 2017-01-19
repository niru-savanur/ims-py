'''
Created on Jan 16, 2017

@author: gustavo
'''
import threading
import time
import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Viewer(tk.Frame):
    '''
    classdocs
    '''    
    def __init__(self, master):
        '''
        Constructor
        '''        
        tk.Frame.__init__(self, master)
        
        self.master = master        
        self.loop = False        
        self.fig = Figure(figsize=(30/3,22.5/3))
        #ax = fig.add_subplot(111, projection='polar')
        self.ax = self.fig.add_subplot(111)
         
        # a tk.DrawingArea
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
    def draw_img(self, img_path):
        img = mpimg.imread(img_path)
        imgplot = self.ax.imshow(img, aspect='auto')
        self.__fit_to_roi()
        
        
    def __fit_to_roi(self):
        plt.ylim(ymin=self.roi["ymin"],ymax=self.roi["ymax"])
        plt.xlim(xmin=self.roi["xmin"],xmax=self.roi["xmax"])    
        
     
    def set_roi(self, roi): 
        self.roi = roi
     
    def plot(self, *args, **kwargs):
        self.ax.plot(*args, **kwargs)
        self.__fit_to_roi()
            
    def save_background(self):
        self.canvas.show()
        self.background = self.fig.canvas.copy_from_bbox(self.ax.bbox)
                

if __name__ == "__main__":
    main = tk.Tk()
    main.wm_title("IMS Viewer")
    # Code to add widgets will go here...
    Viewer(main).pack()#(side="top", fill="both", expand="True")
    
    tk.mainloop()
        