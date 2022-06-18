# Jupyter notebookではうまく動かなかったのでpythonファイルで記述

import tkinter as tk

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

if __name__ == '__main__':
    # p256()
    # p258()
    # p260()
    # p261()
    # p262()
    # p263()
    p264()
