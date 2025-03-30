import time
import datetime

def alarm(alarm_time ):
    print(f"Alarm set for {alarm_time}")
    running = True
    while running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S");
        print(current_time);
        if current_time == alarm_time:
            print("Wake up 😴😫")
            running = False
        time.sleep(1)

alarm_time = input("Enter time 24hr format  (Hrs:Min:Sec): ")
alarm(alarm_time)