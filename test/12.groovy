
import java.util.regex.Matcher
import java.util.regex.Pattern

String str1 = "Jazmyn Bieber_&_Jaxon Bieber" ;
def ans = str1.split("_&_")

ans.each { println  'Normal closure says: Hello ' + it + '!'  }


def groovySays(s) {
    println "Groovy says: Hello ${s}!"
}
ans.each(this.&groovySays)