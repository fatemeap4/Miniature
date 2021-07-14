from graphics import *  
#win2=GraphWin("miniature",1510,830)

def GUIJ(List,jump) :
    win3=GraphWin("miniatureI",1510,830)
    
    rectPC=Rectangle(Point(50,400),Point(100,500)) # pc ok shod
    rectPC.setFill('gray')
    rectPC.setOutline('gray')
    writ1=Point(75,450)
    recTPC=Text(writ1,'pc')
    rectPC.draw(win3)
    recTPC.draw(win3)

    #input line pc ok shod
    Line(Point(50,450),Point(25,450)).draw(win3)
    Line(Point(25,450),Point(25,40)).draw(win3)

    #output line pc instruction memory ok shod
    Line(Point(100,450),Point(190,450)).draw(win3)

    #output line pc multiplexer1 faz1
    Line(Point(150,450),Point(150,120)).draw(win3)

    #output line faz1 adder1
    Line(Point(150,120),Point(200,120)).draw(win3)
    Line(Point(150,100),Point(200,100)).draw(win3)
    Tri=Polygon(Point(200,60),Point(250,90),Point(250,130),Point(200,160))
    Tri.setFill('dim gray')
    Tri.setOutline('dim gray')
    Tri1txt=Text(Point(220,110),'Add')
    Tri1txt.setFill('dark slate gray')
    Tri.draw(win3)
    Tri1txt.draw(win3)
    TriAddtxt=Text(Point(140,100),'4')
    TriAddtxt.draw(win3)

    #faz2 instruction memory
    rectIns=Rectangle(Point(190,380),Point(400,520)) #faz2 mostatil
    rectIns.setFill('deep sky blue')
    rectIns.setOutline('sky blue')
    rectIns.draw(win3)
    rectInstxt=Text(Point(280,500),'Instruction Memory') #faz2 text
    rectInstxt.setSize(8)
    rectInstxt.setFill('blue2')
    rectInstxt.draw(win3)
    Ins=List
    rectInstxt1=Text(Point(295,450),Ins) #vase in vorodi migire tebqe paramtre ersal shode ono inja namayesh mide
    rectInstxt1.setSize(8)
    rectInstxt1.setFill('RoyalBlue4')
    rectInstxt1.draw(win3)

    #faz3 register file
    Line(Point(400,450),Point(430,450)).draw(win3)
    Line(Point(430,450),Point(430,350)).draw(win3)  #avale shakhe1
    Line(Point(430,350),Point(480,350)).draw(win3)  #shakhe 1         #rs
#    rs=Text(Point(440,345),"Rs=")
#    rs.setSize(8)
#    rs.draw(win2)
#    rsIn=Text(Point(460,345),integer_rsi)          ####inja bia vorodi rs ro shakharo bde
#    rsIn.setSize(8)
#    rsIn.draw(win2)
    Line(Point(430,450),Point(480,450)).draw(win3)  #shakhe2          #rt
