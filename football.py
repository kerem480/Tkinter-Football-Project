import tkinter as tk
from tkinter import ttk, NW

from PIL import ImageTk, Image


window=tk.Tk()
window.title("Players Project")
window.geometry("800x600")

pw=ttk.Panedwindow(window,orient=tk.HORIZONTAL)
pw.pack(fill=tk.BOTH,expand=True)

tab1=ttk.Frame(pw,height=100,width=200,relief=tk.SUNKEN)
tab2=ttk.Frame(pw,height=100,width=200,relief=tk.SUNKEN)

pw.add(tab1)
pw.add(tab2)



treeview=ttk.Treeview(tab1,height=20)
treeview.grid(row=0,column=0,padx=20,pady=60)

label1=tk.Label(tab1,text="Players",font="Ariel")
label1.place(x=80,y=30)

label_f1=tk.Label(tab2,text="Team:")
label_f1.place(x=20,y=300)

label_f2=tk.Label(tab2,text="Position:")
label_f2.place(x=20,y=330)

label_f3=tk.Label(tab2,text="Age:")
label_f3.place(x=20,y=360)

label_f4=tk.Label(tab2,text="Height:")
label_f4.place(x=350,y=300)

label_f5=tk.Label(tab2,text="Value:")
label_f5.place(x=350,y=330)

label_f6=tk.Label(tab2,text="Score:")
label_f6.place(x=350,y=360)

item=""
def callback(event):
    global item
    item=treeview.identify("item",event.x,event.y)


treeview.insert("","1","item2",text="Messi")
treeview.insert("","2","item3",text="Ronaldo")
treeview.insert("","3","item4",text="Benzema")
treeview.insert("","4","item5",text="Neymar")
treeview.insert("","5","item6",text="Quaresma")
treeview.insert("","6","item7",text="Mario Gomez")
treeview.bind("<Button-1>",callback)


