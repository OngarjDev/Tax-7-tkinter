from tkinter import * 
from tkinter import ttk,messagebox
from datetime import datetime,time
import csv

def WritetoCSV(data):
    with open("datacutomer.csv","a",newline='',encoding="utf-8") as file:
        fw = csv.writer(file)
        fw.writerow(data)
        print("บันทึกไฟล์สำเร็จ")

def ReadCSV():
    with open("datacutomer.csv",'',newline='',encoding="utf-8") as file:
        fr = csv.reader(file)
        data = list(fr)
        return data

def helpme():
    messagebox.showinfo('ช่วยเหลือ ติดต่อGitHub:ongarj Dev',"โปรดทราบผลงานชิ้นนี้สร้างมาเพื่อการศึกษาtkinter\nสามารถศึกษาได้ที่นี่หากมีข้อสงสัยติดต่อได้ที่ Github: ongarj Dev")

#main progame 
GUI = Tk()
label = Label()
GUI.title('โปรแกรมคำนวณโดยใช้ GUI (Tkinter)')
GUI.geometry('900x700')

menu = Menu(GUI)
GUI.config(menu=menu)
helpmenu = Menu(menu)
menu.add_cascade(label='ช่วยเหลือ', menu=helpmenu)
helpmenu.add_command(label='ออก', command=GUI.quit)
helpmenu.add_command(label='เกี่ยวกับ',command=helpme)

#style tuple :FONT
FONT1 = ('TH SarabunPSK' , 45, 'bold')
FONT2 = ('TH SarabunPSK' , 30 , 'bold')

# windowe UI 
T1 = ttk.Label(GUI,text="โปรแกรมคำนวณภาษี",font=FONT1)
T1.pack()

T2 = ttk.Label(GUI,text="ชื่อสินค้า/product",font=FONT2)
T2.pack()

nameproduct = StringVar()
TextBox1 = ttk.Entry(GUI,font=FONT1,foreground='RED',width= '15',textvariable=nameproduct)
TextBox1.pack(ipadx= 20,ipady=10,pady=20)

T3 = ttk.Label(GUI,text="ราคา/price",font=FONT2)
T3.pack()

prices = StringVar()
TextBox2 = ttk.Entry(GUI,font=FONT1,foreground='RED',width= '15',textvariable=prices)
TextBox2.pack(ipadx= 20,ipady=10,pady=20)

T4 = ttk.Label(GUI,text="จำนวน/amount",font=FONT2)
T4.pack()

numberproduct = StringVar()
TextBox3 = ttk.Entry(GUI,font=FONT1,foreground='RED',width= '15',textvariable=numberproduct)
TextBox3.pack(ipadx= 20,ipady=20,pady=20)

def agree(event=None):
    print("User click button!!!")
    np = nameproduct.get()
    pp = int(prices.get())
    nbp = int(numberproduct.get())
    print(np)
    print(pp)
    print(nbp)
    Ldate = datetime.today().strftime("%d/%m/%Y")
    str(Ldate)
    sum1 = pp*nbp
    vat = pp*nbp *7/100
    data = [np,pp,nbp,sum1,vat,Ldate]
    total = sum1+vat
    WritetoCSV(data)
    textshow1 = 'ชื่อสินค้า/product : {} \n'.format(np)
    textshow2 = 'ราคา/price      : {} บาท\n'.format(pp)
    textshow3 = 'จำนวน/amount    : {} จำนวน\n'.format(nbp)
    textshow4 = 'รวม(ยังไม่รวมภาษี) : {} บาท \n'.format(sum1)
    textshow5 = 'ภาษี            : {} บาท \n'.format(vat)
    textshow6 = 'รวมทั้งหมด+ vat7%: {} บาท'.format(total)
    messagebox.showinfo('ผลลัพธ์',textshow1+textshow2+textshow3+textshow4+textshow5+textshow6)

bt1 = ttk.Button(GUI,text="ยืนยัน",width='50',command=agree,cursor="mouse")
bt1.pack()

GUI.mainloop()
