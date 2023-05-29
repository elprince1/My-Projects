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

String country = 'EGYPT';
bool BMW = false;
bool Mercedes = false;
bool Toyota = false;
String? Gender;

class _TestState extends State<Test> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(),
        drawer: Drawer(),
        body: Container(
          margin: EdgeInsets.only(left: 20, top: 20, right: 20),
          child: Column(children: [
            Text(
              'Choose Country',
              style: TextStyle(fontSize: 22),
            ),
            Expanded(
                flex: 3,
                child: Container(
                    margin: EdgeInsets.only(top: 10, bottom: 10),
                    decoration: BoxDecoration(
                        border: Border.all(width: 1, color: Colors.amber)),
                    //color: Colors.red,
                    height: 190,
                    child: SingleChildScrollView(
                        child: Column(children: [
                      RadioListTile(
                          isThreeLine: true,
                          title: Text('EGYPT'),
                          subtitle: Text('EG'),
                          secondary: Icon(Icons.flag),
                          value: "EGYPT",
                          groupValue: country,
                          onChanged: (val) {
                            setState(() {
                              country = val!;
                            });
                          }),
                      RadioListTile(
                          isThreeLine: true,
                          title: Text('SAUDIA'),
                          subtitle: Text('SA'),
                          secondary: Icon(Icons.flag),
                          value: "SAUDIA",
                          groupValue: country,
                          onChanged: (val) {
                            setState(() {
                              country = val!;
                            });
                          }),
                      RadioListTile(
                          isThreeLine: true,
                          title: Text('EMARATE'),
                          subtitle: Text('EM'),
                          secondary: Icon(Icons.flag),
                          value: "EGYPTEMARATE",
                          groupValue: country,
                          onChanged: (val) {
                            setState(() {
                              country = val!;
                            });
                          })
                    ])))),
            Text(
              'Choose Car',
              style: TextStyle(fontSize: 22),
            ),
            Expanded(
                flex: 3,
                child: Container(
                    margin: EdgeInsets.only(top: 10, bottom: 10),
                    height: 190,
                    decoration: BoxDecoration(
                        border: Border.all(width: 1, color: Colors.red)),
                    child: SingleChildScrollView(
                      child: Column(children: [
                        CheckboxListTile(
                            isThreeLine: true,
                            title: Text('BMW'),
                            subtitle: Text('2022'),
                            secondary: Icon(Icons.car_rental_rounded),
                            value: BMW,
                            onChanged: (val) {
                              setState(() {
                                BMW = val!;
                              });
                            }),
                        CheckboxListTile(
                            isThreeLine: true,
                            title: Text('Mercedes'),
                            subtitle: Text('2023'),
                            secondary: Icon(Icons.car_rental_rounded),
                            value: Mercedes,
                            onChanged: (val) {
                              setState(() {
                                Mercedes = val!;
                              });
                            }),
                        CheckboxListTile(
                            isThreeLine: true,
                            title: Text('Toyota'),
                            subtitle: Text('2021'),
                            secondary: Icon(Icons.car_rental_rounded),
                            value: Toyota,
                            onChanged: (val) {
                              setState(() {
                                Toyota = val!;
                              });
                            })
                      ]),
                    ))),
            Expanded(
                flex: 1,
                child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Expanded(
                          child: Container(
                        //color: Colors.red,
                        margin: EdgeInsets.only(left: 20, bottom: 15),
                        alignment: Alignment.bottomLeft,
                        child: DropdownButtonHideUnderline(
                            child: DropdownButton(
                          hint: Container(
                            child: Text('Gender'),
                            margin: EdgeInsets.only(left: 10),
                          ),
                          items: ['Male', 'Female']
                              .map((e) => DropdownMenuItem(
                                    child: Container(
                                      child: Text('$e'),
                                      margin: EdgeInsets.only(left: 10),
                                    ),
                                    value: e,
                                  ))
                              .toList(),
                          onChanged: (val) {
                            setState(() {
                              Gender = val;
                            });
                          },
                          value: Gender,
                        )),
                      )),
                      Container(
                          margin: EdgeInsets.only(bottom: 15),
                          alignment: Alignment.bottomRight,
                          child: MaterialButton(
                            minWidth: 200,
                            height: 50,
                            onPressed: onClick,
                            child: Text('OK'),
                            color: Colors.amber,
                          ))
                    ]))
          ]),
        ));
  }
}

onClick() {
  print(Mercedes);
  print(BMW);
  print(Toyota);
  print(country);
  print(Gender);
}
