String str1 = "Jazmyn Bieber_&_Jaxon Bieber" ;
String[] ans = str1.split('_&_') ;
String str2 = "jaxon  Too cute! Justin Bieber's adorable half-siblings, Jazmyn and Jaxon, obviously look up to their big brother, as evidenced by this tape of the two of them -- as well as ..."


// loop through splitted string
ans.each { number ->
    println number
    def pattern = /(?i)\b${number}\b/
    def matcher = str2 =~ pattern
     if (matcher) {
        test_status = 'Passed';
     } else {
        test_status = 'Failed'
     }
       if ("Failed".equals(test_status)){
           // split each value of string and looping through each word of a value
          String[] ans1 = number.split(' ');
          ans1.each { value ->
          def pattern1 = /\b${value}\b/
          def matcher1 = str2 =~ pattern1
          if (matcher1) {
             test_status = 'Passed';
             if ("Passed".equals(test_status)) {
                println test_status
                println  ("matched value" + value )

             }else {

             }
            } else {
                test_status = 'Failed'
                println("inside now status" + test_status);
            }
        }
    }
}
