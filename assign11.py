import tkinter as tk
import webbrowser as wb
root=tk.Tk()
#changing the title of the window
root.title("window")
#username
l1=tk.Label(root,text="Username: ",
            font=("Times New Roman",25),
            width=30)
l1.grid()
e1=tk.Entry(root,font=("Times New Roman",25),bg="cyan",width=30)
e1.grid()

#password
l2=tk.Label(root,text="Password: ",
            font=("Times New Roman",25),
            width=30)
l2.grid()
e2=tk.Entry(root,font=("Times New Roman",25),bg="cyan",show="*",width=30)
e2.grid()
#phone
l3=tk.Label(root,text="Phone ",
            font=("Times New Roman",25),
            width=30)
l3.grid()
e3=tk.Entry(root,font=("Times New Roman",25),bg="cyan",show="*",width=30)
e3.grid()
#email
l4=tk.Label(root,text="Email ",
            font=("Times New Roman",25),
            width=30)
l4.grid()
e4=tk.Entry(root,font=("Times New Roman",25),bg="cyan",show="*",width=30)
e4.grid()
#displaymessage
l5=tk.Label(root,text=" ",
            font=("Times New Roman",15),
            height=2)
l5.grid()

#condition

def store():
    print()
    user=e1.get()
    passwd=e2.get()
    no=e3.get()
    id=e4.get()
    print(user)
    print(passwd)
    print(no)
    print(id)
    wb.open("https://www.titan.co.in/faq")
    
    # if user=="" and passwd=="":
    #     f=open("backend.txt","+w")
    #     f.writelines(["Username: ",user,"\nPassword: ",passwd])
    #     l5["text"]="data has been updated successfully!!\nCheck backend.txt"
    # else:
    #     l5["text"]="invalid username or password"
    if e1.get() =="": 
        l5["text"]="fill all the information"
    else:
        f=open("data.txt","+w")
        f.writelines(["username:",user,"\npassword:",passwd,
                      "\nphone:",no,"\nemail:",id])
        wb.open("https://www.youtube.com/")
    if e2.get() =="": 
        l5["text"]="fill all the information"
    else:
        f=open("data.txt")
        f.writelines(["username:",user,"\npassword:",passwd,
                      "\nphone:",no,"\nemail:",id])
    if e3.get() =="": 
        l5["text"]="fill all the information"
    else:
        f=open("data.txt")
        f.writelines(["username:",user,"\npassword:",passwd,
                      "\nphone:",no,"\nemail:",id])
    if e4.get() =="": 
        l5["text"]="fill all the information"
    else:
        f=open("data.txt")
        f.writelines(["username:",user,"\npassword:",passwd,
                      "\nphone:",no,"\nemail:",id])        
#button
b=tk.Button(root,text="Submit",
            font=("Times New Roman",25),
            bg="orange",
            activebackground="yellow",
            command=store
            ).grid()        
root.mainloop()        

        