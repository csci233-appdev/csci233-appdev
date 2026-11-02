# This program connects multiple points with a line.
import tkinter


class MyGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.option_add('*Font', 'Arial 24')
        self.main_window.tk.call('tk', 'scaling', 2.0)
        self.main_window.title('Canvas multi-line Demo')

        # Create the Canvas widget.
        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)

        # Draw a line connecting multiple points.
        self.canvas.create_line(10, 10, 189, 10, 100, 189, 10, 10)

        # Pack the canvas.
        self.canvas.pack()

        # Start the mainloop.
        self.main_window.mainloop()


# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()
