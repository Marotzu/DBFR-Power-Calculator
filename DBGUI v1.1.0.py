import tkinter as tk
import base64
import sys
import os
import locale
from io import BytesIO
import webbrowser

def calculate(*args):
    try:
        if mode_var.get() == "Strength and Defense":
            strength = float(strength_entry.get())
            defense = float(defense_entry.get())
            result = (strength + defense) * 140
        else:
            power_level = float(power_level_entry.get())
            result = (power_level / 140) / 2

        result = int(result)
        formatted_result = locale.format_string("%d", result, grouping=True)
        result_var.set(f"Result: {formatted_result}")
    except ValueError:
        result_var.set("No Input")

def clear_inputs():
    strength_entry.delete(0, tk.END)
    defense_entry.delete(0, tk.END)
    power_level_entry.delete(0, tk.END)
    result_var.set("")

def update_inputs(*args):
    selected_mode = mode_var.get()

    strength_label.pack_forget()
    strength_entry.pack_forget()
    defense_label.pack_forget()
    defense_entry.pack_forget()
    power_level_label.pack_forget()
    power_level_entry.pack_forget()

    if selected_mode == "Strength and Defense":
        strength_label.pack()
        strength_entry.pack()
        defense_label.pack()
        defense_entry.pack()
    else:
        power_level_label.pack()
        power_level_entry.pack()

    calculate()
    result_label.pack(side="bottom")

def open_github():
    webbrowser.open("https://github.com/Marotzu/DBFRPLC")

def copy_to_clipboard():
    result = result_var.get()
    if result:
        result_numbers = result.replace("Result: ", "")
        root.clipboard_clear()
        root.clipboard_append(result_numbers)
        root.update()

locale.setlocale(locale.LC_ALL, "")

root = tk.Tk()
root.title("Stat Calculator")