#    rt=Text(Point(440,445),"Rt=")
#    rt.setSize(8)
#    rt.draw(win2)
#    rtIn=Text(Point(460,445),integer_rti)         #####injam bia vorodi vase rt bde neshon bde
#    rtIn.setSize(8)
#    rtIn.draw(win2)
    Line(Point(430,450),Point(430,550)).draw(win3)  #avale shakhe3
    #Line(Point(430,550),Point(480,550)).draw(win2)  #shakhe3          #rd
    #rd=Text(Point(440,545),"Rd=")
    #rd.setSize(8)
    #rd.draw(win2)
    #rdIn=Text(Point(460,545),integer_rdr)         ####inja bia vase rd adres bde k neshon bde
    #rdIn.setSize(8)
    #rdIn.draw(win2)

    # mostatil registerfile pink
    rectReg=Rectangle(Point(480,280),Point(735,680))
    rectReg.setFill('LightPink1')
    rectReg.setOutline('LightPink1')
    rectReg.draw(win3)
    
    #shoroe khonehaye arr toye registerfile
    rectReg0=Rectangle(Point(510,300),Point(720,320))
    rectReg0txt=Text(Point(610,310),' ')
    rectReg0txt.setSize(8)
    rectReg0txt.draw(win3)
    rectReg0.setOutline('red')
    rectReg0.draw(win3)
    
    
    rectReg1=Rectangle(Point(510,320),Point(720,340)) 
    rectReg1txt=Text(Point(610,310),' ')
    rectReg1txt.setSize(8)
    rectReg1txt.draw(win3)
    rectReg1.setOutline('red')
    rectReg1.draw(win3)

    
    rectReg2=Rectangle(Point(510,340),Point(720,360))
    rectReg2txt=Text(Point(610,350),' ') 
    rectReg2txt.setSize(8)
    rectReg2txt.draw(win3)
    rectReg2.setOutline('red')
    rectReg2.draw(win3)

    
    rectReg3=Rectangle(Point(510,360),Point(720,380))
    rectReg3txt=Text(Point(610,370),' ')
    rectReg3txt.setSize(8)
    rectReg3txt.draw(win3)
    rectReg3.setOutline('red')
    rectReg3.draw(win3)

    
    rectReg4=Rectangle(Point(510,380),Point(720,400))
    rectReg4txt=Text(Point(610,390),' ')
    rectReg4txt.setSize(8)
    rectReg4txt.draw(win3)
    rectReg4.setOutline('red')
    rectReg4.draw(win3)

    
    rectReg5=Rectangle(Point(510,400),Point(720,420))
    rectReg5txt=Text(Point(610,410),' ')
    rectReg5txt.setSize(8)
    rectReg5txt.draw(win3)
    rectReg5.setOutline('red')
    rectReg5.draw(win3)

    
    rectReg6=Rectangle(Point(510,420),Point(720,440))
    rectReg6txt=Text(Point(610,430),' ')
    rectReg6txt.setSize(8)
    rectReg6txt.draw(win3)
    rectReg6.setOutline('red')
    rectReg6.draw(win3)

    
    rectReg7=Rectangle(Point(510,440),Point(720,460))
    rectReg7txt=Text(Point(610,450),' ')
    rectReg7txt.setSize(8)
    rectReg7txt.draw(win3)
    rectReg7.setOutline('red')
    rectReg7.draw(win3)

    
    rectReg8=Rectangle(Point(510,460),Point(720,480))
    rectReg8txt=Text(Point(610,470),' ')
    rectReg8txt.setSize(8)
    rectReg8txt.draw(win3)
    rectReg8.setOutline('red')
    rectReg8.draw(win3)

    
    rectReg9=Rectangle(Point(510,480),Point(720,500))
    rectReg9txt=Text(Point(610,490),' ')
    rectReg9txt.setSize(8)
    rectReg9txt.draw(win3)
    rectReg9.setOutline('red')
    rectReg9.draw(win3)

    
    rectReg10=Rectangle(Point(510,500),Point(720,520))
    rectReg10txt=Text(Point(610,510),' ')
    rectReg10txt.setSize(8)
    rectReg10txt.draw(win3)
    rectReg10.setOutline('red')
    rectReg10.draw(win3)
    
    
    rectReg11=Rectangle(Point(510,520),Point(720,540))
    rectReg11txt=Text(Point(610,530),' ')
    rectReg11txt.setSize(8)
    rectReg11txt.draw(win3)
    rectReg11.setOutline('red')
    rectReg11.draw(win3)
    
    
    rectReg12=Rectangle(Point(510,540),Point(720,560))
    rectReg12txt=Text(Point(610,550),' ')
    rectReg12txt.setSize(8)
    rectReg12txt.draw(win3)
    rectReg12.setOutline('red')
    rectReg12.draw(win3)
    
    
    rectReg13=Rectangle(Point(510,560),Point(720,580))
    rectReg13txt=Text(Point(610,570),' ')
    rectReg13txt.setSize(8)
    rectReg13txt.draw(win3)
    rectReg13.setOutline('red')
    rectReg13.draw(win3)
    
    
    rectReg14=Rectangle(Point(510,580),Point(720,600))
    rectReg14txt=Text(Point(610,590),' ')
    rectReg14txt.setSize(8)
    rectReg14txt.draw(win3)
    rectReg14.setOutline('red')
    rectReg14.draw(win3)
    
    
    rectReg15=Rectangle(Point(510,600),Point(720,620))
    rectReg15txt=Text(Point(610,610),' ')
    rectReg15txt.setSize(8)
    rectReg15txt.draw(win3)
    rectReg15.setOutline('red')
    rectReg15.draw(win3)
    
    
    WritData=Text(Point(510,655),'Writ back')
    WritData.setSize(8)
    WritData.setFill('maroon3')
    WritData.draw(win3)
    
    
    #faz4  sign extention
    Line(Point(430,550),Point(430,750)).draw(win3)
    Line(Point(430,750),Point(500,750)).draw(win3)
    signO=Oval(Point(500,800),Point(700,700))
    signO.setFill('MistyRose3')
    signO.setOutline('MistyRose3')
    signO.draw(win3)
    signOtxt=Text(Point(600,750),'Sign Extension')
    signOtxt.setFill('dim gray')
    signOtxt.draw(win3)
    Line(Point(700,750),Point(760,750)).draw(win3)
