import tkinter as tk
import customtkinter as ctk
import re

class Calc():
    def __init__(self):
        #глобальные переменные
        self.result = None
        self.cache_last_action = None

        #general settings application
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        self._app = ctk.CTk()
        self._app.geometry('350x450')
        self._app.resizable(False, False)
        self._app.title('Калькулятор')

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
        self.__create_button('C', self.__button_clear, 0.65, 0.3)
        self.__create_button('<=', self.__button_backspace, 0.8, 0.3)
        self.__create_button('+', self.__button_plus, 0.8, 0.4)
        self.__create_button('-', self.__button_minus, 0.8, 0.5)
        self.__create_button('*', self.__button_multiply, 0.8, 0.6)
        self.__create_button('/', self.__button_divide, 0.8, 0.7)
        self.__create_button('=', self.__button_result, 0.8, 0.85)
        self.__create_button(',', self.__button_point, 0.5, 0.7)
        #string output information
        self.__create_textbox()
        self._output_string = '0'
        self.__write_output('')

        #if people enter number
        self._app.bind('<Key>', self.__inputChar)

        self._app.mainloop()

    #function button-click reaction
    def __button_1(self):
        self.__replace_first_zero_on_button()
        self.__write_output('1')
    def __button_2(self):
        self.__replace_first_zero_on_button()
        self.__write_output('2')
    def __button_3(self):
        self.__replace_first_zero_on_button()
        self.__write_output('3')
    def __button_4(self):
        self.__replace_first_zero_on_button()
        self.__write_output('4')
    def __button_5(self):
        self.__replace_first_zero_on_button()
        self.__write_output('5')
    def __button_6(self):
        self.__replace_first_zero_on_button()
        self.__write_output('6')
    def __button_7(self):
        self.__replace_first_zero_on_button()
        self.__write_output('7')
    def __button_8(self):
        self.__replace_first_zero_on_button()
        self.__write_output('8')
    def __button_9(self):
        self.__replace_first_zero_on_button()
        self.__write_output('9')
    def __button_0(self):
        self.__replace_first_zero_on_button()
        self.__write_output('0')
    def __button_plus(self):
        try:
            int(self._output_string[-1])
            self.__write_output('+')
        except:
            pass
    def __button_minus(self):
        if self._output_string[-1] != '-' or self._output_string == '':
            self.__replace_first_zero_on_button()
            self.__write_output('-')
    def __button_multiply(self):
        try:
            int(self._output_string[-1])
            self.__write_output('*')
        except:
            pass
    def __button_divide(self):
        try:
            int(self._output_string[-1])
            self.__write_output('/')
        except:
            pass
    def __button_backspace(self):
        if self.cache_last_action is None and len(self._output_string) == 1:
            self._output_string = '0'
        elif self.cache_last_action is None:
            self._output_string = self._output_string[:-1]
        self.__write_output('')
    def __button_clear(self):
        self.cache_last_action = None
        self._output_string = '0'
        self.__write_output('')
    def __button_point(self):
        try:
            int(self._output_string[-1])
            self.__write_output('.')
        except:
            pass

    #Функция срабатывает, когда пользователь нажимает что-то на клавиатуре
    def __inputChar(self, event):
        if event.keysym == '0':
            self.__button_0()
        elif event.keysym == '1':
            self.__button_1()
        elif event.keysym == '2':
            self.__button_2()
        elif event.keysym == '3':
            self.__button_3()
        elif event.keysym == '4':
            self.__button_4()
        elif event.keysym == '5':
            self.__button_5()
        elif event.keysym == '6':
            self.__button_6()
        elif event.keysym == '7':
            self.__button_7()
        elif event.keysym == '8':
            self.__button_8()
        elif event.keysym == '9':
            self.__button_9()
        elif event.keysym == 'plus':
            self.__button_plus()
        elif event.keysym == 'minus':
            self.__button_minus()
        elif event.keysym == 'asterisk':
            self.__button_multiply()
        elif event.keysym == 'slash':
            self.__button_divide()
        elif event.keysym == 'comma':
            self.__button_point()
        elif event.keysym == 'BackSpace':
            self.__button_backspace()
        elif event.keysym == 'c' or event.keysym == 'с':
            self.__button_clear()
        elif event.keysym == 'Return':
            self.__button_result()
        elif event.keysym == 'Escape':
            self._app.destroy()

    #main function
    def __button_result(self):
        self._output_string = self.calculation(self._output_string)
        self.__write_output('')

    #create stuffs
    def __create_button(self, text: str, anchor_func, posX:[float, int], posY:[float, int]) -> ctk.CTkButton:
        but = ctk.CTkButton(master=self._app, text=text, height=40, width=40,
        command=anchor_func, font=('Arial Bold', 24))
        but.place(relx=posX, rely=posY, anchor=tk.CENTER)
        return but
    def __create_textbox(self):
        self.output_panel = ctk.CTkTextbox(master=self._app, width=250, height=30, state=tk.DISABLED, 
        activate_scrollbars=False, font=('Arial', 24))
        self.output_panel.place(relx = 0.5, rely = 0.1, anchor = tk.CENTER)

    #write something
    def __write_output(self, text: str):
        self.output_panel.configure(state=tk.NORMAL)
        self._output_string += text
        self.output_panel.delete('0.0', tk.END)
        self.output_panel.insert('0.0', self._output_string)
        self.output_panel.configure(state=tk.DISABLED)

    #class-methods
    @classmethod
    def operations_in_string(self, string: str) -> list:
        oper = list()
        first_char_is_minus = False
        for item in string:
            if string[0] == '-' and first_char_is_minus is False:
                first_char_is_minus = True
                continue
            if item in ['-', '+', '*', '/']:
                oper.append(item)
        return oper
    @classmethod
    def numbers_in_string(self, string: str) -> list:
        nums = list()
        str_num = ''
        first_char_is_minus = False
        for item in string:
            if string[0] == '-' and first_char_is_minus is False:
                str_num += '-'
                first_char_is_minus = True
                continue
            elif item in ['-', '+', '*', '/']:
                nums.append(float(str_num))
                str_num = ''
            else:
                str_num += item
        nums.append(float(str_num))
        return nums
    @classmethod
    def __calc_para(self, char: str, temp=0, numbers=[], result=None):
        if result is None:
            if char == '+':
                result = numbers[temp] + numbers[temp + 1]
                temp += 2
            elif char == '-':
                result = numbers[temp] - numbers[temp + 1]
                temp += 2
            elif char == '*':
                result = numbers[temp] * numbers[temp + 1]
                temp += 2
            elif char == '/':
                result = numbers[temp] / numbers[temp + 1]
                temp += 2
            return result, temp
        else:
            if char == '+':
                result += numbers[temp]
                temp += 1
            elif char == '-':
                result -= numbers[temp]
                temp += 1
            elif char == '*':
                result *= numbers[temp]
                temp += 1
            elif char == '/':
                result /= numbers[temp]
                temp += 1
            return result, temp
    def calculation(self, string):
        if self.cache_last_action is None or self._output_string != self.result:
            chars = self.operations_in_string(string)
            numbers = self.numbers_in_string(string)

            self.result = None
            temp = 0
            for i in chars:
                self.result, temp = self.__calc_para(char=i, temp=temp, numbers=numbers, result=self.result)

            self.cache_last_action = [chars[-1], str(numbers[-1])]
            self.result = self.result.__round__(2)
            self.result = self.__remove_zeros_in_result_string(str(self.result))
            return self.result
        else:
            self.result = self.result + self.cache_last_action[0] + self.cache_last_action[1]
            numbers = self.numbers_in_string(self.result)

            self.result, temp = self.__calc_para(char=self.cache_last_action[0], temp=0, numbers=numbers)
            self.result = self.result.__round__(2)
            self.result = self.__remove_zeros_in_result_string(str(self.result))
            return self.result
    def __remove_zeros_in_result_string(self, string: str) -> str:
        splitted_string = string.split('.')
        for item in splitted_string[1]:
            if item != '0':
                return string
        return splitted_string[0]
    def __replace_first_zero_on_button(self) -> str:
        if self._output_string == '0':
            self._output_string = ''

def main():
    app = Calc()

if __name__ == '__main__':
    main()