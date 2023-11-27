1. Which package/library did you select?

[Tkinter](https://docs.python.org/3/library/tkinter.html)

2. What is the package/library?

Tkinter is a standard library that provides a simple, yet effective way to build\
simple interfaces. They may not be aesthetically pleasing, but they can serve as a way\
to very quickly come up with a functional interface for a program.\
\
The library is actually just a pythonic interface/wrapper built on top of a Tcl interpreter [[ref]]((https://docs.python.org/3/library/tkinter.html)).\
When you instialize a Tk with
```
import tkinter as tk

root = tk.Tk()
```
* You create your main window that will contain widgets, this window has its own Tcl interpreter,\
and it has its own event loop which is constantly running in the background over the event queue. [[ref]](https://docs.python.org/3/library/tkinter.html#important-tk-concepts).
* The widgets in tkinter have very strict hierarchy, where the parent widgets usually control geometry of their "slave widgets".
* The widgets themselves are the things you see. Buttons, Labels, Canvases, Frames, etc. [[full list]](https://coderslegacy.com/python/list-of-tkinter-widgets/)
* Each widget can have a bind to it, where it will execute a certain Pythonic script/function on a specified event.\
For example this program should print a message in console after pressing a left mouse button on the blue label "Click me":
    ```
    import tkinter as tk
    
    def display(event):
        print("Hello from the callback!")
    
    root = tk.Tk()
    label = tk.Label(root, text="Click me", background="blue")
    label.pack()
    label.bind("<Button-1>")
    root.mainloop()
    ```
Note: the widget must be first displayed by any geometry manager before the `.bind`.[[ref]](https://python-course.eu/tkinter/events-and-binds-in-tkinter.php)

> ### My case (you can track everything said below in the code)

After setting up the boiler plate, I begin constructing the main app class. I have chosen this to be an object,\
since a lot of the things require their own local scope, as well as bits and pieces from other widgets.\

The class have callback functions on top. These callback functions are bound to widgets and are called by their respective widgets.
After callbacks goes the `__init__` method, where the parental class initialized with super, and the hierarchical assignment begins:
* the main frame
    * the canvas frame
        * the canvas widget
    * the control frame
        * the save button widget
        * the save path entry widget
        * the save path button widget
        * the gray scale widget

Some additional assignment is done (path, and the hidden image tracker)

After the initialization is complete, the geometry is initialized using a very powerful `.pack` method.\
It is powerful since it automatically calculates necessary geometry to place the objects according to the\
established hierarchy between them, where child widgets go into parental widgets, and the parental widgets\
are placed well relative to each other. [[ref to packer]](https://docs.python.org/3/library/tkinter.html#the-packer)

After the initialization, and packing (displaying), is done, the callbacks are binded to canvas.

This is a three step process initialization. Yes, it can be done solely in `__init__`,\
but it would not look as pretty...

The same sequence of steps are followed in here, and the mainloop is initialized:
```
root = App()
root.title("EA2")
root.set_geometries()
root.set_binds()

root.mainloop()
```

3. What are the functionalities of the package/library?

Usable, lightweight, okay-looking GUIs can be created using this library.\
The library has all the necessary basic widgets for simple operations.\
Plus, graphics can be achievedusing turtle library and the canvas widget [[example here]](https://compucademy.net/python-turtle-graphics-and-tkinter-gui-programming/)

4. When was it created?

The Python interface `tkinter` was included by default with the first release of Python in 1991.\
The Tcl (Tool Command Language) standalone scripting language first appeared in 1988 [[ref]](https://en.wikipedia.org/wiki/Tcl). \
Initially, it was embedded into C applications

5. Why did you select this package/library?

I have chosen this language, since creating a GUI is an essential part of a viable program...\
However, most options for creating some kind of GUI are overly complicated for a simple act of pressing one button in the middle of a screen to print a "Hello World" in console.

6. How did learning the package/library influence your learning of the language?

There was nothing even a little bit new related to the Python language.

7. How was your overall experience with the package/library?
* When would you recommend this package/library to someone?

Do you need a GUI? Do you need a simple GUI? Do you want to spend only a day on the GUI?\
If all third questions were answered with a yes, then this library must be used.\
There is a reason why it is included in the default package.

* Would you continue using this package/library? Why or why not?

Yes, because it is simple and effective in making a GUI for a simple demonstration.\
Additionally, it can be extended using [`tkinter.tix`](https://docs.python.org/3/library/tkinter.tix.html) and [`tkinter.ttk`](https://docs.python.org/3/library/tkinter.ttk.html) for a pretier design.