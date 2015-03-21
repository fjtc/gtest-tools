# Copyright (c) 2015, FJTC
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# * Neither the name of gtest-tool nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
from Tkinter import *
from tkMessageBox import *

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
        self._tools_menu.add_command(label='Generate main.cpp', command = self._do_generate_main)
        self._menubar.add_cascade(label="Tools", menu=self._tools_menu)
        
        self._help_menu = Menu(self._menubar, tearoff=0)
        self._help_menu.add_command(label='About', command = self._do_about)
        self._menubar.add_cascade(label="Help", menu=self._help_menu)

        root.config(menu=self._menubar)
    
    def createUI(self):
        
        self._createMenuBar()
        
        self.grid(column=0, row=0, sticky=(N, W, E, S))

        self._test_name_label = Label(self)
        self._test_name_label['text'] = 'Test name (must be a valid C identifier.)'
        self._test_name_label.grid(column = 0, row = 0, columnspan=3, sticky=(E,W))
        
        self._test_name_entry = Entry(self)
        self._test_name_entry.grid(column = 0, row = 1, columnspan=3, sticky=(E,W))
        
        self._ok_button = Button(self)
        self._ok_button['text'] = 'OK'
        self._ok_button['command'] = self.do_generate_test
        self._ok_button.grid(column = 1, row = 2, sticky=(E,W))
        
        self._cancel_button = Button(self)
        self._cancel_button['text'] = 'Cancel'
        self._cancel_button['command'] = self.quit
        self._cancel_button.grid(column = 2, row = 2, sticky=(E,W))
        
        self._test_status_label = Label(self)
        self._test_status_label['text'] = 'Test name (must be a valid C identifier.)'
        self._test_status_label.grid(column = 0, row = 3, columnspan=3, sticky=(E,W))
        
    def _do_generate_main(self):
        pass
    
    def do_generate_test(self):
        pass

    def _do_about(self):
        showinfo('OK', ('gtestgen 0.1\n' + 
                        'Copyright (c) 2015, FJTC.\n' + 
                        'All rights reserved.\n' +
                        'This software is licensed under Modified BSD License'))
        pass

if __name__ == '__main__':
    root = Tk()
    root.wm_title('gtestgen')
    app = GTestGenGUI(master=root)
    app.mainloop()
    #root.destroy()
        
    