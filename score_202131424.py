hw = int(input("과제"))

mt = int(input("중간"))

ft = int(input("기말"))

avr = (hw + mt + ft)/3

print("평균: %6.2"%(avr))

score = (hw + mt + ft)/3

if 100 >= score >= 90:
    grade = "A"
elif 90 > score >= 80:
    grade = "B"
elif 80 > score >= 70:
    grade = "C"
elif 70 > score >= 60:
    grade = "D"
else:
    grade = "F"
    
print("등급" + grade)
