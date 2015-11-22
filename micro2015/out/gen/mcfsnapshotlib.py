import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

filename = '5'
f1 = [s.strip() for s in open('../../papergraphs/phases/phasedetection/single.txt').readlines()]
#f2 = [s.strip() for s in open('degradation2/colocation_phase_5.txt').readlines()]
#f2 = [s.strip() for s in open('../../papergraphs/phases/phasedetection/degradation.txt').readlines()]
f3 = [s.strip() for s in open('../../papergraphs/phases/phasedetection/shutter_phase_%s.txt' % filename).readlines()]
#f4 = [s.strip() for s in open('colocation_phase_%s.txt' % filename).readlines()]


benchListBaseline = [ 'gcc', 'perlbench', 'mcf', 'leslie3d', 'povray', 'libquantum', 'astar', 'bzip2', 'milc', 'namd', 'calculix', 'h264ref', 'zeusmp', 'gobmk', 'hmmer', 'tonto', 'sphinx3', 'bwaves', 'gromacs', 'dealII', 'sjeng', 'lbm', 'xalancbmk', 'gamess', 'cactusADM', 'soplex', 'GemsFDTD', 'omnetpp' ]
benchListExperiments = [ 'gcc', 'perlbench', 'mcf', 'leslie3d', 'povray', 'libquantum', 'astar', 'bzip2', 'milc', 'namd', 'calculix', 'h264ref', 'zeusmp', 'gobmk', 'hmmer', 'tonto', 'sphinx3', 'bwaves', 'gromacs', 'dealII', 'sjeng', 'lbm', 'xalancbmk', 'gamess', 'cactusADM', 'soplex', 'GemsFDTD', 'omnetpp' ]
#benchListExperiments = [ 'perlbench', 'astar', 'soplex', 'xalancbmk', 'omnetpp', 'bzip2','povray']
#benchListExperiments = [ 'gcc', 'perlbench', 'astar', 'soplex', 'xalancbmk', 'omnetpp']
colocationListBaseline = [ 'colocating with mcf', 'colocating with povray', 'colocating with astar', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with bzip2' ]
colocationListExperiments = [ 'colocating with mcf', 'colocating with povray', 'colocating with perlbench', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with bzip2' ]

runningList = [ 'mcf' ,'colocating with libquantum']


phaseList_single = defaultdict(list)
phaseList_degradation = defaultdict(lambda  : defaultdict(list))
phaseList_shutter = defaultdict(lambda  : defaultdict(list))
phaseList_colocation = defaultdict(lambda  : defaultdict(list))


llc_miss_phaseList_single = defaultdict(list)
llc_miss_phaseList_degradation = defaultdict(lambda  : defaultdict(list))
llc_miss_phaseList_shutter = defaultdict(lambda  : defaultdict(list))
llc_miss_phaseList_colocation = defaultdict(lambda  : defaultdict(list))

firstList1 = []
secondList1 = []
thirdList1 = []
fourthList1 = []
fifthList1 = []
sixthList1 = []
seventhList1 = []
eighthList1 = []

for line in f1:
    firstList1.append(line)

#for line in f2:
 #   secondList1.append(line)

for line in f3:
    thirdList1.append(line)



#print sixthList1
#print firstList1
global index
global index2

for (j,i) in enumerate(firstList1):
    #print i
    if i in benchListBaseline:
        index = i
    else:
        phaseList_single[index].append(i.split())


for (j,i) in enumerate(secondList1):
    if i in colocationListExperiments:
        index2=i
    elif i in benchListExperiments:
        index=i
    else:
        phaseList_degradation[index2][index].append(i.split())




for (j,i) in enumerate(thirdList1):
    if i in colocationListExperiments:
        index2=i
    elif i in benchListExperiments:
        index=i
    else:
        phaseList_shutter[index2][index].append(i.split())

#print len(phaseList_colocation['colocating with libquantum']['gcc'])
#print len(llc_miss_phaseList_colocation['colocating with libquantum']['gcc'])
##############place to get the lists to plot #############
for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]
    print i
    instruction_list1=[]
    cpi_list1=[]
    instruction_list2=[]
    cpi_list2=[]
    instruction_list3=[]
    cpi_list3=[]
    for (b,a) in enumerate(phaseList_shutter[j][i]):
        if a[0][0] == '-':
            break
        else:
            instruction_list1.append(float(a[1]))
            cpi_list1.append(a[2])

    for (b,a) in enumerate(phaseList_single[i]):
        if a[0][0] == '-':
            break
        else:
            instruction_list2.append(float(a[1])*1.6)
            cpi_list2.append(a[2])

    for (b,a) in enumerate(phaseList_degradation[j][i]):
        if a[0][0] == '-':
            break
        else:
            instruction_list3.append(float(a[1]))
            cpi_list3.append(float(a[14])/10)

    #print instruction_list
    #print cpi_list

    f, ax = plt.subplots(figsize=(12,5))
  
    ax.plot(instruction_list1,cpi_list1, color='r', label='mcf w/ libquantum')
    ax.plot(instruction_list2,cpi_list2, color='g',  label= 'mcf w/o libquantum')
    #ax.plot(instruction_list2,miss_list2, color='c', label='ground truth L3 cache miss rate (per thousand cycles) of %s running alone' %(i))
    #ax.set_title('Phase of lone execution of %s VS phase of %s running with %s'%(i,i,j))
    ax.set_xlabel('Executed instructions', fontsize=23)
    ax.set_ylabel('CPI', fontsize=23)
    #ax.set_ylabel('LLC store misses')
    #ax.set_ylabel('L1 Dcache load misses')
    ax.set_ylim(-0.1,6)
    ax.legend(loc=1,prop={'size':20})
    #plt.savefig('%s_and_libquantum.pdf'%(i),bbox_inches='tight' ,dpi=200)
    del instruction_list1
    del cpi_list1

import os as mars_awesome_os;
import matplotlib.pyplot as mars_awesome_plt;
mars_awesome_plt.savefig('mcfsnapshotlib.eps', bbox_inches='tight');
mars_awesome_os.popen('epstopdf mcfsnapshotlib.eps');
