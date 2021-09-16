import numpy as np
import time
from urllib.request import Request, urlopen
import ssl
from json import loads
import _pickle

totalStart = time.time()


def percentChange(startPoint, currentPoint):
    try:
        x = ((float(currentPoint) - startPoint) / abs(startPoint)) * 100.00
        if x == 0.0:
            return 0.000000001
        else:
            return x
    except:
        return 0.0001


def patternStorage(stat,avgLine):


    startTime = time.time()
    patternAr = []
    threshold = []

    x = len(avgLine) - 30
    y = 31

    while y < x:
        pattern = []

        p1 = percentChange(avgLine[y - 30], avgLine[y - 29])
        p2 = percentChange(avgLine[y - 30], avgLine[y - 28])
        p3 = percentChange(avgLine[y - 30], avgLine[y - 27])
        p4 = percentChange(avgLine[y - 30], avgLine[y - 26])
        p5 = percentChange(avgLine[y - 30], avgLine[y - 25])
        p6 = percentChange(avgLine[y - 30], avgLine[y - 24])
        p7 = percentChange(avgLine[y - 30], avgLine[y - 23])
        p8 = percentChange(avgLine[y - 30], avgLine[y - 22])
        p9 = percentChange(avgLine[y - 30], avgLine[y - 21])
        p10 = percentChange(avgLine[y - 30], avgLine[y - 20])
        p11 = percentChange(avgLine[y - 30], avgLine[y - 19])
        p12 = percentChange(avgLine[y - 30], avgLine[y - 18])
        p13 = percentChange(avgLine[y - 30], avgLine[y - 17])
        p14 = percentChange(avgLine[y - 30], avgLine[y - 16])
        p15 = percentChange(avgLine[y - 30], avgLine[y - 15])
        p16 = percentChange(avgLine[y - 30], avgLine[y - 14])
        p17 = percentChange(avgLine[y - 30], avgLine[y - 13])
        p18 = percentChange(avgLine[y - 30], avgLine[y - 12])
        p19 = percentChange(avgLine[y - 30], avgLine[y - 11])
        p20 = percentChange(avgLine[y - 30], avgLine[y - 10])
        p21 = percentChange(avgLine[y - 30], avgLine[y - 9])
        p22 = percentChange(avgLine[y - 30], avgLine[y - 8])
        p23 = percentChange(avgLine[y - 30], avgLine[y - 7])
        p24 = percentChange(avgLine[y - 30], avgLine[y - 6])
        p25 = percentChange(avgLine[y - 30], avgLine[y - 5])
        p26 = percentChange(avgLine[y - 30], avgLine[y - 4])
        p27 = percentChange(avgLine[y - 30], avgLine[y - 3])
        p28 = percentChange(avgLine[y - 30], avgLine[y - 2])
        p29 = percentChange(avgLine[y - 30], avgLine[y - 1])
        p30 = percentChange(avgLine[y - 30], avgLine[y])

        outcomeRange = avgLine[y + 1]
        


        threshold.append(outcomeRange)
        

        pattern.append(p1)
        pattern.append(p2)
        pattern.append(p3)
        pattern.append(p4)
        pattern.append(p5)
        pattern.append(p6)
        pattern.append(p7)
        pattern.append(p8)
        pattern.append(p9)
        pattern.append(p10)

        pattern.append(p11)
        pattern.append(p12)
        pattern.append(p13)
        pattern.append(p14)
        pattern.append(p15)
        pattern.append(p16)
        pattern.append(p17)
        pattern.append(p18)
        pattern.append(p19)
        pattern.append(p20)

        pattern.append(p21)
        pattern.append(p22)
        pattern.append(p23)
        pattern.append(p24)
        pattern.append(p25)
        pattern.append(p26)
        pattern.append(p27)
        pattern.append(p28)
        pattern.append(p29)
        pattern.append(p30)

        patternAr.append(pattern)
        

        y += 1
    if stat ==1:    
        with open('threshold_storage_thread.pickle','wb') as f:
            _pickle.dump(threshold,f)
        with open('pattern_storage_thread.pickle','wb') as f:
            _pickle.dump(patternAr,f)
    elif stat == 2:
        with open('threshold_storage_cpu.pickle','wb') as f:
            _pickle.dump(threshold,f)
        with open('pattern_storage_cpu.pickle','wb') as f:
            _pickle.dump(patternAr,f)
    elif stat == 3:
        with open('threshold_storage_mem.pickle','wb') as f:
            _pickle.dump(threshold,f)
        with open('pattern_storage_mem.pickle','wb') as f:
            _pickle.dump(patternAr,f)
    endTime = time.time()
    print("Number of Patterns: {}".format(len(patternAr)))

    print('Pattern storing took:', endTime - startTime)
    print("----------------------------------------------------------------------------------------------------------")


