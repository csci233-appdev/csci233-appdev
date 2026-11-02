# This program demonstrates external padding.
import tkinter


class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()
        self.main_window.option_add('*Font', 'Arial 24')
        self.main_window.tk.call('tk', 'scaling', 2.0)

        # Display a title.
        self.main_window.title('Hello World (label)')

        # Create two Label widgets with solid borders.
        self.label1 = tkinter.Label(self.main_window,
                                    text='Hello World!',
                                    borderwidth=5,
                                    relief='solid')
        self.label2 = tkinter.Label(self.main_window,
                                    text='This is my GUI program.',
                                    borderwidth=5,
                                    relief='solid')

        # Display the Labels with 20 pixels of horizontal
        # and vertical external padding.
        self.label1.pack(ipadx=20, ipady=20, padx=20, pady=20)
        self.label2.pack(ipadx=20, ipady=20, padx=20, pady=20)

        # Enter the tkinter main loop.
        self.main_window.mainloop()


# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()
