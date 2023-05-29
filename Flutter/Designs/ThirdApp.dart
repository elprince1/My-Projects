//import 'dart:html';

//import 'dart:js';

import 'package:flutter/material.dart';

String text = 'Hamborg';
main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  Widget build(BuildContext context) {
    return MaterialApp(home: Test());
  }
}

class Test extends StatefulWidget {
  const Test({super.key});

  @override
  State<Test> createState() => _TestState();
}

class _TestState extends State<Test> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(), drawer: Drawer(), body: appDesign());
  }
}

appDesign() {
  return Container(
    child: Column(mainAxisAlignment: MainAxisAlignment.start, children: [
      Expanded(
          child: Container(
        decoration: BoxDecoration(
            color: Color.fromARGB(255, 247, 65, 52),
            borderRadius:
                BorderRadius.vertical(bottom: Radius.elliptical(300, 150))),
        width: double.infinity,
        height: 300,
        child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
          Image(
            image: AssetImage('images/food1.png'),
            //width: 180,
            height: 200,
          ),
          Text(
            'Restaurant',
            style: TextStyle(
                color: Colors.white, fontSize: 25, fontWeight: FontWeight.bold),
          )
        ]),
      )),
      Expanded(
          child: Column(mainAxisAlignment: MainAxisAlignment.start, children: [
        Container(
            margin: EdgeInsets.only(top: 50),
            alignment: Alignment.center,
            child: MaterialButton(
                elevation: 5,
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(30)),
                color: Colors.red,
                textColor: Colors.white,
                minWidth: 250,
                onPressed: () {
                  print('ok');
                },
                child: Text('SIGN UP'))),
        Container(
            margin: EdgeInsets.only(top: 20),
            alignment: Alignment.center,
            child: MaterialButton(
                elevation: 5,
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(30)),
                color: Colors.grey,
                textColor: Colors.white,
                minWidth: 250,
                onPressed: () {
                  print('ok');
                },
                child: Text('SIGN IN'))),
      ]))
    ]),
  );
}