def currentPattern(avgLine,patForRec:list):
    mostRecentPoint = avgLine[-1]
    print("mostRecentPoint: {}".format(mostRecentPoint))

    cp1 = percentChange(avgLine[-31], avgLine[-30])
    cp2 = percentChange(avgLine[-31], avgLine[-29])
    cp3 = percentChange(avgLine[-31], avgLine[-28])
    cp4 = percentChange(avgLine[-31], avgLine[-27])
    cp5 = percentChange(avgLine[-31], avgLine[-26])
    cp6 = percentChange(avgLine[-31], avgLine[-25])
    cp7 = percentChange(avgLine[-31], avgLine[-24])
    cp8 = percentChange(avgLine[-31], avgLine[-23])
    cp9 = percentChange(avgLine[-31], avgLine[-22])
    cp10 = percentChange(avgLine[-31], avgLine[-21])
    cp11 = percentChange(avgLine[-31], avgLine[-20])
    cp12 = percentChange(avgLine[-31], avgLine[-19])
    cp13 = percentChange(avgLine[-31], avgLine[-18])
    cp14 = percentChange(avgLine[-31], avgLine[-17])
    cp15 = percentChange(avgLine[-31], avgLine[-16])
    cp16 = percentChange(avgLine[-31], avgLine[-15])
    cp17 = percentChange(avgLine[-31], avgLine[-14])
    cp18 = percentChange(avgLine[-31], avgLine[-13])
    cp19 = percentChange(avgLine[-31], avgLine[-12])
    cp20 = percentChange(avgLine[-31], avgLine[-11])
    cp21 = percentChange(avgLine[-31], avgLine[-10])
    cp22 = percentChange(avgLine[-31], avgLine[-9])
    cp23 = percentChange(avgLine[-31], avgLine[-8])
    cp24 = percentChange(avgLine[-31], avgLine[-7])
    cp25 = percentChange(avgLine[-31], avgLine[-6])
    cp26 = percentChange(avgLine[-31], avgLine[-5])
    cp27 = percentChange(avgLine[-31], avgLine[-4])
    cp28 = percentChange(avgLine[-31], avgLine[-3])
    cp29 = percentChange(avgLine[-31], avgLine[-2])
    cp30 = percentChange(avgLine[-31], avgLine[-1])

    patForRec.append(cp1)
    patForRec.append(cp2)
    patForRec.append(cp3)
    patForRec.append(cp4)
    patForRec.append(cp5)
    patForRec.append(cp6)
    patForRec.append(cp7)
    patForRec.append(cp8)
    patForRec.append(cp9)
    patForRec.append(cp10)
    patForRec.append(cp11)
    patForRec.append(cp12)
    patForRec.append(cp13)
    patForRec.append(cp14)
    patForRec.append(cp15)
    patForRec.append(cp16)
    patForRec.append(cp17)
    patForRec.append(cp18)
    patForRec.append(cp19)
    patForRec.append(cp20)
    patForRec.append(cp21)
    patForRec.append(cp22)
    patForRec.append(cp23)
    patForRec.append(cp24)
    patForRec.append(cp25)
    patForRec.append(cp26)
    patForRec.append(cp27)
    patForRec.append(cp28)
    patForRec.append(cp29)
    patForRec.append(cp30)




