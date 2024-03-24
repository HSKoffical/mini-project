# import win32com.client
#
# # Calling the Dispatch method of the module which
# # interact with Microsoft Speech SDK to speak
# # the given input from the keyboard
#
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# list1="rahul"
#
#
# shotout="shotout to "+list1
# speaker.Speak(shotout)
# import required module
# import required module
# import os
# import shutil
# shutil.move("C:/Users/Admin/Downloads/alarm-clock-short-6402.mp3",os.getcwd())fr
from playsound import playsound
import time
def sound():
    playsound("C:/Users/Admin/Downloads/alarm-clock-short-6402.mp3")
def time_s():
    print("1 Hours\n"
          "2 Minutes\n"
          "3 Seconds\n"
          "4 Combination\n")

    user_input=int(input(": "))
    if user_input==1:
        user_time = int(input("hour: "))
        sec = user_time
        hour=user_time*3600
        time.sleep(hour)
        sound()
    if user_input==2:
        user_time = int(input("mintues: "))
        sec = user_time
        min=user_time*60
        time.sleep(min)
        sound()
    if user_input==3:
        user_time=int(input("seconds: "))
        sec=user_time
        time.sleep(sec)
        sound()
    if user_input == 4:
        hour=int(input("Hour: "))*3600
        min=int(input("min: "))*60
        sec=int(input("sec: "))
        time.sleep(hour+min+sec)
        sound()

if __name__ == "__main__":
    time_s()


