lesson1=float(input("please enter the scores of farsi:"))
lesson2=float(input("please enter the scores of riazi:"))
lesson3=float(input("please enter the scores of olom:"))
lesson4=float(input("please enter the scores of quran:"))
lesson5=float(input("please enter the scores of hedieh:"))
result1=(lesson1+lesson2+lesson3+lesson4+lesson5)/5

if result1<14:
    result="fail"
else:
    result="pass"

print("*"*50)
print(f"farsi is:{lesson1}")
print(f"riazi is:{lesson2}")
print(f"olom is:{lesson3}")
print(f"quran is:{lesson4}")
print(f"hedieh is:{lesson5}")
print("*"*50)
print(f"result is{result1}")
print("*"*50)
print(f"your student status is:{result}")