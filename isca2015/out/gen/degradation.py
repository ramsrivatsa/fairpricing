from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

benchListBaseline = [ 'milc', 'bwaves', 'mcf', 'astar', 'bzip2', 'h264ref', 'tonto', 'lbm', 'xalancbmk', 'omnetpp', 'libquantum' ]
#benchListExperiments = [ 'perlbench', 'astar', 'soplex', 'xalancbmk', 'omnetpp', 'bzip2','povray']
benchListExperiments = [ 'milc', 'bwaves', 'mcf', 'astar', 'bzip2', 'h264ref', 'tonto', 'lbm', 'xalancbmk', 'omnetpp', 'libquantum' ]
#benchListExperiments = [ 'perlbench', 'astar', 'soplex', 'xalancbmk', 'omnetpp']
colocationListBaseline = [ 'colocating with lbm', 'colocating with povray', 'colocating with astar', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
colocationListExperiments = [ 'colocating with lbm', 'colocating with povray', 'colocating with perlbench', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
#benchListBaseline = [ 'gcc', 'perlbench', 'mcf', 'leslie3d', 'povray', 'libquantum', 'astar', 'bzip2', 'milc', 'namd', 'calculix', 'h264ref', 'zeusmp', 'gobmk', 'hmmer', 'tonto', 'sphinx3', 'bwaves', 'gromacs', 'dealII', 'sjeng', 'lbm', 'xalancbmk', 'gamess', 'cactusADM', 'soplex', 'GemsFDTD', 'omnetpp' ]
#benchListExperiments = [ 'gcc', 'perlbench', 'astar', 'soplex', 'xalancbmk', 'omnetpp']
#colocationListBaseline = [ 'colocating with gcc', 'colocating with mcf', 'colocating with perlbench', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with bzip2' ]
runningList = [ 'milc', 'colocating with libquantum', 'astar', 'colocating with libquantum', 'omnetpp', 'colocating with libquantum', 'mcf', 'colocating with libquantum', 'libquantum', 'colocating with libquantum', 'xalancbmk', 'colocating with libquantum', 'lbm', 'colocating with libquantum'  ]
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
fList = [s.strip() for s in open('../../papergraphs/1.intrograph/single_vm_ground_truth/shutter_cpi_1000.txt').readlines()]
fList2 = [s.strip() for s in open('../../papergraphs/1.intrograph/2_degradation_ground_truth/%s.txt' % filename).readlines()]
fList3 = [s.strip() for s in open('../../papergraphs/1.intrograph/3_degradation_ground_truth/%s.txt' % filename).readlines()]
fList4 = [s.strip() for s in open('../../papergraphs/1.intrograph/degradation_ground_truth/%s.txt' % filename).readlines()]
fList5 = [s.strip() for s in open('../../papergraphs/1.intrograph/prior_work/2_vm_prior_work/%s.txt' % filename2).readlines()]
fList6 = [s.strip() for s in open('../../papergraphs/1.intrograph/prior_work/3_vm_prior_work/%s.txt' % filename2).readlines()]
fList7 = [s.strip() for s in open('../../papergraphs/1.intrograph/prior_work/4_vm_prior_work/%s.txt' % filename2).readlines()]

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
    #dictList_degradation_colocation[j][i].sort()
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
    #for item in final_degradation[j][i]:
    #    plot_list.append(item/final_degradation[j][i][0])
    #print i,j,final_degradation[j][i]
    #x = np.arange(2,len(plot_list)+2,1)
    #ax.plot(np.arange(2,len(plot_list)+2,1), plot_list, label='%s' %(i))
    #ax.set_xticks(np.arange(min(x), max(x)+1, 1.0))
    #del plot_list

print vm2
print vm3
print vm4


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
    denominator2 = sum(float(n) for (m,n) in enumerate(shutter_temp_list) if m!=0 and m!=len(shutter_temp_list)-1)/(len(shutter_temp_list)-2)
    #print len(colo_temp_list)
    #print len(shutter_temp_list)
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
    shutter_vm2 = shutter_vm2 + (plot_degradation[j][i]*-1,)
    #print denominator2/numerator2
    #print j,i,plot_degradation[j][i]
            #print (((numerator2/denominator2)-(numerator1/denominator1))/(numerator2/denominator2))*100

print shutter_vm2


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
    denominator2 = sum(float(n) for (m,n) in enumerate(shutter_temp_list) if m!=0 and m!=len(shutter_temp_list)-1)/(len(shutter_temp_list)-2)
    #print len(colo_temp_list)
    #print len(shutter_temp_list)
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
    shutter_vm3 = shutter_vm3 + (plot_degradation[j][i]*-1,)
    #print denominator2/numerator2
    #print j,i,plot_degradation[j][i]
            #print (((numerator2/denominator2)-(numerator1/denominator1))/(numerator2/denominator2))*100

print shutter_vm3


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
    denominator2 = sum(float(n) for (m,n) in enumerate(shutter_temp_list) if m!=0 and m!=len(shutter_temp_list)-1)/(len(shutter_temp_list)-2)
    #print len(colo_temp_list)
    #print len(shutter_temp_list)
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
    shutter_vm4 = shutter_vm4 + (plot_degradation[j][i]*-1,)
    #print denominator2/numerator2
    #print j,i,plot_degradation[j][i]
            #print (((numerator2/denominator2)-(numerator1/denominator1))/(numerator2/denominator2))*100
print shutter_vm4

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
plt.bar( x, vm2, width, color="r", label='2 corunners running libquantum' )
#plt.text(0.5, 0.5, ha='center', va='center', size=24, alpha=.5)
plt.bar( x+width, vm3, width, color="b", label='3 corunners running libquantum ' )
plt.bar( x+width+width, vm4, width, color="g", label='4 corunners running libquantum ')
plt.ylim(0,6)
plt.ylabel( 'Degradation' )
plt.yticks(np.arange(0, 6, 1))
plt.xticks(())
plt.legend(prop={'size':8})
#plt.xticks(x + width, xaxis, rotation='30', size='8')

plt.subplot(2, 1, 2)
bar4 = plt.bar( x, shutter_vm2, width, color="r", label='2 corunners running libquantum' )
bar5 = plt.bar( x+width, shutter_vm3, width, color="b", label='3 corunners running libquantum ' )
bar6 = plt.bar( x+width+width, shutter_vm4, width, color="g", label='4 corunners running libquantum ')
#plt.yticks(())
#plt.text(0.5, 0.5, 'subplot(2,1,2)', ha='center', va='center',
#        size=24, alpha=.5)

plt.tight_layout()
plt.ylabel( 'Percentage Error' )
plt.xticks(x + width, xaxis, rotation='30', size='12')
plt.ylim(-30,0)
plt.yticks(np.arange(-30, 0, 10))
plt.tight_layout()
#plt.tight_layout()
## default scale is 1 in your original case, scales with other cases:
##plt.show()
plt.savefig('%s_degradation_colocation.png' %(filename),  dpi=125)

#plt.show()

import os as mars_awesome_os;
import matplotlib.pyplot as mars_awesome_plt;
mars_awesome_plt.savefig('degradation.eps', bbox_inches='tight');
mars_awesome_os.popen('epstopdf degradation.eps');
