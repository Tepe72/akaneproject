from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button


class ScreenOne(Screen):
    def __init__(self, **kwargs):
        super(ScreenOne, self).__init__(**kwargs)
        self.label = Label(text="画面1")
        self.next_button = Button(text="次へ", on_press=self.switch_screen)

        self.add_widget(self.label)
        self.add_widget(self.next_button)

    def switch_screen(self):
        self.manager.current = 'screen_two'


class ScreenTwo(Screen):
    def __init__(self, **kwargs):
        super(ScreenTwo, self).__init__(**kwargs)
        self.label = Label(text="画面2")
        self.next_button = Button(text="戻る", on_press=self.switch_screen)

        self.add_widget(self.label)
        self.add_widget(self.next_button)

    def switch_screen(self):
        self.manager.current = 'screen_one'


class Main1App(App):
    pass

    def build(self):
        sm = ScreenManager()
        sm.add_widget(ScreenOne(name='screen_one'))
        sm.add_widget(ScreenTwo(name='screen_two'))
        return sm


# App().run()


if __name__ == '__main__':
    Main1App().run()
