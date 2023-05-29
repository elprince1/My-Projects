from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from ast import literal_eval
from photos import *
import os
direct =os.getcwd()
##list_names ## names
##list       ## bytes
if not os.path.exists(direct+"\\tkfiles"):
    os.mkdir(direct+"\\tkfiles")
    index1=0
    for file in list_names:
        with open(direct+"\\tkfiles\\"+file,"wb") as f1:
            f1.write(list[index1])
        index1+=1
class Designer(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        self.geometry("1920x1017")
        self.win_height=1017
        self.win_width=1920
        self.title("TK-(ELPRINCE)")
        self.state("zoomed")
        self.bind("<Return>",self.apply_com)
        self.bind("<Delete>",self.delete_widget)
        self.bind("<Control-s>",self.bt_save_com)
        self.bind("<Control-n>",self.bt_new_com)
        self.protocol('WM_DELETE_WINDOW', self.exit_com)
        ###############################################################3 widget tools
        self.lbl_widgets=Label(self,text="Widgets",font=("arial",16))
        self.lbl_widgets.place(x=50,y=50)
        self.list_widgets=Listbox(self,bd=0,highlightbackground="gray",highlightcolor="#13c2dc")
        self.list_widgets.place(x=50,y=80,width=140,height=345)
        
        self.image_button_before=PhotoImage(file=direct+"\\tkfiles\\image_button_before.png")
        self.image_button_after=PhotoImage(file=direct+"\\tkfiles\\image_button_after.png")
        self.bt_button=Button(self,image=self.image_button_before,relief="flat",bd=0,bg="white",activebackground="white",
                              command=self.bt_button_com)
        self.bt_button.bind("<Enter>",self.bt_button_enter)
        self.bt_button.bind("<Leave>",self.bt_button_leave)
        self.bt_button.place(x=55,y=85)
        
        self.image_entry_before=PhotoImage(file=direct+"\\tkfiles\\image_entry_before.png")
        self.image_entry_after=PhotoImage(file=direct+"\\tkfiles\\image_entry_after.png")
        self.bt_entry=Button(self,image=self.image_entry_before,relief="flat",bd=0,bg="white",activebackground="white",
                             command=self.bt_entry_com)
        self.bt_entry.bind("<Enter>",self.bt_entry_enter)
        self.bt_entry.bind("<Leave>",self.bt_entry_leave)
        self.bt_entry.place(x=55,y=135)
        
        self.image_label_before=PhotoImage(file=direct+"\\tkfiles\\image_label_before.png")
        self.image_label_after=PhotoImage(file=direct+"\\tkfiles\\image_label_after.png")
        self.bt_label=Button(self,image=self.image_label_before,relief="flat",bd=0,bg="white",activebackground="white",
                            command=self.bt_label_com)
        self.bt_label.bind("<Enter>",self.bt_label_enter)
        self.bt_label.bind("<Leave>",self.bt_label_leave)
        self.bt_label.place(x=55,y=185)
        
        self.image_listbox_before=PhotoImage(file=direct+"\\tkfiles\\image_listbox_before.png")
        self.image_listbox_after=PhotoImage(file=direct+"\\tkfiles\\image_listbox_after.png")
        self.bt_listbox=Button(self,image=self.image_listbox_before,relief="flat",bd=0,bg="white",activebackground="white",
                            command=self.bt_listbox_com)
        self.bt_listbox.bind("<Enter>",self.bt_listbox_enter)
        self.bt_listbox.bind("<Leave>",self.bt_listbox_leave)
        self.bt_listbox.place(x=55,y=235)
        
        self.image_radiobutton_before=PhotoImage(file=direct+"\\tkfiles\\image_radiobutton_before.png")
        self.image_radiobutton_after=PhotoImage(file=direct+"\\tkfiles\\image_radiobutton_after.png")
        self.bt_radiobutton=Button(self,image=self.image_radiobutton_before,relief="flat",bd=0,bg="white",activebackground="white",
                            command=self.bt_radiobutton_com)
        self.bt_radiobutton.bind("<Enter>",self.bt_radiobutton_enter)
        self.bt_radiobutton.bind("<Leave>",self.bt_radiobutton_leave)
        self.bt_radiobutton.place(x=55,y=285)
        
        self.image_checkbutton_before=PhotoImage(file=direct+"\\tkfiles\\image_checkbutton_before.png")
        self.image_checkbutton_after=PhotoImage(file=direct+"\\tkfiles\\image_checkbutton_after.png")
        self.bt_checkbutton=Button(self,image=self.image_checkbutton_before,relief="flat",bd=0,bg="white",activebackground="white",
                            command=self.bt_checkbutton_com)
        self.bt_checkbutton.bind("<Enter>",self.bt_checkbutton_enter)
        self.bt_checkbutton.bind("<Leave>",self.bt_checkbutton_leave)
        self.bt_checkbutton.place(x=55,y=335)
        
        self.image_canvas_before=PhotoImage(file=direct+"\\tkfiles\\image_canvas_before.png")
        self.image_canvas_after=PhotoImage(file=direct+"\\tkfiles\\image_canvas_after.png")
        self.bt_canvas=Button(self,image=self.image_canvas_before,relief="flat",bd=0,bg="white",activebackground="white",
                            command=self.bt_canvas_com)
        self.bt_canvas.bind("<Enter>",self.bt_canvas_enter)
        self.bt_canvas.bind("<Leave>",self.bt_canvas_leave)
        self.bt_canvas.place(x=55,y=385)
        
        ###############################################################3 canvas
        self.lbl_window=Label(self,text="Window",font=("arial",16))
        self.lbl_window.place(x=200,y=50)
        self.canvas=Canvas(self,bg="white",highlightthickness=0)
        self.canvas.bind("<Motion>",self.mouse_moving)
        self.canvas.place(x=200,y=80,width=1400,height=900)
        ###############################################################3 properties
        self.pos_list_properties=1610
        self.pos_lbls=1615
        self.pos_ents1=1745
        self.pos_ents2=1800
        self.pos_ents3=1830
        self.pos_bts=1883
        self.var_id=StringVar()
        self.var_posx=StringVar()
        self.var_posy=StringVar()
        self.var_width=StringVar()
        self.var_height=StringVar()
        self.var_text=StringVar()
        self.var_bg=StringVar()
        self.var_fg=StringVar()
        self.var_font=StringVar()
        self.var_imagebefore=StringVar()
        self.var_imageafter=StringVar()
        self.var_command=StringVar()
        self.var_highlightcolor=StringVar()
        self.var_highlightbackground=StringVar()
        self.var_activebackground=StringVar()
        self.var_activeforeground=StringVar()
        self.var_mouseenterbackground=StringVar()
        self.var_mouseleavebackground=StringVar()
        self.var_mouseenterforeground=StringVar()
        self.var_mouseleaveforeground=StringVar()
        self.lbl_properties=Label(self,text="Properties",font=("arial",16))
        self.lbl_properties.place(x=1610,y=80)
        self.list_properties=Listbox(self,bd=0,highlightbackground="gray",highlightcolor="#13c2dc")
        self.list_properties.place(x=1610,y=110,width=300,height=610)
        self.lbl_id=Label(self,text="id:",fg="#13c2dc",font=("arial",14),bg="white")
        self.lbl_id.place(x=1615,y=115)
        self.lbl_posx=Label(self,text="position-x:",fg="#13c2dc",font=("arial",14),bg="white")
        self.lbl_posx.place(x=1615,y=145)
        self.lbl_posy=Label(self,text="position-y:",fg="#13c2dc",font=("arial",14),bg="white")
        self.lbl_posy.place(x=1615,y=175)
        self.lbl_width=Label(self,text="width:",fg="#13c2dc",font=("arial",14),bg="white")
        self.lbl_width.place(x=1615,y=205)
        self.lbl_height=Label(self,text="height:",fg="#13c2dc",font=("arial",14),bg="white")
        self.lbl_height.place(x=1615,y=235)
        self.lbl_text=Label(self,text="text:",fg="#13c2dc",font=("arial",14),bg="white")
        self.lbl_text.place(x=1615,y=265)
        self.lbl_bg=Label(self,text="bg:",fg="#13c2dc",font=("arial",14),bg="white")
        self.lbl_bg.place(x=1615,y=295)
        self.lbl_fg=Label(self,text="fg:",fg="#13c2dc",font=("arial",14),bg="white")
        self.lbl_fg.place(x=1615,y=325)
        self.lbl_font=Label(self,text="font:",fg="#13c2dc",font=("arial",14),bg="white")
        self.lbl_font.place(x=1615,y=355)
        self.lbl_imagebefore=Label(self,text="image before:",fg="#13c2dc",font=("arial",14),bg="white")
        self.lbl_imagebefore.place(x=1615,y=385)
        self.lbl_imageafter=Label(self,text="image after:",fg="#13c2dc",font=("arial",14),bg="white")
        self.lbl_imageafter.place(x=1615,y=415)
        self.lbl_command=Label(self,text="command:",fg="#13c2dc",font=("arial",14),bg="white")
        self.lbl_command.place(x=1615,y=445)
        self.lbl_highlightcolor=Label(self,text="highlightcolor:",fg="#13c2dc",font=("arial",14),bg="white")
        self.lbl_highlightcolor.place(x=1615,y=475)
        self.lbl_highlightbackground=Label(self,text="highlightbackground:",fg="#13c2dc",font=("arial",14),bg="white")
        self.lbl_highlightbackground.place(x=1615,y=505)
        self.lbl_activebackground=Label(self,text="activebackground:",fg="#13c2dc",font=("arial",14),bg="white")
        self.lbl_activebackground.place(x=1615,y=535)
        self.lbl_activeforeground=Label(self,text="activeforeground:",fg="#13c2dc",font=("arial",14),bg="white")
        self.lbl_activeforeground.place(x=1615,y=565)
        self.lbl_mouseenterbackground=Label(self,text="mouseenterbackground:",fg="#13c2dc",font=("arial",14),bg="white")
        self.lbl_mouseenterbackground.place(x=1615,y=595)
        self.lbl_mouseleavebackground=Label(self,text="mouseleavebackground:",fg="#13c2dc",font=("arial",14),bg="white")
        self.lbl_mouseleavebackground.place(x=1615,y=625)
        self.lbl_mouseenterforeground=Label(self,text="mouseenterforeground:",fg="#13c2dc",font=("arial",14),bg="white")
        self.lbl_mouseenterforeground.place(x=1615,y=655)
        self.lbl_mouseleaveforeground=Label(self,text="mouseleaveforeground:",fg="#13c2dc",font=("arial",14),bg="white")
        self.lbl_mouseleaveforeground.place(x=1615,y=685)
        
        self.ent_id=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_id,relief="flat",highlightthickness=1)
        self.ent_id.place(x=1745,y=120,width=155)
        self.ent_posx=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_posx,relief="flat",highlightthickness=1)
        self.ent_posx.place(x=1745,y=150,width=155)
        self.ent_posy=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_posy,relief="flat",highlightthickness=1)
        self.ent_posy.place(x=1745,y=180,width=155)
        self.ent_width=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_width,relief="flat",highlightthickness=1)
        self.ent_width.place(x=1745,y=210,width=155)
        self.ent_height=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_height,relief="flat",highlightthickness=1)
        self.ent_height.place(x=1745,y=240,width=155)
        self.ent_text=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_text,relief="flat",highlightthickness=1)
        self.ent_text.place(x=1745,y=270,width=155)
        self.ent_bg=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_bg,relief="flat",highlightthickness=1)
        self.ent_bg.place(x=1745,y=300,width=155)
        self.ent_fg=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_fg,relief="flat",highlightthickness=1)
        self.ent_fg.place(x=1745,y=330,width=155)
        self.ent_font=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_font,relief="flat",highlightthickness=1)
        self.ent_font.place(x=1745,y=360,width=155)
        self.ent_imagebefore=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_imagebefore,relief="flat",highlightthickness=1)
        self.ent_imagebefore.place(x=1745,y=390,width=130)
        self.ent_imageafter=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_imageafter,relief="flat",highlightthickness=1)
        self.ent_imageafter.place(x=1745,y=420,width=130)
        self.ent_command=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_command,relief="flat",highlightthickness=1)
        self.ent_command.place(x=1745,y=450,width=155)
        self.ent_highlightcolor=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_highlightcolor,relief="flat",highlightthickness=1)
        self.ent_highlightcolor.place(x=1745,y=480,width=155)
        self.ent_highlightbackground=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_highlightbackground,relief="flat",highlightthickness=1)
        self.ent_highlightbackground.place(x=1800,y=510,width=100)
        self.ent_activebackground=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_activebackground,relief="flat",highlightthickness=1)
        self.ent_activebackground.place(x=1800,y=540,width=100)
        self.ent_activeforeground=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_activeforeground,relief="flat",highlightthickness=1)
        self.ent_activeforeground.place(x=1800,y=570,width=100)
        
        self.ent_mouseenterbackground=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_mouseenterbackground,relief="flat",highlightthickness=1)
        self.ent_mouseenterbackground.place(x=1830,y=600,width=70)
        self.ent_mouseleavebackground=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_mouseleavebackground,relief="flat",highlightthickness=1)
        self.ent_mouseleavebackground.place(x=1830,y=630,width=70)
        self.ent_mouseenterforeground=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_mouseenterforeground,relief="flat",highlightthickness=1)
        self.ent_mouseenterforeground.place(x=1830,y=660,width=70)
        self.ent_mouseleaveforeground=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_mouseleaveforeground,relief="flat",highlightthickness=1)
        self.ent_mouseleaveforeground.place(x=1830,y=690,width=70)
        
        self.bt_browse_imagebefore=Button(self,text="...",relief="flat",fg="gray",activeforeground="#13c2dc",bd=0,command=self.browse_imagebefore)
        self.bt_browse_imagebefore.place(x=1883,y=390)
        self.bt_browse_imageafter=Button(self,text="...",relief="flat",fg="gray",activeforeground="#13c2dc",bd=0,command=self.browse_imageafter)
        self.bt_browse_imageafter.place(x=1883,y=420)
        ###############################################################3 dragged widgets
        self.pos_list_draggedwidgets=520
        self.lbl_draggedwidgets=Label(self,text="D-Widgets",font=("arial",16))
        self.lbl_draggedwidgets.place(x=50,y=430)
        self.list_draggedwidgets=Listbox(self,bd=0,highlightbackground="gray",highlightcolor="#13c2dc",selectmode=SINGLE)
        self.list_draggedwidgets.place(x=50,y=460,width=140,height=520)
        self.list_draggedwidgets.bind("<<ListboxSelect>>",self.click_com)
        #################################################################    header
        self.path_file=StringVar()
        self.pos_lbl_errors=1830
        self.pos_lbl_errors_image=1860
        self.lbl_errors=Label(self,text="0",fg="green",font=("arial",16))
        self.lbl_errors.place(x=1830,y=10)
        self.image_errors=PhotoImage(file=direct+"\\tkfiles\\image_errors.png")
        self.lbl_errors_image=Label(self,image=self.image_errors)
        self.lbl_errors_image.place(x=1860,y=5)
        self.image_save_before=PhotoImage(file=direct+"\\tkfiles\\image_save_before.png")
        self.image_save_after=PhotoImage(file=direct+"\\tkfiles\\image_save_after.png")
        self.image_open_before=PhotoImage(file=direct+"\\tkfiles\\image_open_before.png")
        self.image_open_after=PhotoImage(file=direct+"\\tkfiles\\image_open_after.png")
        self.image_generate_before=PhotoImage(file=direct+"\\tkfiles\\image_generate_before.png")
        self.image_generate_after=PhotoImage(file=direct+"\\tkfiles\\image_generate_after.png")
        self.bt_save=Button(self,image=self.image_save_before,relief="flat",bd=0,command=self.bt_save_com)
        self.bt_save.bind("<Enter>",self.bt_save_enter)
        self.bt_save.bind("<Leave>",self.bt_save_leave)
        self.bt_save.place(x=19,y=10)
        self.bt_open=Button(self,image=self.image_open_before,relief="flat",bd=0,command=self.bt_open_com)
        self.bt_open.bind("<Enter>",self.bt_open_enter)
        self.bt_open.bind("<Leave>",self.bt_open_leave)
        self.bt_open.place(x=66,y=10)
        self.bt_generate=Button(self,image=self.image_generate_before,relief="flat",bd=0,command=self.bt_generate_com)
        self.bt_generate.bind("<Enter>",self.bt_generate_enter)
        self.bt_generate.bind("<Leave>",self.bt_generate_leave)
        self.bt_generate.place(x=112,y=10)
        self.lbl_path=Label(self,text="path:",font=("arial",12))
        self.lbl_path.place(x=155,y=12)
        self.ent_path=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",relief="flat",highlightthickness=1,textvariable=self.path_file)
        self.ent_path.place(x=201,y=15,height=19,width=260)
        #################################################################   window properties
        self.var_win_width=StringVar()
        self.var_win_height=StringVar()
        self.var_win_bg=StringVar()
        self.var_win_overrideredirect=StringVar()
        self.var_win_top=StringVar()
        self.var_win_posx=StringVar()
        self.var_win_posy=StringVar()
        self.var_win_mode=StringVar()
        self.var_win_width.set("1400")
        self.var_win_height.set("900")
        self.var_win_bg.set("white")
        self.var_win_overrideredirect.set("0")
        self.var_win_top.set("0")
        self.var_win_posx.set("center")
        self.var_win_posy.set("center")
        self.var_win_mode.set("self")
        self.lbl_win_bar=Label(self,bg="white")
        self.lbl_win_bar.place(x=300,y=48,width=1298,height=30)
        self.lbl_win_width=Label(self,text="width:",font=("arial",14),bg="white",fg="#13c2dc")
        self.lbl_win_width.place(x=305,y=50)
        self.ent_win_width=Entry(self,textvariable=self.var_win_width,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",relief="flat",highlightthickness=1)
        self.ent_win_width.place(x=360,y=53,width=100)
        self.lbl_win_height=Label(self,text="height:",font=("arial",14),bg="white",fg="#13c2dc")
        self.lbl_win_height.place(x=470,y=50)
        self.ent_win_height=Entry(self,textvariable=self.var_win_height,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",relief="flat",highlightthickness=1)
        self.ent_win_height.place(x=535,y=53,width=100)
        self.lbl_win_bg=Label(self,text="bg:",font=("arial",14),bg="white",fg="#13c2dc")
        self.lbl_win_bg.place(x=645,y=50)
        self.ent_win_bg=Entry(self,textvariable=self.var_win_bg,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",relief="flat",highlightthickness=1)
        self.ent_win_bg.place(x=680,y=53,width=100)
        self.lbl_win_overrideredirect=Label(self,text="overrideredirect:",font=("arial",14),bg="white",fg="#13c2dc")
        self.lbl_win_overrideredirect.place(x=790,y=50)
        self.combo_win_overrideredirect=ttk.Combobox(self,textvariable=self.var_win_overrideredirect)
        self.combo_win_overrideredirect["values"]=("0","1")
        self.combo_win_overrideredirect.place(x=935,y=53,width=50)
        self.lbl_win_top=Label(self,text="topmost:",font=("arial",14),bg="white",fg="#13c2dc")
        self.lbl_win_top.place(x=995,y=50)
        self.combo_win_top=ttk.Combobox(self,textvariable=self.var_win_top)
        self.combo_win_top["values"]=("0","1")
        self.combo_win_top.place(x=1075,y=53,width=50)
        self.lbl_win_posx=Label(self,text="posx:",font=("arial",14),bg="white",fg="#13c2dc")
        self.lbl_win_posx.place(x=1135,y=50)
        self.ent_win_posx=Entry(self,textvariable=self.var_win_posx,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",relief="flat",highlightthickness=1)
        self.ent_win_posx.place(x=1190,y=53,width=100)
        self.lbl_win_posy=Label(self,text="posy:",font=("arial",14),bg="white",fg="#13c2dc")
        self.lbl_win_posy.place(x=1300,y=50)
        self.ent_win_posy=Entry(self,textvariable=self.var_win_posy,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",relief="flat",highlightthickness=1)
        self.ent_win_posy.place(x=1355,y=53,width=100)
        self.lbl_win_mode=Label(self,text="mode:",font=("arial",14),bg="white",fg="#13c2dc")
        self.lbl_win_mode.place(x=1465,y=50)
        self.ent_win_mode=Entry(self,textvariable=self.var_win_mode,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",relief="flat",highlightthickness=1)
        self.ent_win_mode.place(x=1525,y=53,width=65)
        #########################################   status bar
        self.lbl_statusbar=Label(self,bg="#e1e1e1")
        self.lbl_statusbar.place(x=0,y=990,width=2000,height=30)
        self.lbl_mouse_pos=Label(self,bg="#e1e1e1",fg="black",font=("arial",12),text="pos-x: ,pos-y: ")
        self.lbl_mouse_pos.place(x=10,y=990)
        self.lbl_name=Label(self,text="MOSTAFA PRINCE",bg="#e1e1e1")
        self.lbl_name.place(x=1800,y=995)
        ###############################33   common
        self.choice=True
        self.n_button=0
        self.n_label=0
        self.n_entry=0
        self.n_listbox=0
        self.n_radiobutton=0
        self.n_checkbutton=0
        self.n_canvas=0
        self.list_widgets_canvas=[]
        self.list_widgets_options=[]
        self.list_win_options=["1400","900","white","0","0","center","center","self"]
        self.images=[]
        self.last_selected=None
        self.n_errors=0
    
    def bt_button_enter(self,e):
        self.bt_button.config(image=self.image_button_after)
    def bt_button_leave(self,e):
        self.bt_button.config(image=self.image_button_before)
    def bt_button_com(self):
        self.insert_widget("button")
    def bt_entry_enter(self,e):
        self.bt_entry.config(image=self.image_entry_after)
    def bt_entry_leave(self,e):
        self.bt_entry.config(image=self.image_entry_before)
    def bt_entry_com(self):
        self.insert_widget("entry")
    def bt_label_enter(self,e):
        self.bt_label.config(image=self.image_label_after)
    def bt_label_leave(self,e):
        self.bt_label.config(image=self.image_label_before)
    def bt_label_com(self):
        self.insert_widget("label")
    def bt_listbox_enter(self,e):
        self.bt_listbox.config(image=self.image_listbox_after)
    def bt_listbox_leave(self,e):
        self.bt_listbox.config(image=self.image_listbox_before)
    def bt_listbox_com(self):
        self.insert_widget("listbox")
    def bt_radiobutton_enter(self,e):
        self.bt_radiobutton.config(image=self.image_radiobutton_after)
    def bt_radiobutton_leave(self,e):
        self.bt_radiobutton.config(image=self.image_radiobutton_before)
    def bt_radiobutton_com(self):
        self.insert_widget("radiobutton")
    def bt_checkbutton_enter(self,e):
        self.bt_checkbutton.config(image=self.image_checkbutton_after)
    def bt_checkbutton_leave(self,e):
        self.bt_checkbutton.config(image=self.image_checkbutton_before)
    def bt_checkbutton_com(self):
        self.insert_widget("checkbutton")
    def bt_canvas_enter(self,e):
        self.bt_canvas.config(image=self.image_canvas_after)
    def bt_canvas_leave(self,e):
        self.bt_canvas.config(image=self.image_canvas_before)
    def bt_canvas_com(self):
        self.insert_widget("canvas")
    def apply_com(self,e):
        try:
            if self.last_selected !=None:
                index=self.last_selected
                if self.ent_id.get()!="":
                    s=0
                    n=0
                    for i in range(0,len(self.list_widgets_options)):
                        id_widget=self.list_draggedwidgets.get(i)
                        if id_widget==self.ent_id.get():
                            if n==1:
                                self.list_widgets_options[index][0]=self.ent_id.get()+"Error"
                                s=1
                                break
                            n+=1
                    if s==0:
                        self.list_widgets_options[index][0]=self.ent_id.get()
                if self.ent_posx.get()!="" and self.ent_posx.get().isnumeric():
                    self.list_widgets_options[index][1]=str(int(self.ent_posx.get()))
                if self.ent_posy.get()!="" and self.ent_posy.get().isnumeric():
                    self.list_widgets_options[index][2]=str(int(self.ent_posy.get()))
                if self.ent_width.get()!="" and self.ent_width.get().isnumeric():
                    self.list_widgets_options[index][3]=self.ent_width.get()
                if self.ent_height.get()!="" and self.ent_height.get().isnumeric():
                    self.list_widgets_options[index][4]=self.ent_height.get()
                if self.ent_highlightcolor.get()!="" and self.ent_highlightcolor.get()!="None":
                    s=0
                    try:
                        self.list_widgets_canvas[index].config(highlightcolor=self.ent_highlightcolor.get())
                        s=1
                    except:
                        pass
                    if s==1:
                        self.list_widgets_options[index][12]=self.ent_highlightcolor.get()
                    else:
                        self.list_widgets_options[index][12]=self.ent_highlightcolor.get()+"Error"
                else:
                    self.list_widgets_options[index][12]=None
                    self.list_widgets_canvas[index].config(highlightcolor=None)
                if self.ent_highlightbackground.get()!="" and self.ent_highlightbackground.get()!="None":
                    s=0
                    try:
                        self.list_widgets_canvas[index].config(highlightbackground=self.ent_highlightbackground.get())
                        s=1
                    except:
                        pass
                    if s==1:
                        self.list_widgets_options[index][13]=self.ent_highlightbackground.get()
                    else:
                        self.list_widgets_options[index][13]=self.ent_highlightbackground.get()+"Error"
                else:
                    self.list_widgets_options[index][13]=None
                    self.list_widgets_canvas[index].config(highlightbackground=None)
                self.list_widgets_canvas[index].place_configure(x=int(self.list_widgets_options[index][1]),y=int(self.list_widgets_options[index][2]),width=int(self.list_widgets_options[index][3]),
                                                                height=int(self.list_widgets_options[index][4]))
                if (self.list_widgets_canvas[index].winfo_class()=="Button" or self.list_widgets_canvas[index].winfo_class()=="Label" or
                   self.list_widgets_canvas[index].winfo_class()=="Radiobutton" or self.list_widgets_canvas[index].winfo_class()=="Checkbutton"):
                    s=0
                    try:
                        self.list_widgets_canvas[index].config(text=self.ent_text.get())
                        s=1
                    except:
                        pass
                    if s==1:
                        self.list_widgets_options[index][5]=self.ent_text.get()
                    else:
                        self.list_widgets_options[index][5]=self.ent_text.get()+"Error"
                else:
                    self.list_widgets_options[index][5]=""
                if self.ent_bg.get()!="" and self.ent_bg.get()!="None":
                    s=0
                    try:
                        self.list_widgets_canvas[index].config(bg=self.ent_bg.get())
                        s=1
                    except:
                        pass
                    if s==1:
                        self.list_widgets_options[index][6]=self.ent_bg.get()
                    else:
                        self.list_widgets_options[index][6]=self.ent_bg.get()+"Error"
                else:
                    self.list_widgets_options[index][6]=None
                    self.list_widgets_canvas[index].config(bg=None)
                if self.ent_fg.get()!="" and self.ent_fg.get()!="None":
                    s=0
                    try:
                        self.list_widgets_canvas[index].config(fg=self.ent_fg.get())
                        s=1
                    except:
                        pass
                    if s==1:
                        self.list_widgets_options[index][7]=self.ent_fg.get()
                    else:
                        self.list_widgets_options[index][7]=self.ent_fg.get()+"Error"
                else:
                    self.list_widgets_options[index][7]=None
                    self.list_widgets_canvas[index].config(fg=None)
                if (not self.list_widgets_canvas[index].winfo_class()=="Canvas") and self.ent_font.get().isnumeric():
                    s=0
                    try:
                        self.list_widgets_canvas[index].config(font=("arial",int(self.ent_font.get())))
                        s=1
                    except:
                        pass
                    if s==1:
                        self.list_widgets_options[index][8]=self.ent_font.get()
                    else:
                        self.list_widgets_options[index][8]=self.ent_font.get()+"Error"
                else:
                    if not self.ent_font.get().isnumeric() and not self.list_widgets_canvas[index].winfo_class()=="Canvas":
                        if self.ent_font.get()=="None":
                            self.list_widgets_options[index][8]=None
                        else:
                            self.list_widgets_options[index][8]=self.ent_font.get()+"Error"
                    elif not self.ent_font.get().isnumeric() and self.list_widgets_canvas[index].winfo_class()=="Canvas":
                        self.list_widgets_options[index][8]=""
                        
                if self.list_widgets_canvas[index].winfo_class()=="Button" or self.list_widgets_canvas[index].winfo_class()=="Label" or self.list_widgets_canvas[index].winfo_class()=="Canvas":
                    
                    if self.ent_imagebefore.get()!="None" and self.ent_imagebefore.get()!="":
                        s=0
                        
                        try:
                            self.images.append(PhotoImage(file=self.ent_imagebefore.get()))
                            if not self.list_widgets_canvas[index].winfo_class()=="Canvas":
                                self.list_widgets_canvas[index].config(image=self.images[-1])
                                
                            else:
                                
                                self.list_widgets_canvas[index].create_image(0,0,image=self.images[-1],anchor=NW)
                            s=1
                        except:
                            
                            pass
                        if s==1:
                            self.list_widgets_options[index][9]=self.ent_imagebefore.get()
                        else:
                            
                            self.list_widgets_options[index][9]=self.ent_imagebefore.get()+"Error"
                    else:
                        self.list_widgets_options[index][9]=None
                        if not self.list_widgets_canvas[index].winfo_class()=="Canvas":
                            self.list_widgets_canvas[index].config(image="")
                        
                else:
                    self.list_widgets_options[index][9]=""
                if self.list_widgets_canvas[index].winfo_class()=="Button":
                    if self.ent_imageafter.get()!="None" and self.ent_imageafter.get()!="":
                        s=0
                        try:
                            img=PhotoImage(file=self.ent_imageafter.get())
                            s=1
                        except:
                            pass
                        
                        if s==1:
                            self.list_widgets_options[index][10]=self.ent_imageafter.get()
                        else:
                            self.list_widgets_options[index][10]=self.ent_imageafter.get()+"Error"
                    else:
                        self.list_widgets_options[index][10]=None
                    if self.ent_command.get()!="None" and self.ent_command.get()!="":
                        self.list_widgets_options[index][11]=self.ent_command.get()
                    else:
                        self.list_widgets_options[index][11]=None
                else:
                    self.list_widgets_options[index][10]=""
                    self.list_widgets_options[index][11]=""
                self.list_draggedwidgets.delete(index)
                self.list_draggedwidgets.insert(index,self.list_widgets_options[index][0])
                self.n_errors=0
                if self.list_widgets_canvas[index].winfo_class()=="Button" or self.list_widgets_canvas[index].winfo_class()=="Radiobutton" or self.list_widgets_canvas[index].winfo_class()=="Checkbutton":
                    if self.var_activebackground.get()!="" and self.var_activebackground.get()!="None":
                        s=0
                        try:
                            self.list_widgets_canvas[index].config(activebackground=self.var_activebackground.get())
                            s=1
                        except:
                            pass
                        if s==1:
                            self.list_widgets_options[index][14]=self.var_activebackground.get()
                        else:
                            self.list_widgets_options[index][14]=self.var_activebackground.get()+"Error"
                    else:
                        self.list_widgets_options[index][14]=None
                    if self.var_activeforeground.get()!="" and self.var_activeforeground.get()!="None":
                        s=0
                        try:
                            self.list_widgets_canvas[index].config(activeforeground=self.var_activeforeground.get())
                            s=1
                        except:
                            pass
                        if s==1:
                            self.list_widgets_options[index][15]=self.var_activeforeground.get()
                        else:
                            self.list_widgets_options[index][15]=self.var_activeforeground.get()+"Error"
                    else:
                        self.list_widgets_options[index][15]=None
                else:
                    self.list_widgets_options[index][14]=""
                    self.list_widgets_options[index][15]=""
                if self.list_widgets_canvas[index].winfo_class()=="Button":
                    if self.var_mouseenterbackground.get()!="" and self.var_mouseenterbackground.get()!="None":
                        s=0
                        try:
                            bt=Button(self,bg=self.var_mouseenterbackground.get())
                            s=1
                        except:
                            pass
                        if s==1:
                            self.list_widgets_options[index][16]=self.var_mouseenterbackground.get()
                        else:
                            self.list_widgets_options[index][16]=self.var_mouseenterbackground.get()+"Error"
                    else:
                        self.list_widgets_options[index][16]=None
                    if self.var_mouseleavebackground.get()!="" and self.var_mouseleavebackground.get()!="None":
                        s=0
                        try:
                            bt=Button(self,bg=self.var_mouseleavebackground.get())
                            s=1
                        except:
                            pass
                        if s==1:
                            self.list_widgets_options[index][17]=self.var_mouseleavebackground.get()
                        else:
                            self.list_widgets_options[index][17]=self.var_mouseleavebackground.get()+"Error"
                    else:
                        self.list_widgets_options[index][17]=None
                    if self.var_mouseenterforeground.get()!="" and self.var_mouseenterforeground.get()!="None":
                        s=0
                        try:
                            bt=Button(self,bg=self.var_mouseenterforeground.get())
                            s=1
                        except:
                            pass
                        if s==1:
                            self.list_widgets_options[index][18]=self.var_mouseenterforeground.get()
                        else:
                            self.list_widgets_options[index][18]=self.var_mouseenterforeground.get()+"Error"
                    else:
                        self.list_widgets_options[index][18]=None
                    if self.var_mouseleaveforeground.get()!="" and self.var_mouseleaveforeground.get()!="None":
                        s=0
                        try:
                            bt=Button(self,bg=self.var_mouseleaveforeground.get())
                            s=1
                        except:
                            pass
                        if s==1:
                            self.list_widgets_options[index][19]=self.var_mouseleaveforeground.get()
                        else:
                            self.list_widgets_options[index][19]=self.var_mouseleaveforeground.get()+"Error"
                    else:
                        self.list_widgets_options[index][19]=None
                else:
                    self.list_widgets_options[index][16]=""
                    self.list_widgets_options[index][17]=""
                    self.list_widgets_options[index][18]=""
                    self.list_widgets_options[index][19]=""
                for option in self.list_widgets_options[index]:
                    if "Error" in str(option):
                        self.list_draggedwidgets.itemconfigure(index,fg="red")
                        break
                for options in self.list_widgets_options:
                    for option in options:
                        if "Error" in str(option):
                            self.n_errors+=1
                if self.n_errors!=0:
                    self.lbl_errors.config(text=str(self.n_errors),fg="red")
                else:
                    self.lbl_errors.config(text="0",fg="green")
            ####################################################### win properties
            if int(self.var_win_width.get()) in range(50,1401) and int(self.var_win_height.get()) in range(1,901):
                try:
                    #1610 ,50
                    
                    
                    # self.lbl_properties=Label(self,text="Properties",font=("arial",16))
                    # self.lbl_properties.place(x=1610,y=80)
                    # self.list_properties=Listbox(self,bd=0,highlightbackground="gray",highlightcolor="#13c2dc")
                    # self.list_properties.place(x=1610,y=110,width=300,height=610)
                    # self.lbl_id=Label(self,text="id:",fg="#13c2dc",font=("arial",14),bg="white")
                    # self.lbl_id.place(x=1615,y=115)
                    # self.lbl_posx=Label(self,text="position-x:",fg="#13c2dc",font=("arial",14),bg="white")
                    # self.lbl_posx.place(x=1615,y=145)
                    # self.lbl_posy=Label(self,text="position-y:",fg="#13c2dc",font=("arial",14),bg="white")
                    # self.lbl_posy.place(x=1615,y=175)
                    # self.lbl_width=Label(self,text="width:",fg="#13c2dc",font=("arial",14),bg="white")
                    # self.lbl_width.place(x=1615,y=205)
                    # self.lbl_height=Label(self,text="height:",fg="#13c2dc",font=("arial",14),bg="white")
                    # self.lbl_height.place(x=1615,y=235)
                    # self.lbl_text=Label(self,text="text:",fg="#13c2dc",font=("arial",14),bg="white")
                    # self.lbl_text.place(x=1615,y=265)
                    # self.lbl_bg=Label(self,text="bg:",fg="#13c2dc",font=("arial",14),bg="white")
                    # self.lbl_bg.place(x=1615,y=295)
                    # self.lbl_fg=Label(self,text="fg:",fg="#13c2dc",font=("arial",14),bg="white")
                    # self.lbl_fg.place(x=1615,y=325)
                    # self.lbl_font=Label(self,text="font:",fg="#13c2dc",font=("arial",14),bg="white")
                    # self.lbl_font.place(x=1615,y=355)
                    # self.lbl_imagebefore=Label(self,text="image before:",fg="#13c2dc",font=("arial",14),bg="white")
                    # self.lbl_imagebefore.place(x=1615,y=385)
                    # self.lbl_imageafter=Label(self,text="image after:",fg="#13c2dc",font=("arial",14),bg="white")
                    # self.lbl_imageafter.place(x=1615,y=415)
                    # self.lbl_command=Label(self,text="command:",fg="#13c2dc",font=("arial",14),bg="white")
                    # self.lbl_command.place(x=1615,y=445)
                    # self.lbl_highlightcolor=Label(self,text="highlightcolor:",fg="#13c2dc",font=("arial",14),bg="white")
                    # self.lbl_highlightcolor.place(x=1615,y=475)
                    # self.lbl_highlightbackground=Label(self,text="highlightbackground:",fg="#13c2dc",font=("arial",14),bg="white")
                    # self.lbl_highlightbackground.place(x=1615,y=505)
                    # self.lbl_activebackground=Label(self,text="activebackground:",fg="#13c2dc",font=("arial",14),bg="white")
                    # self.lbl_activebackground.place(x=1615,y=535)
                    # self.lbl_activeforeground=Label(self,text="activeforeground:",fg="#13c2dc",font=("arial",14),bg="white")
                    # self.lbl_activeforeground.place(x=1615,y=565)
                    # self.lbl_mouseenterbackground=Label(self,text="mouseenterbackground:",fg="#13c2dc",font=("arial",14),bg="white")
                    # self.lbl_mouseenterbackground.place(x=1615,y=595)
                    # self.lbl_mouseleavebackground=Label(self,text="mouseleavebackground:",fg="#13c2dc",font=("arial",14),bg="white")
                    # self.lbl_mouseleavebackground.place(x=1615,y=625)
                    # self.lbl_mouseenterforeground=Label(self,text="mouseenterforeground:",fg="#13c2dc",font=("arial",14),bg="white")
                    # self.lbl_mouseenterforeground.place(x=1615,y=655)
                    # self.lbl_mouseleaveforeground=Label(self,text="mouseleaveforeground:",fg="#13c2dc",font=("arial",14),bg="white")
                    # self.lbl_mouseleaveforeground.place(x=1615,y=685)
                    
                    # self.ent_id=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_id,relief="flat",highlightthickness=1)
                    # self.ent_id.place(x=1745,y=120,width=155)
                    # self.ent_posx=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_posx,relief="flat",highlightthickness=1)
                    # self.ent_posx.place(x=1745,y=150,width=155)
                    # self.ent_posy=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_posy,relief="flat",highlightthickness=1)
                    # self.ent_posy.place(x=1745,y=180,width=155)
                    # self.ent_width=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_width,relief="flat",highlightthickness=1)
                    # self.ent_width.place(x=1745,y=210,width=155)
                    # self.ent_height=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_height,relief="flat",highlightthickness=1)
                    # self.ent_height.place(x=1745,y=240,width=155)
                    # self.ent_text=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_text,relief="flat",highlightthickness=1)
                    # self.ent_text.place(x=1745,y=270,width=155)
                    # self.ent_bg=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_bg,relief="flat",highlightthickness=1)
                    # self.ent_bg.place(x=1745,y=300,width=155)
                    # self.ent_fg=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_fg,relief="flat",highlightthickness=1)
                    # self.ent_fg.place(x=1745,y=330,width=155)
                    # self.ent_font=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_font,relief="flat",highlightthickness=1)
                    # self.ent_font.place(x=1745,y=360,width=155)
                    # self.ent_imagebefore=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_imagebefore,relief="flat",highlightthickness=1)
                    # self.ent_imagebefore.place(x=1745,y=390,width=130)
                    # self.ent_imageafter=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_imageafter,relief="flat",highlightthickness=1)
                    # self.ent_imageafter.place(x=1745,y=420,width=130)
                    # self.ent_command=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_command,relief="flat",highlightthickness=1)
                    # self.ent_command.place(x=1745,y=450,width=155)
                    # self.ent_highlightcolor=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_highlightcolor,relief="flat",highlightthickness=1)
                    # self.ent_highlightcolor.place(x=1745,y=480,width=155)
                    # self.ent_highlightbackground=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_highlightbackground,relief="flat",highlightthickness=1)
                    # self.ent_highlightbackground.place(x=1800,y=510,width=100)
                    # self.ent_activebackground=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_activebackground,relief="flat",highlightthickness=1)
                    # self.ent_activebackground.place(x=1800,y=540,width=100)
                    # self.ent_activeforeground=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_activeforeground,relief="flat",highlightthickness=1)
                    # self.ent_activeforeground.place(x=1800,y=570,width=100)
                    
                    # self.ent_mouseenterbackground=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_mouseenterbackground,relief="flat",highlightthickness=1)
                    # self.ent_mouseenterbackground.place(x=1830,y=600,width=70)
                    # self.ent_mouseleavebackground=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_mouseleavebackground,relief="flat",highlightthickness=1)
                    # self.ent_mouseleavebackground.place(x=1830,y=630,width=70)
                    # self.ent_mouseenterforeground=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_mouseenterforeground,relief="flat",highlightthickness=1)
                    # self.ent_mouseenterforeground.place(x=1830,y=660,width=70)
                    # self.ent_mouseleaveforeground=Entry(self,highlightbackground="gray",highlightcolor="#13c2dc",bg="#e1e1e1",textvariable=self.var_mouseleaveforeground,relief="flat",highlightthickness=1)
                    # self.ent_mouseleaveforeground.place(x=1830,y=690,width=70)
                    
                    # self.bt_browse_imagebefore=Button(self,text="...",relief="flat",fg="gray",activeforeground="#13c2dc",bd=0,command=self.browse_imagebefore)
                    # self.bt_browse_imagebefore.place(x=1883,y=390)
                    # self.bt_browse_imageafter=Button(self,text="...",relief="flat",fg="gray",activeforeground="#13c2dc",bd=0,command=self.browse_imageafter)
                    # self.bt_browse_imageafter.place(x=1883,y=420)
                    # self.lbl_errors.place(x=1830,y=20)
                    # self.lbl_errors_image.place(x=1860,y=15)
                    
                    
                    self.pos_list_properties-=(int(self.list_win_options[0])-int(self.var_win_width.get()))
                    self.pos_lbls-=(int(self.list_win_options[0])-int(self.var_win_width.get()))
                    self.pos_ents1-=(int(self.list_win_options[0])-int(self.var_win_width.get()))
                    self.pos_ents2-=(int(self.list_win_options[0])-int(self.var_win_width.get()))
                    self.pos_ents3-=(int(self.list_win_options[0])-int(self.var_win_width.get()))
                    self.pos_bts-=(int(self.list_win_options[0])-int(self.var_win_width.get()))
                    self.pos_lbl_errors-=(int(self.list_win_options[0])-int(self.var_win_width.get()))
                    self.pos_lbl_errors_image-=(int(self.list_win_options[0])-int(self.var_win_width.get()))
                    if int(self.var_win_height.get()) >=500 and int(self.list_win_options[1])-int(self.pos_list_draggedwidgets)==380:
                        self.pos_list_draggedwidgets-=(int(self.list_win_options[1])-int(self.var_win_height.get()))
                        self.list_draggedwidgets.place_configure(height=self.pos_list_draggedwidgets)
                    self.canvas.place_configure(width=int(self.var_win_width.get()),height=int(self.var_win_height.get()))
                    
                    self.lbl_errors.place_configure(x=self.pos_lbl_errors,y=10)
                    self.lbl_errors_image.place_configure(x=self.pos_lbl_errors_image,y=5)
                    
                    self.list_properties.place_configure(x=self.pos_list_properties,y=110)
                    self.lbl_properties.place_configure(x=self.pos_list_properties,y=80)
                    self.lbl_id.place_configure(x=self.pos_lbls,y=115)
                    self.lbl_posx.place_configure(x=self.pos_lbls,y=145)
                    self.lbl_posy.place_configure(x=self.pos_lbls,y=175)
                    self.lbl_width.place_configure(x=self.pos_lbls,y=205)
                    self.lbl_height.place_configure(x=self.pos_lbls,y=235)
                    self.lbl_text.place_configure(x=self.pos_lbls,y=265)
                    self.lbl_bg.place_configure(x=self.pos_lbls,y=295)
                    self.lbl_fg.place_configure(x=self.pos_lbls,y=325)
                    self.lbl_font.place_configure(x=self.pos_lbls,y=355)
                    self.lbl_imagebefore.place_configure(x=self.pos_lbls,y=385)
                    self.lbl_imageafter.place_configure(x=self.pos_lbls,y=415)
                    self.lbl_command.place_configure(x=self.pos_lbls,y=445)
                    self.lbl_highlightcolor.place_configure(x=self.pos_lbls,y=475)
                    self.lbl_highlightbackground.place_configure(x=self.pos_lbls,y=505)
                    self.lbl_activebackground.place_configure(x=self.pos_lbls,y=535)
                    self.lbl_activeforeground.place_configure(x=self.pos_lbls,y=565)
                    self.lbl_mouseenterbackground.place_configure(x=self.pos_lbls,y=595)
                    self.lbl_mouseleavebackground.place_configure(x=self.pos_lbls,y=625)
                    self.lbl_mouseenterforeground.place_configure(x=self.pos_lbls,y=655)
                    self.lbl_mouseleaveforeground.place_configure(x=self.pos_lbls,y=685)
                    
                    self.ent_id.place_configure(x=self.pos_ents1,y=120,width=155)
                    self.ent_posx.place_configure(x=self.pos_ents1,y=150,width=155)
                    self.ent_posy.place_configure(x=self.pos_ents1,y=180,width=155)
                    self.ent_width.place_configure(x=self.pos_ents1,y=210,width=155)
                    self.ent_height.place_configure(x=self.pos_ents1,y=240,width=155)
                    self.ent_text.place_configure(x=self.pos_ents1,y=270,width=155)
                    self.ent_bg.place_configure(x=self.pos_ents1,y=300,width=155)
                    self.ent_fg.place_configure(x=self.pos_ents1,y=330,width=155)
                    self.ent_font.place_configure(x=self.pos_ents1,y=360,width=155)
                    self.ent_imagebefore.place_configure(x=self.pos_ents1,y=390,width=130)
                    self.ent_imageafter.place_configure(x=self.pos_ents1,y=420,width=130)
                    self.ent_command.place_configure(x=self.pos_ents1,y=450,width=155)
                    self.ent_highlightcolor.place_configure(x=self.pos_ents1,y=480,width=155)
                    self.ent_highlightbackground.place_configure(x=self.pos_ents2,y=510,width=100)
                    self.ent_activebackground.place_configure(x=self.pos_ents2,y=540,width=100)
                    self.ent_activeforeground.place_configure(x=self.pos_ents2,y=570,width=100)
                    self.ent_mouseenterbackground.place_configure(x=self.pos_ents3,y=600,width=70)
                    self.ent_mouseleavebackground.place_configure(x=self.pos_ents3,y=630,width=70)
                    self.ent_mouseenterforeground.place_configure(x=self.pos_ents3,y=660,width=70)
                    self.ent_mouseleaveforeground.place_configure(x=self.pos_ents3,y=690,width=70)
                    
                    self.bt_browse_imagebefore.place_configure(x=self.pos_bts,y=390)
                    self.bt_browse_imageafter.place_configure(x=self.pos_bts,y=420)
                    
                    self.list_draggedwidgets.place_configure(height=self.pos_list_draggedwidgets)
                    self.list_win_options[0]=self.var_win_width.get()
                    self.list_win_options[1]=self.var_win_height.get()
                    
                except:
                    self.var_win_width.set(self.list_win_options[0])
                    self.var_win_height.set(self.list_win_options[1])
            else:
                self.var_win_width.set(self.list_win_options[0])
                self.var_win_height.set(self.list_win_options[1])
            try:
                self.canvas.config(bg=self.var_win_bg.get())
                self.list_win_options[2]=self.var_win_bg.get()
            except:
                self.var_win_bg.set(self.list_win_options[2])
            if self.var_win_overrideredirect.get()=="0" or self.var_win_overrideredirect.get()=="1":
                self.list_win_options[3]=self.var_win_overrideredirect.get()
            else:
                self.var_win_overrideredirect.set(self.list_win_options[3])
            if self.var_win_top.get()=="0" or self.var_win_top.get()=="1":
                self.list_win_options[4]=self.var_win_top.get()
            else:
                self.var_win_top.set(self.list_win_options[4])
            if self.var_win_posx.get()=="center" or self.var_win_posx.get().isnumeric():
                self.list_win_options[5]=self.var_win_posx.get()
            else:
                self.var_win_posx.set(self.list_win_options[5])
            if self.var_win_posy.get()=="center" or self.var_win_posy.get().isnumeric():
                self.list_win_options[6]=self.var_win_posy.get()
            else:
                self.var_win_posy.set(self.list_win_options[6])
            self.list_win_options[7]=self.var_win_mode.get()
        except:
            pass
       
    def insert_widget(self,mode):
        try:
            if mode=="button":
                self.n_button+=1
                self.list_widgets_canvas.append(Button(self.canvas,text="button"+str(self.n_button),relief="flat",bd=0,font=("arial",10)))
                self.list_widgets_canvas[-1].place(x=10,y=10,width=50,height=20)
                self.list_draggedwidgets.insert(END,"button"+str(self.n_button))
                self.list_widgets_canvas[-1].bind("<Enter>",self.button_enter)
                self.list_widgets_canvas[-1].bind("<Leave>",self.button_leave)
                
                options=["button"+str(self.n_button),10,10,50,20,"button"+str(self.n_button),None,None,10,None,None,None,None,None,None,None,None,None,None,None]
                self.list_widgets_options.append(options)
                
            elif mode=="label":
                self.n_label+=1
                self.list_widgets_canvas.append(Label(self.canvas,text="label"+str(self.n_label),relief="flat",bd=0,font=("arial",10)))
                self.list_widgets_canvas[-1].place(x=10,y=10,width=50,height=20)
                self.list_draggedwidgets.insert(END,"label"+str(self.n_label))
                options=["label"+str(self.n_label),10,10,50,20,"label"+str(self.n_label),None,None,10,None,"","",None,None,"","","","","",""]
                self.list_widgets_options.append(options)
                
            elif mode=="entry":
                self.n_entry+=1
                self.list_widgets_canvas.append(Entry(self.canvas,relief="flat",font=("arial",10),bg="gray",highlightthickness=1))
                self.list_widgets_canvas[-1].place(x=10,y=10,width=150,height=22)
                self.list_draggedwidgets.insert(END,"entry"+str(self.n_entry))
                options=["entry"+str(self.n_entry),10,10,150,22,"","gray",None,10,"","","",None,None,"","","","","",""]
                self.list_widgets_options.append(options)
                
            elif mode=="listbox":
                self.n_listbox+=1
                self.list_widgets_canvas.append(Listbox(self.canvas,relief="flat",font=("arial",10),bd=0,highlightbackground="gray"))
                self.list_widgets_canvas[-1].place(x=10,y=10,width=200,height=300)
                self.list_draggedwidgets.insert(END,"listbox"+str(self.n_listbox))
                options=["listbox"+str(self.n_listbox),10,10,200,300,"",None,None,10,"","","",None,"gray","","","","","",""]
                self.list_widgets_options.append(options)
                
            elif mode=="radiobutton":
                self.n_radiobutton+=1
                self.list_widgets_canvas.append(Radiobutton(self.canvas,text="radiobutton"+str(self.n_radiobutton),relief="flat",bd=0,font=("arial",10)))
                self.list_widgets_canvas[-1].place(x=10,y=10,width=100,height=22)
                self.list_draggedwidgets.insert(END,"radiobutton"+str(self.n_radiobutton))
                options=["radiobutton"+str(self.n_radiobutton),10,10,100,22,"radiobutton"+str(self.n_radiobutton),None,None,10,"","","",None,None,None,None,"","","",""]
                self.list_widgets_options.append(options)
                
            elif mode=="checkbutton":
                self.n_checkbutton+=1
                self.list_widgets_canvas.append(Checkbutton(self.canvas,text="checkbutton"+str(self.n_checkbutton),relief="flat",bd=0,font=("arial",10)))
                self.list_widgets_canvas[-1].place(x=10,y=10,width=100,height=22)
                self.list_draggedwidgets.insert(END,"checkbutton"+str(self.n_checkbutton))
                options=["checkbutton"+str(self.n_checkbutton),10,10,100,22,"checkbutton"+str(self.n_checkbutton),None,None,10,"","","",None,None,None,None,"","","",""]
                self.list_widgets_options.append(options)
                
            elif mode=="canvas":
                self.n_canvas+=1
                self.list_widgets_canvas.append(Canvas(self.canvas,relief="flat",bd=0))
                self.list_widgets_canvas[-1].place(x=10,y=10,width=300,height=200)
                self.list_draggedwidgets.insert(END,"canvas"+str(self.n_canvas))
                options=["canvas"+str(self.n_canvas),10,10,300,200,"",None,"","",None,"","",None,None,"","","","","",""]
                self.list_widgets_options.append(options)
            self.list_widgets_canvas[-1].bind("<B1-Motion>",self.moving)
            try:
                self.list_draggedwidgets.selection_clear(len(self.list_widgets_canvas)-2)
            except:
                pass
            self.list_draggedwidgets.selection_set(len(self.list_widgets_canvas)-1)
            self.click_com()
        except:
            pass
    def click_com(self,e=None):
        try:
            value=self.list_draggedwidgets.curselection()
            if value!=():
                index=value[0]
                self.last_selected=index
                self.var_id.set(self.list_widgets_options[index][0])
                self.var_posx.set(str(int(self.list_widgets_options[index][1])))
                self.var_posy.set(str(int(self.list_widgets_options[index][2])))
                self.var_width.set(self.list_widgets_options[index][3])
                self.var_height.set(self.list_widgets_options[index][4])
                if "Error" in str(self.list_widgets_options[index][5]):
                    self.ent_text.config(fg="red",highlightbackground="red")
                    
                    self.var_text.set(self.list_widgets_options[index][5].replace("Error",""))
                else:
                    self.ent_text.config(fg="black",highlightbackground="gray")
                    self.var_text.set(self.list_widgets_options[index][5])
                if "Error" in str(self.list_widgets_options[index][6]):
                    self.ent_bg.config(fg="red",highlightbackground="red")
                    self.var_bg.set(self.list_widgets_options[index][6].replace("Error",""))
                else:
                    self.ent_bg.config(fg="black",highlightbackground="gray")
                    self.var_bg.set(self.list_widgets_options[index][6])
                if "Error" in str(self.list_widgets_options[index][7]):
                    self.ent_fg.config(fg="red",highlightbackground="red")
                    self.var_fg.set(self.list_widgets_options[index][7].replace("Error",""))
                else:
                    self.ent_fg.config(fg="black",highlightbackground="gray")
                    self.var_fg.set(self.list_widgets_options[index][7])
                if "Error" in str(self.list_widgets_options[index][8]):
                    self.ent_font.config(fg="red",highlightbackground="red")
                    self.var_font.set(self.list_widgets_options[index][8].replace("Error",""))
                else:
                    self.ent_font.config(fg="black",highlightbackground="gray")
                    self.var_font.set(self.list_widgets_options[index][8])
                if "Error" in str(self.list_widgets_options[index][9]):
                    self.ent_imagebefore.config(fg="red",highlightbackground="red")
                    self.var_imagebefore.set(self.list_widgets_options[index][9].replace("Error",""))
                else:
                    self.ent_imagebefore.config(fg="black",highlightbackground="gray")
                    self.var_imagebefore.set(self.list_widgets_options[index][9])
                if "Error" in str(self.list_widgets_options[index][10]):
                    self.ent_imageafter.config(fg="red",highlightbackground="red")
                    self.var_imageafter.set(self.list_widgets_options[index][10].replace("Error",""))
                else:
                    self.ent_imageafter.config(fg="black",highlightbackground="gray")
                    self.var_imageafter.set(self.list_widgets_options[index][10])
                if "Error" in str(self.list_widgets_options[index][11]):
                    self.ent_command.config(fg="red",highlightbackground="red")
                    self.var_command.set(self.list_widgets_options[index][11].replace("Error",""))
                else:
                    self.ent_command.config(fg="black",highlightbackground="gray")
                    self.var_command.set(self.list_widgets_options[index][11])
                if "Error" in str(self.list_widgets_options[index][12]):
                    self.ent_highlightcolor.config(fg="red",highlightbackground="red")
                    self.var_highlightcolor.set(self.list_widgets_options[index][12].replace("Error",""))
                else:
                    self.ent_highlightcolor.config(fg="black",highlightbackground="gray")
                    self.var_highlightcolor.set(self.list_widgets_options[index][12])
                if "Error" in str(self.list_widgets_options[index][13]):
                    self.ent_highlightbackground.config(fg="red",highlightbackground="red")
                    self.var_highlightbackground.set(self.list_widgets_options[index][13].replace("Error",""))
                else:
                    self.ent_highlightbackground.config(fg="black",highlightbackground="gray")
                    self.var_highlightbackground.set(self.list_widgets_options[index][13])
                if "Error" in str(self.list_widgets_options[index][14]):
                    self.ent_activebackground.config(fg="red",highlightbackground="red")
                    self.var_activebackground.set(self.list_widgets_options[index][14].replace("Error",""))
                else:
                    self.ent_activebackground.config(fg="black",highlightbackground="gray")
                    self.var_activebackground.set(self.list_widgets_options[index][14])
                if "Error" in str(self.list_widgets_options[index][15]):
                    self.ent_activeforeground.config(fg="red",highlightbackground="red")
                    self.var_activeforeground.set(self.list_widgets_options[index][15].replace("Error",""))
                else:
                    self.ent_activeforeground.config(fg="black",highlightbackground="gray")
                    self.var_activeforeground.set(self.list_widgets_options[index][15])
                
                if "Error" in str(self.list_widgets_options[index][16]):
                    self.ent_mouseenterbackground.config(fg="red",highlightbackground="red")
                    self.var_mouseenterbackground.set(self.list_widgets_options[index][16].replace("Error",""))
                else:
                    self.ent_mouseenterbackground.config(fg="black",highlightbackground="gray")
                    self.var_mouseenterbackground.set(self.list_widgets_options[index][16])
                if "Error" in str(self.list_widgets_options[index][17]):
                    self.ent_mouseleavebackground.config(fg="red",highlightbackground="red")
                    self.var_mouseleavebackground.set(self.list_widgets_options[index][17].replace("Error",""))
                else:
                    self.ent_mouseleavebackground.config(fg="black",highlightbackground="gray")
                    self.var_mouseleavebackground.set(self.list_widgets_options[index][17])
                if "Error" in str(self.list_widgets_options[index][18]):
                    self.ent_mouseenterforeground.config(fg="red",highlightbackground="red")
                    self.var_mouseenterforeground.set(self.list_widgets_options[index][18].replace("Error",""))
                else:
                    self.ent_mouseenterforeground.config(fg="black",highlightbackground="gray")
                    self.var_mouseenterforeground.set(self.list_widgets_options[index][18])
                if "Error" in str(self.list_widgets_options[index][19]):
                    self.ent_mouseleaveforeground.config(fg="red",highlightbackground="red")
                    self.var_mouseleaveforeground.set(self.list_widgets_options[index][19].replace("Error",""))
                else:
                    self.ent_mouseleaveforeground.config(fg="black",highlightbackground="gray")
                    self.var_mouseleaveforeground.set(self.list_widgets_options[index][19])
        except:
            pass
    def browse_imagebefore(self):
        image_path=filedialog.askopenfilename()
        self.var_imagebefore.set(image_path)
    def browse_imageafter(self):
        image_path=filedialog.askopenfilename()
        self.var_imageafter.set(image_path)
    def button_enter(self,e):
        pass
    def button_leave(self,e):
        pass
    def moving(self,e):
        try:
            value=self.list_draggedwidgets.curselection()
            if value!=():
                index=value[0]
                self.list_widgets_canvas[index].place_configure(x=e.x_root-230,y=e.y_root-111)
                self.var_posx.set(e.x_root-230)
                self.var_posy.set(e.y_root-111)
                self.list_widgets_options[index][1]=e.x_root-230
                self.list_widgets_options[index][2]=e.y_root-111
        except:
            pass
            
    def delete_widget(self,e):
        try:
            value=self.list_draggedwidgets.curselection()
            if value!=():
                index=value[0]
                self.list_draggedwidgets.delete(index)
                self.list_widgets_canvas[index].place_forget()
                self.list_widgets_canvas.pop(index)
                self.list_widgets_options.pop(index)
        except:
            pass
            
    def mouse_moving(self,e):
        self.lbl_mouse_pos.config(text="pos-x:"+str(e.x)+", pos-y:"+str(e.y))
    def bt_save_enter(self,e):
        self.bt_save.config(image=self.image_save_after)
    def bt_save_leave(self,e):
        self.bt_save.config(image=self.image_save_before)
    def bt_save_com(self,e=None):
        try:
            file_path=""
            if self.path_file.get()=="":
                file_path=filedialog.asksaveasfilename(defaultextension=".UIELPRINCE")
            else:
                file_path=self.path_file.get()
            if file_path!="":
                with open(file_path,"w") as f1:
                    f1.write(repr(self.list_win_options)+"\n")
                    f1.write(repr(self.list_widgets_options)+"\n")
                list_types=[]
                for widget in self.list_widgets_canvas:
                    list_types.append(widget.winfo_class())
                with open(file_path,"a") as f1:
                    f1.write(repr(list_types)+"\n")
                    f1.write(str(self.n_button)+"\n")
                    f1.write(str(self.n_label)+"\n")
                    f1.write(str(self.n_entry)+"\n")
                    f1.write(str(self.n_listbox)+"\n")
                    f1.write(str(self.n_radiobutton)+"\n")
                    f1.write(str(self.n_checkbutton)+"\n")
                    f1.write(str(self.n_canvas))
            if self.path_file.get()=="" and file_path!="":
                msgbox=messagebox.showinfo("Saved!","Done!")
            self.path_file.set(file_path)
        except:
            pass
    def bt_new_com(self,e):
        try:
            self.choice=True
            if self.path_file.get()=="":
               self.choice= msgbox=messagebox.askyesnocancel("Warnning","This file will be lost! Are you sure?")
            else:
                self.bt_save_com(None)
            if self.choice==True:
                self.n_button=0
                self.n_label=0
                self.n_entry=0
                self.n_listbox=0
                self.n_radiobutton=0
                self.n_checkbutton=0
                self.n_canvas=0
                for widget in self.list_widgets_canvas:
                    widget.place_forget()
                self.list_draggedwidgets.delete(0,END)
                self.path_file.set("")
                self.list_widgets_canvas=[]
                self.list_widgets_options=[]
                self.list_win_options=[self.list_win_options[0],self.list_win_options[1],"white","0","0","center","center","self"]
                self.canvas.place_configure(width=1400,height=900)
                self.canvas.config(bg="white")
                self.var_win_width.set("1400")
                self.var_win_height.set("900")
                self.var_win_bg.set("white")
                self.var_win_overrideredirect.set("0")
                self.var_win_top.set("0")
                self.var_win_posx.set("center")
                self.var_win_posy.set("center")
                self.var_win_mode.set("center")
                self.images=[]
                self.last_selected=None
                self.n_errors=0
                self.apply_com(None)
                self.ent_id.delete(0,END)
                self.ent_posx.delete(0,END)
                self.ent_posy.delete(0,END)
                self.ent_width.delete(0,END)
                self.ent_height.delete(0,END)
                self.ent_text.delete(0,END)
                self.ent_bg.delete(0,END)
                self.ent_fg.delete(0,END)
                self.ent_font.delete(0,END)
                self.ent_imagebefore.delete(0,END)
                self.ent_imageafter.delete(0,END)
                self.ent_command.delete(0,END)
                self.ent_highlightcolor.delete(0,END)
                self.ent_highlightbackground.delete(0,END)
                self.ent_activebackground.delete(0,END)
                self.ent_activeforeground.delete(0,END)
                self.ent_mouseenterbackground.delete(0,END)
                self.ent_mouseleavebackground.delete(0,END)
                self.ent_mouseenterforeground.delete(0,END)
                self.ent_mouseleaveforeground.delete(0,END)
        except:
            pass
    def bt_open_enter(self,e):
        self.bt_open.config(image=self.image_open_after)
    def bt_open_leave(self,e):
        self.bt_open.config(image=self.image_open_before)
    def bt_open_com(self):
        try:
            file_path=filedialog.askopenfilename()
            if file_path!="":
                self.bt_new_com(None)
                if self.choice==True:
                    self.path_file.set(file_path)
                    list=""
                    with open(file_path,"r") as f1:
                        list=f1.read()
                    list=list.splitlines()
                    
                    self.list_widgets_options=literal_eval(list[1])
                    list_types=literal_eval(list[2])
                    # print(self.list_win_options)
                    # print(self.list_widgets_options)
                    # print(list_types)
                    for option in self.list_widgets_options:
                        self.list_draggedwidgets.insert(END,option[0])
                    
                    self.n_button=int(list[3])
                    self.n_label=int(list[4])
                    self.n_entry=int(list[5])
                    self.n_listbox=int(list[6])
                    self.n_radiobutton=int(list[7])
                    self.n_checkbutton=int(list[8])
                    self.n_canvas=int(list[9])
                    a=literal_eval(list[0])
                    self.var_win_width.set(a[0])
                    self.var_win_height.set(a[1])
                    self.var_win_bg.set(a[2])
                    self.var_win_overrideredirect.set(a[3])
                    self.var_win_top.set(a[4])
                    self.var_win_posx.set(a[5])
                    self.var_win_posy.set(a[6])
                    self.var_win_mode.set(a[7])
                    self.canvas.place(x=200,y=80,width=int(self.var_win_width.get()),height=int(self.var_win_height.get()))
                    self.apply_com(None)
                    self.list_win_options=literal_eval(list[0])
                    index=0
                    for widget_type in list_types:
                        if widget_type=="Button":
                            self.list_widgets_canvas.append(Button(self.canvas,text="button"+str(self.n_button),relief="flat",bd=0,font=("arial",10)))
                            
                            try:                                           ## text
                                self.list_widgets_canvas[-1].config(text=self.list_widgets_options[index][5])
                            except:
                                self.list_widgets_options[index][5]=self.list_widgets_options[index][5]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                            
                            try:                                           ## bg
                                self.list_widgets_canvas[-1].config(bg=self.list_widgets_options[index][6])
                            except:
                                self.list_widgets_options[index][6]=self.list_widgets_options[index][6]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                            
                            try:                                           ## fg
                                self.list_widgets_canvas[-1].config(fg=self.list_widgets_options[index][7])
                            except:
                                self.list_widgets_options[index][7]=self.list_widgets_options[index][7]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                            try:                                           ## font
                                self.list_widgets_canvas[-1].config(font=("arial",int(self.list_widgets_options[index][8])))
                            except:
                                self.list_widgets_options[index][8]=self.list_widgets_options[index][8]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                            try:                                           ## image before
                                if self.list_widgets_options[index][9]==None:
                                    pass
                                else:
                                    self.images.append(PhotoImage(file=self.list_widgets_options[index][9]))
                                    self.list_widgets_canvas[-1].config(image=self.images[-1])
                            except:
                                self.list_widgets_options[index][9]=self.list_widgets_options[index][9]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                            try:                                           ## activebackground
                                self.list_widgets_canvas[-1].config(activebackground=self.list_widgets_options[index][14])
                            except:
                                self.list_widgets_options[index][14]=self.list_widgets_options[index][14]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                            try:                                           ## activeforeground
                                self.list_widgets_canvas[-1].config(activeforeground=self.list_widgets_options[index][15])
                            except:
                                self.list_widgets_options[index][15]=self.list_widgets_options[index][15]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                            
                                
                        elif widget_type=="Label":
                            self.list_widgets_canvas.append(Label(self.canvas,text="label"+str(self.n_label),relief="flat",bd=0,font=("arial",10)))
                            try:                                           ## text
                                self.list_widgets_canvas[-1].config(text=self.list_widgets_options[index][5])
                            except:
                                self.list_widgets_options[index][5]=self.list_widgets_options[index][5]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                            
                            try:                                           ## bg
                                self.list_widgets_canvas[-1].config(bg=self.list_widgets_options[index][6])
                            except:
                                self.list_widgets_options[index][6]=self.list_widgets_options[index][6]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                            
                            try:                                           ## fg
                                self.list_widgets_canvas[-1].config(fg=self.list_widgets_options[index][7])
                            except:
                                self.list_widgets_options[index][7]=self.list_widgets_options[index][7]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                            try:                                           ## font
                                self.list_widgets_canvas[-1].config(font=("arial",int(self.list_widgets_options[index][8])))
                            except:
                                self.list_widgets_options[index][8]=self.list_widgets_options[index][8]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                            try:                                           ## image before
                                if self.list_widgets_options[index][9] !=None:
                                    self.images.append(PhotoImage(file=self.list_widgets_options[index][9]))
                                    self.list_widgets_canvas[-1].config(image=self.images[-1])
                            except:
                                self.list_widgets_options[index][9]=self.list_widgets_options[index][9]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                        elif widget_type=="Entry":
                            self.list_widgets_canvas.append(Entry(self.canvas,relief="flat",font=("arial",10),bg="gray",highlightthickness=1))
                            try:                                           ## bg
                                self.list_widgets_canvas[-1].config(bg=self.list_widgets_options[index][6])
                            except:
                                self.list_widgets_options[index][6]=self.list_widgets_options[index][6]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                            
                            try:                                           ## fg
                                self.list_widgets_canvas[-1].config(fg=self.list_widgets_options[index][7])
                            except:
                                self.list_widgets_options[index][7]=self.list_widgets_options[index][7]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                            try:                                           ## font
                                self.list_widgets_canvas[-1].config(font=("arial",int(self.list_widgets_options[index][8])))
                            except:
                                self.list_widgets_options[index][8]=self.list_widgets_options[index][8]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                            try:                                           ## highlightcolor
                                self.list_widgets_canvas[-1].config(highlightcolor=self.list_widgets_options[index][12])
                            except:
                                self.list_widgets_options[index][12]=self.list_widgets_options[index][12]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                            try:                                           ## highlightbackground
                                self.list_widgets_canvas[-1].config(highlightbackground=self.list_widgets_options[index][13])
                            except:
                                self.list_widgets_options[index][13]=self.list_widgets_options[index][13]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                        elif widget_type=="Listbox":
                            self.list_widgets_canvas.append(Listbox(self.canvas,relief="flat",font=("arial",10),bd=0,highlightbackground="gray"))
                            try:                                           ## bg
                                self.list_widgets_canvas[-1].config(bg=self.list_widgets_options[index][6])
                            except:
                                self.list_widgets_options[index][6]=self.list_widgets_options[index][6]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                            
                            try:                                           ## fg
                                self.list_widgets_canvas[-1].config(fg=self.list_widgets_options[index][7])
                            except:
                                self.list_widgets_options[index][7]=self.list_widgets_options[index][7]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                            try:                                           ## font
                                self.list_widgets_canvas[-1].config(font=("arial",int(self.list_widgets_options[index][8])))
                            except:
                                self.list_widgets_options[index][8]=self.list_widgets_options[index][8]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                            try:                                           ## highlightcolor
                                self.list_widgets_canvas[-1].config(highlightcolor=self.list_widgets_options[index][12])
                            except:
                                self.list_widgets_options[index][12]=self.list_widgets_options[index][12]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                            try:                                           ## highlightbackground
                                self.list_widgets_canvas[-1].config(highlightbackground=self.list_widgets_options[index][13])
                            except:
                                self.list_widgets_options[index][13]=self.list_widgets_options[index][13]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                        elif widget_type=="Radiobutton" or widget_type=="Checkbutton":
                            self.list_widgets_canvas.append(Radiobutton(self.canvas,text="radiobutton"+str(self.n_radiobutton),relief="flat",bd=0,font=("arial",10)))
                            try:                                           ## text
                                self.list_widgets_canvas[-1].config(text=self.list_widgets_options[index][5])
                            except:
                                self.list_widgets_options[index][5]=self.list_widgets_options[index][5]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                            
                            try:                                           ## bg
                                self.list_widgets_canvas[-1].config(bg=self.list_widgets_options[index][6])
                            except:
                                self.list_widgets_options[index][6]=self.list_widgets_options[index][6]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                            
                            try:                                           ## fg
                                self.list_widgets_canvas[-1].config(fg=self.list_widgets_options[index][7])
                            except:
                                self.list_widgets_options[index][7]=self.list_widgets_options[index][7]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                            try:                                           ## font
                                self.list_widgets_canvas[-1].config(font=("arial",int(self.list_widgets_options[index][8])))
                            except:
                                self.list_widgets_options[index][8]=self.list_widgets_options[index][8]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                            try:                                           ## activebackground
                                self.list_widgets_canvas[-1].config(activebackground=self.list_widgets_options[index][14])
                            except:
                                self.list_widgets_options[index][14]=self.list_widgets_options[index][14]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                            try:                                           ## activeforeground
                                self.list_widgets_canvas[-1].config(activeforeground=self.list_widgets_options[index][15])
                            except:
                                self.list_widgets_options[index][15]=self.list_widgets_options[index][15]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                        elif widget_type=="Canvas":
                            self.list_widgets_canvas.append(Canvas(self.canvas,relief="flat",bd=0))
                            try:                                           ## bg
                                self.list_widgets_canvas[-1].config(bg=self.list_widgets_options[index][6])
                            except:
                                self.list_widgets_options[index][6]=self.list_widgets_options[index][6]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                            try:                                           ## image before
                                if self.list_widgets_options[index][9]==None:
                                    pass
                                else:
                                    self.images.append(PhotoImage(file=self.list_widgets_options[index][9]))
                                    self.list_widgets_canvas[-1].create_image(0,0,anchor=NW,image=self.images[-1])
                            except:
                                self.list_widgets_options[index][9]=self.list_widgets_options[index][9]+"Error"
                                self.n_errors+=1
                                self.list_draggedwidgets.itemconfigure(index,fg="red")
                        self.lbl_errors.config(text=str(self.n_errors))
                        self.list_widgets_canvas[-1].place(x=int(self.list_widgets_options[index][1]),y=int(self.list_widgets_options[index][2]),
                                                           width=int(self.list_widgets_options[index][3]),height=int(self.list_widgets_options[index][4]))
                        index+=1
                        self.list_widgets_canvas[-1].bind("<B1-Motion>",self.moving)
        except:
            pass
    def bt_generate_enter(self,e):
        self.bt_generate.config(image=self.image_generate_after)
    def bt_generate_leave(self,e):
        self.bt_generate.config(image=self.image_generate_before)
    def bt_generate_com(self):
        try:
            file_path=filedialog.asksaveasfilename(defaultextension=".py")
            if file_path!="" and self.n_errors==0:
                with open(file_path,"w") as f1:
                    f1.write("from tkinter import *\n"+
                             "class App(Tk):\n")
                    if self.list_win_options[7]=="self":
                        f1.write(f"    def __init__(self):\n"+
                                 f"        Tk.__init__(self)\n")
                        if self.list_win_options[5]=="center" and self.list_win_options[6]!="center":
                            #self.ws = self.winfo_screenwidth()
                            # self.hs = self.winfo_screenheight()
                            # pos_x=round((self.ws-590)/2)
                            # pos_y=round((self.hs-232)/2)
                            f1.write(f"        self.ws = self.winfo_screenwidth()\n"+
                                     f"        pos_x=round((self.ws-{int(self.list_win_options[0])})/2)\n"+
                                     f"        self.geometry('{self.list_win_options[0]}x{self.list_win_options[1]}+'+str(pos_x)+'+{self.list_win_options[6]}')\n")
                            #f1.write(f"\t\tself.geometry('{self.list_win_options[0]}x{self.list_win_options[1]}')")
                        elif self.list_win_options[5]!="center" and self.list_win_options[6]=="center":
                            f1.write(f"        self.hs = self.winfo_screenheight()\n"+
                                     f"        pos_y=round((self.hs-{int(self.list_win_options[1])})/2)\n"+
                                     f"        self.geometry('{self.list_win_options[0]}x{self.list_win_options[1]}+{self.list_win_options[5]}+'+str(pos_y))\n")
                        elif self.list_win_options[5]=="center" and self.list_win_options[6]=="center":
                            f1.write(f"        self.ws = self.winfo_screenwidth()\n"+
                                     f"        pos_x=round((self.ws-{int(self.list_win_options[0])})/2)\n"+
                                     f"        self.hs = self.winfo_screenheight()\n"+
                                     f"        pos_y=round((self.hs-{int(self.list_win_options[1])})/2)\n"+
                                     f"        self.geometry('{self.list_win_options[0]}x{self.list_win_options[1]}+'+str(pos_x)+'+'+str(pos_y))\n")
                        elif self.list_win_options[5]!="center" and self.list_win_options[6]!="center":
                            f1.write(f"        self.geometry('{self.list_win_options[0]}x{self.list_win_options[1]}+{self.list_win_options[5]}+{self.list_win_options[6]}')\n")
                        f1.write(f"        self.config(bg='{self.list_win_options[2]}')\n")              # bg
                        f1.write(f"        self.attributes('-topmost',{int(self.list_win_options[4])})\n")
                        f1.write(f"        self.overrideredirect({int(self.list_win_options[3])})\n")
                        index=0
                        for widget in self.list_widgets_canvas:
                            if widget.winfo_class()=="Button":
                                if self.list_widgets_options[index][9] !=None:
                                    f1.write(f"        self.image_{self.list_widgets_options[index][0]}_before=PhotoImage(file=r'{self.list_widgets_options[index][9]}')\n")
                                if self.list_widgets_options[index][10] !=None:
                                    f1.write(f"        self.image_{self.list_widgets_options[index][0]}_after=PhotoImage(file=r'{self.list_widgets_options[index][10]}')\n")
                                f1.write(f"        self.{self.list_widgets_options[index][0]}=Button(self,text='{self.list_widgets_options[index][5]}',relief='flat',bd=0")      ##text
                                if self.list_widgets_options[index][6] !=None:     ## bg
                                    f1.write(f",\n                 bg='{self.list_widgets_options[index][6]}'")
                                if self.list_widgets_options[index][7] !=None:     ## fg
                                    f1.write(f",\n                 fg='{self.list_widgets_options[index][7]}'")
                                f1.write(f",\n                 font=('arial',{int(self.list_widgets_options[index][8])})")  ## font
                                if self.list_widgets_options[index][9] !=None:     ## image
                                    f1.write(f",\n                 image=self.image_{self.list_widgets_options[index][0]}_before")
                                if self.list_widgets_options[index][11] !=None:    ## command
                                    f1.write(f",\n                 command={self.list_widgets_options[index][11]}")
                                if self.list_widgets_options[index][14] !=None:    ## activebackground
                                    f1.write(f",\n                 activebackground='{self.list_widgets_options[index][14]}'")
                                if self.list_widgets_options[index][15] !=None:    ## activeforeground
                                    f1.write(f",\n                 activeforeground='{self.list_widgets_options[index][15]}'")
                                f1.write(")\n")
                                f1.write(f"        self.{self.list_widgets_options[index][0]}.place(x={int(self.list_widgets_options[index][1])},y={int(self.list_widgets_options[index][2])},"+
                                         f"width={int(self.list_widgets_options[index][3])},height={int(self.list_widgets_options[index][4])})\n")
                            elif widget.winfo_class()=="Label":
                                if self.list_widgets_options[index][9] !=None:
                                    f1.write(f"        self.image_{self.list_widgets_options[index][0]}_before=PhotoImage(file=r'{self.list_widgets_options[index][9]}')\n")
                                f1.write(f"        self.{self.list_widgets_options[index][0]}=Label(self,text='{self.list_widgets_options[index][5]}',relief='flat',bd=0")
                                if self.list_widgets_options[index][6] !=None:     ## bg
                                    f1.write(f",\n                 bg='{self.list_widgets_options[index][6]}'")
                                if self.list_widgets_options[index][7] !=None:     ## fg
                                    f1.write(f",\n                 fg='{self.list_widgets_options[index][7]}'")
                                f1.write(f",\n                 font=('arial',{int(self.list_widgets_options[index][8])})")  ## font
                                if self.list_widgets_options[index][9] !=None:     ## image
                                    f1.write(f",\n                 image=self.image_{self.list_widgets_options[index][0]}_before")
                                f1.write(")\n")
                                f1.write(f"        self.{self.list_widgets_options[index][0]}.place(x={int(self.list_widgets_options[index][1])},y={int(self.list_widgets_options[index][2])},"+
                                         f"width={int(self.list_widgets_options[index][3])},height={int(self.list_widgets_options[index][4])})\n")
                            elif widget.winfo_class()=="Entry":
                                f1.write(f"        self.{self.list_widgets_options[index][0]}=Entry(self,relief='flat',highlightthickness=1")
                                if self.list_widgets_options[index][6] !=None:     ## bg
                                    f1.write(f",\n                 bg='{self.list_widgets_options[index][6]}'")
                                if self.list_widgets_options[index][7] !=None:     ## fg
                                    f1.write(f",\n                 fg='{self.list_widgets_options[index][7]}'")
                                f1.write(f",\n                 font=('arial',{int(self.list_widgets_options[index][8])})")  ## font
                                if self.list_widgets_options[index][12] !=None:    ## highlightcolor
                                    f1.write(f",\n                 highlightcolor='{self.list_widgets_options[index][12]}'")  
                                if self.list_widgets_options[index][13] !=None:    ## highlightbackground
                                    f1.write(f",\n                 highlightbackground='{self.list_widgets_options[index][13]}'")  
                                f1.write(")\n")
                                f1.write(f"        self.{self.list_widgets_options[index][0]}.place(x={int(self.list_widgets_options[index][1])},y={int(self.list_widgets_options[index][2])},"+
                                         f"width={int(self.list_widgets_options[index][3])},height={int(self.list_widgets_options[index][4])})\n")
                            elif widget.winfo_class()=="Listbox":
                                f1.write(f"        self.{self.list_widgets_options[index][0]}=Listbox(self,relief='flat',bd=0")
                                if self.list_widgets_options[index][6] !=None:     ## bg
                                    f1.write(f",\n                 bg='{self.list_widgets_options[index][6]}'")
                                if self.list_widgets_options[index][7] !=None:     ## fg
                                    f1.write(f",\n                 fg='{self.list_widgets_options[index][7]}'")
                                f1.write(f",\n                 font=('arial',{int(self.list_widgets_options[index][8])})")  ## font
                                if self.list_widgets_options[index][12] !=None:    ## highlightcolor
                                    f1.write(f",\n                 highlightcolor='{self.list_widgets_options[index][12]}'")  
                                if self.list_widgets_options[index][13] !=None:    ## highlightbackground
                                    f1.write(f",\n                 highlightbackground='{self.list_widgets_options[index][13]}'")  
                                f1.write(")\n")
                                f1.write(f"        self.{self.list_widgets_options[index][0]}.place(x={int(self.list_widgets_options[index][1])},y={int(self.list_widgets_options[index][2])},"+
                                         f"width={int(self.list_widgets_options[index][3])},height={int(self.list_widgets_options[index][4])})\n")
                            elif widget.winfo_class()=="Radiobutton":
                                f1.write(f"        self.{self.list_widgets_options[index][0]}=Radiobutton(self,text='{self.list_widgets_options[index][5]}',relief='flat',bd=0")
                                if self.list_widgets_options[index][6] !=None:     ## bg
                                    f1.write(f",\n                 bg='{self.list_widgets_options[index][6]}'")
                                if self.list_widgets_options[index][7] !=None:     ## fg
                                    f1.write(f",\n                 fg='{self.list_widgets_options[index][7]}'")
                                f1.write(f",\n                 font=('arial',{int(self.list_widgets_options[index][8])})")  ## font
                                if self.list_widgets_options[index][14] !=None:    ## activebackground
                                    f1.write(f",\n                 activebackground='{self.list_widgets_options[index][14]}'")
                                if self.list_widgets_options[index][15] !=None:    ## activeforeground
                                    f1.write(f",\n                 activeforeground='{self.list_widgets_options[index][15]}'")
                                f1.write(")\n")
                                f1.write(f"        self.{self.list_widgets_options[index][0]}.place(x={int(self.list_widgets_options[index][1])},y={int(self.list_widgets_options[index][2])},"+
                                         f"width={int(self.list_widgets_options[index][3])},height={int(self.list_widgets_options[index][4])})\n")
                            elif widget.winfo_class()=="Checkbutton":
                                f1.write(f"        self.{self.list_widgets_options[index][0]}=Checkbutton(self,text='{self.list_widgets_options[index][5]}',relief='flat',bd=0")
                                if self.list_widgets_options[index][6] !=None:     ## bg
                                    f1.write(f",\n                 bg='{self.list_widgets_options[index][6]}'")
                                if self.list_widgets_options[index][7] !=None:     ## fg
                                    f1.write(f",\n                 fg='{self.list_widgets_options[index][7]}'")
                                f1.write(f",\n                 font=('arial',{int(self.list_widgets_options[index][8])})")  ## font
                                if self.list_widgets_options[index][14] !=None:    ## activebackground
                                    f1.write(f",\n                 activebackground='{self.list_widgets_options[index][14]}'")
                                if self.list_widgets_options[index][15] !=None:    ## activeforeground
                                    f1.write(f",\n                 activeforeground='{self.list_widgets_options[index][15]}'")
                                f1.write(")\n")
                                f1.write(f"        self.{self.list_widgets_options[index][0]}.place(x={int(self.list_widgets_options[index][1])},y={int(self.list_widgets_options[index][2])},"+
                                         f"width={int(self.list_widgets_options[index][3])},height={int(self.list_widgets_options[index][4])})\n")
                            elif widget.winfo_class()=="Canvas":
                                if self.list_widgets_options[index][9] !=None:
                                    f1.write(f"        self.image_{self.list_widgets_options[index][0]}_before=PhotoImage(file=r'{self.list_widgets_options[index][9]}')\n")
                                f1.write(f"        self.{self.list_widgets_options[index][0]}=Canvas(self,relief='flat',bd=0")
                                if self.list_widgets_options[index][6] !=None:     ## bg
                                    f1.write(f",\n                 bg='{self.list_widgets_options[index][6]}'")
                                if self.list_widgets_options[index][7] !=None:     ## fg
                                    f1.write(f",\n                 fg='{self.list_widgets_options[index][7]}'")
                                f1.write(")\n")
                                if self.list_widgets_options[index][9] !=None:     ## image
                                    f1.write(f"        self.{self.list_widgets_options[index][0]}.create_image(0,0,anchor=NW,image=self.image_{self.list_widgets_options[index][0]}_before)\n")
                                f1.write(f"        self.{self.list_widgets_options[index][0]}.place(x={int(self.list_widgets_options[index][1])},y={int(self.list_widgets_options[index][2])},"+
                                         f"width={int(self.list_widgets_options[index][3])},height={int(self.list_widgets_options[index][4])})\n")
                            index+=1
                        index=0
                        for widget in self.list_widgets_canvas:
                            if widget.winfo_class()=="Button":
                                if self.list_widgets_options[index][10]!=None:
                                    f1.write(f"        self.{self.list_widgets_options[index][0]}.bind('<Enter>',self.{self.list_widgets_options[index][0]}_enter)\n")
                                    f1.write(f"        self.{self.list_widgets_options[index][0]}.bind('<Leave>',self.{self.list_widgets_options[index][0]}_leave)\n")
                                elif self.list_widgets_options[index][16]!=None and self.list_widgets_options[index][17]!=None:
                                    f1.write(f"        self.{self.list_widgets_options[index][0]}.bind('<Enter>',self.{self.list_widgets_options[index][0]}_enter)\n")
                                    f1.write(f"        self.{self.list_widgets_options[index][0]}.bind('<Leave>',self.{self.list_widgets_options[index][0]}_leave)\n")
                                elif self.list_widgets_options[index][18]!=None and self.list_widgets_options[index][19]!=None:
                                    f1.write(f"        self.{self.list_widgets_options[index][0]}.bind('<Enter>',self.{self.list_widgets_options[index][0]}_enter)\n")
                                    f1.write(f"        self.{self.list_widgets_options[index][0]}.bind('<Leave>',self.{self.list_widgets_options[index][0]}_leave)\n")
                            index+=1
                        index=0
                        for widget in self.list_widgets_canvas:
                            if widget.winfo_class()=="Button":
                                s=0
                                if self.list_widgets_options[index][10]!=None:
                                    f1.write(f"    def {self.list_widgets_options[index][0]}_enter(self,e):\n")
                                    f1.write(f"        self.{self.list_widgets_options[index][0]}.config(image=self.image_{self.list_widgets_options[index][0]}_after)\n")
                                    s=1
                                if self.list_widgets_options[index][16]!=None and self.list_widgets_options[index][17]!=None:
                                    if s==0:
                                        f1.write(f"    def {self.list_widgets_options[index][0]}_enter(self,e):\n")
                                        s=1
                                    f1.write(f"        self.{self.list_widgets_options[index][0]}.config(bg='{self.list_widgets_options[index][16]}')\n")
                                if self.list_widgets_options[index][18]!=None and self.list_widgets_options[index][19]!=None:
                                    if s==0:
                                        f1.write(f"    def {self.list_widgets_options[index][0]}_enter(self,e):\n")
                                        s=1
                                    f1.write(f"        self.{self.list_widgets_options[index][0]}.config(fg='{self.list_widgets_options[index][18]}')\n")
                                    s=1
                            index+=1
                        index=0
                        for widget in self.list_widgets_canvas:
                            if widget.winfo_class()=="Button":
                                s=0
                                if self.list_widgets_options[index][10]!=None:
                                    f1.write(f"    def {self.list_widgets_options[index][0]}_leave(self,e):\n")
                                    f1.write(f"        self.{self.list_widgets_options[index][0]}.config(image=self.image_{self.list_widgets_options[index][0]}_before)\n")
                                    s=1
                                if self.list_widgets_options[index][16]!=None and self.list_widgets_options[index][17]!=None:
                                    if s==0:
                                        f1.write(f"    def {self.list_widgets_options[index][0]}_leave(self,e):\n")
                                        s=1
                                    f1.write(f"        self.{self.list_widgets_options[index][0]}.config(bg='{self.list_widgets_options[index][17]}')\n")
                                if self.list_widgets_options[index][18]!=None and self.list_widgets_options[index][19]!=None:
                                    if s==0:
                                        f1.write(f"    def {self.list_widgets_options[index][0]}_leave(self,e):\n")
                                        s=1
                                    f1.write(f"        self.{self.list_widgets_options[index][0]}.config(fg='{self.list_widgets_options[index][19]}')\n")
                                    
                            index+=1
                    else:
                        f1.write(f"    def {self.list_win_options[7]}_com(self):\n")
                        f1.write(f"        self.{self.list_win_options[7]}=Toplevel()\n")
                        if self.list_win_options[5]=="center" and self.list_win_options[6]!="center":
                            #self.ws = self.winfo_screenwidth()
                            # self.hs = self.winfo_screenheight()
                            # pos_x=round((self.ws-590)/2)
                            # pos_y=round((self.hs-232)/2)
                            f1.write(f"        self.ws = self.winfo_screenwidth()\n"+
                                     f"        pos_x=round((self.ws-{int(self.list_win_options[0])})/2)\n"+
                                     f"        self.{self.list_win_options[7]}.geometry('{self.list_win_options[0]}x{self.list_win_options[1]}+'+str(pos_x)+'+{self.list_win_options[6]}')\n")
                            #f1.write(f"\t\tself.geometry('{self.list_win_options[0]}x{self.list_win_options[1]}')")
                        elif self.list_win_options[5]!="center" and self.list_win_options[6]=="center":
                            f1.write(f"        self.hs = self.winfo_screenheight()\n"+
                                     f"        pos_y=round((self.hs-{int(self.list_win_options[1])})/2)\n"+
                                     f"        self.{self.list_win_options[7]}.geometry('{self.list_win_options[0]}x{self.list_win_options[1]}+{self.list_win_options[5]}+'+str(pos_y))\n")
                        elif self.list_win_options[5]=="center" and self.list_win_options[6]=="center":
                            f1.write(f"        self.ws = self.winfo_screenwidth()\n"+
                                     f"        pos_x=round((self.ws-{int(self.list_win_options[0])})/2)\n"+
                                     f"        self.hs = self.winfo_screenheight()\n"+
                                     f"        pos_y=round((self.hs-{int(self.list_win_options[1])})/2)\n"+
                                     f"        self.{self.list_win_options[7]}.geometry('{self.list_win_options[0]}x{self.list_win_options[1]}+'+str(pos_x)+'+'+str(pos_y))\n")
                        elif self.list_win_options[5]!="center" and self.list_win_options[6]!="center":
                            f1.write(f"        self.{self.list_win_options[7]}.geometry('{self.list_win_options[0]}x{self.list_win_options[1]}+{self.list_win_options[5]}+{self.list_win_options[6]}')\n")
                        f1.write(f"        self.{self.list_win_options[7]}.config(bg='{self.list_win_options[2]}')\n")              # bg
                        f1.write(f"        self.{self.list_win_options[7]}.attributes('-topmost',{int(self.list_win_options[4])})\n")
                        f1.write(f"        self.{self.list_win_options[7]}.overrideredirect({int(self.list_win_options[3])})\n")
                        index=0
                        for widget in self.list_widgets_canvas:
                            if widget.winfo_class()=="Button":
                                if self.list_widgets_options[index][9] !=None:
                                    f1.write(f"        self.image_{self.list_widgets_options[index][0]}_before=PhotoImage(file=r'{self.list_widgets_options[index][9]}')\n")
                                if self.list_widgets_options[index][10] !=None:
                                    f1.write(f"        self.image_{self.list_widgets_options[index][0]}_after=PhotoImage(file=r'{self.list_widgets_options[index][10]}')\n")
                                f1.write(f"        self.{self.list_widgets_options[index][0]}=Button(self.{self.list_win_options[7]},text='{self.list_widgets_options[index][5]}',relief='flat',bd=0")      ##text
                                if self.list_widgets_options[index][6] !=None:     ## bg
                                    f1.write(f",\n                 bg='{self.list_widgets_options[index][6]}'")
                                if self.list_widgets_options[index][7] !=None:     ## fg
                                    f1.write(f",\n                 fg='{self.list_widgets_options[index][7]}'")
                                f1.write(f",\n                 font=('arial',{int(self.list_widgets_options[index][8])})")  ## font
                                if self.list_widgets_options[index][9] !=None:     ## image
                                    f1.write(f",\n                 image=self.image_{self.list_widgets_options[index][0]}_before")
                                if self.list_widgets_options[index][11] !=None:    ## command
                                    f1.write(f",\n                 command={self.list_widgets_options[index][11]}")
                                if self.list_widgets_options[index][14] !=None:    ## activebackground
                                    f1.write(f",\n                 activebackground='{self.list_widgets_options[index][14]}'")
                                if self.list_widgets_options[index][15] !=None:    ## activeforeground
                                    f1.write(f",\n                 activeforeground='{self.list_widgets_options[index][15]}'")
                                f1.write(")\n")
                                f1.write(f"        self.{self.list_widgets_options[index][0]}.place(x={int(self.list_widgets_options[index][1])},y={int(self.list_widgets_options[index][2])},"+
                                         f"width={int(self.list_widgets_options[index][3])},height={int(self.list_widgets_options[index][4])})\n")
                            elif widget.winfo_class()=="Label":
                                if self.list_widgets_options[index][9] !=None:
                                    f1.write(f"        self.image_{self.list_widgets_options[index][0]}_before=PhotoImage(file=r'{self.list_widgets_options[index][9]}')\n")
                                f1.write(f"        self.{self.list_widgets_options[index][0]}=Label(self.{self.list_win_options[7]},text='{self.list_widgets_options[index][5]}',relief='flat',bd=0")
                                if self.list_widgets_options[index][6] !=None:     ## bg
                                    f1.write(f",\n                 bg='{self.list_widgets_options[index][6]}'")
                                if self.list_widgets_options[index][7] !=None:     ## fg
                                    f1.write(f",\n                 fg='{self.list_widgets_options[index][7]}'")
                                f1.write(f",\n                 font=('arial',{int(self.list_widgets_options[index][8])})")  ## font
                                if self.list_widgets_options[index][9] !=None:     ## image
                                    f1.write(f",\n                 image=self.image_{self.list_widgets_options[index][0]}_before")
                                f1.write(")\n")
                                f1.write(f"        self.{self.list_widgets_options[index][0]}.place(x={int(self.list_widgets_options[index][1])},y={int(self.list_widgets_options[index][2])},"+
                                         f"width={int(self.list_widgets_options[index][3])},height={int(self.list_widgets_options[index][4])})\n")
                            elif widget.winfo_class()=="Entry":
                                f1.write(f"        self.{self.list_widgets_options[index][0]}=Entry(self.{self.list_win_options[7]},relief='flat',highlightthickness=1")
                                if self.list_widgets_options[index][6] !=None:     ## bg
                                    f1.write(f",\n                 bg='{self.list_widgets_options[index][6]}'")
                                if self.list_widgets_options[index][7] !=None:     ## fg
                                    f1.write(f",\n                 fg='{self.list_widgets_options[index][7]}'")
                                f1.write(f",\n                 font=('arial',{int(self.list_widgets_options[index][8])})")  ## font
                                if self.list_widgets_options[index][12] !=None:    ## highlightcolor
                                    f1.write(f",\n                 highlightcolor='{self.list_widgets_options[index][12]}'")  
                                if self.list_widgets_options[index][13] !=None:    ## highlightbackground
                                    f1.write(f",\n                 highlightbackground='{self.list_widgets_options[index][13]}'")  
                                f1.write(")\n")
                                f1.write(f"        self.{self.list_widgets_options[index][0]}.place(x={int(self.list_widgets_options[index][1])},y={int(self.list_widgets_options[index][2])},"+
                                         f"width={int(self.list_widgets_options[index][3])},height={int(self.list_widgets_options[index][4])})\n")
                            elif widget.winfo_class()=="Listbox":
                                f1.write(f"        self.{self.list_widgets_options[index][0]}=Listbox(self.{self.list_win_options[7]},relief='flat',bd=0")
                                if self.list_widgets_options[index][6] !=None:     ## bg
                                    f1.write(f",\n                 bg='{self.list_widgets_options[index][6]}'")
                                if self.list_widgets_options[index][7] !=None:     ## fg
                                    f1.write(f",\n                 fg='{self.list_widgets_options[index][7]}'")
                                f1.write(f",\n                 font=('arial',{int(self.list_widgets_options[index][8])})")  ## font
                                if self.list_widgets_options[index][12] !=None:    ## highlightcolor
                                    f1.write(f",\n                 highlightcolor='{self.list_widgets_options[index][12]}'")  
                                if self.list_widgets_options[index][13] !=None:    ## highlightbackground
                                    f1.write(f",\n                 highlightbackground='{self.list_widgets_options[index][13]}'")  
                                f1.write(")\n")
                                f1.write(f"        self.{self.list_widgets_options[index][0]}.place(x={int(self.list_widgets_options[index][1])},y={int(self.list_widgets_options[index][2])},"+
                                         f"width={int(self.list_widgets_options[index][3])},height={int(self.list_widgets_options[index][4])})\n")
                            elif widget.winfo_class()=="Radiobutton":
                                f1.write(f"        self.{self.list_widgets_options[index][0]}=Radiobutton(self.{self.list_win_options[7]},text='{self.list_widgets_options[index][5]}',relief='flat',bd=0")
                                if self.list_widgets_options[index][6] !=None:     ## bg
                                    f1.write(f",\n                 bg='{self.list_widgets_options[index][6]}'")
                                if self.list_widgets_options[index][7] !=None:     ## fg
                                    f1.write(f",\n                 fg='{self.list_widgets_options[index][7]}'")
                                f1.write(f",\n                 font=('arial',{int(self.list_widgets_options[index][8])})")  ## font
                                if self.list_widgets_options[index][14] !=None:    ## activebackground
                                    f1.write(f",\n                 activebackground='{self.list_widgets_options[index][14]}'")
                                if self.list_widgets_options[index][15] !=None:    ## activeforeground
                                    f1.write(f",\n                 activeforeground='{self.list_widgets_options[index][15]}'")
                                f1.write(")\n")
                                f1.write(f"        self.{self.list_widgets_options[index][0]}.place(x={int(self.list_widgets_options[index][1])},y={int(self.list_widgets_options[index][2])},"+
                                         f"width={int(self.list_widgets_options[index][3])},height={int(self.list_widgets_options[index][4])})\n")
                            elif widget.winfo_class()=="Checkbutton":
                                f1.write(f"        self.{self.list_widgets_options[index][0]}=Checkbutton(self.{self.list_win_options[7]},text='{self.list_widgets_options[index][5]}',relief='flat',bd=0")
                                if self.list_widgets_options[index][6] !=None:     ## bg
                                    f1.write(f",\n                 bg='{self.list_widgets_options[index][6]}'")
                                if self.list_widgets_options[index][7] !=None:     ## fg
                                    f1.write(f",\n                 fg='{self.list_widgets_options[index][7]}'")
                                f1.write(f",\n                 font=('arial',{int(self.list_widgets_options[index][8])})")  ## font
                                if self.list_widgets_options[index][14] !=None:    ## activebackground
                                    f1.write(f",\n                 activebackground='{self.list_widgets_options[index][14]}'")
                                if self.list_widgets_options[index][15] !=None:    ## activeforeground
                                    f1.write(f",\n                 activeforeground='{self.list_widgets_options[index][15]}'")
                                f1.write(")\n")
                                f1.write(f"        self.{self.list_widgets_options[index][0]}.place(x={int(self.list_widgets_options[index][1])},y={int(self.list_widgets_options[index][2])},"+
                                         f"width={int(self.list_widgets_options[index][3])},height={int(self.list_widgets_options[index][4])})\n")
                            elif widget.winfo_class()=="Canvas":
                                if self.list_widgets_options[index][9] !=None:
                                    f1.write(f"        self.image_{self.list_widgets_options[index][0]}_before=PhotoImage(file=r'{self.list_widgets_options[index][9]}')\n")
                                f1.write(f"        self.{self.list_widgets_options[index][0]}=Canvas(self.{self.list_win_options[7]},relief='flat',bd=0")
                                if self.list_widgets_options[index][6] !=None:     ## bg
                                    f1.write(f",\n                 bg='{self.list_widgets_options[index][6]}'")
                                if self.list_widgets_options[index][7] !=None:     ## fg
                                    f1.write(f",\n                 fg='{self.list_widgets_options[index][7]}'")
                                f1.write(")\n")
                                if self.list_widgets_options[index][9] !=None:     ## image
                                    f1.write(f"        self.{self.list_widgets_options[index][0]}.create_image(0,0,anchor=NW,image=self.image_{self.list_widgets_options[index][0]}_before)\n")
                                f1.write(f"        self.{self.list_widgets_options[index][0]}.place(x={int(self.list_widgets_options[index][1])},y={int(self.list_widgets_options[index][2])},"+
                                         f"width={int(self.list_widgets_options[index][3])},height={int(self.list_widgets_options[index][4])})\n")
                            index+=1
                        index=0
                        for widget in self.list_widgets_canvas:
                            if widget.winfo_class()=="Button":
                                if self.list_widgets_options[index][10]!=None:
                                    f1.write(f"        self.{self.list_widgets_options[index][0]}.bind('<Enter>',self.{self.list_widgets_options[index][0]}_enter)\n")
                                    f1.write(f"        self.{self.list_widgets_options[index][0]}.bind('<Leave>',self.{self.list_widgets_options[index][0]}_leave)\n")
                                elif self.list_widgets_options[index][16]!=None and self.list_widgets_options[index][17]!=None:
                                    f1.write(f"        self.{self.list_widgets_options[index][0]}.bind('<Enter>',self.{self.list_widgets_options[index][0]}_enter)\n")
                                    f1.write(f"        self.{self.list_widgets_options[index][0]}.bind('<Leave>',self.{self.list_widgets_options[index][0]}_leave)\n")
                                elif self.list_widgets_options[index][18]!=None and self.list_widgets_options[index][19]!=None:
                                    f1.write(f"        self.{self.list_widgets_options[index][0]}.bind('<Enter>',self.{self.list_widgets_options[index][0]}_enter)\n")
                                    f1.write(f"        self.{self.list_widgets_options[index][0]}.bind('<Leave>',self.{self.list_widgets_options[index][0]}_leave)\n")
                            index+=1
                        index=0
                        for widget in self.list_widgets_canvas:
                            if widget.winfo_class()=="Button":
                                s=0
                                if self.list_widgets_options[index][10]!=None:
                                    f1.write(f"    def {self.list_widgets_options[index][0]}_enter(self,e):\n")
                                    f1.write(f"        self.{self.list_widgets_options[index][0]}.config(image=self.image_{self.list_widgets_options[index][0]}_after)\n")
                                    s=1
                                if self.list_widgets_options[index][16]!=None and self.list_widgets_options[index][17]!=None:
                                    if s==0:
                                        f1.write(f"    def {self.list_widgets_options[index][0]}_enter(self,e):\n")
                                        s=1
                                    f1.write(f"        self.{self.list_widgets_options[index][0]}.config(bg='{self.list_widgets_options[index][16]}')\n")
                                if self.list_widgets_options[index][18]!=None and self.list_widgets_options[index][19]!=None:
                                    if s==0:
                                        f1.write(f"    def {self.list_widgets_options[index][0]}_enter(self,e):\n")
                                        s=1
                                    f1.write(f"        self.{self.list_widgets_options[index][0]}.config(fg='{self.list_widgets_options[index][18]}')\n")
                                    s=1
                            index+=1
                        index=0
                        for widget in self.list_widgets_canvas:
                            if widget.winfo_class()=="Button":
                                s=0
                                if self.list_widgets_options[index][10]!=None:
                                    f1.write(f"    def {self.list_widgets_options[index][0]}_leave(self,e):\n")
                                    f1.write(f"        self.{self.list_widgets_options[index][0]}.config(image=self.image_{self.list_widgets_options[index][0]}_before)\n")
                                    s=1
                                if self.list_widgets_options[index][16]!=None and self.list_widgets_options[index][17]!=None:
                                    if s==0:
                                        f1.write(f"    def {self.list_widgets_options[index][0]}_leave(self,e):\n")
                                        s=1
                                    f1.write(f"        self.{self.list_widgets_options[index][0]}.config(bg='{self.list_widgets_options[index][17]}')\n")
                                if self.list_widgets_options[index][18]!=None and self.list_widgets_options[index][19]!=None:
                                    if s==0:
                                        f1.write(f"    def {self.list_widgets_options[index][0]}_leave(self,e):\n")
                                        s=1
                                    f1.write(f"        self.{self.list_widgets_options[index][0]}.config(fg='{self.list_widgets_options[index][19]}')\n")
                                    
                            index+=1
                    f1.write("a=App()\n"+
                             "a.mainloop()")
                msgbox=messagebox.showinfo("Exported!","Done!")
            else:
                if file_path=="":
                    pass
                else:
                    msgbox=messagebox.showinfo("Can't export!","Please check errors!")
        except:
            pass
                    
    def exit_com(self):
        choice=True
        if self.path_file.get()=="":
            choice=messagebox.askyesno("Warnning","Do you want to save the file?")
        else:
            self.bt_save_com(None)
        if choice==True:
            self.bt_save_com(None)
            self.destroy()
        else:
            self.destroy()
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
        
        
        
        
        
        
        
        
        

        
app=Designer()
app.mainloop()
        