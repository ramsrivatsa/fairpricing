from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

benchListBaseline = [ 'perlbench', 'astar', 'sphinx3', 'h264ref', 'bzip2', 'tonto', 'xalancbmk', 'omnetpp' ]
#benchListExperiments = [ 'perlbench', 'astar', 'soplex', 'xalancbmk', 'omnetpp', 'bzip2','povray']
benchListExperiments = [ 'perlbench', 'astar', 'sphinx3', 'h264ref', 'bzip2', 'tonto', 'xalancbmk', 'omnetpp' ]
#benchListExperiments = [ 'perlbench', 'astar', 'soplex', 'xalancbmk', 'omnetpp']
colocationListBaseline = [ 'colocating with lbm', 'colocating with povray', 'colocating with astar', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
colocationListExperiments = [ 'colocating with lbm', 'colocating with povray', 'colocating with perlbench', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
runningList = [ 'perlbench', 'colocating with libquantum', 'astar', 'colocating with libquantum', 'sphinx3', 'colocating with libquantum', 'bzip2', 'colocating with libquantum', 'xalancbmk', 'colocating with libquantum', 'omnetpp', 'colocating with libquantum'  ]
colocationList = [ 'colocating with libquantum', 'colocating with mcf',  'colocating with sphinx3']
benchList = [  'perlbench', 'astar', 'sphinx3', 'h264ref', 'bzip2', 'tonto', 'xalancbmk', 'omnetpp'  ]
#benchList = [  'astar', 'omnetpp'  ]
#colocationListOracle = [ 'colocating with gcc', 'colocating with colocating with mcf', 'colocating with perlbench', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with bzip2' ]

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.1*height, '%.2f'%float(height), fontsize=8, ha='center', va= 'bottom')

def autolabel2(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., -1.1*height, '%.1f'%float(height), fontsize=8, ha='center', va= 'top')

filename = 'shutter_cpi_1000'
filename2 = 'shutter_cpi_4'
fList = [s.strip() for s in open('../../papergraphs/1.2intrograph/singlevm_23/shutter_cpi_1000.txt').readlines()]
fList2 = [s.strip() for s in open('../../papergraphs/1.2intrograph/2_degradation/%s.txt' % filename).readlines()]
fList3 = [s.strip() for s in open('../../papergraphs/1.2intrograph/3_degradation/%s.txt' % filename).readlines()]
fList4 = [s.strip() for s in open('../../papergraphs/1.2intrograph/4_degradation/%s.txt' % filename).readlines()]
fList5 = [s.strip() for s in open('../../papergraphs/1.2intrograph/2_prior/%s.txt' % filename2).readlines()]
fList6 = [s.strip() for s in open('../../papergraphs/1.2intrograph/3_prior/%s.txt' % filename2).readlines()]
fList7 = [s.strip() for s in open('../../papergraphs/1.2intrograph/4_prior/%s.txt' % filename2).readlines()]

executionground = 'execution_time_1000'
executionprior = 'execution_time_4'
fList8 = [s.strip() for s in open('../../papergraphs/1.2intrograph/2_degradation/%s.txt' % executionground).readlines()]  #degradation
fList9 = [s.strip() for s in open('../../papergraphs/1.2intrograph/2_prior/%s.txt' % executionprior).readlines()]  #degradation
fList10 = [s.strip() for s in open('../../papergraphs/1.2intrograph/3_degradation/%s.txt' % executionground).readlines()]  #degradation
fList11 = [s.strip() for s in open('../../papergraphs/1.2intrograph/3_prior/%s.txt' % executionprior).readlines()]  #degradation
fList12 = [s.strip() for s in open('../../papergraphs/1.2intrograph/4_degradation/%s.txt' % executionground).readlines()]  #degradation
fList13 = [s.strip() for s in open('../../papergraphs/1.2intrograph/4_prior/%s.txt' % executionprior).readlines()]  #degradation

dictList_single_vm = defaultdict(list)
dictList_single_vm_mean = defaultdict(float)
dictList_degradation_colocation = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter2 = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter_prev = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter_prev2 = defaultdict(lambda  : defaultdict(list))
final_degradation = defaultdict(lambda  : defaultdict(list))
plot_degradation = defaultdict(dict)
plot_degradation_error = defaultdict(dict)

execution_time_shutter = defaultdict(lambda  : defaultdict(list))
execution_time_sec_shutter = defaultdict(lambda  : defaultdict(list))
execution_time_shutter2 = defaultdict(lambda  : defaultdict(list))
execution_time_sec_shutter2 = defaultdict(lambda  : defaultdict(list))

std_execution_time = defaultdict(dict)
global index

def print_elapsed_time_shutter(time_shutter):
    for j in colocationList:
        for i in benchList:
            print '%s ||||  %s'%(j,i)
            print time_shutter[j][i]


sep = 'u'
for (b,a) in enumerate(fList8):
    #print a
    if a in colocationList:
        index = a
    else:
        if a in benchList:
            execution_time_shutter[index][a].append((fList8[b+4].split('system '))[1].split('elapsed')[0])

#print execution_time_shutter['colocating with mcf']['perlbench']
#print((s.split(start))[1].split(end)[0])

for j in colocationList:
    for i in benchList:
        for k in execution_time_shutter[j][i]:
            m,s = [float (var) for var in k.split(':')]
            temp = m*60 + s
            execution_time_sec_shutter[j][i].append(temp)

for (b,a) in enumerate(fList9):
    #print a
    if a in colocationList:
        index = a
    else:
        if a in benchList:
            #print index
            #print a
            execution_time_shutter2[index][a].append((fList9[b+4].split('system '))[1].split('elapsed')[0])

for j in colocationList:
    for i in benchList:
        for k in execution_time_shutter2[j][i]:
            #print k
            m,s = [float (var) for var in k.split(':')]
            temp = m*60 + s
            execution_time_sec_shutter2[j][i].append(temp)

overhead2 = ()

for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]

    #print (pause_period/np.mean(execution_time_sec_shutter[j][i]))*10
    overhead2 = overhead2 + ( abs(((np.mean(execution_time_sec_shutter2[j][i])/np.mean(execution_time_sec_shutter[j][i])) - 1)*100)*-1, )
    #print np.mean(execution_time_sec_shutter2[j][i])
    #print np.mean(execution_time_sec_shutter[j][i])

