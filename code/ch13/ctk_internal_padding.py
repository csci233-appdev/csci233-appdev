# This program demonstrates internal padding.
import customtkinter

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = customtkinter.CTk()

        # Display a title.
        self.main_window.title('Hello World (label)')

        # Create two Label widgets with solid borders.
        #
        # Note: there can/will be differences in parameter names, for example
        # borderwidth is border_width in CTk widgets
        #
        # Note: don't think relief is supported in a CTkLabel, would need to fall
        # back to plain tk Label if wanted that? But probably shouldn't and should rely
        # on using customtkinter appearance settings properly to maintain a style/appearance
        self.label1 = customtkinter.CTkLabel(self.main_window,
                                    text='Hello World!',
                                    border_width=5)
        self.label2 = customtkinter.CTkLabel(self.main_window,
                                    text='This is my GUI program.',
                                    border_width=5)

        # Display the Labels with 20 pixels of horizontal
        # and vertical internal padding.
        self.label1.pack(ipadx=20, ipady=20)
        self.label2.pack(ipadx=20, ipady=20)

        # Enter the tkinter main loop.
        self.main_window.mainloop()

# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()