# This program displays two labels with text.
import customtkinter

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = customtkinter.CTk()

        # Display a title.
        self.main_window.title('Hello World (label)')

        # Create two Label widgets.
        self.label1 = customtkinter.CTkLabel(self.main_window, text='Hello World!')
        self.label2 = customtkinter.CTkLabel(self.main_window, text='This is my GUI program.')

        # Call both Label widgets' pack method.
        self.label1.pack()
        self.label2.pack()

        # Enter the tkinter main loop.
        self.main_window.mainloop()

# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()