#print overhead2
del execution_time_shutter
del execution_time_sec_shutter
del execution_time_shutter2
del execution_time_sec_shutter2

## ------------------------------------------------------------------------------

execution_time_shutter = defaultdict(lambda  : defaultdict(list))
execution_time_sec_shutter = defaultdict(lambda  : defaultdict(list))
execution_time_shutter2 = defaultdict(lambda  : defaultdict(list))
execution_time_sec_shutter2 = defaultdict(lambda  : defaultdict(list))

std_execution_time = defaultdict(dict)

sep = 'u'
for (b,a) in enumerate(fList10):
    #print a
    if a in colocationList:
        index = a
    else:
        if a in benchList:
            execution_time_shutter[index][a].append((fList10[b+4].split('system '))[1].split('elapsed')[0])

#print execution_time_shutter['colocating with mcf']['perlbench']
#print((s.split(start))[1].split(end)[0])

for j in colocationList:
    for i in benchList:
        #print i
        for k in execution_time_shutter[j][i]:
            try:
                m,s = [float (var) for var in k.split(':')]
                #print m,s
                temp = m*60 + s
            except:
                h,m,s = [float (var) for var in k.split(':')]
                #print h,m,s
                temp = h*60*60 + m*60 + s
            execution_time_sec_shutter[j][i].append(temp)

for (b,a) in enumerate(fList11):
    #print a
    if a in colocationList:
        index = a
    else:
        if a in benchList:
            #print index
            #print a
            execution_time_shutter2[index][a].append((fList11[b+4].split('system '))[1].split('elapsed')[0])

for j in colocationList:
    for i in benchList:
        for k in execution_time_shutter2[j][i]:
            try:
                m,s = [float (var) for var in k.split(':')]
                #print m,s
                temp = m*60 + s
            except:
                h,m,s = [float (var) for var in k.split(':')]
                #print h,m,s
                temp = h*60*60 + m*60 + s
            execution_time_sec_shutter2[j][i].append(temp)

overhead3 = ()

for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]
    #print i

    #print (pause_period/np.mean(execution_time_sec_shutter[j][i]))*10
    overhead3 = overhead3 + ( abs(((np.mean(execution_time_sec_shutter2[j][i])/np.mean(execution_time_sec_shutter[j][i])) - 1)*100)*-1, )
    #print np.mean(execution_time_sec_shutter2[j][i])
    #print np.mean(execution_time_sec_shutter[j][i])

