class Vehicle {
    var currentSpeed = 0.0
    
    }
class Bicycle: Vehicle {
    var hasBasket = false
}
var array = [Bicycle]()
for item in 1...1000000 {
     
    array.append(Bicycle())
}
