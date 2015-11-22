from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt


benchListBaseline = [ 'milc', 'bwaves', 'mcf', 'astar', 'bzip2', 'h264ref', 'tonto', 'lbm', 'xalancbmk', 'omnetpp', 'libquantum' ]
benchListExperiments = [ 'milc', 'bwaves', 'mcf', 'astar', 'bzip2', 'h264ref', 'tonto', 'lbm', 'xalancbmk', 'omnetpp', 'libquantum' ]
colocationListBaseline = [ 'colocating with lbm', 'colocating with povray', 'colocating with astar', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
colocationListExperiments = [ 'colocating with lbm', 'colocating with povray', 'colocating with perlbench', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
runningList = [ 'milc', 'colocating with libquantum', 'astar', 'colocating with libquantum', 'bzip2', 'colocating with libquantum', 'h264ref', 'colocating with libquantum', 'tonto', 'colocating with libquantum', 'lbm', 'colocating with libquantum', 'xalancbmk', 'colocating with libquantum', 'omnetpp', 'colocating with libquantum', 'mcf', 'colocating with libquantum', 'bwaves', 'colocating with libquantum', 'milc', 'colocating with mcf', 'astar', 'colocating with mcf', 'bzip2',
'colocating with mcf', 'h264ref', 'colocating with mcf', 'tonto', 'colocating with mcf', 'lbm', 'colocating with mcf', 'xalancbmk', 'colocating with mcf', 'omnetpp', 'colocating with mcf', 'mcf', 'colocating with mcf', 'bwaves', 'colocating with mcf', 'milc', 'colocating with lbm', 'astar', 'colocating with lbm', 'bzip2', 'colocating with lbm', 'h264ref', 'colocating with lbm', 'tonto', 'colocating with lbm', 'lbm', 'colocating with lbm', 'xalancbmk', 'colocating with lbm',
'omnetpp', 'colocating with lbm', 'mcf', 'colocating with lbm', 'bwaves', 'colocating with lbm', 'libquantum', 'colocating with libquantum', 'libquantum', 'colocating with mcf', 'libquantum', 'colocating with lbm',  ]


def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%.2f'%float(height), fontsize=8)

def autolabel2(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%.2f'%float(height))

filename = 'shutter_cpi_5'
fList = [s.strip() for s in open('../../papergraphs/3.compareprior/accuracy/phasechange/single_vm_ground_truth/shutter_cpi_1000.txt').readlines()]
fList2 = [s.strip() for s in open('../../papergraphs/3.compareprior/accuracy/phasechange/degradation_ground_truth/shutter_cpi_1000.txt').readlines()]
fList3 = [s.strip() for s in open('../../papergraphs/3.compareprior/accuracy/phasechange/experiment/%s.txt' % filename).readlines()]
fList4 = [s.strip() for s in open('../../papergraphs/3.compareprior/accuracy/shuttering/experiment/shutter_cpi_3.txt').readlines()]

dictList_single_vm = defaultdict(list)
dictList_degradation_colocation = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter_prev = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter2 = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter_prev2 = defaultdict(lambda  : defaultdict(list))
plot_degradation = defaultdict(dict)
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

for (b,a) in enumerate(fList4):
    if a in colocationListExperiments:
        index = a
    else:
        if a in benchListExperiments:
            dictList_degradation_shutter_prev[index][a].append(fList4[b+1])

#for a in xrange(0,len(runningList),2):
#    j = runningList[a+1]
#    i = runningList[a]
#    print i,j,dictList_degradation_shutter[j][i]
#APPENDING DEGRADATION SHUTTER2 as shutter and colocation values are tab separated

for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]
    for elem in dictList_degradation_shutter[j][i]:
        dictList_degradation_shutter2[j][i].extend(elem.strip().split('\t'))
    #print dictList_degradation_shutter2[j][i]

for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]
    for elem in dictList_degradation_shutter_prev[j][i]:
        dictList_degradation_shutter_prev2[j][i].extend(elem.strip().split('\t'))
    #print dictList_degradation_shutter2[j][i]
yaxis = ()
error = ()
xaxis = ()
yaxis2 = ()
error2 = ()
xaxis2 = ()
yaxis3 = ()
error3 = ()
xaxis3 = ()
sum_val = 0

for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]
    denominator1 = sum(float(n) for (m,n) in enumerate(dictList_single_vm[i]))/(len(dictList_single_vm[i]))
    numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_colocation[j][i]))/(len(dictList_degradation_colocation[j][i]))
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
    plot_degradation[j][i] = abs((((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100)
    sum_val = sum_val + float(plot_degradation[j][i])
    #print j,i,plot_degradation[j][i]
    #print plot_degradation_error[j][i]
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    if j == 'colocating with libquantum':
        xaxis = xaxis + (i,)
        yaxis = yaxis + (plot_degradation[j][i],)
        error = error + (plot_degradation_error[j][i],)
    if j == 'colocating with mcf':
        xaxis2 = xaxis2 + (i,)
        yaxis2 = yaxis2 + (plot_degradation[j][i],)
        error2 = error2 + (plot_degradation_error[j][i],)
    if j == 'colocating with lbm':
        xaxis3 = xaxis3 + (i,)
        yaxis3 = yaxis3 + (plot_degradation[j][i],)
        error3 = error3 + (plot_degradation_error[j][i],)
    #print numerator2,denominator2,numerator2/denominator2
    #print denominator2/numerator2
    #print j,i,plot_degradation[j][i]
            #print (((numerator2/denominator2)-(numerator1/denominator1))/(numerator2/denominator2))*100


del plot_degradation
del plot_degradation_error

plot_degradation = defaultdict(dict)
plot_degradation_error = defaultdict(dict)
yaxis4 = ()
error4 = ()
xaxis4 = ()
yaxis5 = ()
error5 = ()
xaxis5 = ()
yaxis6 = ()
error6 = ()
xaxis6 = ()
sum_val = 0

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
    plot_degradation[j][i] = abs((((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100)
    sum_val = sum_val + float(plot_degradation[j][i])
    #print j,i,plot_degradation[j][i]
    #print plot_degradation_error[j][i]
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    if j == 'colocating with libquantum':
        xaxis4 = xaxis4 + (i,)
        yaxis4 = yaxis4 + (plot_degradation[j][i],)
        error4 = error4 + (plot_degradation_error[j][i],)
    if j == 'colocating with mcf':
        xaxis5 = xaxis5 + (i,)
        yaxis5 = yaxis5 + (plot_degradation[j][i],)
        error5 = error5 + (plot_degradation_error[j][i],)
    if j == 'colocating with lbm':
        xaxis6 = xaxis6 + (i,)
        yaxis6 = yaxis6 + (plot_degradation[j][i],)
        error6 = error6 + (plot_degradation_error[j][i],)
    #print numerator2,denominator2,numerator2/denominator2
    #print denominator2/numerator2
    print j,i,plot_degradation[j][i]
            #print (((numerator2/denominator2)-(numerator1/denominator1))/(numerator2/denominator2))*100

#print xaxis
#print yaxis
#print error
#print np.mean(yaxis)
#print np.mean(yaxis2)
#print np.mean(yaxis3)
#print np.mean(sum_val)
#


width=0.25
x = np.arange(len(yaxis))
fig = plt.figure(figsize=(12, 5))
bar1 = plt.bar( x+width, yaxis3, width, color="r", yerr=error, label='Snapshot Shuttering (avg is %.1f)' % (np.mean(yaxis3)))
bar2 = plt.bar( x, yaxis6, width, color="b", yerr=error2,label='Precise Shuttering (avg is %.1f)' % (np.mean(yaxis6)))

plt.xticks(x + width, xaxis, rotation='30', size='20')
plt.xlim(-1,11)
plt.ylim(-1,40)
plt.legend(prop={'size':18})
plt.tight_layout()
plt.grid()
# default scale is 1 in your original case, scales with other cases:
#plt.show()
plt.savefig('%s_error_lbm.png' %(filename),  dpi=125)

import os as mars_awesome_os;
import matplotlib.pyplot as mars_awesome_plt;
mars_awesome_plt.savefig('compareaccuracy3.eps', bbox_inches='tight');
mars_awesome_os.popen('epstopdf compareaccuracy3.eps');
