from Tkinter import *


class GTestGenGUI(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createUI()
    
    def _createMenuBar(self):
      
        self._menubar = Menu(self)
                
        self._file_menu = Menu(self._menubar, tearoff=0)
        self._file_menu.add_command(label='Exit', command = self.quit )
        self._menubar.add_cascade(label="File", menu=self._file_menu)
        
        self._tools_menu = Menu(self._menubar, tearoff=0)
        self._tools_menu.add_command(label='Generate main.cpp', command = self.quit )
        self._menubar.add_cascade(label="Tools", menu=self._tools_menu)
        
        self._menubar.add_command(label="About")

        root.config(menu=self._menubar)
    
    def createUI(self):
        
        self._createMenuBar()
        
        self.grid(column=0, row=0, sticky=(N, W, E, S))
        
        self._test_name_label = Label(self)
        self._test_name_label['text'] = 'Test name (must be a valid C identifier.)'
        self._test_name_label.grid(column = 0, row = 0, columnspan=3, sticky=(E,W))
        
        self._test_name = Entry(self)
        self._test_name.grid(column = 0, row = 1, columnspan=3, sticky=(E,W))
        
        self._ok_button = Button(self)
        self._ok_button['text'] = 'OK'
        self._ok_button.grid(column = 1, row = 2, sticky=(E,W))
        
        self._cancel_button = Button(self)
        self._cancel_button['text'] = 'Cancel'
        self._cancel_button['command'] = self.quit
        self._cancel_button.grid(column = 2, row = 2, sticky=(E,W))

if __name__ == '__main__':
    root = Tk()
    app = GTestGenGUI(master=root)
    app.mainloop()
    root.destroy()
        
    