icon_base64 = """
AAABAAEAICAAAAEAIACoEAAAFgAAACgAAAAgAAAAQAAAAAEAIAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACP/wAAj/4EAI7/KQCN/2wAjf+tAI3/2QCM//EAi//9AIv//QCM//EAjf/ZAI3/rQCN/2wAjv8pAI/+BACP/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACP/wAAkP8DAI7/NgCN/5cAi//fAIf/+wCA//8Aev//AHb//wBz//8Ac///AHb//wB6//8AgP//AIf/+wCL/98Ajf+XAI7/NgCQ/wMAj/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACT/gAAjP8AAI7/GQCN/4gAi//qAIL//wB2//8AbP//AGj//wBn//8AZv//AGb//wBm//8AZv//AGf//wBo//8AbP//AHb//wCC//8Ai//qAI3/iACO/xkAjP8AAJP+AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkf8AAIn/AACO/zQAjf/BAIb//gB2//8Aaf//AGb//wBn//8AZ///AGf//wBn//8AZ///AGf//wBn//8AZ///AGf//wBn//8AZv//AGn//wB2//8Ahv/+AI3/wQCO/zQAif8AAJH/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAJD/AACJ/wAAjv8/AIz/2ACB//8Abf//AGb//wBn//8AZ///AGf//wBn//8AZ///AGf//wBn//8AZ///AGf//wBn//8AZ///AGf//wBn//8AZ///AGb//wBt//8Agf//AIz/2ACO/z8Aif8AAJD/AAAAAAAAAAAAAAAAAACV/gAAjP8AAI3/NACM/9cAf///AGr//wBn//8AZ///AGf//wBn//8AZ///AGf//wBn//8AZ///AGf//wBn//8AZ///AGf//wBn//8AZ///AGf//wBn//8AZ///AGf//wBq//8Af///AIz/1wCN/zQAjP8AAJX+AAAAAAAAAAAAAI7/AACO/xkAjf+/AIH//wBq//8AZ///AGf//wBn//8AZ///AGf//wBn//8AZ///AWX+/wRh/f8AaP//AGf//wRh/P8BZv//AGf//wBn//8AZ///AGf//wBn//8AZ///AGf//wBq//8Agf//AI3/vwCO/xkAjv8AAAAAAACO/wAAk/8CAI3/hgCG//8Abf//AWb//wBn//8AZ///AGf//wBn//8AZ///AGf//wBn//8CZP7/F0Du/w1R9v8RS/P/FEXx/wBm//8AZ///AGf//wBn//8AZ///AGf//wBn//8AZ///AGf//wBu//8Ahv//AI3/hgCT/wIAjv8AAI3/AACN/zUAi//nAHX//0uS//94rf//BWr//wBn//8AZ///AGf//wBn//8AZ///AGf//wBo//8WQu//KCTi/ygk4v8QTfT/AGn//wBn//8AZ///AGf//wBn//8AZ///AGf//wBn//8AZ///AGf//wB2//8Ai//nAI3/NQCN/wAAlv8CAI3/kwCC//8Xdv//yt///5fA//8CaP//AGf//wBn//8AZ///AGf//wBn//8AZ///C1X4/yEv5/8pIeH/KSLh/x416v8HW/r/AGf//wBn//8AZ///AGf//wBn//8AZ///AGf//wBn//8AZ///AGn//wCD//8Ajf+TAJb/AgCO/ycAjP/cAHT//2ej///f6///LID//wBl//8AZ///AGf//wBn//8AZ///AGf//wFl/v8MVPf/EUvz/yMt5v8fM+n/EEzz/wpX+P8AZv//AGf//wBn//8AZ///AGf//wBn//8AZ///AGf//wBn//8AZv//AHb//wCM/9wAjv8nAI7/aACH//oKcf//u9X//5nC//8BZ///AGf//wBn//8AZ///AGf//wBn//8AZ///AGf//wBo//8AaP//FUXw/w9O9P8Aaf//AGj//wBn//8AZ///AGf//wBn//8AZ///AGf//wBn//8AZ///AGf//wBn//8AbP//AIf/+gCN/2gAjf+nAH///yyC///h7f//TpT//wBl//8AZ///AWb//wFn//8AZ///AGj//wFm//8AZ///AGf//wBn//8FX/v/A2H9/wBn//8AZ///AGb//wFm/v8AZ///AGf//wFm/v8AZv//AGf//wBn//8AZ///AGf//wBo//8Agf//AI3/pwCN/9QAeP//V5r//93q//8hev//AGb//wBn//8EYPz/EUvz/wRh/f8KWPj/D0/1/wBn//8AZ///AGf//wBn//8AZ///AGf//wBn//8BZf7/EUvz/wZd+/8GXfv/EUvz/wJk/v8AZ///AGf//wBn//8AZ///AGf//wB7//8Ajf/UAIz/7QB0//94rf//yd7//w1u//8AZ///AGf//wFm/v8cOev/IS/n/yQr5f8OT/X/AGj//wBn//8AZ///AGf//wBn//8AZ///AGf//wBo//8VRfD/Iy3m/yMt5v8WQ+//AGj//wBn//8AZ///AGf//wBn//8AZv//AHf//wCM/+0AjP/4AHL//4m4//+81v//B2v//wBn//8AZ///Bl77/x8z6f8qIOD/KSLh/xNH8f8BZf7/AGf//wBn//8AZ///AGf//wBn//8AZ///A2L9/xk+7f8qIeH/KiHg/xo87P8DYv3/AGf//wBn//8AZ///AGf//wBm//8AdP//AIz/+ACM//gAcv//ibj//7zW//8Hav//AGf//wJk/v8TSPL/HTbq/ycl4v8jLOX/Gzvs/wtV9/8AZ///AGf//wBn//8AZ///AGf//wFm//8PT/X/HDjr/yUo5P8mKOT/HDjr/xBN9P8BZv//AGf//wBn//8AZ///AGb//wB0//8AjP/4AIz/7QB0//94rf//yd7//w1u//8AZ///AGf//wFm/v8CZP7/HDfr/xBN9P8AZ///AWb+/wBn//8AZ///AGf//wBn//8AZ///AGf//wFm/v8BZ///FkLv/xdA7v8BZv//AWb+/wBn//8AZ///AGf//wBn//8AZv//AHf//wCM/+0Ajf/UAHj//1ea///c6v//IXr//wBm//8AZ///AGf//wBn//8LVff/BV/8/wBn//8AZ///AGf//wBn//8AZ///AGf//wBn//8AZ///AGf//wBo//8IWvn/CVn5/wBo//8AZ///AGf//wBo//8AZ///AGf//wBn//8Ae///AI3/1ACN/6cAf///LYL//+Lt//9Nk///AGX//wBn//8AZ///AGf//wBn//8AZ///AGf//wBn//8DY/3/DVH2/wJj/f8EYPz/DVL2/wFm/v8AZ///AGf//wBn//8AZv//AGj//wBx//8Aff//AIL//wB+//8AcP//AGj//wCB//8Ajf+nAI3/aACH//oKcv//vNb//5jB//8BZ///AGf//wBn//8AZ///AGf//wBn//8AZ///AGf//wBm//8ZPe3/HTbq/yAy6P8UR/H/AGj//wBn//8AZ///AGf//wBr//8Aff//AIr//wCM//8AjP//AIz//wCG//8Acv//AIf/+gCN/2gAjv8nAIz/3AB0//9opP//3uv//yt///8AZf//AGf//wBn//8AZ///AGf//wBn//8AZ///AmT+/xk97f8qIOD/KiHh/xNH8f8BZv//AGf//wBn//8Aa///AID//wCL//8Ai///AIv//wCL//8Ai///AIv//wCE//8Ai//cAI7/JwCW/wIAjf+TAIL//xh3///L3///mMD//wVp//8AZ///AGf//wBn//8AZ///AGf//wFl/v8RSvP/ITHn/ygk4v8mJuP/HzTp/w1R9v8AZ///AGj//wB9//8Ai///AIv//wCL//8Ai///AIv//wCL//8Ai///AIv//wCM/5MAlv8CAI3/AACN/zUAi//nAHT//1eZ///n8P//XJ3//wBl//8AZ///AGf//wBn//8AZ///AGb//wNj/f8DYv3/HDjr/xZC7/8DY/3/AmP9/wBm//8Acv//AIr//wCL//8Ai///AIv//wCL//8Ai///AIv//wCL//8AjP/nAI3/NQCN/wAAjv8AAJP/AgCN/4YAhv//BXD//4u4///h7f//SZL//wBm//8AZ///AGf//wBn//8AZ///AGf//wBo//8MU/b/CVn5/wBo//8AZ///AGj//wB///8AjP//AIv//wCL//8Ai///AIv//wCL//8Ai///AIv//wCM/4YAlP8CAI7/AAAAAAAAjv8AAI7/GQCN/78AgP//D3L//53E///j7v//V5r//wBm//8AZv//AGf//wBn//8AZ///AGf//wFm/v8BZv//AGf//wBn//8Aa///AIf//wCL//8Ai///AIv//wCL//8Ai///AIv//wCL//8AjP+/AI7/GQCO/wAAAAAAAAAAAACV/gAAjP8AAI3/NACM/9cAfv//EHL//4q4//+Ou///Jn3//yZ9//8CaP//AGf//wBn//8AZ///AGf//wBn//8AZ///AGf//wBu//8Aif//AIv//wCL//8Ai///AIv//wCL//8Ai///AIz/1wCN/zQAjP8AAJX+AAAAAAAAAAAAAAAAAACQ/wAAif8AAI7/PwCM/9gAgP//BW///whr//+Bs///4u3//2Cf//8AZv//AGf//wBn//8AZ///AGf//wBn//8AZ///AGz//wCH//8Ai///AIv//wCL//8Ai///AIv//wCM/9gAjv8/AIn/AACQ/wAAAAAAAAAAAAAAAAAAAAAAAAAAAACR/wAAif8AAI7/NACN/8EAhv/+AHX//xd2//9no///RY///wBm//8AZ///AGf//wBn//8AZ///AGf//wBn//8AaP//AHz//wCL//8Ai///AIv//wCL//4AjP/BAI3/NACI/wAAkf8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACU/gAAjP8AAI7/GQCN/4gAi//qAIL//wBz//8Aa///AGj//wBn//8AZv//AGb//wBm//8AZv//AGf//wBo//8Ab///AIX//wCL//8Ai//qAI3/iACO/xkAjP8AAJP+AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAj/8AAJD/AwCO/zYAjf+XAIv/3wCH//sAgP//AHr//wB2//8Ac///AHP//wB2//8Aev//AID//wCH//sAi//fAIz/lwCN/zYAkP8DAI//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI//AACP/gQAjv8pAI3/bACN/60Ajf/ZAIz/8QCL//0Ai//9AIz/8QCN/9kAjf+tAI3/bACO/ykAj/4EAI//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/4AB//4AAH/8AAA/+AAAH/AAAA/gAAAHwAAAA4AAAAGAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAABgAAAAcAAAAPgAAAH8AAAD/gAAB/8AAA//gAAf/+AAf8=
 """  # Base64-encoded icon data

