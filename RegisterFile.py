from graphics import *
win=GraphWin("miniatureREGISTER_FILE",1510,830)

def RegisterFile(List) :

    rectPC=Rectangle(Point(50,400),Point(100,500)) # pc ok shod
    rectPC.setFill('gray')
    rectPC.setOutline('gray')
    writ1=Point(75,450)
    recTPC=Text(writ1,'pc')
    rectPC.draw(win)
    recTPC.draw(win)

    #input line pc ok shod
    Line(Point(50,450),Point(25,450)).draw(win)
    Line(Point(25,450),Point(25,40)).draw(win)

    #output line pc instruction memory ok shod
    Line(Point(100,450),Point(190,450)).draw(win)

    #output line pc multiplexer1 faz1
    Line(Point(150,450),Point(150,120)).draw(win)

    #output line faz1 adder1
    Line(Point(150,120),Point(200,120)).draw(win)
    Line(Point(150,100),Point(200,100)).draw(win)
    Tri=Polygon(Point(200,60),Point(250,90),Point(250,130),Point(200,160))
    Tri.setFill('dim gray')
    Tri.setOutline('dim gray')
    Tri1txt=Text(Point(220,110),'Add')
    Tri1txt.setFill('dark slate gray')
    Tri.draw(win)
    Tri1txt.draw(win)
    TriAddtxt=Text(Point(140,100),'4')
    TriAddtxt.draw(win)

    #faz2 instruction memory
    rectIns=Rectangle(Point(190,380),Point(400,520)) #faz2 mostatil
    rectIns.setFill('deep sky blue')
    rectIns.setOutline('sky blue')
    rectIns.draw(win)
    rectInstxt=Text(Point(280,500),'Instruction Memory') #faz2 text
    rectInstxt.setSize(8)
    rectInstxt.setFill('blue2')
    rectInstxt.draw(win)
    
    #faz3 register file
    Line(Point(400,450),Point(430,450)).draw(win)
    Line(Point(430,450),Point(430,350)).draw(win)  #avale shakhe1
    Line(Point(430,350),Point(480,350)).draw(win)  #shakhe 1         #rs
    
    Line(Point(430,450),Point(480,450)).draw(win)  #shakhe2          #rt

    Line(Point(430,450),Point(430,550)).draw(win)  #avale shakhe3
    Line(Point(430,550),Point(480,550)).draw(win)  #shakhe3          #rd
    
    rectReg=Rectangle(Point(480,280),Point(735,680))   # mostatil registerfile pink
    rectReg.setFill('LightPink1')
    rectReg.setOutline('LightPink1')
    rectReg.draw(win)


    #shoroe khonehaye arr toye registerfile
    
    rectReg0=Rectangle(Point(510,300),Point(720,320))                    #reg0    
    rectReg0txt=Text(Point(610,310),List[0])    #inja mohtavaye register0 rikhte mishe
    rectReg0txt.setSize(8)
    rectReg0txt.draw(win)
    rectReg0.setOutline('red')
    rectReg0.draw(win)

    rectReg1=Rectangle(Point(510,320),Point(720,340))   #reg1
    rectReg1txt=Text(Point(610,330),List[1])         # inja mohtava
    rectReg1txt.setSize(8)
    rectReg1txt.draw(win)
    rectReg1.setOutline('red')
    rectReg1.draw(win)

    rectReg2=Rectangle(Point(510,340),Point(720,360))   #reg2
    rectReg2txt=Text(Point(610,350),List[1])        # inja mohtava
    rectReg2txt.setSize(8)
    rectReg2txt.draw(win)
    rectReg2.setOutline('red')
    rectReg2.draw(win)

    rectReg3=Rectangle(Point(510,360),Point(720,380))    #reg3
    rectReg3txt=Text(Point(610,370),List[2])            #mohtava inja
    rectReg3txt.setSize(8)
    rectReg3txt.draw(win)
    rectReg3.setOutline('red')
    rectReg3.draw(win)


    rectReg4=Rectangle(Point(510,380),Point(720,400))     #reg4
    rectReg4txt=Text(Point(610,390),List[4])
    rectReg4txt.setSize(8)
    rectReg4txt.draw(win)
    rectReg4.setOutline('red')
    rectReg4.draw(win)


    rectReg5=Rectangle(Point(510,400),Point(720,420))
    rectReg5txt=Text(Point(610,410),List[5])
    rectReg5txt.setSize(8)
    rectReg5txt.draw(win)
    rectReg5.setOutline('red')
    rectReg5.draw(win)

    rectReg6=Rectangle(Point(510,420),Point(720,440))
    rectReg6txt=Text(Point(610,430),List[6])
    rectReg6txt.setSize(8)
    rectReg6txt.draw(win)
    rectReg6.setOutline('red')
    rectReg6.draw(win)


    rectReg7=Rectangle(Point(510,440),Point(720,460))
    rectReg7txt=Text(Point(610,450),List[7])
    rectReg7txt.setSize(8)
    rectReg7txt.draw(win)
    rectReg7.setOutline('red')
    rectReg7.draw(win)

    rectReg8=Rectangle(Point(510,460),Point(720,480))
    rectReg8txt=Text(Point(610,470),List[8])
    rectReg8txt.setSize(8)
    rectReg8txt.draw(win)
    rectReg8.setOutline('red')
    rectReg8.draw(win)

    rectReg9=Rectangle(Point(510,480),Point(720,500))
    rectReg9txt=Text(Point(610,490),List[9])
    rectReg9txt.setSize(8)
    rectReg9txt.draw(win)
    rectReg9.setOutline('red')
    rectReg9.draw(win)

    rectReg10=Rectangle(Point(510,500),Point(720,520))
    rectReg10txt=Text(Point(610,510),List[10])
    rectReg10txt.setSize(8)
    rectReg10txt.draw(win)
    rectReg10.setOutline('red')
    rectReg10.draw(win)

    rectReg11=Rectangle(Point(510,520),Point(720,540))
    rectReg11txt=Text(Point(610,530),List[11])
    rectReg11txt.setSize(8)
    rectReg11txt.draw(win)
    rectReg11.setOutline('red')
    rectReg11.draw(win)

    rectReg12=Rectangle(Point(510,540),Point(720,560))
    rectReg12txt=Text(Point(610,550),List[12])
    rectReg12txt.setSize(8)
    rectReg12txt.draw(win)
    rectReg12.setOutline('red')
    rectReg12.draw(win)

    rectReg13=Rectangle(Point(510,560),Point(720,580))
    rectReg13txt=Text(Point(610,570),List[13])
    rectReg13txt.setSize(8)
    rectReg13txt.draw(win)
    rectReg13.setOutline('red')
    rectReg13.draw(win)

    rectReg14=Rectangle(Point(510,580),Point(720,600))
    rectReg14txt=Text(Point(610,590),List[14])
    rectReg14txt.setSize(8)
    rectReg14txt.draw(win)
    rectReg14.setOutline('red')
    rectReg14.draw(win)

    rectReg15=Rectangle(Point(510,600),Point(720,620))
    rectReg15txt=Text(Point(610,610),List[15])
    rectReg15txt.setSize(8)
    rectReg15txt.draw(win)
    rectReg15.setOutline('red')
    rectReg15.draw(win)

    WritData=Text(Point(510,655),'Writ back')
    WritData.setSize(8)
    WritData.setFill('maroon3')
    WritData.draw(win)

    #faz4  sign extention
    Line(Point(430,550),Point(430,750)).draw(win)
    Line(Point(430,750),Point(500,750)).draw(win)
    signO=Oval(Point(500,800),Point(700,700))
    signO.setFill('MistyRose3')
    signO.setOutline('MistyRose3')
    signO.draw(win)
    signOtxt=Text(Point(600,750),'Sign Extension')
    signOtxt.setFill('dim gray')
    signOtxt.draw(win)
    Line(Point(700,750),Point(760,750)).draw(win)

    #faz5 adder sign and add2 ok shod
    Line(Point(250,110),Point(800,110)).draw(win) #az adder1 miad
    Line(Point(760,750),Point(760,270)).draw(win)
    sll2=Circle(Point(760,235),35)
    sll2.setFill('salmon1')
    sll2.setOutline('salmon1')
    sll2.draw(win)
    sll2txt=Text(Point(760,235),'Shift left 2')
    sll2txt.setFill('salmon4')
    sll2txt.setSize(8)
    sll2txt.draw(win)
    Line(Point(760,200),Point(760,130)).draw(win)
    Line(Point(760,130),Point(800,130)).draw(win)
    Tri2=Polygon(Point(800,70),Point(845,100),Point(845,140),Point(800,170))
    Tri2.setFill('dim gray')
    Tri2.setOutline('dim gray')
    Tri2txt=Text(Point(820,120),'Add')
    Tri2txt.setFill('dark slate gray')
    Tri2.draw(win)
    Tri2txt.draw(win)


    #Output adder2
    Line(Point(740,110),Point(740,65)).draw(win)
    Line(Point(740,65),Point(900,65)).draw(win)
    Line(Point(900,65),Point(900,100)).draw(win)
    Line(Point(900,100),Point(940,100)).draw(win)
    Line(Point(845,120),Point(940,120)).draw(win)
    Mux3=Oval(Point(940,65),Point(970,155))
    Mux3.setFill('pale green')
    Mux3.setOutline('pale green')
    Mux3.draw(win)
    mux3txt=Text(Point(955,83),'M')
    mux3txt.setSize(10)
    mux3txt.setFill('lime green')
    mux3txt.draw(win)
    mux3txt=Text(Point(955,98),'U')
    mux3txt.setSize(10)
    mux3txt.setFill('lime green')
    mux3txt.draw(win)
    mux3txt=Text(Point(955,113),'X')
    mux3txt.setSize(10)
    mux3txt.setFill('lime green')
    mux3txt.draw(win)
    Line(Point(970,110),Point(1070,110)).draw(win) 
    Line(Point(1070,110),Point(1070,40)).draw(win)
    Line(Point(1070,40),Point(25,40)).draw(win)


    #faz6 output line register file
    Line(Point(735,350),Point(900,350)).draw(win)
    Line(Point(735,410),Point(813,410)).draw(win)
    Line(Point(760,440),Point(810,440)).draw(win)
    Mux2=Oval(Point(810,380),Point(850,490))
    Mux2.setFill('pale green')
    Mux2.setOutline('pale green')
    Mux2.draw(win)
    Mux2txt1=Text(Point(830,410),'M')
    Mux2txt1.setSize(10)
    Mux2txt1.setFill('lime green')
    Mux2txt1.draw(win)
    Mux2txt2=Text(Point(830,430),'U')
    Mux2txt2.setSize(10)
    Mux2txt2.setFill('lime green')
    Mux2txt2.draw(win)
    Mux2txt3=Text(Point(830,450),'X')
    Mux2txt3.setSize(10)
    Mux2txt3.setFill('lime green')
    Mux2txt3.draw(win)
    Line(Point(850,435),Point(900,435)).draw(win) #vorodi alu
    Line(Point(790,410),Point(790,600)).draw(win)
    Line(Point(790,600),Point(1030,600)).draw(win) #vorodi2 mem

    #faz7 Alu
    Alu=Polygon(Point(900,300),Point(960,320),Point(960,455),Point(900,485))
    Alu.setFill('PaleVioletRed1')
    Alu.setOutline('PaleVioletRed1')
    Alu.draw(win)
    Alutxt=Text(Point(930,387.5),'ALU')
    Alutxt.setFill('maroon4')
    Alutxt.draw(win)


    #output Alu
    #lineZero=Line(Point(960,380),Point(1000,380))
    #lineZero.setFill('blue')
    #lineZero.draw(win)
    Line(Point(960,400),Point(1030,400)).draw(win)


    #Memory
    rectmem=Rectangle(Point(1030,350),Point(1120,650))
    rectmem.setFill('MediumOrchid1')
    rectmem.setOutline('MediumOrchid1')
    rectmem.draw(win)
    memtxt=Text(Point(1075,500),'Memory')
    memtxt.setFill('MediumOrchid4')
    memtxt.setSize(8)
    memtxt.draw(win)

    #multiplxer2
    Line(Point(1120,550),Point(1180,550)).draw(win)
    Line(Point(990,400),Point(990,700)).draw(win)
    Line(Point(990,700),Point(1150,700)).draw(win)
    Line(Point(1150,700),Point(1150,580)).draw(win)
    Line(Point(1150,580),Point(1180,580)).draw(win)
    mux2=Oval(Point(1180,520),Point(1210,610))
    mux2.setFill('pale green')
    mux2.setOutline('pale green')
    mux2.draw(win)
    mux2txt1=Text(Point(1195,540),'M')
    mux2txt1.setFill('lime green')
    mux2txt1.setSize(8)
    mux2txt1.draw(win)
    mux2txt2=Text(Point(1195,560),'U')
    mux2txt2.setFill('lime green')
    mux2txt2.setSize(8)
    mux2txt2.draw(win)
    mux2txt3=Text(Point(1195,580),'X')
    mux2txt3.setFill('lime green')
    mux2txt3.setSize(8)
    mux2txt3.draw(win)


    #output mux2
    Line(Point(1210,565),Point(1250,565)).draw(win)
    Line(Point(1250,565),Point(1250,810)).draw(win)
    Line(Point(1250,810),Point(410,810)).draw(win)
    Line(Point(410,810),Point(410,655)).draw(win)
    Line(Point(410,655),Point(480,655)).draw(win)










