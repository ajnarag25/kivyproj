from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.button import MDFlatButton
from Process import kivy

Glist = ['1','2','3','4','5','6','7','8','9','10']
Vlist = ['1','2','3','4','5','6','7','8','9','10']

Rlist = ['1','2','3','4','5']
Blist = ['1','2','3','4','5']

class Item(OneLineIconListItem):
    divider = None

class MobApp(MDApp):
    dial1 = None
    dial2 = None
    dial3 = None
    dial4 = None
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Teal"
        run = Builder.load_string(kivy)
        screen.add_widget(run)
        return screen

    def chk1(self):
        p1 = Glist[0]
        p2 = Glist[1]
        p3 = Glist[2]
        p4 = Glist[3]
        p5 = Glist[4]
        p6 = Glist[5]
        p7 = Glist[6]
        p8 = Glist[7]
        p9 = Glist[8]
        p10 = Glist[9]
        if not self.dial1:
            self.dial1 = MDDialog(title="Your Items are:",
                            size_hint=(0.7,1),
                            type = "simple",
                            items=[
                                Item(text= p1),
                                Item(text= p2),
                                Item(text= p3),
                                Item(text= p4),
                                Item(text= p5),
                                Item(text= p6),
                                Item(text= p7),
                                Item(text= p8),
                                Item(text= p9),
                                Item(text= p10),

                            ],
                            buttons=[
                                    MDFlatButton(
                                        text="OK", text_color=self.theme_cls.primary_color, on_release = self.dis1
                                    ),
                            ],
                        )
        print(Glist[0])
        print(Glist[1])
        print(Glist[2])
        print(Glist[3])
        print(Glist[4])
        print(Glist[5])
        print(Glist[6])
        print(Glist[7])
        print(Glist[8])
        print(Glist[9])

        self.dial1.open()

    def dis1(self,obj):
        self.dial1.dismiss()

    def tp1(self):
        v1 = Vlist[0]
        v2 = Vlist[1]
        v3 = Vlist[2]
        v4 = Vlist[3]
        v5 = Vlist[4]
        v6 = Vlist[5]
        v7 = Vlist[6]
        v8 = Vlist[7]
        v9 = Vlist[8]
        v10 = Vlist[9]

        total = v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8 + v9 + v10
        print(total)
        a1 = "P" + str(total)
        if not self.dial2:
            self.dial2 = MDDialog(title="Your Total Price:",
                            size_hint=(0.7, 1),
                            text = a1,
                            buttons=[
                                MDFlatButton(
                                    text="OK", text_color=self.theme_cls.primary_color,
                                    on_release=self.dis2
                                )
                            ],
                            )

        self.dial2.open()

    def dis2(self,obj):
        self.dial2.dismiss()

    def chk2(self):
        p1 = Rlist[0]
        p2 = Rlist[1]
        p3 = Rlist[2]
        p4 = Rlist[3]
        p5 = Rlist[4]
        if not self.dial3:
            self.dial3 = MDDialog(title="Your Items are:",
                                  size_hint=(0.7, 1),
                                  type="simple",
                                  items=[
                                      Item(text=p1),
                                      Item(text=p2),
                                      Item(text=p3),
                                      Item(text=p4),
                                      Item(text=p5),

                                  ],
                                  buttons=[
                                      MDFlatButton(
                                          text="OK", text_color=self.theme_cls.primary_color, on_release=self.dis3
                                      ),
                                  ],
                                  )

        print(Rlist[0])
        print(Rlist[1])
        print(Rlist[2])
        print(Rlist[3])
        print(Rlist[4])

        self.dial3.open()

    def dis3(self,obj):
        self.dial3.dismiss()

    def tp2(self):
        v1 = Blist[0]
        v2 = Blist[1]
        v3 = Blist[2]
        v4 = Blist[3]
        v5 = Blist[4]

        total = v1 + v2 + v3 + v4 + v5
        print(total)
        a2 = "P" + str(total)
        if not self.dial4:
            self.dial4 = MDDialog(title="Your Total Price:",
                            size_hint=(0.7, 1),
                            text = a2,
                            buttons=[
                                MDFlatButton(
                                    text="OK", text_color=self.theme_cls.primary_color,
                                    on_release=self.dis4
                                )
                            ],
                            )
        self.dial4.open()

    def dis4(self, obj):
        self.dial4.dismiss()

class Main(Screen):
    pass

