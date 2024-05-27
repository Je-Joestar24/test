from kivy.uix.gridlayout import GridLayout

from kivymd.uix.backdrop.backdrop import MDFloatLayout
from kivymd.app import MDApp 
from kivymd.uix.bottomnavigation.bottomnavigation import MDScreen

from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.bottomnavigation.bottomnavigation import MDScreen
from kivy.uix.accordion import FloatLayout
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDIconButton, MDFlatButton
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.core.window import Window
from kivy.clock import Clock


from kivy.uix.boxlayout import BoxLayout
from kivy.garden.mapview import MapView, MapMarkerPopup
from kivy.properties import StringProperty


# Define the KV string
KV = '''
BoxLayout:
    orientation: 'vertical'
    MDFlatButton:
        text:'uwu'

    MapView:
        id: mapview
        lat: 37.7749
        lon: -122.4194
        zoom: 13

    MDLabel:
        text: app.marker_info
        halign: 'center'
        size_hint_y: None
        height: dp(36)
'''

class MapApp(MDApp):
    marker_info = StringProperty()

    def build(self):
        return Builder.load_string(KV)


if __name__ == '__main__':
    MapApp().run()
