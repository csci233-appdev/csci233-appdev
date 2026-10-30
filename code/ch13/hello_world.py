# This program displays a label with text.
import tkinter

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Display a title.
        self.main_window.title('Hello World (label)')

        # Create a Label widget containing the
        # text 'Hello World!'
        self.label = tkinter.Label(self.main_window, text='Hello World!')

        # Call the Label widget's pack method.
        self.label.pack()

        # Enter the tkinter main loop.
        self.main_window.mainloop()

# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()