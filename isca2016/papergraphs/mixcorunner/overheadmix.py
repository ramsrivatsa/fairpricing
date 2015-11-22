from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt


benchList = [ 'gcc', 'perlbench', 'leslie3d', 'povray', 'libquantum', 'astar', 'bzip2', 'milc', 'namd', 'calculix', 'h264ref', 'sphinx3', 'zeusmp', 'gobmk', 'hmmer', 'tonto', 'bwaves', 'gromacs', 'dealII', 'sjeng', 'lbm', 'xalancbmk', 'gamess', 'soplex', 'GemsFDTD', 'omnetpp', 'mcf', 'cactusADM' ]

colocationList = [ 'colocating with libquantum', 'colocating with mcf',  'colocating with milc']
colocationListBaseline = [ 'colocating with libquantum', 'colocating with mcf', 'colocating with milc' ]

runningList = [  'perlbench', 'colocating with milc', 'mcf', 'colocating with milc', 'leslie3d', 'colocating with milc', 'povray', 'colocating with milc', 'libquantum', 'colocating with milc', 'astar', 'colocating with milc', 'bzip2', 'colocating with milc', 'milc', 'colocating with milc', 'namd', 'colocating with milc', 'calculix', 'colocating with milc', 'h264ref', 'colocating with milc', 'gobmk', 'colocating with milc', 'hmmer', 'colocating with milc', 'tonto', 'colocating with milc', 'sphinx3', 'colocating with milc', 'zeusmp', 'colocating with milc',    'bwaves', 'colocating with milc', 'gromacs', 'colocating with milc', 'dealII', 'colocating with milc', 'sjeng', 'colocating with milc', 'lbm', 'colocating with milc', 'xalancbmk', 'colocating with milc', 'gamess', 'colocating with milc', 'cactusADM', 'colocating with milc', 'soplex', 'colocating with milc', 'GemsFDTD', 'colocating with milc', 'omnetpp', 'colocating with milc' ]
runningList2 = [  'leslie3d', 'colocating with milc', 'milc', 'colocating with milc', 'namd', 'colocating with milc', 'calculix', 'colocating with milc', 'gobmk', 'colocating with milc', 'hmmer', 'colocating with milc', 'tonto', 'colocating with milc', 'sphinx3', 'colocating with milc', 'zeusmp', 'colocating with milc', 'bwaves', 'colocating with milc', 'gromacs', 'colocating with milc', 'dealII', 'colocating with milc', 'sjeng', 'colocating with milc', 'gamess', 'colocating with milc', 'cactusADM', 'colocating with milc', 'soplex', 'colocating with milc', 'GemsFDTD', 'colocating with milc' ]
runningList3 = [  'perlbench', 'colocating with milc', 'mcf', 'colocating with milc', 'povray', 'colocating with milc', 'libquantum', 'colocating with milc', 'astar', 'colocating with milc', 'bzip2', 'colocating with milc', 'h264ref', 'colocating with milc',  'lbm', 'colocating with milc', 'xalancbmk', 'colocating with milc', 'omnetpp', 'colocating with milc' ]

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
fList1 = [s.strip() for s in open('degradation/%s.txt' % filename).readlines()]  #degradation
fList2 = [s.strip() for s in open('snapshot/phase_change_10.txt').readlines()]
fList3 = [s.strip() for s in open('priorwork/execution_time_4.txt').readlines()] #prior work
fList4 = [s.strip() for s in open('degradation/execution_time_100.txt').readlines()]  #degradation
#fList3 = [s.strip() for s in open('experiment_libquantum/phase_changes_5.txt').readlines()]
##fList3 = [s.strip() for s in open('../../papergraphs/2.fullspec/overhead/experiment_mcf/%s.txt' % filename).readlines()]
##fList4 = [s.strip() for s in open('../../papergraphs/2.fullspec/overhead/experiment_mcf/phase_changes_5.txt').readlines()]
##fList5 = [s.strip() for s in open('../../papergraphs/2.fullspec/overhead/experiment_sphinx3/%s.txt' % filename).readlines()]
##fList6 = [s.strip() for s in open('../../papergraphs/2.fullspec/overhead/experiment_sphinx3/phase_changes_5.txt').readlines()]
#print fList1


execution_time_shutter = defaultdict(lambda  : defaultdict(list))
execution_time_sec_shutter = defaultdict(lambda  : defaultdict(list))
avg_execution_time_shutter = defaultdict(dict)
execution_time_shutter2 = defaultdict(lambda  : defaultdict(list))
execution_time_sec_shutter2 = defaultdict(lambda  : defaultdict(list))
avg_execution_time_shutter2 = defaultdict(dict)
dictList_phase_change = defaultdict(lambda  : defaultdict(list))
dictList_phase_change2 = defaultdict(lambda  : defaultdict(list))
overhead_snapshot = defaultdict(lambda  : defaultdict(list))
overhead_shutter = defaultdict(lambda  : defaultdict(list))

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
        #print i
        for k in execution_time_shutter[j][i]:
            try:
                #print k
                m,s = [float (var) for var in k.split(':')]
                temp = m*60 + s
            except:
                h,m,s = [float (var) for var in k.split(':')]
                temp = h*3600 + m*60 + s
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
            try:
                m,s = [float (var) for var in k.split(':')]
                temp = m*60 + s
            except:
                h,m,s = [float (var) for var in k.split(':')]
                temp = h*3600 + m*60 + s
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
for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]
    #print j,i
    #print dictList_phase_change2[j][i]
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
    #xaxis = xaxis + (i,)
    #print (pause_period/np.mean(execution_time_sec_shutter[j][i]))*10
    overhead_snapshot[j][i] = (pause_period/np.mean(execution_time_sec_shutter[j][i]))*7.5
    overhead_shutter[j][i] = abs(((np.mean(execution_time_sec_shutter2[j][i])/np.mean(execution_time_sec_shutter[j][i])) - 1)*100)
    #yaxis = yaxis + ( (pause_period/np.mean(execution_time_sec_shutter[j][i]))*7.5  ,)
    #yaxis2 = yaxis2 + ( abs(((np.mean(execution_time_sec_shutter2[j][i])/np.mean(execution_time_sec_shutter[j][i])) - 1)*100), )
    #print '---------------------'


