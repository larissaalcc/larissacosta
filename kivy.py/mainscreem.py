import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
import random


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        exit_button = Button(text = 'Fechar')
        layout.add_widget(exit_button)
        start_button = Button(text="Iniciar Jogo")
        start_button.bind(on_press=self.start_game)
        exit_button.bind(on_press = self.exit_game)
        layout.add_widget(Label(text="Bem-vindo ao Jogo de Adivinhação!"))
        layout.add_widget(start_button)
        self.add_widget(layout)

    def exit_game(self, instance):
        App.get_running_app().stop()


        App.get_running_app()

        App.get_running_app

        App.get
        
    def start_game(self, instance):
        self.manager.current = 'game'