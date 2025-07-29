# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
import obd_handler

class OBDApp(App):
    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.1, 1)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.label = Label(text="Hazır", color=(1,1,1,1), font_size=18, size_hint=(1, 0.2))

        btn_rpm = Button(text="🔄 RPM Oku", size_hint=(1, 0.2), on_press=self.rpm_oku)
        btn_speed = Button(text="🚗 Hız Oku", size_hint=(1, 0.2), on_press=self.hiz_oku)
        btn_dtc = Button(text="🛠 Hata Kodlarını Oku", size_hint=(1, 0.2), on_press=self.hatalari_oku)
        btn_clear = Button(text="🧹 Hata Kodlarını Sil", size_hint=(1, 0.2), on_press=self.hatalari_sil)

        layout.add_widget(btn_rpm)
        layout.add_widget(btn_speed)
        layout.add_widget(btn_dtc)
        layout.add_widget(btn_clear)
        layout.add_widget(self.label)

        return layout

    def rpm_oku(self, instance):
        self.label.text = "Motor devri: " + obd_handler.rpm_oku()

    def hiz_oku(self, instance):
        self.label.text = "Araç hızı: " + obd_handler.hiz_oku()

    def hatalari_oku(self, instance):
        self.label.text = obd_handler.hata_kodlarini_oku()

    def hatalari_sil(self, instance):
        self.label.text = obd_handler.hata_kodlarini_temizle()

if __name__ == "__main__":
    OBDApp().run()