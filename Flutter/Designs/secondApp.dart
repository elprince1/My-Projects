//import 'dart:html';

//import 'dart:js';

import 'package:flutter/material.dart';

main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  Widget build(BuildContext context) {
    return MaterialApp(home: HomePage());
  }
}

class HomePage extends StatelessWidget {
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(), drawer: const Drawer(), body: bodyDesign());
  }
}

bodyDesign() {
  return Container(
      child: SingleChildScrollView(
    scrollDirection: Axis.vertical,
    child: Column(mainAxisAlignment: MainAxisAlignment.spaceAround, children: [
      contPattern(),
      contPattern(),
      contPattern(),
      contPattern(),
      contPattern(),
      contPattern(),
      contPattern()
    ]),
  ));
}

contPattern() {
  return Container(
    margin: const EdgeInsets.symmetric(horizontal: 30, vertical: 20),
    height: 100,
    decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(15), color: Colors.amber),
    child: Row(mainAxisAlignment: MainAxisAlignment.spaceAround, children: [
      const Image(
        image: AssetImage('images/food1.png'),
        //width: 120,
        height: 130,
      ),
      Container(
        child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: const [
              Text(
                'Hamborg',
                style: TextStyle(fontWeight: FontWeight.bold),
              ),
              Text('\$24.00')
            ]),
      ),
      VerticalDivider(
        ,
      ),
      Container(
        child: MaterialButton(
            onPressed: onClick,
            child: Icon(
              Icons.add,
              size: 25,
            ),
            shape: CircleBorder()),
      ),
    ]),
  );
}

onClick() {
  print('added');
}