for a in xrange(0,len(runningList3),2):
    j = runningList3[a+1]
    i = runningList3[a]
    #print j,i,execution_time_sec_shutter2[j][i],execution_time_sec_shutter[j][i]

    #pause_period = ((colocation_avg ) + ((shutter_avg + (colocation_avg * 2)/3) * 3))/4
    #xaxis = xaxis + (i,)
    #print (pause_period/np.mean(execution_time_sec_shutter[j][i]))*10
    #yaxis = yaxis + ( (pause_period/np.mean(execution_time_sec_shutter[j][i]))*7.5  ,)
    overhead_shutter[j][i] = abs(((np.mean(execution_time_sec_shutter2[j][i])/np.mean(execution_time_sec_shutter[j][i])) - 1)*100)
    #yaxis2 = yaxis2 + ( abs(((np.mean(execution_time_sec_shutter2[j][i])/np.mean(execution_time_sec_shutter[j][i])) - 1)*100), )
#print np.mean(yaxis)

del execution_time_shutter
del execution_time_sec_shutter

execution_time_shutter = defaultdict(lambda  : defaultdict(list))
execution_time_sec_shutter = defaultdict(lambda  : defaultdict(list))


sep = 'u'
for (b,a) in enumerate(fList4):
    #print a
    if a in colocationList:
        index = a
    else:
        if a in benchList:
            execution_time_shutter[index][a].append((fList4[b+4].split('system '))[1].split('elapsed')[0])

#print execution_time_shutter['colocating with mcf']['perlbench']
#print((s.split(start))[1].split(end)[0])

for j in colocationList:
    for i in benchList:
        #print i
        for k in execution_time_shutter[j][i]:
            try:
                #print k
                m,s = [float (var) for var in k.split(':')]
                temp = m*60 + s
            except:
                h,m,s = [float (var) for var in k.split(':')]
                temp = h*3600 + m*60 + s
            execution_time_sec_shutter[j][i].append(temp)

for a in xrange(0,len(runningList3),2):
    j = runningList3[a+1]
    i = runningList3[a]
    #print j,i
    #print dictList_phase_change2[j][i]
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
    #xaxis = xaxis + (i,)
    #print (pause_period/np.mean(execution_time_sec_shutter[j][i]))*10
    #yaxis = yaxis + ( (pause_period/np.mean(execution_time_sec_shutter[j][i]))*7.5  ,)
    overhead_snapshot[j][i] = (pause_period/np.mean(execution_time_sec_shutter[j][i]))*7.5
    #yaxis2 = yaxis2 + ( abs(((np.mean(execution_time_sec_shutter2[j][i])/np.mean(execution_time_sec_shutter[j][i])) - 1)*100), )

for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]
    xaxis = xaxis + (i,)
    yaxis = yaxis + ( overhead_snapshot[j][i]  ,)
    yaxis2 = yaxis2 + ( overhead_shutter[j][i], )

print yaxis
print yaxis2


width = 0.25
x = np.arange(len(yaxis))
fig = plt.figure(figsize=(28, 5))
bar2 = plt.bar( x, yaxis2, width, color="k", label='Precise shuttering  (mean: %.2f)' %(np.mean(yaxis2)))
bar1 = plt.bar( x+width, yaxis, width, color="w", label='Snapshot shuttering (mean: %.2f)' %(np.mean(yaxis) ))
#bar3 = plt.bar( x+width+width, yaxis3, width, color="g", label=' colocating with sphinx3 (avg = %.1f)' %(np.mean(yaxis3)))
##bar3 = plt.bar( x+width+width, yaxis3, width, color="g", label='4 corunners (avg is %.1f)' %(np.mean(yaxis3) ))
##autolabel2(bar1)
##autolabel(bar2)
##autolabel2(bar3)
plt.ylabel( 'Execution time \n overhead(%)',fontsize=23)
#plt.title('Overhead due to Prediction of degradation while co-running with milc')
plt.xticks(x + width/2.0, xaxis, rotation='30', size='23', ha='center')
#plt.yticks((-5,0,10,20,30,40,50,60),('','0','10','20','30','40','50','60'),size='25')
plt.yticks((0,5,10,15,20,25),('0','5','10','15','20','25'),size='25')
plt.xlim(-1,27)
plt.grid()
plt.legend(prop={'size':28})
plt.tight_layout()
plt.savefig('mix_overhead.pdf', dpi=125)

