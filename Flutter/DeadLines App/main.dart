//import 'dart:html';
//eeab8289-8802-4197-a197-03c7b312a8a9
import 'package:Deadlines/AllMeetings.dart';
import 'package:Deadlines/AllTasks.dart';
import 'package:Deadlines/ChooseGroup.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/gestures.dart';

import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import 'package:flutter/services.dart';
import 'package:modal_progress_hud_nsn/modal_progress_hud_nsn.dart';

import 'package:Deadlines/EndDone.dart';
import 'package:Deadlines/SplashPage.dart';
import 'package:Deadlines/notification_api.dart';

import 'EndMeet.dart';
import 'Groups.dart';
import 'LoginPage.dart';
import 'SignupPage.dart';
import 'AddTaskMeet.dart';
import 'Participants.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_messaging/firebase_messaging.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';
import 'dart:async';
import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:http/http.dart' as http;
import 'package:timezone/data/latest.dart' as tz;

List list_ids = [];
List list_tasks = [];
List list_meetings = [];
List People = [];
List list_groups = [];
String userName = '';
String userEmail = '';
bool darkTheme = true;
String SignedGroup = '';

Future<void> _firebaseMessagingBackgroundHandler(RemoteMessage message) async {
  // If you're going to use other Firebase services in the background, such as Firestore,
  // make sure you call `initializeApp` before using other Firebase services.
  await Firebase.initializeApp();
  print('Handling a background message ${message.messageId}');
}

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();

  await Firebase.initializeApp();

  FirebaseMessaging.onBackgroundMessage(_firebaseMessagingBackgroundHandler);

  // if (!kIsWeb) {
  //   await setupFlutterNotifications();
  // }

  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  final _auth = FirebaseAuth.instance;
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: _auth.currentUser != null ? Test() : LoginPage(),
    );
  }
}

//
class Test extends StatefulWidget {
  const Test({super.key});

  @override
  State<Test> createState() => _TestState();
}

class _TestState extends State<Test> with SingleTickerProviderStateMixin {
  late AndroidNotificationChannel channel;
  late FlutterLocalNotificationsPlugin flutterLocalNotificationsPlugin;
  String? _token;
  String? initialMessage;
  bool _resolved = false;

  final FirebaseMessaging? _firebaseMessaging = FirebaseMessaging.instance;
  TextEditingController messageCont = TextEditingController();
  bool foundTask = false;
  bool foundMeet = false;
  bool loading = false;
  final _auth = FirebaseAuth.instance;
  final _firestore = FirebaseFirestore.instance;
  late User signedInUser;
  int _counter = 0;
  void _incrementCounter() {
    setState(() {
      // This call to setState tells the Flutter framework that something has
      // changed in this State, which causes it to rerun the build method below
      // so that the display can reflect the updated values. If we changed
      // _counter without calling setState(), then the build method would not be
      // called again, and so nothing would appear to happen.
      _counter++;
    });
  }

  getIDS() async {
    var groups = await _firestore.collection('Groups').get();
    for (var i in list_groups) {
      list_ids.add(i);
    }
    for (var group in groups.docs) {
      if (list_groups.contains(group['Name'])) {
        list_ids[list_groups.indexOf(group['Name'])] = group['ID'];
      }
    }
  }

  void initialization() async {
    // This is where you can initialize the resources needed by your app while
    // the splash screen is displayed.  Remove the following example because
    // delaying the user experience is a bad design practice!
    // ignore_for_file: avoid_print
    print('ready in 3...');
    await Future.delayed(const Duration(seconds: 1));
    print('ready in 2...');
    await Future.delayed(const Duration(seconds: 1));
    print('ready in 1...');
    await Future.delayed(const Duration(seconds: 1));
    print('go!');
  }

  void get_userName() async {
    try {
      final people = await _firestore.collection('Participants').get();
      for (var person in people.docs) {
        if (person['Email'] == userEmail) {
          setState(() {
            userName = person['Name'];
          });
        }
      }
    } catch (e) {
      print(e);
    }
  }

