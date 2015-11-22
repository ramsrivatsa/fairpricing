import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
import matplotlib.cm as cmx
import matplotlib.colors as cl
import matplotlib.pyplot as pl


filename = '5'
f1 = [s.strip() for s in open('../../papergraphs/phases/pmutypes/single.txt').readlines()]
f2 = [s.strip() for s in open('../../papergraphs/phases/pmutypes/degradation.txt').readlines()]
#f3 = [s.strip() for s in open('../../papergraphs/phases/shutter_phase_%s.txt' % filename).readlines()]

benchListBaseline = [ 'gcc', 'perlbench', 'mcf', 'leslie3d', 'povray', 'libquantum', 'astar', 'bzip2', 'milc', 'namd', 'calculix', 'h264ref', 'zeusmp', 'gobmk', 'hmmer', 'tonto', 'sphinx3', 'bwaves', 'gromacs', 'dealII', 'sjeng', 'lbm', 'xalancbmk', 'gamess', 'cactusADM', 'soplex', 'GemsFDTD', 'omnetpp' ]
benchListExperiments = [ 'gcc', 'perlbench', 'mcf', 'leslie3d', 'povray', 'libquantum', 'astar', 'bzip2', 'milc', 'namd', 'calculix', 'h264ref', 'zeusmp', 'gobmk', 'hmmer', 'tonto', 'sphinx3', 'bwaves', 'gromacs', 'dealII', 'sjeng', 'lbm', 'xalancbmk', 'gamess', 'cactusADM', 'soplex', 'GemsFDTD', 'omnetpp' ]
colocationListBaseline = [ 'colocating with mcf', 'colocating with povray', 'colocating with astar', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with bzip2' ]
colocationListExperiments = [ 'colocating with mcf', 'colocating with povray', 'colocating with perlbench', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with bzip2' ]
runningList = [ 'mcf' ,'colocating with astar']

phaseList_single = defaultdict(list)
phaseList_degradation = defaultdict(lambda  : defaultdict(list))
phaseList_shutter = defaultdict(lambda  : defaultdict(list))
phaseList_colocation = defaultdict(lambda  : defaultdict(list))


llc_miss_phaseList_single = defaultdict(list)
llc_miss_phaseList_degradation = defaultdict(lambda  : defaultdict(list))
llc_miss_phaseList_shutter = defaultdict(lambda  : defaultdict(list))
llc_miss_phaseList_colocation = defaultdict(lambda  : defaultdict(list))



def setAxLinesBW(ax):
    MARKERSIZE = 3
    COLORMAP = {
        'g': {'marker': None, 'dash': (None,None)},
        'k': {'marker': None, 'dash': [5,5]},
        'r': {'marker': None, 'dash': [5,3,1,3]},
        'c': {'marker': None, 'dash': [1,3]},
        'm': {'marker': None, 'dash': [5,2,5,2,5,10]},
        'y': {'marker': None, 'dash': [5,3,1,2,1,10]},
        'b': {'marker': '+', 'dash': (None,None)} #[1,2,1,10]}
        }

    for line in ax.get_lines() + ax.get_legend().get_lines():
        origColor = line.get_color()
        line.set_color('black')
        line.set_dashes(COLORMAP[origColor]['dash'])
        line.set_marker(COLORMAP[origColor]['marker'])
        line.set_markersize(MARKERSIZE)

def setFigLinesBW(fig):
    for ax in fig.get_axes():
        setAxLinesBW(ax)

def color_maker(count, map='gnuplot2', min=0.100, max=0.900):
     assert(min >= 0.000 and max <= 1.000 and max > min)
     gran=100000.0
     maker = cmx.ScalarMappable(norm=cl.Normalize(vmin=0, vmax=int(gran)), cmap=pl.get_cmap(map))

     r = [min*gran]
     if count > 1:
         r = [min*gran + gran*x*(max-min)/float(count-1) for x in range(0, count)]

     return [maker.to_rgba(t) for t in r]
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

for line in f2:
    secondList1.append(line)

#for line in f3:
#    thirdList1.append(line)

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
    instruction_list4=[]
    cpi_list4=[]
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
            instruction_list2.append(float(a[1]))
            cpi_list2.append(a[2])

    for (b,a) in enumerate(phaseList_degradation[j][i]):
        if a[0][0] == '-':
            break
        else:
            instruction_list3.append(float(a[1]))
            cpi_list3.append(float(a[14])/10)

    for (b,a) in enumerate(phaseList_degradation[j][i]):
        if a[0][0] == '-':
            break
        else:
            instruction_list4.append(float(a[1]))
            cpi_list4.append(float(a[7])/1)
    #print instruction_list
    #print cpi_list

    color_list = color_maker(3, map="afmhot")
    f, ax1 = plt.subplots(figsize=(12,5))
    ax1.set_xlabel('Executed instructions', fontsize=23)
    ax1.set_ylabel('CPI',fontsize=23)
    ax1.plot(instruction_list2,cpi_list2, color='y', linestyle='-', marker='d', markevery=10, label= 'CPI solo')
    ax1.legend(loc=2,prop={'size':20})
    ax2 = ax1.twinx()
    ax2.plot(instruction_list3,cpi_list3, 'r--',  label= 'LLC store misses \nw/ %s' %(j[16:]))
    ax2.plot(instruction_list4,cpi_list4, color='b', linestyle='-', marker='.',  markevery=20,  label= 'L1-d load misses \nw/ %s' %(j[16:]))
    #ax2.plot(instruction_list3,cpi_list3, color='b',  label= 'co-run: %s with %s' %(i,j[16:]))
    ax2.set_ylabel('PMU Measurements',fontsize=23)
    ax1.set_ylim(-0.5,25)
    ax2.set_ylim(-0.5,25)
    ax2.set_xlim(0,320000000000)
    ax1.tick_params(axis='both', labelsize=18)
    ax2.tick_params(axis='both', labelsize=18)
    ax2.legend(loc=1,prop={'size':17}, ncol=2)
    del instruction_list1
    del cpi_list1

    #setFigLinesBW(f)
    #f.savefig('%s_and_libquantum2.pdf'%(i),bbox_inches='tight' ,dpi=200)

import os as mars_awesome_os;
import matplotlib.pyplot as mars_awesome_plt;
mars_awesome_plt.savefig('mcfl1dastar.eps', bbox_inches='tight');
mars_awesome_os.popen('epstopdf mcfl1dastar.eps');