#rint overhead3
del execution_time_shutter
del execution_time_sec_shutter
del execution_time_shutter2
del execution_time_sec_shutter2


## ------------------------------------------------------------------------------

execution_time_shutter = defaultdict(lambda  : defaultdict(list))
execution_time_sec_shutter = defaultdict(lambda  : defaultdict(list))
execution_time_shutter2 = defaultdict(lambda  : defaultdict(list))
execution_time_sec_shutter2 = defaultdict(lambda  : defaultdict(list))

std_execution_time = defaultdict(dict)

def print_elapsed_time_shutter(time_shutter):
    for j in colocationList:
        for i in benchList:
            print '%s ||||  %s'%(j,i)
            print time_shutter[j][i]


sep = 'u'
for (b,a) in enumerate(fList12):
    #print a
    if a in colocationList:
        index = a
    else:
        if a in benchList:
            execution_time_shutter[index][a].append((fList12[b+4].split('system '))[1].split('elapsed')[0])

#print execution_time_shutter['colocating with mcf']['perlbench']
#print((s.split(start))[1].split(end)[0])

for j in colocationList:
    for i in benchList:
        #print i
        for k in execution_time_shutter[j][i]:
            try:
                m,s = [float (var) for var in k.split(':')]
                #print m,s
                temp = m*60 + s
            except:
                h,m,s = [float (var) for var in k.split(':')]
                #print h,m,s
                temp = h*60*60 + m*60 + s
            execution_time_sec_shutter[j][i].append(temp)

for (b,a) in enumerate(fList13):
    #print a
    if a in colocationList:
        index = a
    else:
        if a in benchList:
            #print index
            #print a
            execution_time_shutter2[index][a].append((fList13[b+4].split('system '))[1].split('elapsed')[0])
            #execution_time_shutter2[index][a].append((fList13[b+4].split('system '))[1].split('elapsed')[0])

for j in colocationList:
    for i in benchList:
        for k in execution_time_shutter2[j][i]:
            try:
                m,s = [float (var) for var in k.split(':')]
                #print m,s
                temp = m*60 + s
            except:
                h,m,s = [float (var) for var in k.split(':')]
                #print h,m,s
                temp = h*60*60 + m*60 + s
            #print k
            execution_time_sec_shutter2[j][i].append(temp)

overhead4 = ()

for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]
    #print i

    #print (pause_period/np.mean(execution_time_sec_shutter[j][i]))*10
    overhead4 = overhead4 + ( (((np.mean(execution_time_sec_shutter2[j][i])/np.mean(execution_time_sec_shutter[j][i])) - 1)*100)*-1, )
    #print np.mean(execution_time_sec_shutter2[j][i])
    #print np.mean(execution_time_sec_shutter[j][i])

#print overhead4
del execution_time_shutter
del execution_time_sec_shutter
del execution_time_shutter2
del execution_time_sec_shutter2

##--------------------------------------------------------------------------


for (b,a) in enumerate(fList):
    if a in benchListBaseline:
        dictList_single_vm[a].append(fList[b+1])

#SORTING LIST CONTAING VALUES OF SINGLE SPEC RUNS INSIDE VMs
for i in benchListBaseline:
    dictList_single_vm[i].sort()
    dictList_single_vm_mean[i] = sum(float(item) for item in dictList_single_vm[i])/len(dictList_single_vm[i])
#    numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_colocation[j][i]))/(len(dictList_degradation_colocation[j][i]))
    #print i,dictList_single_vm_mean[i]

    #print i,dictList_single_vm[i]

for (b,a) in enumerate(fList2):
    #print a
    if a in colocationListBaseline:
       #print a
       index = a
    else:
        if a in benchListExperiments:
            #print a
            dictList_degradation_colocation[index][a].append(fList2[b+1])
#sorting the ground truth values
for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]
    #dictList_degradation_colocation[j][i].sort()
    #print j,i,dictList_degradation_colocation[j][i]

#APPENDING DEGRADATION SHUTTER
for (b,a) in enumerate(fList3):
    if a in colocationListExperiments:
        index = a
    else:
        if a in benchListExperiments:
            dictList_degradation_shutter[index][a].append(fList3[b+1])