icon_data = base64.b64decode(icon_base64)
temp_icon_path = os.path.join(sys._MEIPASS, "temp_icon.ico")
with open(temp_icon_path, "wb") as f:
    f.write(icon_data)

root.iconbitmap(temp_icon_path)

root.geometry("300x250")
root.resizable(False, False)
root.configure(bg="#E6F3FF")

mode_var = tk.StringVar()
mode_var.set("Strength and Defense")

mode_label = tk.Label(root, text="Select Mode:", bg="#E6F3FF")
mode_menu = tk.OptionMenu(root, mode_var, "Strength and Defense", "Power Level")

strength_label = tk.Label(root, text="Strength:", bg="#E6F3FF")
strength_entry = tk.Entry(root)

defense_label = tk.Label(root, text="Defense:", bg="#E6F3FF")
defense_entry = tk.Entry(root)

power_level_label = tk.Label(root, text="Power Level:", bg="#E6F3FF")
power_level_entry = tk.Entry(root)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, bg="#bdd6ff")

clear_button = tk.Button(root, text="Clear", command=clear_inputs)
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
github_button = tk.Button(root, text="GitHub", command=open_github)

mode_label.pack()
mode_menu.pack()
strength_label.pack()
strength_entry.pack()
defense_label.pack()
defense_entry.pack()
power_level_label.pack()
power_level_entry.pack()
result_label.pack(side="bottom")
clear_button.pack()
copy_button.pack()
github_button.pack()

mode_var.trace("w", update_inputs)
strength_entry.bind("<KeyRelease>", calculate)
defense_entry.bind("<KeyRelease>", calculate)
power_level_entry.bind("<KeyRelease>", calculate)

update_inputs()
calculate()

root.mainloop()
