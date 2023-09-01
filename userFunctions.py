from tkinter import *
from tkinter import messagebox

 
userData=['','','','','','']
def _error(title,mes):
    messagebox.showerror(title,mes)
    
def _info(title,mes):
    messagebox.showinfo(title,mes)

def update_database():
    global userData
    lines=[]
    with open('.\database.txt','r') as file:
        lines=file.readlines()
    with open('.\database.txt','w') as file:
        for i in range(len(lines)):
            if lines[i].split('||')[0]==userData[0] :
                lines[i]="{}||{}||{}||{}||{}||{}{}".format(userData[0],userData[1],userData[2],userData[3],userData[4],userData[5],'\n')
                break
        file.writelines(lines)
                  
def checkUserData(id):
    with open('.\database.txt','r') as file:
        for line in file:
            if line.split('||')[0]==id :
                if not line.split('||')[-1][:-1]=='t':
                    return 'locked'
                data=line[:-1]
                return list(data.split('||'))
    return 'not-found'

def getDataFromDB(id):
    with open('.\database.txt','r') as file:
        for line in file:
            if line.split('||')[0]==id :
                data=line[:-1]
                return list(data.split('||'))
    return []
      
def ATM_Actuator_Out(amount):
    global l6
    if not int(amount) % 100 ==0 :
        _error("Invaild Amount",'The allowed values are multiple of 100L.E')
        
    elif int(amount) >5000:
        _error("Invaild Amount",'Maximum allowed value per transaction is 5000 L.E')
    
    elif int(amount) > int(userData[-3]):
        _error("Invaild Amount",'{} is bigger than the current Balance'.format(int(amount)))
    
    else:
        userData[-3]=int(userData[-3])-int(amount)
        _info("Succes","The amount was withdrawed Succesfully")
        l6.config(text=userData[-3])
        accWithd.destroy()
        update_database()
          
def change_password(pass1,pass2):
    if len(pass1)>4:
        _error("Password Error",'Password length must be 4 digit like 1234')
        return
    if not pass1==pass2:
        _error("Password Error",'Password and Re-password must be matched')
        return
    userData[2]=pass1  
    update_database()
    _info("Password Changed","Your Password Has Been Changed")
    accPass.destroy()
       
def changePasswordWindow():
    global accPass
    accPass = Toplevel()
    accPass.title(userData[0])
    WIDTH = 300
    HEIGHT = 400
    x = int((accPass.winfo_screenwidth() / 2) - (WIDTH / 2))
    y = int((accPass.winfo_screenheight() / 2) - (HEIGHT / 2))
    accPass.geometry(f'{WIDTH}x{HEIGHT}+{x}+{y}')
    
    passNewLabel = Label(accPass,font=20,text = "Passwrd:",justify="center")
    passNewLabel.config(font=('callibri', 24))

    passNewEntry = Entry(accPass,justify="center")
    passNewEntry.config(font=('callibri', 18))
    
    
    passNewReLabel = Label(accPass,font=20,text = "Re-Passwrd:",justify="center")
    passNewReLabel.config(font=('callibri', 24))

    passNewReEntry = Entry(accPass,justify="center")
    passNewReEntry.config(font=('callibri', 18))

    but2=Button(accPass,text="Change",command=lambda: change_password(passNewEntry.get(),passNewReEntry.get()))
    
    but2.config(font=('callibri', 18))
    passNewLabel.pack(pady=10)
    passNewEntry.pack(pady=20)
    passNewReLabel.pack(pady=10)
    passNewReEntry.pack(pady=20)
    but2.pack(pady=10)
    
    accPass.mainloop()    
    
def fawryAmountWindow(type):
    global accFawryAmt
    accFawryAmt = Toplevel()
    accFawryAmt.title(userData[0])
    WIDTH = 300
    HEIGHT = 400
    x = int((accFawryAmt.winfo_screenwidth() / 2) - (WIDTH / 2))
    y = int((accFawryAmt.winfo_screenheight() / 2) - (HEIGHT / 2))
    accFawryAmt.geometry(f'{WIDTH}x{HEIGHT}+{x}+{y}')
    
    phoneNumLabel = Label(accFawryAmt,font=20,text = "Phone Number:",justify="center")
    phoneNumLabel.config(font=('callibri', 24))

    phoneNumEntry = Entry(accFawryAmt,justify="center")
    phoneNumEntry.config(font=('callibri', 18))
    
    
    amountLabel = Label(accFawryAmt,font=20,text = "Amount:",justify="center")
    amountLabel.config(font=('callibri', 24))

    amountEntry = Entry(accFawryAmt,justify="center")
    amountEntry.config(font=('callibri', 18))

    but2=Button(accFawryAmt,text="Change",command=lambda: recharge_via_fawry(type,phoneNumEntry.get(),amountEntry.get()))
    
    but2.config(font=('callibri', 18))
    phoneNumLabel.pack(pady=10)
    phoneNumEntry.pack(pady=20)
    amountLabel.pack(pady=10)
    amountEntry.pack(pady=20)
    but2.pack(pady=10)
    
    accFawryAmt.mainloop()    
     
