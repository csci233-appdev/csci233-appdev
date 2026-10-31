# This program creates labels in two different frames.
import customtkinter

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = customtkinter.CTk()

        # Display a title.
        self.main_window.title('Hello World (label)')

        # Display a title.
        self.main_window.title('Frame Demo')

        # Create two frames, one for the top of the
        # window, and one for the bottom.
        self.top_frame = customtkinter.CTkFrame(self.main_window)
        self.bottom_frame = customtkinter.CTkFrame(self.main_window)

        # Create three Label widgets for the
        # top frame.
        self.label1 = customtkinter.CTkLabel(self.top_frame, text='Winken')
        self.label2 = customtkinter.CTkLabel(self.top_frame, text='Blinken')
        self.label3 = customtkinter.CTkLabel(self.top_frame, text='Nod')

        # Pack the labels that are in the top frame.
        # Use the side='top' argument to stack them
        # one on top of the other.
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')

        # Create three Label widgets for the
        # bottom frame.
        self.label4 = customtkinter.CTkLabel(self.bottom_frame, text='Winken')
        self.label5 = customtkinter.CTkLabel(self.bottom_frame, text='Blinken')
        self.label6 = customtkinter.CTkLabel(self.bottom_frame, text='Nod')

        # Pack the labels that are in the bottom frame.
        # Use the side='left' argument to arrange them
        # horizontally from the left of the frame.
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        # Yes, we have to pack the frames too!
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop.
        self.main_window.mainloop()

# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()                           