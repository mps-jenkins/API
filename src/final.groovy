
str1 = "Jazmyn Bieber_&_Jaxon Bieber" ;
assert str1 instanceof String ;
str2 = "jaxon  Too cute! Justin Bieber's adorable half-siblings, Jazmyn and Jaxon, obviously look up to their big brother, as evidenced by this tape of the two of them -- as well as ..."
assert str2 instanceof String ;

def testSwitch(val) {
    def result
    switch (val) {
        case "_&_":
            String[] split1 = str1.split("_&_")
            split1.each(this.&firstmethod)
        case "_AND_":
            String[] ans = str1.split('_AND_')
            break
        case "_|_":
            String[] ans = str1.split('_|_')
            break
        case "_OR_":
            String[] ans = str1.split('_OR_')
            break
        case "Date":
            break
        default:
            break
    }
}

class simple {

}


def firstmethod(s) {
    println "Groovy says: Hello ${s}!"
    def pattern = /(?i)\b${s}\b/
    def matcher = str2 =~ pattern
    if (matcher) {
        test_status = 'Passed';
        println test_status
        }else{
            test_status = 'Failed'
            println test_status
            }
    if ("Failed".equals(test_status)) {
        String[] split2 = s.split(' ')
        split2.each(this.&secondmethod)
        }
    }
def secondmethod(s1) {
    def pattern = /(?i)\b${s1}\b/
    def matcher = str2 =~ pattern
    if (matcher) {
        test_status = 'Passed';
        println test_status
    }else{
        test_status = 'Failed'
        println test_status
    }
}



testSwitch("_&_")
