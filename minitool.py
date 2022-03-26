import os
author="weird"
print("""
                        .▄▄ · ▄▄▄▄▄ ▄▄▄·  ▐ ▄ ▄▄▌  ▄▄▄ . ▄· ▄▌
                        ▐█ ▀. •██  ▐█ ▀█ •█▌▐███•  ▀▄.▀·▐█▪██▌
                        ▄▀▀▀█▄ ▐█.▪▄█▀▀█ ▐█▐▐▌██▪  ▐▀▀▪▄▐█▌▐█▪
                        ▐█▄▪▐█ ▐█▌·▐█ ▪▐▌██▐█▌▐█▌▐▌▐█▄▄▌▐█▀·.
                         ▀▀▀▀  ▀▀▀  ▀  ▀ ▀▀ █▪.▀▀▀  ▀▀▀   ▀ •
                ╔══════════════════════════════════════════════╗
                ║       Welcome to Stanley Tool                ║
                ║ - - -   discord weird#1337             - - - ║
                ╚══════════════════════════════════════════════╝
                    ╔══════════════════════════════════════╗
                    ║https://github.com/weird1337/mini-tool
                    ╚══════════════════════════════════════╝
                        
________________________
1- Light port scan with nmap
2- Get service version information with nmap
3- Check dbs with sqlmap
4- sqlmap sabotage 1
5- find wpscan username
6- wpscan brute
________________________
""")
at = input("Please Choose One Of The Options  -> ")
if at == "1" :
   at2 = input("enter ip or link => ") 
   os.system("nmap " + at2)
if at == "2" : 
   at3 = input("vulnerable ip => ")
   os.system("sudo nmap -sS -sV " + at3)
if at == "3":
   at4 = input("vulnerable url => ")
   os.system("sqlmap -u "+at4 + "--dbs")
if at == "4" :
   at5 = input("vulnerable url =>")
   os.system("sqlmap -u "+at5 + "--tamper=space2comment,between,space2plus -v 2 --hex --random-agent --skip-waf --risk=3 --level=3 --dbs")
if at == "5" :
   at6 = input("target wordpress")
   os.system("wpscan --url "+at6 +"-enumerate u ")
if at =="6" :
   at7 = input ("target wordpress")
   at8 = input ("wordlist yolu")
   os.system("wpscan --url "+at7 +"-enumerate u ")
else : 
  print("something went wrong ")
