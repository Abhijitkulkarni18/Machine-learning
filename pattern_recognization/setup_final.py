from definition_final import *
import numpy as np
import time
from urllib.request import Request, urlopen
import ssl
from json import loads



date, thread_count, cpu, memory = np.loadtxt('server_stats3.txt', unpack=True, delimiter=',')

dataLength = int(thread_count.shape[0])
print('data length is', dataLength)
toWhat = 2700

#---------------------------------------THREAD COUNT---------------------------------------------------------------



avgLine = thread_count

avgLine = avgLine[:toWhat]
patternStorage(stat=1,avgLine)

#---------------------------------------THREAD COUNT---------------------------------------------------------------



#---------------------------------------CPU USAGE---------------------------------------------------------------


avgLine = cpu

avgLine = avgLine[:toWhat]
patternStorage(stat=2,avgLine)

#---------------------------------------CPU USAGE---------------------------------------------------------------


#---------------------------------------MEMORY USAGE---------------------------------------------------------------


avgLine = memory

avgLine = avgLine[:toWhat]
patternStorage(stat=3,avgLine)

#---------------------------------------MEMORY USAGE---------------------------------------------------------------


url = "http://10.38.159.92:5001/get_cis_server_stats?env=psup&service=qa&dc=dc1"

ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
req = Request(url)
i = 1;

while True:
    # try:
    #     data = loads(urlopen(url).read().decode("utf-8"))
    #     for key in data:
    #         # print('Hello')
    #         for k in data[key]:
    #             d = data[key][k]
    #             # print(d)
    #             file = open("server_stats3.txt", "a")
    #             # file.write(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) + "," + d['pid'] + "," + d['thread_count'] + "," + d['cpu'] + "," + d['mem'] + "\n")
    #             # print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) + "," + d['pid'] + "," + d['thread_count'] + "," + d['cpu'] + "," + d['mem'])
    #             # file.write(str(i) + "," + d['thread_count'] + "," + d['cpu'] + "\n")
    #             file.write(str(i) + "," + d['thread_count'] + "," + d['cpu'] + "," + d['mem'] +"\n")
    #
    #             file.close()
    #             break
    # except Exception as e:
    #     print(e)
    predict_value(stat=1)
    predict_value(stat=2)
    predict_value(stat=3)
    time.sleep(10)

