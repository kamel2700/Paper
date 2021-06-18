open class BaseClass(){
    var a = 1
}
class ChildClass:BaseClass(){
    var b = 2
}
fun main(args: Array<String>)
{
    val a: MutableList<ChildClass> = mutableListOf()
    for (i in 0..1000000){
        a.add(ChildClass())
    }
}