

String str1 = "Jazmyn Bieber_|_Jaxon Bieber" ;
if (str1 =~ /\s+/) {
  if (str1 =~ /_AND_/ || str1 =~ /_&_/) {
    println "yes"
    println "yes to _&_"
  } else if (str1 =~ /_|_/ || str1 =~ /_OR_/) {
    println "yes to _|_ "
  }
}