  getGroups() async {
    try {
      final people = await _firestore.collection('Participants').get();

      for (var person in people.docs) {
        if (person['Email'] == userEmail) {
          //////////// token
          await _firestore.collection('Participants').doc(person.id).set({
            'Token': _token,
            'Email': person['Email'],
            'Groups': person['Groups'],
            'LastSigned': person['LastSigned'],
            'Name': person['Name'],
          });
          /////////// groups
          list_groups = person['Groups'];

          if (SignedGroup != '') {
            await _firestore.collection('Participants').doc(person.id).set({
              'Token': _token,
              'Email': person['Email'],
              'Groups': person['Groups'],
              'LastSigned': SignedGroup,
              'Name': person['Name'],
            });
          } else {
            setState(() {
              SignedGroup = person['LastSigned'];
            });
          }
        }
      }
      print(SignedGroup);
      getTasks();
      print(SignedGroup);
      getMeetings();
      print(SignedGroup);
      get_participants();
      print(SignedGroup);
      getChat();
      getIDS();
    } catch (e) {
      print(e);
    }
  }

  void getCurrentUser() {
    try {
      final user = _auth.currentUser;
      if (user != null) {
        signedInUser = user;
        userEmail = user.email!;
        get_userName();
      }
    } catch (e) {
      print(e);
    }
  }

  get_participants() async {
    try {
      final participants = await _firestore.collection('Participants').get();
      print(People);
      for (var person in participants.docs) {
        for (var group in person['Groups']) {
          if (group == SignedGroup) {
            print(person['Name']);
            print(group);
            print(SignedGroup);
            People.add(person['Name']);
          }
        }
      }
    } catch (e) {
      print(e);
    }
  }

  void getTasks() async {
    try {
      // if (!foundTask) {
      //   // await for (var snapshot in _firestore
      //   //     .collection('TasksDeadlines' + SignedGroup)
      //   //     .snapshots()) {
      //   //   setState(() {
      //   //     list_tasks = snapshot.docs;
      //   //   });
      //   // }
      //   var tasks =
      //       await _firestore.collection('TasksDeadlines' + SignedGroup).get();
      //   for (var task in tasks.docs) {
      //     setState(() {
      //       foundTask = true;

      //       list_tasks.add({
      //         'Description': task['Description'],
      //         'Subject': task['Subject'],
      //         'Deadline': task['Deadline']
      //       });
      //     });
      //   }
      // } else {

      await for (var snapshot in _firestore
          .collection('TasksDeadlines' + SignedGroup)
          .orderBy('Deadline')
          .snapshots()) {
        setState(() {
          list_tasks = snapshot.docs;
        });
      }

      print(list_tasks);
    } catch (e) {
      print(e);
    }
  }

  void getMeetings() async {
    try {
      // if (!foundMeet) {
      //   // await for (var snapshot in _firestore
      //   //     .collection('MeetingsDeadlines' + SignedGroup)
      //   //     .snapshots()) {
      //   //   setState(() {
      //   //     list_meetings = snapshot.docs;
      //   //   });
      //   // }
      //   var meetings = await _firestore
      //       .collection('MeetingsDeadlines' + SignedGroup)
      //       .get();
      //   for (var meet in meetings.docs) {
      //     setState(() {
      //       foundMeet = true;
      //       list_meetings.add({
      //         'Description': meet['Description'],
      //         'Subject': meet['Subject'],
      //         'Deadline': meet['Deadline']
      //       });
      //     });
      //   }
      // } else {
      await for (var snapshot in _firestore
          .collection('MeetingsDeadlines' + SignedGroup)
          .orderBy('Deadline')
          .snapshots()) {
        setState(() {
          list_meetings = snapshot.docs;
        });
        // }
      }
    } catch (e) {
      print(e);
    }
  }

  int index_tab = 2;
  bool DarkTheme = true;

  List list_chats = [];
  getChat() async {
    try {
      var chat = await _firestore
          .collection('Chat' + SignedGroup)
          .orderBy('time')
          .get();
      for (var message in chat.docs) {
        list_chats.add({
          'me': true,
          'color': Colors.red,
          'text': message['text'],
          'name': message['name']
        });
      }
    } catch (e) {
      print(e);
    }
  }

  String subtitle = '';
  String content = '';
  String data = '';

