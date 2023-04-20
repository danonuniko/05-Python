# Conditionals

## Simple Exercises

* [w3schools/booleans](https://www.w3schools.com/python/exercise.asp?filename=exercise_booleans1)
* [w3schools/operators](https://www.w3schools.com/python/exercise.asp?filename=exercise_operators1)
* [w3schools/ifelse](https://www.w3schools.com/python/exercise.asp?filename=exercise_ifelse1)

## Exercises

1. Write a program to prompt the user for hours and rate per hour to compute gross pay. Your program give the employee 1.5 times the hourly rate for hours worked above 40 hours

    > #### Example
    > * Enter Hours: **45**
    > * Enter Rate: **10**
    >
    > Pay: **475.0**  (*Tips*: 475 = 40 * 10 + 5 * 10 * 1.5)

    hours = int(input("Introduce el número de horas trabajadas: "))
    rate_hour = int(input("Introduce el precio al que se paga la hora: "))
    if hours > 40:
        ammount = 40 * rate_hour + (hours - 40)*(rate_hour * 1.5)
    else:
        ammount = hours * rate_hour
    print("El dinero que se le debe pagar es", ammount, "€")

* Rewrite your pay program using try and except so that your program handles non-numeric input gracefully.

    > #### Example
    > * Enter Hours: **20**
    > * Enter Rate: **nine**
    >> Error, please enter numeric input
    >
    > * Enter Hours: **forty**
    >> Error, please enter numeric input

    salir = False
    while salir != True:
        hours = input("¿Cuántas horas has trabajado?: ")
        try:
            hours = float(hours)
            salir = True
        except:
            print("Error, please enter numeric value")

    salir = False
    while salir != True:
        price_hour = input("¿A cuánto se paga la hora?: ")
        try:
            price_hour = float(price_hour)
            salir = True
        except:
            print("Error, please enter numeric value")

    if(hours > 40):
        print((hours-40)*price_hour*1.5 + 40*price_hour)
    else:
        print(hours*price_hour)

* Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday. Ask to user for the day number, and it returns the day name (a string).

    while True:
        day_number = input("Introduce un día de la semana del 0 al 6: ")
        try:
            day_number = int(day_number)
            if day_number >= 0 and day_number <= 6:
                break
            else:
                print("Introduce un número entre el 0 y el 6")
        except:
            print("Introduce un valor válido")

    dict_days = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
    print(dict_days[day_number])

* Give the logical opposites of these conditions
    > 1. a > b                              a <= b
    > 2. a >= b                             a < b
    > 3. a >= 18 and day == 3               a < 18 and day != 3
    > 4. a >= 18 and day != 3               a < 18 and day == 3
 