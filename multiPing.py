import os
hostname = ['4.2.2.2', '8.8.8.8', '24.234.182.242']

for index in range(len(hostname)):
response = os.system("ping -c 1 " + hostname[index])

#and then check the response...
if response == 0:
  print hostname[index], 'is up!'
else:
  print hostname[index], 'is down!'