object Main extends App {
   def specialMath(n: Int): BigInt = {
     if (n == 0)
        0 
     else if (n == 1)
        1
     else
        n + specialMath(n - 1) + specialMath(n - 2)
  }
  println( "specialMath of " + 17 + ": = " + specialMath(17) )
}
