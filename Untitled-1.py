from tkinter import *
import tkinter
from tkinter.font import names
from tkinter import messagebox
 
root = Tk()
 
#main window
root["bg"] = "#fafafa"
root.title("Песчихін Лев КМ-14")
root.geometry("500x750")
 
root.resizable(width=False, height=False)
 
canvas = Canvas(root,width=500, height=750)
canvas.pack()
 
 
#                                        Функции
def btc_click():
   course = courseInput.get()
 
   hours1 = round(float(name2.get()) * float(name5_4.get()),2)
   hours2 = round(float(name3.get()) * float(name3_2.get()), 2)
   hours3 = round(float(name4.get()) * float(name4_2.get()), 2)
   hours4 = round(float(name5.get()) * float(name2_2.get()) * 0.25, 2)
   hours5 = round(float(name2_1.get()) * 0.33 * float(name2_3.get() + name4_3.get()), 2)
   hours6 = round(float(name2_2.get()) * float(name3_1.get() * 2), 2)
   hours7 = round(0.25 * (float(name4_1.get()) * float(name2_3.get() + name4_3.get())), 2)
   hours8 = round(float(name5_1.get()) * float(name2_3.get() + name4_3.get()), 2)
   hours9 = round(float((name6_1.get())) * float(name2_3.get() + name4_3.get()), 2)
   hours10 = round(0.5 * float(name7_1.get()) * float(name2_3.get() + name4_3.get()), 2)
   hours11 = round(0.33 * float(name8_1.get()) * float(name2_3.get() + name4_3.get()), 2)
   hours12 = round(0.25 * float(name9_1.get()) * float(name2_3.get() + name4_3.get()), 2)
   hours13 = round(2 * float(name2_1.get()) * float(name2_2.get()) + 0.06 * float(name2.get()) * (float(name2_3.get() + name4_3.get())/25), 2)
 
 
 
  
 
   info_str = f"{course}\nЛекції: {hours1}\nПрактики: {hours2}\nЛабораторні: {hours3}\nІндивідуальні заняття: {hours4}\nЕкзамени: {hours5}\nЗаліки: {hours6} \n Контрольні роботи: {hours7} \n Курсові проекти: {hours8} \nКурсові роботи: {hours9} \nРГР,РР,ГР: {hours10}  \nДКР: {hours11} \nРеферати: {hours12} \nКонсультації: {hours13}"
   messagebox.showinfo(title="Лекції", message=info_str)
 
 
 
 
 
#main frame
frame = Frame(root, bg="grey")
frame.place(relwidth=1,relheight=1)
 
 
 
#title
title = Label(frame, text="Розрахунок навчального навантаження", bg="grey")
title.place(relx=0.25,rely=0.005)
 
#title2
title2= Label(frame, text="Курс навчання, шифр групи:", bg="grey")
title2.place(relx=0.2,rely=0.04)   
 
 
#button GO
btn=Button(frame, text="GO", bg="white", command=btc_click)
btn.place(relx=0.892, rely=0.041)
 
 
#Курс навчання введення даних
courseInput = Entry(frame, bg="white")
courseInput.place(width=120,height=22,relx=0.58,rely=0.041)
 
 
 
#                                           Перший Блок
 
#Аудиторні заняття
frame1=Frame(root,bg="white")
frame1.place(relx=0.05,rely=0.082,width=450,height=170)
 
#Назва заняття
frame2=Frame(frame1,bg="#696969")
frame2.place(width=30,height=175)
 
#A.3.
frame2_name=Label(frame2,text="А.З.",bg="#696969")
frame2_name.place(relx=0.0, rely=0.4)
 
 
 
#names of activities
frame3_name=Frame(frame1,bg="#A9A9A9")
frame3_name.place(width=260, height=170, relx=0.067)
 
class1= Label(frame3_name, text="Лекції, Л годин", bg="#A9A9A9")
class1.place(relx=0,rely=0.01)
 
class1= Label(frame3_name, text="Практика (комп.пр, семінари), П годин)", bg="#A9A9A9")
class1.place(relx=0,rely=0.18)
 
