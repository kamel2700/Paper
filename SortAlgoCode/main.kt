fun main(args: Array<String>) {
    

    var array : List<Int> = List(10000) { kotlin.random.Random.nextInt(1, 1000) }
   
    array = array.sorted()
  


}