def patternRecognition(stat,patForRec:list):
    plotPatAr = []
    patFound = 0
    patDexAr = []
    count_index = 0
    if stat ==1:
        with open('pattern_storage_thread.pickle','rb') as f:
            patternAr= _pickle.load(f)
        with open('threshold_storage_thread.pickle','rb') as f:
            threshold= _pickle.load(f)
    elif stat ==2:
        with open('pattern_storage_cpu.pickle','rb') as f:
            patternAr= _pickle.load(f)
        with open('threshold_storage_cpu.pickle','rb') as f:
            threshold= _pickle.load(f)
    elif stat ==3:
        with open('pattern_storage_mem.pickle','rb') as f:
            patternAr= _pickle.load(f)
        with open('threshold_storage_mem.pickle','rb') as f:
            threshold= _pickle.load(f)
    for eachPattern in patternAr:
        sim1 = 100.00 - abs(percentChange(eachPattern[0], patForRec[0]))
        sim2 = 100.00 - abs(percentChange(eachPattern[1], patForRec[1]))
        sim3 = 100.00 - abs(percentChange(eachPattern[2], patForRec[2]))
        sim4 = 100.00 - abs(percentChange(eachPattern[3], patForRec[3]))
        sim5 = 100.00 - abs(percentChange(eachPattern[4], patForRec[4]))
        sim6 = 100.00 - abs(percentChange(eachPattern[5], patForRec[5]))
        sim7 = 100.00 - abs(percentChange(eachPattern[6], patForRec[6]))
        sim8 = 100.00 - abs(percentChange(eachPattern[7], patForRec[7]))
        sim9 = 100.00 - abs(percentChange(eachPattern[8], patForRec[8]))
        sim10 = 100.00 - abs(percentChange(eachPattern[9], patForRec[9]))

        sim11 = 100.00 - abs(percentChange(eachPattern[10], patForRec[10]))
        sim12 = 100.00 - abs(percentChange(eachPattern[11], patForRec[11]))
        sim13 = 100.00 - abs(percentChange(eachPattern[12], patForRec[12]))
        sim14 = 100.00 - abs(percentChange(eachPattern[13], patForRec[13]))
        sim15 = 100.00 - abs(percentChange(eachPattern[14], patForRec[14]))
        sim16 = 100.00 - abs(percentChange(eachPattern[15], patForRec[15]))
        sim17 = 100.00 - abs(percentChange(eachPattern[16], patForRec[16]))
        sim18 = 100.00 - abs(percentChange(eachPattern[17], patForRec[17]))
        sim19 = 100.00 - abs(percentChange(eachPattern[18], patForRec[18]))
        sim20 = 100.00 - abs(percentChange(eachPattern[19], patForRec[19]))

        sim21 = 100.00 - abs(percentChange(eachPattern[20], patForRec[20]))
        sim22 = 100.00 - abs(percentChange(eachPattern[21], patForRec[21]))
        sim23 = 100.00 - abs(percentChange(eachPattern[22], patForRec[22]))
        sim24 = 100.00 - abs(percentChange(eachPattern[23], patForRec[23]))
        sim25 = 100.00 - abs(percentChange(eachPattern[24], patForRec[24]))
        sim26 = 100.00 - abs(percentChange(eachPattern[25], patForRec[25]))
        sim27 = 100.00 - abs(percentChange(eachPattern[26], patForRec[26]))
        sim28 = 100.00 - abs(percentChange(eachPattern[27], patForRec[27]))
        sim29 = 100.00 - abs(percentChange(eachPattern[28], patForRec[28]))
        sim30 = 100.00 - abs(percentChange(eachPattern[29], patForRec[29]))

        howSim = (sim1 + sim2 + sim3 + sim4 + sim5 + sim6 + sim7 + sim8 + sim9 + sim10
                  + sim11 + sim12 + sim13 + sim14 + sim15 + sim16 + sim17 + sim18 + sim19 + sim20
                  + sim21 + sim22 + sim23 + sim24 + sim25 + sim26 + sim27 + sim28 + sim29 + sim30) / 30.00
        # print("Stat : {}".format(stat))
        if howSim > 99:

            patdex = count_index
            patFound = 1
            xp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                  29, 30]


            plotPatAr.append(eachPattern)
            patDexAr.append(patdex)
            print("Index of the patterns: {}".format(patdex))
        count_index = count_index + 1
    if patFound == 1:

        print('Pattern Found')
        print("Length of plotPatAr: {}".format(len(plotPatAr)))
        print("Length of patDexAr: {}".format(len(patDexAr)))
        # print(patDexAr)
        alert_flag = 0
        for eachPatt in patDexAr:
            print("Index of Matched Pattern: {}".format(eachPatt))
            futurePoints = eachPatt
            print("Prediction :{}".format(threshold[futurePoints]))
            if stat == 1:
                threshold_value = 187
            elif stat == 2:
                threshold_value = 190
            elif stat == 3:
                threshold_value = 195
            if threshold[futurePoints] >= threshold_value and alert_flag == 0:
                alert_flag = 1
                print('--------------------------------Alert---------------------------')

                print('futurePoints: {}'.format(futurePoints))

