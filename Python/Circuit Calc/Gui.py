from tkinter import *
from tkinter import filedialog
import time
from threading import Thread
import circuit
import math
import os
import photos
direct=os.getcwd()
list_bytes=photos.list
list_names=photos.list_names

if not os.path.exists(direct+"\\CircuitFiles"):
    os.mkdir(direct+"\\CircuitFiles")
    counter=0
    for image in list_names:
        with open(direct+"\\CircuitFiles\\"+image,"wb") as f1:
            f1.write(list_bytes[counter])
        counter+=1
    
    

class CircuitAnalysis(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.ws = self.winfo_screenwidth()
        self.hs = self.winfo_screenheight()
        pos_x=round((self.ws-590)/2)
        pos_y=round((self.hs-232)/2)
        self.geometry("590x232+"+str(pos_x)+"+"+str(pos_y))
        self.overrideredirect(1) #Remove border
        self.attributes("-topmost", True)
        self.canvas1=Canvas(self,bg="#353434",highlightthickness=0)
        self.canvas1.place(x=0,y=0,width=590,height=232)
        # direct+"\\CircuitFiles\\image_intro.png"
        self.image_intro=PhotoImage(file=direct+"\\CircuitFiles\\image_intro.png")
        self.image_error=PhotoImage(file=direct+"\\CircuitFiles\\Error.png")
        self.canvas1.create_image(0,0,anchor=NW,image=self.image_intro)
        a=Thread(target=self.loading)
        self.bt_list_setting_active=0
        self.bt_value_active=1
        self.bt_method_active=0
        self.win=1
        self.bt_current_active=0
        self.position=0
        self.bt_Resistance_active=1
        self.bt_Capacitor_active=0
        self.bt_Inductor_active=0
        self.bt_VS_active=0
        self.bt_CS_active=0
        self.bt_Others_active=0
        self.solutions_list=[]
        a.start()
        #self.mainloop()
    def loading(self):
        for i in range(0,589):
            self.canvas1.create_rectangle(0,231,i,231,outline="#1398f5",width=5)
        ## calling the function of the second win
        self.win2()
    def win2(self):
            self.withdraw()
            self.win2=Toplevel()
            self.win2.overrideredirect(1)
            self.win2.bind("<Return>", self.bt_add_com)
            self.win2.bind("<Delete>",self.delete_com)
            self.win2.attributes("-topmost", True)
            pos_x=round((self.ws-1024)/2)
            pos_y=round((self.hs-720)/2)
            self.win2.geometry("1024x720+"+str(pos_x)+"+"+str(pos_y))
            self.canvas2=Canvas(self.win2,bg="white",highlightthickness=0)
            self.canvas2.place(x=0,y=0,width=1024,height=720)
            self.backimage=PhotoImage(file=direct+"\\CircuitFiles\\win2.png")
            self.canvas2.create_image(0,0,anchor=NW,image=self.backimage)
            
            
            self.lbl_vars=Label(self.win2,text="Vars",bg="#212020",highlightthickness=0,bd=0,font=("arial",16),fg="white")
            self.lbl_voltages=Label(self.win2,text="Voltage",bg="#212020",highlightthickness=0,bd=0,font=("arial",16),fg="white")
            self.lbl_powers=Label(self.win2,text="Power",bg="#212020",highlightthickness=0,bd=0,font=("arial",16),fg="white")
            
            self.image_close_before=PhotoImage(file=direct+"\\CircuitFiles\\close_before.png")
            self.image_close_after=PhotoImage(file=direct+"\\CircuitFiles\\close_after.png")
            self.bt_close=Button(self.win2,command=self.close_app,image=self.image_close_before,bg="#212020",
                           activebackground="#212020",relief="flat",highlightthickness=0,bd=0)
            self.bt_close.bind("<Enter>",self.bt_close_enter)
            self.bt_close.bind("<Leave>",self.bt_close_leave)
            self.bt_close.place(x=980,y=15)
            self.listbox1=Listbox(self.win2,bg="#212020",highlightcolor="#1398f5",
                                  highlightbackground="#cb1651",fg="#2290e5",font=("arial",16))
            self.listbox1.place(x=33,y=180,width=284,height=349)
            self.listbox1.bind("<<ListboxSelect>>",self.ClickEventListbox)
            self.listbox2=Listbox(self.win2,bg="#212020",highlightcolor="#1398f5",
                                  highlightbackground="#cb1651",fg="#2290e5",font=("arial",16))
            self.listbox2.place(x=370,y=180,width=284,height=349)
            self.listbox3=Listbox(self.win2,bg="#212020",highlightcolor="#1398f5",
                                  highlightbackground="#cb1651",fg="#2290e5",font=("arial",16))
            self.listbox3.place(x=707,y=180,width=284,height=349)
    
            self.ent=Entry(self.win2,bg="#212020",fg="#1398f5",font=("arial",14,"bold"),highlightthickness=1)
            self.ent.config(highlightcolor="#1398f5",highlightbackground="#cb1651")
            self.ent.place(x=171,y=589,width=432,height=33)
            self.image_add_before=PhotoImage(file=direct+"\\CircuitFiles\\add_before.png")
            self.image_add_after=PhotoImage(file=direct+"\\CircuitFiles\\add_after.png")
            self.bt_add=Button(self.win2,command=self.bt_add_com2,image=self.image_add_before,bg="#212020",
                           activebackground="#212020",relief="flat",highlightthickness=0,bd=0)
            self.bt_add.bind("<Enter>",self.bt_add_enter)
            self.bt_add.bind("<Leave>",self.bt_add_leave)
            
            self.bt_add.place(x=622,y=589)
            self.image_setting_before=PhotoImage(file=direct+"\\CircuitFiles\\setting_before.png")
            self.image_setting_after=PhotoImage(file=direct+"\\CircuitFiles\\setting_after.png")
            self.bt_setting=Button(self.win2,command=self.bt_setting_com,image=self.image_setting_before,bg="#9b9e9e",
                           activebackground="#9b9e9e",relief="flat",highlightthickness=0,bd=0)
            self.bt_setting.bind("<Enter>",self.bt_setting_enter)
            self.bt_setting.bind("<Leave>",self.bt_setting_leave)
            self.bt_setting.place(x=37,y=69)
            self.image_list_setting=PhotoImage(file=direct+"\\CircuitFiles\\list_setting.png")
            self.lbl_setting=Label(self.win2,image=self.image_list_setting,bd=0,highlightthickness=0)
            self.bt_open=Button(self.lbl_setting,bg="#e1e1e1",activebackground="#e1e1e1",relief="flat",
                                highlightthickness=0,bd=0,command=self.bt_open_com,text="Open Saved Circuit",
                                font=("arial",14))
            self.bt_open.bind("<Enter>",self.bt_open_enter)
            self.bt_open.bind("<Leave>",self.bt_open_leave)
            self.bt_open.place(x=5,y=38,width=219,height=28)
            self.bt_save=Button(self.lbl_setting,bg="#e1e1e1",activebackground="#e1e1e1",relief="flat",
                                highlightthickness=0,bd=0,command=self.bt_save_com,text="Save Circuit",
                                font=("arial",14))
            self.bt_save.bind("<Enter>",self.bt_save_enter)
            self.bt_save.bind("<Leave>",self.bt_save_leave)
            self.bt_save.place(x=5,y=72,width=219,height=28)
            self.bt_New=Button(self.lbl_setting,bg="#e1e1e1",activebackground="#e1e1e1",relief="flat",
                                highlightthickness=0,bd=0,command=self.bt_New_com,text="New Circuit",
                                font=("arial",14))
            self.bt_New.bind("<Enter>",self.bt_New_enter)
            self.bt_New.bind("<Leave>",self.bt_New_leave)
            self.bt_New.place(x=5,y=3,width=219,height=28)
            self.bt_About=Button(self.lbl_setting,bg="#e1e1e1",activebackground="#e1e1e1",relief="flat",
                                highlightthickness=0,bd=0,command=self.bt_About_com,text="About",
                                font=("arial",14))
            self.bt_About.bind("<Enter>",self.bt_About_enter)
            self.bt_About.bind("<Leave>",self.bt_About_leave)
            self.bt_About.place(x=5,y=107,width=219,height=28)
            self.bt_Exit=Button(self.lbl_setting,bg="#e1e1e1",activebackground="#e1e1e1",relief="flat",
                                highlightthickness=0,bd=0,command=self.close_app,text="Exit",
                                font=("arial",14))
            self.bt_Exit.bind("<Enter>",self.bt_Exit_enter)
            self.bt_Exit.bind("<Leave>",self.bt_Exit_leave)
            self.bt_Exit.place(x=5,y=141,width=219,height=28)
            
            self.image1=PhotoImage(file=direct+"\\CircuitFiles\\image1.png")
            self.lbl_line2=Label(self.win2,image=self.image1,bd=0,highlightthickness=0)
            self.lbl_line2.place(x=278,y=140)
            
            self.lbl_selected2=Label(self.win2,bg="#1398f5",bd=0,highlightthickness=0)
            self.lbl_selected2.place(x=278,y=115,width=156,height=38)
            
            self.lbl_bar2=Label(self.win2,bg="#454444",bd=0,highlightthickness=0)
            self.lbl_bar2.place(x=278,y=108,width=468,height=41)
            
            self.image_value_before=PhotoImage(file=direct+"\\CircuitFiles\\value_before.png")
            self.image_method_before=PhotoImage(file=direct+"\\CircuitFiles\\Method_before.png")
            self.image_current_before=PhotoImage(file=direct+"\\CircuitFiles\\Current_before.png")
            self.image_value_after=PhotoImage(file=direct+"\\CircuitFiles\\value_after.png")
            self.image_method_after=PhotoImage(file=direct+"\\CircuitFiles\\Method_after.png")
            self.image_current_after=PhotoImage(file=direct+"\\CircuitFiles\\Current_after.png")
            self.bt_value=Button(self.win2,command=self.bt_value_com,image=self.image_value_before,bg="#1398f5",
                               activebackground="#1398f5",relief="flat",highlightthickness=0,bd=0)
            self.bt_value.bind("<Enter>",self.bt_value_enter)
            self.bt_value.bind("<Leave>",self.bt_value_leave)
            self.bt_value.place(x=278,y=108)
            self.bt_method=Button(self.win2,command=self.bt_method_com,image=self.image_method_before,bg="White",
                               activebackground="#1398f5",relief="flat",highlightthickness=0,bd=0)
            self.bt_method.bind("<Enter>",self.bt_method_enter)
            self.bt_method.bind("<Leave>",self.bt_method_leave)
            self.bt_method.place(x=434,y=108)
            self.bt_list_setting_active=0
            self.bt_current=Button(self.win2,command=self.bt_current_com,image=self.image_current_before,bg="White",
                               activebackground="#1398f5",relief="flat",highlightthickness=0,bd=0)
            self.bt_current.bind("<Enter>",self.bt_current_enter)
            self.bt_current.bind("<Leave>",self.bt_current_leave)
            self.bt_current.place(x=590,y=108)
            
            self.lbl_selected1=Label(self.win2,bg="#1398f5",bd=0,highlightthickness=0)
            self.lbl_selected1.place(x=172,y=67,width=153,height=38)
            
            self.image2=PhotoImage(file=direct+"\\CircuitFiles\\image2.png")
            self.lbl_line1=Label(self.win2,image=self.image2,bd=0,highlightthickness=0)
            self.lbl_line1.place(x=172,y=95)
            
            self.lbl_bar1=Label(self.win2,bg="#363636",bd=0,highlightthickness=0)
            self.lbl_bar1.place(x=172,y=60,width=679,height=41)
            
            self.image_resistance_before=PhotoImage(file=direct+"\\CircuitFiles\\Resistance_before.png")
            self.image_capacitor_before=PhotoImage(file=direct+"\\CircuitFiles\\Capacitor_before.png")
            self.image_inductor_before=PhotoImage(file=direct+"\\CircuitFiles\\Inductor_before.png")
            self.image_vs_before=PhotoImage(file=direct+"\\CircuitFiles\\VS_before.png")
            self.image_cs_before=PhotoImage(file=direct+"\\CircuitFiles\\CS_before.png")
            self.image_others_before=PhotoImage(file=direct+"\\CircuitFiles\\Others_before.png")
            
            self.image_resistance_after=PhotoImage(file=direct+"\\CircuitFiles\\Resistance_after.png")
            self.image_capacitor_after=PhotoImage(file=direct+"\\CircuitFiles\\Capacitor_after.png")
            self.image_inductor_after=PhotoImage(file=direct+"\\CircuitFiles\\Inductor_after.png")
            self.image_vs_after=PhotoImage(file=direct+"\\CircuitFiles\\VS_after.png")
            self.image_cs_after=PhotoImage(file=direct+"\\CircuitFiles\\CS_after.png")
            self.image_others_after=PhotoImage(file=direct+"\\CircuitFiles\\Others_after.png")
            
            self.bt_resistance=Button(self.win2,command=self.bt_resistance_com,image=self.image_resistance_before,bg="#1398f5",
                               activebackground="#1398f5",relief="flat",highlightthickness=0,bd=0)
            self.bt_resistance.bind("<Enter>",self.bt_resistance_enter)
            self.bt_resistance.bind("<Leave>",self.bt_resistance_leave)
            self.bt_resistance.place(x=172,y=60)
            
            self.bt_capacitor=Button(self.win2,command=self.bt_capacitor_com,image=self.image_capacitor_before,bg="white",
                               activebackground="#1398f5",relief="flat",highlightthickness=0,bd=0)
            self.bt_capacitor.bind("<Enter>",self.bt_capacitor_enter)
            self.bt_capacitor.bind("<Leave>",self.bt_capacitor_leave)
            self.bt_capacitor.place(x=325,y=60)
            
            self.bt_inductor=Button(self.win2,command=self.bt_inductor_com,image=self.image_inductor_before,bg="white",
                               activebackground="#1398f5",relief="flat",highlightthickness=0,bd=0)
            self.bt_inductor.bind("<Enter>",self.bt_inductor_enter)
            self.bt_inductor.bind("<Leave>",self.bt_inductor_leave)
            self.bt_inductor.place(x=479,y=60)
            
            self.bt_vs=Button(self.win2,command=self.bt_vs_com,image=self.image_vs_before,bg="white",
                               activebackground="#1398f5",relief="flat",highlightthickness=0,bd=0)
            self.bt_vs.bind("<Enter>",self.bt_vs_enter)
            self.bt_vs.bind("<Leave>",self.bt_vs_leave)
            self.bt_vs.place(x=611,y=60)
            
            self.bt_cs=Button(self.win2,command=self.bt_cs_com,image=self.image_cs_before,bg="white",
                               activebackground="#1398f5",relief="flat",highlightthickness=0,bd=0)
            self.bt_cs.bind("<Enter>",self.bt_cs_enter)
            self.bt_cs.bind("<Leave>",self.bt_cs_leave)
            self.bt_cs.place(x=675,y=60)
            
            self.bt_others=Button(self.win2,command=self.bt_others_com,image=self.image_others_before,bg="white",
                               activebackground="#1398f5",relief="flat",highlightthickness=0,bd=0)
            self.bt_others.bind("<Enter>",self.bt_others_enter)
            self.bt_others.bind("<Leave>",self.bt_others_leave)
            self.bt_others.place(x=741,y=60)
            self.ent.focus_set()
            
            self.image_solve_before=PhotoImage(file=direct+"\\CircuitFiles\\solve_before.png")
            self.image_solve_after=PhotoImage(file=direct+"\\CircuitFiles\\solve_after.png")
            self.bt_solve=self.canvas2.create_image(736,542,anchor=NW,image=self.image_solve_before)
            
            self.canvas2.tag_bind(self.bt_solve,"<Enter>",self.bt_solve_enter)
            self.canvas2.tag_bind(self.bt_solve,"<Leave>",self.bt_solve_leave)
            self.canvas2.tag_bind(self.bt_solve,"<Button-1>",self.bt_solve_com)
            
            self.image_loops_before=PhotoImage(file=direct+"\\CircuitFiles\\Loops_before.png")
            self.image_MoreEqns_before=PhotoImage(file=direct+"\\CircuitFiles\\MoreEqns_before.png")
            self.image_voltage_before=PhotoImage(file=direct+"\\CircuitFiles\\voltage_before.png")
            self.image_loops_after=PhotoImage(file=direct+"\\CircuitFiles\\Loops_after.png")
            self.image_MoreEqns_after=PhotoImage(file=direct+"\\CircuitFiles\\MoreEqns_after.png")
            self.image_voltage_after=PhotoImage(file=direct+"\\CircuitFiles\\voltage_after.png")
            self.image_blank=PhotoImage(file=direct+"\\CircuitFiles\\image_blank.png")
            
            self.image_showallsolns_before=PhotoImage(file=direct+"\\CircuitFiles\\showallsolns_before.png")
            self.image_showallsolns_after=PhotoImage(file=direct+"\\CircuitFiles\\showallsolns_after.png")
            self.image_back_before=PhotoImage(file=direct+"\\CircuitFiles\\back_before.png")
            self.image_back_after=PhotoImage(file=direct+"\\CircuitFiles\\back_after.png")
            
            self.image_resistance=PhotoImage(file=direct+"\\CircuitFiles\\resistance.png")
            self.image_capacitor=PhotoImage(file=direct+"\\CircuitFiles\\capacitor.png")
            self.image_inductor=PhotoImage(file=direct+"\\CircuitFiles\\inductor.png")
            self.image_vs=PhotoImage(file=direct+"\\CircuitFiles\\vs.png")
            self.image_cs=PhotoImage(file=direct+"\\CircuitFiles\\cs.png")
            
            self.lbl_images=Label(self.win2,image=self.image_resistance,bd=0,highlightthickness=0,
                                      bg="#212020")
            self.lbl_images.place(x=785,y=127)
            self.lbl_type=Label(self.win2,text="Type:",fg="white",bg="#212020",font=("arial",18))
            self.lbl_type_value=Label(self.win2,text="",fg="white",bg="#212020",font=("arial",18))
            self.lbl_value=Label(self.win2,text="Value:",fg="white",bg="#212020",font=("arial",18))
            self.lbl_value_value=Label(self.win2,text="",fg="white",bg="#212020",font=("arial",18))
            self.lbl_method=Label(self.win2,text="Method:",fg="white",bg="#212020",font=("arial",18))
            self.lbl_method_value=Label(self.win2,text="",fg="white",bg="#212020",font=("arial",18))
            self.lbl_current=Label(self.win2,text="Current:",fg="#ed0c0c",bg="#212020",font=("arial",18))
            self.lbl_current_value=Label(self.win2,text="",fg="#ed0c0c",bg="#212020",font=("arial",18))
            self.lbl_voltage=Label(self.win2,text="Volatge:",fg="#16a2e4",bg="#212020",font=("arial",18))
            self.lbl_voltage_value=Label(self.win2,text="",fg="#16a2e4",bg="#212020",font=("arial",18))
            self.lbl_power=Label(self.win2,text="Power:",fg="#f0d30f",bg="#212020",font=("arial",18))
            self.lbl_power_value=Label(self.win2,text="",fg="#f0d30f",bg="#212020",font=("arial",18))
            self.lbl_powerfactor=Label(self.win2,text="Power Factor:",fg="#ed145b",bg="#212020",font=("arial",18))
            self.lbl_powerfactor_value=Label(self.win2,text="",fg="#ed145b",bg="#212020",font=("arial",18))
            self.lbl_totalpowerabsorbed=Label(self.win2,text="Total Power Absorbed:",fg="white",bg="#212020",font=("arial",18))
            self.lbl_totalpowerabsorbed_value=Label(self.win2,text="",fg="white",bg="#212020",font=("arial",18))
            self.lbl_totalpowerdelivered=Label(self.win2,text="Total Power Delivered:",fg="white",bg="#212020",font=("arial",18))
            self.lbl_totalpowerdelivered_value=Label(self.win2,text="",fg="white",bg="#212020",font=("arial",18))
            
            
            self.image_right_before=PhotoImage(file=direct+"\\CircuitFiles\\right_before.png")
            self.image_right_after=PhotoImage(file=direct+"\\CircuitFiles\\right_after.png")
            self.image_left_before=PhotoImage(file=direct+"\\CircuitFiles\\left_before.png")
            self.image_left_after=PhotoImage(file=direct+"\\CircuitFiles\\left_after.png")
            self.lbl_solutions=Label(self.win2,text="Solutions",fg="white",bg="#212020",font=("arial",20))
            
            self.bt_right=Button(self.win2,bd=0,highlightthickness=0,bg="#212020",activebackground="#212020",relief="flat",image=self.image_right_before,command=self.bt_right_com)
            self.bt_right.bind("<Enter>",self.bt_right_enter)
            self.bt_right.bind("<Leave>",self.bt_right_leave)
            self.bt_right.place(x=954,y=15)
            
            self.bt_left=Button(self.win2,bd=0,highlightthickness=0,bg="#212020",activebackground="#212020",relief="flat",image=self.image_left_before,command=self.bt_left_com)
            self.bt_left.bind("<Enter>",self.bt_left_enter)
            self.bt_left.bind("<Leave>",self.bt_left_leave)
            self.bt_left.place(x=934,y=15)
            
            self.bt_back=self.canvas2.create_image(1200,720,image=self.image_back_before)
            self.canvas2.tag_bind(self.bt_back,"<Enter>",self.bt_back_enter)
            self.canvas2.tag_bind(self.bt_back,"<Leave>",self.bt_back_leave)
            self.canvas2.tag_bind(self.bt_back,"<Button-1>",self.bt_back_com)
            
            self.bt_ShowAllSolns=self.canvas2.create_image(1200,720,image=self.image_showallsolns_before)
            self.canvas2.tag_bind(self.bt_ShowAllSolns,"<Enter>",self.bt_ShowAllSolns_enter)
            self.canvas2.tag_bind(self.bt_ShowAllSolns,"<Leave>",self.bt_ShowAllSolns_leave)
            self.canvas2.tag_bind(self.bt_ShowAllSolns,"<Button-1>",self.bt_ShowAllSolns_com)
            
            self.image_msgbox_problem=PhotoImage(file=direct+"\\CircuitFiles\\msgbox_problem.png")
            self.image_msgbox_about=PhotoImage(file=direct+"\\CircuitFiles\\msgbox_about.png")
            self.lbl_msgbox=Label(self.win2,bd=0,highlightthickness=0,image=self.image_msgbox_problem)
            
            self.bt_close_msgbox=Button(self.win2,bd=0,highlightthickness=0,bg="#353434",activebackground="#353434",relief="flat",image=self.image_close_before,command=self.bt_close_msgbox_com)
            self.bt_close_msgbox.bind("<Enter>",self.bt_close_msgbox_enter)
            self.bt_close_msgbox.bind("<Leave>",self.bt_close_msgbox_leave)
            
            self.list_resistances_value=[]
            self.list_capacitors_value=[]
            self.list_inductors_value=[]
            self.list_resistances_method=[]
            self.list_capacitors_method=[]
            self.list_inductors_method=[]
            self.list_resistances_current=[]
            self.list_capacitors_current=[]
            self.list_inductors_current=[]
            self.list_vs_value=[]
            self.list_vs_method=[]
            self.list_vs_current=[]
            self.list_cs_value=[]
            self.list_cs_method=[]
            self.list_cs_voltage=[]
            self.list_loops=[]
            self.list_MoreEqns=[]
    def close_app(self):
        try:
            self.win2.destroy()
            self.destroy()
        except:
            pass
    def bt_close_enter(self,e):
        try:
            self.bt_close.config(image=self.image_close_after)
        except:
            pass
    def bt_close_leave(self,e):
        try:
            self.bt_close.config(image=self.image_close_before)
        except:
            pass
    def bt_add_com2(self):
        try:
            self.bt_add_com(None)
        except:
            pass
    def bt_add_com(self,e):
        try:
            value1=self.listbox1.curselection()
            value2=self.listbox2.curselection()
            value3=self.listbox3.curselection()
            if self.ent.get()!="":
                if value1==() and value2==() and value3==():
                    if self.bt_value_active==1:
                        value=self.ent.get()
                        self.listbox1.insert(END,value)
                        self.ent.delete(0,END)
                        if self.bt_Resistance_active==1:
                            self.list_resistances_value.append(value)
                            self.bt_method_com()
                        elif self.bt_Capacitor_active==1:
                            self.list_capacitors_value.append(value)
                            self.bt_method_com()
                        elif self.bt_Inductor_active==1:
                            self.list_inductors_value.append(value)
                            self.bt_method_com()
                        elif self.bt_VS_active==1:
                            self.list_vs_value.append(value)
                            self.bt_method_com()
                        elif self.bt_CS_active==1:
                            self.list_cs_value.append(value)
                            self.bt_method_com()
                        elif self.bt_Others_active==1:
                            self.list_loops.append(value)
                    elif self.bt_method_active==1:
                        value=self.ent.get()
                        self.listbox2.insert(END,value)
                        self.ent.delete(0,END)
                        if self.bt_Resistance_active==1:
                            self.list_resistances_method.append(value)
                            self.bt_current_com()
                        elif self.bt_Capacitor_active==1:
                            self.list_capacitors_method.append(value)
                            self.bt_current_com()
                        elif self.bt_Inductor_active==1:
                            self.list_inductors_method.append(value)
                            self.bt_current_com()
                        elif self.bt_VS_active==1:
                            self.list_vs_method.append(value)
                            self.bt_current_com()
                        elif self.bt_CS_active==1:
                            self.list_cs_method.append(value)
                            self.bt_current_com()
                        elif self.bt_Others_active==1:
                            self.list_MoreEqns.append(value)
                    elif self.bt_current_active==1:
                        value=self.ent.get()
                        self.listbox3.insert(END,value)
                        self.ent.delete(0,END)
                        if self.bt_Resistance_active==1:
                            self.list_resistances_current.append(value)
                            self.bt_value_com()
                        elif self.bt_Capacitor_active==1:
                            self.list_capacitors_current.append(value)
                            self.bt_value_com()
                        elif self.bt_Inductor_active==1:
                            self.list_inductors_current.append(value)
                            self.bt_value_com()
                        elif self.bt_VS_active==1:
                            self.list_vs_current.append(value)
                            self.bt_value_com()
                        elif self.bt_CS_active==1:
                            self.list_cs_voltage.append(value)
                            self.bt_value_com()
                else:
                    if value1!=():
                        self.listbox1.delete(value1[0])
                        self.listbox1.insert(value1[0],self.ent.get())
                        if self.bt_Resistance_active==1:
                            self.list_resistances_value[value1[0]]=self.ent.get()
                        elif self.bt_Capacitor_active==1:
                            self.list_capacitors_value[value1[0]]=self.ent.get()
                        elif self.bt_Inductor_active==1:
                            self.list_inductors_value[value1[0]]=self.ent.get()
                        elif self.bt_VS_active==1:
                            self.list_vs_value[value1[0]]=self.ent.get()
                        elif self.bt_CS_active==1:
                            self.list_cs_value[value1[0]]=self.ent.get()
                        elif self.bt_Others_active==1:
                            self.list_loops[value1[0]]=self.ent.get()
                    elif value2!=():
                        self.listbox2.delete(value2[0])
                        self.listbox2.insert(value2[0],self.ent.get())
                        if self.bt_Resistance_active==1:
                            self.list_resistances_method[value2[0]]=self.ent.get()
                        elif self.bt_Capacitor_active==1:
                            self.list_capacitors_method[value2[0]]=self.ent.get()
                        elif self.bt_Inductor_active==1:
                            self.list_inductors_method[value2[0]]=self.ent.get()
                        elif self.bt_VS_active==1:
                            self.list_vs_method[value2[0]]=self.ent.get()
                        elif self.bt_CS_active==1:
                            self.list_cs_method[value2[0]]=self.ent.get()
                        elif self.bt_Others_active==1:
                            self.list_MoreEqns[value2[0]]=self.ent.get()
                    elif value3!=():
                        self.listbox3.delete(value3[0])
                        self.listbox3.insert(value3[0],self.ent.get())
                        if self.bt_Resistance_active==1:
                            self.list_resistances_current[value3[0]]=self.ent.get()
                        elif self.bt_Capacitor_active==1:
                            self.list_capacitors_current[value3[0]]=self.ent.get()
                        elif self.bt_Inductor_active==1:
                            self.list_inductors_current[value3[0]]=self.ent.get()
                        elif self.bt_VS_active==1:
                            self.list_vs_current[value3[0]]=self.ent.get()
                        elif self.bt_CS_active==1:
                            self.list_cs_voltage[value3[0]]=self.ent.get()
                        
                    self.ent.delete(0,END)
        except:
            pass
    def bt_add_enter(self,e):
        try:
            self.bt_add.config(image=self.image_add_after)
        except:
            pass
    def bt_add_leave(self,e):
        try:
            self.bt_add.config(image=self.image_add_before)
        except:
            pass
    def bt_setting_com(self):
        try:
            if self.bt_list_setting_active==0:
                self.lbl_setting.place(x=37,y=114)
                self.bt_list_setting_active=1
            else:
                self.lbl_setting.place_forget()       
                self.bt_list_setting_active=0
        except:
            pass
    def bt_setting_enter(self,e):
        try:
            self.bt_setting.config(image=self.image_setting_after)
        except:
            pass
    def bt_setting_leave(self,e):
        try:
            self.bt_setting.config(image=self.image_setting_before)
        except:
            pass
    def bt_open_enter(self,e):
        try:
            self.bt_open.config(bg="#1398f5")
        except:
            pass
    def bt_open_leave(self,e):
        try:
            self.bt_open.config(bg="#e1e1e1")
        except:
            pass
    def bt_open_com(self):
        try:
            self.lbl_setting.place_forget()
            file_path=filedialog.askopenfilename()
            self.bt_list_setting_active=0
            if file_path !="":
                self.bt_New_com()
                info=""
                with open(file_path,"r") as f1:
                    info=f1.read()
                list_info=info.splitlines()
                for index in range(0,len(list_info)):
                    list_info[index]=list_info[index].split("/")
                for list in list_info:
                    if "Res" in list:
                        self.list_resistances_value.append(list[1])
                        self.list_resistances_method.append(list[2])
                        self.list_resistances_current.append(list[3])
                    elif "Cap" in list:
                        self.list_capacitors_value.append(list[1])
                        self.list_capacitors_method.append(list[2])
                        self.list_capacitors_current.append(list[3])
                    elif "Ind" in list:
                        self.list_inductors_value.append(list[1])
                        self.list_inductors_method.append(list[2])
                        self.list_inductors_current.append(list[3])
                    elif "VS" in list:
                        self.list_vs_value.append(list[1])
                        self.list_vs_method.append(list[2])
                        self.list_vs_current.append(list[3])
                    elif "CS" in list:
                        self.list_cs_value.append(list[1])
                        self.list_cs_method.append(list[2])
                        self.list_cs_voltage.append(list[3])
                    elif "Loop" in list:
                        self.list_loops.append(list[1])
                    elif "MoreEqns" in list:
                        self.list_MoreEqns.append(list[1])
                    self.bt_resistance_com()
        except:
            pass
    def bt_save_com(self):
        # (self.list_resistances_value,self.list_resistances_method,self.list_resistances_current,
        # self.list_capacitors_value,self.list_capacitors_method,self.list_capacitors_current,
        # self.list_inductors_value,self.list_inductors_method,self.list_inductors_current,
        # self.list_vs_value,self.list_vs_method,self.list_vs_current,self.list_cs_value,
        # self.list_cs_method,self.list_cs_voltage,self.list_loops,self.list_MoreEqns)
        try:
            self.lbl_setting.place_forget()
            self.bt_list_setting_active=0
            path_file=filedialog.asksaveasfilename(initialdir='/', title='Save File', filetypes=(('Text Files', 'txt.*'), ('All Files', '*.*')))
            if path_file !="":
                if ".txt" in path_file:
                    path_file=path_file.replace(".txt","")
                with open(path_file,"w") as f1:
                    for index in range(0,len(self.list_resistances_value)):
                        f1.write("Res/"+self.list_resistances_value[index]+"/"+self.list_resistances_method[index]+"/"+
                                 self.list_resistances_current[index]+"\n")
                    for index in range(0,len(self.list_capacitors_value)):
                        f1.write("Cap/"+self.list_capacitors_value[index]+"/"+self.list_capacitors_method[index]+"/"+
                                 self.list_capacitors_current[index]+"\n")
                    for index in range(0,len(self.list_inductors_value)):
                        f1.write("Ind/"+self.list_inductors_value[index]+"/"+self.list_inductors_method[index]+"/"+
                                 self.list_inductors_current[index]+"\n")
                    for index in range(0,len(self.list_vs_value)):
                        f1.write("VS/"+self.list_vs_value[index]+"/"+self.list_vs_method[index]+"/"+
                                 self.list_vs_current[index]+"\n")
                    for index in range(0,len(self.list_cs_value)):
                        f1.write("CS/"+self.list_cs_value[index]+"/"+self.list_cs_method[index]+"/"+
                                 self.list_cs_voltage[index]+"\n")
                    for index in range(0,len(self.list_loops)):
                        f1.write("Loop/"+self.list_loops[index]+"\n")
                    for index in range(0,len(self.list_MoreEqns)):
                        f1.write("MoreEqns/"+self.list_MoreEqns[index]+"\n")
        except:
            pass
    def bt_save_enter(self,e):
        try:
            self.bt_save.config(bg="#1398f5")
        except:
            pass
    def bt_save_leave(self,e):
        try:
            self.bt_save.config(bg="#e1e1e1")
        except:
            pass
    def bt_New_com(self):
        try:
            self.lbl_vars.place_forget()
            self.lbl_voltages.place_forget()
            self.lbl_powers.place_forget()
            self.lbl_setting.place_forget()
            self.bt_list_setting_active=0
            self.listbox1.delete(0,END)
            self.listbox2.delete(0,END)
            self.listbox3.delete(0,END)
            self.win=1
            self.list_resistances_value=[]
            self.list_resistances_current=[]
            self.list_resistances_method=[]
            self.list_capacitors_value=[]
            self.list_capacitors_current=[]
            self.list_capacitors_method=[]
            self.list_inductors_value=[]
            self.list_inductors_current=[]
            self.list_inductors_method=[]
            self.list_vs_value=[]
            self.list_vs_current=[]
            self.list_vs_method=[]
            self.list_cs_value=[]
            self.list_cs_voltage=[]
            self.list_cs_method=[]
            self.list_loops=[]
            self.list_MoreEqns=[]
            
            try:
                self.bt_back_com(None)
            except:
                pass
        except:
            pass
    def bt_New_enter(self,e):
        try:
            self.bt_New.config(bg="#1398f5")
        except:
            pass
    def bt_New_leave(self,e):
        try:
            self.bt_New.config(bg="#e1e1e1")
        except:
            pass
    def bt_About_com(self):
        try:
            self.bt_list_setting_active=0
            self.lbl_setting.place_forget()
            self.lbl_msgbox.config(image=self.image_msgbox_about)
            self.lbl_msgbox.place(x=641,y=575)
            self.bt_close_msgbox.place(x=979,y=580)
        except:
            pass
    def bt_About_enter(self,e):
        try:
            self.bt_About.config(bg="#1398f5")
        except:
            pass
    def bt_About_leave(self,e):
        try:
            self.bt_About.config(bg="#e1e1e1")
        except:
            pass
    def bt_Exit_enter(self,e):
        try:
            self.bt_Exit.config(bg="#1398f5")
        except:
            pass
    def bt_Exit_leave(self,e):
        try:
            self.bt_Exit.config(bg="#e1e1e1")
        except:
            pass
    def bt_value_com(self):
        try:
            self.lbl_selected2.place(x=278,y=115)
            self.bt_value.config(bg="#1398f5")
            self.bt_method.config(bg="white")
            self.bt_current.config(bg="white")
            self.bt_value_active=1
            self.bt_method_active=0
            self.bt_current_active=0
        except:
            pass
    def bt_value_enter(self,e):
        try:
            if self.bt_Others_active==1:
                self.bt_value.config(image=self.image_loops_after)
            else:
                self.bt_value.config(image=self.image_value_after)
        except:
            pass
    def bt_value_leave(self,e):
        try:
            if self.bt_Others_active==1:
                self.bt_value.config(image=self.image_loops_before)
            else:
                self.bt_value.config(image=self.image_value_before)
        except:
            pass
    def bt_method_com(self):
        try:
            self.lbl_selected2.place(x=434,y=115)
            self.bt_value.config(bg="white")
            self.bt_method.config(bg="#1398f5")
            self.bt_current.config(bg="white")
            self.bt_value_active=0
            self.bt_method_active=1
            self.bt_current_active=0
        except:
            pass
    def bt_method_enter(self,e):
        try:
            if self.bt_Others_active==1:
                self.bt_method.config(image=self.image_MoreEqns_after)
                
            else:
                self.bt_method.config(image=self.image_method_after)
        except:
            pass
    def bt_method_leave(self,e):
        try:
            if self.bt_Others_active==1:
                self.bt_method.config(image=self.image_MoreEqns_before)
            else:
                self.bt_method.config(image=self.image_method_before)
        except:
            pass
    def bt_current_com(self):
        try:
            if self.bt_Others_active==0:
                self.lbl_selected2.place(x=590,y=115)
                self.bt_value.config(bg="white")
                self.bt_method.config(bg="white")
                self.bt_current.config(bg="#1398f5")
                self.bt_value_active=0
                self.bt_method_active=0
                self.bt_current_active=1
        except:
            pass
    def bt_current_enter(self,e):
        try:
            if self.bt_CS_active==1:
                self.bt_current.config(image=self.image_voltage_after)
            elif self.bt_Others_active==1:
                self.bt_current.config(image=self.image_blank)
            else:
                self.bt_current.config(image=self.image_current_after)
        except:
            pass
    def bt_current_leave(self,e):
        try:
            if self.bt_CS_active==1:
                self.bt_current.config(image=self.image_voltage_before)
            elif self.bt_Others_active==1:
                self.bt_current.config(image=self.image_blank)
            else:
                self.bt_current.config(image=self.image_current_before)
        except:
            pass
    def bt_resistance_com(self):
        try:
            self.lbl_images.config(image=self.image_resistance)
            self.lbl_images.place_configure(x=785,y=127)
            self.bt_value.config(image=self.image_value_before)
            self.bt_current.config(image=self.image_current_before)
            self.bt_method.config(image=self.image_method_before)
            self.listbox3.config(state="normal")
            self.bt_current.config(state="normal")
            self.bt_value_com()
            self.listbox1.delete(0,END)
            self.listbox2.delete(0,END)
            self.listbox3.delete(0,END)
            for res in self.list_resistances_value:
                self.listbox1.insert(END,res)
            for res in self.list_resistances_method:
                self.listbox2.insert(END,res)
            for res in self.list_resistances_current:
                self.listbox3.insert(END,res)
            self.listbox2.see(0)
            self.lbl_selected1.place(x=172,y=67,width=153,height=38)
            self.bt_resistance.config(bg="#1398f5")
            self.bt_capacitor.config(bg="white")
            self.bt_inductor.config(bg="white")
            self.bt_vs.config(bg="white")
            self.bt_cs.config(bg="white")
            self.bt_others.config(bg="white")
            self.bt_Resistance_active=1
            self.bt_Capacitor_active=0
            self.bt_Inductor_active=0
            self.bt_VS_active=0
            self.bt_CS_active=0
            self.bt_Others_active=0
        except:
            pass
    def bt_resistance_enter(self,e):
        try:
            self.bt_resistance.config(image=self.image_resistance_after)
        except:
            pass
    def bt_resistance_leave(self,e):
        try:
            self.bt_resistance.config(image=self.image_resistance_before)
        except:
            pass
    def bt_capacitor_com(self):
        try:
            self.lbl_images.config(image=self.image_capacitor)
            self.lbl_images.place_configure(x=808,y=111)
            self.bt_value.config(image=self.image_value_before)
            self.bt_current.config(image=self.image_current_before)
            self.bt_method.config(image=self.image_method_before)
            self.listbox3.config(state="normal")
            self.bt_current.config(state="normal")
            self.bt_value_com()
            self.listbox1.delete(0,END)
            self.listbox2.delete(0,END)
            self.listbox3.delete(0,END)
            for cap in self.list_capacitors_value:
                self.listbox1.insert(END,cap)
            for cap in self.list_capacitors_method:
                self.listbox2.insert(END,cap)
            for cap in self.list_capacitors_current:
                self.listbox3.insert(END,cap)
            self.lbl_selected1.place(x=325,y=67,width=154,height=38)
            self.bt_resistance.config(bg="white")
            self.bt_capacitor.config(bg="#1398f5")
            self.bt_inductor.config(bg="white")
            self.bt_vs.config(bg="white")
            self.bt_cs.config(bg="white")
            self.bt_others.config(bg="white")
            self.bt_Resistance_active=0
            self.bt_Capacitor_active=1
            self.bt_Inductor_active=0
            self.bt_VS_active=0
            self.bt_CS_active=0
            self.bt_Others_active=0
        except:
            pass
    def bt_capacitor_enter(self,e):
        try:
            self.bt_capacitor.config(image=self.image_capacitor_after)
        except:
            pass
    def bt_capacitor_leave(self,e):
        try:
            self.bt_capacitor.config(image=self.image_capacitor_before)
        except:
            pass
    def bt_inductor_com(self):
        try:
            self.lbl_images.config(image=self.image_inductor)
            self.lbl_images.place_configure(x=790,y=123)
            self.bt_value.config(image=self.image_value_before)
            self.bt_current.config(image=self.image_current_before)
            self.bt_method.config(image=self.image_method_before)
            self.listbox3.config(state="normal")
            self.bt_current.config(state="normal")
            self.bt_value_com()
            self.listbox1.delete(0,END)
            self.listbox2.delete(0,END)
            self.listbox3.delete(0,END)
            for ind in self.list_inductors_value:
                self.listbox1.insert(END,ind)
            for ind in self.list_inductors_method:
                self.listbox2.insert(END,ind)
            for ind in self.list_inductors_current:
                self.listbox3.insert(END,ind)
            self.lbl_selected1.place(x=479,y=67,width=132,height=38)
            self.bt_resistance.config(bg="white")
            self.bt_capacitor.config(bg="white")
            self.bt_inductor.config(bg="#1398f5")
            self.bt_vs.config(bg="white")
            self.bt_cs.config(bg="white")
            self.bt_others.config(bg="white")
            self.bt_Resistance_active=0
            self.bt_Capacitor_active=0
            self.bt_Inductor_active=1
            self.bt_VS_active=0
            self.bt_CS_active=0
            self.bt_Others_active=0
        except:
            pass
    def bt_inductor_enter(self,e):
        try:
            self.bt_inductor.config(image=self.image_inductor_after)
        except:
            pass
    def bt_inductor_leave(self,e):
        try:
            self.bt_inductor.config(image=self.image_inductor_before)
        except:
            pass
    def bt_vs_com(self):
        try:
            self.lbl_images.config(image=self.image_vs)
            self.lbl_images.place_configure(x=791,y=103)
            self.bt_value.config(image=self.image_value_before)
            self.bt_current.config(image=self.image_current_before)
            self.bt_method.config(image=self.image_method_before)
            self.listbox3.config(state="normal")
            self.bt_current.config(state="normal")
            self.bt_value_com()
            self.listbox1.delete(0,END)
            self.listbox2.delete(0,END)
            self.listbox3.delete(0,END)
            for vs in self.list_vs_value:
                self.listbox1.insert(END,vs)
            for vs in self.list_vs_method:
                self.listbox2.insert(END,vs)
            for vs in self.list_vs_current:
                self.listbox3.insert(END,vs)
            self.lbl_selected1.place(x=611,y=67,width=64,height=38)
            self.bt_resistance.config(bg="white")
            self.bt_capacitor.config(bg="white")
            self.bt_inductor.config(bg="white")
            self.bt_vs.config(bg="#1398f5")
            self.bt_cs.config(bg="white")
            self.bt_others.config(bg="white")
            self.bt_Resistance_active=0
            self.bt_Capacitor_active=0
            self.bt_Inductor_active=0
            self.bt_VS_active=1
            self.bt_CS_active=0
            self.bt_Others_active=0
        except:
            pass
    def bt_vs_enter(self,e):
        try:
            self.bt_vs.config(image=self.image_vs_after)
        except:
            pass
    def bt_vs_leave(self,e):
        try:
            self.bt_vs.config(image=self.image_vs_before)
        except:
            pass
    def bt_cs_com(self):
        try:
            self.lbl_images.config(image=self.image_cs)
            self.lbl_images.place_configure(x=790,y=103)
            self.bt_value.config(image=self.image_value_before)
            self.bt_current.config(image=self.image_voltage_before)
            self.bt_method.config(image=self.image_method_before)
            self.listbox3.config(state="normal")
            self.bt_current.config(state="normal")
            self.bt_value_com()
            self.listbox1.delete(0,END)
            self.listbox2.delete(0,END)
            self.listbox3.delete(0,END)
            for cs in self.list_cs_value:
                self.listbox1.insert(END,cs)
            for cs in self.list_cs_method:
                self.listbox2.insert(END,cs)
            for cs in self.list_cs_voltage:
                self.listbox3.insert(END,cs)
            self.lbl_selected1.place(x=675,y=67,width=66,height=38)
            self.bt_resistance.config(bg="white")
            self.bt_capacitor.config(bg="white")
            self.bt_inductor.config(bg="white")
            self.bt_vs.config(bg="white")
            self.bt_cs.config(bg="#1398f5")
            self.bt_others.config(bg="white")
            self.bt_Resistance_active=0
            self.bt_Capacitor_active=0
            self.bt_Inductor_active=0
            self.bt_VS_active=0
            self.bt_CS_active=1
            self.bt_Others_active=0
        except:
            pass
    def bt_cs_enter(self,e):
        try:
            self.bt_cs.config(image=self.image_cs_after)
        except:
            pass
    def bt_cs_leave(self,e):
        try:
            self.bt_cs.config(image=self.image_cs_before)
        except:
            pass
    def bt_others_com(self):
        try:
            self.lbl_images.place_forget()
            self.bt_current.config(image=self.image_blank)
            self.bt_value.config(image=self.image_loops_before)
            self.bt_method.config(image=self.image_MoreEqns_before)
            self.bt_value_com()
            self.listbox1.delete(0,END)
            self.listbox2.delete(0,END)
            self.listbox3.delete(0,END)
            for loop in self.list_loops:
                self.listbox1.insert(END,loop)
            for eqn in self.list_MoreEqns:
                self.listbox2.insert(END,eqn)
            self.lbl_selected1.place(x=741,y=67,width=111,height=38)
            self.bt_resistance.config(bg="white")
            self.bt_capacitor.config(bg="white")
            self.bt_inductor.config(bg="white")
            self.bt_vs.config(bg="white")
            self.bt_cs.config(bg="white")
            self.bt_others.config(bg="#1398f5")
            self.bt_Resistance_active=0
            self.bt_Capacitor_active=0
            self.bt_Inductor_active=0
            self.bt_VS_active=0
            self.bt_CS_active=0
            self.bt_Others_active=1
            self.listbox3.config(state="disabled")
        except:
            pass
    def bt_others_enter(self,e):
        try:
            self.bt_others.config(image=self.image_others_after)
        except:
            pass
    def bt_others_leave(self,e):
        try:
            self.bt_others.config(image=self.image_others_before)
        except:
            pass
    def delete_com(self,e):
        try:
            value1=self.listbox1.curselection()
            value2=self.listbox2.curselection()
            value3=self.listbox3.curselection()
            if value1!=():
                self.listbox1.delete(value1[0])
                if self.bt_Resistance_active==1:
                    self.list_resistances_value.pop(value1[0])
                elif self.bt_Capacitor_active==1:
                    self.list_capacitors_value.pop(value1[0])
                elif self.bt_Inductor_active==1:
                    self.list_inductors_value.pop(value1[0])
                elif self.bt_VS_active==1:
                    self.list_vs_value.pop(value1[0])
                elif self.bt_CS_active==1:
                    self.list_cs_value.pop(value1[0])
                elif self.bt_Others_active==1:
                    self.list_loops.pop(value1[0])
            elif value2!=():
                self.listbox2.delete(value2[0])
                if self.bt_Resistance_active==1:
                    self.list_resistances_method.pop(value2[0])
                elif self.bt_Capacitor_active==1:
                    self.list_capacitors_method.pop(value2[0])
                elif self.bt_Inductor_active==1:
                    self.list_inductors_method.pop(value2[0])
                elif self.bt_VS_active==1:
                    self.list_vs_method.pop(value2[0])
                elif self.bt_CS_active==1:
                    self.list_cs_method.pop(value2[0])
                elif self.bt_Others_active==1:
                    self.list_MoreEqns.pop(value2[0])
            elif value3!=():
                self.listbox3.delete(value3[0])
                if self.bt_Resistance_active==1:
                    self.list_resistances_current.pop(value3[0])
                elif self.bt_Capacitor_active==1:
                    self.list_capacitors_current.pop(value3[0])
                elif self.bt_Inductor_active==1:
                    self.list_inductors_current.pop(value3[0])
                elif self.bt_VS_active==1:
                    self.list_vs_current.pop(value3[0])
                elif self.bt_CS_active==1:
                    self.list_cs_voltage.pop(value3[0])
        except:
            pass
    def bt_solve_enter(self,e):
        try:
            self.canvas2.itemconfig(self.bt_solve,image=self.image_solve_after)
        except:
            pass
    def bt_solve_leave(self,e):
        try:
            self.canvas2.itemconfig(self.bt_solve,image=self.image_solve_before)
        except:
            pass
    def bt_solve_com(self,e):
        try:
            if self.list_resistances_value==[] and self.list_capacitors_value==[] and self.list_inductors_value==[]:
                pass
            else:
                
                ########### solving
                s=0
                
                list_resistances_value1=self.list_resistances_value.copy()
                list_resistances_method1=self.list_resistances_method.copy()
                list_resistances_current1=self.list_resistances_current.copy()
                list_capacitors_value1=self.list_capacitors_value.copy()
                list_capacitors_method1=self.list_capacitors_method.copy()
                list_capacitors_current1=self.list_capacitors_current.copy()
                list_inductors_value1=self.list_inductors_value.copy()
                list_inductors_method1=self.list_inductors_method.copy()
                list_inductors_current1=self.list_inductors_current.copy()
                list_vs_value1=self.list_vs_value.copy()
                list_vs_method1=self.list_vs_method.copy()
                list_vs_current1=self.list_vs_current.copy()
                list_cs_value1=self.list_cs_value.copy()
                list_cs_method1=self.list_cs_method.copy()
                list_cs_voltage1=self.list_cs_voltage.copy()
                list_loops1=self.list_loops.copy()
                list_MoreEqns1=self.list_MoreEqns.copy()
                try:
                    self.solutions_list=circuit.App().PrepairingVars(list_resistances_value1,list_resistances_method1,list_resistances_current1,
                                                                        list_capacitors_value1,list_capacitors_method1,list_capacitors_current1,
                                                                        list_inductors_value1,list_inductors_method1,list_inductors_current1,
                                                                        list_vs_value1,list_vs_method1,list_vs_current1,list_cs_value1,
                                                                        list_cs_method1,list_cs_voltage1,list_loops1,list_MoreEqns1,"")
                        
                       
                        
                    s=1
                        
                except:
                    self.lbl_msgbox.config(image=self.image_msgbox_problem)
                    self.lbl_msgbox.place(x=641,y=575)
                    self.bt_close_msgbox.place(x=979,y=580)
                ########### if solved
                
                if s==1:
                    self.win=2
                    super_position=False
                    for soln in self.solutions_list:
                        if "cos" in soln:
                            super_position=True
                            break
                    self.canvas2.coords(self.bt_solve, 1024,720)
                    if super_position==False:
                        self.listbox1.delete(0,END)
                        
                        for soln in self.solutions_list:
                            print(soln)
                            try:
                                a=complex(soln[0])
                            except:
                                self.listbox1.insert(END,soln[1])
                        
                        
                        self.listbox2.place_forget()
                        self.listbox3.place_forget()
                        self.lbl_images.place_forget()
                        self.bt_add.place_forget()
                        self.ent.place_forget()
                        self.lbl_bar1.place_forget()
                        self.lbl_line1.place_forget()
                        self.lbl_bar2.place_forget()
                        self.lbl_line2.place_forget()
                        self.bt_resistance.place_forget()
                        self.bt_capacitor.place_forget()
                        self.bt_inductor.place_forget()
                        self.bt_cs.place_forget()
                        self.bt_vs.place_forget()
                        self.bt_others.place_forget()
                        self.bt_value.place_forget()
                        self.bt_method.place_forget()
                        self.bt_current.place_forget()
                        self.lbl_selected1.place_forget()
                        self.lbl_selected2.place_forget()
                        ################3 new win
                        
                        
                        
                        self.listbox1.place_configure(x=186,y=92,width=711,height=248)
                            
                        
                        
                        
                        self.lbl_type.place(x=195,y=342)
                        self.lbl_type_value.place(x=275,y=344)
                        
                        self.lbl_value.place(x=406,y=343)
                        self.lbl_value_value.place(x=490,y=344)
                        
                        
                        self.lbl_method.place(x=642,y=342)
                        self.lbl_method_value.place(x=755,y=342)
                        
                        self.lbl_current.place(x=195,y=396)
                        self.lbl_current_value.place(x=309,y=398)
                        
                        self.lbl_voltage.place(x=196,y=445)
                        self.lbl_voltage_value.place(x=309,y=447)
                        
                        self.lbl_power.place(x=196,y=491)
                        self.lbl_power_value.place(x=309,y=493)
                        
                        self.lbl_powerfactor.place(x=196,y=531)
                        self.lbl_powerfactor_value.place(x=375,y=533)
                        
                        self.lbl_totalpowerabsorbed.place(x=193,y=576)
                        self.lbl_totalpowerabsorbed_value.place(x=481,y=580)
                        
                        self.lbl_totalpowerdelivered.place(x=193,y=617)
                        self.lbl_totalpowerdelivered_value.place(x=481,y=620)
                        
                        
                        self.canvas2.coords(self.bt_ShowAllSolns,870,480)
                        self.canvas2.coords(self.bt_back,215,67)
                        self.lbl_solutions.place(x=468,y=54)
                        self.lbl_totalpowerabsorbed_value.config(text=self.solutions_list[-1][1])
                        self.lbl_totalpowerdelivered_value.config(text=self.solutions_list[-1][0])
                    else:
                        self.lbl_bar1.place_forget()
                        self.lbl_line1.place_forget()
                        self.lbl_bar2.place_forget()
                        self.lbl_line2.place_forget()
                        self.bt_resistance.place_forget()
                        self.bt_capacitor.place_forget()
                        self.bt_inductor.place_forget()
                        self.bt_cs.place_forget()
                        self.bt_vs.place_forget()
                        self.bt_others.place_forget()
                        self.bt_value.place_forget()
                        self.bt_method.place_forget()
                        self.bt_current.place_forget()
                        self.lbl_selected1.place_forget()
                        self.lbl_selected2.place_forget()
                        self.lbl_images.place_forget()
                        self.lbl_solutions.place(x=458,y=34)
                        self.bt_ShowAllSolns_com(None)
                        self.canvas2.coords(self.bt_back,215,67)
                        self.lbl_solutions.place(x=468,y=54)
        except:
            pass
    def bt_back_enter(self,e):
        try:
            self.canvas2.itemconfigure(self.bt_back,image=self.image_back_after)
        except:
            pass
    def bt_back_leave(self,e):
        try:
            self.canvas2.itemconfigure(self.bt_back,image=self.image_back_before)
        except:
            pass
    def bt_back_com(self,e):
        # self.listbox1.delete(0,END)
        # self.listbox2.delete(0,END)
        # self.listbox3.delete(0,END)
        # for value in self.list_resistances_value:
        #     self.listbox1.insert(END,value)
        # for method in self.list_resistances_method:
        #     self.listbox2.insert(END,method)
        # for current in self.list_resistances_current:
        #     self.listbox3.insert(END,current)
        try:
            self.win=1
            self.lbl_images.config(image=self.image_resistance)
            self.lbl_images.place_configure(x=785,y=127)
            self.lbl_solutions.place_forget()
            self.lbl_vars.place_forget()
            self.lbl_voltages.place_forget()
            self.lbl_powers.place_forget()
            self.lbl_type.place_forget()
            self.lbl_value.place_forget()
            self.lbl_method.place_forget()
            self.lbl_current.place_forget()
            self.lbl_voltage.place_forget()
            self.lbl_power.place_forget()
            self.lbl_powerfactor.place_forget()
            self.lbl_totalpowerabsorbed.place_forget()
            self.lbl_totalpowerdelivered.place_forget()
            self.lbl_type_value.place_forget()
            self.lbl_value_value.place_forget()
            self.lbl_method_value.place_forget()
            self.lbl_current_value.place_forget()
            self.lbl_voltage_value.place_forget()
            self.lbl_power_value.place_forget()
            self.lbl_powerfactor_value.place_forget()
            self.lbl_totalpowerabsorbed_value.place_forget()
            self.lbl_totalpowerdelivered_value.place_forget()
            try:
                self.canvas2.coords(self.bt_ShowAllSolns,1200,720)
            except:
                pass
            self.canvas2.coords(self.bt_back,1200,720)
            ##########3
            self.listbox1.config(bg="#212020",fg="#2290e5")
            self.listbox2.config(bg="#212020",fg="#2290e5")
            self.listbox3.config(bg="#212020",fg="#2290e5")
            self.listbox1.place_configure(x=33,y=180,width=284,height=349)
            self.listbox2.place(x=370,y=180,width=284,height=349)
            self.listbox3.place(x=707,y=180,width=284,height=349)
            self.bt_add.place(x=622,y=589)
            self.ent.place(x=171,y=589,width=432,height=33)
            self.canvas2.coords(self.bt_solve, 736,542)
            self.lbl_bar1.place(x=172,y=60,width=679,height=41)
            self.lbl_line1.place(x=172,y=95)
            self.lbl_bar2.place(x=278,y=108,width=468,height=41)
            self.lbl_line2.place(x=278,y=140)
            self.bt_resistance.place(x=172,y=60)
            self.bt_capacitor.place(x=325,y=60)
            self.bt_inductor.place(x=479,y=60)
            self.bt_cs.place(x=675,y=60)
            self.bt_vs.place(x=611,y=60)
            self.bt_others.place(x=741,y=60)
            self.bt_value.place(x=278,y=108)
            self.bt_method.place(x=434,y=108)
            self.bt_current.place(x=590,y=108)
            self.bt_resistance.config(bg="#1398f5")
            self.bt_capacitor.config(bg="white")
            self.bt_inductor.config(bg="white")
            self.bt_vs.config(bg="white")
            self.bt_cs.config(bg="white")
            self.bt_others.config(bg="white")
            self.bt_value.config(image=self.image_value_before,bg="#1398f5")
            self.bt_method.config(image=self.image_method_before,bg="white")
            self.bt_current.config(image=self.image_current_before,bg="white")
            self.lbl_selected1.place(x=172,y=67,width=153,height=38)
            self.lbl_selected2.place(x=278,y=115,width=156,height=38)
            self.bt_resistance_com()
        except:
            pass
    def ClickEventListbox(self,e):
        try:
            if self.win==2:
                index=self.listbox1.curselection()
                if index !=():
                    index=index[0]
                    self.lbl_type_value.config(text=self.solutions_list[index][0])
                    self.lbl_value_value.config(text=self.solutions_list[index][1])
                    self.lbl_method_value.config(text=self.solutions_list[index][2])
                    if self.solutions_list[index][0]=="CS":
                        self.lbl_current_value.config(text=self.solutions_list[index][1])
                        self.lbl_voltage_value.config(text=self.solutions_list[index][3])
                        self.lbl_power_value.config(text=self.solutions_list[index][4])
                        self.lbl_powerfactor_value.config(text=self.solutions_list[index][5])
                    else:
                        self.lbl_current_value.config(text=self.solutions_list[index][3])
                        if self.solutions_list[index][0]=="VS":
                            self.lbl_voltage_value.config(text=self.solutions_list[index][1])
                            self.lbl_power_value.config(text=self.solutions_list[index][4])
                            self.lbl_powerfactor_value.config(text=self.solutions_list[index][5])
                        else:
                            self.lbl_voltage_value.config(text=self.solutions_list[index][4])
                            self.lbl_power_value.config(text=self.solutions_list[index][5])
                            self.lbl_powerfactor_value.config(text=self.solutions_list[index][6])
        except:
            pass
    def bt_ShowAllSolns_com(self,e):
        try:
            if self.win==2:
                self.listbox1.delete(0,END)
                self.listbox2.delete(0,END)
                self.listbox3.delete(0,END)
                self.listbox3.config(state="normal")
                self.listbox1.place_configure(x=33,y=180,width=284,height=349)
                self.listbox2.place(x=370,y=180,width=284,height=349)
                self.listbox3.place(x=707,y=180,width=284,height=349)
                self.lbl_vars.place(x=145,y=145)
                self.lbl_voltages.place(x=478,y=145)
                self.lbl_powers.place(x=820,y=145)
                try:
                    self.canvas2.coords(self.bt_ShowAllSolns,1200,720)
                except:
                    pass
                self.lbl_type.place_forget()
                self.lbl_value.place_forget()
                self.lbl_method.place_forget()
                self.lbl_current.place_forget()
                self.lbl_voltage.place_forget()
                self.lbl_power.place_forget()
                self.lbl_powerfactor.place_forget()
                self.lbl_type_value.place_forget()
                self.lbl_value_value.place_forget()
                self.lbl_method_value.place_forget()
                self.lbl_current_value.place_forget()
                self.lbl_voltage_value.place_forget()
                self.lbl_power_value.place_forget()
                self.lbl_powerfactor_value.place_forget()
                
                
                list_resistances_value1=self.list_resistances_value.copy()
                list_resistances_method1=self.list_resistances_method.copy()
                list_resistances_current1=self.list_resistances_current.copy()
                list_capacitors_value1=self.list_capacitors_value.copy()
                list_capacitors_method1=self.list_capacitors_method.copy()
                list_capacitors_current1=self.list_capacitors_current.copy()
                list_inductors_value1=self.list_inductors_value.copy()
                list_inductors_method1=self.list_inductors_method.copy()
                list_inductors_current1=self.list_inductors_current.copy()
                list_vs_value1=self.list_vs_value.copy()
                list_vs_method1=self.list_vs_method.copy()
                list_vs_current1=self.list_vs_current.copy()
                list_cs_value1=self.list_cs_value.copy()
                list_cs_method1=self.list_cs_method.copy()
                list_cs_voltage1=self.list_cs_voltage.copy()
                list_loops1=self.list_loops.copy()
                list_MoreEqns1=self.list_MoreEqns.copy()
                
                self.solutions_list=circuit.App().PrepairingVars(list_resistances_value1,list_resistances_method1,list_resistances_current1,
                                                            list_capacitors_value1,list_capacitors_method1,list_capacitors_current1,
                                                            list_inductors_value1,list_inductors_method1,list_inductors_current1,
                                                            list_vs_value1,list_vs_method1,list_vs_current1,list_cs_value1,
                                                            list_cs_method1,list_cs_voltage1,list_loops1,list_MoreEqns1,"ShowAllSolns")
                n=0
                for soln in self.solutions_list:
                    if "=" in soln:
                        self.listbox1.insert(END,soln)
                    elif "VA" in soln and ":" in soln:
                        self.listbox3.insert(END,soln)
                    elif "V" in soln and ":" in soln and not soln[0]=="V":
                        self.listbox2.insert(END,soln)
                    elif "leading" in soln or "laging" in soln or "inphase" in soln:
                        if n==0:
                            self.listbox3.insert(END,"---------PowerFactor---------")
                            n=1
                        self.listbox3.insert(END,soln)
                self.lbl_totalpowerabsorbed_value.config(text=self.solutions_list[-2])
                self.lbl_totalpowerdelivered_value.config(text=self.solutions_list[-1])
        except:
            pass
    def bt_ShowAllSolns_enter(self,e):
        try:
            self.canvas2.itemconfig(self.bt_ShowAllSolns, image=self.image_showallsolns_after)
        except:
            pass
    def bt_ShowAllSolns_leave(self,e):
        try:
            self.canvas2.itemconfig(self.bt_ShowAllSolns, image=self.image_showallsolns_before)
        except:
            pass
    def bt_close_msgbox_enter(self,e):
        try:
            self.bt_close_msgbox.config(image=self.image_close_after)
        except:
            pass
    def bt_close_msgbox_leave(self,e):
        try:
            self.bt_close_msgbox.config(image=self.image_close_before)
        except:
            pass
    def bt_close_msgbox_com(self):
        try:
            self.bt_close_msgbox.place_forget()
            self.lbl_msgbox.place_forget()
        except:
            pass
    def bt_right_enter(self,e):
        try:
            self.bt_right.config(image=self.image_right_after)
        except:
            pass
    def bt_right_leave(self,e):
        try:
            self.bt_right.config(image=self.image_right_before)
        except:
            pass
    def bt_right_com(self):
        try:
            if self.position==0:
                pos_x=self.ws-1024
                pos_y=round((self.hs-720)/2)
                self.win2.geometry("1024x720+"+str(pos_x)+"+"+str(pos_y))
                self.position=1
            elif self.position==-1:
                pos_x=round((self.ws-1024)/2)
                pos_y=round((self.hs-720)/2)
                self.win2.geometry("1024x720+"+str(pos_x)+"+"+str(pos_y))
                self.position=0
        except:
            pass
    def bt_left_enter(self,e):
        try:
            self.bt_left.config(image=self.image_left_after)
        except:
            pass
    def bt_left_leave(self,e):
        try:
            self.bt_left.config(image=self.image_left_before)
        except:
            pass
    def bt_left_com(self):
        try:
            if self.position==0:
                pos_y=round((self.hs-720)/2)
                self.win2.geometry("1024x720+0+"+str(pos_y))
                self.position=-1
            elif self.position==1:
                pos_x=round((self.ws-1024)/2)
                pos_y=round((self.hs-720)/2)
                self.win2.geometry("1024x720+"+str(pos_x)+"+"+str(pos_y))
                self.position=0
        except:
            pass
    
        
        
        
        
        

        
        
        
        
app=CircuitAnalysis()

app.mainloop()

