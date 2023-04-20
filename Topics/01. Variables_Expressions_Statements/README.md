# Variables, Expressions and Statements

## Simple Exercises

* [w3schools/comments](https://www.w3schools.com/python/exercise.asp?filename=exercise_comments1)
* [w3schools/variables](https://www.w3schools.com/python/exercise.asp?filename=exercise_variables1)
* [w3schools/datatypes](https://www.w3schools.com/python/exercise.asp?filename=exercise_datatypes1)
* [w3schools/numbers](https://www.w3schools.com/python/exercise.asp?filename=exercise_numbers1)

## Exercises

1. Write a program to prompt the user for hours and rate per hour to compute gross pay.

    > #### Example
    > * Enter Hours: **35**
    > * Enter Rate: **2.75**
    >
    > Pay: **96.25**

    def payAmount(hours, rate):
        return hours*rate

* Add parenthesis to the expression `6 * 1 - 2` to change its value from 4 to -6.

    6 * (1 - 2)

* Evaluate the following numerical expressions in your head, then use the Python interpreter to check your results:

    - 5 % 2             # 1
    - 9 % 5             # 4
    - 15 % 12           # 3
    - 12 % 15           # 12
    - 6 % 6             # 0
    - 0 % 7             # 0
    - 7 % 0             # Error
   
   What happened with the last example? Why? If you were able to correctly anticipate the computer’s response in all but the last one, it is time to move on. If not, take time now to make up examples of your own. Explore the modulus operator until you are confident you understand how it works.

* You look at the clock and it is exactly 2pm. You set an alarm to go off in 51 hours. At what time does the alarm go off? (Hint: you could count on your fingers, but this is not what we’re after. If you are tempted to count on your fingers, change the 51 to 5100.)

    hoursAlarm = 51
    days = 0
    while hoursAlarm > 24:
        hoursAlarm -= 24
        days += 1
    #Con este método por lo menos sabemos cuantas horas debemos sumar dentro de un rago de 24 horas. Bastaría con hacer un nuevo while evaluando desde las 2pm hasta las 00:00 para saber si pertenece al mismo día o al siguiente.

* Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours), and ask for the number of hours to wait. Your program should output what the time will be on the clock when the alarm goes off.

    hora_actual = int(input("Introduce la hora actual en formato 24h: "))
    tiempo_espera = int(input("Introduce dentro de cuantas horas quieres que suene la alarma: "))
    horas_a_sumar = tiempo_espera % 24
    if (horas_a_sumar + hora_actual > 24):
        print(horas_a_sumar + hora_actual - 24)
    else:
        print(horas_a_sumar + hora_actual)

* The formula for computing the final amount if one is earning compound interest is given on Wikipedia as
    
    ![Formula](imgs/compoundInterest.png)

    Write a Python program that assigns the principal amount of $10000 to variable P, assign to n the value 12, and assign to r the interest rate of 8%. Then have the program prompt the user for the number of years t that the money will be compounded for. Calculate and print the final amount after t years.    

    def compound_interest(ammount, number_compound_year, rate_year, years):                 # P = 10000     n = 12      r = 0.08
        return ammount * (1 + (rate_year / number_compound_year))**(number_compound_year * years)