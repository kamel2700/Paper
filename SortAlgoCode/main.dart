import 'dart:math';

main() {
  var rng = new Random();
  var myList = new List(10000);
  for (var i = 0; i < 10000; i++) {
    myList[i] = rng.nextInt(1000);
  }
  myList.sort();
 
}