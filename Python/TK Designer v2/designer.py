from tkinter import *
from tkinter import filedialog,messagebox,ttk
from threading import Thread
from widgets import *
from Themes_Font import *
import os
import time
import shutil
import copy
import sys
from ast import literal_eval
import PyInstaller.__main__
import pygame
#from photos import *


# widgets=[] ## will have the names of the widgets
# widget_properties=[]

# widget_properties_default=[]
# widget_properties_pack={}
# widget_properties_grid={}
# widget_properties_place={}
# widget_properties_pack_defaults={}
# widget_properties_grid_defaults={}
# widget_properties_place_defaults={}
# win_properties={}
# win_properties_defaults={}
# themes=[]
# font_sizes={}
# font_names={}
# def LoadWidgets(filename):
#     source = open(filename, 'r').read() + '\n'
#     comp=compile(source, filename, 'exec')
#     return comp


direct=os.getcwd()
# comp=LoadWidgets(r'widgets.py')
# exec(comp)

# comp=LoadWidgets(r'Themes_Font.py')
# exec(comp)


class TkDesigner(Tk):
    def __init__(self):
        try:
            os.chdir(direct)
            self.registered=1
            Tk.__init__(self)
            #self.ProgramInfo()
            
            #self.attributes('-alpha', 0.7)
            #self.configure(bg='white')
            #self.wm_attributes('-transparentcolor','white')
            self.protocol('WM_DELETE_WINDOW', self.bt_exit_com)
            self.bind('<Return>',self.MainWin)
            self.title('TK design')
            
            self.iconbitmap(r'icons\icon.ico')
            self.attributes('-topmost',1)
            self.width_screen=self.winfo_screenwidth()
            self.height_screen=self.winfo_screenheight()
            pos_x=round((self.width_screen-500)/2)
            pos_y=round((self.height_screen-600)/2)
            self.geometry(f'500x600+{pos_x}+{pos_y}')
            self.configure(bg='#4a4949')
            self.overrideredirect(0)
            self.lbl_header=Label(self,bg='#3e3d3d')
            self.lbl_header.place(x=0,y=0,width=500,height=39)
            self.lbl_title=Label(self,bg='#3e3d3d',fg='#06a7bf',text='TK Design',font=('arial',12,'bold'))
            self.lbl_title.place(x=10,y=10)
            self.lbl_NewOpen=Label(self,bg='#4a4949',fg='white',text='New |Open project',font=('arial',15))
            self.lbl_NewOpen.place(x=47,y=70)
            self.lbl_back=Label(self,bg='#575656')
            self.lbl_back.place(x=47,y=100,width=406,height=284)
            
            self.lbl_path=Label(self,bg='#575656',fg='#13d6e2',text='path',font=('arial',14))
            self.lbl_path.place(x=63,y=230)
            self.ent_path=Entry(self,relief='flat')
            self.ent_path.place(x=63,y=258,width=375,height=26)
            self.ent_path.bind('<Button-1>',self.bt_openFinit_com)
            self.lbl_ProjName=Label(self,bg='#575656',fg='#13d6e2',text='project name',font=('arial',14))
            self.lbl_ProjName.place(x=63,y=148)
            self.ent_ProjName=Entry(self,relief='flat')
            self.ent_ProjName.place(x=63,y=176,width=375,height=26)
            self.lbl_error=Label(self,text='Enter: ',fg='#ec1f0a',bg='#575656',font=('arial',11))
            self.image_open_before=PhotoImage(master=self,file=r'icons\open_before.png')
            self.image_open_after=PhotoImage(master=self,file=r'icons\open_after.png')
            self.bt_open=Button(self,relief='flat',bd=0,command=self.bt_openFinit_com,image=self.image_open_before,bg='#575656',activebackground='#575656')
            self.bt_open.place(x=63,y=323,width=41,height=34)
            self.bt_open.bind('<Enter>',self.bt_open_enter)
            self.bt_open.bind('<Leave>',self.bt_open_leave)
            self.lbl_open=Label(self,text='open project',fg='#13d6e2',bg='#575656',font=('arial',12,'bold'))
            self.lbl_open.bind('<Button-1>',self.bt_openFinit_com)
            self.lbl_open.place(x=107,y=330)
            
            self.lbl_theme=Label(self,fg='white',bg='#4a4949',font=('arial',15),text='Theme')
            self.lbl_theme.place(x=47,y=400)
            self.image_dark_before=PhotoImage(master=self,file=r'icons\dark_before.png')
            self.image_dark_after=PhotoImage(master=self,file=r'icons\dark_after.png')
            self.image_dark_sign=PhotoImage(master=self,file=r'icons\dark_sign.png')
            self.image_light_sign=PhotoImage(master=self,file=r'icons\light_sign.png')
            
            self.bt_dark=Button(self,image=self.image_dark_sign,relief='flat',bd=0,command=self.bt_dark_com)
            self.bt_dark.place(x=141,y=445,width=100,height=112)
            self.bt_dark.bind('<Enter>',self.bt_dark_enter)
            self.bt_dark.bind('<Leave>',self.bt_dark_leave)
            self.image_light_before=PhotoImage(master=self,file=r'icons\light_before.png')
            self.image_light_after=PhotoImage(master=self,file=r'icons\light_after.png')
            self.bt_light=Button(self,image=self.image_light_before,relief='flat',bd=0,command=self.bt_light_com)
            self.bt_light.place(x=260,y=445,width=100,height=112)
            self.bt_light.bind('<Enter>',self.bt_light_enter)
            self.bt_light.bind('<Leave>',self.bt_light_leave)
            self.bt_ok=Button(self,text='ok',fg='white',bg='#06a7bf',activebackground='#06a7bf',activeforeground='white',bd=0,relief='flat',command=self.MainWin,font=('arial',14))
            self.bt_ok.place(x=416,y=558,width=72,height=31)
            self.ConsolHide=False
            self.WinHide=False
            self.playing=False
            self.paused=False
            self.pointer_music=0
            self.Theme=0        # 0 for dark_theme     and    1 for light_theme
            self.list_widgets_on_wins=[]
            self.list_widgets_on_wins_Errors=[]
            self.Error_win=0
            ###
            ###
            self.list_widgets_on_wins_properties=[]
            self.list_wins_properties=copy.deepcopy(win_properties_defaults)
            self.list_entry=[]
            self.list_inputs=[]
            self.list_vars=[]
            self.images=[]
            self.selected=()
            self.pointer_win=0
            self.num_inserted_win=1
            self.num_widget=-1
            self.selected_master=0
            self.index_RemovedWidget=-1
            self.list_frames_on_wins=[]
            self.prev_SelectedWidget=-1
            self.posx_mouse_widget=0
            self.posy_mouse_widget=0
            self.CodeHide=1
            self.n_run=1
            self.WidgetLastCopied=-1
            self.open_file=0
            self.running=0
            self.list_widgets_on_wins_copy_use=[]
            self.list_widgets_on_wins_properties_copy_use=[]
        except:
            pass
    def bt_exit_com(self):
        try:
            self.destroy()
            sys.exit()
        except:
            pass
    def bt_dark_enter(self,e):
        try:
            if self.Theme==1:
                self.bt_dark.config(image=self.image_dark_after)
        except:
            pass
    def bt_dark_leave(self,e):
        try:
            if self.Theme==1:
                self.bt_dark.config(image=self.image_dark_before)
        except:
            pass
    def bt_dark_com(self):
        try:
            self.Theme=0
            self.bt_dark.config(image=self.image_dark_sign)
            self.bt_light.config(image=self.image_light_before)
        except:
            pass
    def bt_light_com(self):
        try:
            self.Theme=1
            self.bt_light.config(image=self.image_light_sign)
            self.bt_dark.config(image=self.image_dark_before)
        except:
            pass
    def bt_light_enter(self,e):
        try:
            if self.Theme==0:
                self.bt_light.config(image=self.image_light_after)
        except:
            pass
    def bt_light_leave(self,e):
        try:
            if self.Theme==0:
                self.bt_light.config(image=self.image_light_before)
        except:
            pass
    def SelectPath(self,e):
        try:
            path=filedialog.askdirectory()
            if path:
                self.ent_path.delete(0,END)
                self.ent_path.insert(END,path)
                self.open_file=0
        except:
            pass
    def MainWin(self,e=None):
        try:
            self.path_project=self.ent_path.get()   # path of the folder of the project
            self.proj_name=self.ent_ProjName.get()
            if not os.path.exists(self.path_project):
                self.lbl_error.config(text='invalid path!')
                self.lbl_error.place(x=63,y=286)
            if not self.CheckId(self.proj_name):
                self.lbl_error.config(text='invalid project name!')
                self.lbl_error.place(x=63,y=286)
           
            if os.path.exists(self.path_project) and self.CheckId(self.proj_name) :
                #print(self.path_project)
                self.withdraw()
                self.main=Toplevel()
                self.main.iconbitmap(r'icons\icon.ico')
                self.main.bind('<Motion>',self.th_posx_posy)
                self.main.title('TK Design')
                self.main.bind('<Return>',self.ClickEnterTotCom)
                self.main.bind('<Delete>',self.DeleteWidget)
                self.main.bind('<Control-s>',self.ControlS)
                self.main.bind('<Control-b>',self.SendBack)
                self.main.bind('<Control-f>',self.SendFront)
                self.main.bind('<Control-q>',self.BringBack)
                self.main.bind('<Control-w>',self.BringFront)
                
                
                self.main.protocol('WM_DELETE_WINDOW', self.ExitFcn)
                self.width_available=self.width_screen-83.32
                #self.height_available_left_right=self.height_screen-176.75-41-53
                self.height_available_left_right=self.height_screen-261
                #self.height_available_center=self.height_screen-174.25-41-53
                self.height_available_center=self.height_screen-260
                self.main.geometry(f'{self.width_screen}x{self.height_screen-41-53}') # 73=height of the task bar +height of the head
                self.main.state('zoomed')
                self.lbl_back=Label(self.main,bg=themes[self.Theme]['win bg'])
                self.lbl_back.place(x=0,y=0,width=1920,height=1080)
                self.lbl_widgets=Label(self.main,text='widgets',font=(font_names['head labels'],font_sizes['head labels']),fg=themes[self.Theme]['labels fg'],bg=themes[self.Theme]['head labels'])
                self.lbl_widgets.place(x=18,y=62,height=25,width=round(0.1584*self.width_available))
                self.listbox_widgets=Listbox(self.main,bg=themes[self.Theme]['lists'],highlightcolor=themes[self.Theme]['lists highlightcolor'],font=(font_names['lists'],font_sizes['lists']),highlightbackground=themes[self.Theme]['lists highlightbackground'],relief='flat',fg=themes[self.Theme]['lists fg'])
                
                self.listbox_widgets.place(x=18,y=87,width=round(0.1584*self.width_available),height=round(0.5477*self.height_available_left_right))
                self.lbl_widgets_on_win=Label(self.main,text='widgets',font=(font_names['head labels'],font_sizes['head labels']),fg=themes[self.Theme]['labels fg'],bg=themes[self.Theme]['head labels'])
                self.lbl_widgets_on_win.place(x=18,y=87+round(0.5477*self.height_available_left_right)+15,height=25,width=round(0.1584*self.width_available))
                self.listbox_widgets_on_win=Listbox(self.main,selectmode=SINGLE,bg=themes[self.Theme]['lists'],highlightcolor=themes[self.Theme]['lists highlightcolor'],font=(font_names['lists'],font_sizes['lists']),highlightbackground=themes[self.Theme]['lists highlightbackground'],relief='flat',fg=themes[self.Theme]['lists fg'])
                self.listbox_widgets_on_win.place(x=18,y=87+round(0.5477*self.height_available_left_right)+15+25,width=round(0.1584*self.width_available),height=round(0.45103*self.height_available_left_right))
                
                self.lbl_filename=Label(self.main,fg='white',bg=themes[self.Theme]['head labels'])
                self.lbl_filename.place(x=18+round(0.1584*self.width_available)+30,y=62,height=25,width=round(0.6412*self.width_available))
                self.lbl_filename_txt=Label(self.main,text='self',font=(font_names['head labels'],font_sizes['head labels']),fg=themes[self.Theme]['labels fg'],bg=themes[self.Theme]['filename bg'])
                self.lbl_filename_txt.place(x=18+round(0.1584*self.width_available)+30+5,y=62,height=25)
                #self.canvas_main=Canvas(self.main,bg='white',highlightthickness=0)
                #self.canvas_main.place(x=18+round(0.1584*self.width_available)+30,y=87,width=round(0.6412*self.width_available),height=round(0.82907*self.height_available_center))
                self.lbl_consol=Label(self.main,text='consol',font=(font_names['head labels'],font_sizes['head labels']),fg=themes[self.Theme]['labels fg'],bg=themes[self.Theme]['head labels'])
                self.lbl_consol.place(x=18+round(0.1584*self.width_available)+30,y=87+round(0.82907*self.height_available_center)+13,height=25,width=round(0.6412*self.width_available))
                self.txt_consol=Text(self.main,bg=themes[self.Theme]['lists'],font=(font_names['lists'],font_sizes['lists']),highlightbackground='orange',relief='flat',fg=themes[self.Theme]["other labels"])
                self.txt_consol.place(x=18+round(0.1584*self.width_available)+30,y=87+round(0.82907*self.height_available_center)+13+25,width=round(0.6412*self.width_available),height=round(0.16877*self.height_available_center))
                self.txt_consol.insert('1.0','\n'*100)
                self.txt_consol.insert('1.0','R[1]: ')
                self.txt_consol.tag_config("green",foreground="#0aff12")
                self.txt_consol.config(state='disabled')
                
                
                
                self.lbl_properties=Label(self.main,text='properties',font=(font_names['head labels'],font_sizes['head labels']),fg=themes[self.Theme]['labels fg'],bg=themes[self.Theme]['head labels'])
                self.lbl_properties.place(x=18+round(0.1584*self.width_available)+30+round(0.6412*self.width_available)+14,y=62,height=25,width=round(0.2003*self.width_available))
                #self.canvas_properties=Canvas(self.main,bg=themes[self.Theme]['lists'],highlightthickness=0)
                #self.canvas_properties.place(x=18+round(0.1584*self.width_available)+30+round(0.6412*self.width_available)+14,y=87,width=round(0.2003*self.width_available),height=round(0.5477*self.height_available_left_right))
                self.lbl_wins=Label(self.main,text='wins',font=(font_names['head labels'],font_sizes['head labels']),fg=themes[self.Theme]['labels fg'],bg=themes[self.Theme]['head labels'])
                self.lbl_wins.place(x=18+round(0.1584*self.width_available)+30+round(0.6412*self.width_available)+14,y=87+round(0.5477*self.height_available_left_right)+15,height=25,width=round(0.2003*self.width_available))
                self.listbox_wins=Listbox(self.main,bg=themes[self.Theme]['lists'],highlightcolor=themes[self.Theme]['lists highlightcolor'],font=(font_names['lists'],font_sizes['lists']),highlightbackground=themes[self.Theme]['lists highlightbackground'],relief='flat',fg=themes[self.Theme]['lists fg'])
                self.listbox_wins.place(x=18+round(0.1584*self.width_available)+30+round(0.6412*self.width_available)+14,y=87+round(0.5477*self.height_available_left_right)+15+25,width=round(0.2003*self.width_available),height=round(0.45103*self.height_available_left_right))
                self.listbox_wins.bind('<Double-Button-1>',self.DoubleClickOpenWin)
                self.lbl_head=Label(self.main,bg=themes[self.Theme]['head bar'],height='2')
                self.lbl_head.pack(side=TOP,fill='x')
                self.lbl_botom=Label(self.main,bg=themes[self.Theme]['status bar'],height='2')
                self.lbl_botom.pack(side=BOTTOM,fill='x')
                self.lbl_status=Label(self.lbl_botom,text='posx:_, posy:_',fg='white',bg=themes[self.Theme]['status bar'],font=('arial',12))
                self.lbl_status.pack(side=LEFT)
                self.image_logo=PhotoImage(master=self.main,file=r"icons\slogan.png")
                self.lbl_logo_right=Label(self.main,bg=themes[self.Theme]['status bar'],image=self.image_logo)
                self.lbl_logo_right.place(x=18+round(0.1584*self.width_available)+30+round(0.6412*self.width_available)+14+round(0.2003*self.width_available)-130,y=87+round(0.5477*self.height_available_left_right)+15+25+round(0.45103*self.height_available_left_right)+27,width=50,height=35)
                self.lbl_logo_elprince=Label(self.main,bg=themes[self.Theme]['status bar'],text='ELPRINCE',fg='#c1212c',font=('arial',13,'bold'))
                self.lbl_logo_elprince.place(x=18+round(0.1584*self.width_available)+30+round(0.6412*self.width_available)+14+round(0.2003*self.width_available)-130+40,y=87+round(0.5477*self.height_available_left_right)+15+25+round(0.45103*self.height_available_left_right)+27)
                
                
                self.bt_exit_win=Button(self.main,bg=themes[self.Theme]['head labels'],activebackground=themes[self.Theme]['head labels'],text='x',relief='flat',fg='white',font=(font_sizes['btns']),activeforeground='white',command=self.bt_exit_win_com)
                self.bt_exit_win.place(x=18+round(0.1584*self.width_available)+30+round(0.6412*self.width_available)-20,y=62,height=25,width=20)
                self.bt_hide_consol=Button(self.main,bg=themes[self.Theme]['head labels'],activebackground=themes[self.Theme]['head labels'],text='-',relief='flat',fg='white',font=('bold',font_sizes['btns']),activeforeground='white',command=self.bt_hide_consol_com)
                self.bt_hide_consol.place(x=18+round(0.1584*self.width_available)+30+round(0.6412*self.width_available)-20,y=87+round(0.82907*self.height_available_center)+13,height=25,width=20)
                
                self.image_stop_before=PhotoImage(master=self.main,file=r'icons\stop_before.png')
                self.image_stop_after=PhotoImage(master=self.main,file=r'icons\stop_after.png')
                self.bt_stop_running=Button(self.main,bg=themes[self.Theme]['head labels'],activebackground=themes[self.Theme]['head labels'],relief='flat',bd=0,command=self.bt_stop_running_com,image=self.image_stop_after)
                self.bt_stop_running.place(x=18+round(0.1584*self.width_available)+30+round(0.6412*self.width_available)-40,y=87+round(0.82907*self.height_available_center)+18,height=15,width=15)
                
                ## adding scroll bar to the main canvas
                
                #self.main_frame.place(x=18+round(0.1584*self.width_available)+30,y=87,width=round(0.6412*self.width_available),height=round(0.82907*self.height_available_center))
                
                self.main_frame=Frame(self.main,bg='white')
                self.main_frame.place(x=18+round(0.1584*self.width_available)+30,y=87,width=round(0.6412*self.width_available),height=round(0.82907*self.height_available_center))
                
                self.my_canvas=Canvas(self.main_frame,scrollregion=(0,0,round(0.6412*self.width_available)-17,round(0.82907*self.height_available_center)-17),highlightthickness=0,bg='white')
                self.my_canvas.place(x=0,y=0,width=round(0.6412*self.width_available)-17,height=round(0.82907*self.height_available_center)-17)
                self.win_width=round(0.6412*self.width_available)-17
                self.win_height=round(0.82907*self.height_available_center)-17
                
                self.my_scrollbar=ttk.Scrollbar(self.main_frame,orient=VERTICAL,command=self.my_canvas.yview)
                
                self.my_scrollbar.pack(side=RIGHT,fill=Y)
                
                self.my_scrollbar2=ttk.Scrollbar(self.main_frame,orient=HORIZONTAL,command=self.my_canvas.xview)
                self.my_scrollbar2.pack(side=BOTTOM,fill=X)
                
                self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
                self.my_canvas.configure(xscrollcommand=self.my_scrollbar2.set)
                
                
                self.second_frame=Frame(self.my_canvas,bg='white')
                self.second_frame.bind('<Button-1>',self.properties_win)
                self.second_frame.bind('<Button-3>',self.RightClick)
                #self.second_frame.bind('<Motion>',self.th_posx_posy)
                
                self.win=self.my_canvas.create_window((0,0),window=self.second_frame,anchor='nw',width=round(0.6412*self.width_available)-17,height=round(0.82907*self.height_available_center)-17)
                
                
                self.list_wins_properties['width']=round(0.6412*self.width_available)-17
                self.list_wins_properties['height']=round(0.82907*self.height_available_center)-17
                
                # for i in range(0,100):
                #     Button(self.second_frame,text='button').grid(column=i,row=i)
                
                ## main screen now is the second_frame we will change width and height of it as the main win
                
                #################################### adding scroll bar to lists
                
                
                self.scrollbar_list_widgets = ttk.Scrollbar(self.main,orient=VERTICAL)
                self.scrollbar_list_widgets.place(x=round(0.1584*self.width_available),y=87,height=round(0.5477*self.height_available_left_right))
                self.listbox_widgets.config(yscrollcommand = self.scrollbar_list_widgets.set)
                self.scrollbar_list_widgets.config(command = self.listbox_widgets.yview)
                self.listbox_widgets.bind('<Double-Button-1>',self.AddWidget)
                
                self.scrollbar_list_widgets_on_win = ttk.Scrollbar(self.main,orient=VERTICAL)
                self.scrollbar_list_widgets_on_win.place(x=round(0.1584*self.width_available),y=87+round(0.5477*self.height_available_left_right)+15+25,height=round(0.45103*self.height_available_left_right))
                self.listbox_widgets_on_win.config(yscrollcommand = self.scrollbar_list_widgets_on_win.set)
                self.scrollbar_list_widgets_on_win.config(command = self.listbox_widgets_on_win.yview)
                self.listbox_widgets_on_win.bind('<<ListboxSelect>>',self.loading_properties)
                self.listbox_widgets_on_win.bind('<Delete>',self.DeleteWidget)
                
                
                self.scrollbar_list_wins = ttk.Scrollbar(self.main,orient=VERTICAL)
                self.scrollbar_list_wins.place(x=18+round(0.1584*self.width_available)+30+round(0.6412*self.width_available)+14+round(0.2003*self.width_available)-18,y=87+round(0.5477*self.height_available_left_right)+15+25,height=round(0.45103*self.height_available_left_right))
                self.listbox_wins.config(yscrollcommand = self.scrollbar_list_wins.set)
                self.scrollbar_list_wins.config(command = self.listbox_wins.yview)
                self.listbox_wins.bind('<Delete>',self.DeleteWin)
                #self.listbox_wins.bind('<Button-1>',self.properties_win)
                
                
                
            
                #self.main_frame_right.place(x=18+round(0.1584*self.width_available)+30+round(0.6412*self.width_available)+14,y=87,width=round(0.2003*self.width_available),height=round(0.5477*self.height_available_left_right))
                self.main_frame_right=Frame(self.main,bg=themes[self.Theme]['lists'])
                self.main_frame_right.place(x=18+round(0.1584*self.width_available)+30+round(0.6412*self.width_available)+14,y=87,width=round(0.2003*self.width_available),height=round(0.5477*self.height_available_left_right))
                
                self.my_canvas_right=Canvas(self.main_frame_right,scrollregion=(0,0,round(0.2003*self.width_available)-17,round(0.5477*self.height_available_left_right)-17),bg=themes[self.Theme]['lists'],highlightthickness=0)
                self.my_canvas_right.place(x=0,y=0,width=round(0.2003*self.width_available)-17,height=round(0.5477*self.height_available_left_right)-17)
                
                self.my_scrollbar_right=ttk.Scrollbar(self.main_frame_right,orient=VERTICAL,command=self.my_canvas_right.yview)
                self.my_scrollbar_right.pack(side=RIGHT,fill=Y)
                
                self.my_scrollbar2_right=ttk.Scrollbar(self.main_frame_right,orient=HORIZONTAL,command=self.my_canvas_right.xview)
                self.my_scrollbar2_right.pack(side=BOTTOM,fill=X)
                
                self.my_canvas_right.configure(yscrollcommand=self.my_scrollbar_right.set)
                self.my_canvas_right.configure(xscrollcommand=self.my_scrollbar2_right.set)
                
                self.second_frame_right=Frame(self.my_canvas_right,bg=themes[self.Theme]['lists'])
        
                self.win_right=self.my_canvas_right.create_window((0,0),window=self.second_frame_right,anchor='nw')
        
        
                
                #######################################################   head
                
                self.inner_distance=round((0.1584*self.width_available-152)/5)
        
                self.image_new_before=PhotoImage(master=self.main,file=r'icons\new_before.png')
                self.image_new_after=PhotoImage(master=self.main,file=r'icons\new_after.png')
                self.bt_new=Button(self.main,image=self.image_new_before,bg=themes[self.Theme]['head bar'],activebackground=themes[self.Theme]['head bar'],bd=0,relief='flat',command=self.bt_new_com)
                self.bt_new.bind('<Enter>',self.bt_new_enter)
                self.bt_new.bind('<Leave>',self.bt_new_leave)
                self.bt_new.place(x=18+self.inner_distance,y=2,width=34,height=34)
                
                self.image_open_before=PhotoImage(master=self.main,file=r'icons\open_before.png')
                self.image_open_after=PhotoImage(master=self.main,file=r'icons\open_after.png')
                self.bt_open=Button(self.main,image=self.image_open_before,bg=themes[self.Theme]['head bar'],activebackground=themes[self.Theme]['head bar'],bd=0,relief='flat',command=self.bt_openFprogram_com)
                self.bt_open.bind('<Enter>',self.bt_open_enter)
                self.bt_open.bind('<Leave>',self.bt_open_leave)
                self.bt_open.place(x=18+self.inner_distance*2+34,y=2,width=41,height=34)
                
                self.image_export_before=PhotoImage(master=self.main,file=r'icons\export_before.png')
                self.image_export_after=PhotoImage(master=self.main,file=r'icons\export_after.png')
                self.bt_export=Button(self.main,image=self.image_export_before,bg=themes[self.Theme]['head bar'],activebackground=themes[self.Theme]['head bar'],bd=0,relief='flat',command=self.bt_export_com)
                self.bt_export.bind('<Enter>',self.bt_export_enter)
                self.bt_export.bind('<Leave>',self.bt_export_leave)
                self.bt_export.place(x=18+self.inner_distance*3+34+41,y=2,width=31,height=34)
                
                self.image_run_before=PhotoImage(master=self.main,file=r'icons\run_before.png')
                self.image_run_after=PhotoImage(master=self.main,file=r'icons\run_after.png')
                self.bt_run=Button(self.main,image=self.image_run_before,bg=themes[self.Theme]['head bar'],activebackground=themes[self.Theme]['head bar'],bd=0,relief='flat',command=self.bt_run_com)
                self.bt_run.bind('<Enter>',self.bt_run_enter)
                self.bt_run.bind('<Leave>',self.bt_run_leave)
                self.bt_run.place(x=18+self.inner_distance*4+34+41+31,y=2,width=46,height=34)
                
                self.image_save_before=PhotoImage(master=self.main,file=r'icons\save_before.png')
                self.image_save_after=PhotoImage(master=self.main,file=r'icons\save_after.png')
                self.bt_save=Button(self.main,image=self.image_save_before,bg=themes[self.Theme]['head bar'],activebackground=themes[self.Theme]['head bar'],bd=0,relief='flat',command=self.save_win)
                self.bt_save.place(x=18+round(0.1584*self.width_available)+30,y=2,height=34,width=34)
                self.bt_save.bind('<Enter>',self.bt_save_enter)
                self.bt_save.bind('<Leave>',self.bt_save_leave)
                
                self.image_code_before=PhotoImage(master=self.main,file=r'icons\code_before.png')
                self.image_code_after=PhotoImage(master=self.main,file=r'icons\code_after.png')
                self.bt_code=Button(self.main,image=self.image_code_before,bg=themes[self.Theme]['head bar'],activebackground=themes[self.Theme]['head bar'],bd=0,relief='flat',command=self.bt_code_com)
                self.bt_code.place(x=18+round(0.1584*self.width_available)+85,y=2,height=34,width=35)
                self.bt_code.bind('<Enter>',self.bt_code_enter)
                self.bt_code.bind('<Leave>',self.bt_code_leave)
                
                self.ent_path_project=Entry(self.main,highlightthickness=1,bg=themes[self.Theme]['search ent bg'],highlightcolor=themes[self.Theme]['lists highlightcolor'],highlightbackground=themes[self.Theme]['lists highlightbackground'],bd=0,fg='white')
                self.ent_path_project.place(x=18+round(0.1584*self.width_available)+100+35,y=8,height=21,width=round(0.6412*self.width_available)-34-35-21-15)
                self.ent_path_project.insert(END,self.path_project)
                self.ent_path_project.config(state='disabled')
                
                self.ent_property=Entry(self.main,highlightthickness=1,bg=themes[self.Theme]['search ent bg'],highlightcolor=themes[self.Theme]['lists highlightcolor'],highlightbackground=themes[self.Theme]['lists highlightbackground'],bd=0,fg=themes[self.Theme]['other labels'])
                self.ent_property.place(x=18+round(0.1584*self.width_available)+30+round(0.6412*self.width_available)+14,y=8,height=21,width=round(0.2003*self.width_available))
                self.ent_property.bind('<Return>',self.set_property)
                
                self.list_nums=[]
                for widget in widgets:
                    self.list_nums.append(1)
                
                
                self.listbox_wins.insert(END,'self')
                
                
                
                
        
                self.menubar=Menu(self.main,background='red',fg='white')
                file=Menu(self.menubar,tearoff=0)
                file.add_command(label='New project',command=self.new_proj_com)
                file.add_command(label='Open project',command=self.bt_openFprogram_com)
                file.add_command(label='Save project',command=self.save_project_com)
                file.add_separator()
                file.add_command(label='Exit',command=self.ExitFcn)
                
                self.menubar.add_cascade(label='File',menu=file)
                
                self.edit=Menu(self.menubar,tearoff=0)
                self.edit.add_command(label='Copy widget',command=self.ControlC)
                self.edit.add_command(label='Paste widget',command=self.ControlV)
                self.edit.add_command(label='Send to back',command=self.SendBack,accelerator= "Ctrl+B")
                self.edit.add_command(label='Send to front',command=self.SendFront,accelerator= "Ctrl+F")
                self.edit.add_command(label='Bring to back',command=self.BringBack,accelerator= "Ctrl+Q")
                self.edit.add_command(label='Bring to front',command=self.BringFront,accelerator= "Ctrl+W")
                
                self.edit.entryconfig('Copy widget',state='disabled')
                self.edit.entryconfig('Send to back',state='disabled')
                self.edit.entryconfig('Send to front',state='disabled')
                self.edit.entryconfig('Bring to back',state='disabled')
                self.edit.entryconfig('Bring to front',state='disabled')
                
                self.edit.entryconfig('Paste widget',state='disabled')
                self.menubar.add_cascade(label='Edit',menu=self.edit)
                
                
                self.window=Menu(self.menubar,tearoff=0)
                self.window.add_command(label='Add new window',command=self.add_win)
                self.window.add_command(label='Add external window',command=self.add_external_win)
                self.window.add_command(label='Save current window',command=self.save_win)
                self.window.add_command(label='Show code',command=self.ShowCode)
                self.window.add_command(label='Show design',command=self.ShowDesign)
                self.window.entryconfig('Show design',state='disabled')
                self.window.add_separator()
                self.window.add_command(label='Close current window',command=self.bt_exit_win_com)
                self.menubar.add_cascade(label='Window',menu=self.window)
                
                self.debug=Menu(self.menubar,tearoff=0)
                self.debug.add_command(label='Export current window',command=self.bt_export_com)
                self.debug.add_command(label='Run project',command=self.bt_run_com)
                self.debug.add_command(label='Run current window',command=self.run_current_win)
                self.debug.add_command(label='Clear consol',command=self.clear_consol)
                self.debug.add_separator()
                self.debug.add_command(label='Stop running',command=self.stop_running)
                
                self.menubar.add_cascade(label='Debug',menu=self.debug)
                self.debug.entryconfig('Stop running',state='disabled')
                
                self.help=Menu(self.menubar,tearoff=0)
                self.help.add_command(label='Program info',command=self.ShowProgramInfo)
                self.menubar.add_cascade(label='Help',menu=self.help)
                
                
                
                self.main.configure(menu=self.menubar)
                
                ################################################ pop up menu right click
                self.my_menu_design=Menu(self.second_frame,tearoff=False)
                self.my_menu_design.add_command(label='Refresh',command=self.Refresh_com)
                self.my_menu_design.add_command(label='Show code',command=self.ShowCode)
                self.my_menu_design.add_command(label='Paste',command=self.ControlV)
                self.my_menu_design.entryconfig('Paste',state='disabled')
                ################################################ pop up menu right click widget
                self.my_menu_widget=Menu(self.second_frame,tearoff=False)
                self.my_menu_widget.add_command(label='Refresh',command=self.Refresh_com)
                self.my_menu_widget.add_command(label='Show code',command=self.ShowCode)
                self.my_menu_widget.add_command(label='Send to back',command=self.SendBack,accelerator= "Ctrl+B")
                self.my_menu_widget.add_command(label='Send to front',command=self.SendFront,accelerator= "Ctrl+F")
                self.my_menu_widget.add_command(label='Bring to back',command=self.BringBack,accelerator= "Ctrl+Q")
                self.my_menu_widget.add_command(label='Bring to front',command=self.BringFront,accelerator= "Ctrl+W")
                self.my_menu_widget.add_command(label='Copy',command=self.ControlC)
                self.my_menu_widget.add_command(label='Paste',command=self.ControlV)
                self.my_menu_widget.entryconfig('Paste',state='disabled')
                self.my_menu_widget.add_command(label='Delete',command=self.DeleteWidget)
                
                
                
                ################################## text to code
                
                self.text = Text(self.main_frame,bg=themes[self.Theme]["code bg"],fg=themes[self.Theme]["other labels"],font=('Consolas',12),undo=True)
                self.text.bind('<Button-3>',self.RightClickText)
                #self.text.place(x=0,y=0,width=round(0.6412*self.width_available)-17,height=round(0.82907*self.height_available_center)-17)
                self.text.tag_config("purple",foreground="#c670e0")
                self.text.tag_config("red",foreground="#ee5c51")
                self.text.tag_config("orange",foreground="#fa9b4e")
                self.text.tag_config("yellow",foreground="#faed5c")
                self.text.tag_config("green",foreground="#82e686")
                self.text.tag_config("cyan",foreground="#57d6e4")
                self.text.tag_config("gray",foreground="#999999")
                
                self.text.bind('<KeyRelease>', self.CorrectColors)
                self.text.bind('<Shift-">', self.qoutes)
                self.text.bind('<Tab>', self.tab)
                self.text.bind('<Shift-Tab>', self.ShiftTab)
                self.text.bind('<Return>',self.EnterClick)
                self.text.bind('<Triple-1>',self.UpdateColors)
                self.text.bind('<Control-v>',self.paste)
                
                self.list_purple=['import','if','elif','else','in','is','and','or','not','def','for','while','pass','class','try','except','return','from']
                self.list_red=['self']
                self.list_orange=['len','print','dict','list','set','sorted','True','False','range','None','super']
                self.list_yellow=['integers']
                self.list_green=['strings']
                self.list_cyan=['def','class']
                
                self.text.tag_configure("current_line", background=themes[self.Theme]["highlight code"])
                
                self.UpdateWidgets()
                self.ConsolLight()
                ################################################# pop up menu2
                self.my_menu_text=Menu(self.text,tearoff=False)
                self.my_menu_text.add_command(label='Show design',command=self.ShowDesign)
                
                if self.open_file:
                    self.open_com(self.path_project)
                    self.open_win_th(self.pointer_win)
                    td=''
                    with open(self.path_project+'\\'+self.proj_name+'.py','r') as f1:
                        td=f1.read()
                    self.text.insert('1.0',td)
                    
                else:
                    self.listbox_widgets_on_win.insert(0,'self')
                    
                    self.text.insert('1.0','from tkinter import *\n')
                    self.text.insert('2.0','from tkinter import ttk\n')
                    
                    self.text.insert('3.0','from self_code import SelfCode\n')
                    self.text.insert('4.0',f'class {self.proj_name}(SelfCode):\n')
                    self.text.insert('5.0','    def __init__(self):\n')
                    self.text.insert('6.0','        super().__init__()\n\n\n\n\n\n')
                    self.text.insert('12.0',f'a={self.proj_name}()\n')
                    self.text.insert('13.0','a.mainloop()\n')
                    
                self.UpdateColors(None)
        except:
            pass
    def ShowProgramInfo(self):
        self.ProgramInfo()
        #self.win1.deiconify()
    def typing_in_ent_property(self,e):
        pass
    def set_property(self,e):
        try:
            property1=self.ent_property.get()
            if self.selected!=() and property1!='':
                if self.selected!=(0,):
                    value=self.selected[0]-1
                    pro,val=property1.split(':')
                    if pro in list(self.list_widgets_on_wins_properties[value].keys()):
                        index=list(self.list_widgets_on_wins_properties[value].keys()).index(pro)
                        self.list_inputs[index].delete(0,END)
                        self.list_inputs[index].insert(END,val)
                        self.ent_property.delete(0,END)
                else:
                    pro,val=property1.split(':')
                    if pro in list(self.list_wins_properties.keys()):
                        index=list(self.list_wins_properties.keys()).index(pro)
                        self.list_inputs[index].delete(0,END)
                        self.list_inputs[index].insert(END,val)
                        self.ent_property.delete(0,END)
        except:
            pass
   
    def ProgramInfo(self):
        try:
            ##########################3 designed using the current program
            self.win1=Toplevel()
            #self.win1.withdraw()
            os.chdir(direct)
            self.win1.title('Program Info')
            self.win1.iconbitmap(r'icons\icon.ico')
            self.ws = self.win1.winfo_screenwidth()
            pos_x=round((self.ws-630)/2)
            self.hs = self.win1.winfo_screenheight()
            pos_y=round((self.hs-250)/2)
            self.win1.geometry("630x250+"+str(pos_x)+"+"+str(pos_y))
            self.win1.config(bg="#343333")
            self.win1.attributes("-topmost",0)
            self.win1.overrideredirect(0)
            self.image_Label1=PhotoImage(master=self.win1,file=r"icons\logo_program.png")
            self.image_Label18=PhotoImage(master=self.win1,file=r"icons\company_logo.png")
            self.Label2=Label(self.win1,
                    text="TK Design",
                    bg="#343333",
                    fg="white",
                    font=("arial",35),
                    )
            self.Label2.place(x=221,y=20,width=264,height=57)
            self.Label2_copy_copy=Label(self.win1,
                    text="ELPRINCE",
                    bg="#343333",
                    fg="#c1212c",
                    font=("arial",20),
                    )
            self.Label2_copy_copy.place(x=292,y=85,width=150,height=42)
            self.Label1=Label(self.win1,
                    text="",
                    bg="#343333",
                    fg="black",
                    font=("arial",13),
                    image=self.image_Label1
                    )
            self.Label1.place(x=-1,y=16,width=226,height=206)
            self.Label2_copy=Label(self.win1,
                    text="v1",
                    bg="#343333",
                    fg="white",
                    font=("arial",18),
                    )
            self.Label2_copy.place(x=461,y=25,width=38,height=38)
            
            self.Label18=Label(self.win1,
                    text="",
                    bg="#343333",
                    fg="black",
                    font=("arial",13),
                    image=self.image_Label18
                    )
            self.Label18.place(x=243,y=85,width=54,height=42)
            
            self.Label19=Label(self.win1,
                    text="for support: ",
                    bg="#343333",
                    fg="white",
                    font=("arial",14,'bold'),
                    
                    )
            self.Label19.place(x=243,y=130)
            
            self.Label20=Label(self.win1,
                    text="https://www.facebook.com/Moustafa162/",
                    bg="#343333",
                    fg="cyan",
                    font=("arial",14,'bold'),
                    
                    )
            self.Label20.place(x=243,y=170)
            
            self.Label21=Label(self.win1,
                    text="https://elprince162.blogspot.com/",
                    bg="#343333",
                    fg="cyan",
                    font=("arial",14,'bold'),
                    
                    )
            self.Label21.place(x=243,y=210)
            
        except:
            pass
    def BringBack(self,e=None):
        try:
            masters=self.listbox_widgets_on_win.get(0,END)
            if self.selected!=(0,):
                value_selected=self.selected[0]-1
                if value_selected!=0:
                    self.list_widgets_on_wins=self.SwapElements(self.list_widgets_on_wins,value_selected,0)
                    self.list_widgets_on_wins_Errors=self.SwapElements(self.list_widgets_on_wins_Errors,value_selected,0)
                    
                    self.list_widgets_on_wins_properties=self.SwapElements(self.list_widgets_on_wins_properties,value_selected,0)
                    self.list_frames_on_wins=self.SwapElements(self.list_frames_on_wins,value_selected,0)
                    
                    
                    self.save_win()
                    self.open_win_th(self.pointer_win)
        except:
            pass
    def BringFront(self,e=None):
        try:
            masters=self.listbox_widgets_on_win.get(0,END)
            last_widget_index=len(masters)-2
            if self.selected!=(0,):
                value_selected=self.selected[0]-1
                if value_selected!=last_widget_index:
                    self.list_widgets_on_wins=self.SwapElements(self.list_widgets_on_wins,value_selected,last_widget_index)
                    self.list_widgets_on_wins_Errors=self.SwapElements(self.list_widgets_on_wins_Errors,value_selected,last_widget_index)
                    
                    self.list_widgets_on_wins_properties=self.SwapElements(self.list_widgets_on_wins_properties,value_selected,last_widget_index)
                    self.list_frames_on_wins=self.SwapElements(self.list_frames_on_wins,value_selected,last_widget_index)
                    
                    
                    
                    self.save_win()
                    self.open_win_th(self.pointer_win)
        except:
            pass
    def SendBack(self,e=None):
        try:
            masters=self.listbox_widgets_on_win.get(0,END)
            if self.selected!=(0,):
                value_selected=self.selected[0]-1
                if value_selected!=0:
                    self.list_widgets_on_wins=self.SwapElements(self.list_widgets_on_wins,value_selected,value_selected-1)
                    self.list_widgets_on_wins_Errors=self.SwapElements(self.list_widgets_on_wins_Errors,value_selected,value_selected-1)
                    
                    self.list_widgets_on_wins_properties=self.SwapElements(self.list_widgets_on_wins_properties,value_selected,value_selected-1)
                    self.list_frames_on_wins=self.SwapElements(self.list_frames_on_wins,value_selected,value_selected-1)
                    
                    
                    self.save_win()
                    self.open_win_th(self.pointer_win)
        except:
            pass
                
    def Refresh_com(self):
        try:
            
            self.save_win()
            self.open_win_th(self.pointer_win)
        except:
            pass
    def SwapElements(self,list1,index1,index2):
        try:
            temp=list1[index1]
            list1[index1]=list1[index2]
            list1[index2]=temp
            return list1
        except:
            pass
    def SendFront(self,e=None):
        try:
            self.selected=(self.selected[0]+1,)
            self.SendBack()
        except:
            pass
    def save_project_com(self):
        try:
            self.save_win()
            self.SaveProj()
        except:
            pass
    def bt_stop_running_com(self):
        try:
            if self.running==1:
                self.stop_running()
        except:
            pass
        
    def bt_save_enter(self,e):
        try:
            self.bt_save.config(image=self.image_save_after)
        except:
            pass
    def bt_save_leave(self,e):
        try:
            self.bt_save.config(image=self.image_save_before)
        except:
            pass
    def bt_code_enter(self,e):
        try:
            self.bt_code.config(image=self.image_code_after)
        except:
            pass
    def bt_code_leave(self,e):
        try:
            self.bt_code.config(image=self.image_code_before)
        except:
            pass
    def bt_code_com(self):
        try:
            if self.CodeHide==1:
                self.ShowCode()
            else:
                self.ShowDesign()
        except:
            pass
    def th_posx_posy(self,e):
        try:
            PlaceInfo=self.main_frame.place_info()
            if PlaceInfo!={}:
                if e.x_root>=18+round(0.1584*self.width_available)+30 and e.y_root>=130 and e.x_root-(18+round(0.1584*self.width_available)+30)<=int(PlaceInfo['width']) and e.y_root-130<=int(PlaceInfo['height']):
                    self.lbl_status.config(text=f'posx:{e.x_root-(18+round(0.1584*self.width_available)+30)}, posy:{e.y_root-130}')
        except:
            pass
        
    def new_proj_com(self):
        try:
            self.save_win()
            self.SaveProj()
            self.main.destroy()
            self.__init__()
        except:
            pass
    def bt_exit_win_com(self):
        try:
            self.save_win()
            self.lbl_filename.place_forget()
            self.lbl_filename_txt.place_forget()
            self.bt_exit_win.place_forget()
            self.main_frame.place_forget()
            self.WinHide=True
            self.window.entryconfig('Close current window',state='disabled')
        except:
            pass
    def bt_hide_consol_com(self):
        try:
            if self.CodeHide==1:
                if (not self.ConsolHide):
                    self.txt_consol.place_forget()
                    self.lbl_consol.place(x=18+round(0.1584*self.width_available)+30,y=87+round(0.82907*self.height_available_center)+13+25+round(0.16877*self.height_available_center)-25,height=25,width=round(0.6412*self.width_available))
                    self.bt_hide_consol.place(x=18+round(0.1584*self.width_available)+30+round(0.6412*self.width_available)-20,y=87+round(0.82907*self.height_available_center)+13+25+round(0.16877*self.height_available_center)-25,height=25,width=20)
                    self.bt_stop_running.place(x=18+round(0.1584*self.width_available)+30+round(0.6412*self.width_available)-40,y=87+round(0.82907*self.height_available_center)+13+25+round(0.16877*self.height_available_center)-20,height=15,width=15)
                
                    if not self.WinHide:
                        if self.win_height>=round(0.82907*self.height_available_center)+round(0.16877*self.height_available_center):
                            self.main_frame.place_configure(height=round(0.82907*self.height_available_center)+round(0.16877*self.height_available_center))
                            self.my_canvas.place_configure(height=round(0.82907*self.height_available_center)+round(0.16877*self.height_available_center)-17)
                            
                        elif round(0.82907*self.height_available_center)+round(0.16877*self.height_available_center)>self.win_height>=round(0.82907*self.height_available_center):
                            self.main_frame.place_configure(height=self.win_height+17)
                            self.my_canvas.place_configure(height=self.win_height)
                    self.ConsolHide=True
                else:
                    self.lbl_consol.place(x=18+round(0.1584*self.width_available)+30,y=87+round(0.82907*self.height_available_center)+13,height=25,width=round(0.6412*self.width_available))
                    self.txt_consol.place(x=18+round(0.1584*self.width_available)+30,y=87+round(0.82907*self.height_available_center)+13+25,width=round(0.6412*self.width_available),height=round(0.16877*self.height_available_center))
                    self.bt_hide_consol.place(x=18+round(0.1584*self.width_available)+30+round(0.6412*self.width_available)-20,y=87+round(0.82907*self.height_available_center)+13,height=25,width=20)
                    self.bt_stop_running.place(x=18+round(0.1584*self.width_available)+30+round(0.6412*self.width_available)-40,y=87+round(0.82907*self.height_available_center)+18,height=15,width=15)
                
                    if not self.WinHide:
                        if self.win_height>=round(0.82907*self.height_available_center):
                            self.main_frame.place_configure(height=round(0.82907*self.height_available_center))
                            self.my_canvas.place_configure(height=round(0.82907*self.height_available_center)-17)
                    self.ConsolHide=False
            else:
                if (not self.ConsolHide):
                    self.ConsolHide=True
                    self.txt_consol.place_forget()
                    self.lbl_consol.place(x=18+round(0.1584*self.width_available)+30,y=87+round(0.82907*self.height_available_center)+13+25+round(0.16877*self.height_available_center)-25,height=25,width=round(0.6412*self.width_available))
                    self.bt_hide_consol.place(x=18+round(0.1584*self.width_available)+30+round(0.6412*self.width_available)-20,y=87+round(0.82907*self.height_available_center)+13+25+round(0.16877*self.height_available_center)-25,height=25,width=20)
                    self.bt_stop_running.place(x=18+round(0.1584*self.width_available)+30+round(0.6412*self.width_available)-40,y=87+round(0.82907*self.height_available_center)+13+25+round(0.16877*self.height_available_center)-20,height=15,width=15)
                
                else:
                    self.ConsolHide=False
                    self.lbl_consol.place(x=18+round(0.1584*self.width_available)+30,y=87+round(0.82907*self.height_available_center)+13,height=25,width=round(0.6412*self.width_available))
                    self.txt_consol.place(x=18+round(0.1584*self.width_available)+30,y=87+round(0.82907*self.height_available_center)+13+25,width=round(0.6412*self.width_available),height=round(0.16877*self.height_available_center))
                    self.bt_hide_consol.place(x=18+round(0.1584*self.width_available)+30+round(0.6412*self.width_available)-20,y=87+round(0.82907*self.height_available_center)+13,height=25,width=20)
                    self.bt_stop_running.place(x=18+round(0.1584*self.width_available)+30+round(0.6412*self.width_available)-40,y=87+round(0.82907*self.height_available_center)+18,height=15,width=15)
        except:
            pass
    
    def UpdateWidgets(self):
        try:
            for i in widgets:
                self.listbox_widgets.insert(END,i)
        except:
            pass
    def bt_new_enter(self,e):
        try:
            self.bt_new.config(image=self.image_new_after)
        except:
            pass
    def bt_new_leave(self,e):
        try:
            self.bt_new.config(image=self.image_new_before)
        except:
            pass
    def bt_new_com(self):
        try:
            self.add_win()
        except:
            pass
    def bt_openFinit_com(self,e=None):
        try:
            path=filedialog.askdirectory()
            if path:
                there_project=0
                list_files=os.listdir(path)
                for file in list_files:
                    if '.config' in file:
                        self.ent_ProjName.delete(0,END)
                        self.ent_ProjName.insert(END,file.replace('.config',''))
                        there_project=1
                        break
                self.ent_path.delete(0,END)
                self.ent_path.insert(END,path)
                if there_project==1:
                    self.open_file=1
                else:
                    self.open_file=0
        except:
            pass
    def bt_openFprogram_com(self):
        try:
            path=filedialog.askdirectory()
            if path:
                self.save_win()
                self.SaveProj()
                self.ReInitParams()
                self.path_project=path
                self.ent_path_project.config(state='normal')
                self.ent_path_project.delete(0,END)
                self.ent_path_project.insert(END,self.path_project)
                self.ent_path_project.config(state='disabled')
                self.open_com(path)
                self.open_win_th(self.pointer_win)
        except:
            pass
    def open_com(self,path):
        # f1.write(repr(self.listbox_wins.get(0,END))+'\n')
        # f1.write(str(self.num_inserted_win)+'\n')
        # f1.write(str(self.pointer_win)+'\n')
        # f1.write(str(self.proj_name))
        #literal_eval
        try:
            list_files=os.listdir(path)
            index=0
            for file in list_files:
                if '.config' in file:
                    break
                index+=1
            
            if index!=len(list_files):
                path_proj=list_files[index]
                x=''
                with open(path+'\\'+path_proj,'r') as f1:
                    x=f1.read()
                list_lines=x.splitlines()
                self.listbox_wins.delete(0,END)
                wins=literal_eval(list_lines[0])
                
                for win in wins:
                    self.listbox_wins.insert(END,win)
                self.num_inserted_win=int(literal_eval(list_lines[1]))
                self.pointer_win=int(literal_eval(list_lines[2]))
                self.proj_name=str(list_lines[3])
        except:
            pass
    def DoubleClickOpenWin(self,e):
        try:
            self.save_win()
            self.open_win_th(None)
        except:
            pass
    def SortingWidgets(self,UnorderedList,args):
        try:
            OrderedList=UnorderedList.copy()
            args_copy=args.copy()
            for index1 in range(0,len(OrderedList)):
                for index2 in range(0,len(OrderedList)):
                    if len(str(OrderedList[index1]).split('.'))<len(str(OrderedList[index2]).split('.')):
                        temp=OrderedList[index1]
                        OrderedList[index1]=OrderedList[index2]
                        OrderedList[index2]=temp
                        for index in range(0,len(args_copy)):
                            temp=args_copy[index][index1]
                            args_copy[index][index1]=args_copy[index][index2]
                            args_copy[index][index2]=temp
                        
            return OrderedList,args_copy
        except:
            pass
    def open_win_th(self,e,win=None):
        try:
            self.open_win(e,win)
        except:
            pass
        # th=Thread(target=self.open_win,args=(e,win))
        # th.start()
    def open_win(self,e,win=None):
        try:
            #self.path_project
            selected=self.listbox_wins.curselection()
            if str(e).isnumeric():
                selected=(e,)
            if selected:
                self.lbl_status.config(text='loading...')
                value=selected[0]
                self.ReInitParams()
                self.main_frame.place_forget()
                self.pointer_win=value
                wins=self.listbox_wins.get(0,END)
                
                current_win=wins[self.pointer_win]
                
                self.listbox_widgets_on_win.insert(END,current_win)
                self.lbl_filename_txt.config(text=current_win)
                self.list_wins_properties['id']=current_win
                if win==None:
                    win=current_win
                
                
                txt=''
                if os.path.exists(self.path_project+'\\'+win+'.uiELPRINCE'):
                    with open(self.path_project+'\\'+win+'.uiELPRINCE','r') as f1:
                        txt=f1.read()
                    list_lines=txt.splitlines()
                    widget_on_wins=literal_eval(list_lines[2])
                    list_errors=literal_eval(list_lines[4])
                    self.Error_win=int(literal_eval(list_lines[5]))
                    widgets_types=literal_eval(list_lines[6])
                    
                    
                    widgets_properties=literal_eval(list_lines[1])
                    self.list_wins_properties=literal_eval(list_lines[0])
                    nums_copy=literal_eval(list_lines[3])
                    self.list_wins_properties['id']=current_win
                    
                    ################################################# sorting widgets:
                    
                    
                    
                    
                    
                    ####################################################################
                    index=0
                    for widget in widgets_types:
                        #AddWidget
                        var=-1
                        if widget=='Button':
                            var=0
                        elif widget=='Entry':
                            var=1
                        elif widget=='Text':
                            var=2
                        elif widget=='Radiobutton':
                            var=3
                        elif widget=='Checkbutton':
                            var=4
                        elif widget=='Canvas':
                            var=5
                        elif widget=='Label':
                            var=6
                        elif widget=='Listbox':
                            var=7
                        elif widget=='Scrollbar':
                            var=8
                        elif widget=='Combobox':
                            var=9
                        elif widget=='Treeview':
                            var=10
                        elif widget=='Frame':
                            var=11
                        
                        self.AddWidget(var,0)
                        index+=1
                    self.list_nums=nums_copy
                    index=0
                    self.list_widgets_on_wins_Errors=list_errors
                    
                    for widget in widgets_types:
                        # self.loading_properties(index+1)
                        # self.list_inputs[2].delete(0,END)
                        # self.list_inputs[2].insert(END,widgets_properties_copy[index]['master'])
                        # self.click_enter(index+1)
                        self.list_widgets_on_wins_properties[index]=widgets_properties[index].copy()
                        valid=self.CheckId(self.list_widgets_on_wins_properties[index]['id'])
                        self.listbox_widgets_on_win.delete(index+1)
                        if valid:
                            self.listbox_widgets_on_win.insert(index+1,self.list_widgets_on_wins_properties[index]['id'])
                        else:
                            self.listbox_widgets_on_win.insert(index+1,widget_on_wins[index])
                        index+=1
                    index=0
                    for widget in widgets_types:
                        master=self.list_widgets_on_wins_properties[index]['master']
                        
                        self.list_widgets_on_wins_properties[index]['master']=current_win
                        if self.list_widgets_on_wins_properties[index]['master']!=current_win:
                            if self.list_widgets_on_wins_properties[index]['master'] in current_win and '_copy' in current_win:
                                master=current_win
                        
                        
                        self.loading_properties(index+1,0)
                        self.list_inputs[2].delete(0,END)
                        self.list_inputs[2].insert(END,master)
                        
                        self.click_enter(index+1)
                        #self.ClickEnterTotCom(index+1)
                        
                        index+=1
                    index=0
                    # for widget in widgets_properties:
                        
                    #     self.loading_properties(index+1)
                    #     self.click_enter(index+1)
                        
                    #     index+=1
                        ###########################  new code
                    # index=0
                    # for widget in widgets_types:
                    #     print(widget)
                    #     print(widgets_properties[index]['master'])
                    #     self.list_widgets_on_wins_properties[index]=widgets_properties[index]
                    #     self.loading_properties(index+1)
                    #     self.click_enter(index+1)
                    #     index+=1
                        ##########################
                        # if index_master!=0:
                        #     ## create the same widget in the new master
                        #     self.num_widget=var
                        #     self.index_RemovedWidget=value
                        #     self.selected_master=self.list_widgets_on_wins[index_master-1]
                        #     self.list_frames_on_wins[value].place_forget()
                        #     self.list_frames_on_wins[value].pack_forget()
                        #     self.AddWidget(None)
                        #     #self.masters_widgets.append({test_value:{self.listbox_widgets_on_win[value+1]}})
                        # else:
                        #     self.list_frames_on_wins[value].place_forget()
                        #     self.list_frames_on_wins[value].pack_forget()
                        #     self.list_widgets_on_wins.pop(value)
                        #     self.list_frames_on_wins.pop(value)
                        #     self.list_widgets_on_wins_Errors.pop(value)
                        #     self.list_widgets_on_wins_properties.pop(value)
                        #     self.listbox_widgets_on_win.delete(value+1)
                        #     self.AddWidget(var)
                        #     value=-1
                        ######################
                #self.ClickEnterTotCom(0)
                self.ShowDesign()
                self.lbl_status.config(text='opened!')
            #literal_eval
            # f1.write(repr(self.list_wins_properties)+'\n'+repr(self.list_widgets_on_wins_properties))
            # f1.write('\n'+repr(self.listbox_widgets_on_win.get(0,END)))
            # f1.write('\n'+repr(self.list_nums))
            # f1.write('\n'+repr(self.list_widgets_on_wins_Errors))
            # f1.write('\n'+str(self.Error_win))
            # f1.write('\n'+str(widgets_types))
        except:
            pass
    def bt_open_enter(self,e):
        try:
            self.bt_open.config(image=self.image_open_after)
        except:
            pass
    def bt_open_leave(self,e):
        try:
            self.bt_open.config(image=self.image_open_before)
        except:
            pass
    def bt_export_enter(self,e):
        try:
            self.bt_export.config(image=self.image_export_after)
        except:
            pass
    def bt_export_leave(self,e):
        try:
            self.bt_export.config(image=self.image_export_before)
        except:
            pass
    def bt_export_com(self):
        try:
            if any(self.list_widgets_on_wins_Errors) or self.Error_win:
                msgbox=messagebox.showinfo("Error!","Check all Errors in the program!")
            else:
                list_wins=list(self.listbox_wins.get(0,END))
                td=self.text.get('1.0',END)
                with open(self.path_project+'\\'+self.proj_name+'.py','w') as f1:
                    f1.write(td)
                with open(self.path_project+'\\'+list_wins[self.pointer_win]+'_code.py','w') as f1:
                    if list_wins[self.pointer_win]=='self':
                        f1.write('from tkinter import *')
                        f1.write('\nfrom tkinter import ttk')
                        f1.write('\nclass SelfCode(Tk):')
                        f1.write('\n    def __init__(self):')
                        f1.write('\n        Tk.__init__(self)')
                        f1.write(f'\n        self.title("{self.list_wins_properties["title"]}")')
                        if self.list_wins_properties['icon']!='None':
                            f1.write(f'\n        self.iconbitmap(r"{self.list_wins_properties["icon"]}")')
                        if self.list_wins_properties['pos_x']=='center' and self.list_wins_properties['pos_y']=='center':
                            f1.write('\n        self.ws = self.winfo_screenwidth()')
                            f1.write(f'\n        pos_x=round((self.ws-{int(self.list_wins_properties["width"])})/2)')
                            f1.write('\n        self.hs = self.winfo_screenheight()')
                            f1.write(f'\n        pos_y=round((self.hs-{int(self.list_wins_properties["height"])})/2)')
                            f1.write(f'\n        self.geometry("{int(self.list_wins_properties["width"])}x{int(self.list_wins_properties["height"])}+"+str(pos_x)+"+"+str(pos_y))')
                        elif self.list_wins_properties['pos_x']=='center' and self.list_wins_properties['pos_y']!='center':
                            f1.write('\n        self.ws = self.winfo_screenwidth()')
                            f1.write(f'\n        pos_x=round((self.ws-{int(self.list_wins_properties["width"])})/2)')
                            f1.write(f'\n        self.geometry("{int(self.list_wins_properties["width"])}x{int(self.list_wins_properties["height"])}+"+str(pos_x)+"+{str(self.list_wins_properties["pos_y"])}")')
                        elif self.list_wins_properties['pos_x']!='center' and self.list_wins_properties['pos_y']=='center':
                            f1.write('\n        self.hs = self.winfo_screenheight()')
                            f1.write(f'\n        pos_y=round((self.hs-{int(self.list_wins_properties["height"])})/2)')
                            f1.write(f'\n        self.geometry("{int(self.list_wins_properties["width"])}x{int(self.list_wins_properties["height"])}+{int(self.list_wins_properties["pos_x"])}+"+str(pos_y))')
                        else:
                            f1.write(f'\n        self.geometry("{int(self.list_wins_properties["width"])}x{int(self.list_wins_properties["height"])}+{int(self.list_wins_properties["pos_x"])}+{int(self.list_wins_properties["pos_y"])}")')
                        f1.write(f'\n        self.config(bg="{self.list_wins_properties["bg"]}")')
                        
                        f1.write(f'\n        self.attributes("-topmost",{int(self.list_wins_properties["topmost"])})')
                        f1.write(f'\n        self.overrideredirect({int(self.list_wins_properties["overrideredirect"])})')
                    else:
                        f1.write('from tkinter import *')
                        f1.write('\nfrom tkinter import ttk')
                        f1.write(f'\nclass {list_wins[self.pointer_win].capitalize()}Code():')
                        f1.write(f'\n    def {list_wins[self.pointer_win]}_fcn(self):')
                        f1.write(f'\n        self.{list_wins[self.pointer_win]}=Toplevel()')
                        f1.write(f'\n        self.{list_wins[self.pointer_win]}.title("{self.list_wins_properties["title"]}")')
                        if self.list_wins_properties['icon']!='None':
                            f1.write(f'\n        self.{list_wins[self.pointer_win]}.iconbitmap(r"{self.list_wins_properties["icon"]}")')
                        if self.list_wins_properties['pos_x']=='center' and self.list_wins_properties['pos_y']=='center':
                            f1.write(f'\n        self.ws = self.{list_wins[self.pointer_win]}.winfo_screenwidth()')
                            f1.write(f'\n        pos_x=round((self.ws-{int(self.list_wins_properties["width"])})/2)')
                            f1.write(f'\n        self.hs = self.{list_wins[self.pointer_win]}.winfo_screenheight()')
                            f1.write(f'\n        pos_y=round((self.hs-{int(self.list_wins_properties["height"])})/2)')
                            f1.write(f'\n        self.{list_wins[self.pointer_win]}.geometry("{int(self.list_wins_properties["width"])}x{int(self.list_wins_properties["height"])}+"+str(pos_x)+"+"+str(pos_y))')
                        elif self.list_wins_properties['pos_x']=='center' and self.list_wins_properties['pos_y']!='center':
                            f1.write(f'\n        self.ws = self.{list_wins[self.pointer_win]}.winfo_screenwidth()')
                            f1.write(f'\n        pos_x=round((self.ws-{int(self.list_wins_properties["width"])})/2)')
                            f1.write(f'\n        self.{list_wins[self.pointer_win]}.geometry("{int(self.list_wins_properties["width"])}x{int(self.list_wins_properties["height"])}+"+str(pos_x)+"+{str(self.list_wins_properties["pos_y"])}")')
                        elif self.list_wins_properties['pos_x']!='center' and self.list_wins_properties['pos_y']=='center':
                            f1.write(f'\n        self.hs = self.{list_wins[self.pointer_win]}.winfo_screenheight()')
                            f1.write(f'\n        pos_y=round((self.hs-{int(self.list_wins_properties["height"])})/2)')
                            f1.write(f'\n        self.{list_wins[self.pointer_win]}.geometry("{int(self.list_wins_properties["width"])}x{int(self.list_wins_properties["height"])}+{int(self.list_wins_properties["pos_x"])}+"+str(pos_y))')
                        else:
                            f1.write(f'\n        self.{list_wins[self.pointer_win]}.geometry("{int(self.list_wins_properties["width"])}x{int(self.list_wins_properties["height"])}+{int(self.list_wins_properties["pos_x"])}+{int(self.list_wins_properties["pos_y"])}")')
                        f1.write(f'\n        self.{list_wins[self.pointer_win]}.config(bg="{self.list_wins_properties["bg"]}")')
                        f1.write(f'\n        self.{list_wins[self.pointer_win]}.attributes("-topmost",{int(self.list_wins_properties["topmost"])})')
                        f1.write(f'\n        self.{list_wins[self.pointer_win]}.overrideredirect({int(self.list_wins_properties["overrideredirect"])})')
                    ################ 
                    
                    ### sorting widgets 
                    temp_list_widgets_on_wins_properties=self.list_widgets_on_wins_properties.copy()
                    #temp_list_widgets_on_wins,args=self.SortingWidgets(self.list_widgets_on_wins,[temp_list_widgets_on_wins_properties])
                    #temp_list_widgets_on_wins_properties=args[0]
                    temp_list_widgets_on_wins=self.list_widgets_on_wins
                    
                        
                    # print(temp_list_widgets_on_wins)
                    # print(temp_list_widgets_on_wins_properties)
                    ######################################################3
                    
                    index=0
                    for widget in temp_list_widgets_on_wins_properties:
                        
                        master='self'
                        if self.list_wins_properties['id']!='self':
                            master=self.list_wins_properties['id']
                        
                        if widget['master']!=master:
                            master='self.'+temp_list_widgets_on_wins_properties[index]['master']
                        else:
                            if master==self.list_wins_properties['id'] and master!='self':
                                master='self.'+master
                        
                        if type(temp_list_widgets_on_wins[index]) is Button:
                            if widget["image"]!='None':
                                f1.write(f'\n        self.image_{widget["id"]}=PhotoImage(master={master},file=r"{widget["image"]}")')
                            f1.write(f'\n        self.{widget["id"]}=Button({master},')
                            f1.write(f'\n                text="{widget["text"]}",')
                            f1.write(f'\n                bg="{widget["bg"]}",')
                            f1.write(f'\n                fg="{widget["fg"]}",')
                            f1.write(f'\n                font=("{widget["font family"]}",{int(widget["font size"])}),')
                            f1.write(f'\n                bd={int(widget["bd"])},')
                            if self.CheckNone(widget["highlightcolor"])==None:
                                f1.write(f'\n                highlightcolor=None,')
                            else:
                                f1.write(f'\n                highlightcolor="{widget["highlightcolor"]}",')
                            if self.CheckNone(widget["highlightbackground"])==None:
                                f1.write(f'\n                highlightbackground=None,')
                            else:
                                f1.write(f'\n                highlightbackground="{widget["highlightbackground"]}",')
                            if self.CheckNone(widget["activebackground"])==None:
                                f1.write(f'\n                activebackground=None,')
                            else:
                                f1.write(f'\n                activebackground="{widget["activebackground"]}",')
                            if self.CheckNone(widget["activeforeground"])==None:
                                f1.write(f'\n                activeforeground=None,')
                            else:
                                f1.write(f'\n                activeforeground="{widget["activeforeground"]}",')
                            f1.write(f'\n                relief="{widget["relief"]}",')
                            
                            
                            if widget["image"]!='None':
                                f1.write(f'\n                image=self.image_{widget["id"]}')
                            f1.write(f'\n                )')
                            
                            
                        elif type(temp_list_widgets_on_wins[index]) is Entry:
                            f1.write(f'\n        self.{widget["id"]}=Entry({master},')
                            f1.write(f'\n                bg="{widget["bg"]}",')
                            f1.write(f'\n                fg="{widget["fg"]}",')
                            f1.write(f'\n                font=("{widget["font family"]}",{int(widget["font size"])}),')
                            f1.write(f'\n                bd={int(widget["bd"])},')
                            if self.CheckNone(widget["highlightcolor"])==None:
                                f1.write(f'\n                highlightcolor=None,')
                            else:
                                f1.write(f'\n                highlightcolor="{widget["highlightcolor"]}",')
                            if self.CheckNone(widget["highlightbackground"])==None:
                                f1.write(f'\n                highlightbackground=None,')
                            else:
                                f1.write(f'\n                highlightbackground="{widget["highlightbackground"]}",')
                            f1.write(f'\n                highlightthickness={int(widget["highlightthickness"])},')
                            if self.CheckNone(widget["show"])==None:
                                f1.write(f'\n                show=None,')
                            else:
                                f1.write(f'\n                show="{widget["show"]}",')
                            f1.write(f'\n                )')
                            
                        elif type(temp_list_widgets_on_wins[index]) is Label:
                            if widget["image"]!='None':
                                f1.write(f'\n        self.image_{widget["id"]}=PhotoImage(master={master},file=r"{widget["image"]}")')
                            f1.write(f'\n        self.{widget["id"]}=Label({master},')
                            f1.write(f'\n                text="{widget["text"]}",')
                            f1.write(f'\n                bg="{widget["bg"]}",')
                            f1.write(f'\n                fg="{widget["fg"]}",')
                            f1.write(f'\n                font=("{widget["font family"]}",{int(widget["font size"])}),')
                            if widget["image"]!='None':
                                f1.write(f'\n                image=self.image_{widget["id"]}')
                            f1.write(f'\n                )')
                        elif type(temp_list_widgets_on_wins[index]) is Listbox:
                            f1.write(f'\n        self.{widget["id"]}=Listbox({master},')
                            f1.write(f'\n                bg="{widget["bg"]}",')
                            f1.write(f'\n                fg="{widget["fg"]}",')
                            f1.write(f'\n                font=("{widget["font family"]}",{int(widget["font size"])}),')
                            f1.write(f'\n                bd={int(widget["bd"])},')
                            if self.CheckNone(widget["highlightcolor"])==None:
                                f1.write(f'\n                highlightcolor=None,')
                            else:
                                f1.write(f'\n                highlightcolor="{widget["highlightcolor"]}",')
                            if self.CheckNone(widget["highlightbackground"])==None:
                                f1.write(f'\n                highlightbackground=None,')
                            else:
                                f1.write(f'\n                highlightbackground="{widget["highlightbackground"]}",')
                            f1.write(f'\n                )')
                        elif type(temp_list_widgets_on_wins[index]) is Text:
                            f1.write(f'\n        self.{widget["id"]}=Text({master},')
                            f1.write(f'\n                bg="{widget["bg"]}",')
                            f1.write(f'\n                fg="{widget["fg"]}",')
                            f1.write(f'\n                font=("{widget["font family"]}",{int(widget["font size"])}),')
                            f1.write(f'\n                bd={int(widget["bd"])},')
                            f1.write(f'\n                )')
                        elif type(temp_list_widgets_on_wins[index]) is Canvas:
                            f1.write(f'\n        self.{widget["id"]}=Canvas({master},')
                            f1.write(f'\n                bg="{widget["bg"]}",')
                            f1.write(f'\n                highlightthickness="{widget["highlightthickness"]}",')
                            f1.write(f'\n                )')
                        elif type(temp_list_widgets_on_wins[index]) is Radiobutton:
                            f1.write(f'\n        self.{widget["id"]}=Radiobutton({master},')
                            f1.write(f'\n                text="{widget["text"]}",')
                            f1.write(f'\n                bg="{widget["bg"]}",')
                            f1.write(f'\n                fg="{widget["fg"]}",')
                            f1.write(f'\n                font=("{widget["font family"]}",{int(widget["font size"])}),')
                            if self.CheckNone(widget["highlightcolor"])==None:
                                f1.write(f'\n                highlightcolor=None,')
                            else:
                                f1.write(f'\n                highlightcolor="{widget["highlightcolor"]}",')
                            if self.CheckNone(widget["highlightbackground"])==None:
                                f1.write(f'\n                highlightbackground=None,')
                            else:
                                f1.write(f'\n                highlightbackground="{widget["highlightbackground"]}",')
                            if self.CheckNone(widget["activebackground"])==None:
                                f1.write(f'\n                activebackground=None,')
                            else:
                                f1.write(f'\n                activebackground="{widget["activebackground"]}",')
                            if self.CheckNone(widget["activeforeground"])==None:
                                f1.write(f'\n                activeforeground=None,')
                            else:
                                f1.write(f'\n                activeforeground="{widget["activeforeground"]}",')
                            f1.write(f'\n                )')
                        elif type(temp_list_widgets_on_wins[index]) is Checkbutton:
                            f1.write(f'\n        self.{widget["id"]}=Checkbutton({master},')
                            f1.write(f'\n                text="{widget["text"]}",')
                            f1.write(f'\n                bg="{widget["bg"]}",')
                            f1.write(f'\n                fg="{widget["fg"]}",')
                            f1.write(f'\n                font=("{widget["font family"]}",{int(widget["font size"])}),')
                            if self.CheckNone(widget["highlightcolor"])==None:
                                f1.write(f'\n                highlightcolor=None,')
                            else:
                                f1.write(f'\n                highlightcolor="{widget["highlightcolor"]}",')
                            if self.CheckNone(widget["highlightbackground"])==None:
                                f1.write(f'\n                highlightbackground=None,')
                            else:
                                f1.write(f'\n                highlightbackground="{widget["highlightbackground"]}",')
                            if self.CheckNone(widget["activebackground"])==None:
                                f1.write(f'\n                activebackground=None,')
                            else:
                                f1.write(f'\n                activebackground="{widget["activebackground"]}",')
                            if self.CheckNone(widget["activeforeground"])==None:
                                f1.write(f'\n                activeforeground=None,')
                            else:
                                f1.write(f'\n                activeforeground="{widget["activeforeground"]}",')
                            f1.write(f'\n                )')
                        elif type(temp_list_widgets_on_wins[index]) is ttk.Scrollbar:
                            f1.write(f'\n        self.{widget["id"]}=ttk.Scrollbar({master},')
                            f1.write(f'\n                orient="{widget["orient"]}",')
                            f1.write(f'\n                )')
                        elif type(temp_list_widgets_on_wins[index]) is ttk.Combobox:
                            f1.write(f'\n        self.{widget["id"]}=ttk.Combobox({master})')
                        elif type(temp_list_widgets_on_wins[index]) is ttk.Treeview:
                            f1.write(f'\n        self.{widget["id"]}=ttk.Treeview({master})')
                        elif type(temp_list_widgets_on_wins[index]) is Frame:
                            f1.write(f'\n        self.{widget["id"]}=Frame({master},')
                            f1.write(f'\n                bg="{widget["bg"]}",')
                            f1.write(f'\n                )')
                        
                        index+=1
                    index=0
                    for widget in self.list_widgets_on_wins_properties:
                        
                        if widget['type']=='place':
                            ## place commands
                            f1.write(f'\n        self.{widget["id"]}.place(x={int(widget["x"])},y={int(widget["y"])},width={int(widget["width"])},height={int(widget["height"])})')
                        elif widget['type']=='pack':
                            ## pack commands
                            if widget["fill"]==None or widget["fill"]=='None':
                                f1.write(f'\n        self.{widget["id"]}.pack(side="{widget["side"]}",padx={int(widget["padx"])},pady={int(widget["pady"])},fill={None},expand="{widget["expand"]}")')
                            else:
                                f1.write(f'\n        self.{widget["id"]}.pack(side="{widget["side"]}",padx={int(widget["padx"])},pady={int(widget["pady"])},fill="{widget["fill"]}",expand="{widget["expand"]}")')
                        
                        index+=1
                self.lbl_status.config(text='Exported!')
        except:
            pass
    def bt_run_com(self):
        # print(self.list_widgets_on_wins_Errors)
        # print(self.Error_win)
        try:
            if self.registered:
                if any(self.list_widgets_on_wins_Errors) or self.Error_win:
                    msgbox=messagebox.showinfo("Error!","Check all Errors in the program!")
                else:
                    self.save_win()
                    self.bt_export_com()
                    td=self.text.get('1.0',END)
                    ## creating file temp to collect all wins and classes in it and run it
                    list_codes_files=[]
                    list_files=os.listdir(self.path_project)
                    td=td.replace('from tkinter import *','')
                    td=td.replace('from tkinter import ttk','')
                    for file in list_files:
                        if '_code.py' in file:
                            with open(self.path_project+'\\'+file,'r') as f1:
                                code=f1.read()
                                code=code.replace('from tkinter import ttk','')
                                code=code.replace('from tkinter import *','')
                                list_codes_files.append(code)
                            list_split=file.split('_')
                            td=td.replace(f'from {file.replace(".py","")} import {list_split[0].capitalize()}Code','')
                    
                    with open(self.path_project+'\\temp.py','w') as f1:
                        f1.write('from tkinter import *\n')
                        f1.write('from tkinter import ttk\n')
                        for code in list_codes_files:
                            code_new=code.replace('overrideredirect(1)','overrideredirect(0)')
                            f1.write(code_new+'\n')
                        f1.write(td)
                    
                        
                    os.chdir(self.path_project)
                    source = open(self.path_project+'\\temp.py', 'r').read() + '\n'
                    self.txt_consol.config(state='normal')
                    txt=self.txt_consol.get(f'{self.n_run}.{0}','end')
                    txt=txt.splitlines()[0]
                    if 'self' in txt or 'current' in txt or 'Error' in txt:
                        self.stop_running()
                    self.txt_consol.insert(f'{self.n_run}.{len(txt)}',f'running self win')
                    
                    self.txt_consol.config(state='disabled')
                    
                    self.debug.entryconfig('Stop running',state='normal')
                    self.running=1
                    self.bt_stop_running.config(image=self.image_stop_before)
                    try:
                        exec(source)
                    except:
                        self.txt_consol.config(state='normal')
                        txt=self.txt_consol.get(f'{self.n_run}.{0}','end')
                        if '\n' in txt:
                            txt=txt.splitlines()[0]
                        self.txt_consol.insert(f'{self.n_run}.{len(txt)}',f' There is Error somewhere!')
                        self.txt_consol.config(state='disabled')
                    
                    self.stop_running()
                    
                    self.ConsolLight()
            else:
                masgbox=messagebox.showinfo('Register','You must register TK Design to enable this feature.')
        except:
            pass
                    
    def run_current_win(self):
        try:
            if self.registered:
                if any(self.list_widgets_on_wins_Errors) and self.Error_win:
                    pass
                else:
                    wins=self.listbox_wins.get(0,END)
                    if wins[self.pointer_win]=='self':
                        self.bt_run_com()
                    else:
                        self.save_win()
                        self.bt_export_com()
                        code=''
                        with open(self.path_project+'\\'+wins[self.pointer_win]+'_code.py','r') as f1:
                            code=f1.read()
                        with open(self.path_project+'\\temp_'+wins[self.pointer_win]+'.py','w') as f1:
                            f1.write(code+'\n')
                            f1.write(f'class temp_{wins[self.pointer_win]}(Tk,{wins[self.pointer_win].capitalize()}Code):\n')
                            f1.write(f'    def __init__(self):\n')
                            f1.write(f'        super().__init__()\n')
                            f1.write(f'        self.withdraw()\n')
                            f1.write(f'        self.{wins[self.pointer_win]}_fcn()\n')
                            f1.write(f'a=temp_{wins[self.pointer_win]}()\n')
                            f1.write(f'a.mainloop()')
                            
                        self.txt_consol.config(state='normal')
                        txt=self.txt_consol.get(f'{self.n_run}.{0}','end')
                        txt=txt.splitlines()[0]
                        if 'self' in txt or 'Error' in txt or 'current' in txt:
                            self.stop_running()
                        
                        self.txt_consol.insert(f'{self.n_run}.{len(txt)}',f'running current win')
                        self.txt_consol.config(state='disabled')
                        os.chdir(self.path_project)
                        source = open(self.path_project+'\\temp_'+wins[self.pointer_win]+'.py', 'r').read() + '\n'
                        self.debug.entryconfig('Stop running',state='normal')
                        self.running=1
                        self.bt_stop_running.config(image=self.image_stop_before)
                        try:
                            exec(source)
                        except:
                            self.txt_consol.config(state='normal')
                            txt=self.txt_consol.get(f'{self.n_run}.{0}','end')
                            if '\n' in txt:
                                txt=txt.splitlines()[0]
                            self.txt_consol.insert(f'{self.n_run}.{len(txt)}',f' There is Error somewhere!')
                            self.txt_consol.config(state='disabled')
                        
                        self.stop_running()
                        
                        self.ConsolLight()
            else:
                masgbox=messagebox.showinfo('Register','You must register TK Design to enable this feature.')
        except:
            pass
    def clear_consol(self):
        try:
            self.txt_consol.config(state='normal')
            self.txt_consol.delete('1.0','end')
            self.n_run=1
            self.txt_consol.insert(f'1.0','\n'*100)
            self.txt_consol.insert(f'1.0',f'R[1]: ')
            self.txt_consol.config(state='disabled')
            self.ConsolLight()
        except:
            pass
    def stop_running(self):
        try:
            self.txt_consol.config(state='normal')
            txt=self.txt_consol.get(f'{self.n_run}.{0}','end')
            if '\n' in txt:
                txt=txt.splitlines()[0]
            self.n_run+=1
            if self.n_run==50:
                self.clear_consol()
                self.txt_consol.config(state='disabled')
            else:
                self.txt_consol.insert(f'{self.n_run}.0',f'R[{self.n_run}]: ')
                self.txt_consol.config(state='disabled')
                self.ConsolLight()
            self.bt_stop_running.config(image=self.image_stop_after)
            self.running=0
            self.debug.entryconfig('Stop running',state='disabled')
        except:
            pass
    def ConsolLight(self):
        try:
            self.txt_consol.config(state='normal')
            td=self.txt_consol.get('1.0','end')
            if '\n' in td:
                td=td.splitlines()
            else:
                td=[td]
            line_index=1
            for line in td:
                if ':' in line:
                    end_index=line.index(':')+1
                    self.txt_consol.tag_add('green', f'{line_index}.{0}', f"{line_index}.{end_index}")
                    line_index+=1
            self.txt_consol.config(state='disabled')
        except:
            pass
    def bt_run_enter(self,e):
        try:
            self.bt_run.config(image=self.image_run_after)
        except:
            pass
    def bt_run_leave(self,e):
        try:
            self.bt_run.config(image=self.image_run_before)
        except:
            pass
   
    
    def loading_properties(self,e,show=1):
        try:
            selected=self.listbox_widgets_on_win.curselection()
            if str(e).isnumeric():
                selected=(int(e),)
            if selected:
                #self.listbox_widgets_on_win.config(state='disabled')
                self.selected=selected
                self.ClickWidget(selected[0])
                select_value=selected[0]
                index_win=-1
                if select_value==0:
                    properties=win_properties
                else:
                    ### error here
                    index_selected=self.get_indexWidget(self.list_widgets_on_wins[select_value-1])
                    properties=widget_properties[index_selected]
                    
                try:
                    self.my_canvas_right.delete(self.win_right)
                    del self.second_frame_right
                except:
                    pass
                self.second_frame_right=Frame(self.my_canvas_right,bg=themes[self.Theme]['lists'])
                if show:
                    self.win_right=self.my_canvas_right.create_window((0,0),window=self.second_frame_right,anchor='nw')
                
                counter_y=20
                max_width=0
                ############################################ labels  
                self.list_entry=[]
                self.list_vars=[]
                self.list_inputs=[]
                if select_value!=0:
                    
                    self.lbl=Label(self.second_frame_right,text='id:',fg=themes[self.Theme]["other labels"],font=('arial',13),bg=themes[self.Theme]['lists'])
                    self.lbl.place(x=10,y=counter_y,height=20)
                    self.lbl.update()
                    if self.lbl.winfo_width()>max_width:
                        max_width=self.lbl.winfo_width()
                        
                    counter_y=50
                    self.lbl=Label(self.second_frame_right,text='type:',fg=themes[self.Theme]["other labels"],font=('arial',13),bg=themes[self.Theme]['lists'])
                    self.lbl.place(x=10,y=counter_y,height=20)
                    self.lbl.update()
                    if self.lbl.winfo_width()>max_width:
                        max_width=self.lbl.winfo_width()
                        
                    counter_y=80
                    self.lbl=Label(self.second_frame_right,text='master:',fg=themes[self.Theme]["other labels"],font=('arial',13),bg=themes[self.Theme]['lists'])
                    self.lbl.place(x=10,y=counter_y,height=20)
                    self.lbl.update()
                    if self.lbl.winfo_width()>max_width:
                        max_width=self.lbl.winfo_width()
                    counter_y=110
                
                if select_value!=0:
                    for pro in widget_properties_place.keys():
                        self.lbl=Label(self.second_frame_right,text=pro+':',fg=themes[self.Theme]["other labels"],font=('arial',13),bg=themes[self.Theme]['lists'])
                        self.lbl.place(x=10,y=counter_y,height=20)
                        self.lbl.update()
                        if self.lbl.winfo_width()>max_width:
                            max_width=self.lbl.winfo_width()
                        counter_y+=30
                
                for pro in properties.keys():
                    self.lbl=Label(self.second_frame_right,text=pro+':',fg=themes[self.Theme]["other labels"],font=('arial',13),bg=themes[self.Theme]['lists'])
                    
                    self.lbl.place(x=10,y=counter_y,height=20)
                    self.lbl.update()
                    if self.lbl.winfo_width()>max_width:
                        max_width=self.lbl.winfo_width()
                    counter_y+=30
                    
                if select_value!=0:
                    for pro in widget_properties_pack.keys():
                        self.lbl=Label(self.second_frame_right,text=pro+':',fg=themes[self.Theme]["other labels"],font=('arial',13),bg=themes[self.Theme]['lists'])
                        self.lbl.place(x=10,y=counter_y,height=20)
                        self.lbl.update()
                        if self.lbl.winfo_width()>max_width:
                            max_width=self.lbl.winfo_width()
                        counter_y+=30
                        
                    for pro in widget_properties_grid.keys():
                        self.lbl=Label(self.second_frame_right,text=pro+':',fg=themes[self.Theme]["other labels"],font=('arial',13),bg=themes[self.Theme]['lists'])
                        self.lbl.place(x=10,y=counter_y,height=20)
                        self.lbl.update()
                        if self.lbl.winfo_width()>max_width:
                            max_width=self.lbl.winfo_width()
                        counter_y+=30
                        
                ############################################################## entries
                counter_y=20
                if select_value!=0:
                    self.list_entry.append(Entry(self.second_frame_right,bd=0,highlightthickness=1))
                    self.list_entry[-1].place(x=10+max_width,y=counter_y,height=20,width=150)
                    self.CheckError(self.list_widgets_on_wins_properties[self.selected[0]-1]['id'])
                    self.list_inputs.append(self.list_entry[-1])
                    
                    counter_y=50
                    self.list_vars.append(StringVar())
                    combo=ttk.Combobox(self.second_frame_right,textvariable=self.list_vars[-1])
                    combo.place(x=10+max_width,y=counter_y,height=20,width=150)
                    combo['values']=['place','pack']
                    combo.set(self.list_widgets_on_wins_properties[self.selected[0]-1]['type'])
                    self.list_inputs.append(combo)
                    
                    counter_y=80
                    self.list_entry.append(Entry(self.second_frame_right,bd=0,highlightthickness=1))
                    self.list_entry[-1].place(x=10+max_width,y=counter_y,height=20,width=150)
                    self.CheckError(self.list_widgets_on_wins_properties[self.selected[0]-1]['master'])
                    self.list_inputs.append(self.list_entry[-1])
                    counter_y=110
                if select_value!=0:
                    pro_num=0
                    keys=list(widget_properties_place.keys())
                    for value in widget_properties_place.values():
                        if value=='string'or value=='int':
                            self.list_entry.append(Entry(self.second_frame_right,bd=0))
                            self.list_entry[-1].place(x=10+max_width,y=counter_y,height=20,width=150)
                            self.CheckError(str(self.list_widgets_on_wins_properties[self.selected[0]-1][keys[pro_num]]))
                            self.list_inputs.append(self.list_entry[-1])
                        elif type(value) is list:
                            if type(value[0])==int:
                                self.list_vars.append(IntVar())
                            elif type(value[0])==str:
                                self.list_vars.append(StringVar())
                            combo=ttk.Combobox(self.second_frame_right,textvariable=self.list_vars[-1])
                            combo.place(x=10+max_width,y=counter_y,height=20,width=150)
                            
                            combo['values']=value
                            combo.set(self.list_widgets_on_wins_properties[self.selected[0]-1][keys[pro_num]])
                            self.list_inputs.append(combo)
                        counter_y+=30
                        pro_num+=1
                    
                pro_num=0
                keys=list(properties.keys())
                for value in properties.values():
                    if value=='string'or value=='int':
                        self.list_entry.append(Entry(self.second_frame_right,bd=0))
                        self.list_entry[-1].place(x=10+max_width,y=counter_y,height=20,width=150)
                        if select_value!=0:
                            self.CheckError(str(self.list_widgets_on_wins_properties[self.selected[0]-1][keys[pro_num]]))
                        else:
                            self.CheckError(str(self.list_wins_properties[keys[pro_num]]))
    
                        self.list_inputs.append(self.list_entry[-1])
                    elif type(value) is list:
                        if type(value[0])==int:
                            self.list_vars.append(IntVar())
                        elif type(value[0])==str:
                            self.list_vars.append(StringVar())
                            
                        combo=ttk.Combobox(self.second_frame_right,textvariable=self.list_vars[-1])
                        combo.place(x=10+max_width,y=counter_y,height=20,width=150)
                        
                        combo['values']=value
                        if select_value!=0:
                            combo.set(self.list_widgets_on_wins_properties[self.selected[0]-1][keys[pro_num]])
                        else:
                            combo.set(str(self.list_wins_properties[keys[pro_num]]))
                        self.list_inputs.append(combo)
                    elif value=='path':
                        self.list_entry.append(Entry(self.second_frame_right,bd=0))
                        self.list_entry[-1].place(x=10+max_width,y=counter_y,height=20,width=150)
                        if select_value!=0:
                            self.CheckError(str(self.list_widgets_on_wins_properties[self.selected[0]-1][keys[pro_num]]))
                        else:
                            self.CheckError(str(self.list_wins_properties[keys[pro_num]]))
    
                        self.list_entry[-1].bind('<Button-1>',self.bt_path_com)
                        self.list_inputs.append(self.list_entry[-1])
                    counter_y+=30
                    pro_num+=1
                    
                ######################### for pack and grid
                if select_value!=0:
                    pro_num=0
                    keys=list(widget_properties_pack.keys())
                    for value in widget_properties_pack.values():
                        if value=='string'or value=='int':
                            self.list_entry.append(Entry(self.second_frame_right,bd=0))
                            self.list_entry[-1].place(x=10+max_width,y=counter_y,height=20,width=150)
                            self.CheckError(str(self.list_widgets_on_wins_properties[self.selected[0]-1][keys[pro_num]]))
                            self.list_inputs.append(self.list_entry[-1])
                        elif type(value) is list:
                            if type(value[0])==int:
                                self.list_vars.append(IntVar())
                            elif type(value[0])==str:
                                self.list_vars.append(StringVar())
                            combo=ttk.Combobox(self.second_frame_right,textvariable=self.list_vars[-1])
                            combo.place(x=10+max_width,y=counter_y,height=20,width=150)
                            
                            combo['values']=value
                            combo.set(self.list_widgets_on_wins_properties[self.selected[0]-1][keys[pro_num]])
                            self.list_inputs.append(combo)
                            
                        counter_y+=30
                        pro_num+=1
                        
                    pro_num=0
                    keys=list(widget_properties_grid.keys())
                    for value in widget_properties_grid.values():
                        if value=='string'or value=='int':
                            self.list_entry.append(Entry(self.second_frame_right,bd=0))
                            self.list_entry[-1].place(x=10+max_width,y=counter_y,height=20,width=150)
                            self.CheckError(str(self.list_widgets_on_wins_properties[self.selected[0]-1][keys[pro_num]]))
                            self.list_inputs.append(self.list_entry[-1])
                        elif type(value) is list:
                            if type(value[0])==int:
                                self.list_vars.append(IntVar())
                            elif type(value[0])==str:
                                self.list_vars.append(StringVar())
                            combo=ttk.Combobox(self.second_frame_right,textvariable=self.list_vars[-1])
                            combo.place(x=10+max_width,y=counter_y,height=20,width=150)
                            
                            combo['values']=value
                            combo.set(self.list_widgets_on_wins_properties[self.selected[0]-1][keys[pro_num]])
                            self.list_inputs.append(combo)
                            
                        counter_y+=30
                        pro_num+=1
                    
                #self.listbox_widgets_on_win.config(state='normal')
                ############################################
                if show:
                    self.my_canvas_right.itemconfigure(self.win_right,width=max_width+155,height=counter_y)
                    self.my_canvas_right.configure(scrollregion=(0,0,max_width+155,counter_y+5))
                else:
                    pass
        except:
            pass
    def AddWidget(self,e,show=1):
        try:
            selected=self.listbox_widgets.curselection()
            if str(e).isnumeric():
                selected=(int(e),)
            masters=[self.second_frame,self.selected_master]
            index_master=0
            if self.num_widget!=-1:
                index_master=1
           
            
            if selected or self.num_widget!=-1:
                value=-1
                if selected and self.num_widget==-1:
                    value=selected[0]
                frame=Frame(masters[index_master],bg=themes[self.Theme]['FrameWidget'])
                conditions=[0,0,0,0,0,0,0,0,0,0,0,0]
                
                if value!=-1:
                    conditions=[widgets[value]=='Button',
                                widgets[value]=='Entry',
                                widgets[value]=='Text',
                                widgets[value]=='Radiobutton',
                                widgets[value]=='Checkbutton',
                                widgets[value]=='Canvas',
                                widgets[value]=='Label',
                                widgets[value]=='Listbox',
                                widgets[value]=='Scrollbar',
                                widgets[value]=='Combobox',
                                widgets[value]=='Treeview',
                                widgets[value]=='Frame'
                                ]
                if conditions[0] or self.num_widget==0:
                    widget=Button(frame,
                              fg='black',
                              font=('arial',13),
                              text='Button',
                              bg='#f0f0f0',
                              bd=0,
                              command=None,
                              highlightcolor=None,
                              highlightbackground=None,
                              activebackground='white',
                              activeforeground='black',
                              image=None,
                              relief='flat',
                              ) 
                    
                elif conditions[1] or self.num_widget==1:
                    widget=Entry(frame,
                            bg='#f0f0f0',
                            fg='black',
                            font=('arial',13),
                            bd=0,
                            highlightcolor=None,
                            highlightbackground=None,
                            show=None,
                            highlightthickness=1
                              )
                elif conditions[2] or self.num_widget==2:
                    widget=Text(frame,
                             bg='#f0f0f0',
                             fg='black',
                             font=('arial',13),
                             bd=0,
                             )
                elif conditions[3] or self.num_widget==3:
                    widget=Radiobutton(frame,
                                    text='Radiobutton',
                                    bg='#f0f0f0',
                                    fg='black',
                                    font=('arial',13),
                                    highlightcolor=None,
                                    highlightbackground=None,
                                    activebackground=None,
                                    activeforeground=None
                                   )
                elif conditions[4] or self.num_widget==4:
                    widget=Checkbutton(frame,
                                    text='Checkbutton',
                                    bg='#f0f0f0',
                                    fg='black',
                                    font=('arial',13),
                                    highlightcolor=None,
                                    highlightbackground=None,
                                    activebackground=None,
                                    activeforeground=None
                                   )
                elif conditions[5] or self.num_widget==5:
                    widget=Canvas(frame,
                                  bg='#f0f0f0',
                                  highlightthickness=0)
                    
                elif conditions[6] or self.num_widget==6:
                    widget=Label(frame,
                                text='Label',
                                bg='#f0f0f0',
                                fg='black',
                                font=('arial',13),
                                image=None
                              )
                elif conditions[7] or self.num_widget==7:
                    widget=Listbox(frame,
                                    bg='white',
                                    fg='black',
                                    font=('arial',13),
                                    highlightcolor='orange',
                                    highlightbackground='black',
                                    bd=0
                                    )
                elif conditions[8] or self.num_widget==8:
                    widget=ttk.Scrollbar(frame,orient='vertical')
                elif conditions[9] or self.num_widget==9:
                    widget=ttk.Combobox(frame)
                elif conditions[10] or self.num_widget==10:
                    widget=ttk.Treeview(frame)
                elif conditions[11] or self.num_widget==11:
                    widget=Frame(frame,bg='orange')
                widget.update()
                
                if self.num_widget==-1:
                    
                    self.list_widgets_on_wins_Errors.append(0)
                    
                    self.list_frames_on_wins.append(frame)
                    self.list_frames_on_wins[-1].bind('<B1-Motion>',self.ResizingWidgets)
                    self.list_widgets_on_wins.append(widget)
                    self.list_widgets_on_wins[-1].bind('<Button-1>',self.ClickWidget)
                    self.list_widgets_on_wins[-1].bind('<B1-Motion>',self.MovingWidget)
                    self.list_widgets_on_wins[-1].bind('<Button-3>',self.ClickRightWidget)
                    self.list_frames_on_wins[-1].config(cursor='bottom_right_corner')
                    self.list_widgets_on_wins[-1].config(cursor='arrow')
                    
                    self.list_frames_on_wins[-1].config(width=widget.winfo_width(),height=widget.winfo_height())
                    self.list_frames_on_wins[-1].place(x=10,y=10)
                    self.list_widgets_on_wins[-1].pack(padx=0,pady=0,fill=BOTH,expand=True)
                    self.listbox_widgets_on_win.insert(END,self.listbox_widgets.get(value)+str(self.list_nums[value]))
                    self.list_widgets_on_wins_properties.append({'id':self.listbox_widgets.get(value)+str(self.list_nums[value]),'type':'place','master':self.listbox_wins.get(0,END)[self.pointer_win]})
                    self.list_widgets_on_wins_properties[-1].update(widget_properties_place_defaults)
                    self.list_widgets_on_wins_properties[-1].update(widget_properties_default[value])
                    self.list_widgets_on_wins_properties[-1].update(widget_properties_pack_defaults)
                    self.list_widgets_on_wins_properties[-1].update(widget_properties_grid_defaults)
                    self.list_widgets_on_wins[-1].update()
                    self.list_widgets_on_wins_properties[-1]['width']=self.list_widgets_on_wins[-1].winfo_width()
                    self.list_widgets_on_wins_properties[-1]['height']=self.list_widgets_on_wins[-1].winfo_height()
                    self.list_nums[value]=self.list_nums[value]+1
                    self.selected=(len(self.listbox_widgets_on_win.get(0,END))-1,)
                    self.loading_properties(len(self.listbox_widgets_on_win.get(0,END))-1,show)
                    
                else:
                    
                    self.list_widgets_on_wins_Errors[self.index_RemovedWidget]=0
                    self.list_frames_on_wins[self.index_RemovedWidget]=frame
                    self.list_frames_on_wins[self.index_RemovedWidget].bind('<B1-Motion>',self.ResizingWidgets)
                    self.list_widgets_on_wins[self.index_RemovedWidget]=widget
                    self.list_widgets_on_wins[self.index_RemovedWidget].bind('<Button-1>',self.ClickWidget)
                    self.list_widgets_on_wins[self.index_RemovedWidget].bind('<B1-Motion>',self.MovingWidget)
                    self.list_widgets_on_wins[self.index_RemovedWidget].bind('<Button-3>',self.ClickRightWidget)
                    self.list_frames_on_wins[self.index_RemovedWidget].config(cursor='bottom_right_corner')
                    self.list_widgets_on_wins[self.index_RemovedWidget].config(cursor='arrow')
                    
                    self.list_frames_on_wins[self.index_RemovedWidget].place(x=10,y=10)
                    self.list_widgets_on_wins[self.index_RemovedWidget].pack(padx=0,pady=0,fill=BOTH,expand=True)
                    
                self.num_widget=-1
        except:
            pass
    def ClickRightWidget(self,e):
        try:
            if self.selected==(1,):
                self.my_menu_widget.entryconfig('Send to back',state='disabled')
                self.my_menu_widget.entryconfig('Bring to back',state='disabled')
            else:
                self.my_menu_widget.entryconfig('Send to back',state='normal')
                self.my_menu_widget.entryconfig('Bring to back',state='normal')
            num_widgets=len(self.list_widgets_on_wins)
            if self.selected==(num_widgets,):
                self.my_menu_widget.entryconfig('Send to front',state='disabled')
                self.my_menu_widget.entryconfig('Bring to front',state='disabled')
            else:
                self.my_menu_widget.entryconfig('Send to front',state='normal')
                self.my_menu_widget.entryconfig('Bring to front',state='normal')
            self.my_menu_widget.tk_popup(e.x_root, e.y_root)
        except:
            pass
    def click_enter(self,e):
        try:
            if self.CodeHide==1:
                value=self.selected[0]-1
                if str(e).isnumeric():
                    value=int(e)-1
                if value==-1: ## win
                    list_wins=self.listbox_wins.get(0,END)
                    index_win=list_wins.index(self.listbox_widgets_on_win.get(0))
                    self.UpdatingWinProperties(index_win)
                elif value==-2:
                    pass
                else:
                    self.UpdatingWidgetProperties(value)
        except:
            pass
    def bt_path_com(self,e):
        try:
            index_ent=int(str(e.widget).split('entry')[1])-1
            path=filedialog.askopenfilename()
            if path:
                self.list_entry[index_ent].delete(0,END)
                self.list_entry[index_ent].insert(END,path)
        except:
            pass
    def CheckNone(self,txt):
        try:
            if txt=='None':
                return None
            else:
                return txt
        except:
            pass
    def CheckError(self,text):
        try:
            Error=False
            txt=text
            if 'Error*' in text:
                Error=True
                txt=text.replace('Error*','')
            self.list_entry[-1].insert(END,txt)
            if Error:
                self.list_entry[-1].config(highlightbackground='red',highlightthickness=1,highlightcolor='red')
        except:
            pass
    def ClickEnterTotCom(self,e):
        try:
            selected=self.selected
            widgets_on_wins=self.list_widgets_on_wins.copy()
            widgets_properties=self.list_widgets_on_wins_properties.copy()
            self.click_enter(e)
            
            if selected!=():
                if selected[0]!=0:
                    value=selected[0]-1
                    There_in=0
                    index=0
                    wins=self.listbox_wins.get(0,END)
                    for widget in widgets_on_wins:
                        if str(widgets_on_wins[value]) in str(widget) and str(widgets_on_wins[value])!=str(widget):
                            
                            There_in=1
                        index+=1
                    if There_in:
                        
                        self.Refresh_com()
        except:
            pass
    def UpdatingWidgetProperties(self,value):
        try:
            Error=0
            keys=list(self.list_widgets_on_wins_properties[value].keys())
            wins=self.listbox_wins.get(0,END)
            for index in range(0,len(self.list_inputs)):
                err=0
                test_value=''
                if keys[index]=='master':
                    test_value=self.list_inputs[index].get()
                    masters=self.listbox_widgets_on_win.get(0,END)
                    if test_value in masters:
                        index_master=masters.index(test_value)
                        
                        if self.list_widgets_on_wins_properties[value][keys[index]]!=test_value and index_master!=value+1:
                            self.list_widgets_on_wins_properties[value][keys[index]]=test_value
                            var=-1
                            if type(self.list_widgets_on_wins[value]) is Button:
                                var=0
                            elif type(self.list_widgets_on_wins[value]) is Entry:
                                var=1
                            elif type(self.list_widgets_on_wins[value]) is Text:
                                var=2
                            elif type(self.list_widgets_on_wins[value]) is Radiobutton:
                                var=3
                            elif type(self.list_widgets_on_wins[value]) is Checkbutton:
                                var=4
                            elif type(self.list_widgets_on_wins[value]) is Canvas:
                                var=5
                            elif type(self.list_widgets_on_wins[value]) is Label:
                                var=6
                            elif type(self.list_widgets_on_wins[value]) is Listbox:
                                var=7
                            elif type(self.list_widgets_on_wins[value]) is ttk.Scrollbar:
                                var=8
                            elif type(self.list_widgets_on_wins[value]) is ttk.Combobox:
                                var=9
                            elif type(self.list_widgets_on_wins[value]) is ttk.Treeview:
                                var=10
                            elif type(self.list_widgets_on_wins[value]) is Frame:
                                var=11
                            if index_master!=0:
                                ## create the same widget in the new master
                                self.num_widget=var
                                self.index_RemovedWidget=value
                                self.selected_master=self.list_widgets_on_wins[index_master-1]
                                self.list_frames_on_wins[value].place_forget()
                                self.list_frames_on_wins[value].pack_forget()
                                #self.list_masters_nums[value]
                                self.AddWidget(None,0)
                                
                                    
                            else:
                                
                                properties=self.list_widgets_on_wins_properties[value].copy()
                                self.list_frames_on_wins[value].place_forget()
                                self.list_frames_on_wins[value].pack_forget()
                                self.list_widgets_on_wins.pop(value)
                                self.list_frames_on_wins.pop(value)
                                self.list_widgets_on_wins_Errors.pop(value)
                                
                                self.list_widgets_on_wins_properties.pop(value)
                                self.listbox_widgets_on_win.delete(value+1)
                                self.AddWidget(var,0)
                                master_win=self.list_widgets_on_wins_properties[-1]['master']
                                self.list_widgets_on_wins_properties[-1]=properties
                                self.list_widgets_on_wins_properties[-1]['master']=master_win
                                self.listbox_widgets_on_win.delete(END)
                                self.listbox_widgets_on_win.insert(END,properties['id'])
                                value=-1
                                self.Refresh_com()
                                break
                                
                    else:
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value+'Error*'
                        err=1
                elif keys[index]=='id':
                    test_value=self.list_inputs[index].get()
                    widgets_inserted=self.listbox_widgets_on_win.get(0,END)
                    
                    if not test_value in widgets_inserted or test_value==widgets_inserted[value+1]:
                        valid=self.CheckId(test_value)
                        if valid:
                            prev_value=widgets_inserted[value+1]
                            self.list_widgets_on_wins_properties[value][keys[index]]=test_value
                            self.listbox_widgets_on_win.delete(value+1)
                            self.listbox_widgets_on_win.insert(value+1,test_value)
                            for indx in range(0,len(self.list_widgets_on_wins_properties)):
                                if self.list_widgets_on_wins_properties[indx]['master']== prev_value:
                                    self.list_widgets_on_wins_properties[indx]['master']=test_value
                        else:
                            self.list_widgets_on_wins_properties[value][keys[index]]=test_value+'Error*'
                            err=1
                    else:
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value+'Error*'
                        err=1
                if keys[index]=='command':
                    test_value=self.list_inputs[index].get()
                    valid=self.CheckId(test_value)
                    if valid:
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value
                    else:
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value+'Error*'
                        err=1
                elif keys[index]=='bg':
                    try:
                        test_value=self.list_inputs[index].get()
                        self.list_widgets_on_wins[value].config(bg=test_value)
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value
                    except:
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value+'Error*'
                        err=1
                elif keys[index]=='fg':
                    try:
                        test_value=self.list_inputs[index].get()
                        self.list_widgets_on_wins[value].config(fg=test_value)
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value
                    except:
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value+'Error*'
                        err=1
                elif keys[index]=='text':
                    ## there is no error in text
                    test_value=self.list_inputs[index].get()
                    self.list_widgets_on_wins[value].config(text=test_value)
                    self.list_widgets_on_wins_properties[value][keys[index]]=test_value
                elif keys[index]=='font family':
                    try:
                        test_value=self.list_inputs[index].get()
                        self.list_widgets_on_wins[value].config(font=(test_value,int(self.list_widgets_on_wins_properties[value][keys[index+1]])))
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value
                    except:
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value+'Error*'
                        err=1
                elif keys[index]=='font size':
                    try:
                        test_value=self.list_inputs[index].get()
                        self.list_widgets_on_wins[value].config(font=(self.list_widgets_on_wins_properties[value][keys[index-1]],int(test_value)))
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value
                    except:
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value+'Error*'
                        err=1
                elif keys[index]=='bd':
                    try:
                        test_value=self.list_inputs[index].get()
                        self.list_widgets_on_wins[value].config(bd=int(test_value))
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value
                    except:
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value+'Error*'
                        err=1
                elif keys[index]=='highlightcolor':
                    try:
                        test_value=self.list_inputs[index].get()
                        self.list_widgets_on_wins[value].config(highlightcolor=self.CheckNone(test_value))
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value
                    except:
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value+'Error*'
                        err=1
                elif keys[index]=='highlightbackground':
                    try:
                        test_value=self.list_inputs[index].get()
                        self.list_widgets_on_wins[value].config(highlightbackground=self.CheckNone(test_value))
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value
                    except:
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value+'Error*'
                        err=1
                elif keys[index]=='activebackground':
                    try:
                        test_value=self.list_inputs[index].get()
                        self.list_widgets_on_wins[value].config(activebackground=self.CheckNone(test_value))
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value
                    except:
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value+'Error*'
                        err=1
                elif keys[index]=='activeforeground':
                    try:
                        test_value=self.list_inputs[index].get()
                        self.list_widgets_on_wins[value].config(activeforeground=self.CheckNone(test_value))
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value
                    except:
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value+'Error*'
                        err=1
                elif keys[index]=='image':
                    try:
                        test_value=self.list_inputs[index].get()
                        image2=None
                        if test_value!='None':
                            image2=PhotoImage(master=self.second_frame,file=test_value)
                        self.images.append(image2)
                        self.list_widgets_on_wins[value].config(image=self.images[-1])
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value
                    except:
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value+'Error*'
                        err=1
                elif keys[index]=='relief':
                    test_value=self.list_inputs[index].get()
                    try:
                        self.list_widgets_on_wins[value].config(relief=test_value)
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value
                    except:
                        pass
                elif keys[index]=='show':
                    try:
                        test_value=self.list_inputs[index].get()
                        self.list_widgets_on_wins[value].config(show=test_value)
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value
                    except:
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value+'Error*'
                        err=1
                elif keys[index]=='highlightthickness':
                    try:
                        test_value=self.list_inputs[index].get()
                        self.list_widgets_on_wins[value].config(highlightthickness=int(test_value))
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value
                    except:
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value+'Error*'
                        err=1
                elif keys[index]=='orient':
                    test_value=self.list_inputs[index].get()
                    if test_value in ['horizontal','vertical']:
                        self.list_widgets_on_wins[value].config(orient=test_value)
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value
                elif keys[index]=='type':
                    test_value=self.list_inputs[index].get()
                    if test_value in ['place','pack']:
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value
    
                if self.list_widgets_on_wins_properties[value]['type']=='place':
                    if keys[index]=='width':
                        try:
                            test_value=self.list_inputs[index].get()
                            self.list_frames_on_wins[value].place_configure(width=int(test_value))
                            self.list_widgets_on_wins_properties[value][keys[index]]=test_value
                        except:
                            self.list_widgets_on_wins_properties[value][keys[index]]=test_value+'Error*'
                            err=1
                    elif keys[index]=='height':
                        try:
                            test_value=self.list_inputs[index].get()
                            self.list_frames_on_wins[value].place_configure(height=int(test_value))
                            self.list_widgets_on_wins_properties[value][keys[index]]=test_value
                        except:
                            self.list_widgets_on_wins_properties[value][keys[index]]=test_value+'Error*'
                            err=1
                    elif keys[index]=='x':
                        try:
                            test_value=self.list_inputs[index].get()
                            self.list_frames_on_wins[value].place_configure(x=int(test_value))
                            self.list_widgets_on_wins[value].pack_configure(padx=0)
                            self.list_widgets_on_wins_properties[value][keys[index]]=test_value
                        except:
                            self.list_widgets_on_wins_properties[value][keys[index]]=test_value+'Error*'
                            err=1
                    elif keys[index]=='y':
                        try:
                            test_value=self.list_inputs[index].get()
                            self.list_frames_on_wins[value].place_configure(y=int(test_value))
                            self.list_widgets_on_wins[value].pack_configure(pady=0)
                            self.list_widgets_on_wins_properties[value][keys[index]]=test_value
                        except:
                            self.list_widgets_on_wins_properties[value][keys[index]]=test_value+'Error*'
                            err=1
                elif self.list_widgets_on_wins_properties[value]['type']=='pack':
                    self.list_frames_on_wins[value].place_forget()
                    if keys[index]=='side':
                        try:
                            test_value=self.list_inputs[index].get()
                            self.list_frames_on_wins[value].pack(side=test_value)
                            self.list_widgets_on_wins_properties[value][keys[index]]=test_value
                        except:
                            pass
                    elif keys[index]=='fill':
                        try:
                            test_value=self.list_inputs[index].get()
                            self.list_frames_on_wins[value].pack(fill=test_value)
                            self.list_widgets_on_wins_properties[value][keys[index]]=test_value
                        except:
                            pass
                    elif keys[index]=='expand':
                        try:
                            test_value=self.list_inputs[index].get()
                            self.list_frames_on_wins[value].pack(expand=test_value)
                            self.list_widgets_on_wins_properties[value][keys[index]]=test_value
                        except:
                            pass
                    elif keys[index]=='padx':
                        try:
                            test_value=self.list_inputs[index].get()
                            test_value=int(test_value)
                            self.list_frames_on_wins[value].pack(padx=test_value)
                            self.list_widgets_on_wins_properties[value][keys[index]]=test_value
                        except:
                            self.list_widgets_on_wins_properties[value][keys[index]]=test_value+'Error*'
                            err=1
                    elif keys[index]=='pady':
                        try:
                            test_value=self.list_inputs[index].get()
                            test_value=int(test_value)
                            self.list_frames_on_wins[value].pack(pady=test_value)
                            self.list_widgets_on_wins_properties[value][keys[index]]=test_value
                        except:
                            self.list_widgets_on_wins_properties[value][keys[index]]=test_value+'Error*'
                            err=1
                    self.list_widgets_on_wins[value].pack_configure(padx=0,pady=0)
                    
                Error=Error or err
                self.list_widgets_on_wins_Errors[value]=Error
                if err:
                    self.list_inputs[index].config(highlightthickness=1,highlightbackground='red',highlightcolor='red')
                else:
                    if type(self.list_inputs[index]) is Entry:
                        self.list_inputs[index].config(highlightthickness=0,highlightbackground='black',highlightcolor='red')
            if self.list_widgets_on_wins_properties[value]['type']=='pack':
                try:
                    masters=self.listbox_widgets_on_win.get(0,END)
                    index=masters.index(self.list_widgets_on_wins_properties[value]['master'])
                    self.loading_properties(index,0)
                    self.click_enter(index)
                    self.loading_properties(value+1,0)
                except:
                    pass
            if Error:
                self.listbox_widgets_on_win.itemconfig(value+1,{'fg':'red'})
            else:
                self.listbox_widgets_on_win.itemconfig(value+1,{'fg':themes[self.Theme]["other labels"]})
        except:
            pass
    def CheckId(self,text_id):
        try:
            valid=True
            if text_id=='':
                valid=False
            else:
                if text_id[0].isalpha():
                    if ("_") in text_id:
                        list=text_id.split('_')
                        for i in list:
                            if not i=='' and not i.isalnum():
                                valid=False
                    else:
                        if not text_id.isalnum():
                            valid=False
                else:
                    valid=False
            return valid
        except:
            pass
    def get_indexWidget(self,widget):
        try:
            index=-1
            if type(widget) is Button:
                index=0
            elif type(widget) is Entry:
                index=1
            elif type(widget) is Text:
                index=2
            elif type(widget) is Radiobutton:
                index=3
            elif type(widget) is Checkbutton:
                index=4
            elif type(widget) is Canvas:
                index=5
            elif type(widget) is Label:
                index=6
            elif type(widget) is Listbox:
                index=7
            elif type(widget) is ttk.Scrollbar:
                index=8
            elif type(widget) is ttk.Combobox:
                index=9
            elif type(widget) is ttk.Treeview:
                index=10
            elif type(widget) is Frame:
                index=11
            return index
        except:
            pass
    def UpdatingWinProperties(self,value):
        # keys=list(win_properties_defaults.keys())
        # for index in range(0,len(self.list_entry)):
        #     new=self.list_entry[index].get()
        #     win_properties_defaults[keys[index]]=new
        try:
            keys=list(self.list_wins_properties.keys())
            Error=0
            for index in range(0,len(self.list_inputs)):
                err=0
                if keys[index]=='id':
                    test_value=self.list_inputs[index].get()
                    valid=self.CheckId(test_value)
                    wins=self.listbox_wins.get(0,END)
                    if test_value!=self.list_wins_properties['id']:
                        if valid and not test_value in wins:
                            self.list_wins_properties[keys[index]]=test_value
                            self.listbox_wins.delete(value)
                            self.listbox_wins.insert(value,test_value)
                            self.listbox_widgets_on_win.delete(0)
                            self.listbox_widgets_on_win.insert(0,test_value)
                            self.lbl_filename_txt.config(text=test_value)
                            indx=0
                            for widget in self.list_widgets_on_wins_properties:
                                self.list_widgets_on_wins_properties[indx]['master']=test_value
                                indx+=1
                        else:
                            self.list_wins_properties[keys[index]]=test_value+'Error*'
                            err=1
                elif keys[index]=='pos_x':
                    test_value=self.list_inputs[index].get()
                    if test_value=='center' or test_value.isnumeric():
                        self.list_wins_properties[keys[index]]=test_value
                    else:
                        self.list_wins_properties[keys[index]]=test_value+'Error*'
                        err=1
                elif keys[index]=='pos_y':
                    test_value=self.list_inputs[index].get()
                    if test_value=='center' or test_value.isnumeric():
                        self.list_wins_properties[keys[index]]=test_value
                    else:
                        self.list_wins_properties[keys[index]]=test_value+'Error*'
                        err=1
                elif keys[index]=='bg':
                    test_value=self.list_inputs[index].get()
                    try:
                        self.second_frame.config(bg=test_value)
                        self.list_wins_properties[keys[index]]=test_value
                    except:
                        self.list_wins_properties[keys[index]]=test_value+'Error*'
                        err=1
                elif keys[index]=='height':
                    test_value=self.list_inputs[index].get()
                    try:
                        test_value=int(test_value)
                        if not self.ConsolHide:
                            if test_value<=round(0.82907*self.height_available_center):
                                self.my_canvas.place_configure(height=test_value)
                                self.main_frame.place_configure(height=test_value+17)
                                
                            elif test_value>round(0.82907*self.height_available_center):
                                self.my_canvas.place_configure(height=round(0.82907*self.height_available_center)-17)
                                self.main_frame.place_configure(height=round(0.82907*self.height_available_center))
                                
                        else:
                            if test_value>=round(0.82907*self.height_available_center)+round(0.16877*self.height_available_center):
                                self.my_canvas.place_configure(height=round(0.82907*self.height_available_center)+round(0.16877*self.height_available_center)-17)
                                self.main_frame.place_configure(height=round(0.82907*self.height_available_center)+round(0.16877*self.height_available_center))
                            else:
                                self.my_canvas.place_configure(height=test_value)
                                self.main_frame.place_configure(height=test_value+17)
                                
                        self.my_canvas.itemconfigure(self.win,height=test_value)
                        self.my_canvas.configure(scrollregion=(0,0,self.win_width,test_value))
                        self.list_wins_properties[keys[index]]=test_value
                        self.win_height=test_value
                            
                    except:
                        self.list_wins_properties[keys[index]]=str(test_value)+'Error*'
                        err=1
                elif keys[index]=='width':
                    test_value=self.list_inputs[index].get()
                    try:
                        test_value=int(test_value)
                        if test_value<=round(0.6412*self.width_available)-17:
                            self.my_canvas.place_configure(width=test_value)
                            self.main_frame.place_configure(width=test_value+17)
                        elif test_value>=round(0.6412*self.width_available)-17:
                            self.my_canvas.place_configure(width=round(0.6412*self.width_available)-17)
                            self.main_frame.place_configure(width=round(0.6412*self.width_available))
                        self.my_canvas.itemconfigure(self.win,width=test_value)
                        self.my_canvas.configure(scrollregion=(0,0,test_value,self.win_height))
                        self.list_wins_properties[keys[index]]=test_value
                        self.win_width=test_value
                    except:
                        self.list_wins_properties[keys[index]]=str(test_value)+'Error*'
                        err=1
                elif keys[index]=='overrideredirect':
                    test_value=self.list_inputs[index].get()
                    if test_value in ['0','1']:
                        self.list_wins_properties[keys[index]]=test_value
                elif keys[index]=='topmost':
                    test_value=self.list_inputs[index].get()
                    if test_value in ['0','1']:
                        self.list_wins_properties[keys[index]]=test_value
                elif keys[index]=='title':
                    test_value=self.list_inputs[index].get()
                    if test_value!='':
                        self.list_wins_properties[keys[index]]=test_value
                
                elif keys[index]=='icon':
                    try:
                        test_value=self.list_inputs[index].get()
                        if '.ico' in test_value:
                            self.list_wins_properties[keys[index]]=test_value
                        else:
                            self.list_wins_properties[keys[index]]='None'
                    except:
                        self.list_widgets_on_wins_properties[value][keys[index]]=test_value+'Error*'
                        err=1
                
                self.main_frame.place_configure(x=18+round(0.1584*self.width_available)+30,y=87)
                if err:
                    self.list_inputs[index].config(highlightthickness=1,highlightbackground='red',highlightcolor='red')
                else:
                    if type(self.list_inputs[index]) is Entry:
                        self.list_inputs[index].config(highlightthickness=0,highlightbackground='black',highlightcolor='red')
                Error=Error or err
                self.Error_win=Error
            if Error:
                self.listbox_widgets_on_win.itemconfig(0,{'fg':'red'})
            else:
                self.listbox_widgets_on_win.itemconfig(0,{'fg':themes[self.Theme]["other labels"]})
        except:
            pass
    def add_external_win(self):
        try:
            if self.registered:
                path_win=filedialog.askopenfilename()
                if path_win:
                    list_path=path_win.split('/')
                    win_name=list_path[-1].split('.')[0]
                    if list_path[-1].split('.')[1]=='uiELPRINCE':
                        wins=self.listbox_wins.get(0,END)
                        win=win_name
                        while win_name in wins:
                            win_name=win_name+'_copy'
                        shutil.copy(path_win, self.path_project+'\\'+win_name+'.uiELPRINCE')
                        self.listbox_wins.insert(END,win_name)
                        # self.open_win_th(len(wins),win)
                        # self.save_win()
                        #self.list_wins_properties['id']=current_win
            else:
                masgbox=messagebox.showinfo('Register','You must register TK Design to enable this feature.')
        except:
            pass
    def add_win(self):
        try:
            if self.registered:
                wins=self.listbox_wins.get(0,END)
                new_win_name='win'+str(self.num_inserted_win)
                while new_win_name in wins:
                    new_win_name+='_copy'
                    
                self.listbox_wins.insert(END,new_win_name)
                self.num_inserted_win+=1
            else:
                masgbox=messagebox.showinfo('Register','You must register TK Design to enable this feature.')
        except:
            pass
    def ReInitParams(self):
        try:
            self.list_widgets_on_wins_properties=[]
            self.list_nums=[]
            for widget in widgets:
                self.list_nums.append(1)
            self.WinHide=False
            self.list_widgets_on_wins=[]
            self.list_frames_on_wins=[]
            self.list_widgets_on_wins_Errors=[]
            self.Error_win=0
            self.list_wins_properties=copy.deepcopy(win_properties_defaults)
            self.list_wins_properties['width']=round(0.6412*self.width_available)-17
            self.list_wins_properties['height']=round(0.82907*self.height_available_center)-17
            self.win_width=round(0.6412*self.width_available)-17
            self.win_height=round(0.82907*self.height_available_center)-17
            self.list_vars=[]
            self.list_entry=[]
            self.list_inputs=[]
            
            self.images=[]
            self.selected=()
            self.num_widget=-1
            self.selected_master=0
            self.index_RemovedWidget=-1
            self.posx_mouse_widget=0
            self.posy_mouse_widget=0
            self.CodeHide=1
            self.prev_SelectedWidget=-1
            
            self.listbox_widgets_on_win.delete(0,END)
            if self.ConsolHide:
                self.bt_hide_consol_com()
            self.my_canvas_right.delete(self.win_right)
            self.my_canvas.delete(self.win)
            del self.second_frame
            self.second_frame=Frame(self.my_canvas,bg='white')
            self.second_frame.bind('<Button-1>',self.properties_win)
            self.second_frame.bind('<Button-3>',self.RightClick)
            #self.second_frame.bind('<Motion>',self.th_posx_posy)
            self.win=self.my_canvas.create_window((0,0),window=self.second_frame,anchor='nw',width=round(0.6412*self.width_available)-17,height=round(0.82907*self.height_available_center)-17)
            self.window.entryconfig('Close current window',state='normal')
            # self.lbl_filename.place_forget()
            # self.lbl_filename_txt.place_forget()
            # self.bt_exit_win.place_forget()
            # self.main_frame.place_forget()
            self.lbl_filename.place(x=18+round(0.1584*self.width_available)+30,y=62,height=25,width=round(0.6412*self.width_available))
            self.lbl_filename_txt.place(x=18+round(0.1584*self.width_available)+30+5,y=62,height=25)
            self.bt_exit_win.place(x=18+round(0.1584*self.width_available)+30+round(0.6412*self.width_available)-20,y=62,height=25,width=20)
            self.main_frame.place(x=18+round(0.1584*self.width_available)+30,y=87,width=round(0.6412*self.width_available),height=round(0.82907*self.height_available_center))
            ###################
        except:
            pass
    def new_proj(self):
        try:
            self.main.destroy()
            self.__init__()
        except:
            pass
    def save_win(self):
        try:
            widgets_types=[]
            wins=list(self.listbox_wins.get(0,END))
            
            for widget in self.list_widgets_on_wins:
                if type(widget) is Button:
                    widgets_types.append('Button')
                elif type(widget) is Listbox:
                    widgets_types.append('Listbox')
                elif type(widget) is Label:
                    widgets_types.append('Label')
                elif type(widget) is Canvas:
                    widgets_types.append('Canvas')
                elif type(widget) is Entry:
                    widgets_types.append('Entry')
                elif type(widget) is Checkbutton:
                    widgets_types.append('Checkbutton')
                elif type(widget) is Radiobutton:
                    widgets_types.append('Radiobutton')
                elif type(widget) is Text:
                    widgets_types.append('Text')
                elif type(widget) is ttk.Scrollbar:
                    widgets_types.append('Scrollbar')
                elif type(widget) is ttk.Combobox:
                    widgets_types.append('Combobox')
                elif type(widget) is ttk.Treeview:
                    widgets_types.append('Treeview')
                elif type(widget) is Frame:
                    widgets_types.append('Frame')
            
            
           
            widgets_names_before=list(self.listbox_widgets_on_win.get(0,END))[1:]
            
            widgets_names=widgets_names_before.copy()
            
            
            widgets_arranged=[]
            masters=[wins[self.pointer_win]]
            
            while True:
                group=[]
                for master in masters:
                    index=0
                    for item in widgets_names:
                        if self.list_widgets_on_wins_properties[index]['master']==master:
                            group.append(item)
                        index+=1
                if group==[]:
                    break
                masters=group.copy()
                widgets_arranged.extend(group)
                
            self.listbox_widgets_on_win.delete(0,END)
            self.listbox_widgets_on_win.insert(END,wins[self.pointer_win])
            for name in widgets_arranged:
                
                self.listbox_widgets_on_win.insert(END,name)
            
            
            
            ################# sorting
            properties_copy=self.list_widgets_on_wins_properties.copy()
            widgets_errors=self.list_widgets_on_wins_Errors.copy()
            widgets_on_wins=self.list_widgets_on_wins.copy()
            frames_on_wins=self.list_frames_on_wins.copy()
            widgets_types_copy=widgets_types.copy()
            
            
            args=[properties_copy,widgets_names,widgets_errors,widgets_types_copy,widgets_on_wins,frames_on_wins]
            args=self.SortingRest(widgets_arranged,widgets_names,args)
            
            properties_copy=args[0]
            widgets_names=args[1]
            widgets_errors=args[2]
            widgets_types_copy=args[3]
            widgets_on_wins=args[4]
            frames_on_wins=args[5]
            
            
            
            
            ############## adding non exists with errors
            indx=0
            for name in widgets_names_before:
                if not name in widgets_names:
                    widgets_names.append(name)
                    properties_copy.append(self.list_widgets_on_wins_properties[indx])
                    widgets_errors.append(self.list_widgets_on_wins_Errors[indx])
                    widgets_types_copy.append(widgets_types[indx])
                    widgets_on_wins.append(self.list_widgets_on_wins[indx])
                    frames_on_wins.append(self.list_frames_on_wins[indx])
                indx+=1
            
            self.list_widgets_on_wins_properties=properties_copy.copy()
            self.list_widgets_on_wins_Errors=widgets_errors.copy()
            widgets_types=widgets_types_copy.copy()
            self.list_widgets_on_wins=widgets_on_wins.copy()
            self.list_frames_on_wins=frames_on_wins.copy()
            
            
            ####################################################
            with open(self.path_project+'\\'+wins[self.pointer_win]+'.uiELPRINCE','w') as f1:
                f1.write(repr(self.list_wins_properties)+'\n'+repr(self.list_widgets_on_wins_properties))
                f1.write('\n'+repr(widgets_names))
                f1.write('\n'+repr(self.list_nums))
                f1.write('\n'+repr(self.list_widgets_on_wins_Errors))
                f1.write('\n'+str(self.Error_win))
                f1.write('\n'+str(widgets_types))
                
                
            #self.bt_export_com()
            td=self.text.get('1.0','end')
            # self.text.insert('1.0','from self_code import SelfCode\n')
            # self.text.insert('2.0',f'class {self.proj_name}(SelfCode):\n')
            if '\n' in td:
                list_lines=td.splitlines()
                index_line_class=-1
                index_line_import=-1
                index=0
                for line in list_lines:
                    if f'{self.proj_name}' in line and 'class' in line:
                        index_line_class=index
                    if f'{wins[self.pointer_win]}_code' in line and 'import' in line:
                        index_line_import=index
                    index+=1
                if not f'{wins[self.pointer_win].capitalize()}Code' in list_lines[index_line_class]:
                    list_lines[index_line_class]=list_lines[index_line_class].replace('):',f',{wins[self.pointer_win].capitalize()}Code):')
                if index_line_import==-1:
                    list_lines.insert(0,f'from {wins[self.pointer_win]}_code import {wins[self.pointer_win].capitalize()}Code')
                
                self.text.delete('1.0',END)
                index=1
                for line in list_lines:
                    self.text.insert(f'{index}.0',line+'\n')
                    index+=1
                self.UpdateColors(None)
                with open(self.path_project+'\\'+self.proj_name+'.py','w') as f1:
                    for line in list_lines:
                        f1.write(line+'\n')
            if any(self.list_widgets_on_wins_Errors) or self.Error_win:
                pass
            else:
                self.bt_export_com()
            self.lbl_status.config(text='saved!')
        except:
            pass
    def SaveProj(self):
        try:
            with open(self.path_project+'\\'+self.proj_name+'.config','w') as f1:
                f1.write(repr(self.listbox_wins.get(0,END))+'\n')
                f1.write(str(self.num_inserted_win)+'\n')
                f1.write(str(self.pointer_win)+'\n')
                f1.write(str(self.proj_name))
        except:
            pass
    def DeleteWidget(self,e=None):
        try:
            if self.selected[0]!=-1:
                value=self.selected[0]-1
                SelectedWidget=self.listbox_widgets_on_win.get(value+1)
                if value!=-1: ### not win its widget
                    index=0
                    widgets=self.list_widgets_on_wins.copy()
                    widgets_listbox=list(self.listbox_widgets_on_win.get(0,END))
                    num_RemovedWidgets=0
            
                    for widget in self.list_widgets_on_wins:
                        if str(self.list_widgets_on_wins[value]).split('.!') == str(widget).split('.!')[:len(str(self.list_widgets_on_wins[value]).split('.!'))] and index!=value:
                            widgets_listbox.pop(index+1-num_RemovedWidgets)
                            self.list_frames_on_wins.pop(index-num_RemovedWidgets)
                            self.list_widgets_on_wins_Errors.pop(index-num_RemovedWidgets)
                            
                            self.list_widgets_on_wins_properties.pop(index-num_RemovedWidgets)
                            widgets.pop(index-num_RemovedWidgets)
                            num_RemovedWidgets+=1
                        index+=1
                    self.list_widgets_on_wins=widgets
                    self.listbox_widgets_on_win.delete(0,END)
                    index_widget=0
                    for widget_name in widgets_listbox:
                        self.listbox_widgets_on_win.insert(END,widget_name)
                        if index_widget!=0:
                            if self.list_widgets_on_wins_Errors[index_widget-1]==1:
                                self.listbox_widgets_on_win.itemconfig(END,{'fg':'red'})
                        index_widget+=1
                    value=widgets_listbox.index(SelectedWidget)-1
                    self.listbox_widgets_on_win.delete(value+1)
                    self.list_frames_on_wins[value].place_forget()
                    self.list_frames_on_wins[value].pack_forget()
                    self.list_frames_on_wins.pop(value)
                    self.list_widgets_on_wins.pop(value)
                    self.list_widgets_on_wins_Errors.pop(value)
                    
                    self.list_widgets_on_wins_properties.pop(value)
                    self.prev_SelectedWidget=-1
                    self.selected=(-1,)
                    self.my_canvas_right.delete(self.win_right)
                    del self.second_frame_right
        except:
            pass
                
    def DeleteWin(self,e):
        try:
            selected=self.listbox_wins.curselection()
            if selected:
                value=selected[0]
                if len(self.listbox_wins.get(0,END)) !=1 and value!=self.pointer_win:
                    ## ask for sure
                    choice=messagebox.askyesno("Warnning","Are you sure to delete "+self.listbox_wins.get(value))
                    if choice:
                        ## deleting
                        self.listbox_wins.delete(value)
                        if value<self.pointer_win:
                            self.pointer_win-=1
                            self.properties_win(None)
        except:
            pass
    def ClickWidget(self,e):
        try:
            value=self.prev_SelectedWidget
            if value!=-1:
                self.list_frames_on_wins[value].update()
                self.list_widgets_on_wins[value].pack_configure(padx=0,pady=0)
            
            if e==None:
                self.selected=(0,)
                self.edit.entryconfig('Send to back',state='disabled')
                self.edit.entryconfig('Send to front',state='disabled')
                self.edit.entryconfig('Bring to back',state='disabled')
                self.edit.entryconfig('Bring to front',state='disabled')
                self.edit.entryconfig('Copy widget',state='disabled')
            else:
                ###################################### getting index of the frame
                if str(e).isnumeric():
                    value=e-1
                else:
                    value=self.list_widgets_on_wins.index(e.widget)
                #######################################
                #print(value)
                self.selected=(value+1,)
                if value!=-1:
                    if e!=None and not str(e).isnumeric():
                        self.posx_mouse_widget=e.x
                        self.posy_mouse_widget=e.y
                    self.list_widgets_on_wins[value].pack_configure(padx=2,pady=2)
                    if not str(e).isnumeric():
                        self.loading_properties(value+1,1)
                    self.prev_SelectedWidget=value
                    
                    self.edit.entryconfig('Copy widget',state='normal')
                    #self.listbox_widgets_on_win.selection_clear(0,END)
                    if value==0:
                        self.edit.entryconfig('Send to back',state='disabled')
                        self.edit.entryconfig('Send to front',state='normal')
                        self.edit.entryconfig('Bring to back',state='disabled')
                        self.edit.entryconfig('Bring to front',state='normal')
                    elif value==len(self.list_widgets_on_wins)-1:
                        self.edit.entryconfig('Send to back',state='normal')
                        self.edit.entryconfig('Send to front',state='disabled')
                        self.edit.entryconfig('Bring to back',state='normal')
                        self.edit.entryconfig('Bring to front',state='disabled')
                    else:
                        self.edit.entryconfig('Send to back',state='normal')
                        self.edit.entryconfig('Send to front',state='normal')
                        self.edit.entryconfig('Bring to back',state='normal')
                        self.edit.entryconfig('Bring to front',state='normal')
        except:
            pass
    def split_nums(self,txt):
        try:
            nums=''
            for i in txt:
                if i.isnumeric():
                    nums=nums+i
            if nums=='':
                nums='1'
            return int(nums)
        except:
            pass
    def properties_win(self,e):
        try:
            self.selected=(0,)
            self.loading_properties(0,1)
            self.ClickWidget(None)
        except:
            pass
    def ResizingWidgets(self,e):
        try:
            value=self.list_frames_on_wins.index(e.widget)
            if self.list_frames_on_wins[value].place_info()!={}:
                self.list_frames_on_wins[value].place_configure(width=e.x,height=e.y)
                self.list_frames_on_wins[value].update()
                frame_width=self.list_frames_on_wins[value].winfo_width()
                frame_height=self.list_frames_on_wins[value].winfo_height()
                
                self.list_widgets_on_wins_properties[value]['width']=frame_width
                self.list_widgets_on_wins_properties[value]['height']=frame_height
                keys=list(self.list_widgets_on_wins_properties[value].keys()) 
                index_width=keys.index('width')
                self.list_inputs[index_width].delete(0,END)
                self.list_inputs[index_width].insert(END,str(frame_width))
                index_height=keys.index('height')
                self.list_inputs[index_height].delete(0,END)
                self.list_inputs[index_height].insert(END,str(frame_height))
        except:
            pass
    def MovingWidget(self,e):
        try:
            widget=e.widget
            value=self.list_widgets_on_wins.index(widget)
            if self.list_frames_on_wins[value].place_info()!={}:
                
                try:
                    masters=self.listbox_widgets_on_win.get(0,END)
                    x_pos=0
                    y_pos=0
                    index_master=-1
                    index_widget=value
                    while index_master!=0:
                        if index_master!=-1:
                            x_pos+=int(self.list_widgets_on_wins_properties[index_master-1]['x'])
                            y_pos+=int(self.list_widgets_on_wins_properties[index_master-1]['y'])
                            index_widget=index_master-1
                        master=self.list_widgets_on_wins_properties[index_widget]['master']
                        index_master=masters.index(master)
                    
                    
                    height_win=int(self.list_wins_properties['height'])
                    width_win=int(self.list_wins_properties['width'])
                    pos_scrollbary=self.my_scrollbar.get()[0]
                    pos_scrollbarx=self.my_scrollbar2.get()[0]
                    marginy=int(pos_scrollbary*height_win)
                    marginx=int(pos_scrollbarx*width_win)
                    
                    
                    
                    
                    posx_mainframe=int(self.main_frame.place_info()['x'])+x_pos
                    posy_mainframe=int(self.main_frame.place_info()['y'])+y_pos
                    
                    keys=list(self.list_widgets_on_wins_properties[value].keys()) 
                    index_x=keys.index('x')
                    self.list_inputs[index_x].delete(0,END)
                    
                    self.list_inputs[index_x].insert(END,str(e.x_root-posx_mainframe-self.posx_mouse_widget+marginx))
                    index_y=keys.index('y')
                    self.list_inputs[index_y].delete(0,END)
                    self.list_inputs[index_y].insert(END,str(e.y_root-posy_mainframe-43-self.posy_mouse_widget+marginy))
                    self.list_widgets_on_wins_properties[value]['x']=str(e.x_root-posx_mainframe-self.posx_mouse_widget+marginx)
                    self.list_widgets_on_wins_properties[value]['y']=str(e.y_root-posy_mainframe-43-self.posy_mouse_widget+marginy)
                    self.list_frames_on_wins[value].place_configure(x=e.x_root-posx_mainframe-self.posx_mouse_widget+marginx,y=e.y_root-posy_mainframe-43-self.posy_mouse_widget+marginy)
                except:
                    pass
        except:
            pass
    def RightClick(self,e):
        try:
            self.my_menu_design.tk_popup(e.x_root, e.y_root)
        except:
            pass
    def RightClickText(self,e):
        try:
            self.my_menu_text.tk_popup(e.x_root, e.y_root)
        except:
            pass
    def ShowDesign(self):
        try:
            self.CodeHide=1
            self.text.place_forget()
            self.my_scrollbar.pack_forget()
            self.my_scrollbar2.pack_forget()
               
            self.my_canvas.place(x=0,y=0,width=round(0.6412*self.width_available)-17,height=round(0.82907*self.height_available_center)-17)
            
            self.my_scrollbar=ttk.Scrollbar(self.main_frame,orient=VERTICAL,command=self.my_canvas.yview)
            self.my_scrollbar.pack(side=RIGHT,fill=Y)
            
            self.my_scrollbar2=ttk.Scrollbar(self.main_frame,orient=HORIZONTAL,command=self.my_canvas.xview)
            self.my_scrollbar2.pack(side=BOTTOM,fill=X)
            
            self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
            self.my_canvas.configure(xscrollcommand=self.my_scrollbar2.set)
            self.loading_properties(0,1)
            self.click_enter(0)
            self.window.entryconfig('Show design',state='disabled')
            self.window.entryconfig('Show code',state='normal')
            self.edit.entryconfig('Copy widget',state='disabled')
            
            self.edit.entryconfig('Send to back',state='disabled')
            self.edit.entryconfig('Send to front',state='disabled')
            self.edit.entryconfig('Bring to back',state='disabled')
            self.edit.entryconfig('Bring to front',state='disabled')
        except:
            pass
    def ShowCode(self):
        try:
            if self.registered:
                self.CodeHide=0
                self.my_canvas.place_forget()
                self.my_scrollbar.pack_forget()
                self.my_scrollbar2.pack_forget()
                self.main_frame.place(x=18+round(0.1584*self.width_available)+30,y=87,width=round(0.6412*self.width_available),height=round(0.82907*self.height_available_center))
                self.text.place(x=0,y=0,width=round(0.6412*self.width_available)-17,height=round(0.82907*self.height_available_center)-17)
                
                self.my_scrollbar=ttk.Scrollbar(self.main_frame,orient=VERTICAL,command=self.text.yview)
                self.my_scrollbar.pack(side=RIGHT,fill=Y)
                self.text.config(yscrollcommand = self.my_scrollbar.set)
                self.my_scrollbar2=ttk.Scrollbar(self.main_frame,orient=HORIZONTAL,command=self.text.xview)
                self.my_scrollbar2.pack(side=BOTTOM,fill=X)
                self.text.config(xscrollcommand = self.my_scrollbar2.set)
                
                self.highlight_current_line()
                
                self.window.entryconfig('Show design',state='normal')
                self.window.entryconfig('Show code',state='disabled')
                self.edit.entryconfig('Copy widget',state='disabled')
                self.edit.entryconfig('Paste widget',state='disabled')
                self.edit.entryconfig('Send to back',state='disabled')
                self.edit.entryconfig('Send to front',state='disabled')
                self.edit.entryconfig('Bring to back',state='disabled')
                self.edit.entryconfig('Bring to front',state='disabled')
            else:
                masgbox=messagebox.showinfo('Register','You must register TK Design to enable this feature.')
        except:
            pass
    def CorrectColors(self,e):
        try:
            Line=''
            if type(e) is str:
                line=e
            else:
                line, col = self.text.index('insert').split('.')
            
            #line=str(int(line)-1)
            td=self.text.get(line+'.0','end')
            # print(line)
            # print(td)
            indexes_blue=self.GetIndexes(line)
            #print(indexes_blue)
            keys=list(indexes_blue.keys())
            count=0
            for index in indexes_blue.keys():
                start=index
                end=start+indexes_blue[index][0]
                if count+1 !=len(keys):
                    self.text.tag_remove("gray", f"{line}.{end}", f"{line}.{keys[count+1]}")
                    self.text.tag_remove("cyan", f"{line}.{end}", f"{line}.{keys[count+1]}")
                    self.text.tag_remove("yellow", f"{line}.{end}", f"{line}.{keys[count+1]}")
                    self.text.tag_remove("green", f"{line}.{end}", f"{line}.{keys[count+1]}")
                    self.text.tag_remove("orange", f"{line}.{end}", f"{line}.{keys[count+1]}")
                    self.text.tag_remove("red", f"{line}.{end}", f"{line}.{keys[count+1]}")
                    self.text.tag_remove("purple", f"{line}.{end}", f"{line}.{keys[count+1]}")
                else:
                    self.text.tag_remove("gray", f"{line}.{end}", f"{line}.{len(td)}")
                    self.text.tag_remove("cyan", f"{line}.{end}", f"{line}.{len(td)}")
                    self.text.tag_remove("yellow", f"{line}.{end}", f"{line}.{len(td)}")
                    self.text.tag_remove("green", f"{line}.{end}", f"{line}.{len(td)}")
                    self.text.tag_remove("orange", f"{line}.{end}", f"{line}.{len(td)}")
                    self.text.tag_remove("red", f"{line}.{end}", f"{line}.{len(td)}")
                    self.text.tag_remove("purple", f"{line}.{end}", f"{line}.{len(td)}")
                self.text.tag_add(indexes_blue[index][1], f"{line}.{start}", f"{line}.{end}")
                self.text.tag_config('purple',foreground="#c670e0")
                self.text.tag_config("red",foreground="#ee5c51")
                self.text.tag_config("orange",foreground="#fa9b4e")
                self.text.tag_config("green",foreground="#82e686")
                self.text.tag_config("yellow",foreground="#faed5c")
                self.text.tag_config("cyan",foreground="#57d6e4")
                self.text.tag_config("gray",foreground="#999999")
                count+=1
            if indexes_blue=={}:
                self.text.tag_remove("purple", f"{line}.{0}", f"{line}.{len(td)}")
                self.text.tag_remove("red", f"{line}.{0}", f"{line}.{len(td)}")
                self.text.tag_remove("orange", f"{line}.{0}", f"{line}.{len(td)}")
                self.text.tag_remove("green", f"{line}.{0}", f"{line}.{len(td)}")
                self.text.tag_remove("yellow", f"{line}.{0}", f"{line}.{len(td)}")
                self.text.tag_remove("cyan", f"{line}.{0}", f"{line}.{len(td)}")
                self.text.tag_remove("gray", f"{line}.{0}", f"{line}.{len(td)}")
            #self.th1.join()
        except:
            pass
    def CheckAlone(self,i,td,index):
        try:
            end=index+len(i)-1
            boolean=True
            if index!=0:
                if not td[index-1] in [' ',':','(',')','@','.','=',',']:
                    boolean=False
            if end!=len(td)-1:
                if not td[end+1] in [' ',':','(',')','@','.','=',',']:
                    boolean=False
            return boolean
        except:
            pass
    def FindText(self,i,td):
        try:
            indexes=[]
            for k in range(0,len(td)):
                if td[k:].find(i)!=-1:
                    index=td[k:].find(i)+k
                    if not index in indexes:
                        indexes.append(index)
                else:
                    break
            return indexes
        except:
            pass
    def highlight_current_line(self, interval=200):
        try:
            self.text.tag_remove("current_line", 1.0, "end")
            self.text.tag_add("current_line", "insert linestart", "insert lineend+1c")
            self.after(interval, self.highlight_current_line)
        except:
            pass
    def qoutes(self,e):
        try:
            line, col = self.text.index('insert').split('.')
            self.text.insert(line+'.'+col,'"')
        except:
            pass
    def tab(self,e):
        try:
            content = self.text.selection_get()
            content_lines=content.splitlines()
            for index in range(0,len(content_lines)):
                content_lines[index]=" "*4+content_lines[index]
            #print(content_lines)
            index_line_start = self.text.index("sel.first")
            index_line_end = self.text.index("sel.last")
            self.text.delete(str(int(float(index_line_start)))+'.0',
                             str(int(float(index_line_end))+1)+'.0')
            # print(index_line_end)
            # print(index_line_start)
            count=0
            #print(content_lines)
            for line in content_lines:
                self.text.insert(str(int(float(index_line_start))+count)+'.0','\n')
                self.text.insert(str(int(float(index_line_start))+count)+'.0',line)
                count+=1
            self.UpdateColors(None)
        except:
            self.text.insert(INSERT, " " * 4)
        return 'break'
    def EnterClick(self,e):
        try:
            line, col = self.text.index('insert').split('.')
            td = self.text.get(line+'.0','end')
            #print(td)
            if '\n' in td:
                td=td.split('\n')[0]
            #print(td)
            if len(td)!=int(col):
                # there are words after enter
                if td[int(col)-1]==':':
                    self.text.insert(line+'.'+col,'\n')
                    num_tabs=self.get_num_tabs(td)
                    self.text.insert(INSERT, " " * (num_tabs+1)*4)
                else:
                    self.text.insert(line+'.'+col,'\n')
                    num_tabs=self.get_num_tabs(td)
                    self.text.insert(INSERT, " " * (num_tabs)*4)
                #self.CorrectColors(line)
                return 'break'
            else:
                # no words after enter
                if len(td)!=0:
                    if (td[-1]==':'):
                        self.text.insert(line+'.'+str(len(td)),'\n')
                        num_tabs=self.get_num_tabs(td)
                        self.text.insert(INSERT, " " * (num_tabs+1)*4)
                    else:
                        self.text.insert(line+'.'+str(len(td)),'\n')
                        num_tabs=self.get_num_tabs(td)
                        self.text.insert(INSERT, " " * (num_tabs)*4)
                    #self.CorrectColors(line)
                    return 'break'
        except:
            pass
    def get_num_tabs(self,td):
        try:
            a=td.strip()
            num=int(td.find(a)/4)
            return num
        except:
            pass
    def GetIndexes(self,line):
        # line, col = self.text.index('insert').split('.')
        # td = self.text.get('current linestart', 'current lineend')
        # line, col = self.text.index('insert').split('.')
        # line=str(int(line)-1)
        try:
            td=self.text.get(line+'.0','end')
            if '\n' in td:
                td=td.splitlines()[0]
            indexes_blue={}
            for i in self.list_purple:
                if i in td:
                    indexes=self.FindText(i,td)
                    for index in indexes:
                        boolean=self.CheckAlone(i,td,index)
                        if boolean:
                            indexes_blue[index]=[len(i),'purple']
            for i in self.list_red:
                if i in td:
                    indexes=self.FindText(i,td)
                    for index in indexes:
                        boolean=self.CheckAlone(i,td,index)
                        if boolean:
                            indexes_blue[index]=[len(i),'red']
            for i in self.list_orange:
                if i in td:
                    indexes=self.FindText(i,td)
                    for index in indexes:
                        boolean=self.CheckAlone(i,td,index)
                        if boolean:
                            indexes_blue[index]=[len(i),'orange']
            indexes_blue.update(self.GetString(td))
            indexes_blue.update(self.GetNums(td))
            indexes_blue.update(self.GetIndexesDefClass(td))
            indexes_blue.update(self.GetIndexesComments(td))
            ## ordering
            indexes_blue=dict(sorted(indexes_blue.items()))
            keys_to_delete=[]
            for key1 in indexes_blue.keys():
                for key2 in indexes_blue.keys():
                    if key2>key1 and indexes_blue[key2][0]+key2<indexes_blue[key1][0]+key1:
                        keys_to_delete.append(key2)
            for key in keys_to_delete:
                indexes_blue.pop(key)
            return indexes_blue
        except:
            pass
    def GetString(self,td):
        try:
            indexes=[]
            index=[]
            if '\'' in td or "\"" in td:
                for k in range(0,len(td)):
                    if td[k]=='\'':
                        index.append(k)
                        if len(index)==2:
                            indexes.append(index)
                            index=[]
                for k in range(0,len(td)):
                    if td[k]=="\"":
                        index.append(k)
                        if len(index)==2:
                            indexes.append(index)
                            index=[]
            dict_indexes={}
            for list in indexes:
                dict_indexes[list[0]]=[list[1]-list[0]+1,'green']
            keys_to_delete=[]
            for key1 in dict_indexes.keys():
                for key2 in dict_indexes.keys():
                    if key2>key1 and dict_indexes[key2][0]+key2<dict_indexes[key1][0]+key1:
                        keys_to_delete.append(key2)
            for key in keys_to_delete:
                dict_indexes.pop(key)
            return dict_indexes
        except:
            pass
    def GetNums(self,td):
        try:
            indexes=[]
            index=[]
            for k in range(0,len(td)):
                if k!=0:
                    if td[k].isnumeric() and (td[k-1] in [' ',':','(',')','@','.','=',',','+','-','[',']','*','/']):
                        index.append(k)
                else:
                    if td[k].isnumeric():
                        index.append(k)
                if k!=len(td)-1:
                    if len(index)==1:
                        if td[k].isnumeric() and td[k+1] in [' ',':','(',')','@','.','=',',','+','-','[',']','*','/']:
                            index.append(k)
                else:
                    if len(index)==1:
                        if td[k].isnumeric():
                            index.append(k)
                if len(index)==2:
                    indexes.append(index)
                    index=[]
            dict_indexes={}
            for list in indexes:
                dict_indexes[list[0]]=[list[1]-list[0]+1,'yellow']
            return dict_indexes
        except:
            pass
    def GetIndexesDefClass(self,td):
        try:
            indexes=[]
            index=[]
            dict_indexes={}
            for k in range(0,len(td)):
                if td[k:].find('class')!=-1:
                    index.append(td[k:].find('class')+k+len('class')+1)
                    if td[k:].find('(')+k-1>td[k:].find('class')+k+len('class')+1:
                        index.append(td[k:].find('(')+k-1)
                        if not index in indexes:
                            indexes.append(index)
                        index=[]
                if td[k:].find('def')!=-1:
                    index.append(td[k:].find('def')+k+len('def')+1)
                    if td[k:].find('(')+k-1>td[k:].find('def')+k+len('def')+1:
                        index.append(td[k:].find('(')+k-1)
                        if not index in indexes:
                            indexes.append(index)
                        index=[]
            for list in indexes:
                dict_indexes[list[0]]=[list[1]-list[0]+1,'cyan']
            return dict_indexes
        except:
            pass
    def GetIndexesComments(self,td):
        try:
            dict_indexes={}
            if td.find('#') !=-1:
                dict_indexes={td.find('#'):[len(td)-td.find('#'),'gray']}
            return dict_indexes
        except:
            pass
    def UpdateColors(self,e):
        try:
            self.text.config(state='disabled')
            AllText=self.text.get('1.0','end')
            lines=AllText.split('\n')
            #print(lines)
            for index in range(1,len(lines)+1):
                self.CorrectColors(str(index))
            self.text.config(state='normal')
        except:
            pass
    def ShiftTab(self,e):
        try:
            content = self.text.selection_get()
            content_lines=content.splitlines()
            if content_lines[0][0:4]==' '*4:
                for index in range(0,len(content_lines)):
                    content_lines[index]=content_lines[index][4:]
                #print(content_lines)
                index_line_start = self.text.index("sel.first")
                index_line_end = self.text.index("sel.last")
                self.text.delete(str(int(float(index_line_start)))+'.0',
                                 str(int(float(index_line_end))+1)+'.0')
                #print(index_line_end)
                #print(index_line_start)
                count=0
                #print(content_lines)
                for line in content_lines:
                    self.text.insert(str(int(float(index_line_start))+count)+'.0','\n')
                    self.text.insert(str(int(float(index_line_start))+count)+'.0',line)
                    count+=1
                self.UpdateColors(None)
            return 'break'
        except:
            pass
        
    def paste(self,e):
        try:
            clipboard = self.clipboard_get()
            #clipboard = clipboard.replace("\n", "\\n")
            try:
                start = self.text.index("sel.first")
                end = self.text.index("sel.last")
                self.text.delete(start, end)
            except TclError:
                pass
    
            self.text.insert("insert", clipboard)
            self.UpdateColors(None)
            return 'break'
        except:
            pass
    def ExitFcn(self):
        # th=Thread(target=self.th_ExitFcn)
        # th.start()
        self.th_ExitFcn()
    def th_ExitFcn(self):
        try:
            self.main.withdraw()
            self.save_win()
            self.SaveProj()
            self.main.destroy()
            self.destroy()
            sys.exit()
        except:
            pass
    def ControlC(self,e=None):
        try:
            if self.selected!=() and self.CodeHide:
                if self.selected[0]!=0:
                    #self.WidgetLastCopied
                    value=self.selected[0]-1
                    if self.list_widgets_on_wins_Errors[value]==0:
                        self.WidgetLastCopied=value
                        self.list_widgets_on_wins_copy_use=self.list_widgets_on_wins.copy()
                        self.list_widgets_on_wins_properties_copy_use=self.list_widgets_on_wins_properties.copy()
                        self.my_menu_design.entryconfig('Paste',state='normal')
                        self.my_menu_widget.entryconfig('Paste',state='normal')
                        self.edit.entryconfig('Paste widget',state='normal')
                    else:
                        msgbox=messagebox.showinfo("Error!","Check errors in the widget!")
        except:
            pass
    def ControlV(self,e=None):
       
        # self.list_widgets_on_wins
        # self.list_widgets_on_wins_properties
        
        try:
            
            if self.WidgetLastCopied!=-1:
                CopiedWidgetsList=[]
                indexes_CopiedWidgetsList=[]
                masters=[]
                widgets_names=[]
                CopiedWidget=self.list_widgets_on_wins_copy_use[self.WidgetLastCopied]
                CopiedWidgetsList.append(CopiedWidget)
                indexes_CopiedWidgetsList.append(self.WidgetLastCopied)
                wins=self.listbox_wins.get(0,END)
                masters.append(wins[self.pointer_win])
                widgets_names.append(self.list_widgets_on_wins_properties_copy_use[self.WidgetLastCopied]['id'])
                
                index=0
                flag=0
                
                for widget in self.list_widgets_on_wins_copy_use:
                    if str(CopiedWidget) in str(widget) and str(CopiedWidget)!=str(widget):
                        CopiedWidgetsList.append(widget)
                        indexes_CopiedWidgetsList.append(index)
                        masters.append(self.list_widgets_on_wins_properties_copy_use[index]['master'])
                        widgets_names.append(self.list_widgets_on_wins_properties_copy_use[index]['id'])
                    if str(widget) in str(CopiedWidget) and str(CopiedWidget)!=str(widget):
                        flag=1
                    index+=1
                ############### adding copy to masters:
                
                
                widgetscopied=[]
                indexes=[]
                new_masters=[]
                index=0
                for widget in widgets_names:
                    copy=widgets_names[index]
                    while copy in widgets_names or copy in widgetscopied or copy in self.listbox_widgets_on_win.get(0,END):
                        copy+='_copy'
                    widgetscopied.append(copy)
                    index+=1
                
                index=0
                for master in masters:
                    if index!=0:
                        indexes.append(widgets_names.index(master))
                    else:
                        indexes.append(None)
                    index+=1
                index=0
                for master in masters:
                    if index==0:
                        new_masters.append(master)
                    else:
                        new_masters.append(widgetscopied[indexes[index]])
                    index+=1
                
                
                #################### sorting copied widgets
                args=[indexes_CopiedWidgetsList,new_masters,widgetscopied]
                CopiedWidgetsList,args=self.SortingWidgets(CopiedWidgetsList,args)
                indexes_CopiedWidgetsList=args[0]
                new_masters=args[1]
                widgetscopied=args[2]
                #########################################
                
                index=0
                for widget in CopiedWidgetsList:
                    var=-1
                    if type(widget) is Button:
                        var=0
                    elif type(widget) is Entry:
                        var=1
                    elif type(widget) is Text:
                        var=2
                    elif type(widget) is Radiobutton:
                        var=3
                    elif type(widget) is Checkbutton:
                        var=4
                    elif type(widget) is Canvas:
                        var=5
                    elif type(widget) is Label:
                        var=6
                    elif type(widget) is Listbox:
                        var=7
                    elif type(widget) is ttk.Scrollbar:
                        var=8
                    elif type(widget) is ttk.Combobox:
                        var=9
                    elif type(widget) is ttk.Treeview:
                        var=10
                    elif type(widget) is Frame:
                        var=11
                    self.AddWidget(var,0)
                    self.list_widgets_on_wins_properties[-1]=self.list_widgets_on_wins_properties_copy_use[indexes_CopiedWidgetsList[index]].copy()
                    self.list_widgets_on_wins_properties[-1]['master']=new_masters[index]
                    self.list_widgets_on_wins_properties[-1]['id']=widgetscopied[index]
                    
                    if index==0:
                        self.list_widgets_on_wins_properties[-1]['x']=10
                        self.list_widgets_on_wins_properties[-1]['y']=10
                    self.listbox_widgets_on_win.delete(END)
                    self.listbox_widgets_on_win.insert(END,self.list_widgets_on_wins_properties[-1]['id'])
                    InsertedWidgets=self.listbox_widgets_on_win.get(0,END)
                    self.loading_properties(len(InsertedWidgets)-1,0)
                    self.click_enter(len(InsertedWidgets)-1)
                    index+=1
                
                if flag or len(CopiedWidgetsList)!=1:
                    self.Refresh_com()
                    
        except:
            pass
    def ControlS(self,e):
        try:
            self.save_win()
        except:
            pass
    def SortingRest(self,OrderedList,UnorderedList,args=[]):
        try:
            args_new=[]
            for i in range(0,len(args)):
                args_new.append([])
            indx=0
            for item in OrderedList:
                index_item=UnorderedList.index(item)
                
                for index in range(0,len(args)):
                    args_new[index].append(args[index][index_item])
                    
                indx+=1
            return args_new
        except:
            pass
    
            
    



App=TkDesigner()
App.mainloop()




