class1= Label(frame3_name, text="Лабораторні, L годин", bg="#A9A9A9")
class1.place(relx=0,rely=0.35)
 
class1= Label(frame3_name, text="Індивідуальні заняття", bg="#A9A9A9")
class1.place(relx=0,rely=0.5)
 
class1= Label(frame3_name, text="Тощо...", bg="#A9A9A9")
class1.place(relx=0,rely=0.65)
 
class1= Label(frame3_name, text="Тощо...", bg="#A9A9A9")
class1.place(relx=0,rely=0.82)
 
 
 
 
#для введення кількості годин
frame4_names=Frame(frame1 )
frame4_names.place(width=160, height=170, relx=0.643)
 
name2=Entry(frame4_names, bg="white")
name2.pack()
 
name3=Entry(frame4_names, bg="white")
name3.pack()
 
name4=Entry(frame4_names, bg="white")
name4.pack()
 
name5=Entry(frame4_names, bg="white")
name5.pack()
 
name6=Entry(frame4_names, bg="white")
name6.pack()
 
name7=Entry(frame4_names, bg="white")
name7.pack()
 
 
 
 
#                                            Другий Блок
frame1_1=Frame(root,bg="white")
frame1_1.place(relx=0.05,rely=0.318,width=450,height=230)
 
 
#Назва заняття
frame2_1=Frame(frame1_1,bg="#696969")
frame2_1.place(width=30,height=230)
 
#К.Р.
frame2_1_name=Label(frame2_1,text="К.Р.",bg="#696969")
frame2_1_name.place(relx=0.0, rely=0.4)
 
 
#names of activities
frame3_1_name=Frame(frame1_1,bg="#A9A9A9")
frame3_1_name.place(width=260, height=230, relx=0.067)
 
class1_1= Label(frame3_1_name, text="Екзамени, Е", bg="#A9A9A9")
class1_1.place(relx=0,rely=0.01)
 
class1_2= Label(frame3_1_name, text="Заліки, Z", bg="#A9A9A9")
class1_2.place(relx=0,rely=0.13)
 
class1_3= Label(frame3_1_name, text="Контр.роб(мод.,темат.), М", bg="#A9A9A9")
class1_3.place(relx=0,rely=0.25)
 
class1_4= Label(frame3_1_name, text="Курсові проекти, Q години", bg="#A9A9A9")
class1_4.place(relx=0,rely=0.38)
 
class1_5= Label(frame3_1_name, text="Курсові роботи, G годин", bg="#A9A9A9")
class1_5.place(relx=0,rely=0.5)
 
class1_6= Label(frame3_1_name, text="РГР, РР, ГР  R", bg="#A9A9A9")
class1_6.place(relx=0,rely=0.62)
 
class1_7= Label(frame3_1_name, text="ДКР", bg="#A9A9A9")
class1_7.place(relx=0,rely=0.73)
 
class1_8= Label(frame3_1_name, text="Реферати", bg="#A9A9A9")
class1_8.place(relx=0,rely=0.85)
 
 
 
#для введення кількості годин
frame4_1_names=Frame(frame1_1)
frame4_1_names.place(width=160, height=230, relx=0.643)
 
name2_1=Entry(frame4_1_names, bg="white")
name2_1.pack()
 
name3_1=Entry(frame4_1_names, bg="white")
name3_1.pack()
 
name4_1=Entry(frame4_1_names, bg="white")
name4_1.pack()
 
name5_1=Entry(frame4_1_names, bg="white")
name5_1.pack()
 
name6_1=Entry(frame4_1_names, bg="white")
name6_1.pack()
 
name7_1=Entry(frame4_1_names, bg="white")
name7_1.pack()
 
name8_1=Entry(frame4_1_names, bg="white")
name8_1.pack()
 
name9_1=Entry(frame4_1_names, bg="white")
name9_1.pack()
 
 
#                                           Третій блок
 
frame1_2=Frame(root,bg="white")
frame1_2.place(relx=0.05,rely=0.635,width=450,height=120)
 
 
#Назва заняття
frame2_2=Frame(frame1_2,bg="#696969")
frame2_2.place(width=80,height=120)
 
