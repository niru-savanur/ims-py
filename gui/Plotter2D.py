'''
Created on Dec 25, 2017

@author: gustavo
'''
import tkinter as tk
import matplotlib.image as mpimg
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Plotter2D(tk.Frame):
    def __init__(self, master, cb=None):
        '''
        Constructor
        '''        
        tk.Frame.__init__(self, master)
        
        self.master = master
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
         
        # a tk.DrawingArea
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
    def plot(self, *args, **kwargs):
        self.available_lines = self.total_lines - self.fixed_lines - self.used_lines

        if self.available_lines > 0:
#             print("Updating line ")
            line_idx = (self.fixed_lines + self.used_lines)            
            self.__update_plot_data( *args, line_idx=line_idx)
            self.update_style(line_idx, **kwargs)
            
        else:
            self.ax.plot(*args, **kwargs)            
            self.update_style(line_idx="last", **kwargs)
            self.total_lines = len(self.ax.get_lines())     
        
        
        