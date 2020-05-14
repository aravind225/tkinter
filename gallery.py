from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Gallery")
#for top icon
root.iconbitmap(r"D:\New folder\facebook_logos_PNG19764.png")
##= for images in list
image1 = Image.open(r"D:\photos\Cat.png")
my_img1=ImageTk.PhotoImage(image1.resize((450, 350), Image.ANTIALIAS))
image2 = Image.open(r"D:\photos\ContentAwareRemoval.png")
my_img2=ImageTk.PhotoImage(image2.resize((450, 350), Image.ANTIALIAS))
image3 = Image.open(r"D:\photos\Lake.png")
my_img3=ImageTk.PhotoImage(image3.resize((450, 350), Image.ANTIALIAS))
image4 = Image.open(r"D:\photos\Psychedelic.jpg")
my_img4=ImageTk.PhotoImage(image4.resize((450, 350), Image.ANTIALIAS))

img_list=[my_img1,my_img2,my_img3,my_img4]

my_label=Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)
def forword(img_num):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label=Label(image=img_list[img_num-1])
    button_forword=Button(root,text=">>",command=lambda:forword(img_num+1))
    button_back=Button(root,text="<<",command=lambda:back(img_num-1))
    
    if img_num==len(img_list):
        button_forword=Button(root,text=">>",state=DISABLED)
    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forword.grid(row=1,column=2)
def back(img_num):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label=Label(image=img_list[img_num-1])
    button_forword=Button(root,text=">>",command=lambda:forword(img_num+1))
    button_back=Button(root,text="<<",command=lambda:back(img_num-1))
    if img_num==1:
        button_back=Button(root,text="<<",command=back,state=DISABLED)
        

    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forword.grid(row=1,column=2)


button_back=Button(root,text="<<",command=back,state=DISABLED)
button_exit=Button(root,text="EXIT",command=root.quit())
button_forword=Button(root,text=">>",command=lambda:forword(2))

 
button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forword.grid(row=1,column=2)




root.mainloop()