def fawryWindow():
    global accFawry
    accFawry = Toplevel()
    accFawry.title(userData[0])
    WIDTH = 300
    HEIGHT = 350
    x = int((accFawry.winfo_screenwidth() / 2) - (WIDTH / 2))
    y = int((accFawry.winfo_screenheight() / 2) - (HEIGHT / 2))
    accFawry.geometry(f'{WIDTH}x{HEIGHT}+{x}+{y}')
    

    but1=Button(accFawry,text="Orange",command=lambda: fawryAmountWindow("Orange"))
    but2=Button(accFawry,text="Etisalat",command=lambda: fawryAmountWindow("Etisalat"))
    but3=Button(accFawry,text="Vodafone",command=lambda: fawryAmountWindow("Vodafone"))
    but4=Button(accFawry,text="We",command=lambda: fawryAmountWindow("We"))
    
    but1.config(font=('callibri', 18),fg='orange')
    but1.pack(pady=10)
    but2.config(font=('callibri', 18),fg="green")
    but2.pack(pady=10)
    but3.config(font=('callibri', 18),fg="red")
    but3.pack(pady=10)
    but4.config(font=('callibri', 18),fg="blue")
    but4.pack(pady=10)
    
    accFawry.mainloop()    

def recharge_via_fawry(type,phone,amount):
    if not len(phone)==11:
        _error("Invalid Phone Number","{} is not a Valid Phone Number".format(phone))
        return
    elif int(amount) > int(userData[-3]):
        _error("Invalid Amount",'{} is bigger than the current Balance'.format(amount))
  
    elif  not ( (type=="Orange" and phone[0]=="0" and phone[1]=="1" and phone[2]=="2") or (type=="Etisalat" and phone[0]=="0" and phone[1]=="1" and phone[2]=="1") or (type=="Vodafone" and phone[0]=="0" and phone[1]=="1" and phone[2]=="0") or (type=="We" and phone[0]=="0" and phone[1]=="1" and phone[2]=="5") ): 
        _error("Invalid Phone Number","{} is not a Valid {} Number".format(phone,type))
        return
    else :
        userData[-3]=int(userData[-3])-int(amount)
        update_database()
        _info("Success","{} was charged to {} succesfully".format(amount,phone))
        accFawryAmt.destroy()
        accFawry.destroy()
        
def unlock_user(id):
    global userData
    userData=getDataFromDB(id)
    userData[-2]=3
    userData[-1]='t'
    update_database()
    
def lock_user(id):
    global userData
    userData=getDataFromDB(id)
    userData[-2]=0
    userData[-1]='f'
    update_database()
    
def checkPassword(id,password):
    global userData
    with open('.\database.txt','r') as file:
        for line in file:
            if line.split('||')[0]==id :
                if line.split('||')[2]==password:
                    data=line[:-1]
                    userData=list(data.split('||'))
                    return True
    return False  
      
def on_closing():
    global accWin
    mainPage.deiconify()
    accWin.destroy()

def destroyAll():
    accWin.destroy()
    mainPage.destroy()

def withdraw():
    global accWithd
    accWithd = Toplevel()
    accWithd.title(userData[0])
    WIDTH = 300
    HEIGHT = 200
    x = int((accWithd.winfo_screenwidth() / 2) - (WIDTH / 2))
    y = int((accWithd.winfo_screenheight() / 2) - (HEIGHT / 2))
    accWithd.geometry(f'{WIDTH}x{HEIGHT}+{x}+{y}')
    
    amountLabel = Label(accWithd,font=20,text = "Amount:",justify="center")
    amountLabel.config(font=('callibri', 24))

    amountEntry = Entry(accWithd,justify="center")
    amountEntry.config(font=('callibri', 18))

    but2=Button(accWithd,text="witherdraw",command=lambda: ATM_Actuator_Out(amountEntry.get()))
    but2.config(font=('callibri', 18))
    amountLabel.pack(pady=10)
    amountEntry.pack(pady=20)
    but2.pack(pady=10)
    
    accWithd.mainloop()
    