  @override
  void initState() {
    setState(() {
      loading = true;
    });
    list_groups = [];
    list_ids = [];
    People = [];
    list_tasks = [];
    list_meetings = [];

    getGroups();

    getCurrentUser();
    requestPermission();
    getToken();

    loadFCM();

    listenFCM();
    initialization();
    super.initState();
    setState(() {
      loading = false;
    });

    //initInfo();
  }

  void listenFCM() async {
    FirebaseMessaging.onMessage.listen((RemoteMessage message) {
      RemoteNotification? notification = message.notification;
      AndroidNotification? android = message.notification?.android;
      if (notification != null && android != null && !kIsWeb) {
        flutterLocalNotificationsPlugin.show(
          notification.hashCode,
          notification.title,
          notification.body,
          NotificationDetails(
            android: AndroidNotificationDetails(
              channel.id,
              channel.name,
              // TODO add a proper drawable resource to android, for now using
              //      one that already exists in example app.
              icon: 'launch_background',
            ),
          ),
        );
      }
    });
  }

  void loadFCM() async {
    if (!kIsWeb) {
      channel = const AndroidNotificationChannel(
        'high_importance_channel', // id
        'High Importance Notifications', // title
        importance: Importance.high,
        enableVibration: true,
      );

      flutterLocalNotificationsPlugin = FlutterLocalNotificationsPlugin();

      /// Create an Android Notification Channel.
      ///
      /// We use this channel in the `AndroidManifest.xml` file to override the
      /// default FCM channel to enable heads up notifications.
      await flutterLocalNotificationsPlugin
          .resolvePlatformSpecificImplementation<
              AndroidFlutterLocalNotificationsPlugin>()
          ?.createNotificationChannel(channel);

      /// Update the iOS foreground notification presentation options to allow
      /// heads up notifications.
      await FirebaseMessaging.instance
          .setForegroundNotificationPresentationOptions(
        alert: true,
        badge: true,
        sound: true,
      );
    }
  }

  void requestPermission() async {
    FirebaseMessaging messaging = FirebaseMessaging.instance;
    NotificationSettings settings = await messaging.requestPermission(
        alert: true,
        announcement: false,
        badge: true,
        carPlay: false,
        criticalAlert: false,
        provisional: false,
        sound: true);
    if (settings.authorizationStatus == AuthorizationStatus.authorized) {
      print('User granted permission');
    } else if (settings.authorizationStatus ==
        AuthorizationStatus.provisional) {
      print('User granted provisional permission');
    } else {
      print('User declined or has not accepted permission');
    }
  }

  void getToken() async {
    await FirebaseMessaging.instance.getToken().then((token) {
      setState(() {
        _token = token;
        print('Token: ' + token!);
      });
    });
  }

