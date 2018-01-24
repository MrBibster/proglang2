import re
log = open('access.log')
ip_list = []
line = log.readline()
while (line):
    temp_ip = re.findall(r'(\d*\.\d*\.\d*\.\d*).*', line)
    current_ip = temp_ip[0]
    if (current_ip != '') and (current_ip not in ip_list):
        regex = re.compile('\d*\.\d*\.\d*')
        ip_subnet = re.findall(regex, current_ip)
        for n in range (len(ip_list)):
            current_subnet = re.findall(regex, ip_list[n])
            if (ip_subnet == current_subnet):
                ip_list.insert((n+1),current_ip)
                break
        if (current_ip not in ip_list):
            ip_list.append(current_ip)
    line = log.readline()
for i in range (len(ip_list)):
    print(ip_list[i])