def createAccountWindow():
    global userData
    global accWin
    global l6
    accWin = Toplevel()
    accWin.title(userData[1])
    WIDTH = 500
    HEIGHT = 230
    x = int((accWin.winfo_screenwidth() / 2) - (WIDTH / 2))
    y = int((accWin.winfo_screenheight() / 2) - (HEIGHT / 2))
    accWin.geometry(f'{WIDTH}x{HEIGHT}+{x}+{y}')

    l1 = Label(accWin, text = "Acc. Number:", width=14,justify="center",font=('callibri', 16))
    l1.grid(row = 0, column = 0, pady = 3,padx=3)
    l2 = Label(accWin, text = userData[0], width=20,justify="center",font=('callibri', 18), fg='#fA7A8C')
    l2.grid(row = 0, column = 1, pady = 3,padx=3)  
    
    l3 = Label(accWin, text = "Acc. Name:", width=14,justify="center",font=('callibri', 16))
    l3.grid(row = 1, column = 0, pady = 3,padx=3)
    l4 = Label(accWin, text = userData[1], width=30,justify="center",font=('callibri', 14), fg='blue')
    l4.grid(row = 1, column = 1, pady = 3,padx=3)  
    
    l5 = Label(accWin, text = "Acc. Balance:", width=14,justify="center",font=('callibri', 16))
    l5.grid(row = 2, column = 0, pady = 3,padx=3)
    l6 = Label(accWin, text = userData[3], width=20,justify="center",font=('callibri', 18), fg='green')
    l6.grid(row = 2, column = 1, pady = 3,padx=3) 
    
    butOut = Button(accWin,text="Withdraw", width=15,justify="center",font=('callibri', 16),command=withdraw)
    butOut.grid(row = 3, column = 0, pady = 3,padx=3)
    butPass = Button(accWin,text="Change Password", width=15,justify="center",font=('callibri', 16),command=changePasswordWindow)
    butPass.grid(row = 3, column = 1, pady = 3,padx=3) 

    butFawry = Button(accWin,text="Fawry Service", width=15,justify="center",font=('callibri', 16),command=fawryWindow)
    butFawry.grid(row = 4, column = 0, pady = 3,padx=3)
    
    butExist = Button(accWin,text="Exist", width=15,justify="center",font=('callibri', 16),fg="red",command=destroyAll)
    butExist.grid(row = 4, column = 1, pady = 3,padx=3) 


    accWin.protocol("WM_DELETE_WINDOW", on_closing)
    accWin.mainloop()

def createAccVerifyWindow(id):
    global accVerify
    global passEntry
    accVerify = Toplevel()
    accVerify.title(id)
    WIDTH = 300
    HEIGHT = 200
    x = int((accVerify.winfo_screenwidth() / 2) - (WIDTH / 2))
    y = int((accVerify.winfo_screenheight() / 2) - (HEIGHT / 2))
    accVerify.geometry(f'{WIDTH}x{HEIGHT}+{x}+{y}')
    
    passLabel = Label(accVerify,font=20,text = "Password :",justify="center")
    passLabel.config(font=('callibri', 24))
    
    passEntry = Entry(accVerify,justify="center",show='*')
    passEntry.config(font=('callibri', 18),width=4)

    but2=Button(accVerify,text="Enter",command=lambda: verifyUser(id,passEntry.get()))
    but2.config(font=('callibri', 18))
    passLabel.pack(pady=10)
    passEntry.pack(pady=20)
    but2.pack(pady=10)
    
    accVerify.mainloop()

def verifyUser(id,password):
    global idEntry
    global accVerify
    global userData
    userData=getDataFromDB(id)
    res=checkPassword(id,password)
    if res==False:
        if int(userData[-2]) > 1 :
            userData[-2]=int(userData[-2])-1
            update_database()
            passEntry.delete(0,END)
            _error("Wrog Password","Remaining Try times = {}".format(int(userData[-2])))
        elif int(userData[-2]) == 1 :
            userData[-2]=int(userData[-2])-1
            userData[-1]='f'
            update_database()
            passEntry.delete(0,END)
            _error("Account Locked","Remaining Try times = 0 Account was Locked !")
    else :
        userData[-2]=3
        update_database()
        accVerify.destroy()
        createAccountWindow()
              
def checkUserId():
    global userData
    global idEntry
    id=idEntry.get()
    res=checkUserData(id)
    if res=='not-found':
        _error("Account Error","This Account Id wasn't Found !")
    elif res=='locked':
        _error("Account Error","This Account Was Locked !")
    else :
        idEntry.delete(0,END)
        mainPage.withdraw()
        createAccVerifyWindow(id)


def mainWindow():
    global mainPage
    global idEntry
    mainPage = Tk()
    mainPage.title("Bank System")
    WIDTH = 300
    HEIGHT = 200
    x = int((mainPage.winfo_screenwidth() / 2) - (WIDTH / 2))
    y = int((mainPage.winfo_screenheight() / 2) - (HEIGHT / 2))
    mainPage.geometry(f'{WIDTH}x{HEIGHT}+{x}+{y}')

    idLabel = Label(mainPage,font=20,text = "ID:",justify="center")
    idLabel.config(font=('callibri', 24))

    idEntry = Entry(mainPage,justify="center")
    idEntry.config(font=('callibri', 18))

    but1=Button(mainPage,text="Enter",command=lambda: checkUserId())

    but1.config(font=('callibri', 18))
    idLabel.pack(pady=10)
    idEntry.pack(pady=20)
    but1.pack(pady=10)

    mainPage.mainloop()