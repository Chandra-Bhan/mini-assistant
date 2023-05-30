import speedtest
from Body.Speak import Speak

def speedTester():
    Speak("Ok Sir! Testing! ")
    speed_test = speedtest.Speedtest()

    def bytes_to_mb(bytes):
      KB=1024
      MB=KB*1024
      return int(bytes/MB)

    download_speed = bytes_to_mb(speed_test.download())
    upload_speed =bytes_to_mb(speed_test.upload())
    print(f"Your download speed is: {download_speed} MB/S ! And Upload Speed is: {upload_speed} MB/S")
    speed=f"Your download speed is: {download_speed} MB/S ! And Upload Speed is: {upload_speed} MB/S"
    Speak(speed)

# speedTester()
