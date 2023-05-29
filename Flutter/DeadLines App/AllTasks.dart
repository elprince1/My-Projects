import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'main.dart';

class AllTasks extends StatefulWidget {
  const AllTasks({super.key});

  @override
  State<AllTasks> createState() => _AllTasksState();
}

class _AllTasksState extends State<AllTasks> {
  List list_all_tasks = [];
  final _firebase = FirebaseFirestore.instance;

  get_AllTasks() async {
    print(list_groups);
    for (var group in list_groups) {
      var tasks_group =
          await _firebase.collection('TasksDeadlines' + group).get();
      for (var task in tasks_group.docs) {
        if (task['Subject'] != '') {
          setState(() {
            list_all_tasks.add({
              'Subject': task['Subject'],
              'Description': task['Description'],
              'Deadline': task['Deadline'],
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
        title: Text('جميع التسليمات'),
        centerTitle: true,
      ),
      body: Container(
        width: double.infinity,
        height: double.infinity,
        child: ListView.builder(
            itemCount: list_all_tasks.length,
            itemBuilder: (context, i) {
              return ItemDesign(
                  title: list_all_tasks[i]['Subject'],
                  desc: list_all_tasks[i]['Description'],
                  Group: list_all_tasks[i]['Group'],
                  deadline: list_all_tasks[i]['Deadline'],
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
