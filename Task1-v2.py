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
Count population growth per second, multiplied by seconds per year
----------------
Output : Total population after certain amount of years
'''


Population = 26277169
Time = 0
minutes_per_year = 60*24*365
Births_per_minute = 60/7 * minutes_per_year
Deaths_per_minute = 60/13 * minutes_per_year
Immigrations_per_minute = 60/45 * minutes_per_year
End_Population = Population+((Immigrations_per_minute+Births_per_minute)-Deaths_per_minute)
Years = 1

start = True

while start:
    Time+=1

    End_Population = Population+((((Immigrations_per_minute+Births_per_minute)-Deaths_per_minute))*Years)
    print('----------')
    print(Time)
    print(Births_per_minute)
    print(Deaths_per_minute)
    print(Immigrations_per_minute)
    Years+=1
    print(f'Year {Time}: {End_Population:,}')
    print('----------')
 #38,140,000, 38,928,400, 38,899,200
    if Time == 5:
        start = False


'''
def main():
    ...

if __name__ == "__main__":
    main()
'''