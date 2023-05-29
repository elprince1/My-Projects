import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'main.dart';

class EndDone extends StatefulWidget {
  const EndDone({super.key});

  @override
  State<EndDone> createState() => _EndDoneState();
}

class _EndDoneState extends State<EndDone> {
  List list_ended_tasks = [];
  final _firebase = FirebaseFirestore.instance;
  bool found = false;
  getDoneTasks() async {
    try {
      if (!found) {
        var Tasks = await _firebase
            .collection('EndedTasks' + SignedGroup)
            .orderBy('Done')
            .get();
        for (var task in Tasks.docs) {
          setState(() {
            found = true;
            list_ended_tasks.add({
              'Description': task['Description'],
              'Subject': task['Subject'],
              'Deadline': task['Deadline'],
              'Done': task['Done']
            });
          });
        }
      } else {
        await for (var snapshot in _firebase
            .collection('EndedTasks' + SignedGroup)
            .orderBy('Done')
            .snapshots()) {
          setState(() {
            list_ended_tasks = snapshot.docs;
          });
        }
      }
    } catch (e) {
      print(e);
    }
  }

  @override
  void initState() {
    // TODO: implement initState
    print(1);
    getDoneTasks();
    print(2);
    super.initState();
  }

  String? key;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: darkTheme ? Colors.grey[900] : Colors.amber,
        title: Text('التسليمات المنتهية'),
        centerTitle: true,
      ),
      body: Container(
        width: double.infinity,
        height: double.infinity,
        child: ListView.builder(
            itemCount: list_ended_tasks.length,
            itemBuilder: (context, i) {
              return ItemDesign(
                  title: list_ended_tasks[i]['Subject'],
                  desc: list_ended_tasks[i]['Description'],
                  doneTime: list_ended_tasks[i]['Done'],
                  deadline: list_ended_tasks[i]['Deadline'],
                  icon: Icons.meeting_room_outlined);
            }),
      ),
    );
  }
}

ItemDesign({title, desc, doneTime, deadline, icon}) {
  return Card(
    margin: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
    child: Row(
      //mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        Expanded(
            child: Container(
                height: 90,
                child: Row(
                  children: [
                    Icon(
                      icon,
                      size: 60,
                    ),
                    Expanded(
                        child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Text(
                          '$title',
                          style: TextStyle(
                              fontSize: 18, fontWeight: FontWeight.bold),
                        ),
                        SizedBox(
                          height: 10,
                        ),
                        Text(
                          '$desc',
                          style: TextStyle(fontSize: 15),
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                        ),
                      ],
                    )),
                  ],
                ))),
        Container(
          margin: EdgeInsets.symmetric(horizontal: 10),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                'Done: $doneTime',
                style: TextStyle(fontSize: 15),
              ),
              SizedBox(
                height: 10,
              ),
              Text(
                'On: $deadline',
                style: TextStyle(fontSize: 15),
              ),
            ],
          ),
        )
      ],
    ),
  );
}

onClick() {
  print(1);
}
