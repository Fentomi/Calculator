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
        self.__create_button('1', self.__button_1, 0.2, 0.4)
        self.__create_button('2', self.__button_2, 0.35, 0.4)
        self.__create_button('3', self.__button_3, 0.5, 0.4)
        self.__create_button('4', self.__button_4, 0.2, 0.5)
        self.__create_button('5', self.__button_5, 0.35, 0.5)
        self.__create_button('6', self.__button_6, 0.5, 0.5)
        self.__create_button('7', self.__button_7, 0.2, 0.6)
        self.__create_button('8', self.__button_8, 0.35, 0.6)
        self.__create_button('9', self.__button_9, 0.5, 0.6)
        self.__create_button('0', self.__button_0, 0.35, 0.7)

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
    
    def __create_button(self, text: str, anchor_func, posX: [float, int], posY: [float, int]) -> ctk.CTkButton:
        but = ctk.CTkButton(master= self._app, text= text, height=40, width=40, command=anchor_func)
        but.place(relx=posX,rely=posY,anchor=tk.CENTER)
        return but
def main():
    app = App()

if __name__ == '__main__':
    main()