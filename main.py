length = 10

names = []
scores = []
percentages = []
grades = []

for x in range(length):
  names.append(input('Please enter student name : '))


for x in range(length):
  number = False
  while not number:
    number = True
    string_in = (input(f'Please enter a score between 0 and 150 for {names[x]}:'))

    for letter in string_in:
      if letter < '0' or letter > '9':
        number = False

  score = int(string_in)

  while score <0 or score >150:
    score = int(input(f'Please enter a valid score between 0 and 150 for {names[x]}:'))


  percentage = score / 150 * 100


  if percentage >=85:
    grade = "A"
  elif percentage <85 and percentage >= 70:
    grade = "B"
  elif percentage <70 and percentage >=55:
    grade = "C"
  elif percentage <55 and percentage >=40:
    grade = "D"
  else:
    grade = 'F'

  percentage = round(percentage,2)

  scores.append(score)
  percentages.append(percentage)
  grades.append(grade)

print()
print (f'{"Name":20}{"Score":20}{"Percentage":20}{"Grade"}')

for x in range (length):
  print (f'{names[x]:20}{scores[x]:<20}{percentages[x]:<20}{grades[x]}')
