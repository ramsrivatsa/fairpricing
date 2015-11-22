from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

benchListBaseline = [ 'gcc', 'perlbench', 'leslie3d', 'povray', 'libquantum', 'astar', 'bzip2', 'milc', 'namd', 'calculix', 'h264ref', 'sphinx3', 'zeusmp', 'gobmk', 'hmmer', 'tonto', 'bwaves', 'gromacs', 'dealII', 'sjeng', 'lbm', 'xalancbmk', 'gamess', 'cactusADM', 'soplex', 'GemsFDTD', 'omnetpp', 'mcf' ]
benchListExperiments = [ 'gcc', 'perlbench', 'leslie3d', 'povray', 'libquantum', 'astar', 'bzip2', 'milc', 'namd', 'calculix', 'h264ref', 'sphinx3', 'zeusmp', 'gobmk', 'hmmer', 'tonto', 'bwaves', 'gromacs', 'dealII', 'sjeng', 'lbm', 'xalancbmk', 'gamess', 'cactusADM', 'soplex', 'GemsFDTD', 'omnetpp', 'mcf' ]
colocationListBaseline = [ 'colocating with lbm', 'colocating with povray', 'colocating with astar', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
colocationListExperiments = [ 'colocating with lbm', 'colocating with povray', 'colocating with perlbench', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
runningList2 = [  'perlbench', 'colocating with libquantum', 'astar', 'colocating with libquantum', 'bzip2', 'colocating with libquantum', 'xalancbmk', 'colocating with libquantum', 'tonto', 'colocating with libquantum', 'h264ref', 'colocating with libquantum', 'omnetpp', 'colocating with libquantum']
runningList3 = [  'perlbench', 'colocating with libquantum', 'astar', 'colocating with libquantum', 'bzip2', 'colocating with libquantum', 'xalancbmk', 'colocating with libquantum', 'tonto', 'colocating with libquantum', 'h264ref', 'colocating with libquantum', 'omnetpp', 'colocating with libquantum']


def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%.2f'%float(height))

def autolabel2(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%.2f'%float(height))

filename = 'shutter_cpi_4'

fList = [s.strip() for s in open('singlevm/shutter_cpi_1000.txt').readlines()]
fList2 = [s.strip() for s in open('10/%s.txt' % filename).readlines()]
fList3 = [s.strip() for s in open('25/%s.txt' % filename).readlines()]
fList4 = [s.strip() for s in open('50/%s.txt' % filename).readlines()]
fList5 = [s.strip() for s in open('75/%s.txt' % filename).readlines()]
fList6 = [s.strip() for s in open('100/%s.txt' % filename).readlines()]
fList7 = [s.strip() for s in open('125/%s.txt' % filename).readlines()]

degradation_list = defaultdict(list)
dictList_single_vm = defaultdict(list)
dictList_degradation_colocation = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter2 = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter3 = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter4 = defaultdict(lambda  : defaultdict(list))
plot_degradation = defaultdict(dict)
plot_degradation2 = defaultdict(dict)
plot_degradation_abs = defaultdict(dict)
plot_degradation_abs2 = defaultdict(dict)


for (b,a) in enumerate(fList):
    if a in benchListBaseline:
        dictList_single_vm[a].append(fList[b+1])
#SORTING LIST CONTAING VALUES OF SINGLE SPEC RUNS INSIDE VMs

for i in benchListBaseline:
    dictList_single_vm[i].sort()
    #print i,dictList_single_vm[i]

#APPENDING DEGRADATION SHUTTER
for (b,a) in enumerate(fList2):
    if a in colocationListExperiments:
        index = a
    else:
        if a in benchListExperiments:
            dictList_degradation_shutter[index][a].append(fList2[b+1])

for (b,a) in enumerate(fList3):
    if a in colocationListExperiments:
        index = a
    else:
        if a in benchListExperiments:
            dictList_degradation_shutter3[index][a].append(fList3[b+1])

for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]
    #print i,j,dictList_degradation_shutter[j][i]
#APPENDING DEGRADATION SHUTTER2 as shutter and colocation values are tab separated
for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]
    for elem in dictList_degradation_shutter[j][i]:
        dictList_degradation_shutter2[j][i].extend(elem.strip().split('\t'))

    for elem in dictList_degradation_shutter3[j][i]:
        dictList_degradation_shutter4[j][i].extend(elem.strip().split('\t'))
    #print dictList_degradation_shutter2[j][i]

yaxis2 = ()
yaxis3 = ()
yaxis_abs2 = ()
yaxis_abs3 = ()
error2 = ()
error3 = ()
xaxis2 = ()
for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]

    denominator1 = sum(float(n) for (m,n) in enumerate(dictList_single_vm[i]) if m!=0 and m!=len(dictList_single_vm[i])-1)/(len(dictList_single_vm[i])-2)
    print denominator1
    #numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_colocation[j][i]))/(len(dictList_degradation_colocation[j][i]))
    shutter_temp_list = []
    shutter_temp_list2 = []
    colo_temp_list = []
    colo_temp_list2 = []
    degradation_temp_list = []
    degradation_temp_list2 = []
    error_temp_list = []
    error_temp_list2 = []
    #print numerator1
    #print denominator1
    for (count,item) in enumerate(dictList_degradation_shutter2[j][i]):
        if count%2==0:
            colo_temp_list.append(item)
        if count%2==1:
            shutter_temp_list.append(item)

    for (count,item) in enumerate(dictList_degradation_shutter4[j][i]):
        if count%2==0:
            colo_temp_list2.append(item)
        if count%2==1:
            shutter_temp_list2.append(item)

    #for (count,item) in enumerate(shutter_temp_list):
    #    degradation_temp_list.append(abs((((float(shutter_temp_list[count])/float(colo_temp_list[count]))-(numerator1/denominator1))/(float(shutter_temp_list[count])/float(colo_temp_list[count])))*100))

    shutter_temp_list.sort()
    shutter_temp_list2.sort()
    colo_temp_list.sort()
    colo_temp_list2.sort()
    #print shutter_temp_list
    #print colo_temp_list
    #print dictList_degradation_shutter2[j][i]
    denominator2 = sum(float(n) for (m,n) in enumerate(shutter_temp_list))/len(shutter_temp_list)
    numerator2 = sum(float(n) for (m,n) in enumerate(colo_temp_list))/len(colo_temp_list)
    #for (m,n) in enumerate(shutter_temp_list):
    #    ratio=float(n)/float(colo_temp_list[m])
    #    error_temp_list.append(abs((((ratio)-(numerator1/denominator1))/(numerator1/denominator1))*100))
    #plot_degradation_error[j][i]=np.std(error_temp_list)

    denominator3 = sum(float(n) for (m,n) in enumerate(shutter_temp_list2))/(len(shutter_temp_list2))
    numerator3 = sum(float(n) for (m,n) in enumerate(colo_temp_list2))/(len(colo_temp_list2))
    #for (m,n) in enumerate(shutter_temp_list2):
    #    ratio=float(n)/float(colo_temp_list2[m])
    #    error_temp_list2.append(abs((((ratio)-(numerator3/denominator3))/(numerator1/denominator1))*100))
    #plot_degradation_error2[j][i]=np.std(error_temp_list2)

    #print numerator2
    #print denominator2
    del shutter_temp_list
    del colo_temp_list
    del degradation_temp_list
    del shutter_temp_list2
    del colo_temp_list2
    del degradation_temp_list2
    plot_degradation[j][i] = ((denominator2/denominator1)-1)*100
    plot_degradation_abs[j][i] = abs(((denominator2/denominator1)-1)*100)
    plot_degradation2[j][i] =((denominator3/denominator1)-1)*100
    plot_degradation_abs2[j][i] = abs(((denominator3/denominator1)-1)*100)
    #print j,i,plot_degradation[j][i]
    #print plot_degradation_error[j][i]
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    degradation_list[i].append(plot_degradation_abs[j][i])
    degradation_list[i].append(plot_degradation_abs2[j][i])
    xaxis2 = xaxis2 + (i,)
    yaxis2 = yaxis2 + (plot_degradation[j][i],)
    yaxis3 = yaxis3 + (plot_degradation2[j][i],)
    yaxis_abs2 = yaxis_abs2 + (plot_degradation_abs[j][i],)
    yaxis_abs3 = yaxis_abs3 + (plot_degradation_abs2[j][i],)
    #error2 = error2 + (plot_degradation_error[j][i],)
    #error3 = error3 + (plot_degradation_error2[j][i],)
    #print numerator2,denominator2,numerator2/denominator2
    #print denominator2/numerator2
    #print j,i,plot_degradation[j][i],plot_degradation2[j][i]
            #print (((numerator2/denominator2)-(numerator1/denominator1))/(numerator2/denominator2))*100
