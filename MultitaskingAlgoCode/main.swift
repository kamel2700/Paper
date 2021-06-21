//swift 5.1.5
import Foundation
import Dispatch

DispatchQueue.global(qos: .background).sync {
    for i in 0...1000 {
        print(String(i) + "child1")
        
    }
}
DispatchQueue.global(qos: .userInteractive).sync {
    for k in 0...1000 {
        print(String(k) + "main")
        
        
    }
}
DispatchQueue.global(qos: .background).sync {
    for i in 0...1000 {
        print(String(i) + "child2")
        
    }
}
DispatchQueue.global(qos: .background).sync {
    for i in 0...1000 {
        print(String(i) + "child3")
        
    }
}
