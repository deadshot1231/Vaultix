from customtkinter import *
import json
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import PhotoImage

set_appearance_mode("Light")  


def message():
       
  if webentry.get()=='' or userentry.get()=='' or passwordentry.get()==0:
       messagebox.showerror(title='invaild input',message='please Enter valid input')
       
current_id=0
def savepassword():
    
    message()
    
    if webentry.get()!='' and userentry.get()!='' and passwordentry.get()!='':
    

           try:
               with open("password.json", "r", encoding="utf-8") as f:
                   data = json.load(f)
           except (FileNotFoundError, json.JSONDecodeError):
               data = []

           new_id = len(data) + 1

    

     

           dic = {
               "id": new_id,
               "website": webentry.get(),
               "username": userentry.get(),
               "password": passwordentry.get()
           }

           data.append(dic)

           with open("password.json", "w", encoding="utf-8") as f:
               json.dump(data, f, indent=4)

def copy(text):
    app.clipboard_clear()
    app.clipboard_append(text)
    app.update()

def view_password(v,p):
    current_text = v.cget("text")
    if current_text=='************':
       v.configure(text=p)
    else:
       v.configure(text='************')

    
    

def showdetail():
          global current_id,new_id

     # if webentry.get()!='' or userentry.get()!='' or passwordentry.get()!='':

     

          try:
             with open("password.json", "r", encoding="utf-8") as file:
               data=  json.load(file)
          except:
                data=[]

          new_id = len(data) 

     # new_id = savepassword()
     

          for i,item in enumerate(data):
                    
                         current_id=item["id"]


                         row = CTkFrame(frame3,fg_color='transparent',corner_radius=20)
                         row.pack(fill='x',pady=4)

                         lock2_icon = CTkImage(
                            light_image=Image.open("lock2.png"),
                            dark_image=Image.open("lock2.png"),
                            size=(25, 25))
                         

                         web_frame = CTkFrame(row, width=200,height=50, fg_color="transparent",)
                         web_frame.pack(side="left")
                         web_frame.pack_propagate(False)

                         user_frame = CTkFrame(row, width=400,height=50, fg_color="transparent")
                         user_frame.pack(side="left")
                         user_frame.pack_propagate(False)

                         pw_frame = CTkFrame(row, width=300,height=50, fg_color="transparent")
                         pw_frame.pack(side="left",padx=80)
                         pw_frame.pack_propagate(False)

                         web=  CTkLabel(web_frame, text= f'   {data[i]["website"]}', anchor="w",image=lock2_icon,
                                        compound='left',font=("inter", 16),
                                        text_color='black').pack(fill="x")
                         user=CTkLabel(user_frame, text=data[i]["username"],font=("inter", 16), anchor="w",text_color='black').pack(fill="x")
                         passw=CTkLabel(pw_frame, text='************',font=("inter", 16), anchor="w",text_color='black')
                         passw.pack(fill="x")

                         button_frame = CTkFrame(row, fg_color="transparent")
                         button_frame.pack(side="left", padx=10)

                         view_icon = CTkImage(
                            light_image=Image.open("eye.png"),
                            dark_image=Image.open("eye.png"),
                            size=(25, 25))
          
                         copy_icon = CTkImage(
                            light_image=Image.open("copy.png"),
                            dark_image=Image.open("copy.png"),
                            size=(25, 25))
          
                         delete_icon = CTkImage(
                            light_image=Image.open("delete.png"),
                            dark_image=Image.open("delete.png"),
                            size=(25, 25))
    
                         view_btn = CTkButton(button_frame,
                         text="",width=45,fg_color="#E0F2FE", text_color="#6B787A"
                         ,image=view_icon,hover_color='#BAE6FD',
                         border_color='#6B787A',border_width=1,
                         command=lambda v=passw, p=data[i]["password"]: view_password(v, p))
                         view_btn.pack(side="left",padx=10)
                         delete_btn = CTkButton(button_frame,
                          text="",width=45,image=delete_icon,fg_color='#f9ab8f',hover_color='#DC2626',
                          command=lambda r=row,ID= current_id: delete_row(r,ID))
                         delete_btn.pack(side="left",padx=10)
                         copy_btn = CTkButton(button_frame,
                          text="",width=45,image=copy_icon,fg_color='#d3f3f1',hover_color='#0D9488',
                          command=lambda h=item["password"] : copy(h))
                         copy_btn.pack(side="left",padx=10)