class Mountainbike(Screen):
    def check1(self, instance, value, p1, val1):
        a = 2500
        b = 2500
        c = 5000
        if value == True and val1 == a:
            self.ids.txt1.text = f'{p1}'
            Glist[0] = p1
            Vlist[0] = val1
            print(("You Selected:" + p1))
            print(Glist)
            print(Vlist)

        elif value == True and val1 == b:
            self.ids.txt1.text = f'{p1}'
            Glist[0] = p1
            Vlist[0] = val1
            print(("You Selected:" + p1))
            print(Glist)
            print(Vlist)

        elif value == True and val1 == c:
            self.ids.txt1.text = f'{p1}'
            Glist[0] = p1
            Vlist[0] = val1
            print(("You Selected:" + p1))
            print(Glist)
            print(Vlist)
        else:
            self.ids.txt1.text = "Please Select"

#MTB PARTS#
class Size(Screen):
    def check2(self, instance, value, p2, val2):
        a = 0
        b = 700
        c = 1500
        if value == True and val2 == a:
            self.ids.txt2.text = f'{p2}'
            Glist[1] = p2
            Vlist[1] = val2
            print("You Selected:"+p2)
            print(Glist)
            print(Vlist)

        elif value == True and val2 == b:
            self.ids.txt2.text = f'{p2}'
            Glist[1] = p2
            Vlist[1] = val2
            print("You Selected:"+p2)
            print(Glist)
            print(Vlist)

        elif value == True and val2 == c:
            self.ids.txt2.text = f'{p2}'
            Glist[1] = p2
            Vlist[1] = val2
            print("You Selected:"+p2)
            print(Glist)
            print(Vlist)

        else:
            self.ids.txt2.text = "Please Select"


class Fork(Screen):
    def check3(self, instance, value, p3, val3):
        a = 3000
        b = 2000
        c = 4000
        if value == True and val3 == a:
            self.ids.txt3.text = f'{p3}'
            Glist[2] = p3
            Vlist[2] = val3
            print(("You Selected:" + p3))
            print(Glist)
            print(Vlist)

        elif value == True and val3 == b:
            self.ids.txt3.text = f'{p3}'
            Glist[2] = p3
            Vlist[2] = val3
            print(("You Selected:" + p3))
            print(Glist)
            print(Vlist)

        elif value == True and val3 == c:
            self.ids.txt3.text = f'{p3}'
            Glist[2] = p3
            Vlist[2] = val3
            print(("You Selected:" + p3))
            print(Glist)
            print(Vlist)

        else:
            self.ids.txt3.text = "Please Select"

class Rwsan(Screen):
    def check4(self, instance, value, p4, val4):
        a = 1600
        b = 2200
        c = 1400
        if value == True and val4 == a:
            self.ids.txt4.text = f'{p4}'
            Glist[3] = p4
            Vlist[3] = val4
            print(("You Selected:" + p4))
            print(Glist)
            print(Vlist)

        elif value == True and val4 == b:
            self.ids.txt4.text = f'{p4}'
            Glist[3] = p4
            Vlist[3] = val4
            print(("You Selected:" + p4))
            print(Glist)
            print(Vlist)

        elif value == True and val4 == c:
            self.ids.txt4.text = f'{p4}'
            Glist[3] = p4
            Vlist[3] = val4
            print(("You Selected:" + p4))
            print(Glist)
            print(Vlist)
        else:
            self.ids.txt4.text = "Please Select"

class Wheelset1(Screen):
    def check5(self, instance, value, p5, val5):
        a = 1800
        b = 1500
        c = 1000
        if value == True and val5 == a:
            self.ids.txt5.text = f'{p5}'
            Glist[4] = p5
            Vlist[4] = val5
            print(("You Selected:" + p5))
            print(Glist)
            print(Vlist)

        elif value == True and val5 == b:
            self.ids.txt5.text = f'{p5}'
            Glist[4] = p5
            Vlist[4] = val5
            print(("You Selected:" + p5))
            print(Glist)
            print(Vlist)

        elif value == True and val5 == c:
            self.ids.txt5.text = f'{p5}'
            Glist[4] = p5
            Vlist[4] = val5
            print(("You Selected:" + p5))
            print(Glist)
            print(Vlist)

        else:
            self.ids.txt5.text = "Please Select"

class Hub(Screen):
    def check6(self, instance, value, p6, val6):
        a = 1000
        b = 2000
        c = 4000
        d = 4500
        if value == True and val6 == a:
            self.ids.txt6.text = f'{p6}'
            Glist[5] = p6
            Vlist[5] = val6
            print(("You Selected:" + p6))
            print(Glist)
            print(Vlist)

        elif value == True and val6 == b:
            self.ids.txt6.text = f'{p6}'
            Glist[5] = p6
            Vlist[5] = val6
            print(("You Selected:" + p6))
            print(Glist)
            print(Vlist)

        elif value == True and val6 == c:
            self.ids.txt6.text = f'{p6}'
            Glist[5] = p6
            Vlist[5] = val6
            print(("You Selected:" + p6))
            print(Glist)
            print(Vlist)

        elif value == True and val6 == d:
            self.ids.txt6.text = f'{p6}'
            Glist[5] = p6
            Vlist[5] = val6
            print(("You Selected:" + p6))
            print(Glist)
            print(Vlist)

        else:
            self.ids.txt6.text = "Please Select"