#print np.mean(yaxis2)

del dictList_degradation_shutter
del dictList_degradation_shutter2
del dictList_degradation_shutter3
del dictList_degradation_shutter4
del plot_degradation
del plot_degradation2
del plot_degradation_abs
del plot_degradation_abs2

dictList_degradation_colocation = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter2 = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter3 = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter4 = defaultdict(lambda  : defaultdict(list))
plot_degradation = defaultdict(dict)
plot_degradation2 = defaultdict(dict)
plot_degradation_abs = defaultdict(dict)
plot_degradation_abs2 = defaultdict(dict)

for (b,a) in enumerate(fList):
    if a in benchListBaseline:
        dictList_single_vm[a].append(fList[b+1])

#SORTING LIST CONTAING VALUES OF SINGLE SPEC RUNS INSIDE VMs
for i in benchListBaseline:
    dictList_single_vm[i].sort()


#APPENDING DEGRADATION SHUTTER
for (b,a) in enumerate(fList4):
    if a in colocationListExperiments:
        index = a
    else:
        if a in benchListExperiments:
            dictList_degradation_shutter[index][a].append(fList4[b+1])

for (b,a) in enumerate(fList5):
    if a in colocationListExperiments:
        index = a
    else:
        if a in benchListExperiments:
            dictList_degradation_shutter3[index][a].append(fList5[b+1])

