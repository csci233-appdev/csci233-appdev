# This program demonstrates external padding.
import customtkinter

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = customtkinter.CTk()

        # Display a title.
        self.main_window.title('Hello World (label)')
        
        # Create two Label widgets with solid borders.
        self.label1 = customtkinter.CTkLabel(self.main_window,
                                             text='Hello World!',
                                             border_width=5)
        self.label2 = customtkinter.CTkLabel(self.main_window,
                                             text='This is my GUI program.',
                                             border_width=5)

        # Display the Labels with 20 pixels of horizontal
        # and vertical external padding.
        self.label1.pack(ipadx=20, ipady=20, padx=20, pady=20)
        self.label2.pack(ipadx=20, ipady=20, padx=20, pady=20)

        # Enter the tkinter main loop.
        self.main_window.mainloop()

# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()