# demonstrating multithreading (multitasking

import time
import threading

def walk_dog():
    time.sleep(8);
    print("You walked the dog");

def wash_dishes():
    time.sleep(6);
    print("You washed the dishes");

def take_out_trash():
    time.sleep(2);
    print("You took out the trash");

# calling these functions without threading it takes a lot of time to complete each task but with threading you can multitask

chore1 = threading.Thread(target=walk_dog)
chore1.start()
chore2 = threading.Thread(target= wash_dishes);
chore2.start()
chore3 = threading.Thread(target= take_out_trash);
chore3.start()

chore1.join();
chore2.join();
chore3.join();
print("You are done for the day.")
