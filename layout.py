from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.boxlayout import BoxLayout 

class HelloApp(App):
    def build(self):
        lo=BoxLayout(orientation='vertical')
        loo=BoxLayout(orientation='horizontal')
        l1=Label(text="Hello World",font_size=50)
        l2=Label(text="This is my page",font_size=50,color=(1,0,0,1))
        l3=Label(text="Horizontal page ", font_size=60, color=(1,1,0,1))
        lo.add_widget(l1)
        lo.add_widget(l2)
        loo.add_widget(l3)
        lo.add_widget(loo)
        return lo

app = HelloApp()
app.run()