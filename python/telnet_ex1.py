import telnetlib
##from scapy.all import *

##########################   R1    ############################
###Telnet
var=telnetlib.Telnet('10.0.0.1')
##print var
a=var.read_until('Password:')
##print a
var.write('321\n')
c=var.read_until('R1>')
##print c
var.write('enable\n')

d=var.read_until('Password:')
##print d
var.write('123\n')
e=var.read_until('R1#')
##print e

## basic config

var.write('conf t\n')
var.write('int f1/0\n')
var.write('ip address 20.0.0.1 255.0.0.0\n')
var.write('no sh\n')
var.write('exit\n')

##Rip config
var.write('router rip\n')
var.write('ver 2\n')
var.write('network 20.0.0.0\n')
var.write('network 10.0.0.0\n')
var.write('end\n')
y=var.read_until('R1#')
##print y
## show routing table
var.write('show ip route\n')
y=var.read_until('R1#')
##print y

#########################     R2 ###################

###Telnet
var=telnetlib.Telnet('10.0.0.2')
##print var
a=var.read_until('Password:')
##print a
var.write('321\n')
c=var.read_until('R2>')
##print c
var.write('enable\n')

d=var.read_until('Password:')
##print d
var.write('123\n')
e=var.read_until('R2#')
##print e

## basic config

var.write('conf t\n')
var.write('int f1/0\n')
var.write('ip address 20.0.0.2 255.0.0.0\n')
var.write('no sh\n')
var.write('exit\n')

##Rip config
var.write('router rip\n')
var.write('ver 2\n')
var.write('network 20.0.0.0\n')
var.write('network 10.0.0.0\n')
var.write('end\n')
y=var.read_until('R2#')
##print y
## show routing table
var.write('show ip route\n')
y=var.read_until('R2#')
##print y
############ Ping from R2 to R1

var.write('ping 20.0.0.1\n')
y=var.read_until('R2#')
print y

##ip = IP()
##print ip.show()
##
##ip = IP()
##ip.src = '10.0.0.10'
##ip.dst = '224.0.0.9'
##ip.proto = 17
##print "From RIP_PKT Funtion: Got ip address"
##print ip.show()
##u=UDP(sport=520,dport=520)
##print u.show()
##RH = RIP(cmd='resp',version=2)
##print ls(RH)
##pkt=RIPEntry()
##pkt.addr = '29.9.9.3'
##pkt.mask ='255.0.0.0'
##pkt.nextHop = '1.1.1.1'
##pkt.metric = int(7)
##
##pk=RIPEntry()
##pk.addr = '29.9.9.4'
##pk.mask ='255.0.0.0'
##pk.nextHop = '2.2.2.2'
##pk.metric = int(7)
##print pkt.show()
##hpkt = ip/u/RH/pkt/pk
##print hpkt.show()
##
##
##send(ip/u/RH/pkt/pk)
##send(ip/u/RH/pkt/pk)
##send(hpkt)
##send(hpkt)
