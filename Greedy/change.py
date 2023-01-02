pay = int(input())

count = 0

change_500 = int(pay/500)
count += change_500
remain = pay % 500

change_100 = int(remain/100)
count += change_100
remain = remain %100

change_50 = int(remain/50)
count += change_50
remain = remain % 50

change_10 = int(remain/10)
count += change_10

print(count)
