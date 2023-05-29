from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os
from PIL import ImageTk, Image
import shutil
from tkinter import messagebox
from threading import Thread
import random

chars='qwertyuiop[]\';lkjhgfdsazxcvbnm,./1234567890+-*\\_^@!#~%&(){} QWERTYUIOPLKJHGFDSAZXCVBNM'
class App(Tk):
    def __init__(self):
        self.enabled=False
        self.enabled_mark = False
        self.enabled_delete = False
        
        self.last_class=1
        self.last_label='start_label'
        self.flag=0
        self.resave=False
        self.labeled=False
        self.entered=False
        self.cur=-1
        self.list_labels_image=[]
        self.list_images=[]
        self.path_folder=''
        self.list_yaml=[]
        self.selected=-1
        self.selected_box=False
        self.boxes=[]
        self.status=0                #1- new proj 2- open proj
        self.color_left='#252525'
        self.color_right='#2e2d2d'
        self.color_top='#1a1a1a'
        self.color_bt='#363636'
        
        Tk.__init__(self)
        self.geometry("1600x950+10+10")
        self.title('DeepLabel')
        self.iconbitmap(bitmap='icon.ico')
        self.state('zoomed')
        #self.resizable(0,0)
        self.config(background='#2e2d2d')
        self.bind('<Delete>',self.delete_box)
        self.bind('<Return>',self.confirm_annotation)
        self.bind('<Right>',self.bt_next_com)
        self.bind('<Left>',self.bt_prev_com)
        self.bind('<Up>',self.move_list_up)
        self.bind('<Down>',self.move_list_down)
        self.bind('<Control-n>',self.new_proj)
        self.bind('<Control-o>',self.open_proj)
        self.bind('<Control-d>',self.DeleteImage)
        self.bind('<Control-m>',self.MarkImage)
        self.bind('<Control-x>',self.close_proj)
        self.protocol('WM_DELETE_WINDOW', self.Exit_prog)
        self.width_screen=self.winfo_screenwidth()
        self.height_screen=self.winfo_screenheight()
        self.width=self.width_screen
        self.height=self.height_screen-84
        self.height_right=self.height-200
        self.label_var = StringVar()
        self.num_annotated=IntVar()
        self.num_unannotated=IntVar()
        self.current_image=IntVar()
        self.class_selected=IntVar()
        self.class_selected.set(1)
        self.menubar = Menu(self)
        self.file=Menu(self.menubar,tearoff=0)
        self.file.add_command(label='New Proj',command=self.new_proj,accelerator="Ctrl+N")
        self.file.add_command(label='Open Proj',command=self.open_proj,accelerator="Ctrl+O")
        self.file.add_command(label='Open External Proj',command=self.open_ex_proj_com)
        self.file.add_command(label='Collect Multiple Labeled',command=self.CollectMultiple)
        self.file.add_command(label='Import Images',command=self.ImportImages)
        self.file.add_command(label='Close Proj',command=self.close_proj,accelerator="Ctrl+X")
        self.file.add_command(label='Number Images',command=self.NumImg)
        #self.file.add_command(label='Number Images Labels',command=self.NumImgLbl)
        self.file.add_command(label='Delete Image',command=self.DeleteImage,accelerator="Ctrl+D")
        self.file.add_command(label='Mark Image',command=self.MarkImage,accelerator="Ctrl+M")
        self.file.add_command(label='Unmark Image',command=self.UnmarkImage)
        self.file.add_command(label='Start at last marked',command=self.StartImage)
        self.file.add_command(label='Health Check',command=self.health_check)
        self.file.add_command(label='Rearrange',command=self.Rearrange)
        self.file.add_command(label='Export Data',command=self.ExportData)
        
        self.file.entryconfig("Delete Image", state="disable")
        self.file.entryconfig("Mark Image", state="disable")
        self.file.entryconfig("Unmark Image", state="disable")
        self.file.entryconfig("Start at last marked", state="disable")
        self.file.entryconfig("Close Proj", state="disable")
        self.file.entryconfig("Health Check", state="disable")
        self.file.entryconfig("Import Images", state="disable")
        self.file.entryconfig("Rearrange", state="disable")
        self.file.entryconfig("Export Data", state="disable")
        
        
        self.file.add_separator()
        self.file.add_command(label='Exit',command=self.Exit_prog)
        self.classes=Menu(self.menubar,tearoff=0)
        self.classes.add_radiobutton(label='Unlabeled',value=1,variable=self.class_selected,command=self.Unlabeled_com)
        
        self.classes.add_radiobutton(label='Labeled',value=2,variable=self.class_selected,command=self.Labeled_com)
        self.classes.add_radiobutton(label='Marked',value=3,variable=self.class_selected,command=self.Marked_com)
        
        self.classes.entryconfig("Unlabeled", state="disable")
        self.classes.entryconfig("Labeled", state="disable")
        self.classes.entryconfig("Marked", state="disable")
        
        self.classes.add_separator()
        
        self.help=Menu(self.menubar,tearoff=0)
        self.help.add_command(label='About DeepLabel',command=self.AboutDeepLabel_com)
        
        
        self.menubar.add_cascade(label='File',menu=self.file)
        self.menubar.add_cascade(label='Classes',menu=self.classes)
        self.menubar.add_cascade(label='Help',menu=self.help)
        
        self.configure(menu=self.menubar)
        
        
        self.lbl_back_left = Label(self,background=self.color_left,bd=0)
        self.lbl_back_left.place(x=0,y=0,height=round(self.height),width=round(0.15625*self.width))
        self.lbl_label = Label(self,text='label',background=self.color_left,foreground='white',
                               font=('arial',17))
        self.lbl_label.place(x=10,y=20)
        self.ent_label = Entry(self,bd=0,relief=FLAT,font=('arial',15),textvariable=self.label_var)
        self.ent_label.place(x=10,y=55,width=round(0.143*self.width),height=25)
        self.ent_label.bind('<Key>',self.Writing)
        self.listbox=Listbox(self,bd=0,relief=FLAT,font=('arial',15),background='#464646',foreground='white')
        self.listbox.place(x=10,y=90,height=round(0.962*self.height_right),width=round(0.143*self.width))
        self.listbox.bind('<ButtonRelease-1>',self.SelectListbox)
        
        
        self.slogan = Image.open('slogan.png')
        self.slogan=self.slogan.resize((50,50))
        self.slogan = ImageTk.PhotoImage(self.slogan)
        self.lbl_slogan = Label(self,image=self.slogan,background=self.color_left)
        self.lbl_slogan.place(x=10,y=100+round(0.962*self.height_right),width=round(0.143*self.width),height=50)
        
        self.program_name = Label(self,text='DeepLabel',font=('arial',24,'bold'),background=self.color_left,foreground='#53c5f9')
        self.program_name.place(x=10,y=150+round(0.962*self.height_right),width=round(0.143*self.width))
        
        
        self.logo = Image.open('logo.png')
        self.logo=self.logo.resize((round(0.143*self.width)-round(0.07*self.width),round(0.035*self.height_right)))
        self.logo = ImageTk.PhotoImage(self.logo)
        self.lbl_logo = Label(self,image=self.logo,background=self.color_left)
        self.lbl_logo.place(x=10,y=190+round(0.962*self.height_right),width=round(0.143*self.width),height=round(0.035*self.height_right))
        
        
        self.lbl_back_right=Label(self,background=self.color_right,bd=0)
        self.lbl_back_right.place(x=round(0.15625*self.width),y=0,width=self.width-round(0.15625*self.width),height=self.height)
        
        self.lbl_back_top=Label(self,background=self.color_top,bd=0)
        self.lbl_back_top.place(x=round(0.15625*self.width),y=0,width=self.width-round(0.15625*self.width),height=round(0.035*self.height))
        self.bt_prev=Button(self,text='Prev',bd=0,relief=FLAT,font=('arial',15),
                            background=self.color_bt,activebackground=self.color_bt,foreground='white',
                            activeforeground='white',command=self.bt_prev_com)
        self.bt_prev.place(x=round(0.161*self.width),y=round(5*self.height/996),width=round(0.036*self.width),height=round(0.025*self.height))
        self.lbl_num=Label(self,textvariable=self.current_image,font=('arial',15),foreground='white',background=self.color_top)
        self.lbl_num.place(x=round(0.577*self.width),y=0)
        self.bt_next=Button(self,text='Next',bd=0,relief=FLAT,font=('arial',15),
                            background=self.color_bt,activebackground=self.color_bt,foreground='white',
                            activeforeground='white',command=self.bt_next_com)
        self.bt_next.place(x=round(0.961*self.width),y=round(5*self.height/996),width=round(0.036*self.width),height=round(0.025*self.height))
        
        self.canvas = Canvas(self,bd=0,highlightthickness=0,background='#2e2d2d')
        self.canvas.place(x=round(0.15625*self.width),y=round(0.0351*self.height),height=round(self.height-(round(0.0351*self.height)+round(0.035*self.height))),width=self.width-round(0.15625*self.width))
        self.canvas.bind('<Button-1>',self.assign_first)
        self.canvas.bind('<B1-Motion>',self.create_label)
        self.canvas.bind('<ButtonRelease-1>',self.verify)
        self.canvas.bind('<Motion>',self.mouse_motion)
        self.canvas.bind('<MouseWheel>',self.mouse_wheel)
        
        
        self.lbl_back_bottom=Label(self,background='#363636')
        self.lbl_back_bottom.place(x=round(0.15625*self.width),y=round(0.965*self.height),height=round(0.0351*self.height),width=self.width-round(0.15625*self.width))
        self.lbl_annotated = Label(self,text='Annotated: ',font=('arial',15),background='#363636',
                                   foreground='white')
        self.lbl_annotated.place(x=round(0.161*self.width),y=round(0.966*self.height))
        self.lbl_num_annotated = Label(self,text='15',font=('arial',15),background='#363636',
                                   foreground='white',textvariable=self.num_annotated)
        self.lbl_num_annotated.place(x=round(0.161*self.width)+100,y=round(0.966*self.height))
        
        self.lbl_unannotated = Label(self,text='UnAnnotated: ',font=('arial',15),background='#363636',
                                   foreground='white')
        self.lbl_unannotated.place(x=round(0.876*self.width),y=round(0.966*self.height))
        self.lbl_num_unannotated = Label(self,text='20',font=('arial',15),background='#363636',
                                   foreground='white',textvariable=self.num_unannotated)
        self.lbl_num_unannotated.place(x=round(0.876*self.width)+125,y=round(0.966*self.height))
        
        self.H_line=self.canvas.create_line(0,round(self.height-(round(0.0351*self.height)+round(0.035*self.height)))/2,self.width-round(0.15625*self.width),round(self.height-(round(0.0351*self.height)+round(0.035*self.height)))/2,dash=(5,1),fill='white')
        self.V_line=self.canvas.create_line((self.width-round(0.15625*self.width))/2,0,(self.width-round(0.15625*self.width))/2,round(self.height-(round(0.0351*self.height)+round(0.035*self.height))),dash=(5,1),fill='white')
    
    def AboutDeepLabel_com(self):
        try:
            self.win_about = Toplevel(background='#363636')
            self.win_about.title('DeepLabel')
            self.win_about.iconbitmap(bitmap='icon.ico')
            x= int((self.width_screen-500)/2)
            y= int((self.height_screen-250)/2)
            self.win_about.geometry(f'500x250+{x}+{y}')
            self.win_about.resizable(0,0)
            self.slogan_about = Image.open('slogan.png')
            self.slogan_about = self.slogan_about.resize((100,100))
            self.slogan_about = ImageTk.PhotoImage(self.slogan_about)
            self.lbl_slogan_about = Label(self.win_about,image=self.slogan_about,background='#363636')
            self.lbl_slogan_about.place(x=210,y=10,width=100,height=100)
            
            self.lblDeepLabel = Label(self.win_about,text='DeepLabel v1',font=('arial',24,'bold'),background='#363636',foreground='#53c5f9')
            self.lblDeepLabel.place(x=160,y=120,width=200)
            
            self.logo_about = Image.open('logo.png')
            self.logo_about =self.logo_about.resize((200,40))
            self.logo_about = ImageTk.PhotoImage(self.logo_about)
            self.lbl_logo_about = Label(self.win_about,image=self.logo_about,background='#363636')
            self.lbl_logo_about.place(x=160,y=175,width=200,height=50)
        except:
            pass
        
        
    def numberImageLabels(self,path,start):
        try:
            list_images = os.listdir(path+'\\images\\')
            count=start
            list_temp=[]
            for image in list_images:
                txt_count=str(count)
                while(len(txt_count)< 6):
                    txt_count='0'+txt_count
                
                if os.path.exists(path+'\\images\\'+txt_count+'.jpg') and image!=txt_count+'.jpg':
                    os.rename(path+'\\images\\'+txt_count+'.jpg',
                              path+'\\images\\'+txt_count+'ELPRINCETEMP.jpg')

                    os.rename(path+'\\labels\\'+txt_count+'.txt',
                              path+'\\labels\\'+txt_count+'ELPRINCETEMP.txt')
                    list_temp.append(txt_count+'ELPRINCETEMP.jpg')
                if os.path.exists(path+'\\images\\'+image):
                    os.rename(path+'\\images\\'+image,
                              path+'\\images\\'+txt_count+'.jpg')
                    label = image.replace('.jpg','.txt')
                    os.rename(path+'\\labels\\'+label,
                              path+'\\labels\\'+txt_count+'.txt')
                count+=1
            for image in list_temp:
                txt_count=str(count)
                while(len(txt_count)< 6):
                    txt_count='0'+txt_count
                os.rename(path+'\\images\\'+image,
                          path+'\\images\\'+txt_count+'.jpg')
                label = image.replace('.jpg','.txt')
                os.rename(path+'\\labels\\'+label,
                          path+'\\labels\\'+txt_count+'.txt')
                count+=1
            return count
        except:
            pass
    
    
    def CollectMultiple(self):
        try:
            self.path_folder = filedialog.askdirectory()
            if self.path_folder and not os.path.exists(self.path_folder+'\\labeled\\'):
                
                self.title('DeepLabel - '+self.path_folder)
                x= int((self.width_screen-300)/2)
                y= int((self.height_screen-80)/2)
                self.win_loading=Toplevel(background='#363636')
                self.win_loading.iconbitmap(bitmap='icon.ico')
                self.win_loading.geometry(f"300x80+{x}+{y}")
                self.win_loading.resizable(0,0)
                self.win_loading.title('DeepLabel')
                self.progBar = ttk.Progressbar(self.win_loading,orient=HORIZONTAL, length=280,mode="determinate")
                self.progBar.place(x=10,y=20)
                
                th1=Thread(target=self.th_CollectMultiple)
                th1.start()
        except:
            pass
        
    def th_CollectMultiple(self):
        try:
            folders = os.listdir(self.path_folder)
            self.list_yaml=[]
            
            os.mkdir(self.path_folder+'\\labeled\\')
            os.mkdir(self.path_folder+'\\labeled\\images\\')
            os.mkdir(self.path_folder+'\\labeled\\labels\\')
            os.mkdir(self.path_folder+'\\classes\\')
            os.mkdir(self.path_folder+'\\images\\')
            
            count=0
            for folder in folders:
                
                lines=[]
                with open(self.path_folder+'\\'+folder+'\\data.yaml','r') as f1:
                    lines=f1.read()
                lines=lines.splitlines()
                list_yaml=[]
                for line in lines:
                    if line.startswith('- '):
                        label = line.replace('- ','')
                        list_yaml.append(label)
                        if not label in self.list_yaml:
                            self.list_yaml.append(label)
                list_labels = os.listdir(self.path_folder+'\\'+folder+'\\labels\\')
                for file in list_labels:
                    lines=[]
                    with open(self.path_folder+'\\'+folder+'\\labels\\'+file,'r') as f1:
                        lines=f1.read()
                    lines=lines.splitlines()
                    with open(self.path_folder+'\\'+folder+'\\labels\\'+file,'w') as f1:
                        for line in lines:
                            list_line = line.split(' ')
                            old_index = int(list_line[0])
                            label = list_yaml[old_index]
                            new_index = self.list_yaml.index(label)
                            new_line = str(new_index)+' '
                            new_list= list_line[1:]
                            c=0
                            for i in new_list:
                                new_line+=i
                                if c!=len(new_list)-1:
                                    new_line+=' '
                                c+=1
                            f1.write(new_line+'\n')
                
                
                count=self.numberImageLabels(self.path_folder+'\\'+folder,count)
                
                progRange = 100/(len(folders)+1)
                self.moveFiles(self.path_folder+'\\'+folder,progRange)
            
                
            with open(self.path_folder+'\\labeled\\data.yaml','w') as f1:
                f1.write('names:\n')
                for label in self.list_yaml:
                    f1.write('- '+label+'\n')
                    
            self.getClasses()
            
            self.progBar['value']=100
            self.win_loading.destroy()
            
            
            for i in range(0,len(self.list_yaml)):
                label=self.list_yaml[i]
                self.classes.add_radiobutton(label=label,value=4+i,variable=self.class_selected,command=self.label_class)
                
            self.class_selected.set(2)
            self.Labeled_com()
                
            self.status=1
            self.file.entryconfig("Delete Image", state="normal")
            self.file.entryconfig("Mark Image", state="normal")
            self.file.entryconfig("Close Proj", state="normal")
            self.file.entryconfig("Health Check", state="normal")
            self.file.entryconfig("Import Images", state="normal")
            self.file.entryconfig("Rearrange", state="normal")
            self.file.entryconfig("Export Data", state="normal")
            self.classes.entryconfig("Unlabeled", state="normal")
            self.classes.entryconfig("Labeled", state="normal")
            self.classes.entryconfig("Marked", state="normal")
            self.file.entryconfig("New Proj", state="disable")
            self.file.entryconfig("Open Proj", state="disable")
            self.file.entryconfig("Open External Proj", state="disable")
            self.file.entryconfig('Collect Multiple Labeled', state="disable")
            if len(self.list_yaml)!=0:
                self.last_label = self.list_yaml[-1]
            self.enabled=True
            self.enabled_mark = True
            self.enabled_delete = True
        except:
            pass
        
            
    def StartImage(self):
        try:
            if os.path.exists(self.path_folder+'\\classes\\marked.txt'):
                marked_images=[]
                with open(self.path_folder+'\\classes\\marked.txt','r') as f1:
                    marked_images=f1.read()
                marked_images=marked_images.splitlines()
                if marked_images!=[]:
                    last_marked = marked_images[-1]
                    if self.last_class == 2:
                        self.Labeled_com(last_marked)
                    else:
                        self.label_class(last_marked)
        except:
            pass
                
    def ExportData(self):
        try:
            
            labeled_imgs = os.listdir(self.path_folder+'\\labeled\\labels')
            self.num_imgs=len(labeled_imgs)
            
            x= int((self.width_screen-600)/2)
            y= int((self.height_screen-250)/2)
            self.win_export = Toplevel(background='#363636')
            self.win_export.iconbitmap(bitmap='icon.ico')
            self.win_export.title('DeepLabel')
            self.win_export.geometry(f'600x250+{x}+{y}')
            self.win_export.resizable(0,0)
            
            
            self.lbl_export = Label(self.win_export,text='Export',background='#363636',foreground='white',
                                   font=('arial',17))
            self.lbl_export.place(x=275,y=10)
            
            self.lbl_train = Label(self.win_export,text='Train:',background='#363636',foreground='white',
                                   font=('arial',15))
            self.lbl_train.place(x=10,y=50)
            
            self.style = ttk.Style(self)
            self.style.configure('custom.Horizontal.TScale', background='#363636')
            
            self.var_train=IntVar()
            self.var_test=IntVar()
            self.var_valid=IntVar()
            
            self.ent_train_var=StringVar()
            self.ent_test_var=StringVar()
            self.ent_valid_var=StringVar()
            
            
            
            
            
            self.slider_train = ttk.Scale(self.win_export, from_=0, to=100, orient='horizontal', variable=self.var_train,style='custom.Horizontal.TScale')
            self.slider_train.place(x=100,y=53,width=250)
            self.slider_train.bind('<ButtonRelease>',self.Save_addition1)
            
            self.perc_train = Entry(self.win_export,textvariable=str(self.var_train),
                                   font=('arial',15),state='readonly')
            self.perc_train.place(x=370,y=53,width=70)
            
            self.lbl_perc = Label(self.win_export,text='%',font=('arial',15),background='#363636',
                                  foreground='white')
            self.lbl_perc.place(x=445,y=53)
            
            self.ent_train = Entry(self.win_export,bd=0,font=('arial',15),textvariable=self.ent_train_var,state='readonly')
            self.ent_train.place(x=480,y=53,height=25,width=100)
            
            self.lbl_test = Label(self.win_export,text='Test:',background='#363636',foreground='white',
                                   font=('arial',15))
            self.lbl_test.place(x=10,y=100)
            
            self.perc_test = Entry(self.win_export,textvariable=str(self.var_test),
                                   font=('arial',15),state='readonly')
            self.perc_test.place(x=370,y=103,width=70)
            
            self.lbl_perc2 = Label(self.win_export,text='%',font=('arial',15),background='#363636',
                                  foreground='white')
            self.lbl_perc2.place(x=445,y=103)
            
            self.ent_test = Entry(self.win_export,bd=0,font=('arial',15),textvariable=self.ent_test_var,state='readonly')
            self.ent_test.place(x=480,y=103,height=25,width=100)
            
            
            self.slider_test = ttk.Scale(self.win_export, from_=0, to=100, orient='horizontal', variable=self.var_test,style='custom.Horizontal.TScale')
            self.slider_test.place(x=100,y=103,width=250)
            self.slider_test.bind('<ButtonRelease>',self.Save_addition2)
            
            self.lbl_valid = Label(self.win_export,text='Valid:',background='#363636',foreground='white',
                                   font=('arial',15))
            self.lbl_valid.place(x=10,y=150)
            
            self.perc_valid = Entry(self.win_export,textvariable=str(self.var_valid),
                                   font=('arial',15),state='readonly')
            self.perc_valid.place(x=370,y=153,width=70)
            
            self.lbl_perc3 = Label(self.win_export,text='%',font=('arial',15),background='#363636',
                                  foreground='white')
            self.lbl_perc3.place(x=445,y=153)
            
            self.ent_valid = Entry(self.win_export,bd=0,font=('arial',15),textvariable=self.ent_valid_var,state='readonly')
            self.ent_valid.place(x=480,y=153,height=25,width=100)
            
            self.slider_valid = ttk.Scale(self.win_export, from_=0, to=100, orient='horizontal', variable=self.var_valid,style='custom.Horizontal.TScale')
            self.slider_valid.place(x=100,y=153,width=250)
            self.slider_valid.bind('<ButtonRelease>',self.Save_addition3)
            
            self.bt_export = Button(self.win_export,text='Export',foreground='white',
                                    bd=0,relief=FLAT,activeforeground='white',
                                    font=('arial',15),background='#2e2d2d',activebackground='#2e2d2d',
                                    command=self.bt_export_com,state='disable')
            self.bt_export.place(x=275,y=200)
        except:
            pass
        
    def bt_export_com(self):
        try:
            
                    
            x= int((self.width_screen-300)/2)
            y= int((self.height_screen-80)/2)
            self.win_loading=Toplevel(background='#363636')
            self.win_loading.iconbitmap(bitmap='icon.ico')
            self.win_loading.geometry(f"300x80+{x}+{y}")
            self.win_loading.resizable(0,0)
            self.win_loading.title('DeepLabel')
            self.progBar = ttk.Progressbar(self.win_loading,orient=HORIZONTAL, length=280,mode="determinate")
            self.progBar.place(x=10,y=20)
            
            th1=Thread(target=self.th_bt_export_com)
            th1.start()
        except:
            pass
        
    def th_bt_export_com(self):
        try:
            self.th_Rearrange('pass')
            if os.path.exists(self.path_folder+'\\exported\\'):
                shutil.rmtree(self.path_folder+'\\exported\\')
                
            os.mkdir(self.path_folder+'\\exported\\')
            os.mkdir(self.path_folder+'\\exported\\train\\')
            os.mkdir(self.path_folder+'\\exported\\train\\images\\')
            os.mkdir(self.path_folder+'\\exported\\train\\labels\\')
            os.mkdir(self.path_folder+'\\exported\\test\\')
            os.mkdir(self.path_folder+'\\exported\\test\\images\\')
            os.mkdir(self.path_folder+'\\exported\\test\\labels\\')
            os.mkdir(self.path_folder+'\\exported\\valid\\')
            os.mkdir(self.path_folder+'\\exported\\valid\\images\\')
            os.mkdir(self.path_folder+'\\exported\\valid\\labels\\')
            
            list_imgs = os.listdir(self.path_folder+'\\labeled\\images\\')
            random.shuffle(list_imgs)
            
            for i in range(0,int(self.ent_train_var.get())):
                shutil.move(self.path_folder+'\\labeled\\images\\'+list_imgs[i],
                            self.path_folder+'\\exported\\train\\images\\'+list_imgs[i])
                label = list_imgs[i].replace('.jpg','.txt')
                shutil.move(self.path_folder+'\\labeled\\labels\\'+label,
                            self.path_folder+'\\exported\\train\\labels\\'+label)
                
                if int(int(self.ent_train_var.get())/33)!=0:
                    if i%(int(int(self.ent_train_var.get())/33))==0:
                        self.progBar['value']+=1
                else:
                    self.progBar['value']+=int(33/int(self.ent_train_var.get()))
                
            for i in range(int(self.ent_train_var.get()),
                           int(self.ent_train_var.get())+int(self.ent_test_var.get())):
                shutil.move(self.path_folder+'\\labeled\\images\\'+list_imgs[i],
                            self.path_folder+'\\exported\\test\\images\\'+list_imgs[i])
                label = list_imgs[i].replace('.jpg','.txt')
                shutil.move(self.path_folder+'\\labeled\\labels\\'+label,
                            self.path_folder+'\\exported\\test\\labels\\'+label)
                
                if int(int(self.ent_test_var.get())/33)!=0:
                    if i%(int(int(self.ent_test_var.get())/33))==0:
                        self.progBar['value']+=1
                else:
                    self.progBar['value']+=int(33/int(self.ent_test_var.get()))
                
            
            for i in range(int(self.ent_train_var.get())+int(self.ent_test_var.get()),len(list_imgs)):
                shutil.move(self.path_folder+'\\labeled\\images\\'+list_imgs[i],
                            self.path_folder+'\\exported\\valid\\images\\'+list_imgs[i])
                label = list_imgs[i].replace('.jpg','.txt')
                shutil.move(self.path_folder+'\\labeled\\labels\\'+label,
                            self.path_folder+'\\exported\\valid\\labels\\'+label)
                
                length=len(list_imgs)-(int(self.ent_train_var.get())+int(self.ent_test_var.get()))
                if int(length/33)!=0:
                    if i%(int(length/33))==0:
                        self.progBar['value']+=1
                else:
                    self.progBar['value']+=int(33/length)
            
            with open(self.path_folder+'\\labeled\\data.yaml','a') as f1:
                f1.write('nc: '+str(len(self.list_yaml))+'\n')
                f1.write('test: ../test/images\n')
                f1.write('train: exported/train/images\n')
                f1.write('val: exported/valid/images\n')
            shutil.move(self.path_folder+'\\labeled\\data.yaml',
                        self.path_folder+'\\exported\\data.yaml')
            self.progBar['value']=100
            self.win_loading.destroy()
            self.win_export.destroy()
            self.close_proj()
            messagebox.showinfo('done!','Exported Successfully!')
        except:
            pass
        
    
    def Save_addition1(self,e):
        try:
            self.bt_export.config(state='normal')
            remain = 100 - self.var_train.get()
            if self.var_test.get()<remain:
                self.var_valid.set(remain-self.var_test.get())
            else:
                self.var_valid.set(remain/2)
                self.var_test.set(remain/2)
            self.ent_train_var.set(int(self.var_train.get()*self.num_imgs/100))
            self.ent_test_var.set(int(self.var_test.get()*self.num_imgs/100))
            self.ent_valid_var.set(int(self.var_valid.get()*self.num_imgs/100))
        except:
            pass
        
    def Save_addition2(self,e):
        try:
            self.bt_export.config(state='normal')
            remain = 100 - self.var_test.get()
            if self.var_train.get()<remain:
                self.var_valid.set(remain-self.var_train.get())
            else:
                self.var_train.set(remain/2)
                self.var_valid.set(remain/2)
            self.ent_train_var.set(int(self.var_train.get()*self.num_imgs/100))
            self.ent_test_var.set(int(self.var_test.get()*self.num_imgs/100))
            self.ent_valid_var.set(int(self.var_valid.get()*self.num_imgs/100))
        except:
            pass
    def Save_addition3(self,e):
        try:
            self.bt_export.config(state='normal')
            remain = 100 - self.var_valid.get()
            if self.var_train.get()<remain:
                self.var_test.set(remain-self.var_train.get())
            else:
                self.var_train.set(remain/2)
                self.var_test.set(remain/2)
            self.ent_train_var.set(int(self.var_train.get()*self.num_imgs/100))
            self.ent_test_var.set(int(self.var_test.get()*self.num_imgs/100))
            self.ent_valid_var.set(int(self.var_valid.get()*self.num_imgs/100))
        except:
            pass
    def Rearrange(self):
        try:
            if self.resave and len(self.boxes)!=0:
                if self.cur>=self.current_image.get():
                    self.save_label(True)
                else:
                    self.save_label(False)
                    
            x= int((self.width_screen-300)/2)
            y= int((self.height_screen-80)/2)
            self.win_loading=Toplevel(background='#363636')
            self.win_loading.iconbitmap(bitmap='icon.ico')
            self.win_loading.geometry(f"300x80+{x}+{y}")
            self.win_loading.resizable(0,0)
            self.win_loading.title('DeepLabel')
            self.progBar = ttk.Progressbar(self.win_loading,orient=HORIZONTAL, length=280,mode="determinate")
            self.progBar.place(x=10,y=20)
            
            t1 = Thread(target=self.th_Rearrange)
            t1.start()
        except:
            pass
    
    def th_Rearrange(self,e=None):
        try:
            removed_list_yaml=[]
            list_yaml_new=self.list_yaml.copy()
            
            count=0
            for label in self.list_yaml:
                if os.path.exists(self.path_folder+'\\classes\\'+label+'.txt'):
                    lines=[]
                    with open(self.path_folder+'\\classes\\'+label+'.txt','r') as f1:
                        lines=f1.read()
                    lines=lines.splitlines()
                    if lines==[]:
                        os.remove(self.path_folder+'\\classes\\'+label+'.txt')
                        removed_list_yaml.append(label)
                else:
                    removed_list_yaml.append(label)
                if e!='pass':
                    if int(len(self.list_yaml)/50)!=0:
                        if count%(int(len(self.list_yaml)/50))==0:
                            self.progBar['value']+=1
                    else:
                        self.progBar['value']+=int(50/len(self.list_yaml))
                count+=1
                    
            if removed_list_yaml!=[]:
                for label in removed_list_yaml:
                    list_yaml_new.remove(label)
                with open(self.path_folder+'\\labeled\\data.yaml','w') as f1:
                    f1.write('names:\n')
                    for label in list_yaml_new:
                        f1.write(f'- {label}\n')
                self.classes.delete(4,END)
                for i in range(0,len(list_yaml_new)):
                    label = list_yaml_new[i]
                    self.classes.add_radiobutton(label=label,value=4+i,variable=self.class_selected,command=self.label_class)
                
                old_indexes=[]
                new_indexes=[]
                count=0
                for label in list_yaml_new:
                    index = self.list_yaml.index(label)
                    old_indexes.append(index)
                    new_indexes.append(count)
                    count+=1
                
                list_files_labeled = os.listdir(self.path_folder+'\\labeled\\labels\\')
                count2=0
                for file in list_files_labeled:
                    lines=[]
                    with open(self.path_folder+'\\labeled\\labels\\'+file,'r') as f1:
                        lines=f1.read()
                    lines=lines.splitlines()
                    new_lines=[]
                    for line in lines:
                        list_line =line.split(' ')
                        old_index = int(list_line[0])
                        index = old_indexes.index(old_index)
                        new_index = new_indexes[index]
                        new_line = str(new_index)+' '
                        list_line=list_line[1:]
                        count=0
                        for i in list_line:
                            new_line+=i
                            if count != len(list_line)-1:
                                new_line+=' '
                            count+=1
                        new_lines.append(new_line)
                    with open(self.path_folder+'\\labeled\\labels\\'+file,'w') as f1:
                        for line in new_lines:
                            f1.write(line+'\n')
                    if e!='pass':
                        if int(len(list_files_labeled)/50)!=0:
                            if count2%(int(len(list_files_labeled)/50))==0:
                                self.progBar['value']+=1
                        else:
                            self.progBar['value']+=int(50/len(list_files_labeled))
                    count2+=1
                    
            self.list_yaml = list_yaml_new.copy()
            if e!='pass':     
                self.progBar['value']=100
                self.win_loading.destroy()
            
                list_unannotated = os.listdir(self.path_folder+'\\images\\')
                if list_unannotated!=[]:
                    self.class_selected.set(1)
                    self.Unlabeled_com()
                else:
                    self.class_selected.set(2)
                    self.Labeled_com()
        except:
            pass
    def ImportImages(self):
        try:
            
            if self.resave:
                if self.cur>=self.current_image.get():
                    self.save_label(True)
                else:
                    self.save_label(False)
                    
            if self.status!=0:
                path_images = filedialog.askdirectory()
                
                if path_images:
                    
                    if not os.path.exists(self.path_folder+'\\images\\'):
                        os.mkdir(self.path_folder+'\\images\\')
                    listImgs_before = os.listdir(self.path_folder+'\\images\\')
                    listImgs_before = sorted(listImgs_before)
                    
                    listImgs_labeled = os.listdir(self.path_folder+'\\labeled\\images\\')
                    listImgs_labeled = sorted(listImgs_labeled)
                    
                    start_num=0
                    if len(listImgs_before)!=0:
                        start_num=int(listImgs_before[-1].replace('.jpg',''))+1
                    elif len(listImgs_labeled)!=0:
                        start_num=int(listImgs_labeled[-1].replace('.jpg',''))+1
                    
                    self.bt_Number_com(path_images,start_num)
                    list_imgs = os.listdir(path_images)
                    
                    found=0
                    for img in list_imgs:
                        if img.endswith('.jpg'):
                            found=1
                            shutil.copy(path_images+'\\'+img, self.path_folder+'\\images\\'+img)
                    if found:
                        self.class_selected.set(1)
                        self.Unlabeled_com()
                        messagebox.showinfo('done!','Done!')
                    else:
                        messagebox.showinfo('warnning!','There are no jpg files!')
                    
        except:
            pass
    def Initialize(self):
        try:
            self.last_label='start_label'
            self.flag=0
            self.resave=False
            self.labeled=False
            self.entered=False
            self.cur=-1
            self.list_labels_image=[]
            self.selected=-1
            self.selected_box=False
            self.boxes=[]
            self.current_image.set(0)
        except:
            pass
        
    def Labeled_com(self,image=None):
        try:
            cond = True
            if self.last_class==3 and len(self.list_images)!=0:
                cond=self.labeled
            if cond:
                if self.resave and len(self.boxes)!=0:
                    if self.cur>=self.current_image.get():
                        self.save_label(True)
                    else:
                        self.save_label(False)
                
                images=os.listdir(self.path_folder+'\\labeled\\images\\')
                num_unannot2=0
                if os.path.exists(self.path_folder+'\\images\\'):
                    images_un=os.listdir(self.path_folder+'\\images\\')
                    num_unannot2=len(images_un)
                images=sorted(images)
                start=0
                if image!=None:
                    start = images.index(image)
                if images!=[]:
                    self.list_images=images.copy()
                    try:
                        self.canvas.delete(self.shown_image)
                    except:
                        pass
                    for i in self.boxes:
                        self.canvas.delete(i)
                    self.Initialize()
                    self.labeled=True
                    self.cur=len(self.list_images)-1
                    path1=self.path_folder+'\\labeled\\images\\'+self.list_images[start]
                    path2=self.path_folder+'\\labeled\\labels\\'+self.list_images[start].replace('.jpg','.txt')
                    self.show_image2(path1, path2)
                    
                    self.current_image.set(start)
                    self.num_annotated.set(len(self.list_images))
                    self.num_unannotated.set(num_unannot2)
                    self.last_class=self.class_selected.get()
                    self.file.entryconfig("Unmark Image", state="disable")
                    self.file.entryconfig("Mark Image", state="normal")
                    self.file.entryconfig("Start at last marked", state="normal")
                    self.file.entryconfig("Delete Image", state="normal")
                    self.enabled_delete=True
                    self.enabled_mark = True
                    
                    
                else:
                    self.class_selected.set(self.last_class)
                    messagebox.showinfo('warnning!','No labeled images!')
            else:
                self.class_selected.set(self.last_class)
                messagebox.showinfo('warnning!','Please label the image!')
        except:
            pass
    def Unlabeled_com(self):
        try:
            cond = True
            print(self.list_images)
            if self.last_class==3 and len(self.list_images)!=0:
                cond=self.labeled
            if cond:
                if self.resave and len(self.boxes)!=0:
                    if self.cur>=self.current_image.get():
                        self.save_label(True)
                    else:
                        self.save_label(False)
                images=os.listdir(self.path_folder+'\\images\\')
                images=sorted(images)
                
                if images!=[]:
                    self.list_images=images
                    try:
                        self.canvas.delete(self.shown_image)
                    except:
                        pass
                    for i in self.boxes:
                        self.canvas.delete(i)
                    self.Initialize()
                    self.show_image(self.path_folder+'\\images\\'+self.list_images[0])
                    self.listbox.delete(0,END)
                    for i in self.list_yaml:
                        self.listbox.insert(END, i)
                    imgs=os.listdir(self.path_folder+'\\labeled\\labels')
                    self.num_annotated.set(len(imgs))
                    self.num_unannotated.set(len(self.list_images))
                    
                    self.last_class=self.class_selected.get()
                    self.file.entryconfig("Unmark Image", state="disable")
                    self.file.entryconfig("Mark Image", state="normal")
                    self.file.entryconfig("Delete Image", state="normal")
                    self.file.entryconfig("Start at last marked", state="disable")
                    self.enabled_mark = True
                    self.enabled_delete = True
                  
                    
                else:
                    self.class_selected.set(self.last_class)
                    messagebox.showinfo('warnning!','No unlabeled images!')
            else:
                self.class_selected.set(self.last_class)
                messagebox.showinfo('warnning!','Please label the image!')
        except:
            pass
    def Marked_com(self):
        try:
            if self.resave:
                if self.cur>=self.current_image.get():
                    self.save_label(True)
                else:
                    self.save_label(False)
            if os.path.exists(self.path_folder+'\\classes\\marked.txt'):
                list_imgs = []
                with open(self.path_folder+'\\classes\\marked.txt','r') as f1:
                    list_imgs=f1.read()
                list_imgs=list_imgs.splitlines()
                if len(list_imgs)!=0:
                    self.file.entryconfig("Delete Image", state="normal")
                    self.file.entryconfig("Unmark Image", state="normal")
                    self.file.entryconfig("Mark Image", state="disable")
                    self.file.entryconfig("Start at last marked", state="disable")
                    self.enabled_mark = False
                    self.enabled_delete = True
                    
                    self.list_images=list_imgs
                    self.canvas.delete(self.shown_image)
                    for i in self.boxes:
                        self.canvas.delete(i)
                    self.Initialize()
                    self.labeled=True
                    self.cur=len(self.list_images)-1
                    path1=self.path_folder+'\\labeled\\images\\'+self.list_images[0]
                    path2=self.path_folder+'\\labeled\\labels\\'+self.list_images[0].replace('.jpg','.txt')
                    self.show_image2(path1, path2)
                    
                    self.num_annotated.set(len(self.list_images))
                    self.num_unannotated.set(0)
                    self.last_class=self.class_selected.get()
                    
                else:
                    self.class_selected.set(self.last_class)
                    messagebox.showinfo('warnning!','There is no marked images!')
            else:
                self.class_selected.set(self.last_class)
                messagebox.showinfo('warnning!','There is no marked images!')
        except:
            pass
    
    def DeleteFromClasses(self,index):
        try:
            last_labels=[]
            with open(self.path_folder+'\\labeled\\labels\\'+self.list_images[index].replace('.jpg','.txt'),'r')as f1:
                last_labels=f1.read()
            last_labels=last_labels.splitlines()
            for line in last_labels:
                index_label=int(line.split(' ')[0])
                last_label=self.list_yaml[index_label]
                list_images=[]
                with open(self.path_folder+'\\classes\\'+last_label+'.txt','r') as f1:
                    list_images=f1.read()
                list_images=list_images.splitlines()
                
                list_images.remove(self.list_images[index])
                with open(self.path_folder+'\\classes\\'+last_label+'.txt','w') as f1:
                    for img in list_images:
                        f1.write(img+'\n')
        except:
            pass
    def DeleteImage(self,e=None):
        try:
            if self.enabled_delete:
                choose =messagebox.askyesno('warnning!','Do you want to delete this image?')
                if choose:
                    
                    self.labeled=True
                    DeletedImageNum=0
                    if len(self.list_images)!=1:
                        if self.current_image.get()!=len(self.list_images)-1:
                            self.bt_next_com('pass')
                            DeletedImageNum=self.current_image.get()-1
                        else:
                            self.bt_prev_com('pass')
                            DeletedImageNum=self.current_image.get()+1
                    else:
                        try:
                            self.canvas.delete(self.shown_image)
                        except:
                            pass
                        for i in self.boxes:
                            self.canvas.delete(i)
                        list_unannotated = os.listdir(self.path_folder+'\\images\\')
                        list_annotated = os.listdir(self.path_folder+'\\labeled\\images\\')
                        num_annot=len(list_annotated)
                        num_unannot=len(list_unannotated)
                        if list_unannotated == self.list_images:
                            num_unannot = 0
                        if list_annotated == self.list_images:
                            num_annot = 0
                        self.Initialize()
                        self.num_annotated.set(num_annot)
                        self.num_unannotated.set(num_unannot)
                        self.label_var.set('')
                        self.listbox.delete(0,END)
                        self.file.entryconfig("Delete Image", state="disable")
                        self.file.entryconfig("Mark Image", state="disable")
                        self.file.entryconfig("Start at last marked", state="disable")
                        self.enabled_mark = False
                        self.enabled_delete = False
                        
                    if os.path.exists(self.path_folder+'\\images\\'+self.list_images[DeletedImageNum]):
                        os.remove(self.path_folder+'\\images\\'+self.list_images[DeletedImageNum])
                    else:
                        os.remove(self.path_folder+'\\labeled\\images\\'+self.list_images[DeletedImageNum])
                        
                        self.DeleteFromClasses(DeletedImageNum)
                        os.remove(self.path_folder+'\\labeled\\labels\\'+self.list_images[DeletedImageNum].replace('.jpg','.txt'))
                    if os.path.exists(self.path_folder+'\\classes\\marked.txt'):
                        list_marked=[]
                        with open(self.path_folder+'\\classes\\marked.txt','r') as f1:
                            list_marked=f1.read()
                        list_marked=list_marked.splitlines()
                        
                        if self.list_images[DeletedImageNum] in list_marked:
                            list_marked.remove(self.list_images[DeletedImageNum])
                            with open(self.path_folder+'\\classes\\marked.txt','w') as f1:
                                for img in list_marked:
                                    f1.write(img+'\n')
                    self.list_images.pop(DeletedImageNum)
                    if DeletedImageNum==self.current_image.get()-1:
                        self.current_image.set(DeletedImageNum)
                
        except:
            pass
    def MarkImage(self,e=None):
        try:
            if self.enabled_mark:
                if self.labeled:
                    if not os.path.exists(self.path_folder+'\\classes\\'):
                        os.mkdir(self.path_folder+'\\classes\\')
                    if os.path.exists(self.path_folder+'\\classes\\marked.txt'):
                        list_marked=[]
                        with open(self.path_folder+'\\classes\\marked.txt','r') as f1:
                            list_marked=f1.read()
                        list_marked=list_marked.splitlines()
                        if not self.list_images[self.current_image.get()] in list_marked:
                            with open(self.path_folder+'\\classes\\marked.txt','a') as f1:
                                f1.write(self.list_images[self.current_image.get()]+'\n')
                            messagebox.showinfo('done!','marked!')
                        else:
                            messagebox.showinfo('warnning!',"It's already marked!")
                    else:
                        with open(self.path_folder+'\\classes\\marked.txt','a') as f1:
                            f1.write(self.list_images[self.current_image.get()]+'\n')
                        messagebox.showinfo('done!','marked!')
                else:
                    messagebox.showinfo('warnning!','please label image at first!')
        except:
            pass
    def UnmarkImage(self):
        try:
            
            if self.labeled:
                
                if self.resave:
                    self.save_label(True)
                    
                        
                unMarked_num=self.current_image.get()
                with open(self.path_folder+'\\classes\\marked.txt','w') as f1:
                    count=0
                    for img in self.list_images:
                        if count!=unMarked_num:
                            f1.write(img+'\n')
                        count+=1
                if len(self.list_images)!=1:
                    if self.current_image.get()!=len(self.list_images)-1:
                        self.bt_next_com('pass')
                        self.current_image.set(unMarked_num)
                    else:
                        self.bt_prev_com('pass')
                else:
                    try:
                        self.canvas.delete(self.shown_image)
                    except:
                        pass
                    for i in self.boxes:
                        self.canvas.delete(i)
                    list_unannotated = os.listdir(self.path_folder+'\\images\\')
                    list_annotated = os.listdir(self.path_folder+'\\labeled\\images\\')
                    num_annot=len(list_annotated)
                    num_unannot=len(list_unannotated)
                    if list_unannotated == self.list_images:
                        num_unannot = 0
                    if list_annotated == self.list_images:
                        num_annot = 0
                    self.Initialize()
                    self.num_annotated.set(num_annot)
                    self.num_unannotated.set(num_unannot)
                    self.label_var.set('')
                    self.listbox.delete(0,END)
                    self.file.entryconfig("Delete Image", state="disable")
                    self.file.entryconfig("Mark Image", state="disable")
                    self.file.entryconfig("Unmark Image", state="disable")
                    self.file.entryconfig("Start at last marked", state="disable")
                    self.enabled_mark = False
                    self.enabled_delete = False
                self.list_images.pop(unMarked_num)
        except:
            pass
    def Exit_prog(self):
        try:
            
            if self.labeled:
                if self.cur==self.current_image.get()-1:
                    self.save_label(False)
                if self.resave:
                    self.save_label(True)
                    
            self.destroy()
        except:
            self.destroy()
    def mouse_wheel(self,e):
        pass
    
    def NumImg(self):
        try:
            self.var_path=StringVar()
            x= int((self.width_screen-350)/2)
            y= int((self.height_screen-125)/2)
            self.win = Toplevel(background='#363636')
            self.win.iconbitmap(bitmap='icon.ico')
            self.win.geometry(f'350x125+{x}+{y}')
            self.win.resizable(0,0)
            self.win.title('DeepLabel')
            
            self.lbl_path = Label(self.win,text='Path',font=('arial',15),background='#363636',foreground='white')
            self.lbl_path.place(x=10,y=10)
            self.ent_path = Entry(self.win,relief=FLAT,font=('arial',13),textvariable=self.var_path)
            self.ent_path.place(x=10,y=45,width=300,height=25)
            self.bt_browse = Button(self.win,text='...',relief=FLAT,background='#2e2d2d',foreground='white',
                                    activebackground='#2e2d2d',bd=0,activeforeground='white',font=('arial',15),
                                    command=self.bt_browse_com)
            self.bt_browse.place(x=320,y=45,height=25,width=20)
            
            self.bt_Num = Button(self.win,text='Number',relief=FLAT,background='#2e2d2d',foreground='white',
                                    activebackground='#2e2d2d',bd=0,activeforeground='white',font=('arial',15),
                                    command=self.bt_Number_com)
            self.bt_Num.place(x=135,y=80)
        except:
            pass
    def bt_browse_com(self):
        try:
            self.path_folder = filedialog.askdirectory()
            self.var_path.set(self.path_folder)
        except:
            pass
    def bt_Number_com(self,path=None,start=None):
        try:
            if path!=None:
                folder_path=path
            else:
                folder_path=self.var_path.get()
            count=0
            if start!=None:
                count=start
            list_imgs=os.listdir(folder_path)
            limit = len(str(len(list_imgs)))
            if path!=None:
                limit=6
            for img in list_imgs:
                txt_count=str(count)
                while (len(txt_count)<limit):
                    txt_count='0'+txt_count
                os.rename(folder_path+'\\'+img,folder_path+'\\'+txt_count+'.jpg')
                count+=1
            if path==None:
                messagebox.showinfo('done!','Done!')
        except:
            pass
    def new_proj(self,e=None):
        try:
            if self.enabled==False:
                self.path_folder = filedialog.askdirectory()
                if (self.path_folder!='' and not os.path.exists(self.path_folder+'\\labeled')
                    and not os.path.exists(self.path_folder+'\\images')):
                    self.title('DeepLabel - '+self.path_folder)
                    os.mkdir(self.path_folder+'\\labeled\\')
                    with open(self.path_folder+'\\labeled\\data.yaml','w') as f1:
                        f1.write('names:\n')
                    self.current_image.set(0)
                    os.mkdir(self.path_folder+'\\labeled\\labels\\')
                    os.mkdir(self.path_folder+'\\labeled\\images\\')
                    os.mkdir(self.path_folder+'\\images\\')
                    
                    #self.list_images = os.listdir(self.path_folder+'\\images\\')
                    
                    #self.list_images=sorted(self.list_images)
                    
                    
                    #self.show_image(self.path_folder+'\\images\\'+self.list_images[self.current_image.get()])
                    self.num_annotated.set(0)
                    self.num_unannotated.set(0)
                    self.status=1
                    self.file.entryconfig("Delete Image", state="disable")
                    self.file.entryconfig("Mark Image", state="disable")
                    self.file.entryconfig("Close Proj", state="normal")
                    self.file.entryconfig("Health Check", state="normal")
                    self.file.entryconfig("Import Images", state="normal")
                    self.file.entryconfig("Rearrange", state="normal")
                    self.file.entryconfig("Export Data", state="normal")
                    self.classes.entryconfig("Unlabeled", state="normal")
                    self.classes.entryconfig("Labeled", state="normal")
                    self.classes.entryconfig("Marked", state="normal")
                    self.file.entryconfig("New Proj", state="disable")
                    self.file.entryconfig("Open Proj", state="disable")
                    self.file.entryconfig("Open External Proj", state="disable")
                    self.file.entryconfig("Start at last marked", state="disable")
                    self.file.entryconfig('Collect Multiple Labeled', state="disable")
                    self.enabled=True
                    self.enabled_mark = False
                    self.enabled_delete = False
        except:
            pass
            
    
    def show_image(self,path):
        try:
            img = Image.open(path)
            
            # real_width = img.width
            # real_height = img.height
            
            new_image=img.resize((1100,620))
            
            
            self.img = ImageTk.PhotoImage(new_image)
            
            
            self.shown_image=self.canvas.create_image((self.width-round(0.15625*self.width)-1100)/2,(round(self.height-(round(0.0351*self.height)+round(0.035*self.height)))-620)/2,image=self.img,anchor=NW)
        except:
            pass
    def getClasses(self):
        try:
            count=1
            list_files = os.listdir(self.path_folder+'\\labeled\\labels\\')
            for file in list_files:
                img=file[:len(file)-4]+'.jpg'
                list_labels=[]
                with open(self.path_folder+'\\labeled\\labels\\'+file,'r') as f1:
                    list_labels=f1.read()
                list_labels=list_labels.splitlines()
                for label in list_labels:
                    index_label = int(label.split(' ')[0])
                    label_name = self.list_yaml[index_label]
                    with open(self.path_folder+'\\classes\\'+label_name+'.txt','a') as f1:
                        f1.write(img+'\n')
                if int(len(list_files)/25)!=0:
                    if count%(int(len(list_files)/25))==0:
                        self.progBar['value']+=1
                else:
                    self.progBar['value']+=int(25/len(list_files))
                count+=1
        except:
            pass
                
    def moveFiles(self,path,progRange=25):
        try:
            list_images_train=os.listdir(path+'\\images\\')
            count=1
            for img in list_images_train:
                lbl=img[:len(img)-4]+'.txt'
                try:
                    shutil.move(path+'\\images\\'+img, 
                                self.path_folder+'\\labeled\\images\\'+img)
                    shutil.move(path+'\\labels\\'+lbl, 
                                self.path_folder+'\\labeled\\labels\\'+lbl)
                except:
                    pass
            
                if int(len(list_images_train)/progRange)!=0:
                    if count%(int(len(list_images_train)/progRange))==0:
                        self.progBar['value']+=1
                else:
                    self.progBar['value']+=int(progRange/len(list_images_train))
                count+=1
            
            list_images_train=os.listdir(path+'\\images\\')
            
            for img in list_images_train:
                lbl=img[:len(img)-4]+'.txt'
                try:
                    shutil.move(path+'\\images\\'+img, 
                                self.path_folder+'\\labeled\\images\\'+img)
                    shutil.move(path+'\\labels\\'+lbl, 
                                self.path_folder+'\\labeled\\labels\\'+lbl)
                except:
                    pass
            
            shutil.rmtree(path)
        except:
            pass
        
    
    def open_ex_proj_com(self):
        try:
            self.path_folder = filedialog.askdirectory()
            if (self.path_folder and os.path.exists(self.path_folder+'\\labeled\\') and 
                 os.path.exists(self.path_folder+'\\labeled\\train\\')):
                x= int((self.width_screen-300)/2)
                y= int((self.height_screen-80)/2)
                self.win_loading=Toplevel(background='#363636')
                self.win_loading.iconbitmap(bitmap='icon.ico')
                self.win_loading.geometry(f"300x80+{x}+{y}")
                self.win_loading.resizable(0,0)
                self.win_loading.title('DeepLabel')
                self.progBar = ttk.Progressbar(self.win_loading,orient=HORIZONTAL, length=280,mode="determinate")
                self.progBar.place(x=10,y=20)
    
                t1=Thread(target=self.open_external_project)
                t1.start()
        except:
            pass
        
        
            
        
    def open_external_project(self):
        try:
            self.title('DeepLabel - '+self.path_folder)
            
            os.mkdir(self.path_folder+'\\labeled\\images\\')
            os.mkdir(self.path_folder+'\\labeled\\labels\\')
            os.mkdir(self.path_folder+'\\classes\\')
            os.mkdir(self.path_folder+'\\images\\')
            
            
            self.moveFiles(self.path_folder+'\\labeled\\train')
            self.moveFiles(self.path_folder+'\\labeled\\test')
            self.moveFiles(self.path_folder+'\\labeled\\valid')
            
            
            list_yaml=[]
            with open(self.path_folder+'\\labeled\\data.yaml','r') as f1:
                list_yaml=f1.read()
            list_yaml=list_yaml.splitlines()
            new_list_yaml=[]
            for line in list_yaml:
                if line=='names:':
                    new_list_yaml.append(line)
                elif line.startswith('- '):
                    new_list_yaml.append(line)
            with open(self.path_folder+'\\labeled\\data.yaml','w') as f1:
                for line in new_list_yaml:
                    f1.write(line+'\n')
                    
            list_yaml=[]
            with open(self.path_folder+'\\labeled\\data.yaml','r') as f1:
                list_yaml=f1.read()
            list_yaml=list_yaml.splitlines()
            for i in range(1,len(list_yaml)):
                label=list_yaml[i].replace('- ','')
                self.list_yaml.append(label)
                self.classes.add_radiobutton(label=label,value=3+i,variable=self.class_selected,command=self.label_class)
            
            self.getClasses()
            
            self.class_selected.set(2)
            self.Labeled_com()
            self.progBar['value']=100
            self.win_loading.destroy()
            
            self.status=1
            self.file.entryconfig("Delete Image", state="normal")
            self.file.entryconfig("Mark Image", state="normal")
            self.file.entryconfig("Close Proj", state="normal")
            self.file.entryconfig("Health Check", state="normal")
            self.file.entryconfig("Import Images", state="normal")
            self.file.entryconfig("Rearrange", state="normal")
            self.file.entryconfig("Export Data", state="normal")
            self.classes.entryconfig("Unlabeled", state="normal")
            self.classes.entryconfig("Labeled", state="normal")
            self.classes.entryconfig("Marked", state="normal")
            self.file.entryconfig("New Proj", state="disable")
            self.file.entryconfig("Open Proj", state="disable")
            self.file.entryconfig("Open External Proj", state="disable")
            self.file.entryconfig("Start at last marked", state="disable")
            self.file.entryconfig('Collect Multiple Labeled', state="disable")
            if len(self.list_yaml)!=0:
                self.last_label = self.list_yaml[-1]
            self.enabled=True
            self.enabled_mark = True
            self.enabled_delete = True
        except:
            pass
    
    def open_proj(self,e=None):
        try:
            if self.enabled==False:
                self.path_folder = filedialog.askdirectory()
                if (self.path_folder and os.path.exists(self.path_folder+'\\labeled\\') and
                    os.path.exists(self.path_folder+'\\images\\') and
                    os.path.exists(self.path_folder+'\\labeled\\data.yaml')):
                    
                    self.title('DeepLabel - '+self.path_folder)
                    
                    list_UnlabeledImgs = os.listdir(self.path_folder+'\\images\\')
                    
                    list_yaml=[]
                    with open(self.path_folder+'\\labeled\\data.yaml','r') as f1:
                        list_yaml=f1.read()
                    list_yaml=list_yaml.splitlines()
                    
                    for i in range(1,len(list_yaml)):
                        label=list_yaml[i].replace('- ','')
                        self.list_yaml.append(label)
                        self.classes.add_radiobutton(label=label,value=3+i,variable=self.class_selected,command=self.label_class)
                        
                    if len(list_UnlabeledImgs)!=0:
                        
                        self.Unlabeled_com()
                        
                    else:
                        
                        self.class_selected.set(2)
                        self.Labeled_com()
                        
                        
                    
                    
                    self.status=1
                    self.file.entryconfig("Delete Image", state="normal")
                    self.file.entryconfig("Mark Image", state="normal")
                    self.file.entryconfig("Close Proj", state="normal")
                    self.file.entryconfig("Health Check", state="normal")
                    self.file.entryconfig("Import Images", state="normal")
                    self.file.entryconfig("Rearrange", state="normal")
                    self.file.entryconfig("Export Data", state="normal")
                    self.classes.entryconfig("Unlabeled", state="normal")
                    self.classes.entryconfig("Labeled", state="normal")
                    self.classes.entryconfig("Marked", state="normal")
                    self.file.entryconfig("New Proj", state="disable")
                    self.file.entryconfig("Open Proj", state="disable")
                    self.file.entryconfig("Open External Proj", state="disable")
                    self.file.entryconfig('Collect Multiple Labeled', state="disable")
                    if len(self.list_yaml)!=0:
                        self.last_label = self.list_yaml[-1]
                    self.enabled=True
                    self.enabled_mark = True
                    self.enabled_delete = True
        except:
            pass
            
    def close_proj(self,e=None):
        try:
            if self.enabled:
                if self.labeled:
                    if self.cur==self.current_image.get()-1:
                        self.save_label(False)
                    if self.resave:
                        self.save_label(True)
                        
                try:
                    self.canvas.delete(self.shown_image)
                except:
                    pass
                for i in self.boxes:
                    self.canvas.delete(i)
                self.title('DeepLabel')
                self.Initialize()
                self.list_yaml=[]
                self.num_annotated.set(0)
                self.num_unannotated.set(0)
                self.label_var.set('')
                self.listbox.delete(0,END)
                self.status=0
                self.classes.delete(4,END)
                self.last_class=1
                self.class_selected.set(1)
                self.file.entryconfig("Delete Image", state="disable")
                self.file.entryconfig("Mark Image", state="disable")
                self.file.entryconfig("Close Proj", state="disable")
                self.file.entryconfig("Health Check", state="disable")
                self.file.entryconfig("Import Images", state="disable")
                self.file.entryconfig("Rearrange", state="disable")
                self.file.entryconfig("Export Data", state="disable")
                self.classes.entryconfig("Unlabeled", state="disable")
                self.classes.entryconfig("Labeled", state="disable")
                self.classes.entryconfig("Marked", state="disable")
                self.file.entryconfig("New Proj", state="normal")
                self.file.entryconfig("Open Proj", state="normal")
                self.file.entryconfig("Open External Proj", state="normal")
                self.file.entryconfig('Collect Multiple Labeled', state="normal")
                self.file.entryconfig("Start at last marked", state="disable")
                self.enabled=False
                self.enabled_mark = False
                self.enabled_delete = False
        except:
            pass
        
    def health_check(self):
        try:
            
            if os.path.exists(self.path_folder+'\\classes\\'):
                x= int((self.width_screen-300)/2)
                y= int((self.height_screen-80)/2)
                self.win_loading=Toplevel(background='#363636')
                self.win_loading.iconbitmap(bitmap='icon.ico')
                self.win_loading.geometry(f"300x80+{x}+{y}")
                self.win_loading.resizable(0,0)
                self.win_loading.title('DeepLabel')
                self.progBar = ttk.Progressbar(self.win_loading,orient=HORIZONTAL, length=280,mode="determinate",
                                               )
                self.progBar.place(x=10,y=20)
                
                # t1=Thread(target=self.health_check_thread)
                
                # t1.start()
                self.health_check_thread()
        except:
            pass
            
            
            
    def health_check_thread(self):
        try:
            list_classes=os.listdir(self.path_folder+'\\classes\\')
            nums_classes=[]
            names_classes=[]
            count=1
            if 'marked.txt' in list_classes:
                list_classes.remove('marked.txt')
            for file in list_classes:
                list_imgs=[]
                names_classes.append(file.replace('.txt',''))
                with open(self.path_folder+'\\classes\\'+file,'r') as f1:
                    list_imgs=f1.read()
                list_imgs=list_imgs.splitlines()
                nums_classes.append(len(list_imgs))
                if int(len(list_classes)/100)!=0:
                    if count%(int(len(list_classes)/100))==0:
                        self.progBar['value']+=1
                else:
                    self.progBar['value']+=int(100/len(list_classes))
                count+=1
            self.progBar['value']=100
            self.win_loading.destroy()
            
            if max(nums_classes)!=0:
            
                self.win_health = Toplevel(background='#2e2d2d')
                self.win_health.iconbitmap(bitmap='icon.ico')
                self.win_health.title('DeepLabel')
                x= int((self.width_screen-1024)/2)
                y= int((self.height_screen-720)/2)
                self.win_health.geometry(f'1024x720+{x}+{y}')
                
                self.lbl_health_check = Label(self.win_health,text='Health Check',font=('arial',17),
                                              background='#2e2d2d',foreground='white')
                self.lbl_health_check.place(x=450,y=10)
                
                self.main_frame=Frame(self.win_health,bg='white')
                self.main_frame.place(x=10,y=60,width=1004,height=650)
                
                self.list_back = Canvas(self.main_frame,background='#363636',bd=0,relief=FLAT,
                                        scrollregion=(0,0,984,30*(len(names_classes)+1)),
                                        highlightthickness=0)
                self.list_back.place(x=0,y=0,width=984,height=650)
                
                self.my_scrollbar=ttk.Scrollbar(self.main_frame,orient=VERTICAL,command=self.list_back.yview)
                self.my_scrollbar.place(x=984,y=0,height=650,width=20)
                
                self.list_back.configure(yscrollcommand=self.my_scrollbar.set)
                
                self.second_frame=Frame(self.list_back,bg='#363636')
                
                self.list_back.create_window((0,0),window=self.second_frame,anchor='nw',width=984,height=30*(len(names_classes)+1))
                
                
                
                names_classes2 = [x for _,x in sorted(zip(nums_classes,names_classes),reverse=True)]
                
                
                
                count=1
                
                max_class = max(nums_classes)
                
                for class_name in names_classes2:
                    index = names_classes.index(class_name)
                    num = nums_classes[index]
                    
                    self.lbl=Label(self.second_frame,text=class_name,foreground='white',background='#363636',font=('arial',15))
                    
                    self.lbl.place(x=20,y=30*count)
                    
        
                    self.progBar = ttk.Progressbar(self.second_frame,orient=HORIZONTAL, length=600,mode="determinate",
                                                   )
                    self.progBar.place(x=250,y=30*count+5,height=20)
                    
                    
                    self.progBar['value'] = int((num/max_class)*100)
                    
                    self.lbl2 = Label(self.second_frame,text=str(num),foreground='white',background='#363636',font=('arial',13))
                    self.lbl2.place(x=860,y=30*count)
                    
                    count+=1
        except:
            pass
    def assign_first(self,e):
        try:
            if (self.status!=0) and self.list_images!=[]:
                if self.labeled or len(self.boxes)==0:
                    self.entered=True
                    self.canvas.delete(self.H_line)
                    self.canvas.delete(self.V_line)
                    self.flag=0
                    self.box_num=0
                    
                    for box in self.boxes:
                        bounds=self.canvas.bbox(box)
                        if (bounds[0]<e.x<bounds[2]) and (bounds[1]<e.y<bounds[3]):
                            self.pos_x=e.x-bounds[0]
                            self.pos_y=e.y-bounds[1]
                            self.flag=1
                            self.selected_box=True
                            self.label=self.boxes[self.box_num]
                            bounds=self.canvas.bbox(self.label)
                            self.label_width=bounds[2]-bounds[0]
                            self.label_height=bounds[3]-bounds[1]
                            break
                        self.box_num+=1
                    if not self.flag:
                        self.labeled=False
                        self.selected_box=True
                        self.start_x=e.x
                        self.start_y=e.y
                        self.label=self.canvas.create_rectangle(self.start_x,self.start_y,e.x,e.y,outline='yellow')
        except:
            pass
           
    def create_label(self,e):
        try:
            if self.status!=0:
                if self.entered:
                    if self.flag:
                        self.resave=True
                        self.move_box(e)
                    else:
                        self.canvas.delete(self.label)
                        self.label=self.canvas.create_rectangle(self.start_x,self.start_y,e.x,e.y,outline='yellow')
        except:
            pass
    def verify(self,e):
        try:
            if self.status!=0:
                if self.entered:
                    self.H_line=self.canvas.create_line(0,round(self.height-(round(0.0351*self.height)+round(0.035*self.height)))/2,self.width-round(0.15625*self.width),round(self.height-(round(0.0351*self.height)+round(0.035*self.height)))/2,dash=(5,1),fill='white')
                    self.V_line=self.canvas.create_line((self.width-round(0.15625*self.width))/2,0,(self.width-round(0.15625*self.width))/2,round(self.height-(round(0.0351*self.height)+round(0.035*self.height))),dash=(5,1),fill='white')
                    
                    try:
                        
                        if self.flag:
                            self.boxes[self.box_num]=self.label
                            self.ent_label.focus()
                        else:
                            self.boxes.append(self.label)
                            self.ent_label.focus()
                            
                            self.label_var.set(self.last_label)
                            self.ent_label.select_range(0,END)
                            self.listbox.delete(0,END)
                            self.listbox.insert(END,self.last_label)
                            self.labeled=True
                            if self.last_label=='start_label':
                                self.labeled=False
                            
                            self.list_labels_image.append(self.last_label)
                        self.resave=True
                    except:
                        pass
                    self.entered=False
        except:
            pass
    def bt_prev_com(self,e=None):
        try:
            if len(self.list_labels_image)==len(self.boxes):
                if self.status!=0:
                    if self.current_image.get()>0:
                        
                        if(self.labeled and not(self.cur>self.current_image.get()-1)) and e!='pass':
                            self.num_annotated.set(self.num_annotated.get()+1)
                            self.num_unannotated.set(self.num_unannotated.get()-1)
                            self.save_label(False)
                            self.cur=self.current_image.get()
                        elif self.resave and len(self.boxes)!=0:
                            self.save_label(True)
                        
                        if (self.labeled or self.cur==self.current_image.get()-1):
                            if(e=='pass'):
                                if self.cur!=self.current_image.get():
                                    self.num_unannotated.set(self.num_unannotated.get()-1)
                                elif self.cur==self.current_image.get():
                                    self.num_annotated.set(self.num_annotated.get()-1)
                                    self.cur-=1
                                
                            self.current_image.set(self.current_image.get()-1)
                            self.canvas.delete(self.shown_image)
                            for i in self.boxes:
                                self.canvas.delete(i)
                            self.boxes=[]
                            self.list_labels_image=[]
                            self.selected_box=False
                            self.selected=-1
                            path1=self.path_folder+'\\labeled\\images\\'+self.list_images[self.current_image.get()]
                            path2=self.path_folder+'\\labeled\\labels\\'+self.list_images[self.current_image.get()].replace('.jpg','.txt')
                            
                            self.show_image2(path1,path2)
                            self.labeled=True
                            self.resave=False
                            self.label_var.set('')
                            self.lbl_num.focus()
        except:
            pass
    def save_label(self,new_flag):
        try:
            if not new_flag:
                shutil.move(self.path_folder+'\\images\\'+self.list_images[self.current_image.get()],
                            self.path_folder+'\\labeled\\images\\'+self.list_images[self.current_image.get()])
            else:
                self.DeleteFromClasses(self.current_image.get())
                
            if not os.path.exists(self.path_folder+'\\classes\\'):
                os.mkdir(self.path_folder+'\\classes\\')
            
            
                
            
            with open(self.path_folder+'\\labeled\\labels\\'+self.list_images[self.current_image.get()].replace('.jpg','.txt'),'w') as f1:
                count=0
                for label in self.list_labels_image:
                    index=self.list_yaml.index(label)
                    bounds=self.canvas.bbox(self.boxes[count])
                    center_x=(((bounds[2]+bounds[0])/2)-(self.width-round(0.15625*self.width)-1100)/2)/1100
                    center_y=(((bounds[3]+bounds[1])/2)-(round(self.height-(round(0.0351*self.height)+round(0.035*self.height)))-620)/2)/620
                    width_x=(bounds[2]-bounds[0])/1100
                    height_y=(bounds[3]-bounds[1])/620
                   
                    f1.write(f'{index} {center_x} {center_y} {width_x} {height_y}')
                    if(count!=len(self.list_labels_image)-1):
                        f1.write('\n')
                        
                    list_images=[]
                    if os.path.exists(self.path_folder+'\\classes\\'+label+'.txt'):
                        with open(self.path_folder+'\\classes\\'+label+'.txt','r') as f2:
                            list_images=f2.read()
                        list_images=list_images.splitlines()
                    if count==0:
                        if not self.list_images[self.current_image.get()] in list_images:
                            with open(self.path_folder+'\\classes\\'+label+'.txt','a') as f3:
                                f3.write(self.list_images[self.current_image.get()]+'\n')
                    else:
                        with open(self.path_folder+'\\classes\\'+label+'.txt','a') as f3:
                            f3.write(self.list_images[self.current_image.get()]+'\n')
                    count+=1
                
        except:
            pass
            
    def show_image2(self,path1,path2):
        try:
            self.show_image(path1)
            txt=[]
            with open(path2,'r') as f1:
                txt=f1.readlines()
            self.listbox.delete(0,END)
            
            for line in txt:
                
                nums=line.split(' ')
                class_num=int(nums[0])
                x1=1100*2*float(nums[1])
                x2=1100*float(nums[3])
                start_x=(x1+x2)/2
                end_x=abs(x2-x1)/2
                y1=620*2*float(nums[2])
                y2=620*float(nums[4])
                start_y=(y1+y2)/2
                end_y=(y1-y2)/2
                var=self.canvas.create_rectangle(start_x+(self.width-round(0.15625*self.width)-1100)/2,start_y+(round(self.height-(round(0.0351*self.height)+round(0.035*self.height)))-620)/2,end_x+(self.width-round(0.15625*self.width)-1100)/2,end_y+(round(self.height-(round(0.0351*self.height)+round(0.035*self.height)))-620)/2,outline='yellow')
                self.boxes.append(var)
                self.listbox.insert(END,self.list_yaml[class_num])
                self.list_labels_image.append(self.list_yaml[class_num])
        except:
            pass
            
    def bt_next_com(self,e=None):
        try:
            if self.status!=0:
                if self.labeled:
                    
                    if(self.current_image.get()<len(self.list_images)-1):
                        self.labeled=False
                        
                        if(self.cur>self.current_image.get()):
                            if self.resave:
                                self.save_label(True)
                            self.labeled=True
                            
                            self.current_image.set(self.current_image.get()+1)
                            
                            for i in self.boxes:
                                self.canvas.delete(i)
                            self.boxes=[]
                            self.list_labels_image=[]
                            
                            path1=self.path_folder+'\\labeled\\images\\'+self.list_images[self.current_image.get()]
                            path2=self.path_folder+'\\labeled\\labels\\'+self.list_images[self.current_image.get()].replace('.jpg','.txt')
                            self.canvas.delete(self.shown_image)
                            self.show_image2(path1,path2)
                            if e=='pass':
                                self.num_annotated.set(self.num_annotated.get()-1)
                                self.cur-=1
                        elif(self.cur==self.current_image.get()):
                            
                            if self.resave:
                                self.save_label(True)
                            
                            
                            self.current_image.set(self.current_image.get()+1)
                            
                            self.canvas.delete(self.shown_image)
                            self.show_image(self.path_folder+'\\images\\'+self.list_images[self.current_image.get()])
                            self.listbox.delete(0,END)
                            for i in self.list_yaml:
                                self.listbox.insert(END,i)
                            for i in self.boxes:
                                self.canvas.delete(i)
                            self.boxes=[]
                            self.list_labels_image=[]
                            if e=='pass':
                                self.num_annotated.set(self.num_annotated.get()-1)
                                self.cur-=1
                        else:
                            if e=='pass':
                                pass
                            else:
                                self.num_annotated.set(self.num_annotated.get()+1)
                                self.save_label(False)
                                self.cur=self.current_image.get()
                            self.current_image.set(self.current_image.get()+1)
                            self.num_unannotated.set(self.num_unannotated.get()-1)
                            
                            
                            self.canvas.delete(self.shown_image)
                            self.show_image(self.path_folder+'\\images\\'+self.list_images[self.current_image.get()])
                            self.listbox.delete(0,END)
                            for i in self.list_yaml:
                                self.listbox.insert(END,i)
                            for i in self.boxes:
                                self.canvas.delete(i)
                            self.boxes=[]
                            self.list_labels_image=[]
                                
                        
                        self.selected_box=False
                        self.selected=-1
                        self.resave=False
                        self.label_var.set('')
                        self.lbl_num.focus()
                        
                        if len(self.boxes)==0:
                            self.labeled=False
        except:
            pass
                
    def resize_box(self,e):
        pass
    def mouse_motion(self,e):
        try:
            self.canvas.delete(self.H_line)
            self.canvas.delete(self.V_line)
            
            self.H_line=self.canvas.create_line(0,e.y,self.width-round(0.15625*self.width),e.y,dash=(5,1),fill='white')
            self.V_line=self.canvas.create_line(e.x,0,e.x,round(self.height-(round(0.0351*self.height)+round(0.035*self.height))),dash=(5,1),fill='white')
        except:
            pass
    def move_box(self,e=None):
        
        try:
            try:
                self.canvas.delete(self.label)
            except:
                pass
            self.start_x=e.x-self.pos_x
            self.start_y=e.y-self.pos_y
            self.label=self.canvas.create_rectangle(self.start_x,self.start_y,self.start_x+self.label_width,self.start_y+self.label_height,outline='yellow')
        except:
            pass
        # print('start x: ',self.start_x)
        # print('start y: ',self.start_y)
        # print('label width+x: ',self.label_width+self.start_x)
        # print('label height+y: ',self.label_height+self.start_y)
    def Writing(self,e):
        try:
            if self.status!=0:
                if(str(e.char)!='' and str(e.char) in chars):
                    
                    self.selected=-1
                    self.listbox.delete(0,END)
                    for i in self.list_yaml:
                        if (self.label_var.get() in i) and (self.label_var.get()!=''):
                            self.listbox.insert(0,i)
        except:
            pass
                    
    def SelectListbox(self,e):
        try:
            selected=self.listbox.curselection()
            if (selected!=()):
                self.selected_box=True
                self.box_num=selected[0]
        except:
            pass
        
            
    def delete_box(self,e):
        try:
            if self.selected_box:
                if len(self.list_labels_image)==len(self.boxes):
                    self.canvas.delete(self.boxes[self.box_num])
                    self.boxes.pop(self.box_num)
                    self.list_labels_image.pop(self.box_num)
                    self.listbox.delete(self.box_num)
                    self.resave = True
            if self.list_labels_image==[]:
                self.labeled=False
            self.selected_box=False
        except:
            pass
    def annotate_image(self,e):
        try:
            if self.status!=0:
                if self.selected_box:
                    self.label_var.set(self.label_var.get()+e.char)
        except:
            pass
    def label_class(self,image=None):
        try:
            cond = True
            if self.last_class==3 and len(self.list_images)!=0:
                cond=self.labeled
            if cond:
                if self.resave and len(self.boxes)!=0:
                    if self.cur>=self.current_image.get():
                        self.save_label(True)
                    else:
                        self.save_label(False)
                index_label=self.class_selected.get()-4
                label = self.list_yaml[index_label]
                list_imgs=[]
                if os.path.exists(self.path_folder+'\\classes\\'+label+'.txt'):
                    with open(self.path_folder+'\\classes\\'+label+'.txt','r') as f1:
                        list_imgs=f1.read()
                    list_imgs=list_imgs.splitlines()
                    list_imgs=set(list_imgs)
                    list_imgs=list(list_imgs)
                    if len(list_imgs)!=0:
                        cond = True
                        if image!=None:
                            cond = image in list_imgs
                        if cond:
                            self.list_images=list_imgs
                            self.canvas.delete(self.shown_image)
                            for i in self.boxes:
                                self.canvas.delete(i)
                            self.Initialize()
                            self.labeled=True
                            self.cur=len(self.list_images)-1
                            start=0
                            if image!=None:
                                start=self.list_images.index(image)
                            path1=self.path_folder+'\\labeled\\images\\'+self.list_images[start]
                            path2=self.path_folder+'\\labeled\\labels\\'+self.list_images[start].replace('.jpg','.txt')
                            self.show_image2(path1, path2)
                            
                            self.current_image.set(start)
                            
                            self.num_annotated.set(len(self.list_images))
                            self.num_unannotated.set(0)
                            self.last_class=self.class_selected.get()
                            self.file.entryconfig("Unmark Image", state="disable")
                            self.file.entryconfig("Mark Image", state="normal")
                            self.file.entryconfig("Delete Image", state="normal")
                            self.file.entryconfig("Start at last marked", state="normal")
                            self.enabled_mark = True
                            self.enabled_delete = True
                        else:
                            messagebox.showinfo('warnning!',"Last marked isn't in this calss!")
                    else:
                        self.class_selected.set(self.last_class)
                        messagebox.showinfo('warnning!',f'{label} class is Empty!')
                else:
                    self.class_selected.set(self.last_class)
                    messagebox.showinfo('warnning!',f'{label} class is Empty!')
            else:
                self.class_selected.set(self.last_class)
                messagebox.showinfo('warnning!','Please label the image!')
        except:
            pass
    def confirm_annotation(self,e):
        try:
            if self.status!=0:
                if self.selected_box:
                    if(self.selected!=-1):
                        self.label_var.set(self.listbox.get(self.selected))
                        
                    if self.label_var.get()!='':
                        isOk=True
                        for i in self.label_var.get():
                            if not i in chars:
                                isOk=False
                                break
                        if isOk:
                            self.last_label=self.label_var.get()
                            if not self.label_var.get() in self.list_yaml:
                                self.classes.add_radiobutton(label=self.label_var.get(),value=4+len(self.list_yaml),variable=self.class_selected,command=self.label_class)
                                with open(self.path_folder+'\\labeled\\data.yaml','a') as f1:
                                    f1.write(f'- {self.label_var.get()}\n')
                                self.list_yaml.append(self.label_var.get())
                                
                            if self.flag:
                                self.resave=True
                                
                            self.list_labels_image[self.box_num]=self.label_var.get()
                            self.listbox.delete(0,END)
                            for i in self.list_labels_image:
                                self.listbox.insert(END,i)
                            self.label_var.set('')
                            
                            self.labeled=True
                            self.selected_box=False
                            self.lbl_num.focus()
        except:
            pass
        
    def move_list_up(self,e):
        try:
            if(self.selected>0):
                self.selected-=1
                self.listbox.selection_clear(0,END)
                self.listbox.selection_set(self.selected)
        except:
            pass
    def move_list_down(self,e):
        try:
            if(self.selected<len(self.listbox.get(0,END))):
                self.selected+=1
                self.listbox.selection_clear(0,END)
                self.listbox.selection_set(self.selected)
        except:
            pass
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
a=App()
a.mainloop()