# This program displays an empty window.
import customtkinter

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = customtkinter.CTk()

        # Enter the tkinter main loop.
        self.main_window.mainloop()

# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()