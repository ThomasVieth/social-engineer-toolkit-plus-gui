##
##
##
##
##

## Imports

from ...core.frame import OptionFrame

##

class AttackFrame(OptionFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.add_option("Spear-Phishing Attack Vectors", self.sub_to_spear)
        self.add_option("Website Attack Vectors", self.sub_to_web)
        self.add_option("Infectious Media Generator", self.sub_to_infect)
        self.add_option("Create a Payload and Listener", self.sub_to_payload)
        self.add_option("Mass Mailer Attack", self.sub_to_mail)
        self.add_option("Arduino-Based Attack Vector", self.sub_to_arduino)
        self.add_option("Wireless Access Point Attack Vector", self.sub_to_wireless)
        self.add_option("QRCode Generator Attack Vector", self.sub_to_qrcode)
        self.add_option("Powershell Attack Vectors", self.sub_to_powershell)
        self.add_option("SMS Spoofing Attack Vector", self.sub_to_sms)

        self.menu.add_command(label="Back", command=self.back)

    def sub_to_spear(self, *args, **kwargs):
        print("Test 1")

    def sub_to_web(self, *args, **kwargs):
        print("Test 2")

    def sub_to_infect(self, *args, **kwargs):
        print("Test 3")

    def sub_to_payload(self, *args, **kwargs):
        print("Test 4")

    def sub_to_mail(self, *args, **kwargs):
        print("Test 5")

    def sub_to_arduino(self, *args, **kwargs):
        print("Test 6")

    def sub_to_wireless(self, *args, **kwargs):
        print("Test 7")

    def sub_to_qrcode(self, *args, **kwargs):
        print("Test 8")

    def sub_to_powershell(self, *args, **kwargs):
        print("Test 9")

    def sub_to_sms(self, *args, **kwargs):
        print("Test 10")

    def back(self, *args, **kwargs):
        frame = self.master.get_frame("MainFrame")
        frame.reset_menu()
        frame.resize_window()
        frame.tkraise()