class Crankset(Screen):
    def check7(self, instance, value, p7, val7):
        a = 1300
        b = 1800
        c = 2100
        if value == True and val7 == a:
            self.ids.txt7.text = f'{p7}'
            Glist[6] = p7
            Vlist[6] = val7
            print(("You Selected:" + p7))
            print(Glist)
            print(Vlist)

        elif value == True and val7 == b:
            self.ids.txt7.text = f'{p7}'
            Glist[6] = p7
            Vlist[6] = val7
            print(("You Selected:" + p7))
            print(Glist)
            print(Vlist)

        elif value == True and val7 == c:
            self.ids.txt7.text = f'{p7}'
            Glist[6] = p7
            Vlist[6] = val7
            print(("You Selected:" + p7))
            print(Glist)
            print(Vlist)

        else:
            self.ids.txt7.text = "Please Select"

class Sws(Screen):
    def check8(self, instance, value, p8, val8):
        a = 600
        b = 650
        c = 800
        if value == True and val8 == a:
            self.ids.txt8.text = f'{p8}'
            Glist[7] = p8
            Vlist[7] = val8
            print(("You Selected:" + p8))
            print(Glist)
            print(Vlist)

        elif value == True and val8 == b:
            self.ids.txt8.text = f'{p8}'
            Glist[7] = p8
            Vlist[7] = val8
            print(("You Selected:" + p8))
            print(Glist)
            print(Vlist)

        elif value == True and val8 == c:
            self.ids.txt8.text = f'{p8}'
            Glist[7] = p8
            Vlist[7] = val8
            print(("You Selected:" + p8))
            print(Glist)
            print(Vlist)
        else:
            self.ids.txt8.text = "Please Select"

class Handlebar(Screen):
    def check9(self, instance, value, p9, val9):
        a = 700
        b = 700
        c = 450
        if value == True and val9 == a:
            self.ids.txt9.text = f'{p9}'
            Glist[8] = p9
            Vlist[8] = val9
            print(("You Selected:" + p9))
            print(Glist)
            print(Vlist)

        elif value == True and val9 == b:
            self.ids.txt9.text = f'{p9}'
            Glist[8] = p9
            Vlist[8] = val9
            print(("You Selected:" + p9))
            print(Glist)
            print(Vlist)

        elif value == True and val9 == c:
            self.ids.txt9.text = f'{p9}'
            Glist[8] = p9
            Vlist[8] = val9
            print(("You Selected:" + p9))
            print(Glist)
            print(Vlist)
        else:
            self.ids.txt9.text = "Please Select"

class Groupset1(Screen):
    def check10(self, instance, value, p10, val10):
        a = 1500
        b = 5000
        c = 10000
        if value == True and val10 == a:
            self.ids.txt10.text = f'{p10}'
            Glist[9] = p10
            Vlist[9] = val10
            print(("You Selected:" + p10))
            print(Glist)
            print(Vlist)

        elif value == True and val10 == b:
            self.ids.txt10.text = f'{p10}'
            Glist[9] = p10
            Vlist[9] = val10
            print(("You Selected:" + p10))
            print(Glist)
            print(Vlist)

        elif value == True and val10 == c:
            self.ids.txt10.text = f'{p10}'
            Glist[9] = p10
            Vlist[9] = val10
            print(("You Selected:" + p10))
            print(Glist)
            print(Vlist)
        else:
            self.ids.txt10.text = "Please Select"

#MTB PARTS#

class Result1(Screen):
    pass


class Roadbike(Screen):
    def check11(self, instance, value, p11, val1):
        a = 5000
        b = 4000
        c = 10000
        if value == True and val1 == a:
            self.ids.txt11.text = f'{p11}'
            Rlist[0] = p11
            Blist[0] = val1
            print(("You Selected:" + p11))
            print(Rlist)
            print(Blist)

        elif value == True and val1 == b:
            self.ids.txt11.text = f'{p11}'
            Rlist[0] = p11
            Blist[0] = val1
            print(("You Selected:" + p11))
            print(Rlist)
            print(Blist)

        elif value == True and val1 == c:
            self.ids.txt11.text = f'{p11}'
            Rlist[0] = p11
            Blist[0] = val1
            print(("You Selected:" + p11))
            print(Rlist)
            print(Blist)

        else:
            self.ids.txt11.text = "Please Select"

