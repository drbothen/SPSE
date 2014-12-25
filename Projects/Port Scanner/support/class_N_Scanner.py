from scapy.all import *
import re

class Netscanner:
    'python port scanner'
    
    def __init__(self):
        pass
    
    def qDiscovery(self, subnet):
        ARPipregx = re.compile(ur'\bpsrc=((25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3})\b')
        ARPmacregx = re.compile(ur'\bhwsrc=([0-9a-fA-F]{2}:??[0-9a-fA-F]{2}:??[0-9a-fA-F]{2}:??[0-9a-fA-F]{2}:??[0-9a-fA-F]{2}:??[0-9a-fA-F]{2})\b')        
        self.qDdict = {}
        answeredARP, unansweredARP=srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=subnet),timeout=2)
        for ARPResponce in answeredARP:
            ip = re.findall(ARPipregx, str(list(ARPResponce)))
            mac = re.findall(ARPmacregx, str(list(ARPResponce)))
            self.qDdict[ip[0][0]] = mac[0]
            
        
        
        
    #def displayparms(self):
    #    print "IP is set to: "
    #    print "Port(s) to scan are: "





test = Netscanner()

test.qDiscovery('192.168.58.0/24')
print test.qDdict
