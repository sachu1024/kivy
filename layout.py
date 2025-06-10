from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.boxlayout import BoxLayout 

class HelloApp(App):
    def build(self):
        lo=BoxLayout(orientation='vertical')
        l1=Label(text="Hello World",font_size=50)
        l2=Label(text="This is my page",font_size=50,color=(1,0,0,1))
        lo.add_widget(l1)
        lo.add_widget(l2)
        return lo

app = HelloApp()
app.run()