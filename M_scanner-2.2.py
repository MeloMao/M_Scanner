# -*- coding: UTF-8 -*-

import socket
import time

openPort = []


def connScan(Host, Port):
    try:
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connSkt.connect((Host, Port))
        print('%d端口开放' % Port)
        connSkt.close()
        openPort.append(Port)
    except:
        print('%d端口关闭' % Port)

def portScan(Host, Ports, speed):
    try:
        IP = socket.gethostbyname(Host)
    except:
        print("无法解析的主机名" % Host)
        return
    print('\n扫描的主机IP是: ' + IP)
    socket.setdefaulttimeout(speed)
    for Port in Ports:
        print('正在扫描的端口：' + str(Port))
        time.sleep(speed)
        connScan(Host, int(Port))
    print('该主机开放的端口有：' + str(openPort))


def main():
    Host = input("请输入要扫描的目标主机:")
    chose1 = int(input("是否扫描默认端口?是请输入1，需要自定义端口请输入2，自定义扫描某范围内所有端口请输入3:"))
    chose2 = int(input("是否需要自定义扫描速率（默认为0.5秒/次）？不需要请输入1，需要输入2："))
    if (chose2 == 2):
        speed = float(input("请输入扫描速率（秒/次）："))
    else:
        speed = 0.5
    if (chose1 == 2):
        c = input("请输入需要扫描的端口（用英文逗号隔开）：")
        Ports = eval(c)
        print("正在扫描自定义端口...")
        portScan(Host, Ports, speed)
    elif (chose1 == 3):
        d = int(input("请输入范围扫描起始端口："))
        e = int(input("请输入范围扫描结束端口："))
        Ports = []
        for i in range(d, e + 1):
            f.append(i)
        portScan(Host, Ports, speed)
    else:
        print("正在扫描默认端口...")
        portScan(Host, [21,22,23,25,53,67,68,69,80,110,139,143,161,389,443,445,1433,1521,2049,2181,3389,3690,5432,5632,5900,7001,7002,8080,9090,27017], speed)

main()
