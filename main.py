import json
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MiniEngineApp(App):
    def build(self):
        engine_status = {"status": "Online", "step": "1"}
        
        layout = BoxLayout(orientation='vertical', padding=20)
        self.label = Label(
            text=f"MI System Mini Engine:\n{json.dumps(engine_status, indent=2)}",
            font_size='18sp',
            halign='center'
        )
        layout.add_widget(self.label)
        return layout

if __name__ == '__main__':
    MiniEngineApp().run()