  drawerDesign({accountName, accountEmail, context}) {
    return Container(
      child: Column(children: [
        UserAccountsDrawerHeader(
            decoration: BoxDecoration(
                color: darkTheme ? Colors.grey[900] : Colors.amber),
            currentAccountPicture: CircleAvatar(
              backgroundColor: darkTheme ? Colors.amber : Colors.green[900],
              radius: 20,
              child: Icon(
                Icons.person,
                color: Colors.white,
                size: 40,
              ),
            ),
            accountName: Text(accountName),
            accountEmail: InkWell(
                onTap: () {
                  showDialog(
                      context: context,
                      builder: (context) {
                        return Directionality(
                            textDirection: TextDirection.rtl,
                            child: AlertDialog(
                              title: Text('تأكيد'),
                              content: Text('هل تريد الانتقال لمجموعة اخرى؟'),
                              actions: [
                                TextButton(
                                    onPressed: () {
                                      Navigator.of(context).pushReplacement(
                                          MaterialPageRoute(builder: (context) {
                                        return ChooseGroup();
                                      }));
                                    },
                                    child: Text('نعم')),
                                TextButton(
                                    onPressed: () {
                                      Navigator.of(context).pop();
                                    },
                                    child: Text('لا')),
                              ],
                            ));
                      });
                },
                child: Text(accountEmail))),
        Container(
          child: SingleChildScrollView(
              child: Column(children: [
            MaterialButton(
              height: 60,
              onPressed: () {
                Navigator.of(context).pop();
                Navigator.of(context)
                    .push(MaterialPageRoute(builder: (context) {
                  return Groups();
                }));
              },
              child: Row(children: [
                Icon(
                  Icons.people,
                  size: 30,
                ),
                SizedBox(
                  width: 10,
                ),
                Text(
                  'مجموعاتي',
                  style: TextStyle(fontSize: 18),
                )
              ]),
            ),
            MaterialButton(
              height: 60,
              onPressed: () {
                Navigator.of(context).pop();
                Navigator.of(context)
                    .push(MaterialPageRoute(builder: (context) {
                  return Participants();
                }));
              },
              child: Row(children: [
                Icon(
                  Icons.person,
                  size: 30,
                ),
                SizedBox(
                  width: 10,
                ),
                Text(
                  'المشاركين',
                  style: TextStyle(fontSize: 18),
                )
              ]),
            ),
            MaterialButton(
              height: 60,
              onPressed: () {
                Navigator.of(context).pop();
                Navigator.of(context)
                    .push(MaterialPageRoute(builder: (context) {
                  return EndDone();
                }));
              },
              child: Row(children: [
                Icon(
                  Icons.done_all_outlined,
                  size: 30,
                ),
                SizedBox(
                  width: 10,
                ),
                Text(
                  'التسليمات المنتهية',
                  style: TextStyle(fontSize: 18),
                )
              ]),
            ),
            MaterialButton(
              height: 60,
              onPressed: () {
                Navigator.of(context).pop();
                Navigator.of(context)
                    .push(MaterialPageRoute(builder: (context) {
                  return EndMeet();
                }));
              },
              child: Row(children: [
                Icon(
                  Icons.meeting_room_sharp,
                  size: 30,
                ),
                SizedBox(
                  width: 10,
                ),
                Text(
                  'الاجتماعات المنتهية',
                  style: TextStyle(fontSize: 18),
                )
              ]),
            ),
            MaterialButton(
              height: 60,
              onPressed: () {
                Navigator.of(context).pop();
                Navigator.of(context)
                    .push(MaterialPageRoute(builder: (context) {
                  return AllTasks();
                }));
              },
              child: Row(children: [
                Icon(
                  Icons.task,
                  size: 30,
                ),
                SizedBox(
                  width: 10,
                ),
                Text(
                  'جميع التسليمات',
                  style: TextStyle(fontSize: 18),
                )
              ]),
            ),
            MaterialButton(
              height: 60,
              onPressed: () {
                Navigator.of(context).pop();
                Navigator.of(context)
                    .push(MaterialPageRoute(builder: (context) {
                  return AllMeetings();
                }));
              },
              child: Row(children: [
                Icon(
                  Icons.meeting_room_outlined,
                  size: 30,
                ),
                SizedBox(
                  width: 10,
                ),
                Text(
                  'جميع الاجتماعات',
                  style: TextStyle(fontSize: 18),
                )
              ]),
            ),
            MaterialButton(
              height: 60,
              onPressed: () {
                showDialog(
                    context: context,
                    builder: (context) {
                      return Directionality(
                          textDirection: TextDirection.rtl,
                          child: AlertDialog(
                            title: Text('تسجيل الخروج'),
                            content: Text('هل تريد فعلا تسجيل الخروج؟'),
                            actions: [
                              TextButton(
                                  onPressed: () {
                                    _auth.signOut();
                                    Navigator.of(context).pushReplacement(
                                        MaterialPageRoute(builder: (context) {
                                      return LoginPage();
                                    }));
                                  },
                                  child: Text('نعم')),
                              TextButton(
                                  onPressed: () {
                                    Navigator.of(context).pop();
                                  },
                                  child: Text('لا'))
                            ],
                          ));
                    });
              },
              child: Row(children: [
                Icon(
                  Icons.logout,
                  size: 30,
                ),
                SizedBox(
                  width: 10,
                ),
                Text(
                  'تسجيل الخروج',
                  style: TextStyle(fontSize: 18),
                )
              ]),
            ),
            Row(
              children: [
                Switch(
                    value: darkTheme,
                    onChanged: (val) {
                      setState(() {
                        darkTheme = val;
                      });
                    }),
                Text(
                  'الوضع المظلم',
                  style: TextStyle(fontSize: 18),
                )
              ],
            ),
            Divider(),
            Container(
              child:
                  Row(mainAxisAlignment: MainAxisAlignment.center, children: [
                Text('مواعيد التسليم'),
                SizedBox(
                  width: 10,
                ),
                Icon(Icons.timelapse_outlined)
              ]),
            )
          ])),
        )
      ]),
    );
  }

