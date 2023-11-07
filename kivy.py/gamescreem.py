import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
import random

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.secret_number = random.randint(1, 50)
        self.attempts = 0

        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text="Tente adivinhar o número (1-50):")
        self.input = TextInput(multiline=False)
        self.check_button = Button(text="Verificar")
        self.check_button.bind(on_press=self.check_guess)

        self.layout.add_widget(self.label)
        self.layout.add_widget(self.input)
        self.layout.add_widget(self.check_button)

        self.add_widget(self.layout)

    def check_guess(self, instance):
        guess = int(self.input.text)
        self.attempts += 1

        if guess < self.secret_number:
            self.label.text = f"Tente um número maior! Tentativas: {self.attempts}"
        elif guess > 50: 
            self.label.text = f'Apenas números menores que 50 '
        elif guess < 0:
            self.label.text = f'Apenas números maiores que 0'
        elif guess > self.secret_number:
            self.label.text = f"Tente um número menor! Tentativas: {self.attempts}"
        else:
            self.label.text = f"Parabéns! Você adivinhou o número em {self.attempts} tentativas."
            self.input.text = ""
            self.secret_number = random.randint(1, 100)
            self.attempts = 0