#!usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel


class SingleSwitchTopo(Topo):
  def build(self, n=2):
    switch = self.addSwitch('s1')
    for h in range(n):
      host = self.addHost('h%s' % (h + 1))
      self.addLink(host, switch)


def simpleTest():
  topo = SingleSwitchTopo(n=3)
  net = Mininet(topo)
  net.start()

  print '===Dumping node info'
  dumpNodeConnections(net.hosts)
  print '==='

  print '===Testing connectivity'
  net.pingAll()
  print '==='

  print '===Stop devices'
  net.stop()
  print '==='


if __name__ == '__main__':
  setLogLevel('info')
  simpleTest()
