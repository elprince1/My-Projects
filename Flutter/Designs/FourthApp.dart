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
    return Scaffold(appBar: AppBar(), drawer: Drawer(), body: appDesign());
  }
}

appDesign() {
  return Container(
      width: double.infinity,
      decoration: BoxDecoration(color: Colors.amber),
      child: Column(
        children: [
          Container(
              margin: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: const [
                  Icon(
                    Icons.arrow_back_rounded,
                    size: 35,
                    color: Colors.white,
                  ),
                  Icon(
                    Icons.add_business_outlined,
                    size: 35,
                    color: Colors.white,
                  )
                ],
              )),
          const Image(
            image: AssetImage('images/food1.png'),
            height: 150,
          ),
          Expanded(
              child: Container(
            margin: EdgeInsets.only(top: 30),
            width: double.infinity,
            height: 300,
            decoration: BoxDecoration(
                boxShadow: [
                  BoxShadow(
                      blurRadius: 2,
                      spreadRadius: 1,
                      color: Color.fromARGB(255, 206, 156, 8))
                ],
                color: Colors.white,
                borderRadius: BorderRadius.vertical(top: Radius.circular(50))),
            child: Column(children: [
              Container(
                margin: EdgeInsets.only(left: 20, top: 20),
                alignment: Alignment.topLeft,
                child: Text(
                  'Hamborg',
                  style: TextStyle(fontWeight: FontWeight.bold, fontSize: 25),
                ),
              ),
              Container(
                margin: EdgeInsets.only(left: 20),
                alignment: Alignment.topLeft,
                child: Text(
                  '1 each',
                  style: TextStyle(fontSize: 15),
                ),
              ),
              Container(
                  margin: EdgeInsets.only(left: 20),
                  alignment: Alignment.topLeft,
                  child: Row(
                    children: [
                      Container(
                        margin: EdgeInsets.only(top: 10),
                        width: 140,
                        height: 35,
                        decoration: BoxDecoration(
                            borderRadius: BorderRadius.all(Radius.circular(30)),
                            color: Color.fromARGB(255, 201, 200, 200)),
                        child: Row(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              MaterialButton(
                                  shape: CircleBorder(),
                                  minWidth: 50,
                                  onPressed: addCom,
                                  child: Icon(Icons.add)),
                              Text(
                                '$num',
                                style: TextStyle(fontSize: 18),
                              ),
                              MaterialButton(
                                  shape: CircleBorder(),
                                  minWidth: 50,
                                  onPressed: addCom,
                                  child: Icon(Icons.remove)),
                            ]),
                      ),
                      Expanded(
                          child: Container(
                        alignment: Alignment.center,
                        padding: EdgeInsets.only(top: 5, left: 60),
                        child: Text(
                          'Rs 30',
                          style: TextStyle(
                              fontWeight: FontWeight.bold, fontSize: 22),
                        ),
                      ))
                    ],
                  )),
              Container(
                margin: EdgeInsets.only(left: 20, top: 10),
                alignment: Alignment.topLeft,
                child: Text(
                  'Product Description',
                  style: TextStyle(fontWeight: FontWeight.bold, fontSize: 15),
                ),
              ),
              Expanded(
                  child: Container(
                margin: EdgeInsets.only(left: 20, top: 10, right: 20),
                child: Text(
                  'A mango is a type of fruit. The mango tree is native to South Asia, from Where it has been taken to become one of the most widely cultivated fruits in the tropics. It is harvested in the month of march ( summer season ) till the end of May.',
                  textAlign: TextAlign.justify,
                ),
              )),
              Container(
                  margin: EdgeInsets.only(top: 10, bottom: 10),
                  child: Row(
                    children: [
                      Expanded(
                          flex: 2,
                          child: Container(
                            margin: EdgeInsets.only(left: 20),
                            child: MaterialButton(
                              height: 50,
                              shape: RoundedRectangleBorder(
                                  borderRadius: BorderRadius.circular(15)),
                              child: Icon(
                                Icons.favorite,
                                size: 35,
                                color: Colors.amber,
                              ),
                              onPressed: addCom,
                            ),
                          )),
                      Spacer(
                        flex: 1,
                      ),
                      Expanded(
                          flex: 5,
                          child: Container(
                            margin: EdgeInsets.only(right: 20),
                            child: MaterialButton(
                              height: 50,
                              child: Text('Add To Card'),
                              color: Colors.amber,
                              shape: RoundedRectangleBorder(
                                  borderRadius: BorderRadius.circular(10)),
                              onPressed: addCom,
                            ),
                          ))
                    ],
                  ))
            ]),
          ))
        ],
      ));
}

addCom() {
  print('add');
}
