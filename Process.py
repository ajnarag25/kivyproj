kivy = """
ScreenManager:
    Main:
    #-------------#
    Mountainbike:
    Size:
    Fork:
    Rwsan:
    Wheelset1:
    Hub:
    Crankset:
    Sws:
    Handlebar:
    Groupset1:
    Result1:
    #-------------#
    Roadbike:
    Wheelset2:
    Groupset2:
    Dropbar:
    Seatpost:
    Result2:


<Main>
    name: "gomain"
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Bike Builder Parts with Prices"
            orientation: "vertical"
        MDLabel:
            text: "" 
            
        MDBottomNavigation:
    
            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'Account'
                icon: 'account-badge'
    
                MDLabel:
                    text: 'Welcome!'
                    halign: 'center'
    
            MDBottomNavigationItem:
                name: 'screen 3'
                text: 'About'
                icon: 'account-circle'
    
                MDLabel:
                    text: 'Here you can now select your desire parts for your future bike and you can see also the total prices of the parts'
                    halign: 'center'
                    
    MDLabel:
        text: "Please Select your Bike" 
        halign: "center"
        pos_hint: {'center_y': 0.6}
        theme_text_color: "Secondary"      
    MDRectangleFlatButton:
        text: "Mountain Bike"
        pos_hint: {'center_x':0.3, 'center_y':0.45}
        on_press: root.manager.current = "mtb"                     
            
    MDRectangleFlatButton:
        text: "Road Bike"
        pos_hint: {'center_x':0.7, 'center_y':0.45}
        on_press: root.manager.current = "rb"


<Mountainbike>
    name: "mtb"
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Mountain Bike Parts"
            orientation: "vertical"
        MDLabel:
            text: "" 
    MDLabel:
        text: "Frame Mtb" 
        halign: "center"
        pos_hint: {'center_y': 0.8} 
        theme_text_color: "Secondary"     
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {'center_x':0.3, 'center_y':0.1}
        on_press: root.manager.current = "gomain"  
        
    MDRectangleFlatButton:
        text: "Next"
        pos_hint: {'center_x':0.7, 'center_y':0.1}
        on_press: root.manager.current = "sz"
        
    MDCard:
        size_hint: None, None
        size: "300dp", "320dp"
        pos_hint: {"center_x": .5, "center_y": .5}
            
        GridLayout:
            cols:2
            MDLabel:
                text: "Foxter"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check1(self, self.active, "Foxter P2,500", 2500)
                    
            MDLabel:
                text: "Trinx"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check1(self, self.active, "Trinx P2,500", 2500)
                        
            MDLabel:
                text: "Mountainpeak"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check1(self, self.active, "Mountainpeak P5,000", 5000)
    MDLabel:
        id: txt1
        text: ""
        halign: "center"
        pos_hint: {"center_y": .2}
        theme_text_color: "Secondary"                
<Size>
    name: "sz"
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Mountain Bike Parts"
            orientation: "vertical"
        MDLabel:
            text: "" 
    MDLabel:
        text: "Please Select your Frame Size" 
        halign: "center"
        pos_hint: {'center_y': 0.8} 
        theme_text_color: "Secondary"     
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {'center_x':0.3, 'center_y':0.1}
        on_press: root.manager.current = "mtb"  
        
    MDRectangleFlatButton:
        text: "Next"
        pos_hint: {'center_x':0.7, 'center_y':0.1}
        on_press: root.manager.current = "frk"
        
    MDCard:
        size_hint: None, None
        size: "300dp", "320dp"
        pos_hint: {"center_x": .5, "center_y": .5}
            
        GridLayout:
            cols:2
            MDLabel:
                text: "26er"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check2(self, self.active, "26er Free", 0)
                    
            MDLabel:
                text: "27.5"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check2(self, self.active, "27.5 (+P700 - Frame Price)", 700)
                        
            MDLabel:
                text: "29er"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check2(self, self.active, "29er (+P1,500 - Frame Price)", 1500)
    MDLabel:
        id: txt2
        text: ""
        halign: "center"
        pos_hint: {"center_y": .2}
        theme_text_color: "Secondary"   
        
<Fork>
    name: "frk"
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Mountain Bike Parts"
            orientation: "vertical"
        MDLabel:
            text: "" 
    MDLabel:
        text: "Fork" 
        halign: "center"
        pos_hint: {'center_y': 0.8} 
        theme_text_color: "Secondary"     
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {'center_x':0.3, 'center_y':0.1}
        on_press: root.manager.current = "sz"  
        
    MDRectangleFlatButton:
        text: "Next"
        pos_hint: {'center_x':0.7, 'center_y':0.1}
        on_press: root.manager.current = "rim"
        
    MDCard:
        size_hint: None, None
        size: "300dp", "320dp"
        pos_hint: {"center_x": .5, "center_y": .5}
            
        GridLayout:
            cols:2
            MDLabel:
                text: "Rigid"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check3(self, self.active, "Rigid P3,000", 3000)
                    
            MDLabel:
                text: "Suspension Fork (Coil)"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check3(self, self.active, "Suspension fork (coil) P2,000", 2000)
                        
            MDLabel:
                text: "Suspension Fork (Air)"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check3(self, self.active, "Suspension fork (air) P4,000", 4000)
    MDLabel:
        id: txt3
        text: ""
        halign: "center"
        pos_hint: {"center_y": .2}
        theme_text_color: "Secondary"    
        
<Rwsan>
    name: "rim"
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Mountain Bike Parts"
            orientation: "vertical"
        MDLabel:
            text: "" 
    MDLabel:
        text: "Rim with spokes and nipples" 
        halign: "center"
        pos_hint: {'center_y': 0.8} 
        theme_text_color: "Secondary"     
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {'center_x':0.3, 'center_y':0.1}
        on_press: root.manager.current = "frk"  
        
    MDRectangleFlatButton:
        text: "Next"
        pos_hint: {'center_x':0.7, 'center_y':0.1}
        on_press: root.manager.current = "ws1"
        
    MDCard:
        size_hint: None, None
        size: "300dp", "320dp"
        pos_hint: {"center_x": .5, "center_y": .5}
            
        GridLayout:
            cols:2
            MDLabel:
                text: "Mavic"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check4(self, self.active, "Mavic P1,600", 1600)
                    
            MDLabel:
                text: "Easton"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check4(self, self.active, "Easton P2,200", 2200)
                        
            MDLabel:
                text: "Kore"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check4(self, self.active, "Kore P1,400", 1400)
    MDLabel:
        id: txt4
        text: ""
        halign: "center"
        pos_hint: {"center_y": .2}
        theme_text_color: "Secondary"     
        
<Wheelset1>
    name: "ws1"
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Mountain Bike Parts"
            orientation: "vertical"
        MDLabel:
            text: "" 
    MDLabel:
        text: "Wheel Set" 
        halign: "center"
        pos_hint: {'center_y': 0.8} 
        theme_text_color: "Secondary"     
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {'center_x':0.3, 'center_y':0.1}
        on_press: root.manager.current = "rim"  
        
    MDRectangleFlatButton:
        text: "Next"
        pos_hint: {'center_x':0.7, 'center_y':0.1}
        on_press: root.manager.current = "hb"
        
    MDCard:
        size_hint: None, None
        size: "300dp", "320dp"
        pos_hint: {"center_x": .5, "center_y": .5}
            
        GridLayout:
            cols:2
            MDLabel:
                text: "Maxxis"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check5(self, self.active, "Maxxis P1,800", 1800)
                    
            MDLabel:
                text: "Compass"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check5(self, self.active, "Compass P1,500", 1500)
                        
            MDLabel:
                text: "Kenda"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check5(self, self.active, "Kenda P1,000", 1000)
    MDLabel:
        id: txt5
        text: ""
        halign: "center"
        pos_hint: {"center_y": .2}
        theme_text_color: "Secondary" 
<Hub>
    name: "hb"
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Mountain Bike Parts"
            orientation: "vertical"
        MDLabel:
            text: "" 
    MDLabel:
        text: "Hubs" 
        halign: "center"
        pos_hint: {'center_y': 0.8} 
        theme_text_color: "Secondary"     
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {'center_x':0.3, 'center_y':0.1}
        on_press: root.manager.current = "ws1"  
        
    MDRectangleFlatButton:
        text: "Next"
        pos_hint: {'center_x':0.7, 'center_y':0.1}
        on_press: root.manager.current = "cs"
        
    MDCard:
        size_hint: None, None
        size: "300dp", "320dp"
        pos_hint: {"center_x": .5, "center_y": .5}
            
        GridLayout:
            cols:2
            MDLabel:
                text: "2 Pawls"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check6(self, self.active, "2 Pawls P1,000", 1000)
                    
            MDLabel:
                text: "3 Pawls"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check6(self, self.active, "3 Pawls P2,000", 2000)
                        
            MDLabel:
                text: "6 Pawls"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check6(self, self.active, "6 Pawls P4,000", 4000)
                
            MDLabel:
                text: "Ratchet"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check6(self, self.active, "Ratchet P4,500", 4500)
    MDLabel:
        id: txt6
        text: ""
        halign: "center"
        pos_hint: {"center_y": .2}
        theme_text_color: "Secondary" 
        
<Crankset>
    name: "cs"
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Mountain Bike Parts"
            orientation: "vertical"
        MDLabel:
            text: "" 
    MDLabel:
        text: "Crank Set" 
        halign: "center"
        pos_hint: {'center_y': 0.8} 
        theme_text_color: "Secondary"     
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {'center_x':0.3, 'center_y':0.1}
        on_press: root.manager.current = "hb"  
        
    MDRectangleFlatButton:
        text: "Next"
        pos_hint: {'center_x':0.7, 'center_y':0.1}
        on_press: root.manager.current = "saddle"
        
    MDCard:
        size_hint: None, None
        size: "300dp", "320dp"
        pos_hint: {"center_x": .5, "center_y": .5}
            
        GridLayout:
            cols:2
            MDLabel:
                text: "Shimano Mt300"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check7(self, self.active, "Shimano Mt300 P1,300", 1300)
                    
            MDLabel:
                text: "Weapon Storm (1by)"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check7(self, self.active, "Weapon Storm (1by) P1,800", 1800)
                        
            MDLabel:
                text: "Sagmit Edison 10 (1by)"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check7(self, self.active, "Sagmit Edison 10 (1by) P2,100", 2100)
                
    MDLabel:
        id: txt7
        text: ""
        halign: "center"
        pos_hint: {"center_y": .2}
        theme_text_color: "Secondary" 
        
<Sws>
    name: "saddle"
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Mountain Bike Parts"
            orientation: "vertical"
        MDLabel:
            text: "" 
    MDLabel:
        text: "Seatpost with Saddle" 
        halign: "center"
        pos_hint: {'center_y': 0.8} 
        theme_text_color: "Secondary"     
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {'center_x':0.3, 'center_y':0.1}
        on_press: root.manager.current = "cs"  
        
    MDRectangleFlatButton:
        text: "Next"
        pos_hint: {'center_x':0.7, 'center_y':0.1}
        on_press: root.manager.current = "handle"
        
    MDCard:
        size_hint: None, None
        size: "300dp", "320dp"
        pos_hint: {"center_x": .5, "center_y": .5}
            
        GridLayout:
            cols:2
            MDLabel:
                text: "Truvativ and stock saddle"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check8(self, self.active, "Truvativ and stock saddle P600", 600)
                    
            MDLabel:
                text: "Wake and stock saddle"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check8(self, self.active, "Wake and stock saddle P650", 650)
                        
            MDLabel:
                text: "Sagmit and stock saddle"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check8(self, self.active, "Sagmit and stock saddle P800", 800)
                
    MDLabel:
        id: txt8
        text: ""
        halign: "center"
        pos_hint: {"center_y": .2}
        theme_text_color: "Secondary" 
        
<Handlebar>
    name: "handle"
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Mountain Bike Parts"
            orientation: "vertical"
        MDLabel:
            text: "" 
    MDLabel:
        text: "Handle Bar" 
        halign: "center"
        pos_hint: {'center_y': 0.8} 
        theme_text_color: "Secondary"     
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {'center_x':0.3, 'center_y':0.1}
        on_press: root.manager.current = "saddle"  
        
    MDRectangleFlatButton:
        text: "Next"
        pos_hint: {'center_x':0.7, 'center_y':0.1}
        on_press: root.manager.current = "gs1"
        
    MDCard:
        size_hint: None, None
        size: "300dp", "320dp"
        pos_hint: {"center_x": .5, "center_y": .5}
            
        GridLayout:
            cols:2
            MDLabel:
                text: "Mountainpeak 800mm"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check9(self, self.active, "Mountainpeak 800mm P700", 700)
                    
            MDLabel:
                text: "Sagmit 800mm"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check9(self, self.active, "Sagmit 800mm P700", 700)
                        
            MDLabel:
                text: "Truvativ 800mm"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check9(self, self.active, "Truvativ 800mm P450", 450)
                
    MDLabel:
        id: txt9
        text: ""
        halign: "center"
        pos_hint: {"center_y": .2}
        theme_text_color: "Secondary"       

<Groupset1>
    name: "gs1"
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Mountain Bike Parts"
            orientation: "vertical"
        MDLabel:
            text: "" 
    MDLabel:
        text: "Group Set" 
        halign: "center"
        pos_hint: {'center_y': 0.8} 
        theme_text_color: "Secondary"     
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {'center_x':0.3, 'center_y':0.1}
        on_press: root.manager.current = "handle"  
        
    MDRectangleFlatButton:
        text: "Next"
        pos_hint: {'center_x':0.7, 'center_y':0.1}
        on_press: root.manager.current = "rs1"
        
    MDCard:
        size_hint: None, None
        size: "300dp", "320dp"
        pos_hint: {"center_x": .5, "center_y": .5}
            
        GridLayout:
            cols:2
            MDLabel:
                text: "Shimano Tourney 8 speed"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check10(self, self.active, "Shimano Tourney 8 speed P1,500", 1500)
                    
            MDLabel:
                text: "Shimano Alivio 9 speed"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check10(self, self.active, "Shimano Alivio 9 speed P5,000", 5000)
                        
            MDLabel:
                text: "Shimano Deore 10 speed"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check10(self, self.active, "Shimano Deore 10 speed P10,000", 10000)
                
    MDLabel:
        id: txt10
        text: ""
        halign: "center"
        pos_hint: {"center_y": .2}
        theme_text_color: "Secondary"        

<Result1>
    id: ss
    name: "rs1"
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Mountain Bike Parts"
            orientation: "vertical"
        MDLabel:
            text: "" 
    MDLabel:
        text: "Result" 
        halign: "center"
        pos_hint: {'center_y': 0.8} 
        theme_text_color: "Secondary"  
           
    MDRectangleFlatButton:
        text: "Show Result"
        pos_hint: {'center_x':0.3, 'center_y':0.5}
        on_press: app.chk1()
        
    MDRectangleFlatButton:
        text: "Show Total Price"
        pos_hint: {'center_x':0.7, 'center_y':0.5}
        on_press: app.tp1()
        
    MDRectangleFlatButton:
        text: "Home"
        pos_hint: {'center_x':0.5, 'center_y':0.3}
        on_press: root.manager.current = "gomain" 
       
        
<Roadbike>
    name: "rb"
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Road Bike Parts"
            orientation: "vertical"
        MDLabel:
            text: "" 
    MDLabel:
        text: "Frame Rb" 
        halign: "center"
        pos_hint: {'center_y': 0.8} 
        theme_text_color: "Secondary"     
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {'center_x':0.3, 'center_y':0.1}
        on_press: root.manager.current = "gomain"  
        
    MDRectangleFlatButton:
        text: "Next"
        pos_hint: {'center_x':0.7, 'center_y':0.1}
        on_press: root.manager.current = "ws2"
        
    MDCard:
        size_hint: None, None
        size: "300dp", "320dp"
        pos_hint: {"center_x": .5, "center_y": .5}
            
        GridLayout:
            cols:2
            MDLabel:
                text: "Foxter Carrera"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check11(self, self.active, "Foxter Carrera P5,000", 5000)
                    
            MDLabel:
                text: "Sunpeed Triton"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check11(self, self.active, "Sunpeed Triton P4,000", 4000)
                        
            MDLabel:
                text: "Giant Defy"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check11(self, self.active, "Giant Defy P10,000", 10000)
                
    MDLabel:
        id: txt11
        text: ""
        halign: "center"
        pos_hint: {"center_y": .2}
        theme_text_color: "Secondary"   
          
<Wheelset2>
    name: "ws2"
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Road Bike Parts"
            orientation: "vertical"
        MDLabel:
            text: "" 
    MDLabel:
        text: "Wheel Set" 
        halign: "center"
        pos_hint: {'center_y': 0.8} 
        theme_text_color: "Secondary"     
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {'center_x':0.3, 'center_y':0.1}
        on_press: root.manager.current = "rb"  
        
    MDRectangleFlatButton:
        text: "Next"
        pos_hint: {'center_x':0.7, 'center_y':0.1}
        on_press: root.manager.current = "gs2"
        
    MDCard:
        size_hint: None, None
        size: "300dp", "320dp"
        pos_hint: {"center_x": .5, "center_y": .5}
            
        GridLayout:
            cols:2
            MDLabel:
                text: "Magic Cosmic"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check12(self, self.active, "Magic Cosmic P6,000", 6000)
                    
            MDLabel:
                text: "Ritchey"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check12(self, self.active, "Ritchey P4,000", 4000)
                        
            MDLabel:
                text: "Giant scr"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check12(self, self.active, "Giant scr P8,000", 8000)
                
    MDLabel:
        id: txt12
        text: ""
        halign: "center"
        pos_hint: {"center_y": .2}
        theme_text_color: "Secondary"   
          
<Groupset2>
    name: "gs2"
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Road Bike Parts"
            orientation: "vertical"
        MDLabel:
            text: "" 
    MDLabel:
        text: "Group Set" 
        halign: "center"
        pos_hint: {'center_y': 0.8} 
        theme_text_color: "Secondary"     
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {'center_x':0.3, 'center_y':0.1}
        on_press: root.manager.current = "ws2"  
        
    MDRectangleFlatButton:
        text: "Next"
        pos_hint: {'center_x':0.7, 'center_y':0.1}
        on_press: root.manager.current = "db"
        
    MDCard:
        size_hint: None, None
        size: "300dp", "320dp"
        pos_hint: {"center_x": .5, "center_y": .5}
            
        GridLayout:
            cols:2
            MDLabel:
                text: "Shimano Tourney sti 7 speed"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check13(self, self.active, "Shimano Tourney sti 7 speed P2,200", 2200)
                    
            MDLabel:
                text: "Shimano Claris sti 8 speed"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check13(self, self.active, "Shimano Claris sti 8 speed P8,000", 8000)
                        
            MDLabel:
                text: "Shimano Sora sti 9 speed"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check13(self, self.active, "Shimano Sora sti 9 speed P10,000", 10000)
            
            MDLabel:
                text: "Shimano Tiagra sti 10 speed"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check13(self, self.active, "Shimano Tiagra sti 10 speed P16,000", 16000)
                
    MDLabel:
        id: txt13
        text: ""
        halign: "center"
        pos_hint: {"center_y": .2}
        theme_text_color: "Secondary"   
        
<Dropbar>
    name: "db"
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Road Bike Parts"
            orientation: "vertical"
        MDLabel:
            text: "" 
    MDLabel:
        text: "Drop Bar" 
        halign: "center"
        pos_hint: {'center_y': 0.8} 
        theme_text_color: "Secondary"     
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {'center_x':0.3, 'center_y':0.1}
        on_press: root.manager.current = "gs2"  
        
    MDRectangleFlatButton:
        text: "Next"
        pos_hint: {'center_x':0.7, 'center_y':0.1}
        on_press: root.manager.current = "sp"
        
    MDCard:
        size_hint: None, None
        size: "300dp", "320dp"
        pos_hint: {"center_x": .5, "center_y": .5}
            
        GridLayout:
            cols:2
            MDLabel:
                text: "Truvativ"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check14(self, self.active, "Truvativ P600", 600)
                    
            MDLabel:
                text: "Sagmit"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check14(self, self.active, "Sagmit P1,000", 1000)
                        
            MDLabel:
                text: "Ec90"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check14(self, self.active, "Ec90 P1,200", 1200)
            
    MDLabel:
        id: txt14
        text: ""
        halign: "center"
        pos_hint: {"center_y": .2}
        theme_text_color: "Secondary"   
        
<Seatpost>
    name: "sp"
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Road Bike Parts"
            orientation: "vertical"
        MDLabel:
            text: "" 
    MDLabel:
        text: "Seatpost" 
        halign: "center"
        pos_hint: {'center_y': 0.8} 
        theme_text_color: "Secondary"     
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {'center_x':0.3, 'center_y':0.1}
        on_press: root.manager.current = "db"  
        
    MDRectangleFlatButton:
        text: "Next"
        pos_hint: {'center_x':0.7, 'center_y':0.1}
        on_press: root.manager.current = "rs2"
        
    MDCard:
        size_hint: None, None
        size: "300dp", "320dp"
        pos_hint: {"center_x": .5, "center_y": .5}
            
        GridLayout:
            cols:2
            MDLabel:
                text: "Ec90 and stock saddle"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check15(self, self.active, "Ec90 and stock saddle P1,300", 1300)
                    
            MDLabel:
                text: "Toseek and stock saddle"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check15(self, self.active, "Toseek and stock saddle P1,000", 1000)
                        
            MDLabel:
                text: "S-Works and stock saddle"
                halign: "center"
                theme_text_color: "Secondary"
            CheckBox:
                group: "frame"
                on_active: root.check15(self, self.active, "S-Works and stock saddle P2,000", 2000)
            
    MDLabel:
        id: txt15
        text: ""
        halign: "center"
        pos_hint: {"center_y": .2}
        theme_text_color: "Secondary"   
        
<Result2>
    name: "rs2"
    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "Road Bike Parts"
            orientation: "vertical"
        MDLabel:
            text: "" 
    MDLabel:
        text: "Result for RB" 
        halign: "center"
        pos_hint: {'center_y': 0.8} 
        theme_text_color: "Secondary"
            
             
    MDRectangleFlatButton:
        text: "Show Result"
        pos_hint: {'center_x':0.3, 'center_y':0.5}
        on_press: app.chk2()
        
    MDRectangleFlatButton:
        text: "Show Total Price"
        pos_hint: {'center_x':0.7, 'center_y':0.5}
        on_press: app.tp2()
        
    MDRectangleFlatButton:
        text: "Home"
        pos_hint: {'center_x':0.5, 'center_y':0.3}
        on_press: root.manager.current = "gomain" 
       
"""