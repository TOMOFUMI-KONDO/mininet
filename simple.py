#!usr/bin/python

from mininet.net import Mininet
from mininet.cli import CLI

net = Mininet()
c0 = net.addController()
h1 = net.addHost('h1', ip='192.168.1.1/24')
s1 = net.addSwitch('s1')
h2 = net.addHost('h2', ip='192.168.1.2/24')

net.addLink(h1, s1)
net.addLink(h2, s1)

net.start()
net.pingAll()
CLI(net)
net.stop()