  chatScreen({list_chat, messageCont}) {
    return Container(
      width: double.infinity,
      height: double.infinity,
      color: Colors.grey[300],
      child: Column(children: [
        Expanded(
            child: SingleChildScrollView(
          child: Column(
            children: List.generate(list_chat.length, (i) {
              return chatItem(
                  direction: list_chat[i]['me']
                      ? TextDirection.ltr
                      : TextDirection.rtl,
                  color: list_chat[i]['color'],
                  text: list_chat[i]['text'],
                  name: list_chat[i]['name']);
            }),
          ),
        )),
        Row(
          children: [
            Expanded(
                child: Container(
                    margin: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
                    height: 50,
                    child: TextFormField(
                        controller: messageCont,
                        decoration: InputDecoration(
                            border: OutlineInputBorder(
                                borderRadius: BorderRadius.circular(50)))))),
            IconButton(
                onPressed: () async {
                  if (messageCont.text != '') {
                    try {
                      final _firebase = FirebaseFirestore.instance;
                      // final chats = await _firebase
                      //     .collection('Chat' + SignedGroup)
                      //     .get();
                      // var person;
                      // try {
                      //   for (var chat in chats.docs) {
                      //     person = chat['name'];
                      //     break;
                      //     // _firebase
                      //     //     .collection('Chat' + SignedGroup)
                      //     //     .doc(chat.id)
                      //     //     .set({'text': messageCont.text, 'name': userName});
                      //   }
                      // } catch (e) {
                      //   person = userName;
                      // }
                      if (list_chats.isNotEmpty) {
                        if (list_chats[0]['name'] == userName) {
                          setState(() {
                            list_chats.add({
                              'text': messageCont.text,
                              'name': userName,
                              'me': true,
                              'color': Colors.red
                            });
                          });
                          // only add
                          await _firebase.collection('Chat' + SignedGroup).add({
                            'text': messageCont.text,
                            'name': userName,
                            'time': FieldValue.serverTimestamp()
                          });
                        } else {
                          final chats = await _firebase
                              .collection('Chat' + SignedGroup)
                              .get();
                          for (var chat in chats.docs) {
                            await _firebase
                                .collection('Chat' + SignedGroup)
                                .doc(chat.id)
                                .delete();
                          }
                          setState(() {
                            list_chats = [
                              {
                                'text': messageCont.text,
                                'name': userName,
                                'me': true,
                                'color': Colors.red
                              }
                            ];
                          });
                          await _firebase.collection('Chat' + SignedGroup).add({
                            'text': messageCont.text,
                            'name': userName,
                            'time': FieldValue.serverTimestamp()
                          });

                          // only write
                        }
                      } else {
                        setState(() {
                          list_chats.add({
                            'text': messageCont.text,
                            'name': userName,
                            'me': true,
                            'color': Colors.red
                          });
                        });
                        // only add
                        await _firebase.collection('Chat' + SignedGroup).add({
                          'text': messageCont.text,
                          'name': userName,
                          'time': FieldValue.serverTimestamp()
                        });
                      }
                      // _firebase
                      //     .collection('Chat' + SignedGroup)
                      //     .add({'text': 'ok', 'name': 'ahmed'});
                    } catch (e) {
                      print(e);
                    }

                    messageCont.clear();
                  }
                },
                icon: Icon(Icons.send))
          ],
        )
      ]),
    );
  }

