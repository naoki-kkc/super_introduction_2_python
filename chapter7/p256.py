# Jupyter notebookではうまく動かなかったのでpythonファイルで記述

import tkinter as tk
import tkinter.messagebox as msg

def p256():
    base = tk.Tk()
    base.mainloop()

def p258():
    base = tk.Tk()
    btn = tk.Button(base, text='push')
    btn.pack()
    base.mainloop()

def p260():
    base = tk.Tk()
    btn1 = tk.Button(base, text='btn_1')
    btn2 = tk.Button(base, text='btn_2')
    btn3 = tk.Button(base, text='btn_3')

    # ボタンを配置
    btn1.pack()
    btn2.pack()
    btn3.pack()

    base.mainloop()

def p261():
    base = tk.Tk()
    btn1 = tk.Button(base, text='btn_1')
    btn2 = tk.Button(base, text='btn_2')
    btn3 = tk.Button(base, text='btn_3')

    # ボタンを左/右指定で配置（指定のないbtn1は中央)
    btn1.pack()
    btn2.pack(side=tk.LEFT)
    btn3.pack(side=tk.RIGHT)

    base.mainloop()

def p262():
    base = tk.Tk()
    btn1 = tk.Button(base, text='btn_1')
    btn2 = tk.Button(base, text='btn_2')
    btn3 = tk.Button(base, text='btn_3')
    
    # グリッド状に配置
    btn1.grid(row=0, column=0)
    btn2.grid(row=0, column=1)
    btn3.grid(row=1, column=1)
    
    base.mainloop()

def p262():
    base = tk.Tk()
    btn1 = tk.Button(base, text='btn_1')
    btn2 = tk.Button(base, text='btn_2')
    btn3 = tk.Button(base, text='btn_3')
    
    # グリッド状に配置
    btn1.grid(row=0, column=0)
    btn2.grid(row=0, column=1)
    btn3.grid(row=1, column=1)
    
    base.mainloop()

def p263():
    base = tk.Tk()
    btn1 = tk.Button(base, text='btn_1')
    btn2 = tk.Button(base, text='btn_2')
    btn3 = tk.Button(base, text='btn_3')
    
    # x座標/y座標を指定して配置
    btn1.place(x=0, y=0)
    btn2.place(x=50, y=50)
    btn3.place(x=100, y=100)
    
    base.mainloop()

def p264():
    base = tk.Tk()
    btn  = tk.Button(base, text='call method', command=p264_call_method)
    btn.pack()
    base.mainloop()

def p264_call_method():
    print('p264_called!')

def p265():
    base = tk.Tk()
    tk.Label(base, text='red', bg='red', width=20).pack()
    tk.Label(base, text='blue', bg='blue', width=20).pack()
    tk.Label(base, text='green', bg='green', width=20).pack()
    base.mainloop()

def p266():
    base = tk.Tk()
    select_dict = {0: 'hoge', 1:'fuga', 2:'foo', 3:'bar'}
    check_dict  = {}

    for i in range(len(select_dict)):
        check_dict[i] = tk.BooleanVar()
        tk.Checkbutton(base, variable=check_dict[i], text=select_dict[i]).pack()
    
    def buy():
        for i in check_dict:
            if check_dict[i].get():
                print(select_dict[i])
    
    tk.Button(base, text='order', command=buy).pack()
    base.mainloop()

def p268():
    base = tk.Tk()
    radio_val = tk.IntVar()
    radio_val.set(1)
    radio_dict = {0:'hoge', 1:'fuga', 2:'foobar'}
    tk.Radiobutton(base, text = radio_dict[0], variable=radio_val, value=0).pack()
    tk.Radiobutton(base, text = radio_dict[1], variable=radio_val, value=1).pack()
    tk.Radiobutton(base, text = radio_dict[2], variable=radio_val, value=2).pack()
    def p268_btn():
        val = radio_val.get()
        print(radio_dict[val])
    tk.Button(base, text='order', command=p268_btn).pack()
    base.mainloop()

def p270():
    base = tk.Tk()
    alert_response = msg.askyesno('alert_title', 'alert_message')
    if alert_response:
        print('ok')
    else:
        print('no')
    base.mainloop()

def p271():
    base = tk.Tk()

    str = tk.StringVar()
    tk.Entry(base, textvariable=str).pack()
    tk.Label(base, textvariable=str).pack()

    base.mainloop()

def p272():
    base = tk.Tk()

    menu   = tk.Menu(base)
    f_menu = tk.Menu(menu)
    f_menu.add_command(label='open file')
    f_menu.add_separator()
    f_menu.add_command(label='save file')
    menu.add_cascade(label='file', menu=f_menu)

    base.config(menu=menu)
    base.mainloop()


if __name__ == '__main__':
    # p256()
    # p258()
    # p260()
    # p261()
    # p262()
    # p263()
    # p264()
    # p265()
    # p266()
    # p268()
    # p270()
    # p271()
    p272()