# obd_handler.py
import obd

# Bağlantı kur (buildozer ile Bluetooth erişimi için pyjnius gerekebilir)
connection = obd.OBD()  # Otomatik port bulur

def rpm_oku():
    response = connection.query(obd.commands.RPM)
    return str(response.value) if not response.is_null() else "Veri yok"

def hiz_oku():
    response = connection.query(obd.commands.SPEED)
    return str(response.value) if not response.is_null() else "Veri yok"

def hata_kodlarini_oku():
    response = connection.query(obd.commands.GET_DTC)
    if response.value:
        return "\n".join(str(code) for code in response.value)
    else:
        return "Hata kodu yok"

def hata_kodlarini_temizle():
    connection.query(obd.commands.CLEAR_DTC)
    return "Hata kodları silindi"