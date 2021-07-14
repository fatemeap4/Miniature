###in the name of God
import re
import sys
from GUIRtype import *
from GUIItype import *
from time import sleep
from RegisterFile import *
from GUIJtype import *

f = input("Please enter the name of your desired file to read from : ")
file = open(f,"r")
cfile = open(f,"r")
list=[]
clist=[]
for line in file:
    line = line.rstrip()
    list.append(line)
print(list)
register_file = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

b_register_file = []  #register file list 32_bit
memory = [0]*65535

for i in range(0,65535):
    memory[i] = i
#print(memory)


for i in range(0,16):
    b_register_file.append("00000000000000000000000000000000")

#print(b_register_file)
def int_to_bin(x): #int to binary
    if x>((2**15)+1):
        sys.exit("This number is too large to be contained in 32 bits !")
    y = format(x,"b")
    z = 32 - len(y)
    p = str(0)
    for i in range(0,z-1):
        p = '0' + p
    y = str(y)
    p = p + y
    return p

def int_to_bin_16bit(x): #int to binary
    if x>((2**15)+1):
        sys.exit("This number is too large to be contained in 32 bits !")
    y = format(x,"b")
    z = 16 - len(y)
    p = str(0)
    for i in range(0,z-1):
        p = '0' + p
    y = str(y)
    p = p + y
    return p


def sign_Extention(of):
    list_16bit = []
    list_16bit.append(of)
    sing = list_16bit[0][0]
    #print(sing)
    if sing == "0":
        sing = "0000000000000000"+str(of)
    elif sing == "1" :
        sing = "1111111111111111"+str(of)
    return sing


def R_Type(each) :

    integer_rsr = int(rsr,2)  # $rs Address
    integer_rtr = int(rtr,2) # $rt Address
    integer_rdr = int(rdr,2) # $rd Address
    in_rsr = register_file[integer_rsr] # $rs content
    in_rtr = register_file[integer_rtr] # $rt content
    in_rdr = register_file[integer_rdr] # $rd content
    b_in_rsr = int_to_bin(in_rsr)
    b_in_rtr = int_to_bin(in_rtr)


    # ALU
    if op == "0000": #add
        in_rdr = in_rsr + in_rtr  #rd=rs+rt
        b_in_rdr = int_to_bin(in_rdr) #32_bit(rd)
        register_file[integer_rdr] = in_rdr #$rd=rd
        b_register_file[integer_rdr] = b_in_rdr #32 bit($rd=rd)
        
    elif op == "0001": #sub
        in_rdr = in_rsr - in_rtr
        b_in_rdr = int_to_bin(in_rdr)
        register_file[integer_rdr] = in_rdr
        b_register_file[integer_rdr] = b_in_rdr
        
    elif op == "0010": #slt
        if in_rsr<in_rtr:
            in_rdr = 1
            b_in_rdr = int_to_bin(1)
            register_file[integer_rdr] = in_rdr
            b_register_file[integer_rdr] = b_in_rdr
        else:
            in_rdr = 0
            b_in_rdr = int_to_bin(0)
            register_file[integer_rdr] = in_rdr
            b_register_file[integer_rdr] = b_in_rdr
            
    elif op == "0011": #orr
        in_rdr = (in_rsr | in_rtr)
        b_in_rdr = int_to_bin(in_rdr)
        register_file[integer_rdr] = in_rdr
        b_register_file[integer_rdr] = b_in_rdr
        
    elif op =="0100": #nand
        in_rdr = not(in_rsr & in_rtr)
        b_in_rdr = int_to_bin(in_rdr)
        register_file[integer_rdr] = in_rdr
        b_register_file[integer_rdr] = b_in_rdr

    GUIR(each,integer_rsr,integer_rtr,integer_rdr,b_in_rsr,b_in_rtr,b_in_rdr)
    sleep(1)
        

def I_Type(each) :
    integer_rsi = int(rsi,2)  # $rs Address
    integer_rti = int(rti,2)  # $rt Address
    integer_offseti = int(offseti,2) #offset_int content
    in_rsi = register_file[integer_rsi]  #rs content
    in_rti = register_file[integer_rti]  #rt content
    offseti_16bit = int_to_bin_16bit(integer_offseti) #offset_16bit
    offseti_32bit= sign_Extention(offseti_16bit)
    b_in_rsi = int_to_bin(in_rsi)
    b_in_rti = int_to_bin(in_rti)
    
    #ze_offset = zero_Extention(offseti_16bit)
    if op == "0101": #addi
        in_rti = in_rsi+integer_offseti #rt=rs+imm
        b_in_rti = int_to_bin(in_rti) #32(rt)
        register_file[integer_rti] = in_rti #$rt=rt
        b_register_file[integer_rti] = b_in_rti #32 bit($rt=rt)
       # print(b_in_rti)
    elif op == "0110" : #slti
        if in_rsi<integer_offseti :
            in_rti = 1
            b_in_rti = int_to_bin(in_rti)
        elif in_rsi>integer_offseti :
            in_rti = 0
            b_in_rti = int_to_bin(in_rti)
        register_file[integer_rti] = in_rti
        b_register_file[integer_rti] = b_in_rti
        
    elif op == "0111": #ori
        in_rti = (in_rsi | integer_offseti) #rt=rs|offset
        b_in_rti = int_to_bin(in_rti) #32(rt)
        register_file[integer_rti] = in_rti #$rt=rt
        b_register_file[integer_rti] = b_in_rti #32 bit($rt=rt)
        
    elif op == "1000" : #lui
        in_rti = offseti_32bit  #rt=32 bit(offset)
        b_in_rti = int_to_bin(in_rti)  #32(rt=32 bit(offset))
        register_file[integer_rti] = in_rti  #$rt=rt=32 bit(offset)
        b_register_file[integer_rti] = b_in_rti  #32 bit(rt=32 bit(offset)_
        
    elif op == "1001" : #lw
        mem_address = in_rsi + integer_offseti #mem_address = content(rsi) + content(offset)
        in_rti = memory[mem_address]   #content(rti) = memory[mem_address]
        b_in_rti = int_to_bin(memory[mem_address])  #32 bit(content(rti) = memory[mem_address])
        register_file[integer_rti] = in_rti
        b_register_file[integer_rti] = b_in_rti
        
    elif op == "1010" : #sw
        mem_address = in_rsi + integer_offseti  # mem_address = content(rsi) + content(offset)
        memory[mem_address] = in_rti  #memory[mem_address_] = content(rti)

    GUII(each,integer_rsi,integer_rti,b_in_rsi,b_in_rti,offseti_32bit)
    sleep(1)


