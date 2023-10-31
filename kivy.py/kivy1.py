import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class HelloWord(App):
    def build (self):
        layout = BoxLayout (orientation='vertical')
        tamanho = '80'
        self.label = Label (text= 'Hello World!!', font_size = tamanho)
        button = Button(text = 'Button', size_hint = (1,0.5))
        Button.bind(one_press = self.on_button)
        layout.add_widget(self.label)
        layout.add_widget(button)
        return layout
    def on_button (self,instance):
         self.label.text = 'Professor Mauricio'
         
if __name__ == "__main__":
    HelloWord().run()