def clear_all():
    answer = messagebox.askyesno(
        "Clear All",
        "Are you sure you want to delete all saved passwords?"
    )

    if not answer:
        return

    # Clear JSON
    with open("password.json", "w", encoding="utf-8") as file:
        json.dump([], file, indent=4)

    # Remove all rows from the scrollable frame
    for widget in frame3.winfo_children():
        widget.destroy()


                         

    
      


def delete_row(n, ID):
    with open("password.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        if item["id"] == ID:
            data.remove(item)
            break

    for i, item in enumerate(data):
        item["id"] = i + 1

    with open("password.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


    for widget in frame3.winfo_children():
        widget.destroy()

    showdetail()

    n.destroy()





def addpasswords():
    global current_id
    savepassword()
    if webentry.get()!='' and userentry.get()!='' and passwordentry.get()!='':
          try:
           with open("password.json", "r", encoding="utf-8") as file:
               data=  json.load(file)
               new_id = len(data) 
          except:
               data=[]
               new_id=1
           

          new_id = len(data)

          row = CTkFrame(frame3,fg_color='transparent')
          row.pack(fill="x",pady=0)

          lock2_icon = CTkImage(
                            light_image=Image.open("lock2.png"),
                            dark_image=Image.open("lock2.png"),
                            size=(25, 25))


          web_frame = CTkFrame(row, width=200,height=50, fg_color="transparent")
          web_frame.pack(side="left")
          web_frame.pack_propagate(False)

          user_frame = CTkFrame(row, width=400,height=50, fg_color="transparent")
          user_frame.pack(side="left")
          user_frame.pack_propagate(False)

          pw_frame = CTkFrame(row, width=300,height=50, fg_color="transparent")
          pw_frame.pack(side="left",padx=80)
          pw_frame.pack_propagate(False)

          web=CTkLabel(web_frame, text=f'   {webentry.get()}', anchor="w",text_color='black',image=lock2_icon,
                       compound='left',font=("inter", 16),).pack(fill="x")
          user=CTkLabel(user_frame, text=userentry.get(), anchor="w",
                        font=("inter", 16),text_color='black').pack(fill="x")
          passw=CTkLabel(pw_frame, text='************', anchor="w",text_color='black',font=("inter", 16),)
          passw.pack(fill="x")
    
          button_frame = CTkFrame(row, fg_color="transparent")
          button_frame.pack(side="left", padx=10)
          

          view_icon = CTkImage(
             light_image=Image.open("eye.png"),
            dark_image=Image.open("eye.png"),
            size=(25, 25))
          
          copy_icon = CTkImage(
             light_image=Image.open("copy.png"),
            dark_image=Image.open("copy.png"),
            size=(25, 25))
          
          delete_icon = CTkImage(
             light_image=Image.open("delete.png"),
            dark_image=Image.open("delete.png"),
            size=(25, 25))
    
          view_btn = CTkButton(button_frame,
                         text="",width=45,image=view_icon,fg_color="#E0F2FE", 
                         text_color="#6B787A",hover_color='#BAE6FD',
                         command=lambda v=passw, p=passwordentry.get(): view_password(v, p))
          view_btn.pack(side="left",padx=10)
          delete_btn = CTkButton(button_frame,
                          text="",width=45,image=delete_icon,fg_color='#f9ab8f',hover_color='#DC2626',
                          command=lambda r=row,ID= current_id: delete_row(r,ID))
          delete_btn.pack(side="left",padx=10)
          copy_btn = CTkButton(button_frame,
                          text="",width=45,image=copy_icon,fg_color='#d3f3f1',hover_color='#0D9488',
                          command=lambda h=passwordentry.get() : copy(h))
          copy_btn.pack(side="left",padx=10)
          webentry.delete(0,END)
          userentry.delete(0,END)
          passwordentry.delete(0,END)
        
def aboutus():
    messagebox.showinfo(
        "About Vaultix",
        """Vaultix is a simple, secure, and modern desktop application
designed to help you organize your passwords in one place.

With an intuitive interface, master key protection, and quick copy
features, Vaultix makes managing your accounts easy while keeping
your information accessible only to you.

Built with a focus on simplicity, speed, and privacy, Vaultix helps
you spend less time searching for passwords and more time getting
things done."""
    )


def setting():
     global locke,theme
     win = CTkToplevel(app)
     win.title("setting")
     win.geometry("400x350")
     win.resizable(False,False)
     win.configure(fg_color="white")
     win.lift()      
     win.focus_force()  
     win.grab_set() 
     locke = StringVar(master=win, value="off")
     bg_icon = CTkImage(
      light_image=Image.open("setbg.png"),
      dark_image=Image.open("setbg.png"),
       size=(400, 350))
     bglabel = CTkLabel(win, text="", image=bg_icon)
     bglabel.image = bg_icon
     bglabel.place(x=0, y=0, relwidth=1, relheight=1)
     win.iconbitmap("icons8-vault-64.ico")

    
    
     if securty:
       locke.set("on")
     else:
       locke.set("off")

     switch = CTkSwitch(win, text="MASTER KEY",text_color='black',font=('',15,'bold')
                        ,button_hover_color='grey',variable=locke, fg_color="grey"
                         ,progress_color="sky blue",button_color="#AAADEF"
                        ,onvalue='on',offvalue='off')
     switch.place(x=50,y=130)
     save2button=CTkButton(win,text='SAVE',fg_color='#6d51a5',command=savesetting,height=35
                           ,hover_color='#6d51a5')
     save2button.place(x=50,y=170)
     resetbutton=CTkButton(win,text='RESET KEY',fg_color='#9491e2',height=35,hover_color='#9491e2'
                           ,command=restkey)
     resetbutton.place(x=50,y=210)
     aboutusbtn=CTkButton(win,text='ABOUT US',fg_color='#6d90b9',hover_color='#6d90b9',height=35,
                        command= aboutus)
     aboutusbtn.place(x=50,y=250)





def restkey():
     global newlockkey
     
     win = CTkToplevel(app)
     win.title("RESET KEY")
     win.geometry("800x550")
     win.resizable(False,False)
     win.configure(fg_color="white")
     win.lift()      
     win.focus_force()  
     win.grab_set()
     win.iconbitmap("icons8-vault-64.ico")
     lockscreen_icon2 = CTkImage(
      light_image=Image.open("lockscreen.png"),
      dark_image=Image.open("lockscreen.png"),
       size=(800, 550))
     lockscreenlabel = CTkLabel(win, text="", image=lockscreen_icon2)
     lockscreenlabel.image = lockscreen_icon2
     lockscreenlabel.place(x=0, y=0, relwidth=1, relheight=1)

     
     newlockkey=CTkEntry(win,height=40,width=300,placeholder_text="Enter new key....",placeholder_text_color='grey')
     newlockkey.place(x=250,y=270)
     reset=CTkButton(win,text='RESET',command=savelock,fg_color='#6d51a5',height=37)
     reset.place(x=330,y=340)
     win.bind("<Return>", lambda e: savelock())

     



def savelock():

     with open('lockkey.txt','w') as f:
          f.write(newlockkey.get())



def savesetting():

     if locke.get()=='on':
         x=True
     else:
          x=False
   


     set={
          "lock_status":x
     }
     
     
          
     with open("saved.json", "w", encoding="utf-8") as f:
               json.dump(set, f, indent=4)


def remember():
               
               global securty

     
               with open("saved.json", "r", encoding="utf-8") as f:
                   history = json.load(f)
               
               securty=history["lock_status"]

g=0

def openapp():
      global g
      with open('lockkey.txt') as f:
          key=f.read()
     
      if lockkey.get()==key:
           g=1
           win1.destroy()
      else:
           messagebox.showwarning('WRONG KEY',message="PLEASE ENTER CORRECT KEY")
  
def lock():
     global lockkey,g,win1
     win1 = CTkToplevel(app)
     win1.withdraw()

     win1.iconbitmap("icons8-vault-64.ico")

     win1.deiconify()
     win1.title("LOCK")
     win1.geometry("800x550")
     win1.resizable(False,False)
     win1.configure(fg_color="white")
     lockscreen_icon = CTkImage(
      light_image=Image.open("lockscreen.png"),
      dark_image=Image.open("lockscreen.png"),
       size=(800, 550))
     lockscreenlabel = CTkLabel(win1, text="", image=lockscreen_icon)
     lockscreenlabel.image = lockscreen_icon
     lockscreenlabel.place(x=0, y=0, relwidth=1, relheight=1)

     
     lockkey=CTkEntry(win1,height=40,width=300,placeholder_text="Enter key....",placeholder_text_color='grey')
     lockkey.place(x=250,y=270)
     submit=CTkButton(win1,text='SUBMIT',command=openapp,fg_color='#6d51a5',height=37)
     submit.place(x=330,y=340)
     win1.bind("<Return>", lambda e: openapp())

     win1.protocol("WM_DELETE_WINDOW", lambda: None)

     win1.lift()      
     win1.focus_force()  
     win1.grab_set() 

def serch12():
     global newlockkey
     win = CTkToplevel(app)
     win.title("SEARCH")
     win.geometry("600x400")
     win.resizable(False,False)
     win.configure(fg_color="#fefeff")
     win.iconbitmap("icons8-vault-64.ico")

     try:
           with open("password.json", "r", encoding="utf-8") as file:
               data=  json.load(file)
               new_id = len(data) 
     except:
               data=[]

     for item in data:

          if item["website"].lower()==serch.get().lower():


           labelweb=CTkLabel(win,text=f'WEBSITE : {item["website"]}'
                          ,text_color='black',font=('',20,'bold')).place(x=80,y=90)
           labeluser=CTkLabel(win,text=f'USERNAME : {item["username"]}'
                          ,text_color='black',font=('',20,'bold')).place(x=80,y=130)
           labelpass=CTkLabel(win,text=f'PASSWORD : {item["password"]}'
                          ,text_color='black',font=('',20,'bold')).place(x=80,y=170)
     
           copyy=CTkButton(win,text='copy',fg_color='#5B6CFF',hover_color="#9CA6F8",
                          command=lambda h=item["password"] : copy(h) 
                          ).place(x=130,y=220)

     win.lift()      
     win.focus_force()  
     win.grab_set()

    





app=CTk()


remember()



if securty==True:
      lock()



app.configure(fg_color='#F5F7FB')
app.iconbitmap("icons8-vault-64.ico")

app.title('VAULTIC')

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
w = int(screen_width * 0.93)
h = int(screen_height * 0.92)

x = (screen_width - w) // 2
y = (screen_height - h-10) // 2


background=CTkImage(
             light_image=Image.open("bg.png"),
            dark_image=Image.open("bg.png"),
            size=(int(screen_width * 0.93), int(screen_height * 0.92)))

backlabel=CTkLabel(app,text='',image=background,
                  font=('Jakarta Sans',18,'bold'),compound='left')
backlabel.place(x=0,y=0)

app.geometry(f"{w}x{h}+{x}+{y}")

head_icon = CTkImage(
    light_image=Image.open("pass.png"),
    dark_image=Image.open("pass.png"),
    size=(25, 25))

headname=CTkLabel(app,text='VAULTIX',text_color='black',image=head_icon,
                  font=('Jakarta Sans',18,'bold'),compound='left')
headname.place(x=60,y=0)


frame1=CTkFrame(app,fg_color="white",width=int(screen_width*0.893),height=int(screen_height*0.153)
                ,corner_radius=30,border_color='#DCE6F2',border_width=1)
frame1.place(x=30,y=60)

add_icon = CTkImage(
    light_image=Image.open("add.png"),
    dark_image=Image.open("add.png"),
    size=(18, 18))

headlabel=CTkLabel(frame1,text='  ADD PASSWORD',text_color='black',
                   image=add_icon,compound='left',font=('',15,),fg_color='transparent')
headlabel.place(x=30,y=-4)


weblable=CTkLabel(frame1,text='Website/App',text_color='black',font=('',15,'bold'),fg_color='transparent')
weblable.place(x=30,y=30)

webentry=CTkEntry(frame1,placeholder_text='🌐 e.g.www.com',width=270,placeholder_text_color='gray'
                  ,height=35,fg_color="#EDF5FF",border_color='#8399a2'
                  ,text_color='black',corner_radius=12)
webentry.place(x=30,y=70)


userlabel=CTkLabel(frame1,text='Username/Email',text_color='black',font=('',15,'bold'),fg_color='transparent')
userlabel.place(x=400,y=30)


userentry=CTkEntry(frame1,placeholder_text='👩🏻‍💼 e.g.abd@gmail.com',width=270,placeholder_text_color='gray'
                  ,height=35,text_color='black',fg_color='#EDF5FF',border_color='#8399a2',corner_radius=12)
userentry.place(x=400,y=70)


passwordlabel=CTkLabel(frame1,text='Password',text_color='black',font=('',15,'bold'),fg_color='transparent')
passwordlabel.place(x=770,y=30)


passwordentry=CTkEntry(frame1,placeholder_text='🔒 Enter Password',width=270,height=35,
                       placeholder_text_color='gray',text_color='black'
                  ,fg_color='#EDF5FF',border_color='#8399a2',corner_radius=12)
passwordentry.place(x=770,y=70)

savebutton=CTkButton(frame1,text='💾 Save',fg_color='#5B6CFF',height=45,text_color='white',
                     corner_radius=12,hover_color="#929CF8",
                     command=addpasswords)
savebutton.place(x=1120,y=70)

frame2=CTkFrame(app,fg_color="white",width=int(screen_width*0.89),height=100
                ,corner_radius=30,border_color='#DCE6F2',border_width=1)
frame2.place(x=30,y=200)

savedlable=CTkLabel(frame2,text='Saved Password',text_color='#ab2aed',font=('',15,'bold'),fg_color='transparent')
savedlable.place(x=30,y=10)

serch=CTkEntry(frame2,placeholder_text='🔍 Search....',width=400,placeholder_text_color='gray'
               ,text_color='black',corner_radius=12
                  ,height=35,fg_color='#EDF5FF',border_color='#8399a2')
serch.place(x=30,y=45)

clear_icon = CTkImage(
    light_image=Image.open("clear.png"),
    dark_image=Image.open("clear.png"),
    size=(25, 25))

clearbutton=CTkButton(frame2,text='Clear all',fg_color='#FEE2E2',height=45,corner_radius=12,
                     text_color='#EF4444',border_color='#EF4444',image=clear_icon
                     ,border_width=1,hover_color="#F69B9B",command=clear_all)
clearbutton.place(x=1120,y=45)

search_icon = CTkImage(
    light_image=Image.open("search.png"),
    dark_image=Image.open("search.png"),
    size=(25, 25))

serchbutton=CTkButton(frame2,text='SEARCH',fg_color='#5B6CFF',height=45,
                     text_color='white',border_color='white',border_width=2,corner_radius=12,
                     image=search_icon,hover_color="#919CFB",
                     command=serch12)
serchbutton.place(x=950,y=45)

frame2_5=CTkFrame(app,fg_color="#ECF9FB",width=int(screen_width*0.89),height=38
                ,corner_radius=20,border_color='#DCE6F2',border_width=1)
frame2_5.place(x=30,y=308)

weblable2=CTkLabel(frame2_5,text='Website/App',text_color='black',font=('',15,'bold'),fg_color='transparent')
weblable2.place(x=40,y=4)

userlabel2=CTkLabel(frame2_5,text='Username/Email',text_color='black',font=('',15,'bold'),fg_color='transparent')
userlabel2.place(x=315,y=4)

passwordlabel=CTkLabel(frame2_5,text='Password',text_color='black',font=('',15,'bold'),fg_color='transparent')
passwordlabel.place(x=750,y=4)

frame3=CTkScrollableFrame(app,fg_color="white",width=int(screen_width*0.87),height=330
                ,corner_radius=30,border_color='#DCE6F2',border_width=2)
frame3.place(x=30,y=350)

showdetail()

no_password=CTkLabel(app,text=f'::Total Password : {new_id}',text_color='#727a9a'
                     ,font=('',15,'bold'),fg_color='transparent')
no_password.place(x=1250,y=5)

setting_icon = CTkImage(
    light_image=Image.open("setting.png"),
    dark_image=Image.open("setting.png"),
    size=(25, 25))

lock_icon = CTkImage(
    light_image=Image.open("lock.png"),
    dark_image=Image.open("lock.png"),
    size=(25, 25))

settingbutton=CTkButton(app,hover_color='#ebf4f5',text='',height=40,width=10,image=setting_icon,
                        fg_color='#bbc7dc',
                    
                     command=setting)
settingbutton.place(x=1150,y=5)

lockbutton=CTkButton(app,hover_color='#ebf4f5',text='',height=40,width=10,image=lock_icon,
                        fg_color='#b5c6e0',
                    
                     command=lock)
lockbutton.place(x=1200,y=5)



app.mainloop()