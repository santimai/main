from ota_update.main.ota_updater import OTAUpdater


def download_and_install_update_if_available():
    ota_updater = OTAUpdater('https://github.com/santimai/main.git')
    ota_updater.download_and_install_update_if_available('wifi-ssid', 'wifi-password')

def start():
    print("COM")
    print("COM_2")

def boot():
    download_and_install_update_if_available()
    start()


boot()

