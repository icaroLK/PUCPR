from time import sleep

count = 0
light = 0

while True:
    sleep(1)
    count += 1
    if count == 864:
        light += 1

    print(count, light)