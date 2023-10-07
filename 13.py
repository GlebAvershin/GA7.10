from ipaddress import *
net = ip_network('192.168.32.160/255.255.255.240')
k = 0
for ip in net:
    if bin(int(ip)).count('1') % 2 == 0:
        k += 1
print(k)

k = 0
for i in range(1, 1000):
    if i % 46 == 0:
        k += 1
print(k)