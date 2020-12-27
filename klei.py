import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.image import Image
from kivy.config import Config

import os.path




class Kleiapp(App):
    def build(self):


        Config.set('graphics', 'width', 800)
        Config.set('graphics', 'height', 600)
        Config.write()

        main = FloatLayout(
            size = (800, 600)
        )

        main.add_widget(Image(
            source = 'bg.jpg',
            size = (800, 600),
            pos= (0,0)
        ))

        main.add_widget(FileChooserIconView(
            pos = (0, 300),
            rootpath= os.path.expanduser("~")+'\\desktop',
            size_hint = (1, 0.5), 
            filters = ['*.txt']
        ))
        main.add_widget(Button(
            text = 'load first file',
            size_hint = (.2, .1),
            pos = (100, 150),
            on_press = self.l1f
        ))
        main.add_widget(Button(
            text = 'load secund file',
            size_hint = (.2, .1),
            pos = (500, 150),
            on_press = self.l2f

        ))

        main.add_widget(Button(
            text = 'Klei!',
            size_hint = (.2, .1),
            pos = (300, 60),
            on_press = self.klei
        ))
        return(main)

    def l1f(self, instance):
        firstf1le = self.root.children[3].selection
        self.f1 = firstf1le[0]

    def l2f(self, instance):
        secf1le = self.root.children[3].selection
        self.f2 = secf1le[0]

    def klei(self, instance):
        f1 = open(self.f1, 'r')
        f2 = open(self.f2, 'r')
        result = open(os.path.expanduser("~")+'\\desktop\\result.txt', 'w')
        t1 = f1.read()
        t2 = f2.read()
        f1.close()
        f2.close()
        result.write(t1+'\n'+t2)
        result.close
Kleiapp().run()
