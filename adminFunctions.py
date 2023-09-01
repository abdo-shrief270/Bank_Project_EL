from tkinter import *
from tkinter import messagebox

 
adminData=['','','']
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
                
def checkAdminData(id):
    with open('.\Admin_database.txt','r') as file:
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

def getAdminDataFromDB(id):
    with open('.\Admin_database.txt','r') as file:
        for line in file:
            if line.split('||')[0]==id :
                data=line[:-1]
                return list(data.split('||'))
    return []
  
def unlock_user(id):
    global userData
    res=checkUserData(id)
    if res=='not-found':
        _error("Account Error","This User Account Id wasn't Found !")
    else :
        userData=getDataFromDB(id)
        userData[-2]=3
        userData[-1]='t'
        update_database()
        _info("Sucess","{} Account Is Running Now".format(userData[1]))
        accWin.deiconify()
        accUnLock.destroy()
        
        
    
    
def lock_user(id):
    global userData
    res=checkUserData(id)
    if res=='not-found':
        _error("Account Error","This User Account Id wasn't Found !")
    else :
        userData=getDataFromDB(id)
        userData[-2]=0
        userData[-1]='f'
        update_database()
        _info("Sucess","{} Account Is Locked Now".format(userData[1]))
        accWin.deiconify()
        accLock.destroy()

    
def checkPassword(id,password):
    with open('.\Admin_database.txt','r') as file:
        for line in file:
            if line.split('||')[0]==id :
                if line.split('||')[-1][:-1]==password:
                    return True
    return False  
      
def on_closing():
    global accWin
    accWin.destroy()
    mainPage.destroy()

def lockAccWindow():
    global accLock
    accLock = Toplevel()
    accLock.title(adminData[0])
    WIDTH = 300
    HEIGHT = 200
    x = int((accLock.winfo_screenwidth() / 2) - (WIDTH / 2))
    y = int((accLock.winfo_screenheight() / 2) - (HEIGHT / 2))
    accLock.geometry(f'{WIDTH}x{HEIGHT}+{x}+{y}')
    
    userIdLabel = Label(accLock,font=20,text = "User Id:",justify="center")
    userIdLabel.config(font=('callibri', 24))

    UserIdEntry = Entry(accLock,justify="center")
    UserIdEntry.config(font=('callibri', 18))

    but2=Button(accLock,text="Lock",command=lambda: lock_user(UserIdEntry.get()))
    but2.config(font=('callibri', 18))
    userIdLabel.pack(pady=10)
    UserIdEntry.pack(pady=20)
    but2.pack(pady=10)

    accLock.mainloop()
    
def unLockAccWindow():
    global accUnLock
    accUnLock = Toplevel()
    accUnLock.title(adminData[0])
    WIDTH = 300
    HEIGHT = 200
    x = int((accUnLock.winfo_screenwidth() / 2) - (WIDTH / 2))
    y = int((accUnLock.winfo_screenheight() / 2) - (HEIGHT / 2))
    accUnLock.geometry(f'{WIDTH}x{HEIGHT}+{x}+{y}')
    
    userIdLabel = Label(accUnLock,font=20,text = "User Id:",justify="center")
    userIdLabel.config(font=('callibri', 24))

    UserIdEntry = Entry(accUnLock,justify="center")
    UserIdEntry.config(font=('callibri', 18))

    but2=Button(accUnLock,text="UnLock",command=lambda: unlock_user(UserIdEntry.get()))
    but2.config(font=('callibri', 18))
    userIdLabel.pack(pady=10)
    UserIdEntry.pack(pady=20)
    but2.pack(pady=10)

    accUnLock.mainloop()
 
def createAccountWindow():
    global adminData
    global accWin
    
    accWin = Toplevel()
    accWin.title(adminData[1])
    WIDTH = 500
    HEIGHT = 150
    x = int((accWin.winfo_screenwidth() / 2) - (WIDTH / 2))
    y = int((accWin.winfo_screenheight() / 2) - (HEIGHT / 2))
    accWin.geometry(f'{WIDTH}x{HEIGHT}+{x}+{y}')

    l1 = Label(accWin, text = "Admin ID:", width=14,justify="center",font=('callibri', 16))
    l1.grid(row = 0, column = 0, pady = 3,padx=3)
    l2 = Label(accWin, text = adminData[0], width=20,justify="center",font=('callibri', 18), fg='#fA7A8C')
    l2.grid(row = 0, column = 1, pady = 3,padx=3)  
    
    l3 = Label(accWin, text = "Admin Name:", width=14,justify="center",font=('callibri', 16))
    l3.grid(row = 1, column = 0, pady = 3,padx=3)
    l4 = Label(accWin, text = adminData[1], width=30,justify="center",font=('callibri', 14), fg='blue')
    l4.grid(row = 1, column = 1, pady = 3,padx=3)  
    
    butOut = Button(accWin,text="Lock Account", width=15,justify="center",font=('callibri', 16),command=lockAccWindow)
    butOut.grid(row = 3, column = 0, pady = 3,padx=3)
    butPass = Button(accWin,text="UnLock Account", width=15,justify="center",font=('callibri', 16),command=unLockAccWindow)
    butPass.grid(row = 3, column = 1, pady = 3,padx=3) 

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
    passEntry.config(font=('callibri', 18))

    but2=Button(accVerify,text="Enter",command=lambda: verifyAdmin(id,passEntry.get()))
    but2.config(font=('callibri', 18))
    passLabel.pack(pady=10)
    passEntry.pack(pady=20)
    but2.pack(pady=10)
    
    accVerify.mainloop()

def verifyAdmin(id,password):
    global accVerify
    global adminData
    adminData=getAdminDataFromDB(id)
    res=checkPassword(id,password)
    if res==False:
        _error("Wrog Password","Password Entered Is Wrong")
    else :
        accVerify.destroy()
        createAccountWindow()
              
def checkAdminId():
    global adminData
    global idEntry
    id=idEntry.get()
    res=checkAdminData(id)
    if res=='not-found':
        _error("Account Error","This Admin Account Id wasn't Found !")
    else :
        idEntry.delete(0,END)
        mainPage.withdraw()
        createAccVerifyWindow(id)


def mainWindow():
    global mainPage
    global idEntry
    mainPage = Tk()
    mainPage.title("Bank System [Admin]")
    WIDTH = 300
    HEIGHT = 200
    x = int((mainPage.winfo_screenwidth() / 2) - (WIDTH / 2))
    y = int((mainPage.winfo_screenheight() / 2) - (HEIGHT / 2))
    mainPage.geometry(f'{WIDTH}x{HEIGHT}+{x}+{y}')

    idLabel = Label(mainPage,font=20,text = "Admin ID:",justify="center")
    idLabel.config(font=('callibri', 24))

    idEntry = Entry(mainPage,justify="center")
    idEntry.config(font=('callibri', 18))

    but1=Button(mainPage,text="Enter",command=lambda: checkAdminId())

    but1.config(font=('callibri', 18))
    idLabel.pack(pady=10)
    idEntry.pack(pady=20)
    but1.pack(pady=10)

    mainPage.mainloop()