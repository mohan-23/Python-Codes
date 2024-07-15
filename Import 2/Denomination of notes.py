amount = 5151

note_2000 = 0
note_500 = 0
note_200 = 0
note_100 = 0
note_50 = 0
note_20 = 0
note_10 = 0
note_1 = 0

if amount >= 2000:
    note_2000 = int(amount/2000)
    amount = amount%2000
if amount >= 500:
    note_500 = int(amount/500)
    amount = amount%500
if amount >= 200:
    note_200 = int(amount/200)
    amount = amount%200
if amount >= 100:
    note_100 = int(amount/100)
    amount = amount%100
if amount >= 50:
    note_50 = int(amount/50)
    amount = amount%50
if amount >= 20:
    note_20 = int(amount/20)
    amount = amount%20
if amount >= 10:
    note_10 = int(amount/10)
    amount = amount%10
note_1 = amount

print(note_2000)
print(note_500)
print(note_200)
print(note_100)
print(note_50)
print(note_20)
print(note_10)
print(note_1)