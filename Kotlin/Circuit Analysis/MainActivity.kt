package com.elprince.startup

import android.content.Context
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.ArrayAdapter
import androidx.core.view.isVisible
import com.google.android.gms.ads.AdRequest
import com.google.android.gms.ads.AdView
import com.google.android.gms.ads.MobileAds
import com.google.android.gms.ads.interstitial.InterstitialAd
import kotlinx.android.synthetic.main.activity_main.*

class Kirchoff_app {
    fun Isnumeric(num:String):Boolean?{
        var x=true
        try{
            var num=num.toDouble()
        }catch(ex:Exception){
            if (num==".") {
                x = true
            }else{
                x=false
            }
        }
        return x
    }
    fun Count(txt:String,chr:String):Int?{
        var count=0
        var cnt=0
        while(cnt<=txt.length-1){
            var p=0
            if (txt[cnt]==chr[0]){
                for( j in chr){
                    if(j==txt[cnt]){
                        p=1
                        cnt+=1
                    }
                    else{
                        p=0
                        break
                    }
                }
                if(p==1){
                    count+=1
                }
            }else{
                cnt+=1
            }
        }

        return count
    }
    fun Inverse(txt:String):String? {
        var x=""
        var i:Int=txt.length-1
        while(i>=0){
            x+=txt[i]
            i--
        }
        return x
    }
    fun copying0(list1:ArrayList<String>):Array<String>?{
        var list2 = list1.toTypedArray()
        return list2
    }
    fun copying(list1:Array<String>,list2:ArrayList<String>):ArrayList<String>?{
        list2.clear()
        for(i in list1){
            list2.add(i)
        }
        return list2
    }
    fun Kirchoff_solving(nodes:ArrayList<String>,loops:ArrayList<String>,resistances:ArrayList<String>,method1:ArrayList<String>,current1:ArrayList<String>,
                         voltages:ArrayList<String>,method2:ArrayList<String>,current2:ArrayList<String>,current_sources:ArrayList<String>,method3:ArrayList<String>,
                         voltage3:ArrayList<String>,eq:ArrayList<String> = arrayListOf()):ArrayList<String> ?{
        val resistances_2:Array<String> = copying0(resistances)!!


        val method1_2:Array<String> = copying0(method1)!!

        val current1_2:Array<String> = copying0(current1)!!

        val voltages_2:Array<String> = copying0(voltages)!!

        val method2_2:Array<String> = copying0(method2)!!

        val current2_2:Array<String> = copying0(current2)!!

        val current_sources_2:Array<String> = copying0(current_sources)!!

        val method3_2:Array<String> = copying0(method3)!!

        val voltage3_2:Array<String> = copying0(voltage3)!!

        var eqts_loops:ArrayList<String> = arrayListOf()
        for (loop in loops){
            var equtn:String=""
            var resistances=copying(resistances_2,resistances)!!
            var method1=copying(method1_2,method1)!!
            var current1=copying(current1_2,current1)!!
            var voltages=copying(voltages_2,voltages)!!
            var method2=copying(method2_2,method2)!!
            var current2=copying(current2_2,current2)!!
            var current_sources=copying(current_sources_2,current_sources)!!
            var method3=copying(method3_2,method3)!!
            var voltage3=copying(voltage3_2,voltage3)!!
            for (count in 0..loop.length-2){
                var cnt:Int=0
                var p:Int=0
                for (method in method1){
                    if (method==loop[count].toString()+loop[count+1].toString()){
                        if (Isnumeric(current1[cnt]) == true){
                            if(Isnumeric(resistances[cnt])==true){
                                equtn+="+"+(resistances[cnt].toDouble()*current1[cnt].toDouble()).toString()
                                p=1
                                if (loop.length==3){
                                    resistances.removeAt(cnt)
                                    method1.removeAt(cnt)
                                    current1.removeAt(cnt)

                                }
                                break
                            }
                            else{
                                if (Isnumeric(resistances[cnt][0].toString())==true){
                                    var num5=""
                                    var num6=""
                                    var s=0
                                    for(p1 in resistances[cnt]){
                                        if (Isnumeric(p1.toString())==false){
                                            num6+=p1
                                            s=1
                                        }else{
                                            if (s==1) {
                                                num6 += p1
                                            }else{
                                                num5+=p1
                                            }
                                        }
                                    }
                                    num5=(current1[cnt].toDouble()*num5.toDouble()).toString()
                                    equtn+="+"+num5+num6
                                }else {
                                    equtn += "+" + current1[cnt] + resistances[cnt]
                                }
                                p=1
                                if (loop.length==3){
                                    resistances.removeAt(cnt)
                                    method1.removeAt(cnt)
                                    current1.removeAt(cnt)
                                }
                                break
                            }
                        }
                        else{
                            if(Isnumeric(resistances[cnt])==true){
                                if (Isnumeric(current1[cnt][0].toString())==true || current1[cnt][0]=='-'){
                                    var num5=""
                                    var num6=""
                                    var s=0
                                    var bcount=0
                                    for(p1 in current1[cnt]){
                                        if (Isnumeric(p1.toString())==false && current1[cnt][bcount]!='-'){
                                            num6+=p1
                                            s=1
                                        }else{
                                            if (s==1) {
                                                num6 += p1
                                            }else{
                                                num5+=p1
                                            }
                                        }
                                        bcount++
                                    }
                                    if(num5=="-"){
                                        num5="-1"
                                    }
                                    num5=(num5.toDouble()*resistances[cnt].toDouble()).toString()
                                    equtn+="+"+num5+num6
                                }else {
                                    equtn+="+"+resistances[cnt]+current1[cnt]
                                }
                                p=1
                                if (loop.length==3){
                                    resistances.removeAt(cnt)
                                    method1.removeAt(cnt)
                                    current1.removeAt(cnt)
                                }
                                break
                            }
                        }

                    }
                    else if(Inverse(method)==loop[count].toString()+loop[count+1].toString()){
                        if (Isnumeric(current1[cnt])==true){
                            if (Isnumeric(resistances[cnt])==true){
                                equtn+="+-"+(resistances[cnt].toDouble()*current1[cnt].toDouble()).toString()
                                p=1
                                if (loop.length==3){
                                    resistances.removeAt(cnt)
                                    method1.removeAt(cnt)
                                    current1.removeAt(cnt)
                                }
                                break
                            }
                            else{
                                if (Isnumeric(resistances[cnt][0].toString())==true){
                                    var num5=""
                                    var num6=""
                                    var s=0
                                    for(p1 in resistances[cnt]){
                                        if (Isnumeric(p1.toString())==false){
                                            num6+=p1
                                            s=1
                                        }else{
                                            if (s==1) {
                                                num6 += p1
                                            }else{
                                                num5+=p1
                                            }
                                        }
                                    }
                                    num5=(num5.toDouble()*current1[cnt].toDouble()).toString()
                                    equtn+="+-"+num5+num6
                                }else {
                                    equtn+="+-"+current1[cnt]+resistances[cnt]
                                }
                                p=1
                                if (loop.length==3){
                                    resistances.removeAt(cnt)
                                    method1.removeAt(cnt)
                                    current1.removeAt(cnt)
                                }
                                break
                            }
                        }
                        else{
                            if (Isnumeric(resistances[cnt])==true){
                                if (Isnumeric(current1[cnt][0].toString())==true|| current1[cnt][0]=='-'){
                                    var num5=""
                                    var num6=""
                                    var s=0
                                    var bcount=0
                                    for(p1 in current1[cnt]){
                                        if (Isnumeric(p1.toString())==false && current1[cnt][bcount]!='-'){
                                            num6+=p1
                                            s=1
                                        }else{
                                            if (s==1) {
                                                num6 += p1
                                            }else{
                                                num5+=p1
                                            }
                                        }
                                        bcount+=1
                                    }
                                    if(num5=="-"){
                                        num5="-1"
                                    }
                                    num5=(num5.toDouble()*resistances[cnt].toDouble()).toString()
                                    equtn+="+-"+num5+num6
                                }else {
                                    equtn+="+-"+resistances[cnt]+current1[cnt]
                                }
                                p=1
                                if(loop.length==3){
                                    resistances.removeAt(cnt)
                                    method1.removeAt(cnt)
                                    current1.removeAt(cnt)
                                }
                                break
                            }
                        }

                    }
                    cnt+=1
                }
                if(p==0){
                    cnt=0
                    for (method in method2){
                        if (method==loop[count].toString()+loop[count+1].toString()){
                            if (Isnumeric(voltages[cnt])==true){

                                equtn+="+-"+voltages[cnt]
                                p=1
                                if (loop.length==3){
                                    voltages.removeAt(cnt)
                                    method2.removeAt(cnt)
                                    current2.removeAt(cnt)
                                }
                                break
                            }
                            else{
                                equtn+="+-"+voltages[cnt]
                                p=1
                                if (loop.length==3){
                                    voltages.removeAt(cnt)
                                    method2.removeAt(cnt)
                                    current2.removeAt(cnt)
                                }
                                break
                            }
                        }
                        else if(Inverse(method)==loop[count].toString()+loop[count+1].toString()){
                            if (Isnumeric(voltages[cnt])==true){
                                equtn+="+"+voltages[cnt]
                                p=1
                                if (loop.length==3){
                                    voltages.removeAt(cnt)
                                    method2.removeAt(cnt)
                                    current2.removeAt(cnt)
                                }
                                break
                            }else{
                                equtn+="+"+voltages[cnt]
                                p=1
                                if (loop.length==3){
                                    voltages.removeAt(cnt)
                                    method2.removeAt(cnt)
                                    current2.removeAt(cnt)
                                }
                                break
                            }
                        }
                        cnt+=1
                    }
                }
                if (p==0){
                    cnt=0
                    for(method in method3){
                        if (method==loop[count].toString()+loop[count+1].toString()){
                            equtn+="+"+voltage3[cnt]
                            p=1
                            if(loop.length==3){
                                current_sources.removeAt(cnt)
                                method3.removeAt(cnt)
                                voltage3.removeAt(cnt)
                            }
                            break
                        }else if(Inverse(method)==loop[count].toString()+loop[count+1].toString()){
                            equtn+="+-"+voltage3[cnt]
                            p=1
                            if(loop.length==3){
                                current_sources.removeAt(cnt)
                                method3.removeAt(cnt)
                                voltage3.removeAt(cnt)
                            }
                            break
                        }
                        cnt+=1
                    }
                }

            }
            equtn+="=0"
            eqts_loops.add(equtn)
        }
        var resistances=copying(resistances_2,resistances)!!
        var method1=copying(method1_2,method1)!!
        var current1=copying(current1_2,current1)!!
        var voltages=copying(voltages_2,voltages)!!
        var method2=copying(method2_2,method2)!!
        var current2=copying(current2_2,current2)!!
        var current_sources=copying(current_sources_2,current_sources)!!
        var method3=copying(method3_2,method3)!!
        var voltage3=copying(voltage3_2,voltage3)!!



        var eqts_nodes=ArrayList<String>()
        for (node in nodes){
            var equtn:String=""
            var cnt: Int=0
            for (method in method1_2){
                if (method[0].toString()==node){
                    equtn+="+"+current1_2[cnt]
                }
                else if(method[1].toString()==node){
                    equtn+="+-"+current1_2[cnt]
                }
                cnt+=1
            }
            cnt=0
            for(method in method2_2){
                if (method[0].toString()==node){
                    equtn+="+"+current2_2[cnt]
                }
                else if(method[1].toString()==node){
                    equtn+="+-"+current2_2[cnt]
                }
                cnt+=1
            }
            cnt=0
            for (method in method3_2){
                if (method[0].toString()==node){
                    equtn+="+"+current_sources_2[cnt]
                }
                else if (method[1].toString()==node){
                    equtn+="+-"+current_sources_2[cnt]
                }
                cnt+=1
            }
            equtn+="=0"
            eqts_nodes.add(equtn)
        }
        var eqts=ArrayList<String>()
        for (i in eqts_loops){
            eqts.add(i)
        }
        for (i in eqts_nodes){
            eqts.add(i)
        }
        if (eq.size!=0){
            for(k in eq){
                var list1 = k.split(":")
                var eqn=""
                var cnt=0
                for(i in list1){
                    if(cnt==0){
                        eqn+=i
                    }
                    else{
                        var count=0
                        var t=0
                        for(method in method1){
                            if(i==method){
                                t=1
                                if(Isnumeric(current1[count])==true){
                                    if(Isnumeric(resistances[count])==true){
                                        eqn+="+-"+(current1[count].toDouble()*resistances[count].toDouble()).toString()+"=0"
                                    }
                                    else{
                                        if (Isnumeric(resistances[count][0].toString())==true){
                                            var num5=""
                                            var num6=""
                                            var s=0
                                            for(p1 in resistances[count]){
                                                if (Isnumeric(p1.toString())==false){
                                                    num6+=p1
                                                    s=1
                                                }else{
                                                    if (s==1) {
                                                        num6 += p1
                                                    }else{
                                                        num5+=p1
                                                    }
                                                }
                                            }
                                            num5=(current1[count].toDouble()*num5.toDouble()).toString()
                                            eqn+="+-"+num5+num6+"=0"
                                        }else {
                                            eqn += "+-" + current1[count] + resistances[count] +"=0"
                                        }

                                    }
                                }
                                else{
                                    if (Isnumeric(resistances[count])==true){
                                        if (Isnumeric(current1[count][0].toString())==true){
                                            var num5=""
                                            var num6=""
                                            var s=0
                                            for(p1 in current1[count]){
                                                if (Isnumeric(p1.toString())==false){
                                                    num6+=p1
                                                    s=1
                                                }else{
                                                    if (s==1) {
                                                        num6 += p1
                                                    }else{
                                                        num5+=p1
                                                    }
                                                }
                                            }
                                            num5=(num5.toDouble()*resistances[count].toDouble()).toString()
                                            eqn+="+-"+num5+num6+"=0"
                                        }else {
                                            eqn+="+-"+resistances[count]+current1[count]+"=0"
                                        }
                                    }
                                }
                                break
                            }
                            else if(i==Inverse(method)){
                                t=1
                                if(Isnumeric(current1[count])==true){
                                    if(Isnumeric(resistances[count])==true){
                                        eqn+="+"+(current1[count].toDouble()*resistances[count].toDouble()).toString()+"=0"
                                    }
                                    else{
                                        if (Isnumeric(resistances[count][0].toString())==true){
                                            var num5=""
                                            var num6=""
                                            var s=0
                                            for(p1 in resistances[count]){
                                                if (Isnumeric(p1.toString())==false){
                                                    num6+=p1
                                                    s=1
                                                }else{
                                                    if (s==1) {
                                                        num6 += p1
                                                    }else{
                                                        num5+=p1
                                                    }
                                                }
                                            }
                                            num5=(current1[count].toDouble()*num5.toDouble()).toString()
                                            eqn+="+"+num5+num6+"=0"
                                        }else {
                                            eqn += "+" + current1[count] + resistances[count]+"=0"
                                        }

                                    }
                                }
                                else{
                                    if (Isnumeric(resistances[count])==true){
                                        if (Isnumeric(current1[count][0].toString())==true){
                                            var num5=""
                                            var num6=""
                                            var s=0
                                            for(p1 in current1[count]){
                                                if (Isnumeric(p1.toString())==false){
                                                    num6+=p1
                                                    s=1
                                                }else{
                                                    if (s==1) {
                                                        num6 += p1
                                                    }else{
                                                        num5+=p1
                                                    }
                                                }
                                            }
                                            num5=(num5.toDouble()*resistances[count].toDouble()).toString()
                                            eqn+="+"+num5+num6+"=0"
                                        }else {
                                            eqn+="+"+resistances[count]+current1[count]+"=0"
                                        }
                                    }
                                }
                                break
                            }
                            count+=1
                        }
                        if (t==0){
                            count=0
                            for(method in method2){
                                if(i==method){
                                    t=1
                                    eqn+="+-"+voltages[count]+"=0"
                                    break
                                }else if(i==Inverse(method)){
                                    t=1
                                    eqn+="+"+voltages[count]+"=0"
                                    break
                                }
                                count+=1
                            }
                        }
                        if(t==0){
                            count=0
                            for(method in method3){
                                if(i==method){
                                    t=1
                                    eqn+="+-"+voltage3[count]+"=0"
                                    break
                                }else if(i==Inverse(method)){
                                    t=1
                                    eqn+="+"+voltage3[count]+"=0"
                                    break
                                }
                                count+=1
                            }
                        }
                    }
                    cnt+=1
                }
                eqts.add(eqn)
            }
        }

        for(i in eq){
            eqts.add(0,eqts[eqts.size-1])
            eqts.removeAt(eqts.size-1)
        }



        return eqts



    }
    fun get_vars(eqts:ArrayList<String>):ArrayList<String>?{
        var vars=ArrayList<String>()

        for (eqn in eqts){

            var count=0
            for (i in eqn){
                var vr:String=""
                if (Isnumeric(i.toString())==false && i.toString()!="+" && i.toString()!="-"&&i.toString()!="="&& i.toString()!="."){
                    var n=count
                    while(true){
                        if (eqn[n].toString()!="+"&&eqn[n].toString()!="="){
                            vr+=eqn[n].toString()
                            n+=1
                        }else{
                            break
                        }
                    }
                    if(vr!=""){
                        if (vars.contains(vr)){
                        }else{
                            vars.add(vr)
                        }
                    }
                }
                count+=1
            }
        }
        return vars
    }
    fun add_same(eqts:ArrayList<String>,vars:ArrayList<String>):ArrayList<String>?{
        var nw_eqns=ArrayList<String>()
        for (eqn in eqts){
            var nw_eqn=""
            for(vr in vars) {
                var str_indx=-1
                var sum=0.00
                var a = Count(eqn, vr)!!
                if (a>=1) {
                    while (a > 0) {
                        var indx = eqn.indexOf(vr, str_indx + 1)
                        str_indx = indx
                        var num = ""
                        for (i in (indx-1).downTo(0)) {
                            if (eqn[i] == '+') {
                                if (num==""){
                                    num="1"
                                }else if (num=="-"){
                                    num="1-"
                                }
                                break
                            } else {
                                num += eqn[i]
                            }
                        }
                        num = Inverse(num)!!
                        if (num[0]=='-'){
                            if(num[1]=='-'){
                                num=num.replace("-","")
                                if(num.length==0){
                                    num="1"
                                }
                                sum += num.toDouble()
                            }else{
                                num=num.replace("-","")
                                if(num.length==0){
                                    num="1"
                                }
                                sum += -1*num.toDouble()
                            }
                        }else{
                            sum += num.toDouble()
                        }
                        a -= 1
                    }
                    nw_eqn+="+"+sum.toString()+vr
                }
            }
            nw_eqns.add(nw_eqn)
        }
        var cnt=0
        for (eqn in eqts){
            var list1=eqn.split("+")
            var sum=0.0
            for (term in list1){
                try{
                    if (term[0]=='-'){
                        if (term[1]=='-') {
                            var a = term.replace("-", "")
                            var b = a
                            if ("=0" in a) {
                                b = a.replace("=0", "")
                            }
                            sum += b.toDouble()
                        }else{
                            var a = term.replace("-", "")
                            var b = a
                            if ("=0" in a) {
                                b = a.replace("=0", "")
                            }
                            sum -= b.toDouble()
                        }
                    }
                    else{
                        var b=term.replace("=0","")
                        sum+=b.toDouble()
                    }
                }catch(ex:Exception){
                }
            }
            if (sum!=0.0){
                nw_eqns[cnt]+="+"+sum.toString()
            }
            nw_eqns[cnt]+="=0"
            cnt+=1
        }

        return nw_eqns
    }
    fun extracting_operators(eqns:ArrayList<String>,vars:ArrayList<String>):ArrayList<DoubleArray>?{
        var list001=ArrayList<String>()
        var a=0
        var b=0
        var c=0
        var d=0
        var e=0
        var cont=0
        var num=""
        var count=0
        var list7=ArrayList<String>()
        for(i in eqns){
            for(p in vars){
                if (p in i){
                    var indx=i.indexOf(p)
                    var operator=""
                    count=indx-1
                    while(true){
                        if (i[indx-1]=='+' || i[indx-1]=='-' || count+1==0){
                            if(i[indx-1]=='-'){
                                operator="1-"
                                break
                            }else{
                                operator="1"
                                break
                            }
                        }else{
                            if(i[count]=='+'||i[count]=='-'){
                                if(i[count]=='-'){
                                    operator+="-"
                                }else if(count==0){
                                    operator+=i[count]
                                }
                                break
                            }else{
                                operator+=i[count]
                                if(count==0){
                                    break
                                }
                            }
                        }
                        count-=1
                    }
                    list001.add(operator)
                }else {
                    list001.add("0")
                }
            }

            num="-"
            var s=0
            a=0
            b=0
            c=0
            d=0
            e=0
            count=0
            for(aa in i){
                if(s==1){
                    s=0
                    continue
                }else{
                    if(aa=='+'||aa=='-'){
                        if(aa=='-'){
                            b=1
                            num+=aa
                        }else{
                            cont+=1
                            a=1
                        }
                        if (a==1 && d==1 &&(c==1 || cont==2||b==1||e==1)){
                            break
                        }

                    }else if(Isnumeric(aa.toString())==true){
                        d=1
                        num+=aa
                    }else if(aa=='='){
                        c=1
                        if (a==1 && d==1 &&(c==1 || cont==2 || b==1 || e==1)){
                            break
                        }
                    }else if(aa=='.'){
                        num+=aa
                    }else if(Isnumeric(aa.toString())==false){
                        a=0
                        b=0
                        c=0
                        d=0
                        e=0
                        cont=0
                        num="-"
                        s=1
                    }else{
                        a=0
                        b=0
                        c=0
                        d=0
                        e=0
                        cont=0
                        num="-"
                    }
                }
            }
            list7.add(num)
        }
        var cnt=0
        var cnt2=0
        var mult=1
        var list1=ArrayList<String>()
        for(i in list001){
            var s=Inverse(list001[cnt]!!)!!
            if(s[0]=='+'){
                var m=s.replace("+","")
                list1.add(m)
            }else{
                list1.add(s)
            }
            if (cnt==mult*vars.size-1){
                if(Count(list7[cnt2],"-")==2){
                    var h=list7[cnt2].replace("-","")
                    list1.add(h)
                }else{
                    list1.add(list7[cnt2])
                }
                cnt2+=1
                mult+=1
            }
            cnt+=1
        }
        var list3:ArrayList<DoubleArray> = arrayListOf()
        var m=0
        while(m <=list1.size-1){
            var list2=ArrayList<Double>()
            for(cg in 0..vars.size){
                list2.add(list1[m].toDouble())
                m+=1
            }
            list3.add(list2.toDoubleArray())
        }
        return list3

    }
    fun Removing_extra_eqns_Solving(args:ArrayList<DoubleArray>,vars:ArrayList<String>):ArrayList<Double>?{
        var remain=1.0
        var result:ArrayList<Double> = arrayListOf()
        for(l in args){
            result.add(l[l.size-1])
        }
        var eqns:ArrayList<DoubleArray> = arrayListOf()
        var count=0
        var y=args[0].size-1
        var g=args.size
        for(i in args) {
            var a: ArrayList<Double> = arrayListOf()
            for (j in 0..i.size - 2) {
                a.add(i[j])
            }
            for (j in 0..g-1) {

                if (j == count) {
                    a.add(1.0)
                } else {
                    a.add(0.0)
                }
            }
            eqns.add(a.toDoubleArray())
            count += 1
        }
        //eqns have now operators with out abs and 100 , 010 , 001 are added!!
        var list1:ArrayList<Double> = arrayListOf()
        for(n in 0..2*y-1){
            list1.add(0.0)
        }
        for( i in 0..y-1){

            if(eqns[i][i]==1.0){
            }else if(eqns[i][i]==0.0){
                // for
                if(eqns[i][i]==0.0 && i!=g-1){
                    for(mn in i+1..g-1) {
                        if(eqns[mn][i]!=0.0) {
                            var temp = eqns[i]
                            eqns[i] = eqns[mn]
                            eqns[mn] = temp
                            break
                        }
                    }
                }//else if(eqns[i][i]==0.0 && i!=0){
                //   var temp=eqns[i]
                //   eqns[i]=eqns[i-1]
                //   eqns[i-1]=temp
                //}

            }

            if (eqns[i][i]!=0.0||eqns[i][i]!=-0.0){
                remain*=eqns[i][i]
                var argsii=eqns[i][i]
                for(h in 0..2*y-1){
                    var l=eqns[i][h]/argsii
                    eqns[i][h]=l
                }
            }
            var n=i
            for(v in i..g-2){
                list1= arrayListOf()
                var s=eqns[n+1][i]
                for(k in eqns[i]){
                    list1.add(-k*s)
                }
                for(counter in 0..eqns[0].size-1){
                    eqns[n+1][counter]=eqns[n+1][counter]+list1[counter]
                }
                n+=1
            }
        }

        count=0
        var cnt=0
        var cnt_eqn=0
        try {
            for (i in eqns) {
                for (j in 0..y - 1) {
                    if (i[j] == 0.0) {
                        count += 1
                    }
                    if (count == y) {
                        eqns.removeAt(cnt)
                        result.removeAt(cnt)
                        cnt_eqn += 1
                    }
                }
                count = 0
                cnt += 1
            }
        }catch(ex:Exception){}
        count=0

        while(true) {
            for (i in eqns) {
                cnt = 0
                for (j in 0..count - 1) {
                    if (i[j] == 0.0) {
                        cnt += 1
                    }
                }
                if (cnt == count) {
                } else {
                    var temp = eqns[cnt]
                    eqns[cnt] = eqns[count]
                    eqns[count] = temp
                }
                count += 1
            }
            var v=0
            var cnt2=0
            var n=0
            for(i in eqns){
                for(j in 0..v-1){
                    if(i[j]==0.0){
                        cnt2+=1
                    }
                }
                if(cnt2==count){
                    n+=1
                }else{
                    break
                }
                v+=1
            }
            if(n==v){
                break
            }
        }
        while(eqns.size>vars.size){
            cnt_eqn+=1
            var nk=eqns.size
            eqns.removeAt(nk-1)
            result.removeAt(nk-1)
        }





        var new_eqns:ArrayList<DoubleArray> = arrayListOf()
        for (i in eqns){
            var a:ArrayList<Double> = arrayListOf()
            for(j in 0..i.size-1-cnt_eqn){
                a.add(i[j])
            }
            new_eqns.add(a.toDoubleArray())
        }
        list1= arrayListOf()
        y=new_eqns.size
        for(n in 0..2*y-1){
            list1.add(0.0)
        }
        for(i in y-1 downTo 0){
            if(new_eqns[i][i]==1.0){
            }else if(new_eqns[i][i]==0.0){
                for(j in new_eqns){
                    if (new_eqns[i][i]==0.0 && i!=y-1){
                        var temp=new_eqns[i]
                        new_eqns[i]=new_eqns[i+1]
                        new_eqns[i+1]=temp
                    }else if(new_eqns[i][i]==0.0 && i!=0){
                        var temp=new_eqns[i]
                        new_eqns[i]=new_eqns[i-1]
                        new_eqns[i-1]=temp
                    }
                }
            }
            if(new_eqns[i][i]!=0.0){
                remain*=new_eqns[i][i]
                var argsii=new_eqns[i][i]
                for(h in 0..2*y-1){
                    var l=new_eqns[i][h]/argsii
                    new_eqns[i][h]=l
                }
            }
            var n=i
            for(v in i downTo 1){
                list1= arrayListOf()
                var s=new_eqns[n-1][i]
                for(k in new_eqns[i]){
                    list1.add(-k*s)
                }
                var counter=0
                for(counter in 0..new_eqns[0].size-1){
                    new_eqns[n-1][counter]=new_eqns[n-1][counter]+list1[counter]
                }
                n-=1
            }
        }






        var inverse:ArrayList<DoubleArray> = arrayListOf()
        g=new_eqns.size
        for(m in 0..y-1){
            var list2:ArrayList<Double> = arrayListOf()
            for(j in g..2*g-1){
                list2.add(new_eqns[m][j])
            }
            inverse.add(list2.toDoubleArray())
        }

        //////////////////////////////////////////solving three equations
        var res:ArrayList<Double> = arrayListOf()
        var sum5=0.0
        for(list0 in inverse){
            sum5=0.0
            for(counter in 0..y-1){
                sum5+=list0[counter]*result[counter]
            }
            res.add(sum5)
        }
        return res

        ////////////////////////////////////////
    }
    fun voltages(vars:ArrayList<String>, values:ArrayList<Double>, resistances: ArrayList<String>, method1: ArrayList<String>, current1: ArrayList<String>)
            :ArrayList<String>?{
        var count=0
        var voltages:ArrayList<String> = arrayListOf()
        for(i in resistances){
            if(Isnumeric(resistances[count])==true){
                if(Isnumeric(current1[count])==true){
                    voltages.add(resistances[count]+":"+method1[count]+":"+(resistances[count].toDouble()*current1[count].toDouble()).toString()+"V")
                }else{
                    var a:Double=1.0
                    var cnt=0
                    for(j in vars){
                        if(j==current1[count]){
                            a=values[cnt]
                            break
                        }else if(j in current1[count]){
                            var num5=""
                            for(ll in current1[count]){
                                if(Isnumeric(ll.toString())==false&&ll!='-'){
                                    break
                                }
                                num5+=ll
                            }
                            if(num5=="-"){
                                num5="-1"
                            }else if(num5==""){
                                num5="1"
                            }
                            a*=num5.toDouble()
                            a*=values[cnt]
                            break
                        }
                        cnt+=1
                    }
                    voltages.add(resistances[count]+":"+method1[count]+":"+(resistances[count].toDouble()*a).toString()+"V")
                }
            }else{
                if(Isnumeric(current1[count])==true){
                    var a:Double=1.0
                    var cnt=0
                    for(j in vars){
                        if(j==resistances[count]){
                            a=values[cnt]
                            break
                        }else if(j in resistances[count]){
                            var num5=""
                            for(ll in resistances[count]){
                                if(Isnumeric(ll.toString())==false&&ll!='-'){
                                    break
                                }
                                num5+=ll
                            }
                            if(num5=="-"){
                                num5="-1"
                            }
                            a=num5.toDouble()
                            a*=values[cnt]
                            break
                        }
                        cnt+=1
                    }
                    voltages.add(resistances[count]+":"+method1[count]+":"+(a*current1[count].toDouble()).toString()+"V")
                }
            }
            count++
        }
        return voltages
    }
    fun power(resistances: ArrayList<String>, method1: ArrayList<String>, current1: ArrayList<String>, voltages: ArrayList<String>,
              method2: ArrayList<String>, current2: ArrayList<String>, current_sources:ArrayList<String>, method3: ArrayList<String>,
              voltage3: ArrayList<String>, vars: ArrayList<String>, values: ArrayList<Double>):ArrayList<String>?  {
        var power:ArrayList<String> = arrayListOf()
        var count=0
        for(i in resistances){
            if(Isnumeric(i)==true){
                if(Isnumeric(current1[count])==true){
                    power.add(i+":"+method1[count]+":"+(i.toDouble()*current1[count].toDouble()*current1[count].toDouble()).toString()+"W")
                }else{
                    var a=1.0
                    var cnt=0
                    for( j in vars){
                        if(j==current1[count]){
                            a=values[cnt]
                            break
                        }else if(j in current1[count]){
                            var num5=""
                            for(ll in current1[count]){
                                if(Isnumeric(ll.toString())==false&&ll!='-'){
                                    break
                                }
                                num5+=ll
                            }
                            if(num5=="-"){
                                num5="-1"
                            }else if(num5==""){
                                num5="1"
                            }
                            a=num5.toDouble()
                            a*=values[cnt]
                            break
                        }
                        cnt++
                    }
                    power.add(i+":"+method1[count]+":"+(i.toDouble()*a*a).toString()+"W")
                }
            }else{
                if(Isnumeric(current1[count])==true){
                    var cnt=0
                    var a=1.0
                    for(j in vars){
                        if(j==i){
                            a=values[cnt]
                            break
                        }else if(j in resistances[count]){
                            var num5=""
                            for(ll in resistances[count]){
                                if(Isnumeric(ll.toString())==false&&ll!='-'){
                                    break
                                }
                                num5+=ll
                            }
                            if(num5=="-"){
                                num5="-1"
                            }else if(num5==""){
                                num5="1"
                            }
                            a*=num5.toDouble()
                            a*=values[cnt]
                            break
                        }
                        cnt++
                    }
                    power.add(i+":"+method1[count]+":"+(a*current1[count].toDouble()*current1[count].toDouble()).toString()+"W")
                }
            }
            count++
        }
        count=0
        for(i in voltages){
            if(Isnumeric(i)==true){
                if(Isnumeric(current2[count])==true){
                    power.add(i+":"+method2[count]+":"+(-i.toDouble()*current2[count].toDouble()).toString()+"W")
                }
                else{
                    var cnt=0
                    var a=1.0
                    for(j in vars){
                        if (j==current2[count]){
                            a=values[cnt]
                            break
                        }else if(j in current2[count]){
                            var num5=""
                            for(ll in current2[count]){
                                if(Isnumeric(ll.toString())==false&&ll!='-'){
                                    break
                                }
                                num5+=ll
                            }
                            if(num5=="-"){
                                num5="-1"
                            }else if(num5==""){
                                num5="1"
                            }
                            a*=num5.toDouble()
                            a*=values[cnt]
                            break
                        }
                        cnt++
                    }
                    power.add(i+":"+method2[count]+":"+(-i.toDouble()*a).toString()+"W")
                }
            }
            else{
                if(Isnumeric(current2[count])==true){
                    var k=i
                    var cnt=0
                    var a=1.0
                    var num=1.0
                    if(Isnumeric(i[0].toString())==true){
                        var num5=""
                        var num6=""
                        var p=0
                        for(l in i){
                            if(Isnumeric(l.toString())==true){
                                if (p==0){
                                    num5+=l
                                }else{
                                    num6+=l
                                    p=1
                                }
                            }
                            else{
                                num6+=l
                                p=1
                            }
                        }
                        num*=num5.toDouble()
                        k=num6
                    }
                    for(j in vars){
                        if(j==k){
                            a=values[cnt]
                            break
                        }
                        cnt++
                    }
                    power.add(voltages[count]+":"+method2[count]+":"+(-a*num*current2[count].toDouble()).toString()+"W")
                }
                else{
                    var a=0.0
                    var cnt=0
                    var k=i
                    var num=1.0
                    if(Isnumeric(i[0].toString())==true){
                        var num5=""
                        var num6=""
                        var p=0
                        for(l in i){
                            if(Isnumeric(l.toString())==true){
                                if (p==0){
                                    num5+=l
                                }else{
                                    num6+=l
                                    p=1
                                }
                            }
                            else{
                                num6+=l
                                p=1
                            }
                        }
                        num*=num5.toDouble()
                        k=num6
                    }
                    for(s in vars){
                        if (k==s){
                            a=values[cnt]
                            break
                        }
                        cnt++
                    }
                    cnt=0
                    var b=0.0
                    for(s in vars){
                        if(s==current2[count]){
                            b=values[cnt]
                            break
                        }
                        cnt++
                    }
                    power.add(voltages[count]+":"+method2[count]+":"+(-a*num*b).toString()+"W")
                }
            }
            count++
        }
        count=0
        for(i in current_sources){
            if(Isnumeric(i)==true){
                var cnt=0
                var a=0.0
                for(j in vars){
                    if(j==voltage3[count]){
                        a=values[cnt]
                        break
                    }
                    cnt++
                }
                power.add(current_sources[count]+":"+method3[count]+":"+(a*current_sources[count].toDouble()).toString()+"W")
            }else{
                var k=i
                var num=1.0
                if(Isnumeric(i[0].toString())==true){
                    var p=0
                    var num5=""
                    var num6=""
                    for(l in i){
                        if(Isnumeric(l.toString())==true){
                            if (p==0){
                                num5+=l
                            }else{
                                num6+=l
                                p=1
                            }
                        }
                        else{
                            num6+=l
                            p=1
                        }
                    }
                    k=num6
                    num*=num5.toDouble()
                }
                var cnt=0
                var a=0.0
                for(s in vars){
                    if(s==k){
                        a=values[cnt]
                        break
                    }
                    cnt++
                }
                cnt=0
                var b=0.0
                for( n in vars){
                    if (n==voltage3[count]){
                        b=values[cnt]
                        break
                    }
                    cnt++
                }
                power.add(current_sources[count]+":"+method3[count]+":"+(a*num*b).toString()+"W")
            }
            count+=1
        }
        return power
    }

}
var l=0
class MainActivity : AppCompatActivity() {

