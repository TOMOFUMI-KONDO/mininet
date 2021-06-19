#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, Host, Node, OVSKernelSwitch
from mininet.link import TCLink
from mininet.log import setLogLevel, info
from mininet.cli import CLI


def my_net_work():
  net = Mininet()

  info('*** Adding controller ***')
  c0 = net.addController(name='c0', controller=Controller, protocol='tcp', port=6633)

  info('\n*** Adding switches ***')
  s1 = net.addSwitch('s1', cls=OVSKernelSwitch, failMode='standalone', stp='True')
  s2 = net.addSwitch('s2', cls=OVSKernelSwitch, failMode='standalone', stp='True')
  s3 = net.addSwitch('s3', cls=OVSKernelSwitch, failMode='standalone', stp='True')

  info('\n*** Adding hosts ***')
  h1 = net.addHost('h1', ip='10.10.10.1/24')
  h2 = net.addHost('h2', ip='10.10.10.2/24')
  h3 = net.addHost('h3', ip='10.10.10.3/24')

  info('\n*** Adding links ***\n')
  type1 = {'cls': TCLink, 'bw': 100}
  type2 = {'cls': TCLink, 'bw': 1000, 'delay': '1000ms'}
  net.addLink(h1, s1, **type1)
  net.addLink(h2, s1, **type1)
  net.addLink(h3, s3, **type2)
  net.addLink(s1, s2, **type1)
  net.addLink(s2, s3, **type1)
  net.addLink(s1, s3, **type2)

  net.start()
  CLI(net)
  net.stop()


if __name__ == '__main__':
  setLogLevel('info')
  my_net_work()
