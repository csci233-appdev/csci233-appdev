# This program displays two labels with text.
import tkinter


class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()
        self.main_window.option_add('*Font', 'Arial 24')
        self.main_window.tk.call('tk', 'scaling', 2.0)

        # Display a title.
        self.main_window.title('Hello World (label)')

        # Create two Label widgets.
        self.label1 = tkinter.Label(self.main_window,
                                    relief='sunken',
                                    borderwidth=5,
                                    text='Hello World!')
        self.label2 = tkinter.Label(self.main_window,
                                    relief='raised',
                                    borderwidth=10,
                                    text='This is my GUI program.')

        # Call both Label widgets' pack method.
        self.label1.pack()
        self.label2.pack()

        # Enter the tkinter main loop.
        self.main_window.mainloop()


# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()
