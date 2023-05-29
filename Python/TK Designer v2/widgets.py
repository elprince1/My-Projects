from tkinter import LEFT,RIGHT,TOP,BOTTOM
widgets=['Button','Entry','Text','Radiobutton','Checkbutton','Canvas','Label','Listbox','Scrollbar','Combobox','Treeview','Frame']
widget_properties=[#botton
                   {
                    'text':'string',
                    'bg':'string',
                    'fg':'string',
                    'font family':'string',
                    'font size':'int',
                    'bd':'int',
                    #'command':'string',
                    'highlightcolor':'string',
                    'highlightbackground':'string',
                    'activebackground':'string',
                    'activeforeground':'string',
                    'image':'path',
                    'relief':['flat','groove','raised','ridge','solid','sunken']
                    },
                   #Entry
                   {
                    'bg':'string',
                    'fg':'string',
                    'font family':'string',
                    'font size':'int',
                    'bd':'int',
                    'highlightcolor':'string',
                    'highlightbackground':'string',
                    'show':'string',
                    'highlightthickness':'int'
                    },
                   #text
                   {
                    'bg':'string',
                    'fg':'string',
                    'font family':'string',
                    'font size':'int',
                    'bd':'int'
                    },
                   #radiobutton
                   {
                    'text':'string',
                    'bg':'string',
                    'fg':'string',
                    'font family':'string',
                    'font size':'int',
                    'highlightcolor':'string',
                    'highlightbackground':'string',
                    'activebackground':'string',
                    'activeforeground':'string'
                    },
                   #checkbutton
                   {
                    'text':'string',
                    'bg':'string',
                    'fg':'string',
                    'font family':'string',
                    'font size':'int',
                    'highlightcolor':'string',
                    'highlightbackground':'string',
                    'activebackground':'string',
                    'activeforeground':'string'
                    },
                   #canvas
                   {
                    'bg':'string',
                    'highlightthickness':'int'
                    },
                   #label
                   {
                    'text':'string',
                    'bg':'string',
                    'fg':'string',
                    'font family':'string',
                    'font size':'int',
                    'image':'path'
                    },
                   #listbox
                   {
                       'bg':'string',
                       'fg':'string',
                       'font family':'string',
                       'font size':'int',
                       'highlightcolor':'string',
                       'highlightbackground':'string',
                       'bd':'int'
                    },
                   #scrollbar
                   {
                    'orient':['vertical','horizontal']
                    },
                   #combobox
                   {
                    
                    },
                   #treeview
                   {
                    
                    },
                   #frame
                   {
                    'bg':'string'
                    }
                   ]
widget_properties_default=[
                    {
                    'text':'Button',
                    'bg':'#f0f0f0',
                    'fg':'black',
                    'font family':'arial',
                    'font size':13,
                    'bd':0,
                    #'command':'None',
                    'highlightcolor':'None',
                    'highlightbackground':'None',
                    'activebackground':'white',
                    'activeforeground':'black',
                    'image':'None',
                    'relief':'flat'
                    },
                   #Entry
                   {
                    'bg':'#f0f0f0',
                    'fg':'black',
                    'font family':'arial',
                    'font size':13,
                    'bd':0,
                    'highlightcolor':'None',
                    'highlightbackground':'None',
                    'show':'',
                    'highlightthickness':1
                    },
                   #text
                   {
                    'bg':'#f0f0f0',
                    'fg':'black',
                    'font family':'arial',
                    'font size':13,
                    'bd':0
                    },
                   #radiobutton
                   {
                    'text':'Radiobutton',
                    'bg':'#f0f0f0',
                    'fg':'black',
                    'font family':'arial',
                    'font size':13,
                    'highlightcolor':'None',
                    'highlightbackground':'None',
                    'activebackground':'None',
                    'activeforeground':'None'
                    },
                   #checkbutton
                   {
                    'text':'Checkbutton',
                    'bg':'#f0f0f0',
                    'fg':'black',
                    'font family':'arial',
                    'font size':13,
                    'highlightcolor':'None',
                    'highlightbackground':'None',
                    'activebackground':'None',
                    'activeforeground':'None'
                    },
                   #canvas
                   {
                    'bg':'#f0f0f0',
                    'highlightthickness':0
                    },
                   #label
                   {
                    'text':'Label',
                    'bg':'#f0f0f0',
                    'fg':'black',
                    'font family':'arial',
                    'font size':13,
                    'image':'None'
                    },
                   #listbox
                   {
                    'bg':'white',
                    'fg':'black',
                    'font family':'arial',
                    'font size':13,
                    'highlightcolor':'orange',
                    'highlightbackground':'black',
                    'bd':0
                    },
                   #scrollbar
                   {
                    'orient':'vertical'
                    },
                   #combobox
                   {
                    
                    },
                   #treeview
                   {
                    
                    },
                   #frame
                   {
                    'bg':'orange'
                    }
                    ]
widget_properties_pack={'side':[LEFT,RIGHT,TOP,BOTTOM],
                        'fill':['None','x','y','both'],
                        'expand':['true','false'],
                        'padx':'int',
                        'pady':'int'
                        }
widget_properties_pack_defaults={'side':LEFT,
                        'fill':'None',
                        'expand':'false',
                        'padx':10,
                        'pady':10
                        }
widget_properties_grid={
                        
                        }
widget_properties_grid_defaults={
                       
                        }
widget_properties_place={
                         'width':'int',
                         'height':'int',
                         'x':'int',
                         'y':'int',
                         }
widget_properties_place_defaults={
                                 'width':10,
                                 'height':10,
                                 'x':10,
                                 'y':10,
                                 }




win_properties={
                'id':'string',
                'pos_x':'int',
                'pos_y':'int',
                'width':'int',
                'height':'int',
                'bg':'string',
                'overrideredirect':[0,1],
                'topmost':[0,1],
                'title':'string',
                'icon':'path'
                }

win_properties_defaults={
                'id':'self',
                'pos_x':'center',
                'pos_y':'center',
                'width':1024,
                'height':720,
                'bg':'white',
                'overrideredirect':0,
                'topmost':0,
                'title':'tk',
                'icon':'None'
                }







