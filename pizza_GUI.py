
########################################################## MAIN PAGE START ###############################################################

# IMPORT MODULES REQUIRED
from tkinter import *
from PIL import Image,ImageTk
import pymysql
import datetime
from datetime import date

conn = pymysql.connect(host="localhost",user="root",password="123456789",database="pizzahub_db")
cursor= conn.cursor()

def main():
    top = Tk()

    # image setting

    employee = PhotoImage(file = "images/employee.png")


# CREATED WINDOW FOR TKINTER
    top.geometry("1600x1600")
    top.title("Pizza hub")
    top.configure(background="grey")


# CREATED TIME & DATE FUNCTIONS

    def dateotime():
        dt = datetime.datetime.now()
        string = dt.strftime('DATE: %d-%m-%y \n    TIME: %H:%M:%S%p')
        DT.config(text = string)
        DT.after(1000,dateotime)

#functions for buttons
##################################################### main page paused ############################################################

##################################################### employee login page start ####################################################
    def emplogin():
    # emplogin PAGE WINDOW CONFIGURATION
        top.destroy()
        toor1 = Tk()
        toor1.geometry("500x500")
        toor1.title("emplogin")
        toor1.configure(background="grey")

    #date & time
        def dateotime():
            dt = datetime.datetime.now()
            string = dt.strftime('DATE: %d-%m-%y \n    TIME: %H:%M:%S%p')
            DT.config(text=string)
            DT.after(1000, dateotime)

        DT = Label(toor1, font=('calibri', 15, 'bold'), bg="grey")
        DT.place(x=10, y=10, anchor='nw')

    # function for employee login button
        def back():
            toor1.destroy()
            main()

        def condition():
            if entrypassword.get() == "123" and  entryusername.get() =="emp":
                 menu()
            else:
                error =  Label(toor1, text ="Error !!!! enter again",bg="grey")
                error.place(x=200, y=400)

######################################################################## employee login page paused #########################################################

