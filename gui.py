from tkinter import *

class App(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.grid()
        self.create()

    def create(self):
        Label(self,text='fools').grid(row=0,column=0,columnspan=2)
        Label(self,text='sergio').grid(row=1,column=0,sticky=W)

        self.person=Entry(self)
        self.person.grid(row=1,column=1,columnspan=2, sticky=W)

        Label(self,text='entry').grid(row=2,column=0,sticky=W)

        self.noun=Entry(self)
        self.noun.grid(row=2,column=1,columnspan=2, sticky=W)

        Label(self,text='booleanvar,Check').grid(row=3,column=0,sticky=W)

        self.isiyh=BooleanVar()
        Checkbutton(self,text='заебись',variable=self.isiyh).grid(row=3,column=1,sticky=W)
        self.isiyh1=BooleanVar()
        Checkbutton(self,text='пиздато',variable=self.isiyh1).grid(row=3,column=2,sticky=W)
        self.isiyh2=BooleanVar()
        Checkbutton(self,text='мандавошка',variable=self.isiyh2).grid(row=3,column=3,sticky=W)

        Label(self,text='stringvar,Radio').grid(row=4,column=0,sticky=W)

        self.boddy=StringVar()
        self.boddy.set(None)
        bodipar=['1','2','3','4']
        column=1
        for part in bodipar:
            Radiobutton(self,text=part,variable=self.boddy,value=part).grid(row=4,column=column,sticky=W)
            column+=1

        Button(self,text='Enter',command=self.itog).grid(row=5,column=0, sticky=W)

        self.text=Text(self,width=50,height=10,wrap=WORD)
        self.text.grid(row=6,column=0,columnspan=4)

    def itog(self):
        person=self.person.get()
        noun=self.noun.get()
        abbi=''
        if self.isiyh.get():
            abbi+="заебись "
        if self.isiyh1.get():
            abbi+='пиздато '
        if self.isiyh2.get():
            abbi+='мандавошка '
        body=self.boddy.get()
        itog=''
        itog=person+' '+noun+' '+abbi+body

        self.text.delete(0.0,END)
        self.text.insert(0.0,itog)

root=Tk()
root.title('fools')
root.geometry('500x500')
app=App(root)
root.mainloop()