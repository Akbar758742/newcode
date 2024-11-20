from tkinter import *
import math
import tkinter.messagebox
from tkinter import ttk

root = Tk()
root.title("Extended Calculator")
root.configure(background='white')
root.resizable(width=False, height=False)
root.geometry("500x600")

# Create notebook for tabs
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Scientific Calculator Tab
calc_frame = Frame(notebook, bg="white")
notebook.add(calc_frame, text="Scientific Calculator")

# Unit Conversion Tab
unit_frame = Frame(notebook, bg="white")
notebook.add(unit_frame, text="Unit Conversion")

# Number System Conversion Tab
number_frame = Frame(notebook, bg="white")
notebook.add(number_frame, text="Number Conversion")

class Calc:
    def __init__(self):
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False

    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.' and secondnum in firstnum:
                return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def mathPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    # Unit Conversion Functions
    def unit_conversion(self, conversion):
        try:
            value = float(unit_input.get())
            if conversion == "meters_to_kilometers":
                result = value / 1000
            elif conversion == "kilometers_to_meters":
                result = value * 1000
            elif conversion == "grams_to_kilograms":
                result = value / 1000
            elif conversion == "kilograms_to_grams":
                result = value * 1000
            else:
                result = "Error"
            unit_result.set(result)
        except:
            unit_result.set("Error")

    # Number System Conversion Functions
    def number_system_conversion(self, conversion):
        try:
            value = int(number_input.get())
            if conversion == "binary":
                result = bin(value).replace("0b", "")
            elif conversion == "octal":
                result = oct(value).replace("0o", "")
            elif conversion == "hexadecimal":
                result = hex(value).replace("0x", "").upper()
            elif conversion == "decimal":
                result = int(value)
            number_result.set(result)
        except:
            number_result.set("Error")

added_value = Calc()

# Scientific Calculator Widgets
txtDisplay = Entry(calc_frame, font=('Helvetica', 20, 'bold'), bg='black', fg='white', bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

# Unit Conversion Widgets
unit_input = Entry(unit_frame, font=('Helvetica', 16), bd=5, width=20, justify=RIGHT)
unit_input.grid(row=0, column=1, padx=10, pady=10)
unit_result = StringVar()
unit_output = Entry(unit_frame, font=('Helvetica', 16), bd=5, width=20, justify=RIGHT, state="readonly", textvariable=unit_result)
unit_output.grid(row=1, column=1, padx=10, pady=10)

Button(unit_frame, text="m to km", command=lambda: added_value.unit_conversion("meters_to_kilometers")).grid(row=0, column=2)
Button(unit_frame, text="km to m", command=lambda: added_value.unit_conversion("kilometers_to_meters")).grid(row=1, column=2)
Button(unit_frame, text="g to kg", command=lambda: added_value.unit_conversion("grams_to_kilograms")).grid(row=2, column=2)
Button(unit_frame, text="kg to g", command=lambda: added_value.unit_conversion("kilograms_to_grams")).grid(row=3, column=2)

# Number Conversion Widgets
number_input = Entry(number_frame, font=('Helvetica', 16), bd=5, width=20, justify=RIGHT)
number_input.grid(row=0, column=1, padx=10, pady=10)
number_result = StringVar()
number_output = Entry(number_frame, font=('Helvetica', 16), bd=5, width=20, justify=RIGHT, state="readonly", textvariable=number_result)
number_output.grid(row=1, column=1, padx=10, pady=10)

Button(number_frame, text="Binary", command=lambda: added_value.number_system_conversion("binary")).grid(row=0, column=2)
Button(number_frame, text="Octal", command=lambda: added_value.number_system_conversion("octal")).grid(row=1, column=2)
Button(number_frame, text="Hex", command=lambda: added_value.number_system_conversion("hexadecimal")).grid(row=2, column=2)
Button(number_frame, text="Decimal", command=lambda: added_value.number_system_conversion("decimal")).grid(row=3, column=2)

root.mainloop()