######################################################################## menue page starts here #############################################################

        def menu():
            toor1.destroy()
            root = Tk()
            root.geometry("1600x1600")
            root.title("Pizza hub")
            root.configure(background="grey")



            # image setting for menue page

            photo3 = Image.open("images/pr.png")
            item0a = ImageTk.PhotoImage(photo3)

            photo4 = Image.open("images/mr.png")
            item1a = ImageTk.PhotoImage(photo4)

            photo5 = Image.open("images/or.png")
            item2a = ImageTk.PhotoImage(photo5)

            photo6 = Image.open("images/sr.png")
            item3a = ImageTk.PhotoImage(photo6)

            photo7 = Image.open("images/ir.png")
            item4a = ImageTk.PhotoImage(photo7)

            photo8 = Image.open("images/cr.png")
            item5a = ImageTk.PhotoImage(photo8)

            photo9 = Image.open("images/br.png")
            item6a = ImageTk.PhotoImage(photo9)

            photo10 = Image.open("images/gr.png")
            item7a = ImageTk.PhotoImage(photo10)

            photo11 = Image.open("images/par.png")
            item8a = ImageTk.PhotoImage(photo11)

            photo12 = Image.open("images/spr.png")
            item9a = ImageTk.PhotoImage(photo12)

            photo13 = Image.open("images/cola.png")
            item10a = ImageTk.PhotoImage(photo13)

            photo14 = Image.open("images/tup.png")
            item11a = ImageTk.PhotoImage(photo14)

            photo15 = Image.open("images/pep.png")
            item12a = ImageTk.PhotoImage(photo15)

            # INITIALISING VARIBLES
            var0 = StringVar(root, 0)
            var1 = StringVar(root,0)
            var2 = StringVar(root,0)
            var3 = StringVar(root,0)
            var4 = StringVar(root,0)
            var5 = StringVar(root,0)
            var6 = StringVar(root,0)
            var7 = StringVar(root,0)
            var8 = StringVar(root,0)
            var9 = StringVar(root,0)
            var10 = StringVar(root,0)
            var11 = StringVar(root,0)
            var12 = StringVar(root,0)
            tvar = StringVar(root,0)


            # FUNCTION TO CLEAR ALL THE ENTRY

            def clear():
                global count0, count1, count2, count3, count4, count5, count6, count7, count8, count9, count10, count11, count12
                count0, count1, count2, count3, count4, count5, count6, count7, count8, count9, count10, count11, count12 = [
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

                total1.delete(0,END)
                total1.insert(0,0)

                item0.delete(0,END)
                item0.insert(0,0)

                item1.delete(0, END)
                item1.insert(0, 0)

                item2.delete(0, END)
                item2.insert(0, 0)

                item3.delete(0, END)
                item3.insert(0, 0)

                item4.delete(0, END)
                item4.insert(0, 0)

                item5.delete(0, END)
                item5.insert(0, 0)

                item6.delete(0, END)
                item6.insert(0, 0)

                item7.delete(0, END)
                item7.insert(0, 0)

                item8.delete(0, END)
                item8.insert(0, 0)

                item9.delete(0, END)
                item9.insert(0, 0)

                item10.delete(0, END)
                item10.insert(0, 0)

                item11.delete(0, END)
                item11.insert(0, 0)

                item12.delete(0, END)
                item12.insert(0, 0)

                cosname.delete(0, END)
                cosnumber.delete(0, END)


            # INITIALISING COUNTERS
            global count0,count1,count2,count3,count4,count5,count6,count7,count8,count9,count10,count11,count12
            count0,count1,count2,count3,count4,count5,count6,count7,count8,count9,count10,count11,count12 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
            # FUNCTION TO INCREMENT ITEMS:
            def I0():
                global count0
                s = var0.get()
                s = int(s)
                item0.delete(0, END)
                count0 = s
                count0 += 1
                item0.insert(0, count0)

            def I1():
                global count1
                s = var1.get()
                s = int(s)
                item1.delete(0, END)
                count1 = s
                count1 += 1
                item1.insert(0, count1)

            def I2():
                global count2
                s = var2.get()
                s = int(s)
                item2.delete(0, END)
                count2 = s
                count2 += 1
                item2.insert(0, count2)

            def I3():
                global count3
                s = var3.get()
                s = int(s)
                item3.delete(0, END)
                count3 = s
                count3 += 1
                item3.insert(0, count3)

            def I4():
                global count4
                s = var4.get()
                s = int(s)
                item4.delete(0, END)
                count4 = s
                count4 += 1
                item4.insert(0, count4)

            def I5():
                global count5
                s = var5.get()
                s = int(s)
                item5.delete(0, END)
                count5 = s
                count5 += 1
                item5.insert(0, count5)

            def I6():
                global count6
                s = var6.get()
                s = int(s)
                item6.delete(0, END)
                count6 = s
                count6 += 1
                item6.insert(0, count6)

            def I7():
                global count7
                s = var7.get()
                s = int(s)
                item7.delete(0, END)
                count7 = s
                count7 += 1
                item7.insert(0, count7)

            def I8():
                global count8
                s = var8.get()
                s = int(s)
                item8.delete(0, END)
                count8 = s
                count8 += 1
                item8.insert(0, count8)

            def I9():
                global count9
                s = var9.get()
                s = int(s)
                item9.delete(0, END)
                count9 = s
                count9 += 1
                item9.insert(0, count9)

            def I10():
                global count10
                s = var10.get()
                s = int(s)
                item10.delete(0, END)
                count10 = s
                count10 += 1
                item10.insert(0, count10)

            def I11():
                global count11
                s = var11.get()
                s = int(s)
                item11.delete(0, END)
                count11 = s
                count11 += 1
                item11.insert(0, count11)

            def I12():
                global count12
                s = var12.get()
                s = int(s)
                item12.delete(0, END)
                count12 = s
                count12 += 1
                item12.insert(0, count12)


        #  CREATED TIME & DATE FUNCTIONS

            def dateotime():
                dt = datetime.datetime.now()
                string = dt.strftime('DATE: %d-%m-%y || TIME: %H:%M:%S%p')
                DT.config(text=string)
                DT.after(1000, dateotime)

            def total_price():
                global counto0
                global counto1
                global counto2
                global counto3
                global counto4
                global counto5
                global counto6
                global counto7
                global counto8
                global counto9
                global counto10
                global counto11
                global counto12
                counto0 = var0.get()
                counto0 = int(counto0)
                counto1 = var1.get()
                counto1 = int(counto1)
                counto2 = var2.get()
                counto2 = int(counto2)
                counto3 = var3.get()
                counto3 = int(counto3)
                counto4 = var4.get()
                counto4 = int(counto4)
                counto5 = var5.get()
                counto5 = int(counto5)
                counto6 = var6.get()
                counto6 = int(counto6)
                counto7 = var7.get()
                counto7 = int(counto7)
                counto8 = var8.get()
                counto8 = int(counto8)
                counto9 = var9.get()
                counto9 = int(counto9)
                counto10 = var10.get()
                counto10 = int(counto10)
                counto11 = var11.get()
                counto11 = int(counto11)
                counto12 = var12.get()
                counto12 = int(counto12)
                global sum
                sum = counto0 * 500 + counto1 * 300 + counto2 *250 + counto3 * 550 + counto4 * 350 + counto5 * 600 + counto6 * 650 + counto7 * 150 + counto8 * 450 + counto9 * 200 + counto10 * 40 + counto11 * 40 + counto12 * 40
                global summa
                summa =  counto0+counto1+counto2+counto3+counto4+counto5+counto6+counto7+counto8+counto9+counto10+counto11+counto12
                total1.delete(0, END)
                total1.insert(0, sum)

        # CREATED DATE & TIME LABEL

            DT = Label(root, font=('calibri', 15, 'bold'), bg="grey")
            DT.place(x=520, y=60, anchor='nw')

        # functions for menuemp
            def logout():
                root.destroy()
                main()

########################################################### menue page paused #################################################################################

########################################################### bill layout starts  #################################################################################
            def bill():
                #wrtoncsv()
                # BILL PAGE WINDOW CONFIGURATION

                bip = Tk()
                bip.geometry("600x600")
                bip.title("BILL")
                bip.configure(background="grey")

                # bill page distroy function

                def quito():
                    global count0, count1, count2, count3, count4, count5, count6, count7, count8, count9, count10, count11, count12
                    count0, count1, count2, count3, count4, count5, count6, count7, count8, count9, count10, count11, count12 = [
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

                    total1.delete(0, END)
                    total1.insert(0, 0)

                    item0.delete(0, END)
                    item0.insert(0, 0)

                    item1.delete(0, END)
                    item1.insert(0, 0)

                    item2.delete(0, END)
                    item2.insert(0, 0)

                    item3.delete(0, END)
                    item3.insert(0, 0)

                    item4.delete(0, END)
                    item4.insert(0, 0)

                    item5.delete(0, END)
                    item5.insert(0, 0)

                    item6.delete(0, END)
                    item6.insert(0, 0)

                    item7.delete(0, END)
                    item7.insert(0, 0)

                    item8.delete(0, END)
                    item8.insert(0, 0)

                    item9.delete(0, END)
                    item9.insert(0, 0)

                    item10.delete(0, END)
                    item10.insert(0, 0)

                    item11.delete(0, END)
                    item11.insert(0, 0)

                    item12.delete(0, END)
                    item12.insert(0, 0)

                    cosname.delete(0, END)
                    cosnumber.delete(0, END)
                    bip.destroy()

                # TIME & DATE DEFINATION FOR DILL PAGE

                def dateotime():
                    dt = datetime.datetime.now()
                    string = dt.strftime('%d-%m-%y || %H:%M:%S%p')
                    DT.config(text=string)
                    DT.after(1000, dateotime)

                monthn= date.today().month
                print(monthn)

                yearn = date.today().year
                print(yearn)

                # DATE & TIME LABEL

                DT = Label(bip, font=(10), bg="grey")
                DT.place(x=425, y=28, anchor='nw')

                # TITTLE LABEL FOR BILL

                tittle1 = Label(bip, text="FINAL BILL", font=("Helvetica", 20, "bold italic"), fg="blue", bg="grey")
                tittle1.place(x=235, y=10)

                # DESIGN LABEL

                itii = Label(bip, font=('aria', 15, 'bold'),
                             text="------------------------------------------------------------------------------------",
                             fg="black", bg="grey", bd=5)
                itii.place(x=0, y=50)

                # LABELS FOR  ITEMS , QUANTITIES & PRICE IN BILL PAGE

                iti = Label(bip, font=('aria', 15, 'bold'), text="ITEMS", bg="grey", fg="black", bd=5)
                iti.place(x=120, y=80)
                iti = Label(bip, font=('aria', 15, 'bold'), text=" QUANTITIES", bg="grey", fg="black", anchor=W)
                iti.place(x=280, y=80)
                iti = Label(bip, font=('aria', 15, 'bold'), text="PRICE", bg="grey", fg="black", anchor=W)
                iti.place(x=490, y=80)

                # DESIGN LABEL

                itii = Label(bip, font=('aria', 15, 'bold'),
                             text="------------------------------------------------------------------------------------",
                             fg="black", bg="grey", bd=5)
                itii.place(x=0, y=105)

                # global inputs for the billpage

                global counto0
                global counto1
                global counto2
                global counto3
                global counto4
                global counto5
                global counto6
                global counto7
                global counto8
                global counto9
                global counto10
                global counto11
                global counto12
                global sum
                global summa

                # ALL DATA LABELS ACCORDING TO HEDDINGS MENTIONED & SELECTED BY USER FROM MAIN PAGE

                it0 = Label(bip, font=('aria', 15, 'bold'), text="Pepperoni Pizza", bg="grey", fg="royalblue3",
                            anchor=W)
                it0.place(x=80, y=130)
                it0 = Label(bip, font=('aria', 15, 'bold'), text=counto0, bg="grey", fg="royalblue3", anchor=W)
                it0.place(x=340, y=130)
                it0 = Label(bip, font=('aria', 15, 'bold'), text=counto0 * 500, bg="grey", fg="royalblue3", anchor=W)
                it0.place(x=515, y=130)

                it1 = Label(bip, font=('aria', 15, 'bold'), text="Mushroom Pizza", bg="grey", fg="royalblue3",
                            anchor=W)
                it1.place(x=80, y=160)
                it1 = Label(bip, font=('aria', 15, 'bold'), text=counto1, bg="grey", fg="royalblue3", anchor=W)
                it1.place(x=340, y=160)
                it1 = Label(bip, font=('aria', 15, 'bold'), text=counto1 * 300, bg="grey", fg="royalblue3", anchor=W)
                it1.place(x=515, y=160)

                it2 = Label(bip, font=('aria', 15, 'bold'), text="Onions Pizza", bg="grey", fg="royalblue3", anchor=W)
                it2.place(x=80, y=190)
                it2 = Label(bip, font=('aria', 15, 'bold'), text=counto2, bg="grey", fg="royalblue3", anchor=W)
                it2.place(x=340, y=190)
                it2 = Label(bip, font=('aria', 15, 'bold'), text=counto2 * 250, bg="grey", fg="royalblue3", anchor=W)
                it2.place(x=515, y=190)

                it3 = Label(bip, font=('aria', 15, 'bold'), text="Sausage Pizza", bg="grey", fg="royalblue3",
                            anchor=W)
                it3.place(x=80, y=220)
                it3 = Label(bip, font=('aria', 15, 'bold'), text=counto3, bg="grey", fg="royalblue3", anchor=W)
                it3.place(x=340, y=220)
                it3 = Label(bip, font=('aria', 15, 'bold'), text=counto3 * 550, bg="grey", fg="royalblue3", anchor=W)
                it3.place(x=515, y=220)

                it4 = Label(bip, font=('aria', 15, 'bold'), text="Classic Italian Pizza", bg="grey", fg="royalblue3",
                            anchor=W)
                it4.place(x=80, y=250)
                it4 = Label(bip, font=('aria', 15, 'bold'), text=counto4, bg="grey", fg="royalblue3", anchor=W)
                it4.place(x=340, y=250)
                it4 = Label(bip, font=('aria', 15, 'bold'), text=counto4 * 350, bg="grey", fg="royalblue3", anchor=W)
                it4.place(x=515, y=250)

                it5 = Label(bip, font=('aria', 15, 'bold'), text="Extra Cheese Pizza", bg="grey", fg="royalblue3",
                            anchor=W)
                it5.place(x=80, y=280)
                it5 = Label(bip, font=('aria', 15, 'bold'), text=counto5, fg="royalblue3", bg="grey", anchor=W)
                it5.place(x=340, y=280)
                it5 = Label(bip, font=('aria', 15, 'bold'), text=counto5 * 600, bg="grey", fg="royalblue3", anchor=W)
                it5.place(x=515, y=280)

                it6 = Label(bip, font=('aria', 15, 'bold'), text="Black Olives Pizza", bg="grey", fg="royalblue3",
                            anchor=W)
                it6.place(x=80, y=310)
                it6 = Label(bip, font=('aria', 15, 'bold'), text=counto6, bg="grey", fg="royalblue3", anchor=W)
                it6.place(x=340, y=310)
                it6 = Label(bip, font=('aria', 15, 'bold'), text=counto6 * 650, bg="grey", fg="royalblue3", anchor=W)
                it6.place(x=515, y=310)

                it7 = Label(bip, font=('aria', 15, 'bold'), text="Green Peppers Pizza", bg="grey", fg="royalblue3",
                            anchor=W)
                it7.place(x=80, y=340)
                it7 = Label(bip, font=('aria', 15, 'bold'), text=counto7, fg="royalblue3", bg="grey", anchor=W)
                it7.place(x=340, y=340)
                it7 = Label(bip, font=('aria', 15, 'bold'), text=counto7 * 150, bg="grey", fg="royalblue3", anchor=W)
                it7.place(x=515, y=340)

                it8 = Label(bip, font=('aria', 15, 'bold'), text="Pineapple Pizza", fg="royalblue3", bg="grey",
                            anchor=W)
                it8.place(x=80, y=370)
                it8 = Label(bip, font=('aria', 15, 'bold'), text=counto8, fg="royalblue3", bg="grey", anchor=W)
                it8.place(x=340, y=370)
                it8 = Label(bip, font=('aria', 15, 'bold'), text=counto8 * 450, fg="royalblue3", bg="grey", anchor=W)
                it8.place(x=515, y=370)

                it9 = Label(bip, font=('aria', 15, 'bold'), text="Spinach Pizza", bg="grey", fg="royalblue3",
                            anchor=W)
                it9.place(x=80, y=400)
                it9 = Label(bip, font=('aria', 15, 'bold'), text=counto9, bg="grey", fg="royalblue3", anchor=W)
                it9.place(x=340, y=400)
                it9 = Label(bip, font=('aria', 15, 'bold'), text=counto9 * 200, bg="grey", fg="royalblue3", anchor=W)
                it9.place(x=515, y=400)

                itcoke = Label(bip, font=('aria', 15, 'bold'), text="Coke", bg="grey", fg="royalblue3", anchor=W)
                itcoke.place(x=80, y=430)
                itcoke = Label(bip, font=('aria', 15, 'bold'), text=counto10, bg="grey", fg="royalblue3", anchor=W)
                itcoke.place(x=340, y=430)
                itcoke = Label(bip, font=('aria', 15, 'bold'), text=counto10 * 40, bg="grey", fg="royalblue3", anchor=W)
                itcoke.place(x=515, y=430)

                ittup = Label(bip, font=('aria', 15, 'bold'), text="Thums Up", bg="grey", fg="royalblue3", anchor=W)
                ittup.place(x=80, y=460)
                ittup = Label(bip, font=('aria', 15, 'bold'), text=counto11, bg="grey", fg="royalblue3", anchor=W)
                ittup.place(x=340, y=460)
                ittup = Label(bip, font=('aria', 15, 'bold'), text=counto11 * 40, bg="grey", fg="royalblue3", anchor=W)
                ittup.place(x=515, y=460)

                itpep = Label(bip, font=('aria', 15, 'bold'), text="Pepsi", fg="royalblue3", bg="grey", anchor=W)
                itpep.place(x=80, y=490)
                itpep = Label(bip, font=('aria', 15, 'bold'), text=counto12, fg="royalblue3", bg="grey", anchor=W)
                itpep.place(x=340, y=490)
                itpep = Label(bip, font=('aria', 15, 'bold'), text=counto12 * 40, fg="royalblue3", bg="grey", anchor=W)
                itpep.place(x=515, y=490)

                # DESIGN LABEL

                itii = Label(bip, font=('aria', 15, 'bold'),
                             text="------------------------------------------------------------------------------------",
                             fg="black", bg="grey", bd=5)
                itii.place(x=0, y=520)

                # DISPLAY OF TOTAL PRICE LABEL

                itt = Label(bip, font=('aria', 15, 'bold'), text=" Total Price:", fg="black", bg="grey", anchor=W)
                itt.place(x=380, y=550)
                itt = Label(bip, font=('aria', 15, 'bold'), text=sum, fg="black", bg="grey", anchor=W)
                itt.place(x=515, y=550)

                # DISPLAY OF TOTAL QUANTITY

                itti = Label(bip, font=('aria', 15, 'bold'), text=" Total Qty.:", fg="black", bg="grey", anchor=W)
                itti.place(x=210, y=550)
                itti = Label(bip, font=('aria', 15, 'bold'), text=summa, fg="black", bg="grey", anchor=W)
                itti.place(x=340, y=550)

                # DATA BASE ELEMENTS

                global cosname
                global cosnumber
                data1 = cosname.get()
                data2 = cosnumber.get()
                sql = "INSERT INTO pizza_db(customer_name,customer_contact,Pepperoni_Pizza,Mushroom_Pizza,Onions_Pizza,Sausage_Pizza,Classic_Italian_Pizza,Extra_Cheese_Pizza,Black_Olives_Pizza,Green_Peppers_Pizza,Pineapple_Pizza,Spinach_Pizza,Coke,Thums_Up,Pepsi,total_items,total_price,monthn,yearn)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                d = (data1, data2, counto0, counto1, counto2, counto3, counto4, counto5, counto6, counto7, counto8, counto9, counto10, counto11, counto12, summa, sum, monthn, yearn)
                cursor.execute(sql, d)
                conn.commit()

                # CUSTOMER DETAIL LABELS

                dot = Label(bip, text="DATE || TIME", font=(10), bg="grey")
                dot.place(x=445, y=10, anchor='nw')

                det = Label(bip, text="NAME:", font=(2), bg="grey")
                det.place(x=0, y=10, anchor='nw')

                det1 = Label(bip, text="CONTACT:", font=(2), bg="grey")
                det1.place(x=0, y=40, anchor='nw')

                na = Label(bip, text=data1, font=(2), bg="grey")
                na.place(x=55, y=8, anchor='nw')

                nu = Label(bip, text=data2, font=(2), bg="grey")
                nu.place(x=85, y=40, anchor='nw')

                quitofy = Button(bip, text="DONE", bg="red",width=10,bd=5,command=quito)
                quitofy.place(x=80,y=550)

                dateotime()
                bip.mainloop()


    ########################################################### bill layout ends  ###################################################################################

############################################################# menue page continues ##############################################################################
        # labels for menue page

            nam = Label(root, text="CUSTOMER NAME:", font=("Helvetica", 15, "bold italic"), fg="BLACK", bg="grey")
            nam.place(x=10, y=20)

            num = Label(root, text="CUSTOMER NUMBER:", font=("Helvetica", 15, "bold italic"), fg="BLACK", bg="grey")
            num.place(x=10, y=60)

            tittle = Label(root, text="PIZZA HUB", font=("Helvetica", 20, "bold italic"), fg="red", bg="grey")
            tittle.place(x=600, y=20)

            MENUE1 = Label(root, text="OUR AUTHENTIC PIZZA MENU", font=("bold", 15), fg="yellow", bg="grey")
            MENUE1.place(x=400, y=100)

            MENUE2 = Label(root, text="EXTRA ADD-ONS (BREVRAGES)", font=("bold", 10), fg="YELLOW", bg="grey")
            MENUE2.place(x=1110, y=100)

            ITEM = Label(root, text="ITEMS", font=("bold", 15), fg="blue", bg="grey")
            ITEM.place(x=114, y=150)

            QUANTITY = Label(root, text="QUANTITIES", font=("bold", 15), fg="blue", bg="grey")
            QUANTITY.place(x=375, y=150)

            ITEM1 = Label(root, text="ITEMS", font=("bold", 15), fg="blue", bg="grey")
            ITEM1.place(x=614, y=150)

            QUANTITY1 = Label(root, text="QUANTITIES", font=("bold", 15), fg="blue", bg="grey")
            QUANTITY1.place(x=873, y=150)

            ITEM2 = Label(root, text="ITEMS", font=("bold", 12), fg="blue", bg="grey")
            ITEM2.place(x=1060, y=150)

            QUANTITY2 = Label(root, text="QUANTITIES", font=("bold", 12), fg="blue", bg="grey")
            QUANTITY2.place(x=1260, y=150)

            M0 = Label(root, text=("Pepperoni Pizza  \t    X\n price:500per"), font=("bold", 10), bg="grey")
            M0.place(x=200, y=214)

            M1 = Label(root, text="Mushroom Pizza  \t    X\n price:300per", font=("bold", 10), bg="grey")
            M1.place(x=200, y=314)

            M2 = Label(root, text="Onions Pizza  \t    X\n price:250per", font=("bold", 10), bg="grey")
            M2.place(x=200, y=414)

            M3 = Label(root, text="Sausage Pizza  \t    X\n price:550per", font=("bold", 10), bg="grey")
            M3.place(x=200, y=514)

            M4 = Label(root, text="Classic Italian Pizza   X\n price:350per", font=("bold", 10), bg="grey")
            M4.place(x=200, y=614)

            M5 = Label(root, text="Extra Cheese Pizza    X\n price:600per", font=("bold", 10), bg="grey")
            M5.place(x=700, y=214)

            M6 = Label(root, text="Black Olives Pizza\t     X\n price:650per", font=("bold", 10), bg="grey")
            M6.place(x=700, y=314)

            M7 = Label(root, text="Green Peppers Pizza  X\n price:150per", font=("bold", 10), bg="grey")
            M7.place(x=700, y=414)

            M8 = Label(root, text="Pineapple Pizza\t     X\n price:450per", font=("bold", 10), bg="grey")
            M8.place(x=700, y=514)

            M9 = Label(root, text="Spinach Pizza \t     X\n price:200per", font=("bold", 10), bg="grey")
            M9.place(x=700, y=614)

            M10 = Label(root, text="Coke\t\tx\n price:40rs/500ml", font=("bold", 10), bg="grey")
            M10.place(x=1140, y=220)

            M11 = Label(root, text="Thums Up\tx\n price:40rs/500ml", font=("bold", 10), bg="grey")
            M11.place(x=1140, y=320)

            M12 = Label(root, text="Pepsi\t\tx\n price:40rs/500ml", font=("bold", 10), bg="grey")
            M12.place(x=1140, y=420)

            Total1 = Label(root, text="Total Price", fg="blue", font=("bold", 20), bg="grey")
            Total1.place(x=1025, y=530)

        # entries for menue

            item0 = Entry(root,textvariable=var0, bd=5)
            item0.place(x=370,y=220)

            item1 = Entry(root,textvariable=var1, bd=5)
            item1.place(x=370, y=320)

            item2 = Entry(root,textvariable=var2, bd=5)
            item2.place(x=370, y=420)

            item3 = Entry(root,textvariable=var3, bd=5)
            item3.place(x=370, y=520)

            item4 = Entry(root, textvariable=var4,bd=5)
            item4.place(x=370, y=620)

            item5 = Entry(root,textvariable=var5, bd=5)
            item5.place(x=870, y=220)

            item6 = Entry(root,textvariable=var6, bd=5)
            item6.place(x=870, y=320)

            item7 = Entry(root,textvariable=var7, bd=5)
            item7.place(x=870, y=420)

            item8 = Entry(root,textvariable=var8, bd=5)
            item8.place(x=870, y=520)

            item9 = Entry(root,textvariable=var9, bd=5)
            item9.place(x=870, y=620)

            item10 = Entry(root, textvariable=var10,bd=5, width=8)
            item10.place(x=1280, y=220)

            item11 = Entry(root, textvariable=var11,bd=5, width=8)
            item11.place(x=1280, y=320)

            item12 = Entry(root, textvariable=var12,bd=5, width=8)
            item12.place(x=1280, y=420)

            total1 = Entry(root, bd=5,textvariable=tvar,)
            total1.place(x=1030, y=575)

            global cosname
            cosname = Entry(root, bd=5, width=30)
            cosname.place(x=250, y=20)

            global cosnumber
            cosnumber = Entry(root, bd=5, width=30)
            cosnumber.place(x=250, y=60)

        #buttons for the menu page

            tot=Button(root,text="TOTAL",width=17,bg="red",bd=5,command=total_price)
            tot.place(x=1180, y=575)

            order = Button(root, text="PLACE ORDER", width=17, bg="red", bd=5,command=bill)
            order.place(x=1180, y=620)

            clear = Button(root, text="CLEAR", width=17, bg="red", bd=5,command=clear)
            clear.place(x=1030, y=620)

            logoutmenue = Button(root, text="LOGOUT", width=15, bg="red", bd=5, command=logout)
            logoutmenue.place(x=1180, y=20)

        # imaged buttons for menue list

            Button(root, image=item0a, bd=4,command=I0).place(x=100, y=200)

            Button(root, text="1", image=item1a, bd=4,command=I1).place(x=100, y=300)

            Button(root, text="1", image=item2a, bd=4,command=I2).place(x=100, y=400)

            Button(root, text="1", image=item3a, bd=4,command=I3).place(x=100, y=500)

            Button(root, text="1", image=item4a, bd=4,command=I4).place(x=100, y=600)

            Button(root, text="1", image=item5a, bd=4,command=I5).place(x=600, y=200)

            Button(root, text="1", image=item6a, bd=4,command=I6).place(x=600, y=300)

            Button(root, text="1", image=item7a, bd=4,command=I7).place(x=600, y=400)

            Button(root, text="1", image=item8a, bd=4,command=I8).place(x=600, y=500)

            Button(root, text="1", image=item9a, bd=4,command=I9).place(x=600, y=600)

            Button(root, text="1", image=item10a, bd=4,command=I10).place(x=1040, y=200)

            Button(root, text="1", image=item11a, bd=4,command=I11).place(x=1040, y=300)

            Button(root, text="1", image=item12a, bd=4,command=I12).place(x=1040, y=400)

            dateotime()
            root.mainloop()
################9##################################################### menue page ends here ####################################################################

##################################################################### employee login page continues ############################################################

    # labels & buttons & entries

        head1 = Label(toor1, text="EMPLOYEE LOGIN", font=("Helvetica", 35, "bold italic"), fg="blue", bg="grey")
        head1.place(x=40, y=100)

        username = Label(toor1, text="Username :", font=("Helvetica", 15, "bold"), fg="black", bg="grey")
        username.place(x=100, y=220)

        entryusername = Entry(toor1, bd=5)
        entryusername.place(x=270, y=222)

        password = Label(toor1, text="Password :", font=("Helvetica", 15, "bold"), fg="black", bg="grey")
        password.place(x=100, y=280)

        entrypassword = Entry(toor1, bd=5,show ="*")
        entrypassword.place(x=270, y=282)

        emplogin = Button(toor1, text="LOGIN", width=15, bg="red", bd=5,command= condition)
        emplogin.place(x=277, y=350)

        backmenue= Button(toor1, text="BACK", width=15, bg="red", bd=5,command= back)
        backmenue.place(x=120, y=350)


        dateotime()
        toor1.mainloop()

####################################################### employee login page ends ##################################################

######################################################## main page continues #######################################################
# CREATED DATE & TIME LABEL

    DT=Label(top,font=('calibri',20,'bold'),bg="grey")
    DT.place(x=70,y=90,anchor='nw')

# labels & buttons

    tittle =Label(top, text="PIZZA HUB", font=("Helvetica",30, "bold italic"),fg="red",bg="grey")
    tittle.place(x=1000, y=80)

    get1 =Label(top, text="WELCOME TO YOUR RESTAURANT MANAGEMENT SYSTEM", font=("Helvetica",30, "bold italic"),fg="blue",bg="grey")
    get1.place(x=100, y=200)

    get2 =Label(top, text="-we made it easy for you !!!!", font=("Helvetica",20, "bold italic"),fg="yellow",bg="grey")
    get2.place(x=950, y=240)

    get3 =Label(top, text="LET'S LOGIN NOW !!!!", font=("Helvetica",40, "bold italic"),fg="purple",bg="grey")
    get3.place(x=100, y=300)


    get3 =Label(top, text="Employee Login", font=("Helvetica",20, "bold italic"),fg="black",bg="grey")
    get3.place(x=560, y=560)




    Button(top,image=employee,bd=4,command = emplogin).place(x=600,y=450)

    quit = Button(top, text="EXIT", width=15, bg="red", bd=5, command= top.destroy)
    quit.place(x=1180, y=20)

    dateotime()
    top.mainloop()
main()
########################################################################### main page ends ################################################################