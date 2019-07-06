
from = -0.1
fromab  = from.abs()
to = 3
toab = to.abs()
fromab.upto(toab) { it ->
    println "${it}"
}


float y = -0.25
float x = 3.78
y.upto(x) { o ->
    println "${o}"
}​


