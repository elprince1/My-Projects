import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:modal_progress_hud_nsn/modal_progress_hud_nsn.dart';
import 'package:Deadlines/SignupPage.dart';

import 'package:Deadlines/main.dart';
import 'main.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_auth/firebase_auth.dart';

class ChooseGroup extends StatefulWidget {
  const ChooseGroup({super.key});

  @override
  State<ChooseGroup> createState() => _ChooseGroupState();
}

class _ChooseGroupState extends State<ChooseGroup> {
  String selected = list_groups[0];
  List<String> list = [];
  @override
  void initState() {
    for (var i in list_groups) {
      list.add(i.toString());
    }
    // TODO: implement initState
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Directionality(
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
                      child: DropdownButton(
                    items: list
                        .map((e) => DropdownMenuItem(
                              child: Text('$e'),
                              value: e,
                            ))
                        .toList(),
                    onChanged: (value) {
                      setState(() {
                        selected = value!;
                        SignedGroup = value;
                      });
                      Navigator.pushReplacement(context,
                          MaterialPageRoute(builder: (context) {
                        return Test();
                      }));
                    },
                    value: selected,
                  ))
                ]))));
  }
}
