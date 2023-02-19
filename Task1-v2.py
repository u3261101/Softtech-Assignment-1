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


Population = 25000000
Time = 0
minutes_per_year = 60*24*365
Deaths = 13/60 * minutes_per_year
Births = 7/60 * minutes_per_year
Immigrations = 45/60 * minutes_per_year
End_Population = Population+((Immigrations+Births)-Deaths)
Years = 5

start = True


while start:
    Time+=1

    End_Population = Population+((((Immigrations+Births)-Deaths))*Years)
    print('----------')
    print(Time)
    print(Births)
    print(Deaths)
    print(Immigrations)
    print(f'{End_Population:,}')
    print('----------')
 #38,140,000, 38,928,400, 38,899,200
    if Time == 1:
        start = False


'''
def main():
    ...

if __name__ == "__main__":
    main()
'''