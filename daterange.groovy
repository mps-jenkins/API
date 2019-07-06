
import static java.util.Calendar.YEAR
//date_range = "March 2002:April 2002"
//date_range = "Dec 1, 2000:Jan 2001"
date_range = "Dec 2000:Jan 21,2001"
//date_range = "Sep 6:Oct 6"
//date_range = "Sep:Oct"


monthsFullNames = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]
monthsAcronym = ["Jan", "Feb", "Mar", "Apr", "May", "Jun","Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
full_data = "Your meeting was found Dec 30, 2000 to be out of date and has been automatically updated."
monthAcronymDayCount = [
        "Jan": 31,
        "Feb": 28,
        "Mar": 31,
        "Apr": 30,
        "May": 31,
        "Jun": 30,
        "Jul": 31,
        "Aug": 31,
        "Sep": 30,
        "Oct": 31,
        "Nov": 30,
        "Dec": 31
]

monthFullNameDayCount = [
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
]

if ( date_range =~ /\b\s*\S+\s*\b\:\b\s*\S+\s*\b/ ) {
    println "yes"
    monthandyearfunction(full_data,date_range)
    fullyearandmonthyearfunction(full_data,date_range)
    monthanddaterangefunction(full_data,date_range)
    monthandmonthrangefunction(full_data,date_range)
    monthyearandfullyearfunction(full_data,date_range)
}



def monthandyearfunction(full_data, date_string ) {
    def date_input = date_string =~ /(?i)\b(\S+)\s*(\d{4})\b\:\b(\S+)\s*(\d{4})\b/
    if (date_input.matches()) {
        firstmonth = date_input[0][1].toString()
        firstyear = date_input[0][2].toInteger()
        secondmonth = date_input[0][3].toString()
        secondyear = date_input[0][4].toInteger()

        println ( firstmonth + "," + firstyear + "," + secondmonth + "," + secondyear  )
        def fromdate = Date.parse("yyyy-MMM-dd", "${firstyear}-${firstmonth}-1")
        if (monthAcronymDayCount.containsKey(secondmonth)) {
            println (monthAcronymDayCount[secondmonth])
            secondday = monthAcronymDayCount[secondmonth]
            println secondday
        }
        secondday = monthAcronymDayCount[secondmonth]
        if ( (secondday.equals(null))) {
            secondday = monthFullNameDayCount[secondmonth]
        }

        def todate = Date.parse("yyyy-MMM-dd", "${secondyear}-${secondmonth}-${secondday}")
        fromdate.upto(todate) { it  ->
            datevalue = "${it.format('MMM dd, yyyy')}"
            println datevalue
            fullDateMatch(full_data,datevalue)
        }
    }
}



def fullyearandmonthyearfunction(full_data, date_string ) {
    def date_input = date_string =~ /(?i)\b(\S+)\b\s+(\d+),\s*\b(\d{4})\b\:\b(\S+)\s*(\d{4})\b/

    if (date_input.matches()) {
        firstmonth = date_input[0][1].toString()
        firstdate = date_input[0][2].toInteger()
        firstyear = date_input[0][3].toInteger()
        secondmonth = date_input[0][4].toString()
        secondyear = date_input[0][5].toInteger()


        def fromdate = Date.parse("yyyy-MMM-dd", "${firstyear}-${firstmonth}-${firstdate}")
        if (monthAcronymDayCount.containsKey(secondmonth)) {
            println (monthAcronymDayCount[secondmonth])
            secondday = monthAcronymDayCount[secondmonth]
            println secondday
        }

        secondday = monthAcronymDayCount[secondmonth]
        if ( (secondday.equals(null))) {
            secondday = monthFullNameDayCount[secondmonth]
        }

        def todate = Date.parse("yyyy-MMM-dd", "${secondyear}-${secondmonth}-${secondday}")
        // println ( secondyear + secondmonth + secondday  )
        println  ("todate" + todate)
        fromdate.upto(todate) { it  ->

            datevalue = "${it.format('MMM dd, yyyy')}"
            println datevalue
            fullDateMatch(full_data,datevalue)
        }
    }
}

def monthyearandfullyearfunction(full_data, date_string ) {
    def date_input = date_string =~ /(?i)\b(\S+)\s*(\d{4})\b\:\b(\S+)\b\s+(\d+),\s*\b(\d{4})\b/
    if (date_input.matches()) {
        firstmonth = date_input[0][1].toString()
        firstyear = date_input[0][2].toInteger()
        secondmonth = date_input[0][3].toString()
        secondday = date_input[0][4].toInteger()
        secondyear = date_input[0][5].toInteger()
        def firstday
        if ( firstday.equals(null)) {
            firstday = 1
        }
        def fromdate = Date.parse("yyyy-MMM-dd", "${firstyear}-${firstmonth}-${firstday}")
        def todate = Date.parse("yyyy-MMM-dd", "${secondyear}-${secondmonth}-${secondday}")
        fromdate.upto(todate) { it  ->
            datevalue = "${it.format('MMM dd, yyyy')}"
            println datevalue
            fullDateMatch(full_data,datevalue)
        }
    }
}

def monthanddaterangefunction(full_data, date_string ) {
    def date_input = date_string =~ /(?i)\b(\S+)\b\s*(\d+)\b\:\b(\S+)\b\s*(\d+)\b/
    if (date_input.matches()) {
        firstmonth = date_input[0][1].toString()
        firstdate = date_input[0][2].toInteger()
        secondmonth = date_input[0][3].toString()
        seconddate = date_input[0][4].toInteger()

        def fromdate = Date.parse("MMM-dd", "${firstmonth}-${firstdate}")
        if (monthAcronymDayCount.containsKey(secondmonth)) {
            println (monthAcronymDayCount[secondmonth])
            secondday = monthAcronymDayCount[secondmonth]
            println secondday
        }
        secondday = monthAcronymDayCount[secondmonth]
        if ( (secondday.equals(null))) {
            secondday = monthFullNameDayCount[secondmonth]
        }
        def todate = Date.parse("MMM-dd", "${secondmonth}-${secondday}")
        fromdate.upto(todate) { it  ->
            datevalue = "${it.format('MMM dd')}"
            println datevalue
            monthAndDayMatch(full_data,datevalue)
        }
    }
}

def monthandmonthrangefunction(full_data, date_string ) {
    def date_input = date_string =~ /(?i)\b(\S+)\b\s*\b\:\b(\S+)\b\s*\b/
    println date_input
    if (date_input.matches()) {
        firstmonth = date_input[0][1].toString()
        secondmonth = date_input[0][2].toString()
        def firstday
        if ( (firstday.equals(null))) {
            firstday = "1"
        }
        def fromdate = Date.parse("MMM-dd", "${firstmonth}-${firstday}")
        if (monthAcronymDayCount.containsKey(secondmonth)) {
            println (monthAcronymDayCount[secondmonth])
            secondday = monthAcronymDayCount[secondmonth]
            println secondday
        }

        secondday = monthAcronymDayCount[secondmonth]
        if ( (secondday.equals(null))) {
            secondday = monthFullNameDayCount[secondmonth]
        }

        def todate = Date.parse("MMM-dd", "${secondmonth}-${secondday}")
        fromdate.upto(todate) { it  ->
            datevalue = "${it.format('MMM dd')}"
            monthAndDayMatch(full_data,datevalue)
        }
    }
}

def fullDateMatch(data, dateString) {
    def dateInputMatch = dateString =~ /(?i)\b(\S+)\b\s+(\d+),\s*\b(\d{4})\b/ ;

    if (dateInputMatch.matches()) {
        month = dateInputMatch[0][1].toString()
        day = dateInputMatch[0][2].toInteger()
        year = dateInputMatch[0][3].toInteger()

        def dateInDataMatch = data =~ /(?i)\b(${month})\b\s+\b(${day})\b,\s*\b(${year})\b/ ;
        if (dateInDataMatch.find()) {
            if (dateInDataMatch.groupCount() == 3) {
                if (monthsFullNames.contains(month)) {
                    println ("In string.. ${data} ... Checking for Month ${month}, Day ${day}, Year ${year}....Total days in this month ${monthFullNameDayCount[month]}")
                    if (month == "February" && (year % 4) == 0) {
                        println "Handling 29 days in February on a leap year..."
                        if (day > 0 && day <= 29) {
                            println "MATCH1" ;
                            return "match" ;
                        }
                    } else if (day > 0 && day <= monthFullNameDayCount[month]) {
                        println "MATCH2" ;
                        return "match" ;
                    }
                } else if (monthsAcronym.contains(month)) {
                    println("In string.. ${data} ... Checking for Month ${month}, Day ${day}, Year ${year}....Total days in this month ${monthAcronymDayCount[month]}")
                    if (month == "Feb" && year % 4 == 0) {
                        println "Handling 29 days in Feb on a leap year..."
                        if (day > 0 && day <= 29) {
                            if (data =~ $ { month })
                                println "MATCH3";
                            return "match";
                        }
                    } else if (day > 0 && day <= monthAcronymDayCount[month]) {
                        println "MATCH4";
                        return "match";
                    }
                }
            }
        }
    }
}


def monthAndDayMatch(data, dateString) {
    def dateInputMatch = dateString =~ /(?i)\b(\S+)\b\s+(\d+)/;

    if (dateInputMatch.matches()) {
        month = dateInputMatch[0][1].toString()
        day = dateInputMatch[0][2].toInteger()

        def dateInDataMatch = data =~ /(?i)\b(${month})\b\s+\b(${day})\b/;
        if (dateInDataMatch.find()) {
            if (dateInDataMatch.groupCount() == 2) {
                if (monthsFullNames.contains(month)) {
                    println("In string.. ${data} ... Checking for Month ${month}, Day ${day}....Total days in this month ${monthFullNameDayCount[month]}")
                    if (month == "February") {
                        println "Handling 29 days in February on a leap year..."
                        if (day > 0 && day <= 29) {
                            println "MATCH";
                            return "match";
                        }
                    } else if (day > 0 && day <= monthFullNameDayCount[month]) {
                        println "MATCH";
                        return "match";
                    }
                } else if (monthsAcronym.contains(month)) {
                    println("In string.. ${data} ... Checking for Month ${month}, Day ${day}....Total days in this month ${monthAcronymDayCount[month]}")
                    if (month == "Feb") {
                        println "Handling 29 days in Feb on a leap year..."
                        if (day > 0 && day <= 29) {
                            println "MATCH";
                            return "match";
                        }
                    } else if (day > 0 && day <= monthAcronymDayCount[month]) {
                        println "MATCH";
                        return "match";
                    }
                }
            }
        }
    }
}​