for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]
    #dictList_degradation_colocation[j][i].sort()
    #print j,i,dictList_degradation_shutter[j][i]

for (b,a) in enumerate(fList4):
    if a in colocationListExperiments:
        index = a
    else:
        if a in benchListExperiments:
            dictList_degradation_shutter2[index][a].append(fList4[b+1])

for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]
    #dictList_degradation_colocation[j][i].sort()
    #print j,i,dictList_degradation_shutter2[j][i]



for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]
    #dictList_degradation_colocation[j][i].sort()
    #print j,i,dictList_degradation_shutter2[j][i]
    sum_of = []
    for n in dictList_degradation_colocation[j][i]:
        sum_of.append(float(n))
    #print np.mean(sum_of)
    final_degradation[j][i].append(np.mean(sum_of))
    del sum_of

    sum_of = []
    for n in dictList_degradation_shutter[j][i]:
        sum_of.append(float(n))
    #print np.mean(sum_of)
    final_degradation[j][i].append(np.mean(sum_of))
    del sum_of

    sum_of = []
    for n in dictList_degradation_shutter2[j][i]:
        sum_of.append(float(n))
    #print np.mean(sum_of)
    final_degradation[j][i].append(np.mean(sum_of))
    del sum_of

xaxis = ()
vm2 = ()
vm3 = ()
vm4 = ()
#fig, ax = plt.subplots()
for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]
    plot_list = []
    xaxis = xaxis + (i,)
    for (count,item) in enumerate(final_degradation[j][i]):
        #print count
        if count == 0:
            vm2 = vm2 + (final_degradation[j][i][0]/dictList_single_vm_mean[i] ,)
        if count == 1:
            vm3 = vm3 + (final_degradation[j][i][1]/dictList_single_vm_mean[i], )
        if count == 2:
            vm4 = vm4 + (final_degradation[j][i][2]/dictList_single_vm_mean[i], )

#print vm2
#print vm3
#print vm4


shutter_vm2 = ()
shutter_vm3 = ()
shutter_vm4 = ()


for (b,a) in enumerate(fList5):
    if a in colocationListExperiments:
        index = a
    else:
        if a in benchListExperiments:
            dictList_degradation_shutter_prev[index][a].append(fList5[b+1])

for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]
    for elem in dictList_degradation_shutter_prev[j][i]:
        dictList_degradation_shutter_prev2[j][i].extend(elem.strip().split('\t'))
    #print dictList_degradation_shutter_prev2[j][i]


for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]
    #print i
    denominator1 = sum(float(n) for (m,n) in enumerate(dictList_single_vm[i]))/(len(dictList_single_vm[i]))
    numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_colocation[j][i]))/(len(dictList_degradation_colocation[j][i]))
    shutter_temp_list = []
    colo_temp_list = []
    degradation_temp_list = []
    error_temp_list = []
    #print numerator1
    #print denominator1
    for (count,item) in enumerate(dictList_degradation_shutter_prev2[j][i]):
        #print item
        if count%2==0:
            colo_temp_list.append(item)
        if count%2==1:
            shutter_temp_list.append(item)

    for (count,item) in enumerate(shutter_temp_list):
        degradation_temp_list.append(abs((((float(shutter_temp_list[count])/float(colo_temp_list[count]))-(numerator1/denominator1))/(float(shutter_temp_list[count])/float(colo_temp_list[count])))*100))

    shutter_temp_list.sort()
    colo_temp_list.sort()
    #print shutter_temp_list
    #print colo_temp_list
    #print dictList_degradation_shutter2[j][i]
    denominator2 = sum(float(n) for (m,n) in enumerate(shutter_temp_list))/len(shutter_temp_list)
    #print len(colo_temp_list)
    #print len(shutter_temp_list)
    numerator2 = sum(float(n) for (m,n) in enumerate(colo_temp_list))/len(colo_temp_list)
    for (m,n) in enumerate(shutter_temp_list):
        ratio=float(n)/float(colo_temp_list[m])
        error_temp_list.append(abs((((ratio)-(numerator1/denominator1))/(numerator1/denominator1))*100))
    plot_degradation_error[j][i]=np.std(error_temp_list)

    #print numerator2
    #print denominator2
    del shutter_temp_list
    del colo_temp_list
    del degradation_temp_list
    #plot_degradation[j][i] = abs((((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100)
    plot_degradation[j][i] = abs(((denominator2/denominator1)-1)*100)
    shutter_vm2 = shutter_vm2 + (plot_degradation[j][i],)
    #print denominator2/numerator2
    #print j,i,plot_degradation[j][i]
            #print (((numerator2/denominator2)-(numerator1/denominator1))/(numerator2/denominator2))*100

