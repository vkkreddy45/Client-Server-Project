from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller, RemoteController
from mininet.topo import Topo
from mininet.log import setLogLevel
from mininet.cli import CLI

setLogLevel('info')

c0 = Controller('c0',port=6633)
c1 = Controller('c1',port=6634)
c2 = Controller('c2',port=6635)
c3 = Controller('c3',port=6636)
c4 = Controller('c4',port=6637)
c5 = Controller('c5',port=6638)
c6 = Controller('c6',port=6639)
c7 = Controller('c7',port=6631)
c8 = Controller('c8',port=6632)
c9 = Controller('c9',port=6630)

cmap={'s0':c0,'s1':c1,'s2':c2,'s3':c3,'s4':c4,'s5':c5,'s6':c6,'s7':c7,'s8':c8,'s9':c9}

class MultiSwitch(OVSSwitch):
	def start(self, controllers):
		return OVSSwitch.start(self, [cmap[self.name]])

class MultipleSwitch(Topo):
	"simple topology with 10 switches & 10 hosts"
	def build(self,n,**_kwargs):
		"adding 10 hosts"
		h0=self.addHost('h0',mac="00:00:00:00:00:01")
		h1=self.addHost('h1',mac="00:00:00:00:00:02")
		h2=self.addHost('h2',mac="00:00:00:00:00:03")
		h3=self.addHost('h3',mac="00:00:00:00:00:04")
		h4=self.addHost('h4',mac="00:00:00:00:00:05")
		h5=self.addHost('h5',mac="00:00:00:00:00:06")
		h6=self.addHost('h6',mac="00:00:00:00:00:07")
		h7=self.addHost('h7',mac="00:00:00:00:00:08")
		h8=self.addHost('h8',mac="00:00:00:00:00:09")
		h9=self.addHost('h9',mac="00:00:00:00:00:10")
		"adding 10 switches"
		s0 = self.addSwitch('s0')
		s1 = self.addSwitch('s1')
		s2 = self.addSwitch('s2')
		s3 = self.addSwitch('s3')
		s4 = self.addSwitch('s4')
		s5 = self.addSwitch('s5')
		s6 = self.addSwitch('s6')
		s7 = self.addSwitch('s7')
		s8 = self.addSwitch('s8')
		s9 = self.addSwitch('s9')
		switches = [s0,s1,s2,s3,s4,s5,s6,s7,s8,s9]
		hosts = [h0,h1,h2,h3,h4,h5,h6,h7,h8,h9]
		for switch,host in zip(switches,hosts):
			self.addLink(switch,host)
		"connecting the hosts"
		self.addLink(s0,s1)
		self.addLink(s0,s2)
		self.addLink(s0,s8)
		self.addLink(s1,s3)
		self.addLink(s1,s9)
		self.addLink(s2,s4)
		self.addLink(s2,s5)
		self.addLink(s2,s7)
		self.addLink(s5,s6)
topo = MultipleSwitch(n=10)
net = Mininet(topo=topo, switch=MultiSwitch, build=False, waitConnected=True)
for c in [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9]:
	net.addController(c)
net.build()
net.start()
CLI(net)
net.stop()
