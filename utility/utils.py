import tkinter as tk


class EntryWithPlaceholder(tk.Entry):
    """
    Custom entry widget with a placeholder.

    This class inherits from `tk.Entry` and adds a placeholder functionality to the entry widget. It displays a
    placeholder text when the widget is empty and loses focus, then removes the placeholder text when the widget gains
    focus or receives user input.

    :param master: The parent widget.
    :param placeholder: The placeholder text to display.
    :param color: The color of the placeholder text.
    """

    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', **kwargs):
        """
        Initialize the EntryWithPlaceholder widget.

        :param master: The parent widget.
        :param placeholder: The placeholder text to display when the widget is empty.
        :param color: The color of the placeholder text.
        """
        super().__init__(master, **kwargs)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']


        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()