#print shutter_vm2


del dictList_degradation_shutter_prev
del dictList_degradation_shutter_prev2
del plot_degradation
del plot_degradation_error

dictList_degradation_shutter_prev = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter_prev2 = defaultdict(lambda  : defaultdict(list))
plot_degradation = defaultdict(dict)
plot_degradation_error = defaultdict(dict)


for (b,a) in enumerate(fList6):
    if a in colocationListExperiments:
        index = a
    else:
        if a in benchListExperiments:
            dictList_degradation_shutter_prev[index][a].append(fList6[b+1])

for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]
    for elem in dictList_degradation_shutter_prev[j][i]:
        dictList_degradation_shutter_prev2[j][i].extend(elem.strip().split('\t'))
    #print dictList_degradation_shutter_prev2[j][i]


for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]
    #print i
    denominator1 = sum(float(n) for (m,n) in enumerate(dictList_single_vm[i]))/(len(dictList_single_vm[i]))
    numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_shutter[j][i]))/(len(dictList_degradation_shutter[j][i]))
    shutter_temp_list = []
    colo_temp_list = []
    degradation_temp_list = []
    error_temp_list = []
    #print numerator1
    #print denominator1
    for (count,item) in enumerate(dictList_degradation_shutter_prev2[j][i]):
        #print item
        if count%2==0:
            colo_temp_list.append(item)
        if count%2==1:
            shutter_temp_list.append(item)

    for (count,item) in enumerate(shutter_temp_list):
        degradation_temp_list.append(abs((((float(shutter_temp_list[count])/float(colo_temp_list[count]))-(numerator1/denominator1))/(float(shutter_temp_list[count])/float(colo_temp_list[count])))*100))

    shutter_temp_list.sort()
    colo_temp_list.sort()
    #print shutter_temp_list
    #print colo_temp_list
    #print dictList_degradation_shutter2[j][i]
    denominator2 = sum(float(n) for (m,n) in enumerate(shutter_temp_list))/len(shutter_temp_list)
    #print len(colo_temp_list)
    #print len(shutter_temp_list)
    numerator2 = sum(float(n) for (m,n) in enumerate(colo_temp_list))/len(colo_temp_list)
    for (m,n) in enumerate(shutter_temp_list):
        ratio=float(n)/float(colo_temp_list[m])
        error_temp_list.append(abs((((ratio)-(numerator1/denominator1))/(numerator1/denominator1))*100))
    plot_degradation_error[j][i]=np.std(error_temp_list)

    #print numerator2
    #print denominator2
    del shutter_temp_list
    del colo_temp_list
    del degradation_temp_list
    #plot_degradation[j][i] = abs((((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100)
    plot_degradation[j][i] = abs(((denominator2/denominator1)-1)*100)
    shutter_vm3 = shutter_vm3 + (plot_degradation[j][i],)
    #print denominator2/numerator2
    #print j,i,plot_degradation[j][i]
            #print (((numerator2/denominator2)-(numerator1/denominator1))/(numerator2/denominator2))*100

#print shutter_vm3


for (b,a) in enumerate(fList7):
    if a in colocationListExperiments:
        index = a
    else:
        if a in benchListExperiments:
            dictList_degradation_shutter_prev[index][a].append(fList7[b+1])

for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]
    for elem in dictList_degradation_shutter_prev[j][i]:
        dictList_degradation_shutter_prev2[j][i].extend(elem.strip().split('\t'))
    #print dictList_degradation_shutter_prev2[j][i]