  @override
  Widget build(BuildContext context) {
    return ModalProgressHUD(
        inAsyncCall: loading,
        child: DefaultTabController(
            initialIndex: 2,
            length: 3,
            child: Scaffold(
                floatingActionButton: index_tab == 0
                    ? null
                    : FloatingActionButton(
                        onPressed: () {
                          Navigator.of(context)
                              .push(MaterialPageRoute(builder: (context) {
                            return AddTaskMeet();
                          }));
                        },
                        child: Icon(Icons.add),
                        backgroundColor:
                            darkTheme ? Colors.grey[900] : Colors.amber,
                      ),
                drawer: Drawer(
                  child: drawerDesign(
                      accountEmail: SignedGroup,
                      accountName: userName,
                      context: context),
                ),
                appBar: AppBar(
                    title: Container(
                        alignment: Alignment.centerRight,
                        width: double.infinity,
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.end,
                          children: [
                            Text(
                              'مواعيد التسليم',
                              style: TextStyle(fontSize: 20),
                            ),
                            SizedBox(
                              width: 10,
                            ),
                            Icon(Icons.timelapse_outlined)
                          ],
                        )),
                    backgroundColor:
                        darkTheme ? Colors.grey[900] : Colors.amber,
                    bottom: TabBar(
                      onTap: (value) {
                        setState(() {
                          index_tab = value;
                        });
                      },
                      splashBorderRadius: BorderRadius.circular(50),
                      padding:
                          EdgeInsets.symmetric(vertical: 10, horizontal: 10),
                      indicator: BoxDecoration(
                          color: darkTheme ? Colors.amber : Colors.grey[700],
                          borderRadius: BorderRadius.circular(50)),
                      isScrollable: true,
                      tabs: [
                        Row(
                          children: const [
                            Icon(Icons.chat),
                            SizedBox(
                              width: 5,
                            ),
                            Text(
                              'الدردشة',
                              style: TextStyle(fontSize: 18),
                            ),
                          ],
                        ),
                        Row(
                          children: const [
                            Icon(Icons.meeting_room),
                            SizedBox(
                              width: 5,
                            ),
                            Text(
                              'الاجتماعات',
                              style: TextStyle(fontSize: 18),
                            ),
                          ],
                        ),
                        Row(
                          children: const [
                            Icon(Icons.drive_file_move_rounded),
                            SizedBox(
                              width: 5,
                            ),
                            Text(
                              'التسليمات',
                              style: TextStyle(fontSize: 18),
                            )
                          ],
                        ),
                      ],
                    )),
                body: Directionality(
                  textDirection: TextDirection.ltr,
                  child: TabBarView(
                    physics: NeverScrollableScrollPhysics(),
                    children: [
                      chatScreen(
                          list_chat: list_chats, messageCont: messageCont),
                      meetingScreen(list_meetings: list_meetings),
                      deliverScreen(list_tasks2: list_tasks)
                    ],
                  ),
                ))));
  }
}

deliverScreen({list_tasks2}) {
  String? vars;
  return Container(
    color: Colors.grey[300],
    width: double.infinity,
    height: double.infinity,
    child: ListView.builder(
        itemCount: list_tasks2.length,
        itemBuilder: (context, i) {
          if (list_tasks2[i]['Subject'] == '') {
            return Container();
          }

          return Dismissible(
              confirmDismiss: (DismissDirection direction) async {
                final confirmed = await showDialog<bool>(
                  context: context,
                  builder: (context) {
                    return AlertDialog(
                      title: Text('تحذير'),
                      content: Text('هل تريد فعلا الحذف؟'),
                      actions: [
                        TextButton(
                          onPressed: () async {
                            final firestore = FirebaseFirestore.instance;
                            var tasks = await firestore
                                .collection('TasksDeadlines' + SignedGroup)
                                .get();
                            for (var task in tasks.docs) {
                              if (task['Subject'] ==
                                      list_tasks2[i]['Subject'] &&
                                  task['Description'] ==
                                      list_tasks2[i]['Description'] &&
                                  task['Deadline'] ==
                                      list_tasks[i]['Deadline']) {
                                firestore
                                    .collection('TasksDeadlines' + SignedGroup)
                                    .doc(task.id)
                                    .delete();
                              }
                            }
                            Navigator.of(context).pop();
                          },
                          child: const Text('نعم'),
                        ),
                        TextButton(
                          onPressed: () => Navigator.pop(context, true),
                          child: const Text('لا'),
                        )
                      ],
                    );
                  },
                );
              },
              key: Key('$vars'),
              child: ItemDesign(
                  task: true,
                  index: i,
                  title: list_tasks2[i]['Subject'],
                  desc: list_tasks2[i]['Description'],
                  time: list_tasks2[i]['Deadline'],
                  context: context,
                  icon: Icons.task));
        }),
  );
}

