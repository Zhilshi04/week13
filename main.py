import tkinter as tk

def convert_temperature():
    try:
        fahrenheit = float(entry_fahrenheit.get())
        celsius = (fahrenheit - 32) * 5/9
        label_result.config(text=f"{fahrenheit:.2f} องศาฟาเรนไฮน์ เท่ากับ {celsius:.2f} องศาเซลเซียส")
    except ValueError:
        label_result.config(text="โปรดป้อนตัวเลขเท่านั้น")

# สร้างหน้าต่าง
root = tk.Tk()
root.title("แปลงอุณหภูมิ ฟาเรนไฮน์ เป็น เซลเซียส")

# สร้างเขตข้อมูลและปุ่ม
label_fahrenheit = tk.Label(root, text="องศาฟาเรนไฮน์:")
label_fahrenheit.grid(row=0, column=0)

entry_fahrenheit = tk.Entry(root)
entry_fahrenheit.grid(row=0, column=1)

button_convert = tk.Button(root, text="แปลง", command=convert_temperature)
button_convert.grid(row=0, column=2)

label_result = tk.Label(root, text="")
label_result.grid(row=1, columnspan=3)

root.mainloop()