for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]
    #print i,j,dictList_degradation_shutter[j][i]
#APPENDING DEGRADATION SHUTTER2 as shutter and colocation values are tab separated
for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]
    for elem in dictList_degradation_shutter[j][i]:
        dictList_degradation_shutter2[j][i].extend(elem.strip().split('\t'))

    for elem in dictList_degradation_shutter3[j][i]:
        dictList_degradation_shutter4[j][i].extend(elem.strip().split('\t'))
    #print dictList_degradation_shutter2[j][i]

yaxis2 = ()
yaxis3 = ()
yaxis_abs2 = ()
yaxis_abs3 = ()
error2 = ()
error3 = ()
xaxis2 = ()
for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]

    denominator1 = sum(float(n) for (m,n) in enumerate(dictList_single_vm[i]) if m!=0 and m!=len(dictList_single_vm[i])-1)/(len(dictList_single_vm[i])-2)
    #numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_colocation[j][i]))/(len(dictList_degradation_colocation[j][i]))
    shutter_temp_list = []
    shutter_temp_list2 = []
    colo_temp_list = []
    colo_temp_list2 = []
    degradation_temp_list = []
    degradation_temp_list2 = []
    error_temp_list = []
    error_temp_list2 = []
    #print numerator1
    #print denominator1
    for (count,item) in enumerate(dictList_degradation_shutter2[j][i]):
        if count%2==0:
            colo_temp_list.append(item)
        if count%2==1:
            shutter_temp_list.append(item)

    for (count,item) in enumerate(dictList_degradation_shutter4[j][i]):
        if count%2==0:
            colo_temp_list2.append(item)
        if count%2==1:
            shutter_temp_list2.append(item)

    #for (count,item) in enumerate(shutter_temp_list):
    #    degradation_temp_list.append(abs((((float(shutter_temp_list[count])/float(colo_temp_list[count]))-(numerator1/denominator1))/(float(shutter_temp_list[count])/float(colo_temp_list[count])))*100))

    shutter_temp_list.sort()
    shutter_temp_list2.sort()
    colo_temp_list.sort()
    colo_temp_list2.sort()
    #print shutter_temp_list
    #print colo_temp_list
    #print dictList_degradation_shutter2[j][i]
    denominator2 = sum(float(n) for (m,n) in enumerate(shutter_temp_list))/len(shutter_temp_list)
    numerator2 = sum(float(n) for (m,n) in enumerate(colo_temp_list))/len(colo_temp_list)
    #for (m,n) in enumerate(shutter_temp_list):
    #    ratio=float(n)/float(colo_temp_list[m])
    #    error_temp_list.append(abs((((ratio)-(numerator1/denominator1))/(numerator1/denominator1))*100))
    #plot_degradation_error[j][i]=np.std(error_temp_list)

    denominator3 = sum(float(n) for (m,n) in enumerate(shutter_temp_list2))/(len(shutter_temp_list2))
    numerator3 = sum(float(n) for (m,n) in enumerate(colo_temp_list2))/(len(colo_temp_list2))
    #for (m,n) in enumerate(shutter_temp_list2):
    #    ratio=float(n)/float(colo_temp_list2[m])
    #    error_temp_list2.append(abs((((ratio)-(numerator3/denominator3))/(numerator1/denominator1))*100))
    #plot_degradation_error2[j][i]=np.std(error_temp_list2)

    #print numerator2
    #print denominator2
    del shutter_temp_list
    del colo_temp_list
    del degradation_temp_list
    del shutter_temp_list2
    del colo_temp_list2
    del degradation_temp_list2
    plot_degradation[j][i] = ((denominator2/denominator1)-1)*100
    plot_degradation_abs[j][i] = abs(((denominator2/denominator1)-1)*100)
    plot_degradation2[j][i] =((denominator3/denominator1)-1)*100
    plot_degradation_abs2[j][i] = abs(((denominator3/denominator1)-1)*100)
    #print j,i,plot_degradation[j][i]
    #print plot_degradation_error[j][i]
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    degradation_list[i].append(plot_degradation_abs[j][i])
    degradation_list[i].append(plot_degradation_abs2[j][i])
    xaxis2 = xaxis2 + (i,)
    yaxis2 = yaxis2 + (plot_degradation[j][i],)
    yaxis3 = yaxis3 + (plot_degradation2[j][i],)
    yaxis_abs2 = yaxis_abs2 + (plot_degradation_abs[j][i],)
    yaxis_abs3 = yaxis_abs3 + (plot_degradation_abs2[j][i],)

