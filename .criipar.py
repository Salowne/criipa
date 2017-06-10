#!usr/bin/evn python3
# encoding: utf-8

__author__ = 'Zwdeff'
__version__ = '0.1'
__copyright__ = 'Copyright (c) 2017 @nZwdeff\n'# All Rights Reserved.

# Github https://github.com/Xdwnff-04x/criipa
# este script gera numeros ips customizados.
# para gerar uma escala de ip especifica defina no
# numero maximo aonde ele tem que gerar .. Para travar um octeto
# Repita o numero no numero maximo.

from os import *
from sys import *
from time import *

v = version_info.major
H = strftime('%d/%m/%Y %H:%M:%S')
print ('Conectando .. via python%s /%s' % (v,H))

if version_info.major < 3:
   print ('\033[91mErro: Progama feito para python3.\033[m')
   sleep(2)
   exit()
sleep(1)

n0 = '\033[90m'
n1 = '\033[91m'
n2 = '\033[92m'
n3 = '\033[93m'
n4 = '\033[94m'
n5 = '\033[95m'
n6 = '\033[96m'
n7 = '\033[96m'

__main__ = '\n 1) = Custom xxx.xxx.xxx.xxx'\
          +'\n 0) = Sair\n\n'
          
# 01 = True.
def case():
  try:
     print ('\033[96m%s\033[m' %(__main__))
     w = input(n6+' :: _\033[92m'+' \033[m')
     
     while w != '01' or w != '1'or w != '00' or w != '0':
        if w == '01' or w == '1' or w == '00' or w == '0':
           if w == '01' or w == '1':
              def ger():
                  n = input(n2+' Gerar IPs xxx.xxx.xxx.xxx [y/n]\033[96m :: _\033[92m'\
                  +' \033[m')
                  if n == 'y' or n == 'Y':
                     ar = input(n2+' De um enter para criar um arquivo .. \033[m')
                     aq = open(input(n2+' Nome para o arquivo\033[96m :: _\033[92m'\
                                    +' \033[m')+ '.txt', 'w')
                     def df():
                         s1 = input(n2+' octeto 1 do IP 1/255\033[96m :: _\033[92m'+' \033[m')
                         try:
                            s1 = int(s1)
                            if s1 > 255:
                               print (n1+' Erro: o octeto deve ser menor ou ingual a 255.')
                         except Exception:
                           print (n1+' Erro: utilize somente numeros inteiros.\033[m')
                           df()
                         s2 = input(n2+' octeto 2 do IP 0/255\033[96m :: _\033[92m'+' \033[m')
                         try:
                            s2 = int(s2)
                            if s2 > 255:
                               print (n1+' Erro: o octeto deve ser menor ou ingual a 255.')
                               df()
                         except Exception:
                            print (n1+' Erro: utilize somente numeros inteiros.\033[m')
                            df()
                         s3 = input(n2+' octeto 3 do IP 0/255\033[96m :: _\033[92m'+' \033[m')
                         try:
                            s3 = int(s3)
                            if s3 > 255:
                               print (n1+' Erro: o octeto deve ser menor ou ingual a 255.')
                               df()
                         except Exception:
                            print (n1+' Erro: utilize somente numeros inteiros.\033[m')
                            df()
                         s4 = input(n2+' octeto 4 do IP 0/255\033[96m :: _\033[92m'+' \033[m')
                         try:
                            s4 = int(s4)
                            if s4 > 255:
                               print (n1+' Erro: o octeto deve ser menor ou ingual a 255.')
                               df()
                         except Exception:
                            print (n1+' Erro: utilize somente numeros inteiros.\033[m')
                            df()
                         def axx():
                          o1 = input(n2+' Numero maximo para octeto 1. 0/255\033[96m'\
                                   +' :: _\033[92m'+' \033[m')
                          try:
                             o1 = int(o1)
                             if o1 < s1:
                                print (n1+'Erro: o numero maximo deve ser maior ou'\
                                      +' ingual ao octeto.\033[m')
                                axx()
                          except Exception:
                             print (n1+' Erro: utilize somente numeros inteiros.\033[m')
                             df()
                          o2 = input(n2+' Numero maximo para octeto 2. 0/255\033[96m'\
                                   +' :: _\033[92m'+' \033[m')
                          try:
                             o2 = int(o2)
                             if o2 < s2:
                                print (n1+'Erro: o numero maximo deve ser maior ou'\
                                      +' ingual ao octeto.\033[m')
                                axx()
                          except Exception:
                             print (n1+' Erro: utilize somente numeros inteiros.\033[m')
                             df()
                          o3 = input(n2+' Numero maximo para octeto 3. 0/255\033[96m'\
                                   +' :: _\033[92m'+' \033[m')
                          try:
                             o3 = int(o3)
                             if o3 < s3:
                                print (n1+'Erro: o numero maximo deve ser maior ou'\
                                      +' ingual ao octeto.\033[m')
                                axx()
                          except Exception:
                             print (n1+' Erro: utilize somente numeros inteiros.\033[m')
                             df()
                          o4 = input(n2+' Numero maximo para octeto 4. 0/255\033[96m'\
                                   +' :: _\033[92m'+' \033[m')
                          try:
                             o4 = int(o4)
                             if o4 < s4:
                                print (n1+'Erro: o numero maximo deve ser maior ou'\
                                      +' ingual ao octeto.\033[m')
                                axx()
                          except Exception:
                             print (n1+' Erro: utilize somente numeros inteiros.\033[m')
                             df()
                          pho = input(n2+' Porta para os IPs :80/:8080\033[96m'\
                                     +' :: _\033[92m'+' \033[m')
                          print (n6+' Gerando IPs no arquivo %s .. \n\033[m' %(aq.name))
                          sleep(2)
                          for a in range(s1, o1+1):
                           for b in range(s2, o2+1):
                            for c in range(s3, o3+1):
                             for d in range(s4, o4+1):
                               aq.write(str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d)+str(pho)+'\n')
                               print (n2+' '+str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d)+str(pho)\
                               +'\033[m')
                               if a == o1 and b == o2 and c == o3 and d == o4:
                                  aq.close()
                                  ger()
                         axx()
                         
                     df()
                  if n == 'n' or n == 'N':
                     case()
              ger()
           if w == '0' or w == '00':
              print (n1+' Saindo ..\033[m')
              sleep(2)
              exit()
        else:
           w = input(n6+' :: _\033[92m'+' \033[m')
  except KeyboardInterrupt:
     print (n1+'\n Saindo ..\033[m')
     sleep(2)
     exit()
if __name__ == '__main__':
  case()