ItemDesign({title, desc, time, icon, context, index, task}) {
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
                        child: Container(
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
                        Text('$time')
                        // Row(
                        //   mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        //   children: [
                        //     Text(
                        //       '$desc',
                        //       style: TextStyle(fontSize: 15),
                        //       maxLines: 1,
                        //       overflow: TextOverflow.ellipsis,
                        //     ),
                        //     Text('$time')
                        //   ],
                        // )
                      ],
                    ))),
                  ],
                ))),
        Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            IconButton(
              onPressed: () async {
                showDialog(
                    context: context,
                    builder: (context) {
                      return Directionality(
                          textDirection: TextDirection.rtl,
                          child: AlertDialog(
                            title: Text('تأكيد'),
                            content: Text('هل تمت فعلا؟'),
                            actions: [
                              TextButton(
                                  onPressed: () async {
                                    Navigator.of(context).pop();
                                    final _firestore =
                                        FirebaseFirestore.instance;
                                    if (task) {
                                      var tasks = await _firestore
                                          .collection(
                                              'TasksDeadlines' + SignedGroup)
                                          .get();
                                      for (var task in tasks.docs) {
                                        if (list_tasks[index]['Subject'] ==
                                                task['Subject'] &&
                                            list_tasks[index]['Deadline'] ==
                                                task['Deadline'] &&
                                            list_tasks[index]['Description'] ==
                                                task['Description']) {
                                          _firestore
                                              .collection('TasksDeadlines' +
                                                  SignedGroup)
                                              .doc(task.id)
                                              .delete();
                                          _firestore
                                              .collection(
                                                  'EndedTasks' + SignedGroup)
                                              .add({
                                            'Subject': task['Subject'],
                                            'Deadline': task['Deadline'],
                                            'Description': task['Description'],
                                            'Done':
                                                "${DateTime.now().day}-${DateTime.now().month}-${DateTime.now().year}/${DateTime.now().hour}:${DateTime.now().minute}"
                                          });
                                        }
                                      }
                                    } else {
                                      var meets = await _firestore
                                          .collection(
                                              'MeetingsDeadlines' + SignedGroup)
                                          .get();
                                      for (var meet in meets.docs) {
                                        if (list_meetings[index]['Subject'] ==
                                                meet['Subject'] &&
                                            list_meetings[index]['Deadline'] ==
                                                meet['Deadline'] &&
                                            list_meetings[index]
                                                    ['Description'] ==
                                                meet['Description']) {
                                          _firestore
                                              .collection('MeetingsDeadlines' +
                                                  SignedGroup)
                                              .doc(meet.id)
                                              .delete();
                                          _firestore
                                              .collection(
                                                  'EndedMeetings' + SignedGroup)
                                              .add({
                                            'Subject': meet['Subject'],
                                            'Deadline': meet['Deadline'],
                                            'Description': meet['Description'],
                                            'Done':
                                                "${DateTime.now().day}-${DateTime.now().month}-${DateTime.now().year}/${DateTime.now().hour}:${DateTime.now().minute}"
                                          });
                                        }
                                      }
                                    }
                                  },
                                  child: Text('نعم')),
                              TextButton(
                                  onPressed: () {
                                    Navigator.of(context).pop();
                                  },
                                  child: Text('لا')),
                            ],
                          ));
                    });
              },
              icon: Icon(Icons.done),
              splashRadius: 20,
            ),
            IconButton(
              onPressed: () {
                showDialog(
                    context: context,
                    builder: (context) {
                      return Directionality(
                          textDirection: TextDirection.rtl,
                          child: AlertDialog(
                            title: Text('تأكيد'),
                            content: Text('هل تريد فعلا التعديل؟'),
                            actions: [
                              TextButton(
                                  onPressed: () {
                                    print(list_tasks[index]['Subject']);
                                    Navigator.of(context).pushReplacement(
                                        MaterialPageRoute(builder: (context) {
                                      return AddTaskMeet(
                                        modify: 2,
                                        type: task ? 'تاسك' : 'اجتماع',
                                        deadline: task
                                            ? list_tasks[index]['Deadline']
                                            : list_meetings[index]['Deadline'],
                                        subject: task
                                            ? list_tasks[index]['Subject']
                                            : list_meetings[index]['Subject'],
                                        description: task
                                            ? list_tasks[index]['Description']
                                            : list_meetings[index]
                                                ['Description'],
                                      );
                                    }));
                                  },
                                  child: Text('نعم')),
                              TextButton(
                                  onPressed: () {
                                    Navigator.of(context).pop();
                                  },
                                  child: Text('لا')),
                            ],
                          ));
                    });
              },
              icon: Icon(Icons.edit),
              splashRadius: 20,
            ),
          ],
        )
      ],
    ),
  );
}

