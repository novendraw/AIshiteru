import kivy
kivy.require('1.11.1')  # Set to your Kivy version
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
import kbs_main

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class RuleDialog(FloatLayout):
    rule = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)

class Kbs(GridLayout):
    loadfile = ObjectProperty(None)
    sourceimage = ObjectProperty(None)
    goal = ObjectProperty(None)
    resultimage = ObjectProperty(None)
    detectresult = ObjectProperty(None)
    matchfacts = ObjectProperty(None)
    hitrules = ObjectProperty(None)
    text_input = ObjectProperty(None)


    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_rule(self):
        with open('./rules.py') as stream:
            content = RuleDialog(cancel=self.dismiss_popup)
            content.text_input.text = stream.read()
        self._popup = Popup(title="Daftar Rule", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def update_data(self, resultimage, matchfacts, hitrules):
        self.resultimage.source = resultimage
        self.matchfacts.text = matchfacts
        self.hitrules.text = hitrules

    def get_result(self, query):
        if (query in self.hitrules.text):
            self.detectresult.text = "True / Found"
        else:
            self.detectresult.text = "False / Not Found"

    def load(self, path ):
        self.sourceimage.source = path[0]
        kbs_main.main(
            self.sourceimage.source,
            self.update_data)
        self.dismiss_popup()

class MyApp(App):
    def build(self):
        return Builder.load_file('kbs.kv')


MyApp().run()