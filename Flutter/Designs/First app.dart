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
    return Scaffold(appBar: AppBar(), drawer: const Drawer(), body: cont);
  }
}

Container cont = Container(
  margin: EdgeInsets.symmetric(horizontal: 30),
  child: Column(children: [
    Expanded(child: Container()),
    Column(mainAxisSize: MainAxisSize.max, children: [
      Container(
        width: double.infinity,
        height: 50,
        alignment: Alignment.center,
        //margin: const EdgeInsets.symmetric(horizontal: 30),
        decoration: BoxDecoration(
            color: Colors.blue,
            border: Border.all(width: 3, color: Colors.black)),
        child: const Text(
          'Strawberry pavlova Recipe',
          style: TextStyle(color: Colors.white, fontSize: 25),
        ),
      ),
      Container(
        height: 30,
      ),
      const Text(
        'Pavlova is a meringue-based dessert named after the Russian ballerina Anna Pavlova. Pavlova features a crisp crust and soft,light inside, topped with fruit and whipped cream',
        //textWidthBasis: TextWidthBasis.longestLine,
        style: TextStyle(fontFamily: 'arial', fontSize: 20),
        textAlign: TextAlign.center,
      ),
      Container(
        height: 30,
      ),
      Container(
        //margin: const EdgeInsets.symmetric(horizontal: 30),
        height: 200,
        decoration: BoxDecoration(
            border: Border.all(width: 1, color: Colors.black),
            color: const Color.fromARGB(255, 235, 220, 177)),
        child:
            Column(mainAxisAlignment: MainAxisAlignment.spaceAround, children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: [
              Row(
                children: const [
                  Icon(
                    Icons.star,
                    size: 25,
                    color: Colors.yellow,
                  ),
                  Icon(
                    Icons.star,
                    size: 25,
                    color: Colors.yellow,
                  ),
                  Icon(
                    Icons.star,
                    size: 25,
                    color: Colors.yellow,
                  ),
                  Icon(
                    Icons.star,
                    size: 25,
                    color: Colors.black,
                  ),
                  Icon(
                    Icons.star,
                    size: 25,
                    color: Colors.black,
                  )
                ],
              ),
              const Text(
                '17 review',
                style: TextStyle(fontSize: 25, fontFamily: 'arial'),
              )
            ],
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: [
              Column(
                children: const [
                  Icon(
                    Icons.restaurant,
                    color: Colors.green,
                    size: 50,
                  ),
                  Text(
                    'Feed',
                    style: TextStyle(fontSize: 20),
                  ),
                  Text('2-4', style: TextStyle(fontSize: 20))
                ],
              ),
              Column(
                children: const [
                  Icon(
                    Icons.grid_view,
                    color: Colors.green,
                    size: 50,
                  ),
                  Text(
                    'Feed',
                    style: TextStyle(fontSize: 20),
                  ),
                  Text('2-4', style: TextStyle(fontSize: 20))
                ],
              ),
              Column(
                children: const [
                  Icon(
                    Icons.coffee,
                    color: Colors.green,
                    size: 50,
                  ),
                  Text(
                    'Feed',
                    style: TextStyle(fontSize: 20),
                  ),
                  Text('2-4', style: TextStyle(fontSize: 20))
                ],
              ),
            ],
          )
        ]),
      ),
    ]),
    Expanded(child: Container()),
  ]),
);
