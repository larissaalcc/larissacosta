import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from excluircadastro import excluir_cadastro
from editarcadastro import Editar_cadastro

class sistema_cadastro(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)        
        
        layout = BoxLayout(orientation = 'vertical')
        grid = GridLayout(cols = 1, size_hint = (1.0, 1.0))
        
        self.input_nome = TextInput(hint_text = "Nome Completo: ")
        grid.add_widget(self.input_nome)
        self.inputnome = self.input_nome
        
        self.input_cpf = TextInput(hint_text = "CPF: ")
        grid.add_widget(self.input_cpf)
        self.inputcpf = self.input_cpf 
        
        self.input_email = TextInput(hint_text = "Email: ")
        grid.add_widget(self.input_email)
        self.inputemail = self.input_email
        
        self.input_telefone = TextInput(hint_text = "Telefone: ")
        grid.add_widget(self.input_telefone)
        self.inputtelefone = self.input_telefone
        
        self.input_endereco = TextInput(hint_text = "Endereço: ")
        grid.add_widget(self.input_endereco)
        self.inputendereco = self.input_endereco
        
        self.botao_cadastrar = Button(text = "Cadastrar")
        grid.add_widget(self.botao_cadastrar)
               
        self.botao_editar = Button (text = "Editar Cadastro")
        grid.add_widget(self.botao_editar)
        
        self.botao_editar.bind (on_press = self.editar)
                
        self.botao_excluir = Button (text = "Excluir Cadastro")
        grid.add_widget(self.botao_excluir)
        
        self.botao_excluir.bind (on_press = self.excluir)
        
        self.botao_sair = Button(text = "Sair")
        grid.add_widget(self.botao_sair)
        
        self.botao_sair.bind (on_press = self.exit_game)
    
        layout.add_widget(grid)

        self.add_widget(layout)
        
    def editar(self,instance):
        self.manager.current = 'Editar cadastro'
    
    def excluir (self,instance):
        self.manager.current = 'Excluir cadastro'
        
        
    
            
    def exit_game(self, instance):
        App.get_running_app().stop()

        App.get_running_app()

        App.get_running_app

        App.get_running_app
    
        
        

    
