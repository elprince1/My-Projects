import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'main.dart';

class Participants extends StatefulWidget {
  const Participants({super.key});

  @override
  State<Participants> createState() => _ParticipantsState();
}

class _ParticipantsState extends State<Participants> {
  @override
  Widget build(BuildContext context) {
    @override
    void initState() {
      super.initState();
    }

    return Scaffold(
      appBar: AppBar(
        backgroundColor: darkTheme ? Colors.grey[900] : Colors.amber,
        title: Text('المشاركين'),
        centerTitle: true,
      ),
      body: Container(
        margin: EdgeInsets.symmetric(horizontal: 20, vertical: 20),
        width: double.infinity,
        height: double.infinity,
        child: ListView.separated(
          itemCount: People.length,
          itemBuilder: (context, i) {
            return Item(color: Colors.amber, name: People[i]);
          },
          separatorBuilder: (context, index) {
            return SizedBox(
              height: 10,
            );
          },
        ),
      ),
    );
  }
}

Item({color, name}) {
  return Row(
    mainAxisAlignment: MainAxisAlignment.end,
    children: [
      Text(
        '$name',
        style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
      ),
      SizedBox(
        width: 10,
      ),
      CircleAvatar(
        backgroundColor: color,
        radius: 25,
        child: Icon(
          Icons.person,
          color: Colors.white,
          size: 30,
        ),
      )
    ],
  );
}