#RB PARTS#
class Wheelset2(Screen):
    def check12(self, instance, value, p12, val2):
        a = 6000
        b = 4000
        c = 8000
        if value == True and val2 == a:
            self.ids.txt12.text = f'{p12}'
            Rlist[1] = p12
            Blist[1] = val2
            print(("You Selected:" + p12))
            print(Rlist)
            print(Blist)

        elif value == True and val2 == b:
            self.ids.txt12.text = f'{p12}'
            Rlist[1] = p12
            Blist[1] = val2
            print(("You Selected:" + p12))
            print(Rlist)
            print(Blist)

        elif value == True and val2 == c:
            self.ids.txt12.text = f'{p12}'
            Rlist[1] = p12
            Blist[1] = val2
            print(("You Selected:" + p12))
            print(Rlist)
            print(Blist)

        else:
            self.ids.txt12.text = "Please Select"

class Groupset2(Screen):
    def check13(self, instance, value, p13, val3):
        a = 2200
        b = 8000
        c = 10000
        d = 16000
        if value == True and val3 == a:
            self.ids.txt13.text = f'{p13}'
            Rlist[2] = p13
            Blist[2] = val3
            print(("You Selected:" + p13))
            print(Rlist)
            print(Blist)

        elif value == True and val3 == b:
            self.ids.txt13.text = f'{p13}'
            Rlist[2] = p13
            Blist[2] = val3
            print(("You Selected:" + p13))
            print(Rlist)
            print(Blist)

        elif value == True and val3 == c:
            self.ids.txt13.text = f'{p13}'
            Rlist[2] = p13
            Blist[2] = val3
            print(("You Selected:" + p13))
            print(Rlist)
            print(Blist)

        elif value == True and val3 == d:
            self.ids.txt13.text = f'{p13}'
            Rlist[2] = p13
            Blist[2] = val3
            print(("You Selected:" + p13))
            print(Rlist)
            print(Blist)

        else:
            self.ids.txt13.text = "Please Select"

class Dropbar(Screen):
    def check14(self, instance, value, p14, val4):
        a = 600
        b = 1000
        c = 1200
        if value == True and val4 == a:
            self.ids.txt14.text = f'{p14}'
            Rlist[3] = p14
            Blist[3] = val4
            print(("You Selected:" + p14))
            print(Rlist)
            print(Blist)

        elif value == True and val4 == b:
            self.ids.txt14.text = f'{p14}'
            Rlist[3] = p14
            Blist[3] = val4
            print(("You Selected:" + p14))
            print(Rlist)
            print(Blist)

        elif value == True and val4 == c:
            self.ids.txt14.text = f'{p14}'
            Rlist[3] = p14
            Blist[3] = val4
            print(("You Selected:" + p14))
            print(Rlist)
            print(Blist)

        else:
            self.ids.txt14.text = "Please Select"

class Seatpost(Screen):
    def check15(self, instance, value, p15, val5):
        a = 1300
        b = 1000
        c = 2000
        if value == True and val5 == a:
            self.ids.txt15.text = f'{p15}'
            Rlist[4] = p15
            Blist[4] = val5
            print(("You Selected:" + p15))
            print(Rlist)
            print(Blist)

        elif value == True and val5 == b:
            self.ids.txt15.text = f'{p15}'
            Rlist[4] = p15
            Blist[4] = val5
            print(("You Selected:" + p15))
            print(Rlist)
            print(Blist)

        elif value == True and val5 == c:
            self.ids.txt15.text = f'{p15}'
            Rlist[4] = p15
            Blist[4] = val5
            print(("You Selected:" + p15))
            print(Rlist)
            print(Blist)

        else:
            self.ids.txt15.text = "Please Select"
#RB PARTS#

class Result2(Screen):
    pass



go = ScreenManager()
go.add_widget(Main(name="gomain"))
#---------------------------------------#
go.add_widget(Mountainbike(name="mtb"))
go.add_widget(Size(name="sz"))
go.add_widget(Fork(name="frk"))
go.add_widget(Rwsan(name="rim"))
go.add_widget(Wheelset1(name="ws1"))
go.add_widget(Hub(name="hb"))
go.add_widget(Crankset(name="cs"))
go.add_widget(Sws(name="saddle"))
go.add_widget(Handlebar(name="handle"))
go.add_widget(Groupset1(name="gs1"))
go.add_widget(Result1(name="rs1"))
#------------------------------------------#
go.add_widget(Roadbike(name="rb"))
go.add_widget(Wheelset2(name="ws2"))
go.add_widget(Groupset2(name="gs2"))
go.add_widget(Dropbar(name="db"))
go.add_widget(Seatpost(name="sp"))
go.add_widget(Result2(name="rs2"))



MobApp().run()