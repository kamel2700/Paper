//'main' method must be in a class 'Rextester'.
//openjdk version '11.0.5' 

import java.util.*;
import java.lang.*;

class Rextester {
    public static void main (String[] args) {
        new SimpleThread("main").start();
        new SimpleThread("child1").start();
        new SimpleThread("child2").start();
        new SimpleThread("child3").start();
    }
}


class SimpleThread extends Thread {
    public SimpleThread(String str) {
        super(str);
    }
    public void run() {
        for (int i = 0; i < 1000; i++) {
            System.out.println(i + "step" + getName());
            
        }
        System.out.println("DONE! " + getName());
    }
}