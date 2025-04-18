import random

Hinata = 0
Kageyama = 0
Tsukishima = 0
Daichi = 0
Asahi = 0

Q1 = input("What word would people close to you use to describe you? \n a) Energetic \n b) Talented \n c) Grumpy \n d) Reliable \n e) Nervous \n")
if Q1 == "a":
  Hinata += 1
elif Q1 == "b":
  Kageyama += 1
elif Q1 == "c":
  Tsukishima += 1
elif Q1 == "d":
  Daichi += 1
elif Q1 == "e":
  Asahi += 1
else:
  print("Invalid input. Please enter a valid option.")

Q2 = input("Are you good at studying? \n a) Yes \n b) No \n c) I'm okay \n")
if Q2 == "a":
  Tsukishima += 1
elif Q2 == "b":
  Kageyama += 1
  Hinata += 1
elif Q2 == "c":
  Daichi += 1
  Asahi += 1
else:
  print("Invalid input. Please enter a valid option.")

Q3 = input("Are you calm and collected under pressure? \n a) Yes \n b) No \n")
if Q3 == "a":
  Tsukishima += 1
  Daichi += 1
  Kageyama += 1
elif Q3 == "b":
  Asahi += 1
  Hinata += 1
else:
  print("Invalid input. Please enter a valid option.")

Q4 = input("How do you react to a challenging situation? \n a) Calmly analyse the situation \n b) Delegate across the team \n c) Express frustration \n d) Avoid the situation \n")
if Q4 == "a":
  Tsukishima += 1
  Kageyama += 1
elif Q4 == "b":
  Daichi += 1
elif Q4 == "c":
  Hinata += 1
elif Q4 == "d":
  Asahi += 1
else:
  print("Invalid input. Please enter a valid option.")

Q5 = input("When do you have the most fun? \n a) When I'm winning \n b) When others need me \n c) When I'm facing a challenge \n d) When I'm in a team \n")
if Q5 == "a":
  Kageyama += 1
elif Q5 == "b":
  Daichi += 1
elif Q5 == "c":
  Hinata += 1
  Tsukishima += 1
elif Q5 == "d":
  Asahi += 1
else:
  print("Invalid input. Please enter a valid option.")

if Hinata > 2:
  print ("You're Hinata! You are a fun-loving, energetic person who is always looking for the next adventure. You are very optimistic and have a great sense of humor. You are also very loyal to your friends and family.")
if Kageyama > 2:
  print ("You're Kageyama! You are a talented and hardworking person who is always striving to be the best. You are very competitive and have a strong sense of justice. You are also very loyal to your friends and family.")
if Tsukishima > 2:
  print ("You're Tsukishima! You are a grumpy and sarcastic person who is always looking for the next challenge. You are very intelligent and have a great sense of humor. You are also very loyal to your friends and family.")
if Daichi > 2:
  print ("You're Daichi! You are a reliable and responsible person who is always looking out for others. You are very hardworking and have a great sense of humor. You are also very loyal to your friends and family.")
if Asahi > 2:
  print ("You're Asahi! You are a nervous and shy person who is always looking for the next challenge. You are very intelligent and have a great sense of humor. You are also very loyal to your friends and family.")