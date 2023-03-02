'''
Write  a  GUI program  for  calculating  the  quiz  mark  for  ST1  unit.  The  program 
should read four inputs as quiz mark for each quiz, save it as integers, and calculator the sum 
of four quiz marks and display the sum. A test run of the working program is as shown below:
'''

print("A  console  interface  program  for  calculating  the  quiz  mark  for  ST1  unit")
Quiz1 = int(input('Enter quiz 1 marks(out  of 10) '))
Quiz2 = int(input('Enter quiz 2 marks(out  of 10) '))
Quiz3 = int(input('Enter quiz 3 marks(out  of 10) '))
Quiz4 = int(input('Enter quiz 4 marks(out  of 10) '))

Total = Quiz1+Quiz2+Quiz3+Quiz4

print(f"The quiz marks for ST1 unit is {Total}")