del dictList_degradation_shutter
del dictList_degradation_shutter2
del dictList_degradation_shutter3
del dictList_degradation_shutter4
del plot_degradation
del plot_degradation2
del plot_degradation_abs
del plot_degradation_abs2

dictList_degradation_colocation = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter2 = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter3 = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter4 = defaultdict(lambda  : defaultdict(list))
plot_degradation = defaultdict(dict)
plot_degradation2 = defaultdict(dict)
plot_degradation_abs = defaultdict(dict)
plot_degradation_abs2 = defaultdict(dict)


#APPENDING DEGRADATION SHUTTER
for (b,a) in enumerate(fList6):
    if a in colocationListExperiments:
        index = a
    else:
        if a in benchListExperiments:
            dictList_degradation_shutter[index][a].append(fList6[b+1])

for (b,a) in enumerate(fList7):
    if a in colocationListExperiments:
        index = a
    else:
        if a in benchListExperiments:
            dictList_degradation_shutter3[index][a].append(fList7[b+1])

for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]
    #print i,j,dictList_degradation_shutter[j][i]
#APPENDING DEGRADATION SHUTTER2 as shutter and colocation values are tab separated
for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]
    for elem in dictList_degradation_shutter[j][i]:
        dictList_degradation_shutter2[j][i].extend(elem.strip().split('\t'))

    for elem in dictList_degradation_shutter3[j][i]:
        dictList_degradation_shutter4[j][i].extend(elem.strip().split('\t'))
    #print dictList_degradation_shutter2[j][i]

