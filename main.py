from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import SlideTransition
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
import random

Builder.load_string("""
<HomeScreen>: 
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Во что хотите поиграть в Декодирование или в числа'
            font_size: 30
            color: .5,.8,.4,1
        Button:
            text: 'Числа'
            font_size: 30
            color: .5,.8,.4,1
            on_press: root.manager.current = 'add'
        Label:
            
        Button:
            text: 'Декодирование'
            color: .5,.8,.4,1
            font_size: 30
            on_press: root.manager.current = 'ad'
        Label:
        Label:

<GomeScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: one
            text: ''
            font_size: 30
            color: .5,.8,.4,1
        TextInput:
            id: two
            text: ''
            font_size: 30
            multiline: False

        Label:
        Label:
            id: three
            text: ''
            font_size: 30
            color: .5,.8,.4,1
        Label:
        Label:
        Button:
            id: fory
            text: 'Нажми меня что бы начать'
            on_press: root.gor()
        Label:
        Label:
        Button:
            text: 'Выйти в главное меню.'
            on_press: 
                root.manager.transition.direction = 'right'
                root.manager.current = 'HOME'
        Label:
        Label:
        Label:

<UomeScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: one
            text: ''
            font_size: 30
            color: .5,.8,.4,1
        TextInput:
            id: two
            text: ''
            font_size: 30
            multiline: False

        Label:
        Label:
            id: three
            text: ''
            font_size: 30
            color: .5,.8,.4,1
        Label:
        Label:
            id: you
            text: ''
            font_size: 30
            color: .5,.8,.4,1
        Button:
            id: fory
            text: 'Нажми меня что бы начать'
            on_press: root.gor()
        Label:
        Label:
        Button:
            text: 'Выйти в главное меню.'
            on_press: 
                root.manager.transition.direction = 'right'
                root.manager.current = 'HOME'
        Label:
        Label:
        Label:


""")

class HomeScreen(Screen):
    pass

I = -1
G = -1
class GomeScreen(Screen):

    def gor(self):
        global I
        I += 1
        if I == 0:
            self.ids['fory'].text = 'Проверить / Далее'
            self.ids['one'].text = '5 * 4 = '

        if I == 1:
            self.ids['one'].text = '20 * 9 = '
            if self.ids.two.text == '20':
                self.ids['three'].text = "Молодец"
        if I == 2:
            self.ids['one'].text = '10 * 90 = '
            if self.ids.two.text == '180':
                self.ids['three'].text = "Великолепно"
        if I == 3 :
            self.ids['one'].text = ' 85 * 90 = '
            if self.ids.two.text != '900':
                self.ids['three'].color = 1, 0, 0, 1
                self.ids['three'].text = "Ошибочка(. Но нечего сташного продожай"
        if I == 4:
            if self.ids.two.text != '7650':
                self.ids['three'].color = 1, 0, 0, 1
                self.ids['three'].text = "Неувязочка получилась. Подумай над этим"

class UomeScreen(Screen):
    def gor(self):
        global G
        G += 1
        if G == 0:
            self.ids['fory'].text = 'Проверить / Далее'
            self.ids['one'].text = 'Йе мйхезцчзшкч цереч Ыкмехб'
            self.ids['you'].text = 'закодировано на 5 символов'
        if G == 1:
            self.ids['one'].text = 'Шйцус Ючт!!'
            self.ids['you'].text = 'закодировано на 9 символов'
            if self.ids.two.text == 'Да здравствует салат Цезарь':
                self.ids['three'].text = "Умничка"
        if G == 2:
            if self.ids.two.text != 'Панки Хой!!':
                self.ids['three'].color = 1, 0, 0, 1
                self.ids['three'].text = "Ну что же ты так. Правельный ответ: Панки Хой!!"

class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='HOME'))
        self.add=GomeScreen(name='add')
        self.ad=UomeScreen(name='ad')
        sm.add_widget(self.add)
        sm.add_widget(self.ad)
        return sm

MyApp().run()