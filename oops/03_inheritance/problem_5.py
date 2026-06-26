class Device:
    def power_on(self):
        print("Device Powered On")

class InternetEnabled:
    def connect_wifi(self):
        print("Connected to WiFi")

class SmartTV(Device, InternetEnabled):
    def watch_netflix(self):
        print("Netflix Started")

tv = SmartTV()
tv.power_on()
tv.connect_wifi()
tv.watch_netflix()

print(SmartTV.__mro__)