for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]
    #print i
    denominator1 = sum(float(n) for (m,n) in enumerate(dictList_single_vm[i]))/(len(dictList_single_vm[i]))
    numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_shutter2[j][i]))/(len(dictList_degradation_shutter2[j][i]))
    shutter_temp_list = []
    colo_temp_list = []
    degradation_temp_list = []
    error_temp_list = []
    #print numerator1
    #print denominator1
    for (count,item) in enumerate(dictList_degradation_shutter_prev2[j][i]):
        #print item
        if count%2==0:
            colo_temp_list.append(item)
        if count%2==1:
            shutter_temp_list.append(item)

    for (count,item) in enumerate(shutter_temp_list):
        degradation_temp_list.append(abs((((float(shutter_temp_list[count])/float(colo_temp_list[count]))-(numerator1/denominator1))/(float(shutter_temp_list[count])/float(colo_temp_list[count])))*100))

    shutter_temp_list.sort()
    colo_temp_list.sort()
    #print shutter_temp_list
    #print colo_temp_list
    #print dictList_degradation_shutter2[j][i]
    denominator2 = sum(float(n) for (m,n) in enumerate(shutter_temp_list))/len(shutter_temp_list)
    #print len(colo_temp_list)
    #print len(shutter_temp_list)
    numerator2 = sum(float(n) for (m,n) in enumerate(colo_temp_list))/len(colo_temp_list)
    for (m,n) in enumerate(shutter_temp_list):
        ratio=float(n)/float(colo_temp_list[m])
        error_temp_list.append(abs((((ratio)-(numerator1/denominator1))/(numerator1/denominator1))*100))
    plot_degradation_error[j][i]=np.std(error_temp_list)

    #print numerator2
    #print denominator2
    del shutter_temp_list
    del colo_temp_list
    del degradation_temp_list
    #plot_degradation[j][i] = abs((((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100)
    plot_degradation[j][i] = abs(((denominator2/denominator1)-1)*100)
    shutter_vm4 = shutter_vm4 + (plot_degradation[j][i],)
    #print denominator2/numerator2
    #print j,i,plot_degradation[j][i]
            #print (((numerator2/denominator2)-(numerator1/denominator1))/(numerator2/denominator2))*100
#print shutter_vm4

del dictList_degradation_shutter_prev
del dictList_degradation_shutter_prev2
del plot_degradation
del plot_degradation_error

dictList_degradation_shutter_prev = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter_prev2 = defaultdict(lambda  : defaultdict(list))
plot_degradation = defaultdict(dict)
plot_degradation_error = defaultdict(dict)


width=0.2
x = np.arange(len(vm2))
plt.figure(figsize=(6, 4))
plt.subplot(2, 1, 1)
plt.bar( x, shutter_vm2, width, color="r", label='w/ 1 libquantum' )
#plt.text(0.5, 0.5, ha='center', va='center', size=24, alpha=.5)
plt.bar( x+width, shutter_vm3, width, color="b", label='w/ 2 libquantum' )
plt.bar( x+width+width, shutter_vm4, width, color="g", label='w/ 3 libquantum')
plt.ylim(0,60)
plt.ylabel( 'Estimation \n error (%)' , multialignment='center')
plt.yticks(np.arange(0, 60, 10))

plt.xticks(())
plt.legend(prop={'size':9}, loc=2)
#plt.xticks(x + width, xaxis, rotation='30', size='8')

plt.subplot(2, 1, 2)
bar4 = plt.bar( x, overhead2, width, color="r", label='2 corunners running libquantum' )
bar5 = plt.bar( x+width, overhead3, width, color="b", label='3 corunners running libquantum ' )
bar6 = plt.bar( x+width+width, overhead4, width, color="g", label='4 corunners running libquantum ')
#bar4.tick_params(axis='x', labelsize=28)
plt.yticks(())
#plt.text(0.5, 0.5, 'subplot(2,1,2)', ha='center', va='center',
 #       size=24, alpha=.5)

plt.tight_layout()
plt.ylabel( 'Shuttering \n overhead (%)', fontsize=12, multialignment='center')
plt.xticks(x + width, xaxis, rotation='30', size='12')
#plt.ylim(-15,0)
plt.yticks(np.arange(-15,0,5), ('15','10','5'))
#labels = np.arange(-15,0,5)
#plt.yticks(labels)
#labels[1] = 'testing'
plt.tight_layout()
#plt.tight_layout()
## default scale is 1 in your original case, scales with other cases:
##plt.show()

import os as mars_awesome_os;
import matplotlib.pyplot as mars_awesome_plt;
mars_awesome_plt.savefig('overheads_precise_shuttering.eps', bbox_inches='tight');
mars_awesome_os.popen('epstopdf overheads_precise_shuttering.eps');
