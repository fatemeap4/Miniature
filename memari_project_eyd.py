#In the name of God
import re
import sys
print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * *\n"
      "*                                                   *\n"
      "*        Welcome to 'Miniature' assembeler          *\n"
      "*                                                   *\n"
      "* * * * * * * * * * * * * * * * * * * * * * * * * * *")

f = input("Please enter the name of your desired file to read from : ")
outputfile =input ("now please enter the name of file you want to write on : ")

lable = []
instruction = []
#c_instruction = instruction.copy()
field0r = [] #rd
field1r = [] #rs
field2r = [] #rt
field0i = [] #rt
field1i = [] #rs
offseti = [] #imm or offset
offsetj = [] #offset

file = open(f,"r")
cfile = open(f,"r")

def twos_complement(n, bits):
    s = bin(n & int("1" * bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)



def R_type (x,y,z):
    field0r.append(x)
    field1r.append(y)
    field2r.append(z)

def I_type(x,y,z):
    field0i.append(x)
    field1i.append(y)
    offseti.append(z)

def J_type(x):
    offsetj.append(x)

def f0r():
    for index, i in enumerate(field0r):
        j = int(i)
        b = format(j, 'b')
        if j == 1 or j==0:
            k = "000" + b
        elif j > 1 and j < 4:
            k = "00" + b
        elif j >= 4 and j < 8:
            k = "0" + b
        else:
            k = b
        field0r[index] = k


def f1r():
    for index, i in enumerate(field1r):
        m=0
        j = int(i)
        b = format(j, 'b')
        if j == 1 or j==0:
            m = "000" + b
        elif j > 1 and j < 4:
            m = "00" + b
        elif j >= 4 and j < 8:
            m = "0" + b
        else:
            m = b
        field1r[index] = m

def f2r():
    for index, i in enumerate(field2r):
        p = 0
        e = int(i)
        b = format(e, 'b')
        if e == 1 or e==0:
            p = "000" + b
        elif e > 1 and e < 4:
            p = "00" + b
        elif e >= 4 and e < 8:
            p = "0" + b
        else:
            p = b
        field2r[index] = p

def f0i():
    for index, i in enumerate(field0i):
        j = int(i)
        b = format(j, 'b')
        if j == 1 or j==0:
            k = "000" + b
        elif j > 1 and j < 4:
            k = "00" + b
        elif j >= 4 and j < 8:
            k = "0" + b
        else:
            k = b
        field0i[index] = k

def f1i():

    for index, i in enumerate(field1i):
        j = int(i)
        s = 0
        b = format(j, 'b')
        if j == 1 or j==0:
            s = "000" + b
        elif j > 1 and j < 4:
            s = "00" + b
        elif j >= 4 and j < 8:
            s = "0" + b
        else:
            s = b
        field1i[index] = s

def ofi(r):
    r = str(r)

    if r.startswith("-"):
        t = int(r)
        p = twos_complement(t,16)
        offseti[-1] = p


    if r.isdigit():
        if int(r) > ((2**15)+1):
            sys.exit(str(r) +"This offset is too large to be contained in 16 bits !")


        else:
            b = int(r)
            a = format(b, 'b')
            lenth = len(a)
            x = 16 - lenth
            p = str(0)
            for i in range(0, x - 1):
                p = '0' + p
            a = str(a)
            p = p + a
            offseti[-1] = p


    if r.isalpha():
        if r in lable:
            x = lable.index(r)
            b = int(x)
            a = format(b, 'b')
            lenth = len(a)
            j = 16 - lenth
            p = str(0)
            for i in range(0, j - 1):
                p = '0' + p
            a = str(a)
            p = p + a
            offseti[-1] = p
        else:
            sys.exit("label " + "'" + r + "'" + " is not defined :(")

def ofj(r) :

    if r in lable :

        x = lable.index(r)
        b = int(x)
        a = format(b, 'b')
        lenth = len(a)
        j = 16 - lenth
        p = str(0)
        for i in range(0, j - 1):
            p = '0' + p
        a = str(a)
        p = p + a
        offsetj[-1] =p

    else:
        sys.exit("label "+ "'"+r+"'" + " is not defined :(")



for line in cfile:
    l = line
    q = re.split("    ",l)
    lable.append(q[0])

for line in file:
    a = re.split("    |,",line)

#    lable.append(a[0])
    instruction.append(a[1])
    for n, i in enumerate(instruction):
        if i == "add":
            op = "0000"
            R_type(a[2],a[3],a[4])
            f0r()
            f1r()
            f2r()
            instruction[n] ="0000"+ str(op) + str(field1r[-1]) + str(field2r[-1]) + str(field0r[-1]) + "000000000000"
            #integer = int(instruction[n] ,2)
            #instruction[n] = integer

        elif i == "sub":
            op = "0001"
            R_type(a[2], a[3], a[4])
            f0r()
            f1r()
            f2r()
            instruction[n] = "0000"+str(op) + str(field1r[-1]) + str(field2r[-1]) + str(field0r[-1]) + "000000000000"
            #integer = int(instruction[n] ,2)
            #instruction[n] = integer

        elif i == "slt":
            op = "0010"
            R_type(a[2],a[3],a[4])
            f0r()
            f1r()
            f2r()
            instruction[n] = "0000"+str(op) + str(field1r[-1]) + str(field2r[-1]) + str(field0r[-1]) + "000000000000"
            #integer = int(instruction[n],2)
            #instruction[n] = integer

        elif i == "or":
            op = "0011"
            R_type(a[2],a[3],a[4])
            f0r()
            f1r()
            f2r()
            instruction[n] = "0000"+str(op) + str(field1r[-1]) + str(field2r[-1]) + str(field0r[-1]) + "000000000000"
            #integer = int(instruction[n], 2)
            #instruction[n] = integer

        elif i == "nand":
            op = "0100"
            R_type(a[2],a[3],a[4])
            f0r()
            f1r()
            f2r()
            instruction[n] = "0000"+ str(op) + str(field1r[-1]) + str(field2r[-1]) + str(field0r[-1]) + "000000000000"
            #integer = int(instruction[n], 2)
            #instruction[n] = integer

        elif i == "addi":
            op= "0101"
            I_type(a[2],a[3],a[4])
            f0i()
            f1i()
            ofi(a[4])
            instruction[n] = "0000" + str(op) + str(field1i[-1]) + str(field0i[-1]) + str(offseti[-1])
            #integer = int(instruction[n], 2)
            #instruction[n] = integer

        elif i == "slti":
            op = "0110"
            I_type(a[2], a[3], a[4])
            f0i()
            f1i()
            ofi(a[4])
            instruction[n] = "0000" + str(op) + str(field1i[-1]) + str(field0i[-1]) + str(offseti[-1])
            #integer = int(instruction[n], 2)
            #instruction[n] = integer

        elif i == "ori":
            op = "0111"
            I_type(a[2], a[3], a[4])
            f0i()
            f1i()
            ofi(a[4])
            instruction[n] = "0000" + str(op) + str(field1i[-1]) + str(field0i[-1]) + str(offseti[-1])
            #integer = int(instruction[n], 2)
            #instruction[n] = integer

        elif i == "lui":
            op = "1000"
            a[3] = "0000"
            I_type(a[2], a[3], a[4])
            f0i()
            f1i()
            ofi(a[4])
            instruction[n] = "0000" + str(op) + "0000" + str(field0i[-1]) + str(offseti[-1])
            #integer = int(instruction[n], 2)
            #instruction[n] = integer

        elif i == "lw":
            I_type(a[2],a[3],a[4])
            op = "1001"
            f0i()
            f1i()
            ofi(a[4])
            instruction[n] = "0000" + str(op) + str(field1i[-1]) +str(field0i[-1]) + str(offseti[-1])
            #integer = int(instruction[n], 2)
            #instruction[n] = integer

        elif i == "sw":
            op = "1010"
            I_type(a[2], a[3], a[4])
            f0i()
            f1i()
            ofi(a[4])
            instruction[n] = "0000" + str(op) + str(field1i[-1]) + str(field0i[-1]) + str(offseti[-1])
            #integer = int(instruction[n], 2)
            #instruction[n] = integer

        elif i == "beq":
            op = "1011"
            I_type(a[2], a[3], a[4])
            f0i()
            f1i()
            ofi(a[4])
            instruction[n] = "0000" + str(op) + str(field1i[-1]) + str(field0i[-1]) + str(offseti[-1])
            #integer = int(instruction[n], 2)
            #instruction[n] = integer

        elif i == "jalr":
            op = "1100"
            a[4] = "0000"
            I_type(a[2], a[3], a[4])
            f0i()
            f1i()
            ofi(a[4])
            instruction[n] = "0000" + str(op) + str(field1i[-1]) + str(field0i[-1]) +"0000000000000000"
            #integer = int(instruction[n], 2)
            #instruction[n] = integer

        elif i == "j":
            op = "1101"
            J_type(a[2])
            ofj(a[2])
            instruction[n] = "0000" + str(op) + "00000000" + str(offsetj[-1])
            #integer = int(instruction[n], 2)
            #instruction[n] = integer

        elif i == "halt":
            op = "1110"
            instruction[n] = "0000" + str(op) + "00000000" + "0000000000000000"
            #integer = int(instruction[n], 2)
            #instruction[n] = integer

        elif i == ".fill":
            if a[2].startswith("-"):
                #a[2].replace("-","")
                instruction[n] = int(a[2])
            if a[2].isdigit():
                instruction[n] = int(a[2])
            elif a[2].isalpha():
                if a[2] in lable:
                    x = lable.index(a[2])
                    x = int(x)
                    instruction[n] = x


print(instruction)


for index , each in enumerate(instruction):
    each = str(each)
    if each.isalpha():
        sys.exit("This instruction is not defined :(")


f = open(outputfile,"w")
for index, each in enumerate(instruction):
    #f.write(str(index))
    #f.write(": ")
    f.write(str(each))
    f.write("\n")

f.close()

#finished)
