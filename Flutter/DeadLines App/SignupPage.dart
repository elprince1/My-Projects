import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:Deadlines/LoginPage.dart';
import 'package:Deadlines/SignupPage.dart';

import 'package:Deadlines/main.dart';
import 'main.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:modal_progress_hud_nsn/modal_progress_hud_nsn.dart';

class SignupPage extends StatefulWidget {
  @override
  State<SignupPage> createState() => _SignupPageState();
}

class _SignupPageState extends State<SignupPage> {
  TextEditingController emailCont = TextEditingController();
  TextEditingController passwordCont1 = TextEditingController();
  TextEditingController passwordCont2 = TextEditingController();
  TextEditingController nameCont = TextEditingController();
  TextEditingController GroupIDCont = TextEditingController();
  bool flag_email = false;
  bool flag_password = false;
  var formKey = GlobalKey<FormState>();
  final _auth = FirebaseAuth.instance;
  final _firestore = FirebaseFirestore.instance;
  bool visible1 = true;
  bool visible2 = true;
  bool saving = false;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: ModalProgressHUD(
          inAsyncCall: saving,
          child: Directionality(
              textDirection: TextDirection.rtl,
              child: Container(
                  width: double.infinity,
                  child: Stack(children: [
                    Container(
                      alignment: Alignment.center,
                      width: double.infinity,
                      height: 150,
                      decoration: BoxDecoration(
                        color: Colors.grey[900],
                      ),
                    ),
                    Form(
                        key: formKey,
                        child: Center(
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
                                  controller: nameCont,
                                  keyboardType: TextInputType.name,
                                  decoration: InputDecoration(
                                      fillColor: Colors.white,
                                      filled: true,
                                      //prefix: Icon(Icons.email),
                                      label: Text('الاسم'),
                                      prefixIcon: Icon(Icons.person),
                                      border: OutlineInputBorder(
                                          borderRadius:
                                              BorderRadius.circular(10))),
                                ),
                                SizedBox(
                                  height: 20,
                                ),
                                TextFormField(
                                  onChanged: (value) {
                                    flag_email = true;
                                  },
                                  autovalidateMode: AutovalidateMode.always,
                                  validator: (value) {
                                    final bool emailValid = RegExp(
                                            r"^[a-zA-Z0-9.a-zA-Z0-9.!#$%&'*+-/=?^_`{|}~]+@[a-zA-Z0-9]+\.[a-zA-Z]+")
                                        .hasMatch(value!);
                                    if (!emailValid && flag_email) {
                                      return 'البريد غير صحيح';
                                    }
                                  },
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
                                  onChanged: (value) {
                                    flag_password = true;
                                  },
                                  autovalidateMode: AutovalidateMode.always,
                                  validator: (value) {
                                    if (value!.length < 6 && flag_password) {
                                      return 'عدد الحروف يجب ان يكون أكبر من 5';
                                    }
                                  },
                                  controller: passwordCont1,
                                  obscureText: visible1,
                                  decoration: InputDecoration(
                                      suffixIcon: IconButton(
                                        icon: Icon(visible1
                                            ? Icons.visibility
                                            : Icons.visibility_off),
                                        onPressed: () {
                                          setState(() {
                                            visible1 = !visible1;
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
                                SizedBox(
                                  height: 20,
                                ),
                                TextFormField(
                                  autovalidateMode: AutovalidateMode.always,
                                  validator: (value) {
                                    if (value != passwordCont1.text) {
                                      return 'الباسورد غير متطابق';
                                    }
                                  },
                                  controller: passwordCont2,
                                  obscureText: visible2,
                                  decoration: InputDecoration(
                                      suffixIcon: IconButton(
                                        icon: Icon(visible2
                                            ? Icons.visibility
                                            : Icons.visibility_off),
                                        onPressed: () {
                                          setState(() {
                                            visible2 = !visible2;
                                          });
                                        },
                                      ),
                                      fillColor: Colors.white,
                                      filled: true,
                                      //prefix: Icon(Icons.email),
                                      label: Text('تأكيد كلمة المرور'),
                                      prefixIcon: Icon(Icons.lock),
                                      border: OutlineInputBorder(
                                          borderRadius:
                                              BorderRadius.circular(10))),
                                ),
                                SizedBox(
                                  height: 20,
                                ),
                                TextFormField(
                                  controller: GroupIDCont,
                                  decoration: InputDecoration(
                                      fillColor: Colors.white,
                                      filled: true,
                                      label:
                                          Text('المجموعة المراد التسجيل بها'),
                                      prefixIcon: Icon(Icons.people),
                                      border: OutlineInputBorder(
                                          borderRadius:
                                              BorderRadius.circular(10))),
                                ),
                                Row(
                                  mainAxisAlignment: MainAxisAlignment.start,
                                  children: [
                                    Text("لديك حساب بالفعل "),
                                    TextButton(
                                        onPressed: () {
                                          Navigator.of(context).pushReplacement(
                                              MaterialPageRoute(
                                                  builder: (context) {
                                            return LoginPage();
                                          }));
                                        },
                                        child: Text('تسجيل الدخول')),
                                  ],
                                ),
                                MaterialButton(
                                  shape: RoundedRectangleBorder(
                                      borderRadius: BorderRadius.circular(10)),
                                  color: Colors.grey[900],
                                  onPressed: () async {
                                    if (formKey.currentState!.validate() &&
                                        nameCont.text != '' &&
                                        emailCont.text != '' &&
                                        passwordCont1.text != '' &&
                                        passwordCont2.text != '' &&
                                        GroupIDCont.text != '') {
                                      setState(() {
                                        saving = true;
                                      });
                                      bool error = false;
                                      try {
                                        final groups = await _firestore
                                            .collection('Groups')
                                            .get();
                                        List groups_list = [];

                                        for (var group in groups.docs) {
                                          if (group['ID'] == GroupIDCont.text) {
                                            groups_list.add(group['Name']);
                                            SignedGroup = group['Name'];
                                          }
                                        }
                                        if (groups_list.isEmpty) {
                                          error = true;
                                        } else {
                                          final newUser = await _auth
                                              .createUserWithEmailAndPassword(
                                            email: emailCont.text,
                                            password: passwordCont1.text,
                                          );

                                          _firestore
                                              .collection('Participants')
                                              .add({
                                            'Name': nameCont.text,
                                            'Email': emailCont.text,
                                            'Groups': groups_list,
                                            'LastSigned': groups_list[0],
                                          });
                                        }
                                      } catch (e) {
                                        error = true;
                                        print(e);
                                      }
                                      setState(() {
                                        saving = false;
                                      });
                                      if (!error) {
                                        Navigator.of(context).pushReplacement(
                                            MaterialPageRoute(
                                                builder: (context) {
                                          return Test();
                                        }));
                                      } else {
                                        return showDialog(
                                            context: context,
                                            builder: (context) {
                                              return AlertDialog(
                                                title: Text('التسجيل خاطيء'),
                                                content: Text(
                                                    'راجع التعليمات المكتوبة'),
                                              );
                                            });
                                      }
                                    } else {
                                      return showDialog(
                                          context: context,
                                          builder: (context) {
                                            return AlertDialog(
                                              title: Text('التسجيل خاطيء'),
                                              content: Text(
                                                  'راجع التعليمات المكتوبة'),
                                            );
                                          });
                                    }
                                  },
                                  child: Text(
                                    'انشاء حساب',
                                    style: TextStyle(
                                        fontSize: 20, color: Colors.white),
                                  ),
                                )
                              ])),
                        )))
                  ])))),
    );
  }
}