#    ofset=Text(Point(730,745),'offset')
#    ofset.setSize(8)
#    ofset.setFill('blue')
#    ofset.draw(win2)
    
    
    #faz5 adder sign and add2 ok shod
    Line(Point(250,110),Point(800,110)).draw(win3) #az adder1 miad
    Line(Point(760,750),Point(760,270)).draw(win3)
    sll2=Circle(Point(760,235),35)
    sll2.setFill('salmon1')
    sll2.setOutline('salmon1')
    sll2.draw(win3)
    sll2txt=Text(Point(760,235),'Shift left 2')
    sll2txt.setFill('salmon4')
    sll2txt.setSize(8)
    sll2txt.draw(win3)
    Line(Point(760,200),Point(760,130)).draw(win3)
    Line(Point(760,130),Point(800,130)).draw(win3)
    Tri2=Polygon(Point(800,70),Point(845,100),Point(845,140),Point(800,170))
    Tri2.setFill('dim gray')
    Tri2.setOutline('dim gray')
    Tri2txt=Text(Point(820,120),'Add')
    Tri2txt.setFill('dark slate gray')
    Tri2.draw(win3)
    Tri2txt.draw(win3)
    
    
    
    #Output adder2
    Line(Point(740,110),Point(740,65)).draw(win3)
    Line(Point(740,65),Point(900,65)).draw(win3)
    Line(Point(900,65),Point(900,100)).draw(win3)
    Line(Point(900,100),Point(940,100)).draw(win3)
    Line(Point(845,120),Point(940,120)).draw(win3)
    Mux3=Oval(Point(940,65),Point(970,155))
    Mux3.setFill('pale green')
    Mux3.setOutline('pale green')
    Mux3.draw(win3)
    mux3txt=Text(Point(955,83),'0 M')
    mux3txt.setSize(10)
    mux3txt.setFill('lime green')
    mux3txt.draw(win3)
    mux3txt=Text(Point(955,100),'  U')
    mux3txt.setSize(10)
    mux3txt.setFill('lime green')
    mux3txt.draw(win3)
    mux3txt=Text(Point(955,115),'1 X')
    mux3txt.setSize(10)
    mux3txt.setFill('lime green')
    mux3txt.draw(win3)
    Line(Point(970,110),Point(1070,110)).draw(win3) 
    Line(Point(1070,110),Point(1070,40)).draw(win3)
    Line(Point(1070,40),Point(25,40)).draw(win3)
    
    
    #faz6 output line register file
    Line(Point(735,350),Point(900,350)).draw(win3)
    rs=Text(Point(790,345),'out1')
    rs.setFill('blue')
    rs.setSize(8)
    rs.draw(win3)
    
#    t2='Out1='+str(rsi)
#    Out1=Text(Point(1300,125),str(t2))
#    Out1.setFill('blue')
#    Out1.setSize(10)
#    Out1.draw(win2)
#    
    rt=Text(Point(865,420 ),'out2')
    rt.setFill('blue')
    rt.setSize(8)
    rt.draw(win3)
    
