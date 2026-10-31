# This program demonstrates a Button widget.
# When the user clicks the Button, an
# info dialog box is displayed.
import customtkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = customtkinter.CTk()

        # Display a title.
        self.main_window.title('Button Demo')

        # Create a Button widget. The text 'Click Me!'
        # should appear on the face of the Button. The
        # do_something method should be executed when
        # the user clicks the Button.
        self.my_button = customtkinter.CTkButton(self.main_window,
                                        text='Click Me!',
                                        command=self.do_something)

        # Pack the Button.
        self.my_button.pack()

        # Enter the customtkinter main loop.
        self.main_window.mainloop()

    # The do_something method is a callback function
    # for the Button widget.
    #
    # Note: The base customtkinter doesn't have a messagebox.  There are some additional
    # python packages that seem to add that we could try, but just fall back to the
    # basic message box for now
    def do_something(self):
        # Display an info dialog box.
        tkinter.messagebox.showinfo('Response', 'Thanks for clicking the button.')

# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()