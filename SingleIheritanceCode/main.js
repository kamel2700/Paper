class ClassA {
    constructor(){
        this.name ="classA"
    
    };
    }
class ClassB extends ClassA {
    constructor(){
        super();
        this.name1 ="classB"
    
    };
    }

let array = new Array(1000000);
for (let i =0; i< 1000000; i++){
    array[i] = new ClassB();
    

}
