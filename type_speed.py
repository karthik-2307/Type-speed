import time
from tkinter import *
from tkinter import messagebox
global count
count=0
window=Tk()
named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%M", named_tuple)
var1=int(time_string)+1
def fn(event):
    # txt="It is entirely a matter of usage and there is no definite answer it depends on which style guide you follow and not all style guides will accept spaces between paragraphs at all  except where there is a new section"
    # print(txt.index(" "))
    txt="hello"
    # print("you did something "+event.keysym)
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime(" %H:%M:%S", named_tuple)
    # print(time_string)
    time_string = time.strftime("%M", named_tuple)
    # print(int(time_string)+2)
    # print(var1)
    var=len(list)
    # print(txt[0])
    if int(time_string)==var1:
        return
    elif txt[var]==event.keysym :
       list.append(1)
    elif event.keysym=="space" and var in list1:
        list.append(1)
    # list.append(1)
    # print(len(list))
    # print(len(txt))
    print(len(list))
    if len(list)==len(txt):
         messagebox.askokcancel(title="Check",message="You are Passed in typing")
    elif var1<=int(time_string):
         messagebox.askokcancel(title="Check",message="Your failed in this test")
window.title("TYPE CHECKER")
count=0
list=[]
list1=[]
print(len(list))
# text=Label(window,text="It is entirely a matter of usage and there is no definite answer it depends on which style guide you follow and not all style guides will accept spaces between paragraphs at all  except where there is a new section").pack()
text=Label(window,text="hello").pack()
check="It is entirely a matter of usage and there is no definite answer it depends on which style guide you follow and not all style guides will accept spaces between paragraphs at all  except where there is a new section."
for i in range(0,len(check)):
    if check[i]==" ":
        list1.append(i)
# print(list1)

inp=Text(window).pack()
window.bind("<Key>",fn)
window.mainloop()