onClick() {
  print(1);
}

meetingScreen({list_meetings}) {
  String? key;
  return Container(
    color: Colors.grey[300],
    width: double.infinity,
    height: double.infinity,
    child: ListView.builder(
        itemCount: list_meetings.length,
        itemBuilder: (context, i) {
          if (list_meetings[i]['Subject'] == '') {
            return Container();
          }
          return Dismissible(
              confirmDismiss: (DismissDirection direction) async {
                final confirmed = await showDialog<bool>(
                  context: context,
                  builder: (context) {
                    return Directionality(
                        textDirection: TextDirection.rtl,
                        child: AlertDialog(
                          title: Text('تحذير'),
                          content: Text('هل تريد فعلا الحذف؟'),
                          actions: [
                            TextButton(
                              onPressed: () async {
                                final firestore = FirebaseFirestore.instance;
                                var tasks = await firestore
                                    .collection(
                                        'MeetingsDeadlines' + SignedGroup)
                                    .get();
                                for (var task in tasks.docs) {
                                  if (task['Subject'] ==
                                          list_meetings[i]['Subject'] &&
                                      task['Description'] ==
                                          list_meetings[i]['Description'] &&
                                      task['Deadline'] ==
                                          list_meetings[i]['Deadline']) {
                                    firestore
                                        .collection(
                                            'MeetingsDeadlines' + SignedGroup)
                                        .doc(task.id)
                                        .delete();
                                  }
                                }
                                Navigator.of(context).pop();
                              },
                              child: const Text('نعم'),
                            ),
                            TextButton(
                              onPressed: () => Navigator.pop(context, true),
                              child: const Text('لا'),
                            )
                          ],
                        ));
                  },
                );
              },
              key: Key('$key'),
              child: ItemDesign(
                  task: false,
                  index: i,
                  title: list_meetings[i]['Subject'],
                  desc: list_meetings[i]['Description'],
                  time: list_meetings[i]['Deadline'],
                  context: context,
                  icon: Icons.meeting_room_outlined));
        }),
  );
}

chatItem({direction, color, text, name}) {
  return Container(
    width: double.infinity,
    //color: Colors.green,
    margin: EdgeInsets.symmetric(horizontal: 10, vertical: 5),
    child: Directionality(
        textDirection: direction,
        child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
          CircleAvatar(
            child: Icon(
              Icons.person,
              color: Colors.white,
            ),
            backgroundColor: color,
          ),
          SizedBox(
            width: 10,
          ),
          Expanded(
              flex: 3,
              child: Container(
                padding: EdgeInsets.all(5),
                decoration: BoxDecoration(
                    color: Colors.grey[600],
                    borderRadius: BorderRadius.circular(10)),
                child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        '$name',
                        style: TextStyle(
                            color: Colors.amber, fontWeight: FontWeight.bold),
                      ),
                      Text(
                        '$text',
                        style: TextStyle(fontSize: 20, color: Colors.white),
                      )
                    ]),
              )),
          Expanded(flex: 1, child: SizedBox())
        ])),
  );
}
