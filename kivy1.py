import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

class firstBotao(App):
    def build(self):
        layout = BoxLayout(orientation = 'horizontal')
        grid = GridLayout(cols = 1, size_hint = (1.0,1.0))

        self.image1 = Image(source = 'download.jpg', opacity = 0)
        self.image2 = Image(source = 'vinijr.jpg', opacity = 0)
        grid.add_widget(self.image1)
        grid.add_widget(self.image2)

        button1  = Button(text='bellingol')
        grid.add_widget(button1)
        button2  = Button(text='vini jr.')
        grid.add_widget(button2)

        button1.bind(on_press = self.bellingol)
        button2.bind(on_press = self.vinijr)
        
        layout.add_widget(grid)
        

        return layout

    def bellingol(self,bellinghan):
        self.image1.opacity = 100
        self.image2.opacity = 0
        
    def vinijr(self,vinicius):
        self.image1.opacity = 0
        self.image2.opacity = 100
        
if __name__ == '__main__':    
    firstBotao().run()