yaxis2 = ()
yaxis3 = ()
yaxis_abs2 = ()
yaxis_abs3 = ()
error2 = ()
error3 = ()
xaxis2 = ()
for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]

    denominator1 = sum(float(n) for (m,n) in enumerate(dictList_single_vm[i]) if m!=0 and m!=len(dictList_single_vm[i])-1)/(len(dictList_single_vm[i])-2)
    #numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_colocation[j][i]))/(len(dictList_degradation_colocation[j][i]))
    shutter_temp_list = []
    shutter_temp_list2 = []
    colo_temp_list = []
    colo_temp_list2 = []
    degradation_temp_list = []
    degradation_temp_list2 = []
    error_temp_list = []
    error_temp_list2 = []
    #print numerator1
    #print denominator1
    for (count,item) in enumerate(dictList_degradation_shutter2[j][i]):
        if count%2==0:
            colo_temp_list.append(item)
        if count%2==1:
            shutter_temp_list.append(item)

    for (count,item) in enumerate(dictList_degradation_shutter4[j][i]):
        if count%2==0:
            colo_temp_list2.append(item)
        if count%2==1:
            shutter_temp_list2.append(item)

    #for (count,item) in enumerate(shutter_temp_list):
    #    degradation_temp_list.append(abs((((float(shutter_temp_list[count])/float(colo_temp_list[count]))-(numerator1/denominator1))/(float(shutter_temp_list[count])/float(colo_temp_list[count])))*100))

    shutter_temp_list.sort()
    shutter_temp_list2.sort()
    colo_temp_list.sort()
    colo_temp_list2.sort()
    #print shutter_temp_list
    #print colo_temp_list
    #print dictList_degradation_shutter2[j][i]
    denominator2 = sum(float(n) for (m,n) in enumerate(shutter_temp_list))/len(shutter_temp_list)
    numerator2 = sum(float(n) for (m,n) in enumerate(colo_temp_list))/len(colo_temp_list)
    #for (m,n) in enumerate(shutter_temp_list):
    #    ratio=float(n)/float(colo_temp_list[m])
    #    error_temp_list.append(abs((((ratio)-(numerator1/denominator1))/(numerator1/denominator1))*100))
    #plot_degradation_error[j][i]=np.std(error_temp_list)

    denominator3 = sum(float(n) for (m,n) in enumerate(shutter_temp_list2))/(len(shutter_temp_list2))
    numerator3 = sum(float(n) for (m,n) in enumerate(colo_temp_list2))/(len(colo_temp_list2))
    #for (m,n) in enumerate(shutter_temp_list2):
    #    ratio=float(n)/float(colo_temp_list2[m])
    #    error_temp_list2.append(abs((((ratio)-(numerator3/denominator3))/(numerator1/denominator1))*100))
    #plot_degradation_error2[j][i]=np.std(error_temp_list2)

    #print numerator2
    #print denominator2
    del shutter_temp_list
    del colo_temp_list
    del degradation_temp_list
    del shutter_temp_list2
    del colo_temp_list2
    del degradation_temp_list2
    plot_degradation[j][i] = ((denominator2/denominator1)-1)*100
    plot_degradation_abs[j][i] = abs(((denominator2/denominator1)-1)*100)
    plot_degradation2[j][i] =((denominator3/denominator1)-1)*100
    plot_degradation_abs2[j][i] = abs(((denominator3/denominator1)-1)*100)
    #print j,i,plot_degradation[j][i]
    #print plot_degradation_error[j][i]
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    degradation_list[i].append(plot_degradation_abs[j][i])
    degradation_list[i].append(plot_degradation_abs2[j][i])
    xaxis2 = xaxis2 + (i,)
    yaxis2 = yaxis2 + (plot_degradation[j][i],)
    yaxis3 = yaxis3 + (plot_degradation2[j][i],)
    yaxis_abs2 = yaxis_abs2 + (plot_degradation_abs[j][i],)
    yaxis_abs3 = yaxis_abs3 + (plot_degradation_abs2[j][i],)

xaxis = [10,25,50,75,100,125]
for a in xrange(0,len(runningList3),2):
    j = runningList2[a+1]
    i = runningList2[a]
    plt.plot(xaxis,degradation_list[i],label = '%s' %(i))
    #print i,degradation_list[i]

plt.xlabel('Shuttering Time', fontsize=25)
plt.ylabel('Error', fontsize=25)
plt.legend()
plt.show()


#width=0.25
#x = np.arange(len(yaxis2))
#fig = plt.figure(figsize=(12, 5))
##bar1 = plt.bar( x, yaxis, width, color="r", label='colocating with libquatum (avg = %.2f)' %(np.mean(yaxis_abs)))
#bar2 = plt.bar( x+width, yaxis_abs2, width, color="g", yerr=error2, label='Snapshot Shuttering  (avg = %.2f)' %(np.mean(yaxis_abs2)))
#bar1 = plt.bar( x, yaxis_abs3, width, color="r", yerr=error3, label='Precise Shuttering (avg = %.2f)' %(np.mean(yaxis_abs3)))
##bar3 = plt.bar( x+width+width, yaxis3, width, color="g", label='colocating with sphinx  (avg = %.2f)' %(np.mean(yaxis_abs3)))
##autolabel(bar1)
##autolabel(bar2)
#plt.ylabel( 'Percentage Error' )
#plt.title('Error in predicting degradation when co-locating with libquantum')
#plt.xticks(x + width/2.0, xaxis2, rotation='30', size='10',  ha='center', va='top')
#plt.ylim(-10,60)
#plt.xlim(-1,26)
#plt.grid()
#plt.tight_layout()
#plt.legend()
#plt.plot(xaxis,degradation_list['perlbench'],label = 'perlbench')
#plt.plot(xaxis,degradation_list['tonto'],label = 'tonto')
#plt.plot(xaxis,degradation_list['astar'],label = 'astar')
#plt.plot(xaxis,degradation_list['astar'],label = 'xalancbmk')
#plt.plot(xaxis,degradation_list['bzip2'],label = 'bzip2')
#plt.savefig('%s_line.png' %(filename), dpi=125)

