from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

benchListBaseline = [ 'gcc', 'perlbench', 'leslie3d', 'povray', 'libquantum', 'astar', 'bzip2', 'milc', 'namd', 'calculix', 'h264ref', 'sphinx3', 'zeusmp', 'gobmk', 'hmmer', 'tonto', 'bwaves', 'gromacs', 'dealII', 'sjeng', 'lbm', 'xalancbmk', 'gamess', 'cactusADM', 'soplex', 'GemsFDTD', 'omnetpp', 'mcf' ]
benchListExperiments = [ 'gcc', 'perlbench', 'leslie3d', 'povray', 'libquantum', 'astar', 'bzip2', 'milc', 'namd', 'calculix', 'h264ref', 'sphinx3', 'zeusmp', 'gobmk', 'hmmer', 'tonto', 'bwaves', 'gromacs', 'dealII', 'sjeng', 'lbm', 'xalancbmk', 'gamess', 'cactusADM', 'soplex', 'GemsFDTD', 'omnetpp', 'mcf' ]
colocationListBaseline = [ 'colocating with lbm', 'colocating with povray', 'colocating with astar', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
colocationListExperiments = [ 'colocating with lbm', 'colocating with povray', 'colocating with perlbench', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
runningList = [  'perlbench', 'colocating with libquantum', 'mcf', 'colocating with libquantum', 'leslie3d', 'colocating with libquantum', 'povray', 'colocating with libquantum', 'libquantum', 'colocating with libquantum', 'astar', 'colocating with libquantum', 'bzip2', 'colocating with libquantum', 'milc', 'colocating with libquantum', 'namd', 'colocating with libquantum', 'calculix', 'colocating with libquantum', 'h264ref', 'colocating with libquantum', 'gobmk', 'colocating with libquantum', 'hmmer', 'colocating with libquantum', 'tonto', 'colocating with libquantum', 'sphinx3', 'colocating with libquantum', 'bwaves', 'colocating with libquantum', 'gromacs', 'colocating with libquantum', 'dealII', 'colocating with libquantum', 'sjeng', 'colocating with libquantum', 'lbm', 'colocating with libquantum', 'xalancbmk', 'colocating with libquantum', 'gamess', 'colocating with libquantum', 'cactusADM', 'colocating with libquantum', 'soplex', 'colocating with libquantum', 'GemsFDTD', 'colocating with libquantum', 'omnetpp', 'colocating with libquantum' ]
runningList2 = [  'perlbench', 'colocating with mcf', 'mcf', 'colocating with mcf', 'leslie3d', 'colocating with mcf', 'povray', 'colocating with mcf', 'libquantum', 'colocating with mcf', 'astar', 'colocating with mcf', 'bzip2', 'colocating with mcf', 'milc', 'colocating with mcf', 'namd', 'colocating with mcf', 'calculix', 'colocating with mcf', 'h264ref', 'colocating with mcf', 'gobmk', 'colocating with mcf', 'hmmer', 'colocating with mcf', 'tonto', 'colocating with mcf', 'sphinx3', 'colocating with mcf', 'bwaves', 'colocating with mcf', 'gromacs', 'colocating with mcf', 'dealII', 'colocating with mcf', 'sjeng', 'colocating with mcf', 'lbm', 'colocating with mcf', 'xalancbmk', 'colocating with mcf', 'gamess', 'colocating with mcf', 'cactusADM', 'colocating with mcf', 'soplex', 'colocating with mcf', 'GemsFDTD', 'colocating with mcf', 'omnetpp', 'colocating with mcf' ]


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

filename = 'shutter_cpi_5'
fList = [s.strip() for s in open('../../papergraphs/2.fullspec/accuracy/libquantumcorunner/single_vm_ground_truth/shutter_cpi_1000.txt').readlines()]
fList2 = [s.strip() for s in open('../../papergraphs/2.fullspec/accuracy/libquantumcorunner/degradation_ground_truth/shutter_cpi_1000.txt').readlines()]
fList3 = [s.strip() for s in open('../../papergraphs/2.fullspec/accuracy/libquantumcorunner/experiment_1/%s.txt' % filename).readlines()]

fList4 = [s.strip() for s in open('../../papergraphs/2.fullspec/accuracy/mcfcorunner/single_vm_ground_truth/shutter_cpi_1000.txt').readlines()]
fList5 = [s.strip() for s in open('../../papergraphs/2.fullspec/accuracy/mcfcorunner/degradation_ground_truth_mcf/shutter_cpi_1000.txt').readlines()]
fList6 = [s.strip() for s in open('../../papergraphs/2.fullspec/accuracy/mcfcorunner/experiment_1_mcf/%s.txt' % filename).readlines()]

fList7 = [s.strip() for s in open('../../papergraphs/2.fullspec/accuracy/sphinx3corunner/single_vm_ground_truth/shutter_cpi_1000.txt').readlines()]
fList8 = [s.strip() for s in open('../../papergraphs/2.fullspec/accuracy/sphinx3corunner/degradation_ground_truth_sphinx3/shutter_cpi_1000.txt').readlines()]
fList9 = [s.strip() for s in open('../../papergraphs/2.fullspec/accuracy/sphinx3corunner/experiment_1_sphinx3/%s.txt' % filename).readlines()]

dictList_single_vm = defaultdict(list)
dictList_degradation_colocation = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter2 = defaultdict(lambda  : defaultdict(list))
plot_degradation = defaultdict(dict)
plot_degradation_abs = defaultdict(dict)
plot_degradation_error = defaultdict(dict)

for (b,a) in enumerate(fList):
    if a in benchListBaseline:
        dictList_single_vm[a].append(fList[b+1])

#SORTING LIST CONTAING VALUES OF SINGLE SPEC RUNS INSIDE VMs
for i in benchListBaseline:
    dictList_single_vm[i].sort()
    #print i,dictList_single_vm[i]

global index
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
    dictList_degradation_colocation[j][i].sort()
    #print j,i,dictList_degradation_colocation[j][i]

#for a in xrange(0,len(runningList),2):
#    j = runningList[a+1]
#    i = runningList[a]
#    numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_colocation[j][i]) if m!=0 and m!=len(dictList_degradation_colocation[j][i])-1)/(len(dictList_degradation_colocation[j][i])-2)
#    print numerator1
#    #print dictList_degradation_colocation[runningList[a+1]][runningList[a]]
#    #print numerator1

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
    #print i,j,dictList_degradation_shutter[j][i]
#APPENDING DEGRADATION SHUTTER2 as shutter and colocation values are tab separated
for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]
    for elem in dictList_degradation_shutter[j][i]:
        dictList_degradation_shutter2[j][i].extend(elem.strip().split('\t'))
    #print dictList_degradation_shutter2[j][i]

yaxis = ()
yaxis_abs = ()
error = ()
xaxis = ()
for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]
    #print i,j
    #print dictList_single_vm[i]
    #print dictList_degradation_colocation[j][i]
    #print dictList_degradation_shutter2[j][i]
    denominator1 = sum(float(n) for (m,n) in enumerate(dictList_single_vm[i]) if m!=0 and m!=len(dictList_single_vm[i])-1)/(len(dictList_single_vm[i])-2)
    numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_colocation[j][i]) if m!=0 and m!=len(dictList_degradation_colocation[j][i])-1)/(len(dictList_degradation_colocation[j][i])-2)
    shutter_temp_list = []
    colo_temp_list = []
    degradation_temp_list = []
    error_temp_list = []
    #print numerator1
    #print denominator1
    for (count,item) in enumerate(dictList_degradation_shutter2[j][i]):
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
    denominator2 = sum(float(n) for (m,n) in enumerate(shutter_temp_list) if m!=0 and m!=len(shutter_temp_list)-1)/(len(shutter_temp_list)-2)
    numerator2 = sum(float(n) for (m,n) in enumerate(colo_temp_list) if m!=0 and m!=len(colo_temp_list)-1)/(len(colo_temp_list)-2)
    for (m,n) in enumerate(shutter_temp_list):
        ratio=float(n)/float(colo_temp_list[m])
        error_temp_list.append(abs((((ratio)-(numerator1/denominator1))/(numerator1/denominator1))*100))
    plot_degradation_error[j][i]=np.std(error_temp_list)

    #print numerator2
    #print denominator2
    del shutter_temp_list
    del colo_temp_list
    del degradation_temp_list
    plot_degradation[j][i] = (((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100
    plot_degradation_abs[j][i] = abs((((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100)
    #print j,i,plot_degradation[j][i]
    #print plot_degradation_error[j][i]
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    xaxis = xaxis + (i,)
    yaxis = yaxis + (plot_degradation[j][i],)
    yaxis_abs = yaxis_abs + (plot_degradation_abs[j][i],)
    error = error + (plot_degradation_error[j][i],)
    #print numerator2,denominator2,numerator2/denominator2
    #print denominator2/numerator2
    #print j,i,plot_degradation[j][i]
            #print (((numerator2/denominator2)-(numerator1/denominator1))/(numerator2/denominator2))*100

#print xaxis
print np.mean(yaxis)
#print error


del dictList_single_vm
del dictList_degradation_colocation
del dictList_degradation_shutter
del dictList_degradation_shutter2
del plot_degradation
del plot_degradation_error

dictList_single_vm = defaultdict(list)
dictList_degradation_colocation = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter2 = defaultdict(lambda  : defaultdict(list))
plot_degradation = defaultdict(dict)
plot_degradation_error = defaultdict(dict)

for (b,a) in enumerate(fList4):
    if a in benchListBaseline:
        dictList_single_vm[a].append(fList4[b+1])

#SORTING LIST CONTAING VALUES OF SINGLE SPEC RUNS INSIDE VMs
for i in benchListBaseline:
    dictList_single_vm[i].sort()
    #print i,dictList_single_vm[i]

for (b,a) in enumerate(fList5):
    #print a
    if a in colocationListBaseline:
       #print a
       index = a
    else:
        if a in benchListExperiments:
            #print a
            dictList_degradation_colocation[index][a].append(fList5[b+1])

#sorting the ground truth values
for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]
    dictList_degradation_colocation[j][i].sort()
    #print j,i,dictList_degradation_colocation[j][i]

#for a in xrange(0,len(runningList),2):
#    j = runningList[a+1]
#    i = runningList[a]
#    numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_colocation[j][i]) if m!=0 and m!=len(dictList_degradation_colocation[j][i])-1)/(len(dictList_degradation_colocation[j][i])-2)
#    print numerator1
#    #print dictList_degradation_colocation[runningList[a+1]][runningList[a]]
#    #print numerator1

#APPENDING DEGRADATION SHUTTER
for (b,a) in enumerate(fList6):
    if a in colocationListExperiments:
        index = a
    else:
        if a in benchListExperiments:
            dictList_degradation_shutter[index][a].append(fList6[b+1])

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
    #print dictList_degradation_shutter2[j][i]

yaxis2 = ()
yaxis_abs2 = ()
error2 = ()
xaxis2 = ()
for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]
    #print i,j
    #print dictList_single_vm[i]
    #print dictList_degradation_colocation[j][i]
    #print dictList_degradation_shutter2[j][i]
    denominator1 = sum(float(n) for (m,n) in enumerate(dictList_single_vm[i]) if m!=0 and m!=len(dictList_single_vm[i])-1)/(len(dictList_single_vm[i])-2)
    numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_colocation[j][i]) if m!=0 and m!=len(dictList_degradation_colocation[j][i])-1)/(len(dictList_degradation_colocation[j][i])-2)
    shutter_temp_list = []
    colo_temp_list = []
    degradation_temp_list = []
    error_temp_list = []
    #print numerator1
    #print denominator1
    for (count,item) in enumerate(dictList_degradation_shutter2[j][i]):
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
    denominator2 = sum(float(n) for (m,n) in enumerate(shutter_temp_list) if m!=0 and m!=len(shutter_temp_list)-1)/(len(shutter_temp_list)-2)
    numerator2 = sum(float(n) for (m,n) in enumerate(colo_temp_list) if m!=0 and m!=len(colo_temp_list)-1)/(len(colo_temp_list)-2)
    for (m,n) in enumerate(shutter_temp_list):
        ratio=float(n)/float(colo_temp_list[m])
        error_temp_list.append(abs((((ratio)-(numerator1/denominator1))/(numerator1/denominator1))*100))
    plot_degradation_error[j][i]=np.std(error_temp_list)

    #print numerator2
    #print denominator2
    del shutter_temp_list
    del colo_temp_list
    del degradation_temp_list
    plot_degradation[j][i] = (((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100
    plot_degradation_abs[j][i] = abs((((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100)
    #print j,i,plot_degradation[j][i]
    #print plot_degradation_error[j][i]
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    xaxis2 = xaxis2 + (i,)
    yaxis2 = yaxis2 + (plot_degradation[j][i],)
    yaxis_abs2 = yaxis_abs2 + (plot_degradation_abs[j][i],)
    error2 = error2 + (plot_degradation_error[j][i],)
    #print numerator2,denominator2,numerator2/denominator2
    #print denominator2/numerator2
    #print j,i,plot_degradation[j][i]
            #print (((numerator2/denominator2)-(numerator1/denominator1))/(numerator2/denominator2))*100
print np.mean(yaxis2)



del dictList_single_vm
del dictList_degradation_colocation
del dictList_degradation_shutter
del dictList_degradation_shutter2
del plot_degradation
del plot_degradation_error

dictList_single_vm = defaultdict(list)
dictList_degradation_colocation = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter2 = defaultdict(lambda  : defaultdict(list))
plot_degradation = defaultdict(dict)
plot_degradation_error = defaultdict(dict)

for (b,a) in enumerate(fList7):
    if a in benchListBaseline:
        dictList_single_vm[a].append(fList7[b+1])

#SORTING LIST CONTAING VALUES OF SINGLE SPEC RUNS INSIDE VMs
for i in benchListBaseline:
    dictList_single_vm[i].sort()
    #print i,dictList_single_vm[i]

for (b,a) in enumerate(fList8):
    #print a
    if a in colocationListBaseline:
       #print a
       index = a
    else:
        if a in benchListExperiments:
            #print a
            dictList_degradation_colocation[index][a].append(fList8[b+1])

#sorting the ground truth values
for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]
    dictList_degradation_colocation[j][i].sort()
    #print j,i,dictList_degradation_colocation[j][i]

#for a in xrange(0,len(runningList),2):
#    j = runningList[a+1]
#    i = runningList[a]
#    numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_colocation[j][i]) if m!=0 and m!=len(dictList_degradation_colocation[j][i])-1)/(len(dictList_degradation_colocation[j][i])-2)
#    print numerator1
#    #print dictList_degradation_colocation[runningList[a+1]][runningList[a]]
#    #print numerator1

#APPENDING DEGRADATION SHUTTER
for (b,a) in enumerate(fList9):
    if a in colocationListExperiments:
        index = a
    else:
        if a in benchListExperiments:
            dictList_degradation_shutter[index][a].append(fList9[b+1])

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
    #print dictList_degradation_shutter2[j][i]

yaxis3 = ()
yaxis_abs3 = ()
error3 = ()
xaxis3 = ()
for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]
    #print i,j
    #print dictList_single_vm[i]
    #print dictList_degradation_colocation[j][i]
    #print dictList_degradation_shutter2[j][i]
    denominator1 = sum(float(n) for (m,n) in enumerate(dictList_single_vm[i]) if m!=0 and m!=len(dictList_single_vm[i])-1)/(len(dictList_single_vm[i])-2)
    numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_colocation[j][i]) if m!=0 and m!=len(dictList_degradation_colocation[j][i])-1)/(len(dictList_degradation_colocation[j][i])-2)
    shutter_temp_list = []
    colo_temp_list = []
    degradation_temp_list = []
    error_temp_list = []
    #print numerator1
    #print denominator1
    for (count,item) in enumerate(dictList_degradation_shutter2[j][i]):
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
    denominator2 = sum(float(n) for (m,n) in enumerate(shutter_temp_list) )/(len(shutter_temp_list))
    numerator2 = sum(float(n) for (m,n) in enumerate(colo_temp_list))/(len(colo_temp_list))
    for (m,n) in enumerate(shutter_temp_list):
        ratio=float(n)/float(colo_temp_list[m])
        error_temp_list.append(abs((((ratio)-(numerator1/denominator1))/(numerator1/denominator1))*100))
    plot_degradation_error[j][i]=np.std(error_temp_list)

    #print numerator2
    #print denominator2
    del shutter_temp_list
    del colo_temp_list
    del degradation_temp_list
    plot_degradation[j][i] = (((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100
    plot_degradation_abs[j][i] = abs((((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100)
    #print j,i,plot_degradation[j][i]
    #print plot_degradation_error[j][i]
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    xaxis3 = xaxis3 + (i,)
    yaxis3 = yaxis3 + (plot_degradation[j][i],)
    yaxis_abs3 = yaxis_abs3 + (plot_degradation_abs[j][i],)
    error3 = error3 + (plot_degradation_error[j][i],)
    #print numerator2,denominator2,numerator2/denominator2
    #print denominator2/numerator2
    #print j,i,plot_degradation[j][i]
            #print (((numerator2/denominator2)-(numerator1/denominator1))/(numerator2/denominator2))*100
print np.mean(yaxis3)


width=0.25
x = np.arange(len(yaxis))
fig = plt.figure(figsize=(12, 5))
bar1 = plt.bar( x, yaxis, width, color="r", label='colocating with libquatum (avg = %.2f)' %(np.mean(yaxis_abs)))
bar2 = plt.bar( x+width, yaxis2, width, color="b", label='colocating with mcf  (avg = %.2f)' %(np.mean(yaxis_abs2)))
bar3 = plt.bar( x+width+width, yaxis3, width, color="g", label='colocating with sphinx  (avg = %.2f)' %(np.mean(yaxis_abs3)))
#autolabel(bar1)
#autolabel(bar2)
plt.ylabel( 'Percentage Error' )
plt.title('Error in predicting degradation')
plt.xticks(x + width/2.0, xaxis, rotation='30', size='10',  ha='center', va='top')
plt.ylim(-100,100)
plt.xlim(-1,25)
plt.grid()
plt.tight_layout()
plt.legend()
#plt.savefig('accuracy.png')
#plt.show()
#plt.savefig('%s_error.png' %(filename), dpi=125)

import os as mars_awesome_os;
import matplotlib.pyplot as mars_awesome_plt;
mars_awesome_plt.savefig('accuracy.eps', bbox_inches='tight');
mars_awesome_os.popen('epstopdf accuracy.eps');
