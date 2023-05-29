//import 'dart:html';

import 'package:flutter/material.dart';

String text = 'Hamborg';
int num = 3;
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
    return Scaffold(
      appBar: AppBar(),
      drawer: Drawer(),
      body: Container(
          width: double.infinity,
          height: double.infinity,
          child: Stack(children: [
            Container(
                width: double.infinity,
                height: double.infinity,
                child: Image(
                  image: AssetImage('images/map1.jpeg'),
                  fit: BoxFit.cover,
                )),
            Container(
                width: double.infinity,
                //margin: EdgeInsets.symmetric(horizontal: 20),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Container(
                        margin: EdgeInsets.only(top: 50),
                        width: 150,
                        height: 45,
                        alignment: Alignment.center,
                        padding:
                            EdgeInsets.symmetric(horizontal: 5, vertical: 5),
                        decoration: BoxDecoration(
                            color: Colors.amber,
                            borderRadius:
                                BorderRadius.all(Radius.circular(10))),
                        child: Text(
                          'اختر سيارتك',
                          style: TextStyle(color: Colors.black, fontSize: 25),
                        )),
                    Expanded(
                        child: Container(
                            alignment: Alignment.center,
                            margin: EdgeInsets.only(top: 10),
                            width: double.infinity,
                            height: 500,
                            child: SingleChildScrollView(
                                child: Column(
                              children: [
                                rowPattern(),
                                rowPattern(),
                                rowPattern()
                              ],
                            )))),
                    Bar(),
                  ],
                ))
          ])),
    );
  }
}

String? car;
rowPattern() {
  return Row(
    mainAxisAlignment: MainAxisAlignment.spaceAround,
    children: [
      Container(
          margin: EdgeInsets.symmetric(vertical: 10, horizontal: 10),
          height: 170,
          width: 170,
          decoration: BoxDecoration(
              boxShadow: [
                BoxShadow(color: Colors.amber, blurRadius: 10, spreadRadius: 3)
              ],
              color: Colors.white,
              borderRadius: BorderRadius.circular(10),
              border: Border.all(color: Colors.amber, width: 2)),
          child: Container(
            child: Column(children: [
              Expanded(
                  flex: 4,
                  child: Container(
                      child: Image(image: AssetImage('images/car1.png')))),
              Expanded(
                  child: Text(
                'سيارة خاصة',
                style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
              ))
            ]),
          )),
      Container(
          margin: EdgeInsets.symmetric(vertical: 10, horizontal: 10),
          height: 170,
          width: 170,
          decoration: BoxDecoration(
              boxShadow: [
                BoxShadow(color: Colors.amber, blurRadius: 10, spreadRadius: 3)
              ],
              color: Colors.white,
              borderRadius: BorderRadius.circular(10),
              border: Border.all(color: Colors.amber, width: 2)),
          child: Container(
            child: Column(children: [
              Expanded(
                  flex: 4,
                  child: Container(
                      child: Image(image: AssetImage('images/car1.png')))),
              Expanded(
                  child: Text(
                'سيارة مميزة',
                style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
              ))
            ]),
          ))
    ],
  );
}

Bar() {
  return Container(
    height: 50,
    width: double.infinity,
    decoration: BoxDecoration(color: Colors.amber),
    child: Row(mainAxisAlignment: MainAxisAlignment.spaceAround, children: [
      MaterialButton(
          onPressed: onClick,
          child: Column(
            children: [
              Icon(
                Icons.person,
                size: 28,
              ),
              Text('بياناتي')
            ],
          )),
      MaterialButton(
          onPressed: onClick,
          child: Column(
            children: [
              Icon(
                Icons.favorite,
                size: 28,
              ),
              Text('المفضلة')
            ],
          )),
      MaterialButton(
          onPressed: onClick,
          child: Column(
            children: [
              Icon(
                Icons.monetization_on,
                size: 28,
              ),
              Text('الدفع')
            ],
          )),
      MaterialButton(
          onPressed: onClick,
          child: Column(
            children: [
              Icon(
                color: Colors.white,
                Icons.home,
                size: 28,
              ),
              Text(
                'الرئيسية',
                style: TextStyle(color: Colors.white),
              )
            ],
          )),
    ]),
  );
}

onClick() {
  print('ok');
}
