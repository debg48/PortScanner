#!/usr/bin/python3

from socket import *
import optparse
from threading import *

def connScan(tgHost,tgPort):
        try:
                sock=socket(AF_INET,SOCK_STREAM)
                sock.connect((tgHost,tgPort))
                print('[+]%d/tcp Open'%tgPort)
        except:
                print('[-]%d/tcp Closed'%tgPort)
        finally:
                sock.close()

def portscan(tgHost,tgPort):
        try:
                tgIP=gethostbyname(tgHost)
        except:
                print('[!] Unkonown Host %s'%tgHost)
        try:
                tgName=gethostbyaddr(tgIP)
                print('[+] Scan Result :' + tgName[0])
        except:
                print('[+]Scan Reults for:' + tgIP)
        setdefaulttimeout(0)
        for port in tgPort:
                t=Thread(target=connScan,args=(tgHost,int(port)))
                t.start()

def main():
        parser=optparse.OptionParser("Usage of Program :" + " -H <target host> -p <target port> ")
        parser.add_option('-H',dest='tgHost',type='string',help='specify target host')
        parser.add_option('-p',dest='tgPort',type='string',help='specify target port seperated by comma')
        (options,args)=parser.parse_args()
        tgHost=options.tgHost
        tgPort=str(options.tgPort).split(',')

        if (tgHost==None) | (tgPort[0]==None):
                print (parser.usage)
                exit(0)

        portscan(tgHost,tgPort)

if __name__=='__main__':
        main()
