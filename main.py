from kivy.app import App 
from kivy.uix.label import Label 

class HelloApp(App):
    def build(self):
        l1=Label(text="Hello this is my first code",font_size=50)
        return l1

app = HelloApp()
app.run()