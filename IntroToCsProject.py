from socket import * 

#if __name__ == '__main__':

common_ports = {
 
	'21': 'FTP',
	'22': 'SSH',
	'23': 'TELNET',
	'25': 'SMTP',
	'53': 'DNS',
	'69': 'TFTP',
	'80': 'HTTP',
	'109': 'POP2',
	'110': 'POP3',
	'123': 'NTP',
	'137': 'NETBIOS-NS',
	'138': 'NETBIOS-DGM',
	'139': 'NETBIOS-SSN',
	'143': 'IMAP',
	'156': 'SQL-SERVER',
	'389': 'LDAP',
	'443': 'HTTPS',
	'546': 'DHCP-CLIENT',
	'547': 'DHCP-SERVER',
	'995': 'POP3-SSL',
	'993': 'IMAP-SSL',
	'2086': 'WHM/CPANEL',
	'2087': 'WHM/CPANEL',
	'2082': 'CPANEL',
	'2083': 'CPANEL',
	'3306': 'MYSQL',
	'8443': 'PLESK',
	'10000': 'VIRTUALMIN/WEBMIN'
}


target = input('Enter host to scan: ')
targetIP = gethostbyname(target)
print('-'*60)
print ('Please wait while it scans ', targetIP)
print('-'*60)



#scan reserved ports
for i in range(1, 65535):
    s = socket(AF_INET, SOCK_STREAM)
    result = s.connect_ex((targetIP, i))
    if(result == 0) :
        port = str(i)
        function = common_ports.get(port, "Unknown use")
        print ('Open port found: {0} for {1}'.format(i, function))
    s.close()
