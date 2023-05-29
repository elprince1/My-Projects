import math
import cmath
class App():
    
    #Omega float
    def __init__(self):
        self.SuperProcess=False
    def CheckVars(self,list,mode=None):
        for index in range(0,len(list)):
            if self.CheckNumeric(list[index]) and not "j" in list[index]:   ## independent
                if mode=="S":
                    if not "<" in list[index] and not ":" in list[index]:
                        list[index]+="<0:0"
                elif mode=="C":
                    if not "<" in list[index] and not ":" in list[index]:
                        list[index]+="<0"
            elif not self.CheckNumeric(list[index]): ## dependent
                num=""
                var=""
                s=0
                n=0
                first=""
                for char in list[index]:
                    if s==0:
                        if self.CheckNumeric(char):
                                num+=char
                        else:
                            if n==0:
                                first="yes"
                            var+=char
                            s=1
                    else:
                        var+=char
                    n+=1
                if first !="yes":
                    list[index]=num+"*"+var
        return list
    def PrepairingVars(self,ResValue, ResMethod, ResCurrent, CapValue, CapMethod,
                    CapCurrent, IndValue, IndMethod, IndCurrent, VSValue,
                    VSMethod, VSCurrent, CSValue, CSMethod, CSVoltage, Loops,
                    MoreEqns,output):
        self.SuperProcess=False
        ResValue=self.CheckVars(ResValue)
        ResCurrent=self.CheckVars(ResCurrent,"C")
        CapValue=self.CheckVars(CapValue)
        CapCurrent=self.CheckVars(CapCurrent,"C")
        IndValue=self.CheckVars(IndValue)
        IndCurrent=self.CheckVars(IndCurrent,"C")
        VSValue=self.CheckVars(VSValue,"S")
        VSCurrent=self.CheckVars(VSCurrent,"C")
        CSValue=self.CheckVars(CSValue,"S")
        CSVoltage=self.CheckVars(CSVoltage,"C")
        
        
        soln=self.regulator(ResValue, ResMethod, ResCurrent, CapValue, CapMethod,
                            CapCurrent, IndValue, IndMethod, IndCurrent, VSValue,
                            VSMethod, VSCurrent, CSValue, CSMethod, CSVoltage, Loops,
                            MoreEqns)
        soln=self.ModifyingLastResult(soln)
        list_solution=[]
        for i in soln:
            for j in i:
                for k in j:
                    list_solution.append(k)
        if output=="ShowAllSolns":
            return list_solution
        else:
            if self.SuperProcess==False:
                list_solution=self.GetVarsElements(list_solution, ResValue, ResMethod, ResCurrent, CapValue,
                                          CapMethod, CapCurrent, IndValue, IndMethod, IndCurrent,
                                          VSValue, VSMethod, VSCurrent, CSValue, CSMethod, CSVoltage)
            return list_solution
    def GetNodes(self,ResMethod,CapMethod,IndMethod,VSMethod,CSMethod):
        chars=""
        for method in ResMethod:
            chars+=method
        for method in CapMethod:
            chars+=method
        for method in IndMethod:
            chars+=method
        for method in VSMethod:
            chars+=method
        for method in CSMethod:
            chars+=method
        NewChars=""
        for char in chars:
            if not char in NewChars:
                NewChars+=char
        chars=NewChars
        # chars has now all points used in the circuit
        nodes=[]
        for char in chars:
            count=0
            for method in ResMethod:
                if char in method:
                    count+=1
            for method in CapMethod:
                if char in method:
                    count+=1
            for method in IndMethod:
                if char in method:
                    count+=1
            for method in VSMethod:
                if char in method:
                    count+=1
            for method in CSMethod:
                if char in method:
                    count+=1
            if count>2:
                nodes.append(char)
        return nodes
    def ConvertToPolar(self,cartisien):
        cartisien=str(cartisien)
        cartisien=cartisien.replace("(","")
        cartisien=cartisien.replace(")","")
        real=""
        imagine=""
        cmp=complex(cartisien)
        cmp_real=str(cmp.real)
        cmp_imag=str(cmp.imag)
        if "e" in str(cmp_real) and "e" in str(cmp_imag):
            cartisien="0j"
        elif "e" in str(cmp_real) and not "e" in str(cmp_imag):
            cartisien=str(float(cmp_imag))+"j"
        elif not "e" in str(cmp_real) and "e" in str(cmp_imag):
            cartisien=str(float(cmp_real))
        cmp=complex(cartisien)
        cmp_real=str(cmp.real)
        cmp_imag=str(cmp.imag)
        if (cmp_real=="0.0" or cmp_real=="-0.0") and not (cmp_imag =="0.0" or cmp_imag=="-0.0"):
            cartisien=str(float(cmp_imag))+"j"
        elif not (cmp_real=="0.0" or cmp_real=="-0.0") and (cmp_imag =="0.0" or cmp_imag=="-0.0"):
            cartisien=str(float(cmp_real))
        elif (cmp_real=="0.0" or cmp_real=="-0.0") and (cmp_imag =="0.0" or cmp_imag=="-0.0"):
            cartisien="0j"
        cartisien=cartisien.replace("(","")
        cartisien=cartisien.replace(")","")
        polar=cmath.polar(complex(cartisien))
        return str(polar[0])+"<"+str(polar[1]*180/math.pi)
        # if "+" in cartisien:
        #     list=cartisien.split("+")
        #     real=list[0]
        #     imagine=list[1].replace("j","")
        #     if cartisien[0]=="-":
        #         degrees=str(math.degrees(math.atan(float(imagine)/float(real)))+180)
        #     else:
        #         degrees=str(math.degrees(math.atan(float(imagine)/float(real))))
        # else:
        #     if "-" in cartisien and cartisien[0]!="-":
        #         list=cartisien.split("-")
        #         real=list[0]
        #         imagine="-"+list[1].replace("j","")
        #         degrees=str(math.degrees(math.atan(float(imagine)/float(real))))
        #     elif  "-" in cartisien and cartisien[0]=="-":
        #         if cartisien.count("-")==2:
        #             cartisien=cartisien[1:]
        #             list=cartisien.split("-")
        #             real="-"+list[0]
        #             imagine="-"+list[1].replace("j","")
        #             degrees=str(math.degrees(math.atan(float(imagine)/float(real)))-180)
        #         else:
        #             degrees="-90"
        #             real="0.0"
        #             imagine=cartisien.replace("j","")
        #     elif not "-" in cartisien:
        #         degrees="90"
        #         real="0.0"
        #         imagine=cartisien.replace("j","")
       
    def ConvertToCartisien(self,polar):
        list=polar.split("<")
        real=str(float(list[0])*math.cos(float(list[1])*math.pi/180))
        imagine=str(float(list[0])*math.sin(float(list[1])*math.pi/180))
        if imagine[0]=="-":
            return real + imagine+"j"
        else:
            return real +"+"+ imagine+"j"
    def CheckNumeric(self,text):
        text=text.replace(".","")
        text=text.replace("<","")
        text=text.replace("j","")
        text=text.replace(":","")
        if text=="":
            text="0"
        if not text[0]=="-" and "-" in text:
            text=text.replace("-","")
        if text[0]=="-":
            text=text[1:]
        return text.isnumeric()
    def GetEqns(self,ResValue1,ResMethod1,ResCurrent1,CapValue1,CapMethod1,
                CapCurrent1,IndValue1,IndMethod1,IndCurrent1,
                VSValue1,VSMethod1,VSCurrent1,CSValue1,
                CSMethod1,CSVoltage1,Loops,MoreEqns,Omega):
        RESULT_EQNS=[]
        for loop in Loops:
            ResCurrent=ResCurrent1.copy()
            ResValue=ResValue1.copy()
            ResMethod=ResMethod1.copy()
            CapMethod=CapMethod1.copy()
            CapValue=CapValue1.copy()
            CapCurrent=CapCurrent1.copy()
            IndMethod=IndMethod1.copy()
            IndValue=IndValue1.copy()
            IndCurrent=IndCurrent1.copy()
            CSValue=CSValue1.copy()
            CSVoltage=CSVoltage1.copy()
            CSMethod=CSMethod1.copy()
            VSMethod=VSMethod1.copy()
            VSValue=VSValue1.copy()
            VSCurrent=VSCurrent1.copy()
            EQN=""
            for index in range(0,len(loop)):
                if index==len(loop)-1:
                    break
                method=loop[index]+loop[index+1]
                if method in ResMethod:
                    index_method=ResMethod.index(method)
                    if self.CheckNumeric(ResValue[index_method]) and self.CheckNumeric(ResCurrent[index_method]):
                        current=self.ConvertToCartisien(ResCurrent[index_method])
                        Res=str(float(ResValue[index_method])*complex(current))
                        Res=Res.replace("(","")
                        Res=Res.replace(")","")
                        Res=self.ConvertToPolar(Res)
                        EQN+="+"+Res
                    elif self.CheckNumeric(ResValue[index_method]) and not self.CheckNumeric(ResCurrent[index_method]):
                        EQN+="+"+str(ResValue[index_method])+"*"+str(ResCurrent[index_method])
                    elif not self.CheckNumeric(ResValue[index_method]) and self.CheckNumeric(ResCurrent[index_method]):
                        EQN+="+"+str(ResCurrent[index_method])+"*"+str(ResValue[index_method])
                    ResMethod.pop(index_method)
                    ResValue.pop(index_method)
                    ResCurrent.pop(index_method)
                elif method[::-1] in ResMethod:
                    index_method=ResMethod.index(method[::-1])
                    if self.CheckNumeric(ResValue[index_method]) and self.CheckNumeric(ResCurrent[index_method]):
                        current=self.ConvertToCartisien(ResCurrent[index_method])
                        Res=str(float(ResValue[index_method])*complex(current))
                        Res=Res.replace("(","")
                        Res=Res.replace(")","")
                        Res=self.ConvertToPolar(Res)
                        EQN+="+-"+Res
                    elif self.CheckNumeric(ResValue[index_method]) and not self.CheckNumeric(ResCurrent[index_method]):
                        EQN+="+-"+str(ResValue[index_method])+"*"+str(ResCurrent[index_method])
                    elif not self.CheckNumeric(ResValue[index_method]) and self.CheckNumeric(ResCurrent[index_method]):
                        EQN+="+-"+str(ResCurrent[index_method])+"*"+str(ResValue[index_method])
                    ResMethod.pop(index_method)
                    ResValue.pop(index_method)
                    ResCurrent.pop(index_method)
                elif method in CapMethod:
                    index_method=CapMethod.index(method)
                    if self.CheckNumeric(CapValue[index_method]) and self.CheckNumeric(CapCurrent[index_method]):
                        current=self.ConvertToCartisien(CapCurrent[index_method])
                        if "j" in CapValue[index_method]:
                            CapValue[index_method]=CapValue[index_method].replace("-","")
                            Res=str(complex(CapValue[index_method])*complex(current))
                            Res=Res.replace("(","")
                            Res=Res.replace(")","")
                            Res=self.ConvertToPolar(Res)
                            EQN+="+-"+Res
                        else:
                            impedance=1/(Omega*float(CapValue[index_method]))
                            Res=str(impedance*complex(current))
                            Res=Res.replace("(","")
                            Res=Res.replace(")","")
                            Res=self.ConvertToPolar(Res)
                            EQN+="+-"+str(Res)
                    elif self.CheckNumeric(CapValue[index_method]) and not self.CheckNumeric(CapCurrent[index_method]):
                        if "j" in CapValue[index_method]:
                            CapValue[index_method]=CapValue[index_method].replace("j","")
                            CapValue[index_method]=CapValue[index_method].replace("-","")
                            EQN+="+-"+str(CapValue[index_method])+"j*"+str(CapCurrent[index_method])
                        else:
                            impedance=1/(Omega*float(CapValue[index_method]))
                            EQN+="+-"+str(impedance)+"j*"+str(CapCurrent[index_method])
                    elif not self.CheckNumeric(CapValue[index_method]) and self.CheckNumeric(CapCurrent[index_method]):
                        EQN+="+"+str(CapCurrent[index_method])+"*"+str(CapValue[index_method])+"c"
                    CapMethod.pop(index_method)
                    CapValue.pop(index_method)
                    CapCurrent.pop(index_method)
                elif method[::-1] in CapMethod:
                    index_method=CapMethod.index(method[::-1])
                    if self.CheckNumeric(CapValue[index_method]) and self.CheckNumeric(CapCurrent[index_method]):
                        current=self.ConvertToCartisien(CapCurrent[index_method])
                        if "j" in CapValue[index_method]:
                            CapValue[index_method]=CapValue[index_method].replace("-","")
                            Res=str(complex(CapValue[index_method])*complex(current))
                            Res=Res.replace("(","")
                            Res=Res.replace(")","")
                            Res=self.ConvertToPolar(Res)
                            EQN+="+"+Res
                        else:
                            impedance=1/(Omega*float(CapValue[index_method]))
                            Res=str(impedance*complex(current))
                            Res=Res.replace("(","")
                            Res=Res.replace(")","")
                            Res=self.ConvertToPolar(Res)
                            EQN+="+"+Res
                    elif self.CheckNumeric(CapValue[index_method]) and not self.CheckNumeric(CapCurrent[index_method]):
                        if "j" in CapValue[index_method]:
                            CapValue[index_method]=CapValue[index_method].replace("j","")
                            CapValue[index_method]=CapValue[index_method].replace("-","")
                            EQN+="+"+str(CapValue[index_method])+"j*"+str(CapCurrent[index_method])
                        else:
                            impedance=1/(Omega*float(CapValue[index_method]))
                            EQN+="+"+str(impedance)+"j*"+str(CapCurrent[index_method])
                    elif not self.CheckNumeric(CapValue[index_method]) and self.CheckNumeric(CapCurrent[index_method]):
                        EQN+="+-"+str(CapCurrent[index_method])+"*"+str(CapValue[index_method])+"c"
                    CapMethod.pop(index_method)
                    CapValue.pop(index_method)
                    CapCurrent.pop(index_method)
                elif method in IndMethod:
                    index_method=IndMethod.index(method)
                    if self.CheckNumeric(IndValue[index_method]) and self.CheckNumeric(IndCurrent[index_method]):
                        current=self.ConvertToCartisien(IndCurrent[index_method])
                        if "j" in IndValue[index_method]:
                            Res=str(complex(IndValue[index_method])*complex(current))
                            Res=Res.replace("(","")
                            Res=Res.replace(")","")
                            Res=self.ConvertToPolar(Res)
                            EQN+="+"+Res
                        else:
                            impedance=Omega*float(IndValue[index_method])
                            Res=str(impedance*complex(current))
                            Res=Res.replace("(","")
                            Res=Res.replace(")","")
                            Res=self.ConvertToPolar(Res)
                            EQN+="+"+Res
                    elif self.CheckNumeric(IndValue[index_method]) and not self.CheckNumeric(IndCurrent[index_method]):
                        if "j" in IndValue[index_method]:
                            IndValue[index_method]=IndValue[index_method].replace("j","")
                            EQN+="+"+str(IndValue[index_method])+"j*"+str(IndCurrent[index_method])
                        else:
                            impedance=Omega*float(IndValue[index_method])
                            EQN+="+"+str(impedance)+"j*"+str(IndCurrent[index_method])
                    elif not self.CheckNumeric(IndValue[index_method]) and self.CheckNumeric(IndCurrent[index_method]):
                        EQN+="+"+str(IndCurrent[index_method])+"*"+str(IndValue[index_method])+"l"
                    IndMethod.pop(index_method)
                    IndValue.pop(index_method)
                    IndCurrent.pop(index_method)
                elif method[::-1] in IndMethod:
                    
                    index_method=IndMethod.index(method[::-1])
                    if self.CheckNumeric(IndValue[index_method]) and self.CheckNumeric(IndCurrent[index_method]):
                        current=self.ConvertToCartisien(IndCurrent[index_method])
                        if "j" in IndValue[index_method]:
                            Res=str(complex(IndValue[index_method])*complex(current))
                            Res=Res.replace(")","")
                            Res=Res.replace("(","")
                            Res=self.ConvertToPolar(Res)
                            EQN+="+-"+Res
                        else:
                            impedance=Omega*float(IndValue[index_method])
                            Res=str(impedance*complex(current))
                            Res=Res.replace(")","")
                            Res=Res.replace("(","")
                            Res=self.ConvertToPolar(Res)
                            EQN+="+-"+Res
                    elif self.CheckNumeric(IndValue[index_method]) and not self.CheckNumeric(IndCurrent[index_method]):
                        if "j" in IndValue[index_method]:
                            IndValue[index_method]=IndValue[index_method].replace("j","")
                            EQN+="+-"+str(IndValue[index_method])+"j*"+str(IndCurrent[index_method])
                        else:
                            impedance=Omega*float(IndValue[index_method])
                            EQN+="+-"+str(impedance)+"j*"+str(IndCurrent[index_method])
                    elif not self.CheckNumeric(IndValue[index_method]) and self.CheckNumeric(IndCurrent[index_method]):
                        EQN+="+-"+str(IndCurrent[index_method])+"*"+str(IndValue[index_method])+"l"
                    IndMethod.pop(index_method)
                    IndValue.pop(index_method)
                    IndCurrent.pop(index_method)
                elif method in VSMethod:
                    index_method=VSMethod.index(method)
                    EQN+="+-"+str(VSValue[index_method])
                    VSMethod.pop(index_method)
                    VSValue.pop(index_method)
                    VSCurrent.pop(index_method)
                elif method[::-1] in VSMethod:
                    index_method=VSMethod.index(method[::-1])
                    EQN+="+"+str(VSValue[index_method])
                    VSMethod.pop(index_method)
                    VSValue.pop(index_method)
                    VSCurrent.pop(index_method)
                elif method in CSMethod:
                    index_method=CSMethod.index(method)
                    EQN+="+"+str(CSVoltage[index_method])
                    CSMethod.pop(index_method)
                    CSValue.pop(index_method)
                    CSVoltage.pop(index_method)
                elif method[::-1] in CSMethod:
                    index_method=CSMethod.index(method[::-1])
                    EQN+="+-"+str(CSVoltage[index_method])
                    CSMethod.pop(index_method)
                    CSValue.pop(index_method)
                    CSVoltage.pop(index_method)
            EQN=EQN[1:]
            RESULT_EQNS.append(EQN)
            
        ResCurrent=ResCurrent1.copy()
        ResValue=ResValue1.copy()
        ResMethod=ResMethod1.copy()
        CapMethod=CapMethod1.copy()
        CapValue=CapValue1.copy()
        CapCurrent=CapCurrent1.copy()
        IndMethod=IndMethod1.copy()
        IndValue=IndValue1.copy()
        IndCurrent=IndCurrent1.copy()
        CSValue=CSValue1.copy()
        CSVoltage=CSVoltage1.copy()
        CSMethod=CSMethod1.copy()
        VSMethod=VSMethod1.copy()
        VSValue=VSValue1.copy()
        VSCurrent=VSCurrent1.copy()
        for info in MoreEqns:
            list_info=info.split(":")
            if list_info[1] in ResMethod:
                index_method=ResMethod.index(list_info[1])
                voltage=""
                if self.CheckNumeric(ResValue[index_method]) and self.CheckNumeric(ResCurrent[index_method]):
                    current=self.ConvertToCartisien(ResCurrent[index_method])
                    Res=str(float(ResValue[index_method])*complex(current))
                    Res=Res.replace("(","")
                    Res=Res.replace(")","")
                    Res=self.ConvertToPolar(Res)
                    voltage=Res
                elif self.CheckNumeric(ResValue[index_method]) and not self.CheckNumeric(ResCurrent[index_method]):
                    voltage=str(ResValue[index_method])+"*"+str(ResCurrent[index_method])
                elif not self.CheckNumeric(ResValue[index_method]) and self.CheckNumeric(ResCurrent[index_method]):
                    voltage=str(ResCurrent[index_method])+"*"+str(ResValue[index_method])
                RESULT_EQNS.append(list_info[0]+"+-"+voltage)
            elif list_info[1][::-1] in ResMethod:
                index_method=ResMethod.index(list_info[1][::-1])
                voltage=""
                if self.CheckNumeric(ResValue[index_method]) and self.CheckNumeric(ResCurrent[index_method]):
                    current=self.ConvertToCartisien(ResCurrent[index_method])
                    Res=str(float(ResValue[index_method])*complex(current))
                    Res=Res.replace("(","")
                    Res=Res.replace(")","")
                    Res=self.ConvertToPolar(Res)
                    voltage=Res
                elif self.CheckNumeric(ResValue[index_method]) and not self.CheckNumeric(ResCurrent[index_method]):
                    voltage=str(ResValue[index_method])+"*"+str(ResCurrent[index_method])
                elif not self.CheckNumeric(ResValue[index_method]) and self.CheckNumeric(ResCurrent[index_method]):
                    voltage=str(ResCurrent[index_method])+"*"+str(ResValue[index_method])
                RESULT_EQNS.append(list_info[0]+"+"+voltage)
            elif list_info[1] in CapMethod:
                index_method=CapMethod.index(list_info[1])
                voltage=""
                if self.CheckNumeric(CapValue[index_method]) and self.CheckNumeric(CapCurrent[index_method]):
                    current=self.ConvertToCartisien(CapCurrent[index_method])
                    if "j" in CapValue[index_method]:
                        CapValue[index_method]=CapValue[index_method].replace("-","")
                        Res=str(complex(CapValue[index_method])*complex(current))
                        Res=Res.replace("(","")
                        Res=Res.replace(")","")
                        Res=self.ConvertToPolar(Res)
                        voltage=Res
                    else:
                        impedance=1/(Omega*float(CapValue[index_method]))
                        Res=str(impedance*complex(current))
                        Res=Res.replace("(","")
                        Res=Res.replace(")","")
                        Res=self.ConvertToPolar(Res)
                        voltage=str(Res)
                elif self.CheckNumeric(CapValue[index_method]) and not self.CheckNumeric(CapCurrent[index_method]):
                    if "j" in CapValue[index_method]:
                        CapValue[index_method]=CapValue[index_method].replace("j","")
                        CapValue[index_method]=CapValue[index_method].replace("-","")
                        voltage=str(CapValue[index_method])+"j*"+str(CapCurrent[index_method])
                    else:
                        impedance=1/(Omega*float(CapValue[index_method]))
                        voltage=str(impedance)+"j*"+str(CapCurrent[index_method])
                elif not self.CheckNumeric(CapValue[index_method]) and self.CheckNumeric(CapCurrent[index_method]):
                    voltage="-"+str(CapCurrent[index_method])+"*"+str(CapValue[index_method])+"c"
                RESULT_EQNS.append(list_info[0]+"+"+voltage)
            elif list_info[1][::-1] in CapMethod:
                index_method=CapMethod.index(list_info[1][::-1])
                voltage=""
                if self.CheckNumeric(CapValue[index_method]) and self.CheckNumeric(CapCurrent[index_method]):
                    current=self.ConvertToCartisien(CapCurrent[index_method])
                    if "j" in CapValue[index_method]:
                        CapValue[index_method]=CapValue[index_method].replace("-","")
                        Res=str(complex(CapValue[index_method])*complex(current))
                        Res=Res.replace("(","")
                        Res=Res.replace(")","")
                        Res=self.ConvertToPolar(Res)
                        voltage=Res
                    else:
                        impedance=1/(Omega*float(CapValue[index_method]))
                        Res=str(impedance*complex(current))
                        Res=Res.replace("(","")
                        Res=Res.replace(")","")
                        Res=self.ConvertToPolar(Res)
                        voltage=str(Res)
                    RESULT_EQNS.append(list_info[0]+"+-"+voltage)
                elif self.CheckNumeric(CapValue[index_method]) and not self.CheckNumeric(CapCurrent[index_method]):
                    if "j" in CapValue[index_method]:
                        CapValue[index_method]=CapValue[index_method].replace("j","")
                        CapValue[index_method]=CapValue[index_method].replace("-","")
                        voltage=str(CapValue[index_method])+"j*"+str(CapCurrent[index_method])
                        RESULT_EQNS.append(list_info[0]+"+-"+voltage)
                    else:
                        impedance=1/(Omega*float(CapValue[index_method]))
                        voltage=str(impedance)+"j*"+str(CapCurrent[index_method])
                        RESULT_EQNS.append(list_info[0]+"+-"+voltage)
                elif not self.CheckNumeric(CapValue[index_method]) and self.CheckNumeric(CapCurrent[index_method]):
                    voltage=str(CapCurrent[index_method])+"*"+str(CapValue[index_method])+"c"
                    RESULT_EQNS.append(list_info[0]+"+"+voltage)
            elif list_info[1] in IndMethod:
                index_method=IndMethod.index(list_info[1])
                voltage=""
                if self.CheckNumeric(IndValue[index_method]) and self.CheckNumeric(IndCurrent[index_method]):
                    current=self.ConvertToCartisien(IndCurrent[index_method])
                    if "j" in IndValue[index_method]:
                        Res=str(complex(IndValue[index_method])*complex(current))
                        Res=Res.replace("(","")
                        Res=Res.replace(")","")
                        Res=self.ConvertToPolar(IndCurrent[index_method])
                        voltage=Res
                    else:
                        impedance=Omega*float(IndValue[index_method])
                        Res=str(impedance*complex(current))
                        Res=Res.replace("(","")
                        Res=Res.replace(")","")
                        Res=self.ConvertToPolar(IndCurrent[index_method])
                        voltage=Res
                elif self.CheckNumeric(IndValue[index_method]) and not self.CheckNumeric(IndCurrent[index_method]):
                    if "j" in IndValue[index_method]:
                        IndValue[index_method]=IndValue[index_method].replace("j","")
                        voltage=str(IndValue[index_method])+"j*"+str(IndCurrent[index_method])
                    else:
                        impedance=Omega*float(IndValue[index_method])
                        voltage=str(impedance)+"j*"+str(IndCurrent[index_method])
                elif not self.CheckNumeric(IndValue[index_method]) and self.CheckNumeric(IndCurrent[index_method]):
                    voltage=str(IndCurrent[index_method])+"*"+str(IndValue[index_method])+"l"
                RESULT_EQNS.append(list_info[0]+"+-"+voltage)
            elif list_info[1][::-1] in IndMethod:
                index_method=IndMethod.index(list_info[1][::-1])
                voltage=""
                if self.CheckNumeric(IndValue[index_method]) and self.CheckNumeric(IndCurrent[index_method]):
                    current=self.ConvertToCartisien(IndCurrent[index_method])
                    if "j" in IndValue[index_method]:
                        Res=str(complex(IndValue[index_method])*complex(current))
                        Res=Res.replace("(","")
                        Res=Res.replace(")","")
                        Res=self.ConvertToPolar(IndCurrent[index_method])
                        voltage=Res
                    else:
                        impedance=Omega*float(IndValue[index_method])
                        Res=str(impedance*complex(current))
                        Res=Res.replace("(","")
                        Res=Res.replace(")","")
                        Res=self.ConvertToPolar(IndCurrent[index_method])
                        voltage=Res
                elif self.CheckNumeric(IndValue[index_method]) and not self.CheckNumeric(IndCurrent[index_method]):
                    if "j" in IndValue[index_method]:
                        IndValue[index_method]=IndValue[index_method].replace("j","")
                        voltage=str(IndValue[index_method])+"j*"+str(IndCurrent[index_method])
                    else:
                        impedance=Omega*float(IndValue[index_method])
                        voltage=str(impedance)+"j*"+str(IndCurrent[index_method])
                elif not self.CheckNumeric(IndValue[index_method]) and self.CheckNumeric(IndCurrent[index_method]):
                    voltage=str(IndCurrent[index_method])+"*"+str(IndValue[index_method])+"l"
                RESULT_EQNS.append(list_info[0]+"+"+voltage)
        Nodes=self.GetNodes(ResMethod, CapMethod, IndMethod, VSMethod, CSMethod)
        for node in Nodes:
            EQN=""
            for method in ResMethod:
                if method[0]==node:
                    EQN+="+"+str(ResCurrent[ResMethod.index(method)])
                elif method[-1]==node:
                    EQN+="+-"+str(ResCurrent[ResMethod.index(method)])
            for method in CapMethod:
                if method[0]==node:
                    EQN+="+"+str(CapCurrent[CapMethod.index(method)])
                elif method[-1]==node:
                    EQN+="+-"+str(CapCurrent[CapMethod.index(method)])
            for method in IndMethod:
                if method[0]==node:
                    EQN+="+"+str(IndCurrent[IndMethod.index(method)])
                elif method[-1]==node:
                    EQN+="+-"+str(IndCurrent[IndMethod.index(method)])
            if VSMethod!=[]:
                index_method=0
                for method in VSMethod:
                    if method[0]==node:
                        EQN+="+"+str(VSCurrent[index_method])
                    elif method[-1]==node:
                        EQN+="+-"+str(VSCurrent[index_method])
                    index_method+=1
            if CSMethod!=[]:
                index_method=0
                for method in CSMethod:
                    if method[0]==node:
                        EQN+="+"+str(CSValue[index_method])
                    elif method[-1]==node:
                        EQN+="+-"+str(CSValue[index_method])
                    index_method+=1
            EQN=EQN[1:]
            RESULT_EQNS.append(EQN)
        #print(RESULT_EQNS)
        
        return RESULT_EQNS
    def CollectOperators(self,RESULT_EQNS):
        EqnsAfter=[]
        for eqn in RESULT_EQNS:
            terms=eqn.split("+")
            for index in range(0,len(terms)):
                if "*" in terms[index]:
                    terms[index]=terms[index].split("*")
                else:
                    if terms[index][0]=="-":
                        terms[index]=["-1",terms[index][1:]]
                    else:
                        terms[index]=["1",terms[index]]
            # terms[[op,var1],[op,var2],[op,var3],var4]
            #print(terms)
            ############################# adding j together in the same var and not j together in the same var
            count_out=0
            for term1 in terms:
                count_in=0
                for term2 in terms:
                    if count_in!=count_out:
                        if term1[1]==term2[1]!="":
                            if "j" in term1[0] and "j" in term2[0]:
                                # term1[0]=term1[0].replace("j","")
                                # term2[0]=term2[0].replace("j","")
                                # if term1[0][0]=="-":
                                #     term1[0]=float(term1[0][1:])*-1
                                # if term2[0][0]=="-":
                                #     term2[0]=float(term2[0][1:])*-1
                                # term2[0]=str(float(term1[0])+float(term2[0]))+"j"
                                term2[0]=str(complex(term1[0])+complex(term2[0]))
                                term1[0]=""
                                term1[1]=""
                            elif not "j" in term1[0] and not "j" in term2[0]:
                                # if term1[0][0]=="-":
                                #     term1[0]=float(term1[0][1:])*-1
                                # if term2[0][0]=="-":
                                #     term2[0]=float(term2[0][1:])*-1
                                # term2[0]=str(float(term1[0])+float(term2[0]))
                                term2[0]=str(complex(term1[0])+complex(term2[0]))
                                term1[0]=""
                                term1[1]=""
                                #print(terms)
                            elif not "j" in term1[0] and "j" in term2[0]:
                                # if "-" in term2[0]:
                                #     term2[0]=term2[0].replace("-","")
                                #     term2[0]=term1[0]+"-"+term2[0]
                                # else:
                                #     term2[0]=term1[0]+"+"+term2[0]
                                term2[0]=str(complex(term1[0])+complex(term2[0]))
                                term1[0]=""
                                term1[1]=""
                            elif "j" in term1[0] and not "j" in term2[0]:
                                # if "-" in term1[0]:
                                #     term1[0]=term1[0].replace("-","")
                                #     term2[0]=term2[0]+"-"+term1[0]
                                # else:
                                #     term2[0]=term2[0]+"+"+term1[0]
                                term2[0]=str(complex(term1[0])+complex(term2[0]))
                                term1[0]=""
                                term1[1]=""
                    count_in+=1
                count_out+=1
            while True:
                s=0
                for term in terms:
                    if term[0]==term[1]:
                        terms.remove(term)
                        s=1
                if s==0:
                    break
            EqnsAfter.append(terms)
        #print(EqnsAfter)
        return EqnsAfter
    def removing_repeated_eqns(self,EqnsAfter):
        count_out=0
        for eqn1 in EqnsAfter:
            count_in=0
            for eqn2 in EqnsAfter:
                if count_out!=count_in:
                    ln=0
                    for term1 in eqn1:
                        for term2 in eqn2:
                            if "<" in term2[0]:
                                term2[0]=self.ConvertToCartisien(term2[0])
                            if "<" in term1[0]:
                                term1[0]=self.ConvertToCartisien(term1[0])
                            if term1[1]==term2[1] and complex(term1[0])==-1*complex(term2[0]):
                                ln+=1
                    if ln==len(eqn1)==len(eqn2):
                        for term in eqn2:
                            term[0]=""
                            term[1]=""
                count_in+=1
            count_out+=1
        #print(EqnsAfter)
        while True:
            k=0
            for eqn in EqnsAfter:
                s=0
                for term in eqn:
                    if term[0]!="" or term[1]!="":
                        s=1
                if s==0:
                    EqnsAfter.remove(eqn)
                    k=1
            if k==0:
                break
        return EqnsAfter
                            
    def GetVars(self,EqnsAfter):
        ## getting vars in Eqns:
        vars=[]
        for eqn in EqnsAfter:
            for term in eqn:
                if not self.CheckNumeric(term[1]) :
                    vars.append(term[1])
        vars=set(vars)
        vars=list(vars)
        return vars
    def SolvingEqns(self,EqnsAfter,vars):
        Matrix=[]
        for eqn in EqnsAfter:
            Row=[]
            for var in vars:
                Found=False
                for term in eqn:
                    if var == term[1]:
                        Found=True
                        if "<" in term[0]:
                            car=self.ConvertToCartisien(term[0])
                            Row.append(car)
                        else:
                            Row.append(term[0])
                        break
                if not Found:
                    Row.append("0")
            Found=False
            for term in eqn:
                if self.CheckNumeric(term[1]):
                    if "<" in term[1]:
                        list=term[1].split("<")
                        real=float(list[0])*math.cos(float(list[1])*(math.pi/180))
                        imagine=float(list[0])*math.sin(float(list[1])*(math.pi/180))
                        if term[0]=="-1":
                            if "-" in str(imagine):
                                imagine=str(imagine).replace("-","")
                                term[1]=str(real)+"-"+str(imagine)+"j"
                            else:
                                term[1]=str(real)+"+"+str(imagine)+"j"
                        else:
                            if str(imagine)[0]=="-" and str(real)[0]=="-":
                                imagine=str(imagine).replace("-","")
                                real=str(real).replace("-","")
                                term[1]=str(real)+"+"+str(imagine)+"j"
                            elif str(imagine)[0]!="-" and str(real)[0]=="-":
                                real=str(real).replace("-","")
                                term[1]=str(real)+"-"+str(imagine)+"j"
                            elif str(imagine)[0]=="-" and str(real)[0]!="-":
                                imagine=str(imagine).replace("-","")
                                term[1]="-"+str(real)+"+"+str(imagine)+"j"
                            elif str(imagine)[0]!="-" and str(real)[0]!="-":
                                term[1]="-"+str(real)+"-"+str(imagine)+"j"
                        if len(Row)==len(vars):
                            Row.append(term[1])
                            Found=True
                        elif len(Row)>len(vars):
                            Row[-1]=str(complex(Row[-1])+complex(term[1]))
            if not Found:
                Row.append("0")
            Matrix.append(Row)
        #print(Matrix)
        # for i in Matrix:
        #     print(i)
        n_matrix=len(Matrix)
        while n_matrix>len(vars):
            Matrix.pop()
            n_matrix-=1
        # print("\n")
        # for i in Matrix:
        #     print(i)
        ############################ solving
        ########## 0 in the matrix remained
        for index1 in range(0,len(Matrix)):
            element=Matrix[index1][index1]
            if complex(element)==0j or complex(element)==-0j:
                for index2 in range(index1+1,len(Matrix)):
                    if complex (Matrix[index2][index1]) !=0j and complex(Matrix[index2][index1])!=-0j:
                        temp=Matrix[index1]
                        Matrix[index1]=Matrix[index2]
                        Matrix[index2]=temp
        index1=0
        while index1 <len(Matrix):
            s=0
            for index2 in range(0,len(Matrix)):
                if complex(Matrix[index2][index1])!=0j and complex(Matrix[index2][index1])!=-0j:
                    s=1
            if s==0:
                for index2 in range(0,len(Matrix)):
                    Matrix[index2].pop(index1)
                vars.pop(index1)
                Matrix.pop()
            index1+=1
        ####################################
        # print("\n")
        # for i in Matrix:
        #     print(i)
        index=0
        for Row in Matrix:
            op=Row[index]
            if complex(op)==0j or complex(op)==-0j:
                for index2 in range(index+1,len(Matrix)):
                    if complex (Matrix[index2][index]) !=0j and complex(Matrix[index2][index])!=-0j:
                        temp=Matrix[index]
                        Matrix[index]=Matrix[index2]
                        Matrix[index2]=temp
                        break
            op=Matrix[index][index]
            for ele_index in range(0,len(Row)):
                Matrix[index][ele_index]=complex(Matrix[index][ele_index])/complex(op)
            for index2 in range(index+1,len(Matrix)):
                op=complex(Matrix[index2][index])*-1
                count=0
                for element in Matrix[index]:
                    Matrix[index2][count]=complex(Matrix[index2][count])+complex(op*element)
                    count+=1
            
            index+=1
            
        # print("\n\n")
        # for i in Matrix:
        #     print(i)
        for index in range(len(Matrix)-1,-1,-1):
            Row=Matrix[index]
            op=Row[index]
            for ele_index in range(0,len(Row)):
                Row[ele_index]=complex(Row[ele_index])/complex(op)
            for index2 in range(index-1,-1,-1):
                op=complex(Matrix[index2][index])*-1
                count=0
                for element in Row:
                    Matrix[index2][count]=complex(Matrix[index2][count])+complex(op*element)
                    count+=1
        # for i in Matrix:
        #     print(i)
        solution=[]
        index=0
        for var in vars:
            solution.append(var+"="+str(Matrix[index][-1]))
            index+=1
        return solution
    def SuperPosition(self,ResValue,ResMethod1,ResCurrent,CapValue,CapMethod1,
                CapCurrent,IndValue,IndMethod1,IndCurrent,
                VSValue,VSMethod1,VSCurrent,dep_indep_vs,CSValue,
                CSMethod1,CSVoltage,dep_indep_cs,Loops,MoreEqns):
        ################### deviding dependent and independent cs and vs
        self.SuperProcess=True
        depcs_value=[]
        depcs_method=[]
        depcs_voltage=[]
        indepcs_value=[]
        indepcs_method=[]
        indepcs_voltage=[]
        depvs_value=[]
        depvs_method=[]
        depvs_current=[]
        indepvs_value=[]
        indepvs_method=[]
        indepvs_current=[]
        index=0
        for vs in VSValue:
            if dep_indep_vs[index]=="d": #dependent
                depvs_current.append(VSCurrent[index])
                depvs_method.append(VSMethod1[index])
                depvs_value.append(vs)
            else:
                indepvs_current.append(VSCurrent[index])
                indepvs_method.append(VSMethod1[index])
                indepvs_value.append(vs)
            index+=1
        index=0
        for cs in CSValue:
            if dep_indep_cs[index]=="d": #dependend
                depcs_method.append(CSMethod1[index])
                depcs_value.append(cs)
                depcs_voltage.append(CSVoltage[index])
            else:
                indepcs_method.append(CSMethod1[index])
                indepcs_value.append(cs)
                indepcs_voltage.append(CSVoltage[index])
            index+=1
        # print(depcs_value)
        # print(depcs_method)
        # print(depcs_voltage)
        # print(indepcs_value)
        # print(indepcs_method)
        # print(indepcs_voltage)
        # print(depvs_value)
        # print(depvs_method)
        # print(depvs_current)
        # print(indepvs_value)
        # print(indepvs_method)
        # print(indepvs_current)
        ########################################################################
        ################# getting the sources in each solving
        CSources=[]
        CSmethods=[]
        CSvoltages=[]
        VSources=[]
        VSmethods=[]
        VScurrents=[]
        for independent in indepvs_value:
            VSources.append(depvs_value)
            VSmethods.append(depvs_method)
            VScurrents.append(depvs_current)
            CSources.append(depcs_value)
            CSmethods.append(depcs_method)
            CSvoltages.append(depcs_voltage)
        for independent in indepcs_value:
            CSources.append(depcs_value)
            CSmethods.append(depcs_method)
            CSvoltages.append(depcs_voltage)
            VSources.append(depvs_value)
            VSmethods.append(depvs_method)
            VScurrents.append(depvs_current)
        index=0
        for independent in indepvs_value:
            VSources[index]=VSources[index]+[independent]
            VSmethods[index]=VSmethods[index]+[indepvs_method[index]]
            VScurrents[index]=VScurrents[index]+[indepvs_current[index]]
            index+=1
        n=index
        for independent in indepcs_value:
            CSources[index]=CSources[index]+[independent]
            CSmethods[index]=CSmethods[index]+[indepcs_method[index-n]]
            CSvoltages[index]=CSvoltages[index]+[indepcs_voltage[index-n]]
            index+=1
        # print(CSources,"    current sources")   
        # print(VSources,"    voltage sources")
        sources=[CSources,CSmethods,CSvoltages,VSources,VSmethods,VScurrents]
        return sources
    def SolvingAllSuper(self,ResValue,ResMethod,ResCurrent,CapValue,CapMethod,
                CapCurrent,IndValue,IndMethod,IndCurrent,
                VSValue,VSMethod,VSCurrent,CSValue,
                CSMethod,CSVoltage,Loops,MoreEqns):
        list_res=[]
        list_nums=[]
        dep_indep_cs=[]
        dep_indep_vs=[]
        # getting dependent and independent
        for source in  VSValue:
            if self.CheckNumeric(source):
                dep_indep_vs.append("i")
            else:
                dep_indep_vs.append("d")
        for source in  CSValue:
            if self.CheckNumeric(source):
                dep_indep_cs.append("i")
            else:
                dep_indep_cs.append("d")
        ####################################
        sources=self.SuperPosition(ResValue, ResMethod, ResCurrent, CapValue, CapMethod,
                           CapCurrent, IndValue, IndMethod, IndCurrent, VSValue,
                           VSMethod, VSCurrent, dep_indep_vs, CSValue, CSMethod,
                           CSVoltage, dep_indep_cs, Loops, MoreEqns)
        
        #sources=[CSources,CSmethods,CSvoltages,VSources,VSmethods,VScurrents]
        CSources=sources[0]
        VSources=sources[3]
        solns=[]
        omega_list=[]
        
        for index in range(0,len(VSources)):
            list_in=[]
            VSValue1=VSValue.copy()
            CSValue1=CSValue.copy()
            omega=0.0
            for n in range(0,len(VSValue1)):
                if not VSValue1[n] in VSources[index]:
                    VSValue1[n]="0<0"
                if not VSValue1[n]=="0":
                    if":" in VSValue1[n]:
                        list=VSValue1[n].split(":")
                        VSValue1[n]=list[0]
                        if list[1]=="0":
                            omega=0.00000000001
                        else:
                            omega=float(list[1])
            for n in range(0,len(CSValue1)):
                if not CSValue1[n] in CSources[index]:
                    CSValue1[n]="0<0"
                if not CSValue1[n]=="0":
                    if ":" in CSValue1[n]:
                        list=CSValue1[n].split(":")
                        CSValue1[n]=list[0]
                        if list[1]=="0":
                            omega=0.00000000001
                        else:
                            omega=float(list[1])
            omega_list.append(omega)
            ## solving
            EQNS=self.GetEqns(ResValue, ResMethod, ResCurrent, CapValue,
                               CapMethod, CapCurrent, IndValue, IndMethod,
                               IndCurrent, VSValue1, VSMethod, VSCurrent, CSValue1,
                               CSMethod, CSVoltage, Loops, MoreEqns, omega)
            
            EqnsAfter=self.CollectOperators(EQNS)
            
            EqnsAfter=self.removing_repeated_eqns(EqnsAfter)
            
            
            vars=self.GetVars(EqnsAfter)
            
            soln=self.SolvingEqns(EqnsAfter,vars)
            
            res=self.GetVoltagePower(ResValue, ResMethod, ResCurrent, CapValue, CapMethod,
                                      CapCurrent, IndValue, IndMethod, IndCurrent, soln,
                                      omega, VSValue1, CSValue1, VSCurrent, CSVoltage, VSMethod,
                                      CSMethod)
            #print(index)
            #print(res)
            res.pop()
            res.pop()
            list_res.append(res)
            
                    
            
            if solns!=[]:
                count=0
                for var in soln:
                    list_soln=var.split("=")
                    list_soln_polar=self.ConvertToPolar(list_soln[1]).split("<")   #5<0
                    
                    #print("\n")
                    if omega==0.00000000001:
                        #solns[count]=str(solns[count]+"+"+str(float(list_soln_polar[0])*math.cos(float(list_soln_polar[1])*math.pi/180)))
                        
                        list_in.append(str(float(list_soln_polar[0])*math.cos(float(list_soln_polar[1])*math.pi/180)))
                    else:
                        solns[count]=str(solns[count]+"+"+list_soln_polar[0]+"cos("+str(omega_list[-1])+
                                     "t+"+list_soln_polar[1]+")")
                        
                    count+=1
            else:
                for value in soln:
                    list_value=value.split("=")
                    value_polar=self.ConvertToPolar(list_value[1])
                    list_value_polar=value_polar.split("<")
                    if omega==0.00000000001:
                        #solns.append(list_value[0]+"="+str(float(list_value_polar[0])*math.cos(float(list_value_polar[1])*math.pi/180)))
                        
                        list_in.append(str(float(list_value_polar[0])*math.cos(float(list_value_polar[1])*math.pi/180)))
                    else:
                        solns.append(list_value[0]+"="+list_value_polar[0]+"cos("+str(omega_list[-1])+"t+"+
                                     list_value_polar[1]+")")
            list_nums.append(list_in)
        index=0
        while index < len(list_nums):
            if list_nums[index]==[]:
                list_nums.pop(index)
                index-=1
            index+=1
        list_total=[]
        for list in list_nums:
            count=0
            for num in list:
                try:
                    list_total[count]+=float(num)
                except:
                    list_total.append(0)
                    list_total[count]+=float(num)
                count+=1
        if list_total !=[]:
            for index in range(0,len(solns)):
                solns[index]+="+"+str(list_total[index])
        
        list_res_collected=[[],[]]
        #print(list_res)
        ### list_res=[list_result_eachtime,list_result_eachtime]   
        ### list_result_eachtime=[list_result,list_result]
        for list_result_eachtime in list_res:
            count=0
            for list_result in list_result_eachtime:
                index=0
                for item in list_result:
                    n=1
                    list_parts1=item.split(":")
                    value1=list_parts1[-1]
                    if "VA" in value1:
                        value1=value1.replace("VA","")
                        n=2
                    if "V" in value1:
                        value1=value1.replace("V","")
                        n=1
                    value1=value1.strip()
                    s=0
                    try:
                
                        value_collected=list_res_collected[count][index]
                        s=1
                    except:
                        s=0
                    if s==1:
                        polar_form=self.ConvertToPolar(value1)
                        list_polar=polar_form.split("<")
                        cos_form=""
                        if float(list_polar[0])==0.0 or float(list_polar[0])==-0.0:
                            index+=1
                            continue
                        if omega_list[list_res.index(list_result_eachtime)]==0.00000000001:
                            
                            cos_form=str(float(list_polar[0])*math.cos(float(list_polar[1])*math.pi/180))+"+"
                        else:
                            cos_form=str(list_polar[0]+"cos("+str(omega_list[list_res.index(list_result_eachtime)])+
                                         "t+"+list_polar[1]+")+")
                        list_res_collected[count][index]+= cos_form
                        
                    else:
                        
                        list_res_collected[count].append("0")
                        list=item.split(":")
                        value1=list[-1].replace("VA","")
                        value1=value1.replace("V","")
                        value1=value1.strip()
                        
                        polar_form=self.ConvertToPolar(value1)
                        list_polar=polar_form.split("<")
                        
                        if float(list_polar[0])==0.0 or float(list_polar[0])==-0.0:
                            list_res_collected[count][index]=list[0]+":"+list[1]+":"+list[2]+": "
                            index+=1
                            continue
                        if omega_list[list_res.index(list_result_eachtime)]==0.00000000001:
                            cos_form=str(float(list_polar[0])*math.cos(float(list_polar[1])*math.pi/180))+"+"
                        else:
                            cos_form=str(list_polar[0]+"cos("+str(omega_list[list_res.index(list_result_eachtime)])+
                                         "t+"+list_polar[1]+")+")
                        list_res_collected[count][index]=list[0]+":"+list[1]+":"+list[2]+": "+cos_form
                    index+=1
                count+=1
        
        for list in list_res_collected:
            for index in range(0,len(list)):
                list[index]=list[index][:len(list[index])-1]
                split_list=list[index].split(":")
                if split_list[-1].strip()=="":
                    list[index]+=" 0.0 "
                if list_res_collected.index(list)==0:
                    list[index]+=" V"
                else:
                    list[index]+=" VA"
        
        # for i in list_res_collected:
        #     for j in i:
        #         print(j)
        
        list_res_collected=[solns]+list_res_collected
        return [list_res_collected]
    def SolvingAllNotSuper(self,ResValue,ResMethod,ResCurrent,CapValue,CapMethod,
                           CapCurrent,IndValue,IndMethod,IndCurrent,
                           VSValue,VSMethod,VSCurrent,CSValue,
                           CSMethod,CSVoltage,Loops,MoreEqns):
        omega=0.0
        for index in range(0,len(VSValue)):
            if ":" in VSValue[index]:
                list=VSValue[index].split(":")
                if list[1]=="0":
                    omega=0.00000000001
                else:
                    omega=float(list[1])
                VSValue[index]=list[0]
        for index in range(0,len(CSValue)):
            if ":" in CSValue[index]:
                list=CSValue[index].split(":")
                if list[1]=="0":
                    omega=0.00000000001
                else:
                    omega=float(list[1])
                CSValue[index]=list[0]
        EQNS=self.GetEqns(ResValue, ResMethod, ResCurrent, CapValue, CapMethod,
                          CapCurrent, IndValue, IndMethod, IndCurrent, VSValue,
                          VSMethod, VSCurrent, CSValue, CSMethod, CSVoltage, Loops,
                          MoreEqns,omega)
        EqnsAfter=self.CollectOperators(EQNS)
        
        EqnsAfter=self.removing_repeated_eqns(EqnsAfter)
        
        vars=self.GetVars(EqnsAfter)
        
        soln=self.SolvingEqns(EqnsAfter,vars)
        #print(soln)
        res=self.GetVoltagePower(ResValue, ResMethod, ResCurrent, CapValue, CapMethod,
                                 CapCurrent, IndValue, IndMethod, IndCurrent, soln,
                                 omega, VSValue, CSValue, VSCurrent, CSVoltage, VSMethod,
                                 CSMethod)
        #print(res)
        final_result=[[soln],res]
        return final_result
    def regulator(self,ResValue,ResMethod,ResCurrent,CapValue,CapMethod,
                  CapCurrent,IndValue,IndMethod,IndCurrent,
                  VSValue,VSMethod,VSCurrent,CSValue,
                  CSMethod,CSVoltage,Loops,MoreEqns):####### regulates when solving using super position or without it
        omega=[]
        for source in VSValue:
            if ":" in source:
                list=source.split(":")
                omega.append(list[1])
        for source in CSValue:
            if ":" in source:
                list=source.split(":")
                omega.append(list[1])
        s=0
        for i in omega:
            if i!=omega[0]:
                s=1
        soln=[]
        if s==0:
            soln=self.SolvingAllNotSuper(ResValue, ResMethod, ResCurrent, CapValue,
                                         CapMethod, CapCurrent, IndValue, IndMethod,
                                         IndCurrent, VSValue, VSMethod, VSCurrent, CSValue,
                                         CSMethod, CSVoltage, Loops, MoreEqns)
            
        else:
            soln=self.SolvingAllSuper(ResValue, ResMethod, ResCurrent, CapValue,
                                      CapMethod, CapCurrent, IndValue, IndMethod,
                                      IndCurrent, VSValue, VSMethod, VSCurrent, CSValue,
                                      CSMethod, CSVoltage, Loops, MoreEqns)
        
        return soln
    def GetVoltagePower(self,ResValue,ResMethod,ResCurrent,CapValue,CapMethod,CapCurrent,
                   IndValue,IndMethod,IndCurrent,solns,omega,VSValue,CSValue,VSCurrent,
                   CSVoltage,VSMethod,CSMethod):
        voltages=[]
        powers=[]
        PowerFactors=[]
        power_abs=0j
        power_del=0j
        for index in range(0,len(ResValue)):
            if self.CheckNumeric(ResValue[index]) and self.CheckNumeric(ResCurrent[index]):
                current=self.ConvertToCartisien(ResCurrent[index])
                volt=str(complex(ResValue[index])*complex(current))
                voltages.append("Res: "+ResValue[index]+" : "+ResMethod[index]+" : "+volt+" V")
                power=str(complex(ResValue[index])*complex(current).conjugate()*complex(current))
                power_abs+=complex(power)
                powers.append("Res: "+ResValue[index]+" : "+ResMethod[index]+" : "+power+" VA")
                PowerFactors.append("Res: "+ResValue[index]+" : "+ResMethod[index]+" : 1 inphase")
            elif self.CheckNumeric(ResValue[index]) and not self.CheckNumeric(ResCurrent[index]):
                current=""
                for soln in solns:
                    if ResCurrent[index] in soln:
                        list_soln=soln.split("=")
                        current=list_soln[1]
                volt=str(complex(ResValue[index])*complex(current))
                voltages.append("Res: "+ResValue[index]+" : "+ResMethod[index]+" : "+volt+" V")
                power=str(complex(ResValue[index])*complex(current).conjugate()*complex(current))
                power_abs+=complex(power)
                powers.append("Res: "+ResValue[index]+" : "+ResMethod[index]+" : "+power+" VA")
                PowerFactors.append("Res: "+ResValue[index]+" : "+ResMethod[index]+" : 1 inphase")
            elif not self.CheckNumeric(ResValue[index]) and self.CheckNumeric(ResCurrent[index]):
                current=self.ConvertToCartisien(ResCurrent[index])
                value=""
                for soln in solns:
                    if ResValue[index] in soln:
                        list_soln=soln.split("=")
                        value=list_soln[1]
                volt=str(complex(value)*complex(current))
                voltages.append("Res: "+ResValue[index]+" : "+ResMethod[index]+" : "+volt+" V")
                power=str(complex(value)*complex(current).conjugate()*complex(current))
                power_abs+=complex(power)
                powers.append("Res: "+ResValue[index]+" : "+ResMethod[index]+" : "+power+" VA")
                PowerFactors.append("Res: "+ResValue[index]+" : "+ResMethod[index]+" : 1 inphase")
        
        for index in range(0,len(CapValue)):
            if self.CheckNumeric(CapValue[index]) and self.CheckNumeric(CapCurrent[index]):
                current=self.ConvertToCartisien(CapCurrent[index])
                impedance=""
                if "j" in CapValue[index]:
                    impedance=CapValue[index]
                else:
                    impedance="-"+str(1/(float(CapValue[index])*omega))+"j"
                volt=str(complex(impedance)*complex(current))
                voltages.append("Cap: "+CapValue[index]+" : "+CapMethod[index]+" : "+volt+" V")
                power=str(complex(impedance)*complex(current)*complex(current).conjugate())
                leading_laging=""
                if complex(power).imag<0:   #delivered
                    power_del+=complex(power)
                    leading_laging=" leading"
                else:
                    power_abs+=complex(power)
                    leading_laging=" laging"
                powers.append("Cap: "+CapValue[index]+" : "+CapMethod[index]+" : "+power+" VA")
                if complex(power).__abs__()!=0:
                    PowerFactors.append("Cap: "+CapValue[index]+" : "+CapMethod[index]+" : "+str(complex(power).real/complex(power).__abs__())+leading_laging)
            elif self.CheckNumeric(CapValue[index]) and not self.CheckNumeric(CapCurrent[index]):
                current=""
                impedance=""
                if "j" in CapValue[index]:
                    impedance=CapValue[index]
                else:
                    impedance="-"+str(1/(float(CapValue[index])*omega))+"j"
                for soln in solns:
                    if CapCurrent[index] in soln:
                        list_soln=soln.split("=")
                        current=list_soln[1]
                volt=str(complex(impedance)*complex(current))
                voltages.append("Cap: "+CapValue[index]+" : "+CapMethod[index]+" : "+volt+" V")
                power=str(complex(impedance)*complex(current)*complex(current).conjugate())
                leading_laging=""
                if complex(power).imag<0:   #delivered
                    power_del+=complex(power)
                    leading_laging=" leading"
                else:
                    power_abs+=complex(power)
                    leading_laging=" laging"
                powers.append("Cap: "+CapValue[index]+" : "+CapMethod[index]+" : "+power+" VA")
                if complex(power).__abs__()!=0:
                    PowerFactors.append("Cap: "+CapValue[index]+" : "+CapMethod[index]+" : "+str(complex(power).real/complex(power).__abs__())+leading_laging)
            elif not self.CheckNumeric(CapValue[index]) and self.CheckNumeric(CapCurrent[index]):
                current=self.ConvertToCartisien(CapCurrent[index])
                impedance=""
                for soln in solns:
                    if CapValue[index]+"c" in soln:
                        list_soln=soln.split("=")
                        impedance=list_soln[1]
                volt=str(complex(impedance)*complex(current))
                voltages.append("Cap: "+CapValue[index]+" : "+CapMethod[index]+" : "+volt+" V")
                power=str(complex(impedance)*complex(current)*complex(current).conjugate())
                leading_laging=""
                if complex(power).imag<0:   #delivered
                    power_del+=complex(power)
                    leading_laging=" leading"
                else:
                    power_abs+=complex(power)
                    leading_laging=" laging"
                powers.append("Cap: "+CapValue[index]+" : "+CapMethod[index]+" : "+power+" VA")
                if complex(power).__abs__()!=0:
                    PowerFactors.append("Cap: "+CapValue[index]+" : "+CapMethod[index]+" : "+str(complex(power).real/complex(power).__abs__())+leading_laging)
        
        for index in range(0,len(IndValue)):
            if self.CheckNumeric(IndValue[index]) and self.CheckNumeric(IndCurrent[index]):
                impedance=""
                if "j" in IndValue[index]:
                    impedance=IndValue[index]
                else:
                    impedance=str(float(IndValue[index])*omega)+"j"
                current=self.ConvertToCartisien(IndCurrent[index])
                volt=str(complex(impedance)*complex(current))
                voltages.append("Ind: "+IndValue[index]+" : "+IndMethod[index]+" : "+volt+" V")
                power=str(complex(impedance)*complex(current)*complex(current).conjugate())
                leading_laging=""
                if complex(power).imag<0:   #delivered
                    power_del+=complex(power)
                    leading_laging=" leading"
                else:
                    power_abs+=complex(power)
                    leading_laging=" laging"
                powers.append("Ind: "+IndValue[index]+" : "+IndMethod[index]+" : "+power+" VA")
                if complex(power).__abs__()!=0:
                    PowerFactors.append("Ind: "+IndValue[index]+" : "+IndMethod[index]+" : "+str(complex(power).real/complex(power).__abs__())+leading_laging)
            elif self.CheckNumeric(IndValue[index]) and not self.CheckNumeric(IndCurrent[index]):
                current=""
                impedance=""
                if "j" in IndValue[index]:
                    impedance=IndValue[index]
                else:
                    impedance=str(float(IndValue[index])*omega)+"j"
                for soln in solns:
                    if IndCurrent[index] in soln:
                        list_soln=soln.split("=")
                        current=list_soln[1]
                volt=str(complex(impedance)*complex(current))
                voltages.append("Ind: "+IndValue[index]+" : "+IndMethod[index]+" : "+volt+" V")
                power=str(complex(impedance)*complex(current)*complex(current).conjugate())
                leading_laging=""
                if complex(power).imag<0:   #delivered
                    power_del+=complex(power)
                    leading_laging=" leading"
                else:
                    power_abs+=complex(power)
                    leading_laging=" laging"
                powers.append("Ind: "+IndValue[index]+" : "+IndMethod[index]+" : "+power+" VA")
                if complex(power).__abs__()!=0:
                    PowerFactors.append("Ind: "+IndValue[index]+" : "+IndMethod[index]+" : "+str(complex(power).real/complex(power).__abs__())+leading_laging)
            elif not self.CheckNumeric(IndValue[index]) and self.CheckNumeric(IndCurrent[index]):
                current=self.ConvertToCartisien(IndCurrent[index])
                impedance=""
                for soln in solns:
                    list_soln=soln.split("=")
                    value=list_soln[1]
                volt=str(complex(impedance)*complex(current))
                voltages.append("Ind: "+IndValue[index]+" : "+IndMethod[index]+" : "+volt+" V")
                power=str(complex(impedance)*complex(current)*complex(current).conjugate())
                leading_laging=""
                if complex(power).imag<0:   #delivered
                    power_del+=complex(power)
                    leading_laging=" leading"
                else:
                    power_abs+=complex(power)
                    leading_laging=" laging"
                powers.append("Ind: "+IndValue[index]+" : "+IndMethod[index]+" : "+power+" VA")
                if complex(power).__abs__()!=0:
                    PowerFactors.append("Ind: "+IndValue[index]+" : "+IndMethod[index]+" : "+str(complex(power).real/complex(power).__abs__())+leading_laging)
        
        for index in range(0,len(VSValue)):
            if self.CheckNumeric(VSValue[index]) and self.CheckNumeric(VSCurrent[index]):
                value=self.ConvertToCartisien(VSValue[index])
                current=self.ConvertToCartisien(VSCurrent[index])
                power=str(-1*complex(value)*complex(current).conjugate())
                leading_laging=""
                if complex(power).imag<0:   #delivered
                    power_del+=complex(str(complex(power).imag)+"j")
                    leading_laging=" leading"
                else:
                    power_abs+=complex(str(complex(power).imag)+"j")
                    leading_laging=" laging"
                if complex(power).real<0:   #delivered
                    power_del+=complex(power).real
                else:
                    power_abs+=complex(power).real
                powers.append("VS: "+VSValue[index]+" : "+VSMethod[index]+" : "+power+" VA")
                if complex(power).__abs__()!=0:
                    PowerFactors.append("VS: "+VSValue[index]+" : "+VSMethod[index]+" : "+str(abs(complex(power).real)/complex(power).__abs__())+leading_laging)
            elif self.CheckNumeric(VSValue[index]) and not self.CheckNumeric(VSCurrent[index]):
                value=self.ConvertToCartisien(VSValue[index])
                current=""
                for soln in solns:
                    if VSCurrent[index] in soln:
                        list_soln=soln.split("=")
                        current=list_soln[1]
                power=str(-1*complex(value)*complex(current).conjugate())
                leading_laging=""
                if complex(power).imag<0:   #delivered
                    power_del+=complex(str(complex(power).imag)+"j")
                    leading_laging=" leading"
                else:
                    power_abs+=complex(str(complex(power).imag)+"j")
                    leading_laging=" laging"
                if complex(power).real<0:   #delivered
                    power_del+=complex(power).real
                else:
                    power_abs+=complex(power).real
                powers.append("VS: "+VSValue[index]+" : "+VSMethod[index]+" : "+power+" VA")
                if complex(power).__abs__()!=0:
                    PowerFactors.append("VS: "+VSValue[index]+" : "+VSMethod[index]+" : "+str(abs(complex(power).real)/complex(power).__abs__())+leading_laging)
            elif not self.CheckNumeric(VSValue[index]) and self.CheckNumeric(VSCurrent[index]):
                value=""
                current=self.ConvertToCartisien(VSCurrent[index])
                var=VSValue[index]
                op=1
                if "*" in VSValue[index]:
                    list_value=VSValue[index].split("*")
                    var=list_value[1]
                    op=list_value[0]
                for soln in solns:
                    if var in soln:
                        list_soln=soln.split("=")
                        value=list_soln[1]
                power=str(-1*complex(current).conjugate()*complex(value)*complex(op))
                leading_laging=""
                if complex(power).imag<0:   #delivered
                    power_del+=complex(str(complex(power).imag)+"j")
                    leading_laging=" leading"
                else:
                    power_abs+=complex(str(complex(power).imag)+"j")
                    leading_laging=" laging"
                if complex(power).real<0:   #delivered
                    power_del+=complex(power).real
                else:
                    power_abs+=complex(power).real
                powers.append("VS: "+VSValue[index]+" : "+VSMethod[index]+" : "+power+" VA")
                if complex(power).__abs__()!=0:
                    PowerFactors.append("VS: "+VSValue[index]+" : "+VSMethod[index]+" : "+str(abs(complex(power).real)/complex(power).__abs__())+leading_laging)
            elif not self.CheckNumeric(VSValue[index]) and not self.CheckNumeric(VSCurrent[index]):
                current=""
                value=""
                var=VSValue[index]
                op=1
                if "*" in VSValue[index]:
                    list_value=VSValue[index].split("*")
                    var=list_value[1]
                    op=list_value[0]
                for soln in solns:
                    if var in soln:
                        list_soln=soln.split("=")
                        value=list_soln[1]
                    if VSCurrent[index] in soln:
                        list_soln=soln.split("=")
                        current=list_soln[1]
                power=str(complex(current).conjugate()*complex(value)*complex(op)*-1)
                if complex(power).imag<0:   #delivered
                    power_del+=complex(str(complex(power).imag)+"j")
                    leading_laging=" leading"
                else:
                    power_abs+=complex(str(complex(power).imag)+"j")
                    leading_laging=" laging"
                if complex(power).real<0:   #delivered
                    power_del+=complex(power).real
                else:
                    power_abs+=complex(power).real
                powers.append("VS: "+VSValue[index]+" : "+VSMethod[index]+" : "+power+" VA")
                if complex(power).__abs__()!=0:
                    PowerFactors.append("VS: "+VSValue[index]+" : "+VSMethod[index]+" : "+str(abs(complex(power).real)/complex(power).__abs__())+leading_laging)
        for index in range(0,len(CSValue)):
            if self.CheckNumeric(CSValue[index]) and self.CheckNumeric(CSVoltage[index]):
                value=self.ConvertToCartisien(CSValue[index])
                voltage=self.ConvertToCartisien(VSValue[index])
                power=str(complex(value).conjugate()*complex(voltage))
                leading_laging=""
                if complex(power).imag<0:   #delivered
                    leading_laging=" leading"
                    power_del+=complex(str(complex(power).imag)+"j")
                else:
                    leading_laging=" laging"
                    power_abs+=complex(str(complex(power).imag)+"j")
                if complex(power).real<0:   #delivered
                    power_del+=complex(power).real
                else:
                    power_abs+=complex(power).real
                powers.append("CS: "+CSValue[index]+" : "+CSMethod[index]+" : "+power+" VA")
                if complex(power).__abs__()!=0:
                    PowerFactors.append("CS: "+CSValue[index]+" : "+CSMethod[index]+" : "+str(abs(complex(power).real)/complex(power).__abs__())+leading_laging)
            elif self.CheckNumeric(CSValue[index]) and not self.CheckNumeric(CSVoltage[index]):
                value=self.ConvertToCartisien(CSValue[index])
                voltage=""
                leading_laging=""
                for soln in solns:
                    if CSVoltage[index] in soln:
                        list_soln=soln.split("=")
                        voltage=list_soln[1]
                power=str(complex(value).conjugate()*complex(voltage))
                if complex(power).imag<0:   #delivered
                    power_del+=complex(str(complex(power).imag)+"j")
                    leading_laging=" leading"
                else:
                    power_abs+=complex(str(complex(power).imag)+"j")
                    leading_laging=" laging"
                if complex(power).real<0:   #delivered
                    power_del+=complex(power).real
                else:
                    power_abs+=complex(power).real
                powers.append("CS: "+CSValue[index]+" : "+CSMethod[index]+" : "+power+" VA")
                if complex(power).__abs__()!=0:
                    PowerFactors.append("CS: "+CSValue[index]+" : "+CSMethod[index]+" : "+str(abs(complex(power).real)/complex(power).__abs__())+leading_laging)
            elif not self.CheckNumeric(CSValue[index]) and self.CheckNumeric(CSVoltage[index]):
                
                value=""
                var=CSValue[index]
                op=1
                voltage=self.ConvertToCartisien(VSValue[index])
                leading_laging=""
                if "*" in CSValue[index]:
                    list_value=CSValue[index].split("*")
                    var = list_value[1]
                    op=list_value[0]
                for soln in solns:
                    if var in soln:
                        list_soln=soln.split("=")
                        value=list_soln[1]
                power=str(complex(value).conjugate()*complex(voltage)*complex(op))
                if complex(power).imag<0:   #delivered
                    power_del+=complex(str(complex(power).imag)+"j")
                    leading_laging=" leading"
                else:
                    power_abs+=complex(str(complex(power).imag)+"j")
                    leading_laging=" laging"
                if complex(power).real<0:   #delivered
                    power_del+=complex(power).real
                else:
                    power_abs+=complex(power).real
                powers.append("CS: "+CSValue[index]+" : "+CSMethod[index]+" : "+power+" VA")
                if complex(power).__abs__()!=0:
                    PowerFactors.append("CS: "+CSValue[index]+" : "+CSMethod[index]+" : "+str(abs(complex(power).real)/complex(power).__abs__())+leading_laging)
            elif not self.CheckNumeric(CSValue[index]) and not self.CheckNumeric(CSVoltage[index]):
                voltage=""
                value=""
                var=CSValue[index]
                op=1
               
                if "*" in CSValue[index]:
                    list_value=CSValue[index].split("*")
                    var=list_value[1]
                    op=list_value[0]
                for soln in solns:
                    if var in soln:
                        list_soln=soln.split("=")
                        value=list_soln[1]
                    if CSVoltage[index] in soln:
                        list_soln=soln.split("=")
                        voltage=list_soln[1]
                power=str(complex(value).conjugate()*complex(voltage)*complex(op))
                if complex(power).imag<0:   #delivered
                    power_del+=complex(str(complex(power).imag)+"j")
                    leading_laging=" leading"
                else:
                    power_abs+=complex(str(complex(power).imag)+"j")
                    leading_laging=" laging"
                if complex(power).real<0:   #delivered
                    power_del+=complex(power).real
                else:
                    power_abs+=complex(power).real
                powers.append("CS: "+CSValue[index]+" : "+CSMethod[index]+" : "+power+" VA")
                if complex(power).__abs__()!=0:
                    PowerFactors.append("CS: "+CSValue[index]+" : "+CSMethod[index]+" : "+str(abs(complex(power).real)/complex(power).__abs__())+leading_laging)
        list_result=[voltages,powers,PowerFactors,[power_abs,power_del]]
        return list_result
    def ModifyingLastResult(self,soln):
        
        SuperPosition=False
        for i in soln:
            for j in i:
                for item in j:
                    
                    if "cos" in str(item):
                        SuperPosition=True
                        break
        if SuperPosition==False:
            
            for i in soln:
                for j in i:
                    for index in range(0,len(j)):
                        if "=" in str(j[index]):
                            list_item=j[index].split("=")
                            solution=complex(list_item[1])
                            real_part=str(solution.real)
                            imag_part=str(solution.imag)
                            if "e" in real_part and "e" in imag_part:
                                solution="0.0"
                            elif "e" in real_part and not "e" in imag_part:
                                solution=str(imag_part)+"j"
                            elif not "e" in real_part and "e" in imag_part:
                                solution=str(real_part)
                            j[index]=list_item[0]+"="+str(solution)
                            real_part=str(complex(solution).real)
                            imag_part=str(complex(solution).imag)
                            if "." in real_part:
                                list_real_part=real_part.split(".")
                                kasr=list_real_part[1]
                                while len(kasr)>4:
                                    kasr=kasr[0:len(kasr)-1]
                                real_part=list_real_part[0]+"."+kasr
                            if "." in imag_part:
                                list_imag_part=imag_part.split(".")
                                kasr=list_imag_part[1]
                                while len(kasr)>4:
                                    kasr=kasr[0:len(kasr)-1]
                                imag_part=list_imag_part[0]+"."+kasr
                            solution=complex(float(real_part),float(imag_part))
                            j[index]=list_item[0]+"="+str(solution)
                        if ":" in str(j[index]):
                            
                            list=j[index].split(":")
                            s=0
                            try:
                                value=list[-1].replace("VA","")
                                value=value.replace("V","")
                                value=value.strip()
                                a=complex(value)
                                s=0
                            except:
                                s=1
                            if s==0:
                                removed=""
                                solution=list[-1]
                                if "VA" in list[-1]:
                                    solution=list[-1].replace("VA","")
                                    removed="VA"
                                if "V" in solution:
                                    solution=solution.replace("V","")
                                    removed="V"
                                solution=solution.strip()
                                solution=complex(solution)
                                real_part=str(solution.real)
                                imag_part=str(solution.imag)
                                if "e" in real_part and "e" in imag_part:
                                    solution="0.0"
                                elif "e" in real_part and not "e" in imag_part:
                                    solution=str(imag_part)+"j"
                                elif not "e" in real_part and "e" in imag_part:
                                    solution=real_part
                                
                                j[index]=list[0]+":"+list[1]+":"+list[2]+": "+str(solution)+" "+removed
                                real_part=str(complex(solution).real)
                                imag_part=str(complex(solution).imag)
                                if "." in real_part:
                                    list_real_part=real_part.split(".")
                                    kasr=list_real_part[1]
                                    while len(kasr)>4:
                                        kasr=kasr[0:len(kasr)-1]
                                    real_part=list_real_part[0]+"."+kasr
                                if "." in imag_part:
                                    list_imag_part=imag_part.split(".")
                                    kasr=list_imag_part[1]
                                    while len(kasr)>4:
                                        kasr=kasr[0:len(kasr)-1]
                                    imag_part=list_imag_part[0]+"."+kasr
                                solution=complex(float(real_part),float(imag_part))
                                j[index]=list[0]+":"+list[1]+":"+list[2]+": "+str(solution)+" "+removed
                                
                            else:
                                solution=list[-1].strip()
                                list_solution=solution.split(" ")
                                solution=list_solution[0]+" "+list_solution[1]
                                kasr=list_solution[0]
                                r=0
                                if "e" in kasr:
                                    solution="0.0 "+ list_solution[1]
                                    r=1
                                if r==0:
                                    if "." in kasr:
                                        list_kasr=list_solution[0].split(".")
                                        kasr=list_kasr[1]
                                        while len(kasr)>4:
                                            kasr=kasr[0:len(kasr)-1]
                                            solution=list_kasr[0]+"."+kasr+" "+list_solution[1]
                                j[index]=list[0]+":"+list[1]+":"+list[2]+": "+str(solution)
                        if not "=" in str(j[index]) and not ":" in str(j[index]):
                            solution=complex(j[index])
                            real_part=str(solution.real)
                            imag_part=str(solution.imag)
                            if "e" in real_part and not "e" in imag_part:
                                solution=imag_part+"j"
                            elif not "e" in real_part and "e" in imag_part:
                                solution=real_part
                            elif "e" in real_part and "e" in imag_part:
                                solution="0.0"
                            solution=complex(solution)
                            real_part=str(solution.real)
                            imag_part=str(solution.imag)
                            if "." in real_part:
                                list_kasr=real_part.split(".")
                                kasr=list_kasr[1]
                                while len(kasr)>4:
                                    kasr=kasr[:len(kasr)-1]
                                real_part=float(list_kasr[0]+"."+kasr)
                            if "." in imag_part:
                                list_kasr=imag_part.split(".")
                                kasr=list_kasr[1]
                                while len(kasr)>4:
                                    kasr=kasr[:len(kasr)-1]
                                imag_part=float(list_kasr[0]+"."+kasr)
                            j[index]=str(complex(real_part,imag_part))
        return soln
    def GetVarsElements(self,list_solution,ResValue, ResMethod, ResCurrent, CapValue, CapMethod,
                        CapCurrent, IndValue, IndMethod, IndCurrent, VSValue,
                        VSMethod, VSCurrent, CSValue, CSMethod, CSVoltage):
                        
        
        # print(list_solution)
        # for i in list_solution:
        #     print(i)
        pf_type="inphase"
        mode="Res"
        Resistances=self.process(ResValue, ResMethod, ResCurrent, list_solution, mode, pf_type)
        pf_type="leading"
        mode="Cap"
        Capacitors=self.process(CapValue, CapMethod, CapCurrent, list_solution, mode, pf_type)
        pf_type="laging"
        mode="Ind"
        Inductors=self.process(IndValue, IndMethod, IndCurrent, list_solution, mode, pf_type)
        mode="VS"
        pf_type=None
        VSources=self.process(VSValue, VSMethod, VSCurrent, list_solution, mode, pf_type)
        mode="CS"
        pf_type=None
        CSources=self.process(CSValue, CSMethod, CSVoltage, list_solution, mode, pf_type)
        # print("\n")
        # print("Resistances")
        # print(Resistances)
        # print("\n")
        # print("Capacitors")
        # print(Capacitors)
        # print("\n")
        # print("Inductors")
        # print(Inductors)
        # print("\n")
        # print("VSources")
        # print(VSources)
        # print("\n")
        # print("CSources")
        # print(CSources)
        list_elements=[]
        for list in Resistances:
            list_elements.append(list)
        for list in Capacitors:
            list_elements.append(list)
        for list in Inductors:
            list_elements.append(list)
        for list in VSources:
            list_elements.append(list)
        for list in CSources:
            list_elements.append(list)
        list_elements.append([list_solution[-1],list_solution[-2]])
        return list_elements
    def process(self,list_value,list_method,list_current,list_solution,mode,pf_type):
        
        list_result=[]
        index=0
        for value in list_value:
            list_info=[]
            ### element
            
            ### type
            list_info.append(mode)
            ### value
            if self.CheckNumeric(value):
                list_info.append(value)
            else:
                found=False
                ## searching for it's value in soln
                for solution in list_solution:
                    if "=" in solution:
                        list=solution.split("=")
                        if value ==list[0]:
                            list_info.append(list[1])
                            found=True
                            break
                if not found:
                    list_info.append(value)
            ### method
            list_info.append(list_method[index])
            ### current
            if self.CheckNumeric(list_current[index]):
                list_info.append(list_current[index])
            else:
                ## searching for current in soln
                found=False
                for solution in list_solution:
                    if "=" in solution:
                        list=solution.split("=")
                        if list_current[index]==list[0]:
                            list_info.append(list[1])
                            found=True
                            break
                if not found:
                    list_info.append(list_current[index])
            ### voltage,power,power factor
            for solution in list_solution:
                if ":" in solution:
                    list=solution.split(":")
                    if list[0]==mode and list[2].strip()==list_method[index] and "VA" in list[3] and list[1].strip()==value:
                        list_info.append(list[-1].strip())
                    elif list[0]==mode and list[2].strip()==list_method[index] and "V" in list[3] and list[1].strip()==value:
                        list_info.append(list[-1].strip())
                    elif list[0]==mode and list[2].strip()==list_method[index] and list[1].strip()==value:
                        list_info.append(list[-1].strip())
            
            list_result.append(list_info)
            index+=1
        return list_result
if __name__=="__main__":
        
    ResValue=["50","0","50"]
    ResMethod=["dc","ec","ac"]
    ResCurrent=["I3","I4","I2"]
    CapValue=["-25j"]
    CapMethod=["de"]
    CapCurrent=["I4"]
    IndValue=["25j"]
    IndMethod=["ba"]
    IndCurrent=["I1"]
    VSValue=["0.1v1"]
    VSMethod=["cb"]
    VSCurrent=["I1"]
    CSValue=["20I1","0.0143<65.22"]
    CSMethod=["cd","ca"]
    CSVoltage=["v2","v3"]
    Loops=["aca","abca","cdc","cdec"]
    
    MoreEqns=["v1:de"]
    
    
    a=App().PrepairingVars(ResValue, ResMethod, ResCurrent, CapValue, CapMethod,
                            CapCurrent, IndValue, IndMethod, IndCurrent, VSValue,
                            VSMethod, VSCurrent, CSValue, CSMethod, CSVoltage, Loops,
                            MoreEqns,"ShowAllSolns")
    
    for list in a:
        print(list)



    # a=App().ConvertToPolar("2")
    # print(a)
