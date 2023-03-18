# Show time every second
import time

while True:
    t = open("clock.txt", "a")
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    t.write(result + "\n")
    time.sleep(1)
    t.close()
