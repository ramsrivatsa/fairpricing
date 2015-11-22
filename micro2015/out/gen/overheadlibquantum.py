from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt



benchList = [ 'gcc', 'perlbench', 'leslie3d', 'povray', 'libquantum', 'astar', 'bzip2', 'milc', 'namd', 'calculix', 'h264ref', 'sphinx3', 'zeusmp', 'gobmk', 'hmmer', 'tonto', 'bwaves', 'gromacs', 'dealII', 'sjeng', 'lbm', 'xalancbmk', 'gamess', 'soplex', 'GemsFDTD', 'omnetpp', 'mcf', 'cactusADM' ]

colocationList = [ 'colocating with libquantum', 'colocating with mcf',  'colocating with sphinx3']
colocationListBaseline = [ 'colocating with libquantum', 'colocating with mcf', 'colocating with sphinx3' ]


runningList = [  'perlbench', 'colocating with libquantum', 'mcf', 'colocating with libquantum', 'leslie3d', 'colocating with libquantum', 'povray', 'colocating with libquantum', 'libquantum', 'colocating with libquantum', 'astar', 'colocating with libquantum', 'bzip2', 'colocating with libquantum', 'milc', 'colocating with libquantum', 'namd', 'colocating with libquantum', 'calculix', 'colocating with libquantum', 'h264ref', 'colocating with libquantum', 'gobmk', 'colocating with libquantum', 'hmmer', 'colocating with libquantum', 'tonto', 'colocating with libquantum', 'sphinx3', 'colocating with libquantum', 'bwaves', 'colocating with libquantum', 'gromacs', 'colocating with libquantum', 'dealII', 'colocating with libquantum', 'sjeng', 'colocating with libquantum', 'lbm', 'colocating with libquantum', 'xalancbmk', 'colocating with libquantum', 'gamess', 'colocating with libquantum', 'soplex', 'colocating with libquantum', 'cactusADM', 'colocating with libquantum', 'GemsFDTD', 'colocating with libquantum', 'omnetpp', 'colocating with libquantum' ]

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%.2f'%float(height), fontsize=8 )

def autolabel2(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., -1.25*height, '%.2f'%float(height),
                ha='center', va='top', fontsize=8)
        #plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%.2f'%float(height))


filename = 'execution_time_1000'
fList1 = [s.strip() for s in open('../../papergraphs/accuracy/libquantumcorunner/degradation2/%s.txt' % filename).readlines()]  #degradation
fList2 = [s.strip() for s in open('../../papergraphs/accuracy/libquantumcorunner/snapshot/phase_change_5.txt').readlines()]
fList3 = [s.strip() for s in open('../../papergraphs/accuracy/libquantumcorunner/priorwork/execution_time_5.txt').readlines()] #prior work



execution_time_shutter = defaultdict(lambda  : defaultdict(list))
execution_time_sec_shutter = defaultdict(lambda  : defaultdict(list))
avg_execution_time_shutter = defaultdict(dict)
execution_time_shutter2 = defaultdict(lambda  : defaultdict(list))
execution_time_sec_shutter2 = defaultdict(lambda  : defaultdict(list))
avg_execution_time_shutter2 = defaultdict(dict)
dictList_phase_change = defaultdict(lambda  : defaultdict(list))
dictList_phase_change2 = defaultdict(lambda  : defaultdict(list))

std_execution_time = defaultdict(dict)

def print_elapsed_time_shutter(time_shutter):
    for j in colocationList:
        for i in benchList:
            print '%s ||||  %s'%(j,i)
            print time_shutter[j][i]


sep = 'u'
for (b,a) in enumerate(fList1):
    #print a
    if a in colocationList:
        index = a
    else:
        if a in benchList:
            execution_time_shutter[index][a].append((fList1[b+4].split('system '))[1].split('elapsed')[0])

#print execution_time_shutter['colocating with mcf']['perlbench']
#print((s.split(start))[1].split(end)[0])

for j in colocationList:
    for i in benchList:
        for k in execution_time_shutter[j][i]:
            m,s = [float (var) for var in k.split(':')]
            temp = m*60 + s
            execution_time_sec_shutter[j][i].append(temp)

