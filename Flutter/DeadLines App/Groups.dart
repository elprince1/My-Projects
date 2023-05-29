import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:flutter_launcher_icons/xml_templates.dart';
import 'package:modal_progress_hud_nsn/modal_progress_hud_nsn.dart';
import 'main.dart';

class Groups extends StatefulWidget {
  const Groups({super.key});

  @override
  State<Groups> createState() => _GroupsState();
}

class _GroupsState extends State<Groups> {
  TextEditingController GroupNameCont = TextEditingController();
  TextEditingController GroupIDCont = TextEditingController();
  TextEditingController IDCont = TextEditingController();
  bool loading = false;
  final _firebase = FirebaseFirestore.instance;
  @override
  void initState() {
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: darkTheme ? Colors.grey[900] : Colors.amber,
        title: Text('مجموعاتي'),
        centerTitle: true,
      ),
      body: Directionality(
          textDirection: TextDirection.rtl,
          child: Container(
            child: Column(children: [
              Expanded(
                  child: ListView.builder(
                itemBuilder: (context, i) {
                  return Card(
                    child: Row(children: [
                      Icon(
                        Icons.people,
                        size: 30,
                      ),
                      Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            '  ${list_groups[i]}',
                            style: TextStyle(
                                fontSize: 18, fontWeight: FontWeight.bold),
                          ),
                          Text(
                            '  ${list_ids[i]}',
                            style: TextStyle(fontSize: 18),
                          )
                        ],
                      )
                    ]),
                  );
                },
                itemCount: list_groups.length,
              )),
              Container(
                margin: EdgeInsets.all(20),
                width: double.infinity,
                height: 40,
                child: Row(children: [
                  Expanded(
                      child: TextFormField(
                    controller: IDCont,
                    textDirection: TextDirection.ltr,
                    decoration: InputDecoration(
                        border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(10))),
                  )),
                  SizedBox(
                    width: 10,
                  ),
                  MaterialButton(
                    shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(10)),
                    color: darkTheme ? Colors.grey[900] : Colors.amber,
                    child: Text(
                      'اضافة',
                      style: TextStyle(fontSize: 18, color: Colors.white),
                    ),
                    onPressed: () async {
                      var groups = await _firebase.collection('Groups').get();
                      bool found = false;
                      for (var group in groups.docs) {
                        if (group['ID'] == IDCont.text) {
                          found = true;
                          // adding it to my groups
                          var people =
                              await _firebase.collection('Participants').get();

                          for (var person in people.docs) {
                            if (person['Email'] == userEmail) {
                              List list = person['Groups'];
                              if (!list.contains(group['Name'])) {
                                list.add(group['Name']);
                                _firebase
                                    .collection('Participants')
                                    .doc(person.id)
                                    .update({
                                  'Name': person['Name'],
                                  'Email': person['Email'],
                                  'Groups': list,
                                });
                                IDCont.clear();
                                setState(() {
                                  list_groups.add(group['Name']);
                                  list_ids.add(group['ID']);
                                });

                                return showDialog(
                                    context: context,
                                    builder: (context) {
                                      return Directionality(
                                          textDirection: TextDirection.rtl,
                                          child: AlertDialog(
                                            title: Text('تسجيل ناجح'),
                                            content: Text(
                                                'تمت اضافتك في المجموعة بنجاح'),
                                          ));
                                    });
                              } else {
                                return showDialog(
                                    context: context,
                                    builder: (context) {
                                      return Directionality(
                                          textDirection: TextDirection.rtl,
                                          child: AlertDialog(
                                            title: Text('تسجيل مرتين'),
                                            content: Text('أنت مسجل بالفعل'),
                                          ));
                                    });
                              }
                            }
                          }
                        }
                      }
                      if (!found) {
                        return showDialog(
                            context: context,
                            builder: (context) {
                              return Directionality(
                                  textDirection: TextDirection.rtl,
                                  child: AlertDialog(
                                    title: Text('تسجيل خاطيء'),
                                    content: Text('لا توجد مجموعة'),
                                  ));
                            });
                      }
                    },
                  ),
                ]),
              ),
              Container(
                  margin: EdgeInsets.symmetric(horizontal: 20),
                  width: double.infinity,
                  child: MaterialButton(
                    onPressed: () {
                      showModalBottomSheet(
                          context: context,
                          builder: (context) {
                            return ModalProgressHUD(
                                inAsyncCall: loading,
                                child: Directionality(
                                    textDirection: TextDirection.rtl,
                                    child: Container(
                                      margin: EdgeInsets.all(10),
                                      height: 215,
                                      width: double.infinity,
                                      child: Column(children: [
                                        TextField(
                                          controller: GroupNameCont,
                                          decoration: InputDecoration(
                                              hintText: 'اسم المجموعة',
                                              prefixIcon: Icon(Icons.people),
                                              border: OutlineInputBorder(
                                                  borderRadius:
                                                      BorderRadius.circular(
                                                          15))),
                                        ),
                                        SizedBox(
                                          height: 20,
                                        ),
                                        TextField(
                                          controller: GroupIDCont,
                                          keyboardType: TextInputType.number,
                                          decoration: InputDecoration(
                                              hintText: 'كود المجموعة',
                                              prefixIcon: Icon(Icons.code),
                                              border: OutlineInputBorder(
                                                  borderRadius:
                                                      BorderRadius.circular(
                                                          15))),
                                        ),
                                        SizedBox(
                                          height: 10,
                                        ),
                                        MaterialButton(
                                          color: Colors.grey[900],
                                          onPressed: () async {
                                            if (GroupIDCont.text != '' &&
                                                GroupNameCont.text != '') {
                                              setState(() {
                                                loading = true;
                                              });
                                              final groups = await _firebase
                                                  .collection('Groups')
                                                  .get();
                                              bool found = false;
                                              for (var group in groups.docs) {
                                                if (group['ID'] ==
                                                        GroupIDCont.text ||
                                                    group['Name'] ==
                                                        GroupNameCont.text) {
                                                  found = true;
                                                }
                                              }
                                              if (found) {
                                                showDialog(
                                                    context: context,
                                                    builder: (context) {
                                                      return Directionality(
                                                          textDirection:
                                                              TextDirection.rtl,
                                                          child: AlertDialog(
                                                            title: Text(
                                                                'لم تتم العملية'),
                                                            content: Text(
                                                                'هذه المجموعة موجودة مسبقا'),
                                                          ));
                                                    });
                                              } else {
                                                try {
                                                  var file = await _firebase
                                                      .collection('Groups');

                                                  file.add({
                                                    'ID': GroupIDCont.text,
                                                    'Name': GroupNameCont.text,
                                                  });

                                                  file = await _firebase
                                                      .collection(
                                                          'MeetingsDeadlines' +
                                                              GroupNameCont
                                                                  .text);
                                                  file.add({
                                                    'Deadline': '',
                                                    'Description': '',
                                                    'Subject': '',
                                                  });
                                                  file = await _firebase
                                                      .collection(
                                                          'TasksDeadlines' +
                                                              GroupNameCont
                                                                  .text);
                                                  file.add({
                                                    'Deadline': '',
                                                    'Description': '',
                                                    'Subject': '',
                                                  });
                                                  var users = await _firebase
                                                      .collection(
                                                          'Participants')
                                                      .get();
                                                  for (var user in users.docs) {
                                                    if (user['Email'] ==
                                                        userEmail) {
                                                      list_groups.add(
                                                          GroupNameCont.text);
                                                      _firebase
                                                          .collection(
                                                              'Participants')
                                                          .doc(user.id)
                                                          .update({
                                                        'Groups': list_groups
                                                      });
                                                    }
                                                  }
                                                  setState(() {
                                                    list_ids
                                                        .add(GroupIDCont.text);
                                                  });
                                                  showDialog(
                                                      context: context,
                                                      builder: (context) {
                                                        return Directionality(
                                                            textDirection:
                                                                TextDirection
                                                                    .rtl,
                                                            child: AlertDialog(
                                                              title: Text(
                                                                  'تمت العملية'),
                                                              content: Text(
                                                                  'تم انشاء المجموعة بنجاح'),
                                                            ));
                                                      });
                                                  GroupIDCont.text = '';
                                                  GroupNameCont.text = '';
                                                } catch (e) {
                                                  showDialog(
                                                      context: context,
                                                      builder: (context) {
                                                        return Directionality(
                                                            textDirection:
                                                                TextDirection
                                                                    .rtl,
                                                            child: AlertDialog(
                                                              title: Text(
                                                                  'لم تتم العملية'),
                                                              content: Text(
                                                                  'حدث خطأ'),
                                                            ));
                                                      });
                                                }
                                              }

                                              setState(() {
                                                loading = false;
                                              });
                                            }
                                          },
                                          child: Text(
                                            'انشاء المجموعة',
                                            style: TextStyle(
                                                fontSize: 18,
                                                color: Colors.white),
                                          ),
                                        )
                                      ]),
                                    )));
                          });
                    },
                    child: Text(
                      'انشاء مجموعة',
                      style: TextStyle(fontSize: 18, color: Colors.white),
                    ),
                    color: Colors.blue,
                  ))
            ]),
          )),
    );
  }
}
