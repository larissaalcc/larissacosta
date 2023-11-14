import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from excluircadastro import excluir_cadastro
from editarcadastro import Editar_cadastro
from sistema import sistema_cadastro

class app(App):
    def build(self):
        screen = ScreenManager()
        screen.add_widget(sistema_cadastro (name = 'Tela Inicial'))
        screen.add_widget(Editar_cadastro(name = 'Editar cadastro'))
        screen.add_widget(excluir_cadastro(name = 'Excluir cadastro'))
        
        return screen

if __name__ == '__main__':    
    app().run()