import tkinter as tk
import customtkinter as ctk

class App(): 
    def __init__(self):
        #general settings application
        ctk.set_appearance_mode('System')
        self._app = ctk.CTk()
        self._app.geometry('350x450')
        self._app.resizable(False, False)
        self._app.title('Калькуляктер!')

        #num buttons
        but1 = self.__create_button('1', self.__button_1, 0.2, 0.4)
        but2 = ctk.CTkButton(master= self._app, text='2', height=40, width=40, command=self.__button_2)
        but2.place(relx=0.35,rely=0.4,anchor=tk.CENTER)
        but3 = ctk.CTkButton(master= self._app, text='3', height=40, width=40, command=self.__button_3)
        but3.place(relx=0.5,rely=0.4,anchor=tk.CENTER)
        but4 = ctk.CTkButton(master= self._app, text='4', height=40, width=40, command=self.__button_4)
        but4.place(relx=0.2,rely=0.5,anchor=tk.CENTER)
        but5 = ctk.CTkButton(master= self._app, text='5', height=40, width=40, command=self.__button_5)
        but5.place(relx=0.35,rely=0.5,anchor=tk.CENTER)
        but6 = ctk.CTkButton(master= self._app, text='6', height=40, width=40, command=self.__button_6)
        but6.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        but7 = ctk.CTkButton(master= self._app, text='7', height=40, width=40, command=self.__button_7)
        but7.place(relx=0.2,rely=0.6,anchor=tk.CENTER)
        but8 = ctk.CTkButton(master= self._app, text='8', height=40, width=40, command=self.__button_8)
        but8.place(relx=0.35,rely=0.6,anchor=tk.CENTER)
        but9 = ctk.CTkButton(master= self._app, text='9', height=40, width=40, command=self.__button_9)
        but9.place(relx=0.5,rely=0.6,anchor=tk.CENTER)
        but0 = ctk.CTkButton(master= self._app, text='0', height=40, width=40, command=self.__button_0)
        but0.place(relx=0.35,rely=0.7,anchor=tk.CENTER)

        #operation buttons
        but_plus = ctk.CTkButton(master=self._app,text='+', height=40, width=40, command=self.__button_plus)
        but_plus.place(relx=0.8, rely=0.4, anchor=tk.CENTER)
        but_minus = ctk.CTkButton(master=self._app,text='-', height=40, width=40, command=self.__button_minus)
        but_minus.place(relx=0.8, rely=0.5, anchor=tk.CENTER)
        but_multiply = ctk.CTkButton(master=self._app,text='*', height=40, width=40, command=self.__button_multiply)
        but_multiply.place(relx=0.8, rely=0.6, anchor=tk.CENTER)
        but_divide = ctk.CTkButton(master=self._app,text='/', height=40, width=40, command=self.__button_divide)
        but_divide.place(relx=0.8, rely=0.7, anchor=tk.CENTER)
        but_result = ctk.CTkButton(master=self._app,text='=', height=40, width=40, command=self.__button_result)
        but_result.place(relx=0.8, rely=0.85, anchor=tk.CENTER)

        #string output information
        self.output_panel = ctk.CTkTextbox(master=self._app, width=200, height=10) #state=tk.DISABLED чтобы заблокировать поле ввода пользователю
        self.output_panel.place(relx = 0.5, rely = 0.1, anchor = tk.CENTER)
        self._output_string = ''

        #bottom label
        info_label = ctk.CTkLabel(self._app, text='Сделал Никита старший.', text_color='Blue')
        info_label.place(relx=0.4, rely=0.85, anchor=tk.CENTER)

        self._app.mainloop()

    #function button-click reaction
    def __button_1(self):
        self._output_string += '1'
        self.output_panel.delete('0.0', tk.END)
        self.output_panel.insert('0.0', self._output_string)
    def __button_2(self):
        self._output_string += '2'
        self.output_panel.delete('0.0', tk.END)
        self.output_panel.insert('0.0', self._output_string)
    def __button_3(self):
        self._output_string += '3'
        self.output_panel.delete('0.0', tk.END)
        self.output_panel.insert('0.0', self._output_string)
    def __button_4(self):
        self._output_string += '4'
        self.output_panel.delete('0.0', tk.END)
        self.output_panel.insert('0.0', self._output_string)
    def __button_5(self):
        self._output_string += '5'
        self.output_panel.delete('0.0', tk.END)
        self.output_panel.insert('0.0', self._output_string)
    def __button_6(self):
        self._output_string += '6'
        self.output_panel.delete('0.0', tk.END)
        self.output_panel.insert('0.0', self._output_string)
    def __button_7(self):
        self._output_string += '7'
        self.output_panel.delete('0.0', tk.END)
        self.output_panel.insert('0.0', self._output_string)
    def __button_8(self):
        self._output_string += '8'
        self.output_panel.delete('0.0', tk.END)
        self.output_panel.insert('0.0', self._output_string)
    def __button_9(self):
        self._output_string += '9'
        self.output_panel.delete('0.0', tk.END)
        self.output_panel.insert('0.0', self._output_string)
    def __button_0(self):
        self._output_string += '0'
        self.output_panel.delete('0.0', tk.END)
        self.output_panel.insert('0.0', self._output_string)
    def __button_plus(self):
        self._output_string += '+'
        self.output_panel.delete('0.0', tk.END)
        self.output_panel.insert('0.0', self._output_string)
    def __button_minus(self):
        self._output_string += '-'
        self.output_panel.delete('0.0', tk.END)
        self.output_panel.insert('0.0', self._output_string)
    def __button_multiply(self):
        self._output_string += '*'
        self.output_panel.delete('0.0', tk.END)
        self.output_panel.insert('0.0', self._output_string)
    def __button_divide(self):
        self._output_string += '/'
        self.output_panel.delete('0.0', tk.END)
        self.output_panel.insert('0.0', self._output_string)
    def __button_result(self):
        if '+' in self._output_string:
            nums = self._output_string.split('+')
            self._output_string = str(int(nums[0]) + int(nums[1]))
        elif '-' in self._output_string:
            nums = self._output_string.split('-')
            self._output_string = str(int(nums[0]) - int(nums[1]))
        elif '*' in self._output_string:
            nums = self._output_string.split('*')
            self._output_string = str(int(nums[0]) * int(nums[1]))
        elif '/' in self._output_string:
            nums = self._output_string.split('/')
            self._output_string = str(int(nums[0]) / int(nums[1]))
        else:
            self._output_string = '0'
            
        self.output_panel.delete('0.0', tk.END)
        self.output_panel.insert('0.0', self._output_string)

def main():
    app = App()

if __name__ == '__main__':
    main()