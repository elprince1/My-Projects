import 'dart:convert';

import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:modal_progress_hud_nsn/modal_progress_hud_nsn.dart';
import 'main.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:date_time_picker/date_time_picker.dart';
import 'package:http/http.dart' as http;

String? Subject;
String? Description;
String? Deadline;

var selected;
TextEditingController? subjectCont;
TextEditingController? descriptionCont;
TextEditingController? deadlineCont;
int? modified;

class AddTaskMeet extends StatefulWidget {
  AddTaskMeet(
      {type = 'تاسك',
      subject = '',
      description = '',
      deadline = '',
      modify = 1}) {
    subjectCont = TextEditingController(text: subject);
    descriptionCont = TextEditingController(text: description);
    deadlineCont = TextEditingController(text: deadline);
    selected = type;
    modified = modify;
    Subject = subject;
    Description = description;
    Deadline = deadline;
  }

  @override
  State<AddTaskMeet> createState() => _AddTaskMeetState();
}

class _AddTaskMeetState extends State<AddTaskMeet> {
  final _fireStore = FirebaseFirestore.instance;

  bool saving = false;

  sendPushMessage(String token, String body, String title) async {
    try {
      await http.post(
        Uri.parse('https://fcm.googleapis.com/fcm/send'),
        headers: <String, String>{
          'Content-Type': 'application/json',
          'Authorization': 'key=eeab8289-8802-4197-a197-03c7b312a8a9'
        },
        body: jsonEncode(<String, dynamic>{
          'priority': 'high',
          'data': <String, dynamic>{
            'click_action': 'FLUTTER_NOTIFICATION_CLICK',
            'status': 'done',
            'body': body,
            'title': title,
          },
          "notification": <String, dynamic>{
            "title": title,
            'body': body,
            'android_channel_id': 'dbfood'
          },
          'to': token,
        }),
      );
    } catch (e) {
      if (kDebugMode) {
        print('error push notification');
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          icon: Icon(Icons.arrow_back_sharp),
          onPressed: () {
            Navigator.of(context)
                .pushReplacement(MaterialPageRoute(builder: (context) {
              return Test();
            }));
          },
        ),
        backgroundColor: darkTheme ? Colors.grey[900] : Colors.amber,
        title: Text('اضافة'),
        centerTitle: true,
      ),
      body: Container(
        margin: EdgeInsets.symmetric(horizontal: 20, vertical: 10),
        width: double.infinity,
        height: double.infinity,
        child: ModalProgressHUD(
            inAsyncCall: saving,
            child: Directionality(
                textDirection: TextDirection.rtl,
                child: SingleChildScrollView(
                  child: Column(
                    children: [
                      Icon(
                        Icons.timelapse_outlined,
                        size: 50,
                      ),
                      Text(
                        'مواعيد التسليم',
                        style: TextStyle(
                            fontSize: 20, fontWeight: FontWeight.bold),
                      ),
                      Row(
                        children: [
                          Text(
                            'النوع',
                            style: TextStyle(fontSize: 18),
                          ),
                          SizedBox(
                            width: 20,
                          ),
                          Expanded(
                              child: DropdownButton(
                            isExpanded: true,
                            items: ['تاسك', 'اجتماع']
                                .map((e) => DropdownMenuItem(
                                      child: Text(
                                        e,
                                        style: TextStyle(fontSize: 18),
                                      ),
                                      value: e,
                                    ))
                                .toList(),
                            onChanged: (val) {
                              if (modified == 1) {
                                setState(() {
                                  selected = val!;
                                });
                              }
                            },
                            value: selected,
                          )),
                        ],
                      ),
                      Row(
                        children: [
                          Text(
                            'المادة',
                            style: TextStyle(fontSize: 18),
                          ),
                          SizedBox(
                            width: 20,
                          ),
                          Expanded(
                              child: TextFormField(
                            controller: subjectCont,
                          )),
                        ],
                      ),
                      Row(
                        children: [
                          Text(
                            'الوصف',
                            style: TextStyle(fontSize: 18),
                          ),
                          SizedBox(
                            width: 20,
                          ),
                          Expanded(
                              child: TextFormField(
                            controller: descriptionCont,
                            maxLines: 5,
                          )),
                        ],
                      ),
                      SizedBox(
                        height: 10,
                      ),
                      Row(
                        children: [
                          Text(
                            'وقت التسليم',
                            style: TextStyle(fontSize: 18),
                          ),
                          SizedBox(
                            width: 20,
                          ),
                          Expanded(
                              child: TextFormField(
                            onTap: () {
                              showModalBottomSheet(
                                  context: context,
                                  builder: (context) {
                                    return Container(
                                        margin: EdgeInsets.symmetric(
                                            horizontal: 10),
                                        child: Directionality(
                                            textDirection: TextDirection.rtl,
                                            child: DateTimePicker(
                                              type: DateTimePickerType
                                                  .dateTimeSeparate,
                                              dateMask: 'd MMM, yyyy',
                                              initialValue:
                                                  DateTime.now().toString(),
                                              firstDate:
                                                  DateTime(DateTime.now().year),
                                              lastDate: DateTime(2100),
                                              icon: Icon(Icons.event),
                                              dateLabelText: 'التاريخ',
                                              timeLabelText: "الساعة",
                                              onChanged: (value) {
                                                deadlineCont?.text = value;
                                              },

                                              // onSaved: (val) {
                                              //   print(val);
                                              //   deadlineCont?.text = val!;
                                              // },
                                            )));
                                  });
                            },
                            readOnly: true,
                            controller: deadlineCont,
                            keyboardType: TextInputType.datetime,
                          )),
                        ],
                      ),
                      SizedBox(
                        height: 10,
                      ),
                      MaterialButton(
                        onPressed: () async {
                          //

                          // final persons =
                          //     await _fireStore.collection('Participants').get();
                          // for (var person in persons.docs) {
                          //   print(person['Name']);
                          //   sendPushMessage(person['Token'], 'ok', 'ok yahh');
                          // }
                          //
                          if (modified == 1) {
                            if (subjectCont!.text != '' &&
                                descriptionCont!.text != '' &&
                                deadlineCont!.text != '') {
                              setState(() {
                                saving = true;
                              });
                              if (selected == 'تاسك') {
                                try {
                                  await _fireStore
                                      .collection(
                                          'TasksDeadlines' + SignedGroup)
                                      .add({
                                    'Subject': subjectCont!.text,
                                    'Description': descriptionCont!.text,
                                    'Deadline': deadlineCont!.text,
                                  });
                                } catch (e) {
                                  print(e);
                                }
                              } else {
                                try {
                                  await _fireStore
                                      .collection(
                                          'MeetingsDeadlines' + SignedGroup)
                                      .add({
                                    'Subject': subjectCont!.text,
                                    'Description': descriptionCont!.text,
                                    'Deadline': deadlineCont!.text,
                                  });
                                } catch (e) {
                                  print(e);
                                }
                              }

                              setState(() {
                                saving = false;
                              });

                              Navigator.of(context).pop();
                            }
                          } else {
                            if (subjectCont!.text != '' &&
                                descriptionCont!.text != '' &&
                                deadlineCont!.text != '') {
                              setState(() {
                                saving = true;
                              });
                              if (selected == 'تاسك') {
                                try {
                                  var tasks = await _fireStore
                                      .collection(
                                          'TasksDeadlines' + SignedGroup)
                                      .get();
                                  for (var task in tasks.docs) {
                                    if (task['Subject'] == Subject &&
                                        task['Deadline'] == Deadline &&
                                        task['Description'] == Description) {
                                      _fireStore
                                          .collection(
                                              'TasksDeadlines' + SignedGroup)
                                          .doc(task.id)
                                          .set({
                                        'Subject': subjectCont!.text,
                                        'Deadline': deadlineCont!.text,
                                        'Description': descriptionCont!.text,
                                      });
                                    }
                                  }
                                } catch (e) {
                                  print(e);
                                }
                              } else {
                                try {
                                  var meets = await _fireStore
                                      .collection(
                                          'MeetingsDeadlines' + SignedGroup)
                                      .get();
                                  for (var meet in meets.docs) {
                                    if (meet['Subject'] == Subject &&
                                        meet['Deadline'] == Deadline &&
                                        meet['Description'] == Description) {
                                      _fireStore
                                          .collection(
                                              'MeetingsDeadlines' + SignedGroup)
                                          .doc(meet.id)
                                          .set({
                                        'Subject': subjectCont!.text,
                                        'Deadline': deadlineCont!.text,
                                        'Description': descriptionCont!.text,
                                      });
                                    }
                                  }
                                } catch (e) {
                                  print(e);
                                }
                              }

                              setState(() {
                                saving = false;
                              });

                              Navigator.of(context).pop();
                            }
                          }
                        },
                        color: darkTheme ? Colors.grey[900] : Colors.amber,
                        shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(10)),
                        child: Text(
                          'اضافة',
                          style: TextStyle(color: Colors.white, fontSize: 18),
                        ),
                      ),
                      Container(
                        width: double.infinity,
                        height: 180,
                        decoration: BoxDecoration(
                            image: DecorationImage(
                                image: AssetImage('images/1.jpg'),
                                fit: BoxFit.cover)),
                      )
                    ],
                  ),
                ))),
      ),
    );
  }
}

onClick() {
  print(1);
}
