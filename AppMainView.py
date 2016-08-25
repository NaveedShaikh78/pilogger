import thread
import time
from Tkinter import *
import ttk
import App
#import AutoPopUPView
import AutoComplete

autocmp = __import__('AutoComplete')
root = Tk()
root.grid_columnconfigure(0, weight=1)
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
class AppMainView:
  def __init__(self):
    self.macstatus = StringVar()
    self.operator = StringVar()
    self.operation = StringVar()
    self.jobno = StringVar()
    self.idlereson = StringVar()
    self.sclr = StringVar()
    frame = Frame(root)
    self.frame=frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.pack(expand=True,fill=X)
    self.sclr.set('Red')
    rowcolor0 = '#40E0D0'
    rowcolor1 = 'cyan'
    lb=Label(frame,  anchor=W, bg=rowcolor1 , padx = 5 , text="Machine Status ")            .grid(row=0,column=0,sticky=W+E+N+S)
    lb=Label(frame,  anchor=W, bg=rowcolor1 , padx = 0, width=01, text=":")                 .grid(row=0,column=1,sticky=W+E+N+S)
    lb=Label(frame,  anchor=W, bg=self.sclr.get(), padx = 5, width=12, textvariable = self.macstatus) .grid(row=0,column=2,sticky=W+E+N+S)
    lb=Label(frame,  anchor=W, bg=rowcolor0 , padx = 5, width=12, text="Operator Name")     .grid(row=1,column=0,sticky=W+E+N+S)
    lb=Label(frame,  anchor=W, bg=rowcolor0 , padx = 0, width=01, text=":")                 .grid(row=1,column=1,sticky=W+E+N+S)
    self.lboperator=Label(frame,  anchor=W, bg=rowcolor0 , padx = 5, width=12, textvariable=self.operator); 
    self.lboperator.grid(row=1,column=2,sticky=W+E+N+S);
    self.lboperator.bind("<Button-1>",self.labelClicked );
    lb=Label(frame,  anchor=W, bg=rowcolor1 , padx = 5, width=12, text="Job No")            .grid(row=2,column=0,sticky=W+E+N+S)
    lb=Label(frame,  anchor=W, bg=rowcolor1 , padx = 0, width=01, text=":")                 .grid(row=2,column=1,sticky=W+E+N+S)
    self.lbjobno=Label(frame,  anchor=W, bg=rowcolor1 , padx = 5, width=12, textvariable=self.jobno);  
    self.lbjobno.grid(row=2,column=2,sticky=W+E+N+S);
    self.lbjobno.bind("<Button-1>",self.labelClicked );
    lb=Label(frame,  anchor=W, bg=rowcolor0 , padx = 5, width=12, text="Operation")         .grid(row=3,column=0,sticky=W+E+N+S)
    lb=Label(frame,  anchor=W, bg=rowcolor0 , padx = 0, width=01, text=":")                 .grid(row=3,column=1,sticky=W+E+N+S)
    self.lboperation=Label(frame,  anchor=W, bg=rowcolor0 , padx = 5, width=12, textvariable=self.operation);
    self.lboperation.grid(row=3,column=2,sticky=W+E+N+S);
    self.lboperation.bind("<Button-1>",self.labelClicked );
    lb=Label(frame,  anchor=W, bg=rowcolor1 , padx = 5, width=12, text="Idele Reason")      .grid(row=4,column=0,sticky=W+E+N+S)
    lb=Label(frame,  anchor=W, bg=rowcolor1 , padx = 0, width=01, text=":")                 .grid(row=4,column=1,sticky=W+E+N+S)
    self.lbidlereson=Label(frame,  anchor=W, bg=rowcolor1 , padx = 5, width=12, textvariable=self.idlereson);
    self.lbidlereson.grid(row=4,column=2,sticky=W+E+N+S);
    self.lbidlereson.bind("<Button-1>",self.labelClicked );
    OperatorList = ('apple', 'banana', 'CranBerry', 'dogwood', 'alpha', 'Acorn','Accorn', 'Anise' )

  def labelClicked(self, event):
      self.strvar=StringVar()
      if self.lboperator==event.widget  :  strvar=self.operator
      if self.lbjobno==event.widget     :  strvar=self.jobno
      if self.lboperation==event.widget :  strvar=self.operation
      if self.lbidlereson==event.widget :  strvar=self.idlereson
      OperatorList = ('apple', 'banana', 'CranBerry', 'dogwood', 'alpha', 'Acorn','Accorn', 'Anise' )
      self.insderframe=Frame(self.frame)
      self.insderframe.columnconfigure(0, weight=1)
      #self.insderframe.pack(expand=True,fill=X)
      self.insderframe.grid(column=0,row=0,columnspan=10,rowspan=10,sticky=W+E+N+S)
      AutoComplete.AutocompleteEntry(OperatorList,self.insderframe,strvar).grid(column=0,row=0,sticky=W+E+N+S)
      Button(self.insderframe,text="Cancel",command =self.cancelInput).grid(column=1,row=0,sticky=W+E+N+S)
  def cancelInput(self):
      self.insderframe.destroy()
    #AutoPopUPView.AutoPopUPView().Show(self.frame,operator)