    lateinit var mAdView : AdView
    var resistances:ArrayList<String> = arrayListOf()
    var method1:ArrayList<String> = arrayListOf()
    var current1:ArrayList<String> = arrayListOf()
    var voltages:ArrayList<String> = arrayListOf()
    var method2:ArrayList<String> = arrayListOf()
    var current2:ArrayList<String> = arrayListOf()
    var current_sources:ArrayList<String> = arrayListOf()
    var method3:ArrayList<String> = arrayListOf()
    var voltages3:ArrayList<String> = arrayListOf()
    var eq:ArrayList<String> = arrayListOf()
    var nodes:ArrayList<String> = arrayListOf()
    var loops: ArrayList<String> = arrayListOf()
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        if(l==0) {
            val intent = Intent(this, MainActivity3::class.java)
            startActivity(intent)
            l = 1
        }
        if(l==1){
            setContentView(R.layout.activity_main)
            MobileAds.initialize(this) {}
            mAdView = findViewById(R.id.adView)
            val adRequest = AdRequest.Builder().build()
            mAdView.loadAd(adRequest)
        }
        ///////////////////////////////////////////////////////////
    }
    fun bt_save(){
        try {

            var cnt = 1
            var sharedPreferences1 = getSharedPreferences("resistances", Context.MODE_PRIVATE)
            var editor1 = sharedPreferences1.edit()
            editor1.clear()
            editor1.apply()
            var sharedPreferences2 = getSharedPreferences("method1", Context.MODE_PRIVATE)
            var editor2 = sharedPreferences2.edit()
            editor2.clear()
            editor2.apply()
            var sharedPreferences3 = getSharedPreferences("current1", Context.MODE_PRIVATE)
            var editor3 = sharedPreferences3.edit()
            editor3.clear()
            editor3.apply()
            var sharedPreferences4 = getSharedPreferences("voltages", Context.MODE_PRIVATE)
            var editor4 = sharedPreferences4.edit()
            editor4.clear()
            editor4.apply()
            var sharedPreferences5 = getSharedPreferences("method2", Context.MODE_PRIVATE)
            var editor5 = sharedPreferences5.edit()
            editor5.clear()
            editor5.apply()
            var sharedPreferences6 = getSharedPreferences("current2", Context.MODE_PRIVATE)
            var editor6 = sharedPreferences6.edit()
            editor6.clear()
            editor6.apply()
            var sharedPreferences7 = getSharedPreferences("current_sources", Context.MODE_PRIVATE)
            var editor7 = sharedPreferences7.edit()
            editor7.clear()
            editor7.apply()
            var sharedPreferences8 = getSharedPreferences("method3", Context.MODE_PRIVATE)
            var editor8 = sharedPreferences8.edit()
            editor8.clear()
            editor8.apply()
            var sharedPreferences9 = getSharedPreferences("voltages3", Context.MODE_PRIVATE)
            var editor9 = sharedPreferences9.edit()
            editor9.clear()
            editor9.apply()
            var sharedPreferences10 = getSharedPreferences("eqns", Context.MODE_PRIVATE)
            var editor10 = sharedPreferences10.edit()
            editor10.clear()
            editor10.apply()
            var sharedPreferences11 = getSharedPreferences("nodes", Context.MODE_PRIVATE)
            var editor11 = sharedPreferences11.edit()
            editor11.clear()
            editor11.apply()
            var sharedPreferences12 = getSharedPreferences("loops", Context.MODE_PRIVATE)
            var editor12 = sharedPreferences12.edit()
            editor12.clear()
            editor12.apply()

            var count = 1
            for (i in resistances) {
                var editor = sharedPreferences1.edit()
                editor.putString("Res" + count.toString(), i)
                editor.apply()
                count++
            }
            count = 1
            for (i in method1) {
                var editor = sharedPreferences2.edit()
                editor.putString("Meth" + count.toString(), i)
                editor.apply()
                count++
            }
            count = 1
            for (i in current1) {
                var editor = sharedPreferences3.edit()
                editor.putString("Cur" + count.toString(), i)
                editor.apply()
                count++
            }
            count = 1
            for (i in voltages) {
                var editor = sharedPreferences4.edit()
                editor.putString("Volt" + count.toString(), i)
                editor.apply()
                count++
            }
            count = 1
            for (i in method2) {
                var editor = sharedPreferences5.edit()
                editor.putString("Meth" + count.toString(), i)
                editor.apply()
                count++
            }
            count = 1
            for (i in current2) {
                var editor = sharedPreferences6.edit()
                editor.putString("Cur" + count.toString(), i)
                editor.apply()
                count++
            }
            count = 1
            for (i in current_sources) {
                var editor = sharedPreferences7.edit()
                editor.putString("Cur" + count.toString(), i)
                editor.apply()
                count++
            }
            count = 1
            for (i in method3) {
                var editor = sharedPreferences8.edit()
                editor.putString("Meth" + count.toString(), i)
                editor.apply()
                count++
            }
            count = 1
            for (i in voltages3) {
                var editor = sharedPreferences9.edit()
                editor.putString("Volt" + count.toString(), i)
                editor.apply()
                count++
            }
            count = 1
            for (i in eq) {
                var editor = sharedPreferences10.edit()
                editor.putString("Eq" + count.toString(), i)
                editor.apply()
                count++
            }
            count = 1
            for (i in nodes) {
                var editor = sharedPreferences11.edit()
                editor.putString("Node" + count.toString(), i)
                editor.apply()
                count++
            }
            count = 1
            for (i in loops) {
                var editor = sharedPreferences12.edit()
                editor.putString("Loop" + count.toString(), i)
                editor.apply()
                count++
            }
        }catch (ex:Exception){
        }
    }
    fun bt_recent(view:View){
        ////////////////////////////// new
        try {
            resistances = arrayListOf()
            method1 = arrayListOf()
            current1 = arrayListOf()
            voltages = arrayListOf()
            method2 = arrayListOf()
            current2 = arrayListOf()
            current_sources = arrayListOf()
            method3 = arrayListOf()
            voltages3 = arrayListOf()
            eq = arrayListOf()
            nodes = arrayListOf()
            loops = arrayListOf()
            if (count_tab != 0) {
                count_tab = 0
                count_radio = 0
                radio_value.setText("Value")
                radio_method.setText("Method")
                radio_current.setText("Current")
                radio_value.isChecked = true
                previous.isEnabled = false
                textview_title.setText("Resistances")
                next.setText("Next")
            }
            val my_adapter10 = ArrayAdapter(this, android.R.layout.simple_list_item_1, arrayListOf<String>())
            List1.adapter = my_adapter10
            val my_adapter20 = ArrayAdapter(this, android.R.layout.simple_list_item_1, arrayListOf<String>())
            List2.adapter = my_adapter20
            val my_adapter30 = ArrayAdapter(this, android.R.layout.simple_list_item_1, arrayListOf<String>())
            List3.adapter = my_adapter30
            //////////////////////////////////////recent
            var sharedPreferences1 = getSharedPreferences("resistances", Context.MODE_PRIVATE)
            var count = 1
            while (true) {
                var value = sharedPreferences1.getString("Res" + count.toString(), "None").toString()
                if (value == "None") {
                    break
                }
                resistances.add(value)
                count++
            }
            val my_adapter1 = ArrayAdapter(this, android.R.layout.simple_list_item_1, resistances)
            List1.adapter = my_adapter1

            var sharedPreferences2 = getSharedPreferences("method1", Context.MODE_PRIVATE)
            count = 1
            while (true) {
                var value = sharedPreferences2.getString("Meth" + count.toString(), "None").toString()
                if (value == "None") {
                    break
                }
                method1.add(value)
                count++
            }
            val my_adapter2 = ArrayAdapter(this, android.R.layout.simple_list_item_1, method1)
            List2.adapter = my_adapter2


            var sharedPreferences3 = getSharedPreferences("current1", Context.MODE_PRIVATE)
            count = 1
            while (true) {
                var value = sharedPreferences3.getString("Cur" + count.toString(), "None").toString()
                if (value == "None") {
                    break
                }
                current1.add(value)
                count++
            }
            val my_adapter3 = ArrayAdapter(this, android.R.layout.simple_list_item_1, current1)
            List3.adapter = my_adapter3


            var sharedPreferences4 = getSharedPreferences("voltages", Context.MODE_PRIVATE)
            count = 1
            while (true) {
                var value = sharedPreferences4.getString("Volt" + count.toString(), "None").toString()
                if (value == "None") {
                    break
                }
                voltages.add(value)
                count++
            }


            var sharedPreferences5 = getSharedPreferences("method2", Context.MODE_PRIVATE)
            count = 1
            while (true) {
                var value = sharedPreferences5.getString("Meth" + count.toString(), "None").toString()
                if (value == "None") {
                    break
                }
                method2.add(value)
                count++
            }

            var sharedPreferences6 = getSharedPreferences("current2", Context.MODE_PRIVATE)
            count = 1
            while (true) {
                var value = sharedPreferences6.getString("Cur" + count.toString(), "None").toString()
                if (value == "None") {
                    break
                }
                current2.add(value)
                count++
            }

            var sharedPreferences7 = getSharedPreferences("current_sources", Context.MODE_PRIVATE)
            count = 1
            while (true) {
                var value = sharedPreferences7.getString("Cur" + count.toString(), "None").toString()
                if (value == "None") {
                    break
                }
                current_sources.add(value)
                count++
            }

            var sharedPreferences8 = getSharedPreferences("method3", Context.MODE_PRIVATE)
            count = 1
            while (true) {
                var value = sharedPreferences8.getString("Meth" + count.toString(), "None").toString()
                if (value == "None") {
                    break
                }
                method3.add(value)
                count++
            }


            var sharedPreferences9 = getSharedPreferences("voltages3", Context.MODE_PRIVATE)
            count = 1
            while (true) {
                var value = sharedPreferences9.getString("Volt" + count.toString(), "None").toString()
                if (value == "None") {
                    break
                }
                voltages3.add(value)
                count++
            }

            var sharedPreferences10 = getSharedPreferences("eqns", Context.MODE_PRIVATE)
            count = 1
            while (true) {
                var value = sharedPreferences10.getString("Eq" + count.toString(), "None").toString()
                if (value == "None") {
                    break
                }
                eq.add(value)
                count++
            }

            var sharedPreferences11 = getSharedPreferences("nodes", Context.MODE_PRIVATE)
            count = 1
            while (true) {
                var value = sharedPreferences11.getString("Node" + count.toString(), "None").toString()
                if (value == "None") {
                    break
                }
                nodes.add(value)
                count++
            }


            var sharedPreferences12 = getSharedPreferences("loops", Context.MODE_PRIVATE)
            count = 1
            while (true) {
                var value = sharedPreferences12.getString("Loop" + count.toString(), "None").toString()
                if (value == "None") {
                    break
                }
                loops.add(value)
                count++
            }
        }catch(ex:Exception){}
    }
    var count_tab=0
    var count_radio=0
    fun next_com(view:View){
        try {
            if (count_tab == 0) {
                textview_title.setText("Voltages")
                count_tab = 1
                previous.isEnabled = true
                count_radio = 0
                radio_value.isChecked = true
                val my_adapter1 = ArrayAdapter(this, android.R.layout.simple_list_item_1, voltages)
                List1.adapter = my_adapter1
                val my_adapter2 = ArrayAdapter(this, android.R.layout.simple_list_item_1, method2)
                List2.adapter = my_adapter2
                val my_adapter3 = ArrayAdapter(this, android.R.layout.simple_list_item_1, current2)
                List3.adapter = my_adapter3
                //val intent = Intent(this,MainActivity2::class.java)
                //startActivity(intent)
                //val intent = Intent(this, MainActivityResults::class.java)
                // intent.putExtra("results",list_results)
                //startActivity(intent)
            } else if (count_tab == 1) {
                textview_title.setText("Current  Src")
                count_tab = 2
                count_radio = 0
                radio_value.isChecked = true
                radio_current.setText("Voltage")
                val my_adapter1 =
                    ArrayAdapter(this, android.R.layout.simple_list_item_1, current_sources)
                List1.adapter = my_adapter1
                val my_adapter2 = ArrayAdapter(this, android.R.layout.simple_list_item_1, method3)
                List2.adapter = my_adapter2
                val my_adapter3 = ArrayAdapter(this, android.R.layout.simple_list_item_1, voltages3)
                List3.adapter = my_adapter3
            } else if (count_tab == 2) {
                textview_title.setText("Others")
                next.setText("Result")
                count_tab = 3
                count_radio = 0
                radio_value.isChecked = true
                val my_adapter1 = ArrayAdapter(this, android.R.layout.simple_list_item_1, eq)
                List1.adapter = my_adapter1
                val my_adapter2 = ArrayAdapter(this, android.R.layout.simple_list_item_1, nodes)
                List2.adapter = my_adapter2
                val my_adapter3 = ArrayAdapter(this, android.R.layout.simple_list_item_1, loops)
                List3.adapter = my_adapter3
                radio_value.setText("+eqns")
                radio_method.setText("nodes")
                radio_current.setText("loops")
            } else if (count_tab == 3) {
                bt_save()
                ///////////////////////////////////process
                var list_results: ArrayList<String> = arrayListOf()
                var resistances_2: ArrayList<String> = arrayListOf()
                for (i in resistances) {
                    var count = 0
                    var indx = i.indexOf(".")
                    var num = ""
                    for (j in i) {
                        if (count > indx) {
                            num += j
                        }
                        count++
                    }
                    resistances_2.add(num)
                }
                var method1_2: ArrayList<String> = arrayListOf()
                for (i in method1) {
                    var count = 0
                    var indx = i.indexOf(".")
                    var num = ""
                    for (j in i) {
                        if (count > indx) {
                            num += j
                        }
                        count++
                    }
                    method1_2.add(num)
                }
                var current1_2: ArrayList<String> = arrayListOf()
                for (i in current1) {
                    var count = 0
                    var indx = i.indexOf(".")
                    var num = ""
                    for (j in i) {
                        if (count > indx) {
                            num += j
                        }
                        count++
                    }
                    current1_2.add(num)
                }
                var voltages_2: ArrayList<String> = arrayListOf()
                for (i in voltages) {
                    var count = 0
                    var indx = i.indexOf(".")
                    var num = ""
                    for (j in i) {
                        if (count > indx) {
                            num += j
                        }
                        count++
                    }
                    voltages_2.add(num)
                }
                var method2_2: ArrayList<String> = arrayListOf()
                for (i in method2) {
                    var count = 0
                    var indx = i.indexOf(".")
                    var num = ""
                    for (j in i) {
                        if (count > indx) {
                            num += j
                        }
                        count++
                    }
                    method2_2.add(num)
                }
                var current2_2: ArrayList<String> = arrayListOf()
                for (i in current2) {
                    var count = 0
                    var indx = i.indexOf(".")
                    var num = ""
                    for (j in i) {
                        if (count > indx) {
                            num += j
                        }
                        count++
                    }
                    current2_2.add(num)
                }
                var current_sources_2: ArrayList<String> = arrayListOf()
                for (i in current_sources) {
                    var count = 0
                    var indx = i.indexOf(".")
                    var num = ""
                    for (j in i) {
                        if (count > indx) {
                            num += j
                        }
                        count++
                    }
                    current_sources_2.add(num)
                }
                var method3_2: ArrayList<String> = arrayListOf()
                for (i in method3) {
                    var count = 0
                    var indx = i.indexOf(".")
                    var num = ""
                    for (j in i) {
                        if (count > indx) {
                            num += j
                        }
                        count++
                    }
                    method3_2.add(num)
                }
                var voltages3_2: ArrayList<String> = arrayListOf()
                for (i in voltages3) {
                    var count = 0
                    var indx = i.indexOf(".")
                    var num = ""
                    for (j in i) {
                        if (count > indx) {
                            num += j
                        }
                        count++
                    }
                    voltages3_2.add(num)
                }
                var eq_2: ArrayList<String> = arrayListOf()
                for (i in eq) {
                    var count = 0
                    var indx = i.indexOf(".")
                    var num = "+"
                    for (j in i) {
                        if (count > indx) {
                            num += j
                        }
                        count++
                    }
                    eq_2.add(num)
                }
                var nodes_2: ArrayList<String> = arrayListOf()
                for (i in nodes) {
                    var count = 0

                    var indx = i.indexOf(".")
                    var num = ""
                    for (j in i) {
                        if (count > indx) {
                            num += j
                        }
                        count++
                    }
                    nodes_2.add(num)
                }
                var loops_2: ArrayList<String> = arrayListOf()
                for (i in loops) {
                    var count = 0
                    var indx = i.indexOf(".")
                    var num = ""
                    for (j in i) {
                        if (count > indx) {
                            num += j
                        }
                        count++
                    }
                    loops_2.add(num)
                }
                var a = Kirchoff_app().Kirchoff_solving(
                    nodes_2,
                    loops_2,
                    resistances_2,
                    method1_2,
                    current1_2,
                    voltages_2,
                    method2_2,
                    current2_2,
                    current_sources_2,
                    method3_2,
                    voltages3_2,
                    eq_2
                )!!
                var b = Kirchoff_app().get_vars(a)!!
                var c = Kirchoff_app().add_same(a, b)!!
                var d = Kirchoff_app().extracting_operators(c, b)!!
                var e = Kirchoff_app().Removing_extra_eqns_Solving(d, b)!!
                list_results.add("--------------variables-----------------")
                var count = 0
                for (i in e) {
                    var txt = b[count] + " = " + i
                    list_results.add(txt)
                    count++
                }
                list_results.add("--------------voltages-----------------")
                var f = Kirchoff_app().voltages(b, e!!, resistances_2, method1_2, current1_2)!!
                for (i in f) {
                    list_results.add(i)
                }
                list_results.add("--------------power-----------------")
                var g = Kirchoff_app().power(
                    resistances_2,
                    method1_2,
                    current1_2,
                    voltages_2,
                    method2_2,
                    current2_2,
                    current_sources_2,
                    method3_2,
                    voltages3_2,
                    b,
                    e
                )!!
                for (i in g) {
                    list_results.add(i)
                }

                val intent = Intent(this, MainActivity2::class.java)
                intent.putExtra("results", list_results)
                startActivity(intent)
            }
        }catch(ex:Exception){
        }
    }
    fun previous_com(view:View){
        try {
            if (count_tab == 1) {
                textview_title.setText("Resistances")
                count_tab = 0
                previous.isEnabled = false
                count_radio = 0
                radio_value.isChecked = true
                val my_adapter1 = ArrayAdapter(this, android.R.layout.simple_list_item_1, resistances)
                List1.adapter = my_adapter1
                val my_adapter2 = ArrayAdapter(this, android.R.layout.simple_list_item_1, method1)
                List2.adapter = my_adapter2
                val my_adapter3 = ArrayAdapter(this, android.R.layout.simple_list_item_1, current1)
                List3.adapter = my_adapter3
            } else if (count_tab == 2) {
                textview_title.setText("Voltages")
                radio_current.setText("Current")
                count_tab = 1
                count_radio = 0
                radio_value.isChecked = true
                val my_adapter1 = ArrayAdapter(this, android.R.layout.simple_list_item_1, voltages)
                List1.adapter = my_adapter1
                val my_adapter2 = ArrayAdapter(this, android.R.layout.simple_list_item_1, method2)
                List2.adapter = my_adapter2
                val my_adapter3 = ArrayAdapter(this, android.R.layout.simple_list_item_1, current2)
                List3.adapter = my_adapter3
            } else if (count_tab == 3) {
                radio_value.setText("Value")
                radio_method.setText("Method")
                textview_title.setText("Current Src")
                radio_current.setText("Voltage")
                next.setText("Next")
                count_tab = 2
                count_radio = 0
                radio_value.isChecked = true
                val my_adapter1 = ArrayAdapter(this, android.R.layout.simple_list_item_1, current_sources)
                List1.adapter = my_adapter1
                val my_adapter2 = ArrayAdapter(this, android.R.layout.simple_list_item_1, method3)
                List2.adapter = my_adapter2
                val my_adapter3 = ArrayAdapter(this, android.R.layout.simple_list_item_1, voltages3)
                List3.adapter = my_adapter3
            }
        }catch (ex:Exception){}
    }
    fun value_com(view:View){
        count_radio=0
        //tabLayout.isFocusable=true
    }
    fun method_com(view:View){
        count_radio=1
    }
    fun current_com(view:View){
        count_radio=2
    }
    fun bt_add(view:View){
        try {
            if (textbox.text.toString() != "" && textbox_edit.text.toString() == "") {
                if (count_tab == 0 && count_radio == 0) {
                    resistances.add((resistances.size + 1).toString() + "." + textbox.text.toString())
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, resistances)
                    List1.adapter = my_adapter
                    radio_method.isChecked = true
                    count_radio = 1
                } else if (count_tab == 0 && count_radio == 1) {
                    method1.add((method1.size + 1).toString() + "." + textbox.text.toString())
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, method1)
                    List2.adapter = my_adapter
                    radio_current.isChecked = true
                    count_radio = 2
                } else if (count_tab == 0 && count_radio == 2) {
                    current1.add((current1.size + 1).toString() + "." + textbox.text.toString())
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, current1)
                    List3.adapter = my_adapter
                    radio_value.isChecked = true
                    count_radio = 0
                } else if (count_tab == 1 && count_radio == 0) {
                    voltages.add((voltages.size + 1).toString() + "." + textbox.text.toString())
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, voltages)
                    List1.adapter = my_adapter
                    radio_method.isChecked = true
                    count_radio = 1
                } else if (count_tab == 1 && count_radio == 1) {
                    method2.add((method2.size + 1).toString() + "." + textbox.text.toString())
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, method2)
                    List2.adapter = my_adapter
                    radio_current.isChecked = true
                    count_radio = 2
                } else if (count_tab == 1 && count_radio == 2) {
                    current2.add((current2.size + 1).toString() + "." + textbox.text.toString())
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, current2)
                    List3.adapter = my_adapter
                    radio_value.isChecked = true
                    count_radio = 0
                } else if (count_tab == 2 && count_radio == 0) {
                    current_sources.add((current_sources.size + 1).toString() + "." + textbox.text.toString())
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, current_sources)
                    List1.adapter = my_adapter
                    radio_method.isChecked = true
                    count_radio = 1
                } else if (count_tab == 2 && count_radio == 1) {
                    method3.add((method3.size + 1).toString() + "." + textbox.text.toString())
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, method3)
                    List2.adapter = my_adapter
                    radio_current.isChecked = true
                    count_radio = 2
                } else if (count_tab == 2 && count_radio == 2) {
                    voltages3.add((voltages3.size + 1).toString() + "." + textbox.text.toString())
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, voltages3)
                    List3.adapter = my_adapter
                    radio_value.isChecked = true
                    count_radio = 0
                } else if (count_tab == 3 && count_radio == 0) {
                    eq.add((eq.size + 1).toString() + "." + textbox.text.toString())
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, eq)
                    List1.adapter = my_adapter
                } else if (count_tab == 3 && count_radio == 1) {
                    nodes.add((nodes.size + 1).toString() + "." + textbox.text.toString())
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, nodes)
                    List2.adapter = my_adapter
                } else if (count_tab == 3 && count_radio == 2) {
                    loops.add((loops.size + 1).toString() + "." + textbox.text.toString())
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, loops)
                    List3.adapter = my_adapter
                }
                textbox.setText("")
            } else if (textbox.text.toString() != "" && textbox_edit.text.toString() != "") {
                if (count_tab == 0 && count_radio == 0) {
                    resistances[textbox_edit.text.toString().toInt() - 1] = (textbox_edit.text.toString().toInt()).toString() + "." + textbox.text.toString()
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, resistances)
                    List1.adapter = my_adapter
                } else if (count_tab == 0 && count_radio == 1) {
                    method1[textbox_edit.text.toString().toInt() - 1] = (textbox_edit.text.toString().toInt()).toString() + "." + textbox.text.toString()
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, method1)
                    List2.adapter = my_adapter
                } else if (count_tab == 0 && count_radio == 2) {
                    current1[textbox_edit.text.toString().toInt() - 1] = (textbox_edit.text.toString().toInt()).toString() + "." + textbox.text.toString()
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, current1)
                    List3.adapter = my_adapter
                } else if (count_tab == 1 && count_radio == 0) {
                    voltages[textbox_edit.text.toString().toInt() - 1] = (textbox_edit.text.toString().toInt()).toString() + "." + textbox.text.toString()
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, voltages)
                    List1.adapter = my_adapter
                } else if (count_tab == 1 && count_radio == 1) {
                    method2[textbox_edit.text.toString().toInt() - 1] = (textbox_edit.text.toString().toInt()).toString() + "." + textbox.text.toString()
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, method2)
                    List2.adapter = my_adapter
                } else if (count_tab == 1 && count_radio == 2) {
                    current2[textbox_edit.text.toString().toInt() - 1] = (textbox_edit.text.toString().toInt()).toString() + "." + textbox.text.toString()
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, current2)
                    List3.adapter = my_adapter
                } else if (count_tab == 2 && count_radio == 0) {
                    current_sources[textbox_edit.text.toString().toInt() - 1] = (textbox_edit.text.toString().toInt()).toString() + "." + textbox.text.toString()
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, current_sources)
                    List1.adapter = my_adapter
                } else if (count_tab == 2 && count_radio == 1) {
                    method3[textbox_edit.text.toString().toInt() - 1] = (textbox_edit.text.toString().toInt()).toString() + "." + textbox.text.toString()
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, method3)
                    List2.adapter = my_adapter
                } else if (count_tab == 2 && count_radio == 2) {
                    voltages3[textbox_edit.text.toString().toInt() - 1] = (textbox_edit.text.toString().toInt()).toString() + "." + textbox.text.toString()
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, voltages3)
                    List3.adapter = my_adapter
                } else if (count_tab == 3 && count_radio == 0) {
                    eq[textbox_edit.text.toString().toInt() - 1] = (textbox_edit.text.toString().toInt()).toString() + "." + textbox.text.toString()
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, eq)
                    List1.adapter = my_adapter
                } else if (count_tab == 3 && count_radio == 1) {
                    nodes[textbox_edit.text.toString().toInt() - 1] = (textbox_edit.text.toString().toInt()).toString() + "." + textbox.text.toString()
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, nodes)
                    List2.adapter = my_adapter
                } else if (count_tab == 3 && count_radio == 2) {
                    loops[textbox_edit.text.toString().toInt() - 1] = (textbox_edit.text.toString().toInt()).toString() + "." + textbox.text.toString()
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, loops)
                    List3.adapter = my_adapter
                }
                textbox.setText("")
                textbox_edit.setText("")
            } else if (textbox.text.toString() == "" && textbox_edit.text.toString() != "") {
                if (count_tab == 0 && count_radio == 0) {
                    resistances.removeAt(textbox_edit.text.toString().toInt() - 1)
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, resistances)
                    List1.adapter = my_adapter
                } else if (count_tab == 0 && count_radio == 1) {
                    method1.removeAt(textbox_edit.text.toString().toInt() - 1)
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, method1)
                    List2.adapter = my_adapter
                } else if (count_tab == 0 && count_radio == 2) {
                    current1.removeAt(textbox_edit.text.toString().toInt() - 1)
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, current1)
                    List3.adapter = my_adapter
                } else if (count_tab == 1 && count_radio == 0) {
                    voltages.removeAt(textbox_edit.text.toString().toInt() - 1)
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, voltages)
                    List1.adapter = my_adapter
                } else if (count_tab == 1 && count_radio == 1) {
                    method2.removeAt(textbox_edit.text.toString().toInt() - 1)
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, method2)
                    List2.adapter = my_adapter
                } else if (count_tab == 1 && count_radio == 2) {
                    current2.removeAt(textbox_edit.text.toString().toInt() - 1)
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, current2)
                    List3.adapter = my_adapter
                } else if (count_tab == 2 && count_radio == 0) {
                    current_sources.removeAt(textbox_edit.text.toString().toInt() - 1)
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, current_sources)
                    List1.adapter = my_adapter
                } else if (count_tab == 2 && count_radio == 1) {
                    method3.removeAt(textbox_edit.text.toString().toInt() - 1)
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, method3)
                    List2.adapter = my_adapter
                } else if (count_tab == 2 && count_radio == 2) {
                    voltages3.removeAt(textbox_edit.text.toString().toInt() - 1)
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, voltages3)
                    List3.adapter = my_adapter
                } else if (count_tab == 3 && count_radio == 0) {
                    eq.removeAt(textbox_edit.text.toString().toInt() - 1)
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, eq)
                    List1.adapter = my_adapter
                } else if (count_tab == 3 && count_radio == 1) {
                    nodes.removeAt(textbox_edit.text.toString().toInt() - 1)
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, nodes)
                    List2.adapter = my_adapter
                } else if (count_tab == 3 && count_radio == 2) {
                    loops.removeAt(textbox_edit.text.toString().toInt() - 1)
                    val my_adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, loops)
                    List3.adapter = my_adapter
                }
                textbox_edit.setText("")
            }
        }catch (ex:Exception){}
    }


    fun bt_new(view:View){
        try {
            val intent = Intent(this, MainActivity::class.java)
            startActivity(intent)
            resistances = arrayListOf()
            method1 = arrayListOf()
            current1 = arrayListOf()
            voltages = arrayListOf()
            method2 = arrayListOf()
            current2 = arrayListOf()
            current_sources = arrayListOf()
            method3 = arrayListOf()
            voltages3 = arrayListOf()
            eq = arrayListOf()
            nodes = arrayListOf()
            loops = arrayListOf()
            if (count_tab != 0) {
                count_tab = 0
                count_radio = 0
                radio_value.setText("Value")
                radio_method.setText("Method")
                radio_current.setText("Current")
                radio_value.isChecked = true
                previous.isEnabled = false
                textview_title.setText("Resistances")
                next.setText("Next")

            }
            val my_adapter1 = ArrayAdapter(this, android.R.layout.simple_list_item_1, loops)
            List1.adapter = my_adapter1
            val my_adapter2 = ArrayAdapter(this, android.R.layout.simple_list_item_1, loops)
            List2.adapter = my_adapter2
            val my_adapter3 = ArrayAdapter(this, android.R.layout.simple_list_item_1, loops)
            List3.adapter = my_adapter3
        }catch(ex:Exception){}
    }


}