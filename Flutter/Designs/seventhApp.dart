//import 'dart:html';

import 'package:flutter/material.dart';

main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  Widget build(BuildContext context) {
    return MaterialApp(debugShowCheckedModeBanner: false, home: Test());
  }
}

class Test extends StatefulWidget {
  const Test({super.key});

  @override
  State<Test> createState() => _TestState();
}

int counter = 1;

class _TestState extends State<Test> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        color: Colors.white,
        child: Column(children: [
          nameBar(),
          ActivePeople(),
          Expanded(
              child: Container(
            child: SingleChildScrollView(
                child: Column(
              children: [
                OldChat(image: 'images/logo.jpg'),
                OldChat(image: 'images/logo.jpg'),
                OldChat(image: 'images/logo.jpg'),
                OldChat(image: 'images/logo.jpg'),
                OldChat(image: 'images/logo.jpg'),
                OldChat(image: 'images/logo.jpg'),
              ],
            )),
          )),
          Footer(),
        ]),
      ),
    );
  }
}

nameBar() {
  return Container(
      margin: EdgeInsets.symmetric(horizontal: 20, vertical: 10),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Expanded(
              child: Container(
                  child: Column(
            children: [
              Container(
                  alignment: Alignment.topLeft,
                  child: Text(
                    'Hi,Moustafa',
                    style: TextStyle(color: Colors.grey),
                  )),
              Container(
                  alignment: Alignment.topLeft,
                  child: Text('Welcome back!',
                      style:
                          TextStyle(fontSize: 17, fontWeight: FontWeight.bold)))
            ],
          ))),
          Container(
            width: 40,
            height: 40,
            decoration: BoxDecoration(
                boxShadow: [
                  BoxShadow(color: Colors.grey, blurRadius: 5, spreadRadius: 1)
                ],
                borderRadius: BorderRadius.circular(15),
                image: DecorationImage(
                    image: AssetImage('images/logo.jpg'), fit: BoxFit.fill)),
          )
        ],
      ));
}

ActivePeople() {
  return Container(
    margin: EdgeInsets.symmetric(horizontal: 20),
    child: SingleChildScrollView(
        scrollDirection: Axis.horizontal,
        child: Row(mainAxisAlignment: MainAxisAlignment.center, children: [
          ActiveOne(
              child: Icon(
                Icons.person,
                color: Colors.white,
              ),
              name: 'Invite'),
          ActiveOne(child: faceActive('images/logo.jpg'), name: 'Mohamed'),
          ActiveOne(child: faceActive('images/logo.jpg'), name: 'Khaled'),
          ActiveOne(child: faceActive('images/logo.jpg'), name: 'Ahmed'),
          ActiveOne(child: faceActive('images/logo.jpg'), name: 'Ali'),
          ActiveOne(child: faceActive('images/logo.jpg'), name: 'prince'),
        ])),
  );
}

ActiveOne({child, name}) {
  return Container(
      width: 70,
      margin: EdgeInsets.only(top: 20),
      child: Column(
        children: [
          CircleAvatar(backgroundColor: Colors.black, child: child),
          Container(margin: EdgeInsets.only(top: 5), child: Text('$name')),
        ],
      ));
}

faceActive(image) {
  return Container(
    width: 50,
    height: 50,
    decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(30),
        image: DecorationImage(image: AssetImage(image), fit: BoxFit.fill)),
  );
}

OldChat({image}) {
  return Container(
    margin: EdgeInsets.symmetric(vertical: 10, horizontal: 20),
    child: Row(mainAxisAlignment: MainAxisAlignment.start, children: [
      InkWell(
          child: Container(
        width: 60,
        height: 60,
        decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(30),
            image: DecorationImage(image: AssetImage(image), fit: BoxFit.fill)),
      )),
      Expanded(
          child: Container(
              margin: EdgeInsets.only(left: 15),
              alignment: Alignment.centerLeft,
              child: Column(
                mainAxisAlignment: MainAxisAlignment.start,
                children: [
                  Container(
                    width: double.maxFinite,
                    child: Text(
                      'Mohamed',
                      style:
                          TextStyle(fontSize: 19, fontWeight: FontWeight.bold),
                    ),
                  ),
                  Container(
                    width: double.maxFinite,
                    child: Text(
                      'how are you?',
                      style: TextStyle(fontSize: 16),
                    ),
                  )
                ],
              )))
    ]),
  );
}

Footer() {
  return Container(
    height: 50,
    decoration: BoxDecoration(
        border: Border.all(color: Colors.grey, width: 1),
        borderRadius: BorderRadius.vertical(top: Radius.circular(20))),
    child: Row(mainAxisAlignment: MainAxisAlignment.spaceAround, children: [
      IconButton(
          onPressed: onClick,
          icon: Icon(
            Icons.chat,
            size: 30,
          )),
      IconButton(
          onPressed: onClick,
          icon: Icon(
            Icons.mic,
            size: 30,
          )),
      IconButton(
          onPressed: onClick,
          icon: Icon(
            Icons.people,
            size: 30,
          )),
      IconButton(
          onPressed: onClick,
          icon: Icon(
            Icons.store_mall_directory,
            size: 30,
          ))
    ]),
  );
}

onClick() {
  print('1');
}
