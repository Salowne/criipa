#!usr/bin/evn python3
# encoding: utf-8

__author__ = 'Zwdeff'
__version__ = '1.0'
__copyright__ = 'Copyright (c) 2017 @nZwdeff\n'# All Rights Reserved.

"""
Github https://github.com/Xdwnff-04x/criipa
This script generates custom ips numbers.
To generate a specific IP range defined in
Maximum number where it should generate .. To lock an octet
Repeat the number at the maximum number.
The generated IPs will be saved in the created file
At the beginning of the program.
"""

from sys import *
from time import *

if version_info.major < 3:
   print ('\033[91mErro: Program made for python3.\033[m')
   sleep(2)
   exit()

n0 = '\033[90m'
n1 = '\033[91m'
n2 = '\033[92m'
n3 = '\033[93m'
n4 = '\033[94m'
n5 = '\033[95m'
n6 = '\033[96m'
n7 = '\033[96m'
__Banner__ = '\n Generate custom IPs Numbers _'

__main__ = '\033[92m 1) =\033[32m xxx.xxx.xxx.xxx\n'\
          +'\033[92m 0) =\033[32m exit\n'

print (n2+' %s\033[m' %(__Banner__))
print (n2+'\n Author:\033[32m %s\n\033[92m Version:\033[32m %s\n\033[m'\
%(__author__,__version__))

def case():
  try:
     print (n2+'%s\033[m' %(__main__))
     
     w = input(n2+' :: _ \033[m')
     while w != '01' or w != '1'or w != '00' or w != '0':
        if w == '01' or w == '1' or w == '00' or w == '0':
           if w == '01' or w == '1':
              def gerator(s1,s2,s3,s4,o1,o2,o3,o4,arq,pho):
                  for a in range(s1, o1+1):
                   for b in range(s2, o2+1):
                    for c in range(s3, o3+1):
                     for d in range(s4, o4+1):
                         arq.write(str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d)+str(pho)+'\n')
                         print (n2+' '+str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d)+str(pho)\
                         +'\033[m')
                         if a == o1 and b == o2 and c == o3 and d == o4:
                            print (n2+'\n\033[32m Completed. IPs saved in file %s\033[m'\
                            %(arq.name))
                            sleep(2)
                            arq.close()
                            case()
              print (n2+'\n Create a file .. \033[m')
              sleep(2)
              arq = open(input(n2+' Name for file :: _ \033[m')+ '.txt', 'w')
              def retu(s1,s2,s3,s4,arq):
                  o1 = input(n2+' Maximum octet number 1. 0/255 :: _ \033[m')
                  try:
                     o1 = int(o1)
                     if o1 < s1:
                        print (n1+'Error: The maximum number must be greater or'\
                              +' The octet.\033[m')
                        retu(s1,s2,s3,s4,arq)
                  except Exception:
                     print (n1+' Error: Use only integer numbers.\033[m')
                     retu(s1,s2,s3,s4,arq)
                  o2 = input(n2+' Maximum octet number 2. 0/255 :: _ \033[m')
                  try:
                     o2 = int(o2)
                     if o2 < s2:
                        print (n1+'Error: The maximum number must be greater or'\
                              +' The octet.\033[m')
                        retu(s1,s2,s3,s4,arq)
                  except Exception:
                     print (n1+' Error: Use only integer numbers.\033[m')
                     retu(s1,s2,s3,s4,arq)
                  o3 = input(n2+' Maximum octet number 3. 0/255 :: _ \033[m')
                  try:
                     o3 = int(o3)
                     if o3 < s3:
                        print (n1+'Error: The maximum number must be greater or'\
                              +' The octet.\033[m')
                        retu(s1,s2,s3,s4,arq)
                  except Exception:
                     print (n1+' Error: Use only integer numbers.\033[m')
                     retu(s1,s2,s3,s4,arq)
                  o4 = input(n2+' Maximum octet number 4. 0/255 :: _ \033[m')
                  try:
                     o4 = int(o4)
                     if o4 < s4:
                        print (n1+'Error: The maximum number must be greater or'\
                              +' The octet.\033[m')
                        retu(s1,s2,s3,s4,arq)
                  except Exception:
                     print (n1+' Error: Use only integer numbers.\033[m')
                     retu(s1,s2,s3,s4,arq)
                  pho = input(n2+' Port for IPs :80/:8080 :: _ \033[m')
                        
                  print ('\n\033[32m Generating IPs in file %s .. \n\033[m' %(arq.name))
                  sleep(2)
                  gerator(s1,s2,s3,s4,o1,o2,o3,o4,arq,pho)
                  
              def defe(arq):
                  s1 = input(n2+' IP octet 1. 1/255 :: _ \033[m')
                  try:
                     s1 = int(s1)
                     if s1 > 255:
                        print (n1+' Error: The octet must be less than or equal to 255.')
                  except Exception:
                    print (n1+' Error: Use only integer numbers.\033[m')
                    defe(arq)
                  s2 = input(n2+' IP octet 2. 0/255 :: _ \033[m')
                  try:
                     s2 = int(s2)
                     if s2 > 255:
                        print (n1+' Error: The octet must be less than or equal to 255.')
                        defe(arq)
                  except Exception:
                     print (n1+' Error: Use only integer numbers.\033[m')
                     defe(arq)
                  s3 = input(n2+' IP octet 3. 0/255 :: _ \033[m')
                  try:
                     s3 = int(s3)
                     if s3 > 255:
                        print (n1+' Error: The octet must be less than or equal to 255.')
                        defe(arq)
                  except Exception:
                     print (n1+' Error: Use only integer numbers.\033[m')
                     defe(arq)
                  s4 = input(n2+' IP octet 4. 0/255 :: _ \033[m')
                  try:
                     s4 = int(s4)
                     if s4 > 255:
                        print (n1+' Error: The octet must be less than or equal to 255.')
                        defe(arq)
                  except Exception:
                     print (n1+' Error: Use only integer numbers.\033[m')
                     defe(arq)
                  retu(s1,s2,s3,s4,arq)
                  
              if __name__ == '__main__':
                 defe(arq)
           if w == '0' or w == '00':
              print (n1+' Going out ..\033[m')
              sleep(2)
              exit()
        else:
           w = input(n2+' :: _ \033[m')
  except KeyboardInterrupt:
     print (n1+'\n Going out ..\033[m')
     sleep(2)
     exit()
if __name__ == '__main__':
   case()