def J_Type() :
    integer_offsetj = int(offsetj,2) #offsetj_int content
    for index,each in enumerate(list):
        jump = list[integer_offsetj]
        if jump[4:8] == "0000" or jump[4:8] == "0001" or jump[4:8] == "0010" or jump[4:8] == "0011" or jump[4:8] == "0100":
            #R_Type
            rsr = each[8:12]
            rtr = each[12:16]
            rdr = each[16:20]
            R_Type(each)

        elif jump[4:8] == "0101" or jump[4:8] == "0110" or jump[4:8] == "0111" or jump[4:8] == "1000" or jump[4:8] == "1001" or jump[4:8] == "1010" or jump[4:8] == "1011" or jump[4:8] == "1100" :
            #I_Type
            rsi = each[8:12]
            rti = each[12:16]
            offseti = each[16:]
            I_Type(each)



for index,each in enumerate(list):

    op = each[4:8]  #opcod
    #categorize by opcod
    if op == "0000" or op == "0001" or op == "0010" or op == "0011" or op == "0100":
        #R-Type
        rsr = each[8:12]
        rtr = each[12:16]
        rdr = each[16:20]
        R_Type(each)
        
    elif op == "0101" or op == "0110" or op == "0111" or op == "1000" or op == "1001" or op == "1010" or  op == "1100" :#or op == "1011" :
        #I_Type
        rsi = each[8:12]
        rti = each[12:16]
        offseti = each[16:]
        I_Type(each)
        
    elif op == "1011": #beq
        #I_Type
        rsi = each[8:12]
        rti = each[12:16]
        offseti = each[16:]
        integer_rsi = int(rsi, 2)  # $rs Address
        integer_rti = int(rti, 2)  # $rt Address
        integer_offseti = int(offseti, 2)  # offset_int content
        in_rsib = register_file[integer_rsi]  # rs content
        in_rtib = register_file[integer_rti]  # rt content
        if in_rsib == in_rtib:
            for index,each in enumerate(list):
                branch = list[integer_offseti]
            if branch[4:8] == "0000" or branch[4:8] == "0001" or branch[4:8] == "0010" or branch[4:8] == "0011" or branch[4:8] == "0100":
                op = branch[4:8]
                rsr = branch[8:12]
                rtr = branch[12:16]
                rdr = branch[16:20]
                R_Type(branch)
            elif branch[4:8] == "0101" or branch[4:8] == "0110" or branch[4:8] == "0111" or branch[4:8] == "1000" or branch[4:8] == "1001" or branch[4:8] == "1010" or branch[4:8] =="1100" :
                op = branch[4:8]
                rsi = branch[8:12]
                rti = branch[12:16]
                offseti = branch[16:]
                I_Type(branch)

    elif op == "1101" or op == "1110":
        #J_Type
        offsetj = each[16:]
        integer_offsetj = int(offsetj, 2)  # offsetj_int content

        for index,each in enumerate(list):
            jump = list[integer_offsetj]
        if jump[4:8] == "0000" or jump[4:8] == "0001" or jump[4:8] == "0010" or jump[4:8] == "0011" or jump[4:8] == "0100":
            op = jump[4:8]
            rsr = jump[8:12]
            rtr = jump[12:16]
            rdr = jump[16:20]
            GUIJ(each,integer_offsetj)
            sleep(2)
            R_Type(each)
        elif jump[4:8] == "0101" or jump[4:8] == "0110" or jump[4:8] == "0111" or jump[4:8] == "1000" or jump[4:8] == "1001" or jump[4:8] == "1010" or jump[4:8] =="1100" :
            op = jump[4:8]
            rsi = jump[8:12]
            rti = jump[12:16]
            offseti = jump[16:]
            GUIJ(each,jump)
            sleep(2)
            I_Type(each)
        
    print(register_file)
    
RegisterFile(b_register_file)
print('\n'+'* * * * * * * * * * * * * * * * * * * * ')
print(str(len(list))+ ' instructions have been executed.')
