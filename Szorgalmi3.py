try:
    Number = input("Kérem a másodpercet:")
    Second = int(Number)

    if Second < 0 :
        print("Invalid input")
    elif Second == 0 :
        print("Now")
    else:
        secondInMin = 60
        secondInHour = 60 * secondInMin
        secondInDays = 24 * secondInHour
        secondInYears = 365 * secondInDays

        Years = Second // secondInYears
        Second = Second - Years * secondInYears

        Days = Second // secondInDays
        Second = Second - Days * secondInDays

        Hours = Second // secondInHour
        Second = Second - Hours * secondInHour

        Minutes = Second // secondInMin
        Masodperc = Second - Minutes*secondInMin

        number_of_units = 0
        if Years > 0 :
            number_of_units +=1
        if(Days > 0) :
            number_of_units +=1
        if(Hours > 0) :
            number_of_units+=1
        if(Minutes > 0) :
            number_of_units +=1
        if(Masodperc > 0) :
            number_of_units +=1

        output = ""
        if Years > 0 :
            output += str(Years) + "year"
            if Years > 1 :
                output+="s"
            if number_of_units > 2 :
                output += ", "
            elif number_of_units == 2 :
                output += " and "
            number_of_units -=1

        if Days > 0 :
            output += str(Days) + "Day"
            if Days > 1 :
                output+="s"
            if number_of_units > 2 :
                output += ", "
            elif number_of_units == 2 :
                output += " and "
            number_of_units -=1

        if Hours > 0 :
            output += str(Hours) + "Hour"
            if Hours > 1 :
                output+="s"
            if number_of_units > 2 :
                output += ", "
            elif number_of_units == 2 :
                output += " and "
            number_of_units -=1

        if Minutes > 0 :
            output += str(Minutes) + "minute"
            if Minutes > 1 :
                output+="s"
            if number_of_units > 2 :
                output += ", "
            elif number_of_units == 2 :
                output += " and "
            number_of_units -=1

        if Masodperc > 0 :
            output += str(Masodperc) + "second"
            if Masodperc > 1 :
                output+="s"
            if number_of_units > 2 :
                output += ", "
            elif number_of_units == 2 :
                output += " and "
            number_of_units -=1

    print(output)
except ValueError :
    print("Invalid bemenet")
