counter = 1
i= 1
while counter <= 10:
    counter += 1
    if counter % 2 == 0:
        continue
    i += 1
    print(f'#{i}_{counter}')