#    t3='Out2='+str(offset)            #inja bayad offset ezafe beshe k out2 neshonesh bde
#    Out2=Text(Point(1300,150),str(t3))
#    Out2.setFill('blue')
#    Out2.setSize(10)
#    Out2.draw(win2)
    
    Line(Point(735,410),Point(813,410)).draw(win3)
    Line(Point(760,440),Point(810,440)).draw(win3)
    Mux2=Oval(Point(810,380),Point(850,490))
    Mux2.setFill('pale green')
    Mux2.setOutline('pale green')
    Mux2.draw(win3)
    Mux2txt1=Text(Point(830,410),'0 M')
    Mux2txt1.setSize(10)
    Mux2txt1.setFill('lime green')
    Mux2txt1.draw(win3)
    Mux2txt2=Text(Point(830,430),'  U')
    Mux2txt2.setSize(10)
    Mux2txt2.setFill('lime green')
    Mux2txt2.draw(win3)
    Mux2txt3=Text(Point(830,450),'1 X')
    Mux2txt3.setSize(10)
    Mux2txt3.setFill('lime green')
    Mux2txt3.draw(win3)
    Line(Point(850,435),Point(900,435)).draw(win3) #vorodi alu
    Line(Point(790,410),Point(790,600)).draw(win3)
    Line(Point(790,600),Point(1030,600)).draw(win3) #vorodi2 mem


    #faz7 Alu
    Alu=Polygon(Point(900,300),Point(960,320),Point(960,455),Point(900,485))
    Alu.setFill('PaleVioletRed1')
    Alu.setOutline('PaleVioletRed1')
    Alu.draw(win3)
    Alutxt=Text(Point(930,387.5),'ALU')
    Alutxt.setFill('maroon4')
    Alutxt.draw(win3)


    #output Alu
    Line(Point(960,400),Point(1030,400)).draw(win3)
    Out=Text(Point(985,390),'Output3')
    Out.setFill('blue')
    Out.setSize(8)
    Out.draw(win3)
    
#    t4='Output3='+str(rti)
#    OutPut=Text(Point(1300,100),str(t4))
#    OutPut.setSize(10)
#    OutPut.setFill('blue')
#    OutPut.draw(win2)

    #Memory
    rectmem=Rectangle(Point(1030,350),Point(1120,650))
    rectmem.setFill('MediumOrchid1')
    rectmem.setOutline('MediumOrchid1')
    rectmem.draw(win3)
    memtxt=Text(Point(1075,500),'Memory')
    memtxt.setFill('MediumOrchid4')
    memtxt.setSize(8)
    memtxt.draw(win3)


    #multiplxer2
    Line(Point(1120,550),Point(1180,550)).draw(win3)
    Line(Point(990,400),Point(990,700)).draw(win3)
    Line(Point(990,700),Point(1150,700)).draw(win3)
    Line(Point(1150,700),Point(1150,580)).draw(win3)
    Line(Point(1150,580),Point(1180,580)).draw(win3)
    mux2=Oval(Point(1180,520),Point(1210,610))
    mux2.setFill('pale green')
    mux2.setOutline('pale green')
    mux2.draw(win3)
    mux2txt1=Text(Point(1195,540),'1 M')
    mux2txt1.setFill('lime green')
    mux2txt1.setSize(8)
    mux2txt1.draw(win3)
    mux2txt2=Text(Point(1195,560),' U')
    mux2txt2.setFill('lime green')
    mux2txt2.setSize(8)
    mux2txt2.draw(win3)
    mux2txt3=Text(Point(1195,580),'0 X')
    mux2txt3.setFill('lime green')
    mux2txt3.setSize(8)
    mux2txt3.draw(win3)


    #output mux2
    Line(Point(1210,565),Point(1250,565)).draw(win3)
    Line(Point(1250,565),Point(1250,810)).draw(win3)
    Line(Point(1250,810),Point(410,810)).draw(win3)
    Line(Point(410,810),Point(410,655)).draw(win3)
    Line(Point(410,655),Point(480,655)).draw(win3)

    #jump address
    text='jump address = '+str(jump)
    jumpAdd=Text(Point(480,35),text)
    jumpAdd.setFill('blue')
    jumpAdd.setSize(10)
    jumpAdd.draw(win3)




    
