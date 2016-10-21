#! /usr/local/bin/python
# -*- coding: utf-8 -*-

import libvirt
import xml.etree.ElementTree

#本机虚拟化的链接
hostUri = 'qemu+ssh://shiyanlou@localhost/system'


#根据用户需求配置虚拟机名字、CPU个数、RAM空间大小、磁盘所在路径
def configVM(XMLString, VMName, cpuNum, ramNum, diskPosition):
    if XMLString == None:
        return None
    
    #配置虚拟机名    
    XMLString = XMLString.replace("<name>", "<name>" + VMName)
    
    #配置cpu个数
    XMLString = XMLString.replace("<vcpu>", "<vcpu>" + str(cpuNum))
    
    #配置内存大小
    XMLString = XMLString.replace("<memory>", "<memory>" + str(ramNum))
    
    #配置磁盘所在位置
    XMLString = XMLString.replace("<source file='", "<source file='" + diskPosition)
    
    #返回配置数据
    return XMLString
    
#创建并启动虚拟机
def createVM(VMName, cpuNum, ramNum, diskPosition):
    
    #打开本机虚拟化链接
    host = libvirt.open(hostUri)
    
    #打开虚拟机配置文件
    fd = open('/home/shiyanlou/Code/shiyanlou_cs354/virtscripts/louvm1.xml')
    
    #读取虚拟机配置数据    
    domainXMLString = fd.read()

    #配置虚拟机
    domainXMLString = configVM(domainXMLString, VMName, cpuNum, ramNum, diskPosition)    
    
    #创建并启动虚拟机
    domain = host.createXML(domainXMLString, 0)
    
    # 查看虚拟机状态
    if domain.state()[0] == libvirt.VIR_DOMAIN_RUNNING:
        return True

    return False
    
#强制关机虚拟机（同时也删除虚拟机）
def  shutdownVM(vmname):
    #打开本机虚拟化链接
    host = libvirt.open(hostUri)

    #根据虚拟机名字查找虚拟机
    domain = host.lookupByName(vmname)

    #关闭并删除虚拟机
    domain.destroy()

    return True

#启动虚拟机
def startVM(vmname):
    #打开本机虚拟化链接
    host = libvirt.open(hostUri)

    #根据虚拟机名字查找虚拟机
    domain = host.lookupByName(vmname)

    #启动虚拟机
    domain.create()
    
    if domain.state()[0] == libvirt.VIR_DOMAIN_RUNNING:
        return True

    return False
    
#获取VNC端口号
def getVNCPort(vmname):
    #打开本机虚拟化链接
    host = libvirt.open(hostUri)

    #根据虚拟机名字查找虚拟机
    domain = host.lookupByName(vmname)

    #获取虚拟机XML字符串
    domainXMLString = domain.XMLDesc()

#    from StringIO import StringIO 

#    file = StringIO(domainXMLString)
     
#    doc = xml.etree.ElementTree.parse(file)

    #将字符串格式化为XML文件流
    root = xml.etree.ElementTree.fromstring(domainXMLString)
    
    #查找graphics节点并返回端口号
    nodeFind = root.getiterator("graphics")
    for node in nodeFind:
        for key,value in node.items(): 
            if key == 'port':
                return value
    return -1
    
#重启虚拟机
def  rebootVM(vmname):
    #打开本机虚拟化链接
    host = libvirt.open(hostUri)

    #根据虚拟机名字查找虚拟机
    domain = host.lookupByName(vmname)

    #重启虚拟机
    domain.reboot()
    
    #判断虚拟机是否重启成功
    if domain.state()[0] == libvirt.VIR_DOMAIN_RUNNING:
        return True
    
    return False

#删除虚拟机    
def deleteVM(vmname):
    #打开本机虚拟化链接
    host = libvirt.open(hostUri)

    #根据虚拟机名字查找虚拟机
    domain = host.lookupByName(vmname)

    删除虚拟机
    domain.destroy()
#    domain.undefine()
    
    return True
    
##print createVM("vm1", 1, 102400, "/home/shiyanlou/louvm1.qcow2")
#print getVNCPort('vm1')





