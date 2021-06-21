//Kotlin 1.1

fun main(args: Array<String>) {
  
    
    val thread = Thread {
    println("Thread Main has run.")
        for (i in 1..1000){
            println("$i: Main")
        }
}

    val thread2 = Thread {
    println("Thread Child 1 has run.")
        for (i in 1..1000){
            println("$i: Child 1")
            
        }
}
    val thread3 = Thread {
    println("Thread Child 2 has run.")
        for (i in 1..1000){
            println("$i: Child 2")
            
        }
}
val thread4 = Thread {
    println("Thread Child 3 has run.")
        for (i in 1..1000){
            println("$i: Child 3")
            
        }
}
thread.start()
thread2.start()
thread3.start()
thread4.start()
thread.join()
thread2.join()
thread3.join()
thread4.join()
}