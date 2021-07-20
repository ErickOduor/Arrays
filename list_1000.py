# code below gives a program that creates a list by accepting 1000 inputs one at a time and on completion tries to access item a[1000]
i = 0
while i <= 999:
    a = [i]
    while True:
        try:
            a.append(int(input("Key in integer value: ")))
            i += 1
            break
        except Exception:
            print('Invalid input, not an integer please try again')
            pass
print(a[1000])






