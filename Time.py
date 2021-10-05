
#this code executes multiple different methods within the time class, using the fields hours, minutes and seconds
class Time :
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def getHours(self):
        return self.hours

    def getMinutes(self):
        return self.minutes

    def getSeconds(self):
        return self.seconds
    #Method toString
    #returns timeAsString the string representation of an instance of the time class
    def toString(self):
        return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)
    #Method timeInSeconds
    #returns timeInSecs the time in seconds of an instance of the Time object
    def timeInSeconds(self):
        timeInSec = self.seconds + self.minutes*60 + self.hours*60*60
        return timeInSec
    #Method changeTheTime
    #Change the time fields of an instance of the time class
    #Precondition: All of the values are within  the regular ranges for time - hours, minutes and seconds
    #@param h # of hours
    #@param m # of minutes
    #@param s # of seconds
    def changeTheTime(self, h, m, s):
        self.hours = h
        self.minutes = m
        self.seconds = s
    #Method twelveHourClock
    #return a the string representation of an instance of the time object with a morning or evening tag
    def twelveHourClock(self):
        a = ""
        #this if statement assigns am or pm to the end of the string representation of an instance of the time object
        #based on if the value in the hours position is equal to or after 12 --- pm --- or before --- am ---
        if self.hours >= 12 :
            a = str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds) + " pm"
        else :
            a = str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds) + " am"
        return a
    #Method whatTimeIsIt
    #return timeOfDay the time of day of an instance of the time object
    def whatTimeIsIt(self):
        timeOfDay = ""
        #this if statement assigns a specific time of day to the variable time of day based on what value is in the hour position
        if self.hours > 6 and self.hours <= 12 :
            timeOfDay = "morning"
        elif self.hours > 12 and self.hours <= 17 :
            timeOfDay = "afternoon"
        elif self.hours > 17 and self.hours <= 22 :
            timeOfDay = "evening"
        elif self.hours >+ 22 or self.hours <= 6 :
            timeOfDay = "night"

        return timeOfDay
    #Method compareTo
    #param t an instance of the Time object
    #return differenceInTimes the difference between the time in number of seconds between the object that called the method and the parameter object
    def compareTo(self, t):
        secondsTimeObjParam = self.hours * 3600 + self.minutes * 60 + self.seconds
        secondsTimeObjCall = t.getHours() * 3600 + t.getMinutes() * 60 + t.getSeconds()
        differenceInTimes = 0
        differenceInTimes = secondsTimeObjParam - secondsTimeObjCall

        return differenceInTimes