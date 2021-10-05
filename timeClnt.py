from Time import Time

class timeClnt :
    t1 = Time(16, 42, 8)
    t2 = Time(12, 38, 2)
    t3 = Time(6, 38, 12)
    t4 = Time(20, 42, 8)
    t5 = Time(15, 15, 15)
    t6 = Time(20, 20, 20)

    print("t1 = " + str(t1))
    print("t2 = " + str(t2))
    print("t3 = " + str(t3))

    hours = t1.getHours()
    minutes = t1.getMinutes()
    seconds = t1.getSeconds()

    print("Hours = " + str(hours))
    print("Minutes = " + str(minutes))
    print("Minutes = " + str(seconds))

    print("the string representation of the t1 = " + t1.toString())
    print("the string representation of the t2 = " + t2.toString())

    print("the time in seconds of t1 is " + str(t1.timeInSeconds()))
    print("the time in seconds of t2 is " + str(t2.timeInSeconds()))

    t5.changeTheTime(14, 25, 6)
    t6.changeTheTime(12, 12, 12)

    print(str(t5.toString()))
    print(str(t6.toString()))

    print("the twelve hour clock representation of t1 is " + t1.twelveHourClock())
    print("the twelve hour clock representation of t2 is " + t2.twelveHourClock())

    print("the time of day of time t1 =" + t1.whatTimeIsIt())
    print("the time of day of time t2 =" + t2.whatTimeIsIt())
    print("the time of day of time t3 =" + t3.whatTimeIsIt())
    print("the time of day of time t4 =" + t4.whatTimeIsIt())

    x = Time(12, 6, 8)
    y = Time(12, 38, 2)
    z = Time(6, 58, 2)

    compareToTest1 = t1.compareTo(x)

    compareToTest2 = t2.compareTo(y)

    compareToTest3 = z.compareTo(t4)

    print( "the difference between Time object that called the method and the Time object parameter =" + str(compareToTest1))
    print("the difference between Time object that called the method and the Time object parameter =" + str(compareToTest2))
    print("the difference between Time object that called the method and the Time object parameter =" + str(compareToTest3))