from ntpath import join
from posixpath import split
import sys  
class ip_founder:
    class_name=""
    class_type=""
    Apart=int(input("enter part A of the ip\t"))
    Bpart=int(input("enter part B of the ip\t"))
    Cpart=int(input("enter part C of the ip\t"))
    Dpart=int(input("enter part D of the ip\t"))    
    ip=[str(Apart),str(Bpart),str(Cpart),str(Dpart)]
    ip_add=(".").join(ip)
    if (Apart<=127):
        class_name='A'
    elif (Apart>=128 and Apart<=191) and (Bpart>255):
        class_name='B'
    elif (Apart>=192 and Apart<=223) and (Bpart>255) and (Cpart>255) and (Dpart>255):
        class_name='C'
    elif (Apart>=224 and Apart<293) and (Bpart>255) and (Cpart>255) and (Dpart>255):
        class_name='D'
    else:
        print("i don't know what the hell is this")
    if class_name=='A' and (Apart==10) and (Bpart==0) and (Cpart==0) and (Dpart==0):
        class_type="private"
        print (class_type)
    elif (class_name=='B') and (Apart==172) and (Bpart>=16 and Bpart<=31) and (Cpart<=255) and (Dpart<=255):
        class_type="private"
    elif (class_name=='C') and (Apart==192) and(Bpart==168) and(Cpart<=255) and(Dpart<=255):
        class_type="private"
    else:
        class_type="public"
    print(ip_add)
    print(class_type)
    print(class_name)