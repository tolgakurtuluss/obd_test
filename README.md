# OBD Asistan

Python‑Kivy tabanlı Android uygulama. ELM327 OBD‑II cihazıyla çalışma:
- RPM, hız okuma
- Hata kodlarını okuma/silme
- Buildozer ile `.apk` oluşturma

## Kurulum
```bash
git clone https://github.com/KULLANICI_ADIN/obd-asistan.git
cd obd-asistan
pip install -r requirements.txt
buildozer android debug