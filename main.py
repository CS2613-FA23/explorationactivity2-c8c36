import tkinter as tk
from tkinter import filedialog, simpledialog
from PIL import Image
import numpy as np
import os

BRUSH_SIZE = 16
STYLE = {
   "main_frame": "lightyellow1",
   "canvas_frame": "lightyellow2",
   "control_frame": "lightyellow3",
   "canvas": "black"
}


class App(tk.Tk):
   def __draw_pixel(self, event):
      gray_lvl = self.gray_scale.get()
      x0 = (event.x//BRUSH_SIZE-1*(event.x == 24*BRUSH_SIZE))
      y0 = (event.y//BRUSH_SIZE-1*(event.y == 24*BRUSH_SIZE))
      self.img[y0][x0] = gray_lvl

      x0, y0 = x0*BRUSH_SIZE, y0*BRUSH_SIZE
      x1, y1 = x0+BRUSH_SIZE, y0+BRUSH_SIZE
      
      if gray_lvl == 0:
         gray_lvl = "black"
      elif gray_lvl == 100:
         gray_lvl = "white"
      else:
         gray_lvl = "gray{}".format(gray_lvl) 

      self.canvas.create_rectangle(x0, y0, x1, y1, fill=gray_lvl, outline=gray_lvl, width=0)
   
   def __erase_pixel(self, event):
      x0 = (event.x//BRUSH_SIZE-1*(event.x == 24*BRUSH_SIZE))
      y0 = (event.y//BRUSH_SIZE-1*(event.y == 24*BRUSH_SIZE))
      self.img[y0][x0] = 0.
      x0, y0 = x0*BRUSH_SIZE, y0*BRUSH_SIZE
      x1, y1 = x0+BRUSH_SIZE, y0+BRUSH_SIZE
      self.canvas.create_rectangle(x0, y0, x1, y1, fill="black", outline="black", width=0)

   def __browse_dirs(self):
      self.save_dir = filedialog.askdirectory()
      self.save_path_entry.delete(0, tk.END)
      self.save_path_entry.insert(0, self.save_dir)

   def __save_img(self):
      answer = simpledialog.askstring("Image Name", "Input the name for your image. Leave the space empty for default value", parent=self)
      
      image_name = "image"
      if answer == "":
         i = 0
         while(image_name+str(i) in os.listdir(os.path.join(self.save_dir))):
            i += 1
         image_name = image_name+str(i)
      elif answer is None:
         return
      else:
         image_name = answer
      
      image_name = image_name+".png"
      with Image.fromarray(self.img).convert("L") as im:
         im.save(os.path.join(self.save_dir, image_name))

   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.main_frame = tk.Frame(self, background=STYLE["main_frame"])
      
      self.canvas_frame = tk.Frame(self.main_frame, background=STYLE["canvas_frame"])
      self.control_frame = tk.Frame(self.main_frame, background=STYLE["control_frame"])

      self.canvas = tk.Canvas(self.canvas_frame, width=24*BRUSH_SIZE, height=24*BRUSH_SIZE, background=STYLE["canvas"], highlightthickness=0)
      
      self.save_button = tk.Button(self.control_frame, text="Save Image", command=self.__save_img)
      self.save_path_entry = tk.Entry(self.control_frame, width=50)
      self.save_path_button = tk.Button(self.control_frame, text="Set Save Path", command=self.__browse_dirs)
      self.gray_scale = tk.Scale(self.control_frame, from_=0, to=100, orient="horizontal", label="gray scale", length="60m")
      self.gray_scale.set(50)

      self.save_dir = os.curdir
      self.save_path_entry.insert(0, self.save_dir)
      self.img = np.zeros((24, 24))

   
   def set_geometries(self):
      self.main_frame.pack()
      self.canvas_frame.pack()      
      self.canvas.pack()

      self.control_frame.pack()
      self.gray_scale.pack()
      self.save_path_entry.pack(padx=20)
      self.save_path_button.pack(pady=10)
      self.save_button.pack(padx=10, pady=10)

   def set_binds(self):
      self.canvas.bind("<Button-1>", self.__draw_pixel)
      self.canvas.bind("<B1-Motion>", self.__draw_pixel)

      self.canvas.bind("<Button-3>", self.__erase_pixel)
      self.canvas.bind("<B3-Motion>", self.__erase_pixel)


root = App()
root.title("Test")
root.set_geometries()
root.set_binds()

root.mainloop()