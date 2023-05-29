import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'main.dart';

class EndMeet extends StatefulWidget {
  const EndMeet({super.key});

  @override
  State<EndMeet> createState() => _EndMeetState();
}

class _EndMeetState extends State<EndMeet> {
  List list_ended_meetings = [];
  final _firebase = FirebaseFirestore.instance;
  bool found = false;
  getDoneMeetings() async {
    try {
      if (!found) {
        // await for (var snapshot in _firestore
        //     .collection('MeetingsDeadlines' + SignedGroup)
        //     .snapshots()) {
        //   setState(() {
        //     list_meetings = snapshot.docs;
        //   });
        // }
        var meetings = await _firebase
            .collection('EndedMeetings' + SignedGroup)
            .orderBy('Done')
            .get();
        for (var meet in meetings.docs) {
          setState(() {
            found = true;
            list_ended_meetings.add({
              'Description': meet['Description'],
              'Subject': meet['Subject'],
              'Deadline': meet['Deadline'],
              'Done': meet['Done']
            });
          });
        }
      } else {
        await for (var snapshot in _firebase
            .collection('EndedMeetings' + SignedGroup)
            .orderBy('Done')
            .snapshots()) {
          setState(() {
            list_ended_meetings = snapshot.docs;
          });
        }
      }
    } catch (e) {
      print(e);
    }
  }

  @override
  void initState() {
    getDoneMeetings();
    super.initState();
  }

  String? key;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: darkTheme ? Colors.grey[900] : Colors.amber,
        title: Text('الاجتماعات المنتهية'),
        centerTitle: true,
      ),
      body: Container(
        width: double.infinity,
        height: double.infinity,
        child: ListView.builder(
            itemCount: list_ended_meetings.length,
            itemBuilder: (context, i) {
              return ItemDesign(
                  title: list_ended_meetings[i]['Subject'],
                  desc: list_ended_meetings[i]['Description'],
                  doneTime: list_ended_meetings[i]['Done'],
                  deadline: list_ended_meetings[i]['Deadline'],
                  icon: Icons.meeting_room_outlined);
            }),
      ),
    );
  }
}

ItemDesign({title, desc, time, icon, doneTime, deadline}) {
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