for (b,a) in enumerate(fList3):
    #print a
    if a in colocationList:
        index = a
    else:
        if a in benchList:
            #print index
            #print a
            execution_time_shutter2[index][a].append((fList3[b+4].split('system '))[1].split('elapsed')[0])

#print execution_time_shutter['colocating with mcf']['perlbench']
#print((s.split(start))[1].split(end)[0])

for j in colocationList:
    for i in benchList:
        for k in execution_time_shutter2[j][i]:
            #print k
            m,s = [float (var) for var in k.split(':')]
            temp = m*60 + s
            execution_time_sec_shutter2[j][i].append(temp)

for (b,a) in enumerate(fList2):
    if a in colocationList:
        index = a
    else:
        if a in benchList:
            dictList_phase_change[index][a].append(fList2[b+1])

for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]
    #print j,i
    for elem in dictList_phase_change[j][i]:
        dictList_phase_change2[j][i].extend(elem.strip().split('\t'))
    #print dictList_phase_change2[j][i]

yaxis = ()
yaxis2= ()
yaxis_abs = ()
error = ()
xaxis = ()
#print dictList_phase_change2['colocating with mcf']['perlbench']
for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]
    print j,i
    print dictList_phase_change2[j][i]
    #print i,j
    shutter_temp_list = []
    colo_temp_list = []
    for (count,item) in enumerate(dictList_phase_change2[j][i]):
        if count%2==1:
            colo_temp_list.append(float(item))
        if count%2==0:
            shutter_temp_list.append(float(item))
    #print shutter_temp_list
    shutter_avg = sum(shutter_temp_list)/len(shutter_temp_list)
    colocation_avg = sum(colo_temp_list)/len(colo_temp_list)
    del shutter_temp_list
    del colo_temp_list

    pause_period = ((colocation_avg ) + ((shutter_avg + (colocation_avg * 2)/3) * 3))/4
    xaxis = xaxis + (i,)
    #print (pause_period/np.mean(execution_time_sec_shutter[j][i]))*10
    yaxis = yaxis + ( (pause_period/np.mean(execution_time_sec_shutter[j][i]))*10  ,)
    yaxis2 = yaxis2 + ( (((np.mean(execution_time_sec_shutter2[j][i])/np.mean(execution_time_sec_shutter[j][i])) - 1)*100), )
    print np.mean(execution_time_sec_shutter2[j][i])
    print np.mean(execution_time_sec_shutter[j][i])
    #print '---------------------'

print yaxis2
#print np.mean(yaxis)


width = 0.25
x = np.arange(len(yaxis))
fig = plt.figure(figsize=(28, 5))
bar2 = plt.bar( x, yaxis2, width, color="k", label='Shuttering  (mean: %.2f)' %(np.mean(yaxis2)))
bar1 = plt.bar( x+width, yaxis, width, color="lightgrey", label='Snapshot (mean: %.2f)' %(np.mean(yaxis) ))


plt.ylabel( 'Execution time \n overhead (%)',fontsize='23' )
#plt.title('Overhead due to Prediction of degradation while co-running with LIBQUANTUM')
plt.xticks(x + width/2.0, xaxis, rotation='30', size='23', ha='center')
#plt.yticks((-5,0,10,20,30,40,50,60),('','0','10','20','30','40','50','60'),size='25')
plt.yticks((0,5,10,15),('0','5','10','15'),size='25')
#plt.yticks(np.arange(-10, 60, 10),size='25')
plt.xlim(-1,26)
plt.grid()
plt.legend(loc=9, ncol=2, prop={'size':28})
#leg.get_frame().set_alpha(0.1)
plt.tight_layout()
#plt.savefig('phase_chagnge_overheadmaybe.png', dpi=125)

import os as mars_awesome_os;
import matplotlib.pyplot as mars_awesome_plt;
mars_awesome_plt.savefig('overheadlibquantum.eps', bbox_inches='tight');
mars_awesome_os.popen('epstopdf overheadlibquantum.eps');