global label_benzema5
def buttonFunction():
    global img,panel,label_f1_c,label_benzema5

    print("İşlem Yapılıyor...")
    if item != "":
        print("Lütfen Bir Seçenek Seçiniz",item)

        if item == "item2":
            img = ImageTk.PhotoImage(Image.open("C:\\Users\\90533\\Desktop\\messi2 (3).jpg"))
            panel = tk.Label(tab2,image=img,height=250,width=300).place(x=120,y=30)
            label_f1_c=tk.Label(tab2,text="Paris Saint Germain")
            label_f1_c.place(x=60,y=300)
            label_f2_c = tk.Label(tab2, text="Forward")
            label_f2_c.place(x=70,y=330)
            label_f3_c = tk.Label(tab2, text="35")
            label_f3_c.place(x=60, y=360)
            label_f4_c = tk.Label(tab2, text="168")
            label_f4_c.place(x=400, y=300)
            label_f5_c = tk.Label(tab2, text="50mil.€")
            label_f5_c.place(x=400, y=330)
            label_f6_c = tk.Label(tab2, text="752")
            label_f6_c.place(x=400, y=360)

            label_messi = tk.Label(tab2,
                                   text="Messi was born on June 24, 1987, in Rosario, Argentina. As a young boy, Messi tagged along")
            label_messi2 = tk.Label(tab2,
                                    text="when his two older brothers played soccer with their friends,unintimidated by the bigger boys.")
            label_mess3 = tk.Label(tab2,
                                   text="At the age of 8,he was recruited to join the youth system of Newell's Old Boys,a Rosario-based club.")

            label_mess3.place(x=10, y=440)
            label_messi.place(x=10, y=400)
            label_messi2.place(x=10, y=420)

        elif item == "item3":
            img = ImageTk.PhotoImage(Image.open("C:\\Users\\90533\\Desktop\\ronaldo4 (2).jpg"))
            panel = tk.Label(tab2,image=img,height=250,width=300).place(x=120,y=30)
            label_f1_c=tk.Label(tab2,text="Manchster United")
            label_f1_c.place(x=60,y=300)
            label_f2_c = tk.Label(tab2, text="Forward")
            label_f2_c.place(x=70,y=330)
            label_f3_c = tk.Label(tab2, text="37")
            label_f3_c.place(x=60, y=360)
            label_f4_c = tk.Label(tab2, text="187")
            label_f4_c.place(x=400, y=300)
            label_f5_c = tk.Label(tab2, text="30mil.€")
            label_f5_c.place(x=400, y=330)
            label_f6_c = tk.Label(tab2, text="807")
            label_f6_c.place(x=400, y=360)

            label_ronaldo = tk.Label(tab2,
                                   text="Ronaldo was born on February 5, 1985, in Funchal, Madeira, Portugal")
            label_ronaldo3 = tk.Label(tab2,
                                    text="a small island off the western coast of the country.")
            label_ronaldo2 = tk.Label(tab2,
                                    text="Ronaldo is the youngest of four children born to Maria Dolores dos Santos and José Dinis Aveiro.")

            label_ronaldo.place(x=10, y=400)
            label_ronaldo3.place(x=10, y=440)
            label_ronaldo2.place(x=10, y=420)

        elif item == "item4":
            img = ImageTk.PhotoImage(Image.open("C:\\Users\\90533\\Desktop\\benzema (3).jpg"))
            panel = tk.Label(tab2,image=img,height=250,width=300).place(x=120,y=30)
            label_f1_c=tk.Label(tab2,text="Real Madrid")
            label_f1_c.place(x=60,y=300)
            label_f2_c = tk.Label(tab2, text="Forward")
            label_f2_c.place(x=70,y=330)
            label_f3_c = tk.Label(tab2, text="34")
            label_f3_c.place(x=60, y=360)
            label_f4_c = tk.Label(tab2, text="185")
            label_f4_c.place(x=400, y=300)
            label_f5_c = tk.Label(tab2, text="30mil.€")
            label_f5_c.place(x=400, y=330)
            label_f6_c = tk.Label(tab2, text="386")
            label_f6_c.place(x=400, y=360)

            label_benzema = tk.Label(tab2,
                                   text="Born in Lyon to Algerian parents, Benzema began his senior career with hometown club")
            label_benzema3 = tk.Label(tab2,
                                    text="Olympique Lyonnais in 2005, contributing sporadically to three Ligue 1 title wins. In 2008")
            label_benzema2 = tk.Label(tab2,
                                    text="He was named the league's Player of the Year and in the Team of the Year having finished")


            label_benzema.place(x=10, y=400)
            label_benzema2.place(x=10, y=440)
            label_benzema3.place(x=10, y=420)



        elif item == "item5":
            img = ImageTk.PhotoImage(Image.open("C:\\Users\\90533\\Desktop\\neymar.jpg"))
            panel = tk.Label(tab2,image=img,height=250,width=300).place(x=120,y=30)
            label_f1_c=tk.Label(tab2,text="Paris Saint German")
            label_f1_c.place(x=60,y=300)
            label_f2_c = tk.Label(tab2, text="Forward")
            label_f2_c.place(x=70,y=330)
            label_f3_c = tk.Label(tab2, text="30")
            label_f3_c.place(x=60, y=360)
            label_f4_c = tk.Label(tab2, text="175")
            label_f4_c.place(x=400, y=300)
            label_f5_c = tk.Label(tab2, text="75mil.€")
            label_f5_c.place(x=400, y=330)
            label_f6_c = tk.Label(tab2, text="275")
            label_f6_c.place(x=400, y=360)

            label_ronaldo = tk.Label(tab2,
                                   text="Already a football legend with Brazil and FC Barcelona")
            label_ronaldo3 = tk.Label(tab2,
                                    text="Neymar Jr is now making history with French club Paris St-Germain.")
            label_ronaldo2 = tk.Label(tab2,
                                    text="Inspired by his father, Neymar Jr become a national hero and also one of the so-called ‘MSN’")

            label_ronaldo.place(x=10, y=400)
            label_ronaldo3.place(x=10, y=440)
            label_ronaldo2.place(x=10, y=420)

        elif item == "item6":
            img = ImageTk.PhotoImage(Image.open("C:\\Users\\90533\\Desktop\\quaresma (2).jpg"))
            panel = tk.Label(tab2,image=img,height=250,width=300).place(x=120,y=30)
            label_f1_c=tk.Label(tab2,text="Guimares")
            label_f1_c.place(x=60,y=300)
            label_f2_c = tk.Label(tab2, text="Forward")
            label_f2_c.place(x=70,y=330)
            label_f3_c = tk.Label(tab2, text="38")
            label_f3_c.place(x=60, y=360)
            label_f4_c = tk.Label(tab2, text="175")
            label_f4_c.place(x=400, y=300)
            label_f5_c = tk.Label(tab2, text="300tho.€")
            label_f5_c.place(x=400, y=330)
            label_f6_c = tk.Label(tab2, text="108")
            label_f6_c.place(x=400, y=360)

            label_ronaldo = tk.Label(tab2,
                                   text="Ricardo Andrade Quaresma Bernardo is a Portuguese professional footballer ")
            label_ronaldo3 = tk.Label(tab2,
                                    text="who was born on September 26 1983 in Lisbon, Portugal.")
            label_ronaldo2 = tk.Label(tab2,
                                    text="He mainly plays the role of a winger. He has been part of the national side since 1999.")

            label_ronaldo.place(x=10, y=400)
            label_ronaldo3.place(x=10, y=440)
            label_ronaldo2.place(x=10, y=420)

        elif item == "item7":
            img = ImageTk.PhotoImage(Image.open("C:\\Users\\90533\\Desktop\\mario (3).jpg"))
            panel = tk.Label(tab2,image=img,height=250,width=300).place(x=120,y=30)
            label_f1_c=tk.Label(tab2,text="Retired")
            label_f1_c.place(x=60,y=300)
            label_f2_c = tk.Label(tab2, text="Forward")
            label_f2_c.place(x=70,y=330)
            label_f3_c = tk.Label(tab2, text="37")
            label_f3_c.place(x=60, y=360)
            label_f4_c = tk.Label(tab2, text="189")
            label_f4_c.place(x=400, y=300)
            label_f5_c = tk.Label(tab2, text="None")
            label_f5_c.place(x=400, y=330)
            label_f6_c = tk.Label(tab2, text="319")
            label_f6_c.place(x=400, y=360)

            label_ronaldo = tk.Label(tab2,
                                   text="He is a German professional footballer.He played as a forward for the Germany national football team from 2007 to 2018 where he played")
            label_ronaldo3 = tk.Label(tab2,
                                    text="team from 2007 to 2018 where he played 78 matches of the game and scored 31 goals. also played for several professional football clubs")
            label_ronaldo2 = tk.Label(tab2,
                                    text="such as VfB Stuttgart, Bayern Munich, Fiorentina, Beşiktaş, and VfL Wolfsburg.")

            label_ronaldo.place(x=10, y=400)
            label_ronaldo3.place(x=10, y=440)
            label_ronaldo2.place(x=10, y=420)

            


        else:
            print("Lütfen Seçenek Seç")




button=tk.Button(tab1,text="ENTER",width=10,command=buttonFunction)
button.grid(row=1,column=0,padx=5,pady=5)






tk.mainloop()