def predict_value(stat):

    # date, mem = np.loadtxt('server_stats3.txt', unpack=True, delimiter=',')
    #
    # dataLength = int(mem.shape[0])
    # print('data length is', dataLength)
    #
    # patternAr = []
    # performanceAr = []
    # threshold = []
    #
    #
    # avgLine = mem
    #
    # toWhat = 2700
    # avgLine = avgLine[:toWhat]
    # patternStorage(avgLine,patternAr=patternAr,performanceAr=performanceAr,threshold=threshold)

    count = 0

    # url = "http://10.38.159.92:5001/get_cis_server_stats?env=psup&service=qa&dc=dc1"
    #
    # ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    # ctx.check_hostname = False
    # ctx.verify_mode = ssl.CERT_NONE
    # req = Request(url)
    # i = 1;
    # while True:
    #     try:
    #         data = loads(urlopen(url).read().decode("utf-8"))
    #         for key in data:
    #             # print('Hello')
    #             for k in data[key]:
    #                 d = data[key][k]
    #                 # print(d)
    #                 file = open("server_stats3.txt", "a")
    #                 # file.write(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) + "," + d['pid'] + "," + d['thread_count'] + "," + d['cpu'] + "," + d['mem'] + "\n")
    #                 # print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) + "," + d['pid'] + "," + d['thread_count'] + "," + d['cpu'] + "," + d['mem'])
    #                 # file.write(str(i) + "," + d['thread_count'] + "," + d['cpu'] + "\n")
    #                 file.write(str(i) + "," + d['thread_count'] + "\n")
    #
    #                 file.close()
    #                 break
    #         i = i + 30
    #         time.sleep(1)
    #     except Exception as e:
    #         print(e)
    date, thread_count, cpu, memory = np.loadtxt('server_stats3.txt', unpack=True, delimiter=',')
    if(stat == 1):
        avgLine = thread_count
    elif(stat == 2):
        avgLine = cpu
    elif(stat == 3):
        avgLine = memory
    dataLength = thread_count.shape[0]
    print("New Datalength is: {}".format(dataLength))
    avgLine = avgLine[:dataLength]
    patForRec = []


    currentPattern(avgLine,patForRec=patForRec)
    patternRecognition(stat,patForRec=patForRec)
    count = count + 1
    print("Executing: {} times".format(count))

    totalEnd = time.time() - totalStart
    print('Entire processing took:', totalEnd, 'seconds')
    print("---------------------------------------------------------------------------")
        # time.sleep(10)

