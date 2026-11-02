# This program demonstrates a simple Listbox.
import tkinter


class ListboxExample:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.option_add('*Font', 'Arial 24')
        self.main_window.tk.call('tk', 'scaling', 2.0)

        # Display a title.
        self.main_window.title('Listbox Demo')

        # Create a Listbox widget.
        self.listbox = tkinter.Listbox(self.main_window)
        self.listbox.pack(padx=10, pady=10)

        # Populate the Listbox with the data.
        self.listbox.insert(0, 'Monday')
        self.listbox.insert(1, 'Tuesday')
        self.listbox.insert(2, 'Wednesday')
        self.listbox.insert(3, 'Thursday')
        self.listbox.insert(4, 'Friday')
        self.listbox.insert(5, 'Saturday')
        self.listbox.insert(6, 'Sunday')

        # Start the main loop.
        self.main_window.mainloop()


# Create an instance of the ListboxExample class.
if __name__ == '__main__':
    listbox_example = ListboxExample()
