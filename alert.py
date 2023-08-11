
#*modules*#
import pyautogui
import time

#*input for the time sleep*#
time_for_alert_second = int(input('how many second for alert , enter integer number : '))
time_for_alert_minute = int(input('how many minute for alert , enter integer number : '))
time_for_alert_hours = int(input('how many hours for alert , enter integer number : '))

time_for_alert_hours * 3600
time_for_alert_minute * 60

time.sleep(time_for_alert_second,)
time.sleep(time_for_alert_minute)
time.sleep(time_for_alert_hours)

pyautogui.alert(text= 'give up ,donkey',title='المنبه ',button='ok')