'''
The ABS projections on population is based on the following assumptions:
One birth every 7 seconds
One death every 13 seconds
One new immigrant every 45 seconds
Write a program  (GUI program) to display the population for each of the next five years. Use the 
current Australian population and that one year has 365 days.

Input : Amount of years to predict population for
Process :
----------------
Count timer - every few seconds add a point to death, birth, immigration (timer%DBI?)
Total = (immi+birth)-death
----------------
Output : Total population after certain amount of years
'''

Deaths = 0
Births = 0
Immigrations = 0
Population = 25000000
End_Population = Population+((Immigrations+Births)-Deaths)
Time = 0
hours_per_year = 24*365
Years = 5

start = True


while start:
    Time+=1

    if Time%7 ==0:
        Births += 1
    if Time%13 ==0:
        Deaths += 1
    if Time%45 ==0:
        Immigrations += 1

    End_Population = Population+((((Immigrations+Births)-Deaths)*hours_per_year)*Years)
    print('----------')
    print(Time)
    print(Births)
    print(Deaths)
    print(Immigrations)
    print(f'{End_Population:,}')
    print('----------')
 #38,140,000, 38,928,400, 38,899,200
    if Time == 3600:
        start = False


'''
def main():
    ...

if __name__ == "__main__":
    main()
'''