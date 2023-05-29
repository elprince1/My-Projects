import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:modal_progress_hud_nsn/modal_progress_hud_nsn.dart';
import 'package:Deadlines/SignupPage.dart';

import 'package:Deadlines/main.dart';
import 'ChooseGroup.dart';
import 'main.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_auth/firebase_auth.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  TextEditingController emailCont = TextEditingController();
  TextEditingController passwordCont = TextEditingController();
  final _auth = FirebaseAuth.instance;
  bool visible = true;
  bool saving = false;
  final _firestore = FirebaseFirestore.instance;
  getGroups() async {
    try {
      final people = await _firestore.collection('Participants').get();
      for (var person in people.docs) {
        if (person['Email'] == emailCont.text) {
          list_groups = person['Groups'];
        }
      }
    } catch (e) {
      print(e);
    }
  }

  @override
  Widget build(BuildContext context) {
    return WillPopScope(
      onWillPop: () async {
        //dispose();
        return false;
      },
      child: Scaffold(
        body: ModalProgressHUD(
            inAsyncCall: saving,
            child: Directionality(
                textDirection: TextDirection.ltr,
                child: Container(
                    width: double.infinity,
                    child: Stack(children: [
                      Container(
                        width: double.infinity,
                        height: 200,
                        decoration: BoxDecoration(
                            color: Colors.grey[500],
                            borderRadius: BorderRadius.only(
                                bottomLeft: Radius.circular(0),
                                bottomRight: Radius.circular(100))),
                        child: Container(
                          width: double.infinity,
                          height: 200,
                          decoration: BoxDecoration(
                              color: Colors.grey[700],
                              borderRadius: BorderRadius.only(
                                  bottomLeft: Radius.circular(0),
                                  bottomRight: Radius.circular(150))),
                          child: Container(
                              alignment: Alignment.center,
                              width: double.infinity,
                              height: 200,
                              decoration: BoxDecoration(
                                  color: Colors.grey[900],
                                  borderRadius: BorderRadius.only(
                                      bottomLeft: Radius.circular(0),
                                      bottomRight: Radius.circular(250))),
                              child: Column(
                                mainAxisAlignment: MainAxisAlignment.center,
                                children: [
                                  Icon(
                                    Icons.timelapse_outlined,
                                    size: 50,
                                    color: Colors.white,
                                  ),
                                  Text(
                                    'مواعيد التسليم',
                                    style: TextStyle(
                                        fontSize: 30, color: Colors.white),
                                  ),
                                ],
                              )),
                        ),
                      ),
                      Center(
                          child: Container(
                        color: Colors.grey[50],
                        padding: const EdgeInsets.symmetric(horizontal: 20),
                        child: SingleChildScrollView(
                            child: Column(
                                mainAxisAlignment: MainAxisAlignment.center,
                                children: [
                              SizedBox(
                                height: 20,
                              ),
                              TextFormField(
                                controller: emailCont,
                                keyboardType: TextInputType.emailAddress,
                                decoration: InputDecoration(
                                    fillColor: Colors.white,
                                    filled: true,
                                    //prefix: Icon(Icons.email),
                                    label: Text('البريد الالكتروني'),
                                    prefixIcon: Icon(Icons.email),
                                    border: OutlineInputBorder(
                                        borderRadius:
                                            BorderRadius.circular(10))),
                              ),
                              SizedBox(
                                height: 20,
                              ),
                              TextFormField(
                                controller: passwordCont,
                                obscureText: visible,
                                decoration: InputDecoration(
                                    suffixIcon: IconButton(
                                      icon: Icon(visible
                                          ? Icons.visibility
                                          : Icons.visibility_off),
                                      onPressed: () {
                                        setState(() {
                                          visible = !visible;
                                        });
                                      },
                                    ),
                                    fillColor: Colors.white,
                                    filled: true,
                                    //prefix: Icon(Icons.email),
                                    label: Text('كلمة المرور'),
                                    prefixIcon: Icon(Icons.lock),
                                    border: OutlineInputBorder(
                                        borderRadius:
                                            BorderRadius.circular(10))),
                              ),
                              Row(
                                mainAxisAlignment: MainAxisAlignment.end,
                                children: [
                                  TextButton(
                                      onPressed: () {
                                        Navigator.of(context).pushReplacement(
                                            MaterialPageRoute(
                                                builder: (context) {
                                          return SignupPage();
                                        }));
                                      },
                                      child: Text('انشاء حساب')),
                                  Text("اذا كان ليس لديك حساب فقم ب"),
                                ],
                              ),
                              MaterialButton(
                                shape: RoundedRectangleBorder(
                                    borderRadius: BorderRadius.circular(10)),
                                color: Colors.grey[900],
                                onPressed: () async {
                                  setState(() {
                                    saving = true;
                                  });
                                  try {
                                    final user =
                                        await _auth.signInWithEmailAndPassword(
                                            email: emailCont.text,
                                            password: passwordCont.text);
                                    if (user != null) {
                                      await getGroups();
                                      print(list_groups);
                                      Navigator.of(context).pushReplacement(
                                          MaterialPageRoute(builder: (context) {
                                        return ChooseGroup();
                                      }));
                                    }
                                  } catch (e) {
                                    setState(() {
                                      saving = false;
                                    });
                                    return showDialog(
                                        context: context,
                                        builder: (context) {
                                          return Directionality(
                                              textDirection: TextDirection.rtl,
                                              child: AlertDialog(
                                                title: Text(
                                                  'خطأ في تسجيل الدخول',
                                                  style:
                                                      TextStyle(fontSize: 20),
                                                ),
                                                content: Text(
                                                    'البريد الالكتروني أو الباسورد غير صحيح'),
                                              ));
                                        });
                                  }

                                  setState(() {
                                    saving = false;
                                  });
                                },
                                child: Text(
                                  'تسجيل الدخول',
                                  style: TextStyle(
                                      fontSize: 20, color: Colors.white),
                                ),
                              )
                            ])),
                      ))
                    ])))),
      ),
    );
  }
}
