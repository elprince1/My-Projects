
import customtkinter as ctk
from tkinter import END,LEFT,filedialog
from threading import Thread

import sounddevice as sd
import wavio as wv
import time
import numpy as np
import datetime
from scipy.io import wavfile
import PIL
from ultralytics import YOLO




freq = 44100 #N = 44100*5

# Recording duration
duration = 30*60

model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)


ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('blue')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1024x720')
        self.title('Chat App')
        
        self.bind('<Return>',self.bt_send_com)
        
        self.list_persons=[]
        self.list_chat=[]
        self.list_frames=[]
        self.list_labels_info=[]
        self.list_rec={}   ####{index:[bt,slider,label],index2:[],index3:[],index4:[]}
        self.list_images=[]
        
        
        self.time1=0
        self.time2=0
        
        self.index_rec=-1
        
        self.timeNow=0
        self.stopped=0
        self.diff_chat=0
        
        self.playing=0
        self.Exactduration=0
        self.duration=0
        self.recording1=0
        self.my_name=''
        self.index_chat=-1
        self.index_mode=0
        ## 0 --> text
        ## 1 --> recording
        ## 2 --> stop record
        self.get_chats_Net()
        
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=5)
        
        self.upperFrame = ctk.CTkFrame(self,corner_radius=0,fg_color='#191919')
        self.upperFrame.grid(row=0,column=0,columnspan=2,sticky='nswe')
        
        self.upperFrame.grid_rowconfigure(0, weight=1)
        self.upperFrame.grid_columnconfigure((0,2,3), weight=0)
        self.upperFrame.grid_columnconfigure(1, weight=1)
        
        #################
        self.ch = ctk.CTkLabel(self.upperFrame, text=self.my_name[0],font=('arial',20,'bold'),height=30,width=30,fg_color='#037562',corner_radius=5)
        self.ch.grid(row=0,column=3,padx=10,pady=10)
        self.lbl_text=ctk.CTkLabel(self.upperFrame, text=self.my_name,font=('arial',16,'bold'))
        self.lbl_text.grid(row=0,column=2,pady=5,sticky='e')
        ##################
        
        self.bt_logOut = ctk.CTkButton(self.upperFrame, text='Logout',width=50,height=20,command=self.bt_logout_com)
        self.bt_logOut.grid(row=0,column=1,sticky='ws',pady=5)
        
        self.lblLogo = ctk.CTkLabel(self.upperFrame,text='Chat App',font=('arial',22,'bold'))
        self.lblLogo.grid(row=0,column=0,padx=10,pady=10)
        
        self.leftFrame = ctk.CTkScrollableFrame(self,fg_color='#403F3F',corner_radius=0)
        self.leftFrame.grid(row=1,column=0,sticky='nswe')
        
        self.leftFrame.grid_columnconfigure(0, weight=1)
        
        self.rightFrame = ctk.CTkFrame(self,fg_color='transparent',corner_radius=0)
        self.rightFrame.grid(row=1,column=1,sticky='nswe')
        
        self.rightFrame.grid_columnconfigure(0, weight=1)
        self.rightFrame.grid_rowconfigure((0,2,3), weight=0)
        self.rightFrame.grid_rowconfigure(1, weight=1)
        
        self.headerFrame = ctk.CTkFrame(self.rightFrame,corner_radius=0,fg_color='#212222',height=0)
        self.headerFrame.grid(row=0,column=0,sticky='nswe')
        
        self.headerFrame.grid_rowconfigure(0, weight=1)
        self.headerFrame.grid_columnconfigure(0, weight=0)
        self.headerFrame.grid_columnconfigure(1, weight=1)
        
        #self.lblChatName = ctk.CTkLabel(self.headerFrame,text='Ahmed Ali',font=('arial',20,'bold'))
        #self.lblChatName.grid(row=0,column=0,sticky='w',padx=10,pady=5)
        
        self.chatFrame = ctk.CTkScrollableFrame(self.rightFrame,corner_radius=0)
        self.chatFrame.grid(row=1,column=0,sticky='nswe')
        self.chatFrame.grid_columnconfigure(0, weight=1)
        
        self.recFrame = ctk.CTkFrame(self.rightFrame,fg_color='#212222',corner_radius=0,height=0)
        self.recFrame.grid(row=2,column=0,sticky='nswe')
        
        self.recFrame.grid_rowconfigure(0, weight=1)
        
        self.recFrame.grid_columnconfigure((0,2,3,4), weight=0)
        self.recFrame.grid_columnconfigure(1, weight=1)
        
        self.recFrame.grid_forget()
        
        
        
        self.footerFrame = ctk.CTkFrame(self.rightFrame,corner_radius=0,height=0)
        self.footerFrame.grid(row=3,column=0,sticky='nswe')
        
        self.footerFrame.grid_rowconfigure(0, weight=1)
        self.footerFrame.grid_columnconfigure(0, weight=1)
        self.footerFrame.grid_columnconfigure(1, weight=0)
        self.footerFrame.grid_columnconfigure(2, weight=0)
        
        self.frame_images = ctk.CTkScrollableFrame(self.rightFrame)
        # self.frame_images.grid(row=0,column=0,rowspan=3,sticky='nswe')
        
        self.load_chats(self.list_persons)
        self.init_chat(None,self.index_chat,self.list_chat[self.index_chat])#,e,index,list_chat
    
    
    
        # variables of chat rec
        self.playing_chat=0
        self.stopped_chat=0
        self.Exactduration_chat=0
        self.duration_chat=0
    
    
    
    def bt_logout_com(self):
        pass
    
    
    def bt_send_com(self,e=None):
        ent_user = self.ent.get()
        self.ent.delete(0,END)
        
        if self.index_mode==0:
            # text
            if ent_user!='':
                self.bsk_frame =ctk.CTkFrame(self.chatFrame,fg_color='transparent')
                self.bsk_frame.grid(row=len(self.list_frames),column=0,sticky='e',ipady=5)
                
                
                self.bsk_frame.grid_columnconfigure((0,1), weight=0)
                self.bsk_frame.grid_rowconfigure(0, weight=1)
                
                self.ch = ctk.CTkLabel(self.bsk_frame, text=self.my_name[0],font=('arial',20,'bold'),height=30,width=30,fg_color='#037562',corner_radius=5)
                self.ch.grid(row=0,column=1,padx=10,pady=10,sticky='n')
                
                self.frame_text = ctk.CTkFrame(self.bsk_frame,corner_radius=15,height=30,fg_color='#212222')
                self.frame_text.grid(row=0,column=0)
                
                self.lbl_text=ctk.CTkLabel(self.frame_text, text=ent_user,font=('arial',20),wraplength=200,justify=LEFT)
                self.lbl_text.grid(row=0,column=0,padx=10,pady=5,sticky='w')
                
                self.list_frames.append(self.bsk_frame)
                
                
                
                self.lower_frame = ctk.CTkFrame(self.frame_text,fg_color='transparent',corner_radius=20)
                self.lower_frame.grid(row=1,column=0,pady=2,padx=7,sticky='nswe')
                
                self.lower_frame.grid_rowconfigure(0, weight=0)
                
                self.lower_frame.grid_columnconfigure(0, weight=0)
                
                self.lower_frame.grid_columnconfigure(1, weight=1)
                
                timeNow = datetime.datetime.now()
                hour = timeNow.hour
                AM_PM = ' AM'
                if hour>=12:
                    AM_PM = ' PM'
                    if hour>12:
                        hour-=12
                hour = str(hour)
                minute = str(timeNow.minute)
                if len(hour)==1:
                    hour='0'+hour
                if len(minute)==1:
                    minute='0'+minute
                timeNowStr = hour + ':'+ minute + AM_PM
                
                self.lbl_time = ctk.CTkLabel(self.lower_frame,text=timeNowStr,font=('arial',11),text_color='#403F3F')
                self.lbl_time.grid(row=0,column=1,sticky='w',padx=5)
                
                
                self.lbl_seen = ctk.CTkLabel(self.lower_frame,text='.',text_color='red')
                self.lbl_seen.grid(row=0,column=0)
                
                self.list_labels_info[self.index_chat][0].configure(text=ent_user[0:10]+('...' if len(ent_user)>10 else ''))
                self.list_labels_info[self.index_chat][1].configure(text=timeNowStr)
                
                
                self.list_chat[self.index_chat].append({'M':ent_user,'R':False,'seen':False,'time':timeNowStr,'I':False})
                
            else:
                self.bt_send.configure(text='Stop')
                self.time1=time.time()
                t1 = Thread(target=self.record_fcn)
                t1.start()
                self.index_mode=1
        elif self.index_mode==1:
            # stop
            self.time2=time.time()
            self.Exactduration=self.time2-self.time1
            self.recFrame.grid(row=2,column=0,sticky='nswe')
            #print(self.recording1)
            sd.stop()
            self.timeNow=datetime.datetime.now()
            #print(self.recording1)
            wv.write(f"{self.timeNow.year}-{self.timeNow.month}-{self.timeNow.day}-{self.timeNow.hour}-{self.timeNow.minute}-{self.timeNow.second}.wav", self.recording1[0:int(self.Exactduration*freq)], freq, sampwidth=2)
            self.bt_send.configure(text='Send/Rec')
            self.index_mode=2
            self.bt_play = ctk.CTkButton(self.recFrame,text='|>',font=('arial',18,'bold'),width=30,command=self.bt_Play_com)
            self.bt_play.grid(row=0,column=0,padx=5,pady=10)
            
            self.slider_rec = ctk.CTkSlider(self.recFrame,command=self.slider_com)
            self.slider_rec.grid(row=0,column=1,sticky='we',padx=5,pady=10)
            self.slider_rec.set(0)
            
            self.lbl_time = ctk.CTkLabel(self.recFrame,text='00:00|'+self.time_formate(int(np.ceil(self.Exactduration))))
            self.lbl_time.grid(row=0,column=2,padx=5,pady=10)
            
            self.bt_send_rec = ctk.CTkButton(self.recFrame,text='send',font=('arial',18),command=self.bt_send_rec_com)
            self.bt_send_rec.grid(row=0,column=3,padx=5,pady=10)
            
            self.bt_remove = ctk.CTkButton(self.recFrame, text='X',font=('arial',18,'bold'),width=30,fg_color='#403F3F',hover_color='red',command=self.exit_rec)
            self.bt_remove.grid(row=0,column=4,padx=5,pady=10)
    
    
    def exit_rec(self):
        self.recFrame.grid_forget()
        self.index_mode=0
        sd.stop()
        self.playing=0
        self.stopped=1
    def bt_send_rec_com(self):
        self.bsk_frame =ctk.CTkFrame(self.chatFrame,fg_color='transparent')
        self.bsk_frame.grid(row=len(self.list_frames),column=0,sticky='e',ipady=5)
        
        
        self.bsk_frame.grid_columnconfigure((0,1), weight=0)
        self.bsk_frame.grid_rowconfigure(0, weight=1)
        
        self.ch = ctk.CTkLabel(self.bsk_frame, text=self.my_name[0],font=('arial',20,'bold'),height=30,width=30,fg_color='#037562',corner_radius=5)
        self.ch.grid(row=0,column=1,padx=10,pady=10,sticky='n')
        
        self.frame_rec = ctk.CTkFrame(self.bsk_frame,corner_radius=15,height=30,fg_color='#212222')
        self.frame_rec.grid(row=0,column=0)
        
        self.frame_rec.grid_rowconfigure(0, weight=1)
        self.frame_rec.grid_columnconfigure((0,2), weight=0)
        self.frame_rec.grid_columnconfigure(1, weight=1)
        
        self.bt_play_chat = ctk.CTkButton(self.frame_rec,text='|>',font=('arial',18,'bold'),width=30,fg_color='#037562',command =lambda a=len(self.list_frames): self.bt_Play_chat_com(a))
        self.bt_play_chat.grid(row=0,column=0,padx=5,pady=10)
        
        self.slider_rec_chat = ctk.CTkSlider(self.frame_rec,button_color='#037562',command=lambda val, ind=len(self.list_frames):self.slider_chat_com(val,ind))
        self.slider_rec_chat.grid(row=0,column=1,sticky='we',padx=5,pady=10)
        self.slider_rec_chat.set(0)
        
        self.lbl_time_chat = ctk.CTkLabel(self.frame_rec,text='00:00|'+self.time_formate(int(np.ceil(self.Exactduration))))
        self.lbl_time_chat.grid(row=0,column=2,padx=5,pady=10)
        
        self.list_rec[len(self.list_frames)]=[self.bt_play_chat,self.slider_rec_chat,self.lbl_time_chat]
        
        self.list_frames.append(self.bsk_frame)
        
        
        self.lower_frame = ctk.CTkFrame(self.frame_rec,fg_color='transparent',corner_radius=20)
        self.lower_frame.grid(row=1,column=0,columnspan=3,pady=2,padx=7,sticky='nswe')
        
        self.lower_frame.grid_rowconfigure(0, weight=0)
        
        self.lower_frame.grid_columnconfigure(0, weight=0)
        
        self.lower_frame.grid_columnconfigure(1, weight=1)
        
        timeNow = datetime.datetime.now()
        hour = timeNow.hour
        AM_PM = ' AM'
        if hour>=12:
            AM_PM = ' PM'
            if hour>12:
                hour-=12
        hour = str(hour)
        minute = str(timeNow.minute)
        if len(hour)==1:
            hour='0'+hour
        if len(minute)==1:
            minute='0'+minute
        timeNowStr = hour + ':'+ minute + AM_PM
        
        self.lbl_time = ctk.CTkLabel(self.lower_frame,text=timeNowStr,font=('arial',11),text_color='#403F3F')
        self.lbl_time.grid(row=0,column=1,sticky='w',padx=5)
        
        self.list_labels_info[self.index_chat][0].configure(text='record')
        self.list_labels_info[self.index_chat][1].configure(text=timeNowStr)
        
        
        
        self.lbl_seen = ctk.CTkLabel(self.lower_frame,text='.',text_color='red')
        self.lbl_seen.grid(row=0,column=0)


        
        
        
        
        
        self.list_chat[self.index_chat].append({'M':f"{self.timeNow.year}-{self.timeNow.month}-{self.timeNow.day}-{self.timeNow.hour}-{self.timeNow.minute}-{self.timeNow.second}.wav",'R':True,'seen':False,'time':timeNowStr,'I':False})
        
        
        self.exit_rec()
    def slider_com(self,value):
        self.bt_Play_com()
    def bt_Play_com(self):
        if self.playing_chat==0:
            if self.playing==0: 
                self.stopped=0
                self.bt_play.configure(text='||')
                sd.play(self.recording1[int(self.slider_rec.get()*self.Exactduration*freq):int(self.Exactduration*freq)],freq)
                self.duration = int(self.slider_rec.get()*self.Exactduration)
                self.t1 = Thread(target=self.duration_func)
                self.t1.start()
                self.playing=1
            else:
                self.bt_play.configure(state='disabled')
                self.slider_rec.configure(state='disabled')
                self.bt_play.configure(text='|>')
                sd.stop()
                self.playing=0
                self.stopped=1
        else:
            self.playing_chat=0
            self.list_rec[self.index_rec][0].configure(state='disabled')
            self.list_rec[self.index_rec][1].configure(state='disabled')
            self.list_rec[self.index_rec][0].configure(text='|>')
            sd.stop()
            self.stopped_chat=1
            
            while( self.list_rec[self.index_rec][0].cget('state')!='normal'):
                pass
            self.bt_Play_com()
            
            
    def duration_func(self):
        while(self.duration<self.Exactduration and self.stopped==0): # 5.2 --> 5 6
            self.duration+=1
            self.lbl_time.configure(text=self.time_formate(self.duration)+'|'+self.time_formate(int(np.ceil(self.Exactduration))))#01:10|2:00
            self.slider_rec.set(self.duration/self.Exactduration)
            time.sleep(1)
        if self.stopped==0:
            self.bt_play.configure(text='|>')
            self.slider_rec.set(0)
            self.duration=0
            self.playing=0
            self.lbl_time.configure(text='00:00|'+self.time_formate(int(np.ceil(self.Exactduration))))
        else:
            self.stopped=0
            self.bt_play.configure(state='normal')
            self.slider_rec.configure(state='normal')
    def time_formate(self,sec): # 70
        minutes = str(int(sec/60))  #01
        seconds = str(sec%60)       #10
        if(len(minutes)==1):
            minutes='0'+minutes
        if(len(seconds)==1):
            seconds='0'+seconds
        
        return minutes+':'+seconds
        
        
            
    def record_fcn(self):
        self.recording1 = sd.rec(int(duration * freq), samplerate=freq, channels=2)
    def get_chats_Net(self):
        self.my_name = "Mostafa Prince"
        self.list_persons=[
            {
                "name":'Mostafa Khaled',
                'time':'8:26 PM'
            },
            {
                "name":'Ahmed Mohamed',
                'time':'9:16 PM'
            },
        ]
        self.list_chat=[
            [{'H':'hello','R':False,'time':'11:25 PM','seen':True,'I':False},
             {'M':'hello,','R':False,'time':'11:26 PM','seen':True,'I':False},
             {'H':'how are you?','R':False,'time':'12:25 AM','seen':True,'I':False},
             {'M':"I'm fine. I want to tell you some thing.",'R':False,'time':'01:25 AM','seen':True,'I':False},
             {'H':r'C:\Users\ELPRINCE\Desktop\2024-1-16-9-32-32.wav','R':True,'time':'01:26 AM','seen':True,'I':False}],
            [{'H':'hello','R':False,'time':'01:25 PM','seen':True,'I':False},
             {'M':'Hello,','R':False,'time':'02:25 PM','seen':True,'I':False},
             {'H':'How old are you?','R':False,'time':'03:35 PM','seen':True,'I':False},
             {'H':[r'C:\Users\ELPRINCE\Desktop\image.png',
                   r'C:\Users\ELPRINCE\Desktop\image.png',
                   r'C:\Users\ELPRINCE\Desktop\image.png',
                   r'C:\Users\ELPRINCE\Desktop\image.png',
                   r'C:\Users\ELPRINCE\Desktop\image.png'],'R':False,'time':'03:45 PM','seen':True,'I':True},
             
             
            {'M':"15",'R':False,'time':'04:20 PM','seen':True,'I':False},
            {'M':[r'C:\Users\ELPRINCE\Desktop\image.png'],'R':False,'time':'04:20 PM','seen':True,'I':True},
            ]
        ]
        
    def load_chats(self,ListPersons):
        for i in range(len(ListPersons)):
            info = list(self.list_chat[i][-1].values())[0]
            if list(self.list_chat[i][-1].values())[1]:
                info='record'
            if self.list_chat[i][-1]['I']:
                info='image'
                
            self.basicFrame = ctk.CTkFrame(self.leftFrame,fg_color='transparent',height=100,corner_radius=0)
            self.basicFrame.grid(row=i,column=0,sticky='nswe',pady=5)
            
            self.basicFrame.grid_rowconfigure(0, weight=1)
            self.basicFrame.grid_columnconfigure(0, weight=0)
            self.basicFrame.grid_columnconfigure(1, weight=1)
            
            self.lbl_ch = ctk.CTkLabel(self.basicFrame, text=ListPersons[i]['name'][0],font=('arial',20,'bold'),height=40,width=40,fg_color='#1AA1BF',corner_radius=10)
            self.lbl_ch.grid(row=0,column=0,padx=10,pady=10)
            self.lbl_ch.bind('<Button-1>',lambda e,a=i,chat=self.list_chat[i] :self.init_chat(e,a,chat))
            
            
            self.frameInfo = ctk.CTkFrame(self.basicFrame,fg_color='transparent',corner_radius=0)
            self.frameInfo.grid(row=0,column=1,sticky='nswe')
            self.frameInfo.bind('<Button-1>',lambda e,a=i,chat=self.list_chat[i] :self.init_chat(e,a,chat))
            
            self.frameInfo.grid_columnconfigure(0, weight=1)
            self.frameInfo.grid_rowconfigure((1,2,3), weight=0)
            self.frameInfo.grid_rowconfigure((0,4), weight=1)
            
            self.lbl_name=ctk.CTkLabel(self.frameInfo, text=ListPersons[i]['name'][0:20]+('...' if len(ListPersons[i]['name'])>20 else ''),font=('arial',18,'bold'),height=5)
            self.lbl_name.grid(row=1,column=0,sticky='w')
            self.lbl_name.bind('<Button-1>',lambda e,a=i,chat=self.list_chat[i] :self.init_chat(e,a,chat))
            
            self.lbl_Info=ctk.CTkLabel(self.frameInfo, text=info[0:10]+('...' if len(info)>10 else ''),font=('arial',15),height=5)
            self.lbl_Info.grid(row=2,column=0,sticky='w')
            self.lbl_Info.bind('<Button-1>',lambda e,a=i,chat=self.list_chat[i] :self.init_chat(e,a,chat))
            
            
            self.lbl_time=ctk.CTkLabel(self.frameInfo, text=ListPersons[i]['time'],font=('arial',15),height=5)
            self.lbl_time.grid(row=3,column=0,sticky='w')
            self.lbl_time.bind('<Button-1>',lambda e,a=i,chat=self.list_chat[i] :self.init_chat(e,a,chat))
            
            self.list_labels_info.append([self.lbl_Info,self.lbl_time])
            
            self.lbl_divider = ctk.CTkFrame(self.basicFrame,fg_color='#1AA1BF',height=3)
            self.lbl_divider.grid(row=1,column=0,columnspan=2,sticky='nswe',pady=5,padx=5)
    
    def browse_images(self):
        self.images=filedialog.askopenfilenames()
        if self.images:
            
            for widget in self.list_images:
                widget.grid_forget()
            self.list_images=[]
            self.frame_images.grid(row=0,column=0,rowspan=3,sticky='nswe')
            self.frame_images.grid_columnconfigure(0, weight=1)
            
            for ind in range(len(self.images)):
                self.img = PIL.Image.open(self.images[ind])
                self.img = ctk.CTkImage(light_image=self.img,size=(350,450))
                self.lbl_img = ctk.CTkLabel(self.frame_images, text='',image=self.img)
                self.lbl_img.grid(row=ind,column=0,pady=10)
                self.list_images.append(self.lbl_img)
            self.bt_exit = ctk.CTkButton(self.frame_images, text='X',width=50,command=self.bt_exit_image_com)
            self.bt_exit.grid(row=0,column=0,padx=10,pady=10,sticky='ne')
            self.list_images.append(self.bt_exit)
            
            self.frame_left = ctk.CTkScrollableFrame(self.frame_images,width=150)
            self.frame_left.grid(row=0,column=0,padx=10,pady=10,sticky='nsw')
            self.bt_send_image = ctk.CTkButton(self.frame_left, text='send',command=self.bt_send_image_com)
            self.bt_send_image.pack()
            self.list_images.append(self.frame_left)
            
            for ind in range(len(self.images)):
                results = model(self.images[ind])  # predict on an image
                
                
                for i in results[0].boxes.cls:
                    #print(model.names[int(i)])
                    self.frame_cont = ctk.CTkFrame(self.frame_left,corner_radius=20,border_color='white',border_width=2,width=100,fg_color='transparent')
                    self.frame_cont.pack(pady=10,fill='both',expand=True)
                    self.lbl_obj = ctk.CTkLabel(self.frame_cont,text=model.names[int(i)])
                    self.lbl_obj.pack(padx=5,pady=5)
                
    def bt_send_image_com(self):
        loop=1
        if len(self.images)<4:
            loop = len(self.images)
            
        for i in range(0,loop):
            self.bsk_frame =ctk.CTkFrame(self.chatFrame,fg_color='transparent')
            self.bsk_frame.grid(row=len(self.list_frames),column=0,sticky='e',ipady=5)
            
            
            self.bsk_frame.grid_columnconfigure((0,1), weight=0)
            self.bsk_frame.grid_rowconfigure(0, weight=1)
            
            self.ch = ctk.CTkLabel(self.bsk_frame, text=self.my_name[0],font=('arial',20,'bold'),height=30,width=30,fg_color='#037562',corner_radius=5)
            self.ch.grid(row=0,column=1,padx=10,pady=10,sticky='n')
            
            self.frame_text = ctk.CTkFrame(self.bsk_frame,corner_radius=15,height=30,fg_color='#212222')
            self.frame_text.grid(row=0,column=0)
            
            if len(self.images)>=4:
                self.master_frame = ctk.CTkFrame(self.frame_text,fg_color='transparent')
                self.master_frame.grid(row=0,column=0,padx=10,pady=10)
                self.master_frame.columnconfigure((0,1), weight=0)
                self.master_frame.rowconfigure((0,1), weight=0)
                for ind in range(0,4):
                    binary = bin(ind).replace('0b','')
                    if len(binary)==1:
                        binary='0'+binary
                    self.img = PIL.Image.open(self.images[ind])
                    self.img = ctk.CTkImage(light_image=self.img,size=(75,100))
                    self.lbl_img = ctk.CTkLabel(self.master_frame, text='',image=self.img)
                    
                    self.lbl_img.grid(row=binary[0],column=binary[1])
                    self.lbl_img.bind('<Button-1>',lambda  e, a=len(self.list_frames): self.openImage(e,a))
                if len(self.images)>4:
                    diff = len(self.images) -4 
                    self.lbl_diff = ctk.CTkLabel(self.lbl_img,text='+'+str(diff),font=('arial',18))
                    self.lbl_diff.grid(row=0,column=0,sticky='se')
            else:
                self.img = PIL.Image.open(self.images[i])
                self.img = ctk.CTkImage(light_image=self.img,size=(150,200))
                self.lbl_img = ctk.CTkLabel(self.frame_text, text='',image=self.img)
                self.lbl_img.grid(row=0,column=0,padx=10,pady=10)
                self.lbl_img.bind('<Button-1>',lambda  e, a=len(self.list_frames): self.openImage(e,a))
            
            self.lower_frame = ctk.CTkFrame(self.frame_text,fg_color='transparent',corner_radius=20)
            self.lower_frame.grid(row=1,column=0,pady=2,padx=7,sticky='nswe')
            
            self.lower_frame.grid_rowconfigure(0, weight=0)
            
            self.lower_frame.grid_columnconfigure(0, weight=0)
            
            self.lower_frame.grid_columnconfigure(1, weight=1)
            
            timeNow = datetime.datetime.now()
            hour = timeNow.hour
            AM_PM = ' AM'
            if hour>=12:
                AM_PM = ' PM'
                if hour>12:
                    hour-=12
            hour = str(hour)
            minute = str(timeNow.minute)
            if len(hour)==1:
                hour='0'+hour
            if len(minute)==1:
                minute='0'+minute
            timeNowStr = hour + ':'+ minute + AM_PM
            
            self.lbl_time = ctk.CTkLabel(self.lower_frame,text=timeNowStr,font=('arial',11),text_color='#403F3F')
            self.lbl_time.grid(row=0,column=1,sticky='w',padx=5)
            
            
            self.lbl_seen = ctk.CTkLabel(self.lower_frame,text='.',text_color='red')
            self.lbl_seen.grid(row=0,column=0)
            
            self.list_labels_info[self.index_chat][0].configure(text='images')
            self.list_labels_info[self.index_chat][1].configure(text=timeNowStr)
            
            if loop==1:
                self.list_chat[self.index_chat].append({'M':list(self.images),'R':False,'time':timeNowStr,'seen':False,'I':True})
            else:
                self.list_chat[self.index_chat].append({'M':[self.images[i]],'R':False,'time':timeNowStr,'seen':False,'I':True})
            self.list_frames.append(self.bsk_frame)
        
        self.frame_images.grid_forget()
    def init_chat(self,e,index,list_chat):
        if self.index_chat==-1 and self.index_chat!=index:
            self.ent = ctk.CTkEntry(self.footerFrame,placeholder_text='write here')
            self.ent.grid(row=0,column=0,sticky='nswe',padx=5,pady=10)
            
            
            self.bt_browse = ctk.CTkButton(self.footerFrame, text='...',width=50,command=self.browse_images)
            self.bt_browse.grid(row=0,column=1)
            
            self.bt_send = ctk.CTkButton(self.footerFrame, text='Send/Rec',font=('arial',18),command=self.bt_send_com)
            self.bt_send.grid(row=0,column=2,padx=5,pady=10)
            
        if self.index_chat!=index:
            if self.playing_chat==1:
                self.diff_chat=1
                
                sd.stop()
                self.playing_chat=0
                
                
                
            self.exit_rec()
            
            self.index_chat = index
            
            self.ch = ctk.CTkLabel(self.headerFrame, text=self.list_persons[index]['name'][0],font=('arial',20,'bold'),height=30,width=30,fg_color='#1AA1BF',corner_radius=5)
            self.ch.grid(row=0,column=0,padx=10,pady=10)
        
            
            self.lbl_text=ctk.CTkLabel(self.headerFrame, text=self.list_persons[index]['name'],font=('arial',16,'bold'))
            self.lbl_text.grid(row=0,column=1,pady=5,sticky='w')
            
            for i in range(len(self.list_frames)):
                self.list_frames[i].grid_forget()
                
            self.list_frames=[]
            self.list_rec={}
                
            
            for i in range(len(list_chat)):
                stick='e'
                sticky_time='w'
                row_pos=1
                ch=self.my_name[0]
                color='#037562'
                key_send_per = list(list_chat[i].keys())[0]
                if key_send_per=='H':
                    sticky_time='e'
                    stick='w'
                    row_pos=0
                    ch = self.list_persons[index]['name'][0]
                    color='#1AA1BF'
                
                
                
                self.bsk_frame =ctk.CTkFrame(self.chatFrame,fg_color='transparent')
                self.bsk_frame.grid(row=i,column=0,sticky=stick,ipady=5)
                
                
                
                self.bsk_frame.grid_columnconfigure((0,1), weight=0)
                self.bsk_frame.grid_rowconfigure(0, weight=1)
                
                self.ch = ctk.CTkLabel(self.bsk_frame, text=ch,font=('arial',20,'bold'),height=30,width=30,fg_color=color,corner_radius=5)
                self.ch.grid(row=0,column=row_pos,padx=10,pady=10,sticky='n')
                
                self.frame_text = ctk.CTkFrame(self.bsk_frame,corner_radius=15,height=30,fg_color='#212222')
                self.frame_text.grid(row=0,column=1-row_pos)
                
                self.frame_text.grid_rowconfigure((0,1), weight=0)
                self.frame_text.grid_columnconfigure(0, weight=0)
                
                if list_chat[i]['I']:
                    # 1 2 3 \\ 4 5 6 7 
                    if len(list_chat[i][key_send_per])>=4:
                        self.master_frame = ctk.CTkFrame(self.frame_text,fg_color='transparent')
                        self.master_frame.grid(row=0,column=0,padx=10,pady=10)
                        self.master_frame.columnconfigure((0,1), weight=0)
                        self.master_frame.rowconfigure((0,1), weight=0)
                        for ind in range(0,4):
                            binary = bin(ind).replace('0b','')
                            if len(binary)==1:
                                binary='0'+binary
                            self.img = PIL.Image.open(list_chat[i][key_send_per][ind])
                            self.img = ctk.CTkImage(light_image=self.img,size=(75,100))
                            self.lbl_img = ctk.CTkLabel(self.master_frame, text='',image=self.img)
                            
                            self.lbl_img.grid(row=binary[0],column=binary[1])
                            self.lbl_img.bind('<Button-1>',lambda  e, a=i: self.openImage(e,a))
                        if len(list_chat[i][key_send_per])>4:
                            diff = len(list_chat[i][key_send_per]) -4 
                            self.lbl_diff = ctk.CTkLabel(self.lbl_img,text='+'+str(diff),font=('arial',18))
                            self.lbl_diff.grid(row=0,column=0,sticky='se')
                    else:
                        self.img = PIL.Image.open(list_chat[i][key_send_per][0])
                        self.img = ctk.CTkImage(light_image=self.img,size=(150,200))
                        self.lbl_img = ctk.CTkLabel(self.frame_text, text='',image=self.img)
                        self.lbl_img.grid(row=0,column=0,padx=10,pady=10)
                        self.lbl_img.bind('<Button-1>',lambda  e, a=i: self.openImage(e,a))
                else:
                    span=3
                    if list_chat[i]['R']==False:
                        self.lbl_text=ctk.CTkLabel(self.frame_text, text=list(list_chat[i].values())[0],font=('arial',20),wraplength=200,justify=LEFT)
                        self.lbl_text.grid(row=0,column=0,padx=10,pady=5,sticky='w')
                        span=1
                    else:
                        key1 = list(self.list_chat[self.index_chat][i].keys())[0]
                        rec_path=self.list_chat[self.index_chat][i][key1]
                        
                        freq,data=wavfile.read(rec_path)
                        
                        Exactduration_chat = len(data)/freq
                        
                        self.bt_play_chat = ctk.CTkButton(self.frame_text,text='|>',font=('arial',18,'bold'),width=30,fg_color=color,command=lambda a=i:self.bt_Play_chat_com(a))
                        self.bt_play_chat.grid(row=0,column=0,padx=5,pady=10)
                        
                        self.slider_rec_chat = ctk.CTkSlider(self.frame_text,button_color=color,command=lambda val, ind=i:self.slider_chat_com(val,ind))
                        self.slider_rec_chat.grid(row=0,column=1,sticky='we',padx=5,pady=10)
                        self.slider_rec_chat.set(0)
                        
                        self.lbl_time_chat = ctk.CTkLabel(self.frame_text,text='00:00|'+self.time_formate(int(np.ceil(Exactduration_chat))))
                        self.lbl_time_chat.grid(row=0,column=2,padx=5,pady=10)
                        
                        self.list_rec[i]=[self.bt_play_chat,self.slider_rec_chat,self.lbl_time_chat]
                    
                self.lower_frame = ctk.CTkFrame(self.frame_text,fg_color='transparent',corner_radius=20)
                self.lower_frame.grid(row=1,column=0,columnspan=span,pady=2,padx=7,sticky='nswe')
                
                self.lower_frame.grid_rowconfigure(0, weight=0)
                
                self.lower_frame.grid_columnconfigure(0, weight=0)
                
                self.lower_frame.grid_columnconfigure(1, weight=1)
                
                self.lbl_time = ctk.CTkLabel(self.lower_frame,text=self.list_chat[self.index_chat][i]['time'],font=('arial',11),text_color='#403F3F')
                self.lbl_time.grid(row=0,column=1,sticky=sticky_time,padx=5)
                
                if list(list_chat[i].keys())[0]=='M':
                    color_seen='red'
                    if list_chat[i]['seen']:
                        color_seen = '#1AA1BF'
                    self.lbl_seen = ctk.CTkLabel(self.lower_frame,text='.',text_color=color_seen)
                    self.lbl_seen.grid(row=0,column=0)
                
                
                self.list_frames.append(self.bsk_frame)
                
             
    def openImage(self,e,index):
        for widget in self.list_images:
            widget.grid_forget()
        self.list_images=[]
        self.frame_images.grid(row=0,column=0,rowspan=3,sticky='nswe')
        self.frame_images.grid_columnconfigure(0, weight=1)
        key_H_M = list(self.list_chat[self.index_chat][index].keys())[0]
        for ind in range(len(self.list_chat[self.index_chat][index][key_H_M])):
            self.img = PIL.Image.open(self.list_chat[self.index_chat][index][key_H_M][ind])
            self.img = ctk.CTkImage(light_image=self.img,size=(350,450))
            self.lbl_img = ctk.CTkLabel(self.frame_images, text='',image=self.img)
            self.lbl_img.grid(row=ind,column=0,pady=10)
            self.list_images.append(self.lbl_img)
        self.bt_exit = ctk.CTkButton(self.frame_images, text='X',width=50,command=self.bt_exit_image_com)
        self.bt_exit.grid(row=0,column=0,padx=10,pady=10,sticky='ne')
        self.list_images.append(self.bt_exit)
    def bt_exit_image_com(self):
        self.frame_images.grid_forget()
    def bt_Play_chat_com(self,index_rec):
        if self.playing==0:
            key1 = list(self.list_chat[self.index_chat][index_rec].keys())[0]
            rec_path=self.list_chat[self.index_chat][index_rec][key1]
            
            freq,data=wavfile.read(rec_path)
            
            self.Exactduration_chat = len(data)/freq
            
            if self.playing_chat==0:
                self.index_rec = index_rec
                self.stopped_chat=0
                self.list_rec[index_rec][0].configure(text='||')
                sd.play(data[int(self.list_rec[index_rec][1].get()*self.Exactduration_chat*freq):int(self.Exactduration_chat*freq)],freq)
                self.duration_chat = int(self.list_rec[index_rec][1].get()*self.Exactduration_chat)
                t1 = Thread(target=lambda a=index_rec:self.duration_func_chat(index_rec))
                t1.start()
                self.playing_chat=1
            elif self.playing_chat==1 and self.index_rec==index_rec:
                self.list_rec[index_rec][0].configure(state='disabled')
                self.list_rec[index_rec][1].configure(state='disabled')
                self.list_rec[index_rec][0].configure(text='|>')
                sd.stop()
                self.playing_chat=0
                self.stopped_chat=1
            elif self.playing_chat==1 and self.index_rec!=index_rec:
                self.list_rec[self.index_rec][0].configure(state='disabled')
                self.list_rec[self.index_rec][1].configure(state='disabled')
                self.list_rec[self.index_rec][0].configure(text='|>')
                sd.stop()
                self.stopped_chat=1
                
                
                
                while( self.list_rec[self.index_rec][0].cget('state')!='normal'):
                    pass
                
                self.index_rec = index_rec
                self.stopped_chat=0
                self.list_rec[index_rec][0].configure(text='||')
                sd.play(data[int(self.list_rec[index_rec][1].get()*self.Exactduration_chat*freq):int(self.Exactduration_chat*freq)],freq)
                self.duration_chat = int(self.list_rec[index_rec][1].get()*self.Exactduration_chat)
                t1 = Thread(target=lambda a=index_rec:self.duration_func_chat(index_rec))
                t1.start()
                self.playing_chat=1
        else:
            self.bt_play.configure(state='disabled')
            self.slider_rec.configure(state='disabled')
            self.bt_play.configure(text='|>')
            sd.stop()
            self.playing=0
            self.stopped=1
            
            while( self.bt_play.cget('state')!='normal'):
                pass
            
            self.bt_Play_chat_com(index_rec)
            
        
        
    def duration_func_chat(self,index_rec):
        while(self.duration_chat<self.Exactduration_chat and self.stopped_chat==0 and self.diff_chat==0): # 5.2 --> 5 6
            self.duration_chat+=1
            self.list_rec[index_rec][2].configure(text=self.time_formate(self.duration_chat)+'|'+self.time_formate(int(np.ceil(self.Exactduration_chat))))#01:10|2:00
            self.list_rec[index_rec][1].set(self.duration_chat/self.Exactduration_chat)
            time.sleep(1)
        if self.diff_chat==0:
            if self.stopped_chat==0:
                self.list_rec[index_rec][0].configure(text='|>')
                self.list_rec[index_rec][1].set(0)
                self.duration_chat=0
                self.playing_chat=0
                self.list_rec[index_rec][2].configure(text='00:00|'+self.time_formate(int(np.ceil(self.Exactduration_chat))))
            else:
                self.stopped_chat=0
                
                self.list_rec[index_rec][0].configure(state='normal')
                self.list_rec[index_rec][1].configure(state='normal')
            
        else:
            self.diff_chat=0
    def slider_chat_com(self,value,index_rec):
        self.bt_Play_chat_com(index_rec)
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__=='__main__':
    app=App()
    app.mainloop()






















