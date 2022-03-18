age=33
while True:
  guess=int(input("enter your guess"))
  if guess < age:
    print("enter bigger guess")
  elif guess > age:
    print("enter lower guess")
  else:
    print("right guess")
    break     # else çalışırsa break yap demek
