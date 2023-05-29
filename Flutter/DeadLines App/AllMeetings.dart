import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'main.dart';

class AllMeetings extends StatefulWidget {
  const AllMeetings({super.key});

  @override
  State<AllMeetings> createState() => _AllMeetingsState();
}

class _AllMeetingsState extends State<AllMeetings> {
  List list_all_meetings = [];
  final _firebase = FirebaseFirestore.instance;

  get_AllTasks() async {
    print(list_groups);
    for (var group in list_groups) {
      var meetings_group =
          await _firebase.collection('MeetingsDeadlines' + group).get();
      for (var meeting in meetings_group.docs) {
        if (meeting['Subject'] != '') {
          setState(() {
            list_all_meetings.add({
              'Subject': meeting['Subject'],
              'Description': meeting['Description'],
              'Deadline': meeting['Deadline'],
              'Group': group
            });
          });
        }
      }
    }
  }

  @override
  void initState() {
    get_AllTasks();
    super.initState();
  }

  String? key;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: darkTheme ? Colors.grey[900] : Colors.amber,
        title: Text('جميع الاجتماعات'),
        centerTitle: true,
      ),
      body: Container(
        width: double.infinity,
        height: double.infinity,
        child: ListView.builder(
            itemCount: list_all_meetings.length,
            itemBuilder: (context, i) {
              return ItemDesign(
                  title: list_all_meetings[i]['Subject'],
                  desc: list_all_meetings[i]['Description'],
                  Group: list_all_meetings[i]['Group'],
                  deadline: list_all_meetings[i]['Deadline'],
                  icon: Icons.meeting_room_outlined);
            }),
      ),
    );
  }
}

ItemDesign({title, desc, time, icon, Group, deadline}) {
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
                'Group: $Group',
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
