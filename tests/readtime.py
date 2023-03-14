import time
def read_time(sentence):
    print(sentence)
    lstt = sentence.split()
    time_count = 0
    for item in lstt:
        if len(item) > 3:
            time_count += 1
        else:
            time_count += 0.4
    while time_count < (len(lstt) - 4):
        time_count += 1
    print(time_count/3)
    time.sleep(time_count/3)
#read_time("Do you say if I go now but how can you not.")
#read_time("Wherever shall that pleasure ship which Harold purchased travel this occassion, furthermore what people and what number will ride?")
#read_time("A quick brown fox jumped over the lazy dog.")
read_time("You sit up. It seems you have fallen from the sky and crashed through the roof of an old man's home. That's somewhat unusual.")