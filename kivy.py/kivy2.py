import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class firstBotao(App):
    def build(self):
        layout = BoxLayout(orientation = 'vertical')
        grid = GridLayout(cols = 1, size_hint = (1.0, 1.0))

        self.text_no_input = TextInput()
        grid.add_widget(self.troca_nome)
        
        button1.bind (on_press = self.troca_nome)
        
        text_input = TextInput(text = 'Digite seu Nome')
        grid.add_widget(text_input)

        button1 = Button(text = 'Login')
        grid.add_widget(button1)

        button2 = Button(text = 'Cancelar')
        grid.add_widget(button2)

        layout.add_widget(grid)

        return layout
    
    def troca_nome(self,):
        self.text_no_input = 'larissa'
        

if __name__ == '__main__':    
    firstBotao().run()