#Групи/Бюдж
frame2_2_name=Label(frame2_2,text="Групи",bg="#696969")
frame2_2_name.place(relx=0.0, rely=0.4)
 
frame2_3_name=Label(frame2_2,text="Бюдж",bg="#696969")
frame2_3_name.place(relx=0.43, rely=0.2)
 
 
 
#names of activities
frame3_2_name=Frame(frame1_2,bg="#A9A9A9")
frame3_2_name.place(width=210, height=170, relx=0.175)
 
class1_1= Label(frame3_2_name, text="Академічні бюдж., Г", bg="#A9A9A9")
class1_1.place(relx=0,rely=0.015)
 
class1_2= Label(frame3_2_name, text="Підгрупи для ПЗ, ГП", bg="#A9A9A9")
class1_2.place(relx=0,rely=0.18)
 
class1_3= Label(frame3_2_name, text="Підгр. для лаб. робіт, ГL", bg="#A9A9A9")
class1_3.place(relx=0,rely=0.35)
 
class1_4= Label(frame3_2_name, text="Академ контрактні, ГК", bg="#A9A9A9")
class1_4.place(relx=0,rely=0.52)
 
 
 
#для введення кількості годин
frame4_2_names=Frame(frame1_2)
frame4_2_names.place(width=160, height=170, relx=0.643)
 
name2_2=Entry(frame4_2_names, bg="white")
name2_2.pack()
 
name3_2=Entry(frame4_2_names, bg="white")
name3_2.pack()
 
name4_2=Entry(frame4_2_names, bg="white")
name4_2.pack()
 
name5_2=Entry(frame4_2_names, bg="white")
name5_2.pack()
 
 
 
 
#                                            Четвертий блок
 
frame1_3=Frame(root,bg="white")
frame1_3.place(relx=0.05,rely=0.805,width=450,height=140)
 
 
#Назва заняття
frame2_3=Frame(frame1_3,bg="#696969")
frame2_3.place(width=80,height=140)
 
 
frame2_3_name=Label(frame2_3,text="Кільк.",bg="#696969")
frame2_3_name.place(relx=0.0, rely=0.4)
 
frame2_4_name=Label(frame2_3,text="Бюдж",bg="#696969")
frame2_4_name.place(relx=0.43, rely=0.2)
 
frame2_4_name=Label(frame2_3,text="Контр",bg="#696969")
frame2_4_name.place(relx=0.43, rely=0.55)
 
 
 
#names of activities
frame3_3_name=Frame(frame1_3,bg="#A9A9A9")
frame3_3_name.place(width=210, height=170, relx=0.175)
 
class1_2= Label(frame3_3_name, text="Б", bg="#A9A9A9")
class1_2.place(relx=0.4,rely=0.015)
 
class1_3= Label(frame3_3_name, text="К", bg="#A9A9A9")
class1_3.place(relx=0.4,rely=0.18)
 
class1_4= Label(frame3_3_name, text="БК", bg="#A9A9A9")
class1_4.place(relx=0.4,rely=0.35)
 
class1_5= Label(frame3_3_name, text="КК", bg="#A9A9A9")
class1_5.place(relx=0.4,rely=0.52)
 
class1_6= Label(frame3_3_name, text="Кількість бюджетних потоків, P", bg="#A9A9A9")
class1_6.place(relx=0.01,rely=0.66)
 
 
#для введення кількості годин
frame4_3_names=Frame(frame1_3)
frame4_3_names.place(width=160, height=170, relx=0.643)
 
name2_3=Entry(frame4_3_names, bg="white")
name2_3.pack()
 
name3_3=Entry(frame4_3_names, bg="white")
name3_3.pack()
 
name4_3=Entry(frame4_3_names, bg="white")
name4_3.pack()
 
name5_3=Entry(frame4_3_names, bg="white")
name5_3.pack()
 
name5_4=Entry(frame4_3_names, bg="white")
name5_4.pack()
 
 
 
 
 
 
 
root.mainloop()