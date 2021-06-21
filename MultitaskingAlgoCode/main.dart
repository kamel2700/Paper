Future<void> printOrderMessage() async {
  for (var i = 1; i <= 1000; i++) {
  
      print(i);
  }
 // var order = await fetchUserOrder();
 // print('Your order is: $order');
}

Future<void> printOrderMessage1() async {
  for (var i = 1; i <= 1000; i++) {
  
      print(i);
  }
 // var order = await fetchUserOrder();
 // print('Your order is: $order');
}
Future<void> printOrderMessage2() async {
  for (var i = 1; i <= 1000; i++) {
  
      print(i);
  }
 // var order = await fetchUserOrder();
 // print('Your order is: $order');
}
Future<void> printOrderMessage3() async {
  for (var i = 1; i <= 1000; i++) {
  
      print(i);
  }
 // var order = await fetchUserOrder();
 // print('Your order is: $order');
}

Future<String> fetchUserOrder() {
  // Imagine that this function is more complex and slow.
  return Future.delayed(Duration(milliseconds: 1), () => 'Large Latte');
}

Future<void> main() async {
  //countSeconds();
  printOrderMessage();
  printOrderMessage1();
  printOrderMessage2();
  printOrderMessage3();
}

// You can ignore this function - it's here to visualize delay time in this example.
/*void countSeconds() {
  for (var i = 1; i <= 1000; i++) {
    Future.delayed(Duration(milliseconds: 1), () => print(i));
  }
}*/