from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

#benchList = [ 'gcc', 'perlbench', 'leslie3d', 'povray', 'libquantum', 'astar', 'bzip2', 'milc', 'namd', 'calculix', 'h264ref', 'sphinx3', 'zeusmp', 'gobmk', 'hmmer', 'tonto', 'bwaves', 'gromacs', 'dealII', 'sjeng', 'lbm', 'xalancbmk', 'gamess', 'cactusADM', 'soplex', 'GemsFDTD', 'omnetpp' ]
#benchList = [ 'gcc', 'perlbench', 'sjeng', 'soplex', 'astar', 'libquantum', 'tonto', 'milc', 'dealII', 'xalancbmk' ]
#colocationList = [ 'colocating with milc', 'colocating with libquantum', 'colocating with astar' ]
#benchList = [ 'gcc', 'perlbench', 'sjeng', 'soplex', 'astar', 'libquantum' ]
#benchList = [ 'perlbench', 'sjeng', 'soplex', 'astar', 'libquantum' ]
#benchList = [ 'gcc', 'mcf', 'perlbench', 'astar', 'libquantum', 'povray', 'omnetpp', 'bzip2' ]
#colocationList = [ 'colocating with libquantum', 'colocating with astar' ]
#colocationListBaseline = [ 'colocating with milc', 'colocating with libquantum', 'colocating with astar' ]

benchList = [ 'gcc', 'perlbench', 'leslie3d', 'povray', 'libquantum', 'astar', 'bzip2', 'milc', 'namd', 'calculix', 'h264ref', 'sphinx3', 'zeusmp', 'gobmk', 'hmmer', 'tonto', 'bwaves', 'gromacs', 'dealII', 'sjeng', 'lbm', 'xalancbmk', 'gamess', 'soplex', 'GemsFDTD', 'omnetpp', 'mcf', 'cactusADM' ]
colocationList = [ 'colocating with libquantum', 'colocating with mcf',  'colocating with sphinx3', 'colocating with milc', 'colocating with namd' ]
colocationListBaseline = [ 'colocating with libquantum', 'colocating with mcf', 'colocating with sphinx3', 'colocating with milc', 'colocating with namd' ]

runningList=( 'perlbench',  'colocating with milc' ,  'mcf' , 'colocating with milc' , 'povray', 'colocating with milc' , 'libquantum' , 'colocating with milc' , 'astar',  'colocating with milc' , 'bzip2','colocating with milc' , 'h264ref',  'colocating with milc' , 'lbm', 'colocating with milc' , 'xalancbmk' , 'colocating with milc' , 'omnetpp' , 'colocating with milc', 'perlbench',  'colocating with namd' ,  'mcf' , 'colocating with namd' , 'povray', 'colocating with namd' , 'libquantum' , 'colocating with namd' , 'astar',  'colocating with namd' , 'bzip2',  'colocating with namd' , 'h264ref',  'colocating with namd' , 'lbm', 'colocating with namd' , 'xalancbmk' , 'colocating with namd' , 'omnetpp' , 'colocating with namd'      )

#colocationListBaseline = [ 'colocating with gcc', 'colocating with mcf', 'colocating with perlbench', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with lbm' ]
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
fList2 = [s.strip() for s in open('snapshot/phase_change_5.txt').readlines()]
#fList3 = [s.strip() for s in open('priorwork/execution_time_5.txt').readlines()] #prior work
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

###for (b,a) in enumerate(fList3):
###    #print a
###    if a in colocationList:
###        index = a
###    else:
###        if a in benchList:
###            #print index
###            #print a
###            execution_time_shutter2[index][a].append((fList3[b+4].split('system '))[1].split('elapsed')[0])

#print execution_time_shutter['colocating with mcf']['perlbench']
#print((s.split(start))[1].split(end)[0])

###for j in colocationList:
###    for i in benchList:
###        for k in execution_time_shutter2[j][i]:
###            #print k
###            m,s = [float (var) for var in k.split(':')]
###            temp = m*60 + s
###            execution_time_sec_shutter2[j][i].append(temp)

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
    #yaxis2 = yaxis2 + ( abs(((np.mean(execution_time_sec_shutter2[j][i])/np.mean(execution_time_sec_shutter[j][i])) - 1)*100), )
    #print '---------------------'

#print yaxis2
#print np.mean(yaxis)

#del execution_time_shutter
#del execution_time_sec_shutter
#del avg_execution_time_shutter
#del dictList_phase_change
#del dictList_phase_change2
#
#execution_time_shutter = defaultdict(lambda  : defaultdict(list))
#execution_time_sec_shutter = defaultdict(lambda  : defaultdict(list))
#avg_execution_time_shutter = defaultdict(dict)
#dictList_phase_change = defaultdict(lambda  : defaultdict(list))
#dictList_phase_change2 = defaultdict(lambda  : defaultdict(list))
#std_execution_time = defaultdict(dict)
#
#def print_elapsed_time_shutter(time_shutter):
#    for j in colocationList:
#        for i in benchList:
#            print '%s ||||  %s'%(j,i)
#            print time_shutter[j][i]
#
#sep = 'u'
#for (b,a) in enumerate(fList3):
#    #print a
#    if a in colocationList:
#        index = a
#    else:
#        if a in benchList:
#            execution_time_shutter[index][a].append((fList3[b+4].split('system '))[1].split('elapsed')[0])
#
##print execution_time_shutter['colocating with mcf']['perlbench']
##print((s.split(start))[1].split(end)[0])
#
#for j in colocationList:
#    for i in benchList:
#        for k in execution_time_shutter[j][i]:
#            m,s = [float (var) for var in k.split(':')]
#            temp = m*60 + s
#            execution_time_sec_shutter[j][i].append(temp)
#
#
#for (b,a) in enumerate(fList4):
#    if a in colocationList:
#        index = a
#    else:
#        if a in benchList:
#            dictList_phase_change[index][a].append(fList4[b+1])
#        print dictList_phase_change2[j][i]
#            #print fList4[b+1]
#
#
#for a in xrange(0,len(runningList2),2):
#    j = runningList2[a+1]
#    i = runningList2[a]
#    for elem in dictList_phase_change[j][i]:
#        dictList_phase_change2[j][i].extend(elem.strip().split('\t'))
#        #print dictList_phase_change2[j][i]
#
#yaxis2 = ()
#yaxis_abs2 = ()
#error2 = ()
#xaxis2 = ()
#for a in xrange(0,len(runningList2),2):
#    j = runningList2[a+1]
#    i = runningList2[a]
#    #print i,j
#    shutter_temp_list = []
#    colo_temp_list = []
#    print dictList_phase_change2[j][i]
#    for (count,item) in enumerate(dictList_phase_change2[j][i]):
#        if count%2==1:
#            colo_temp_list.append(float(item))
#        if count%2==0:
#            shutter_temp_list.append(float(item))
#
#    shutter_avg = sum(shutter_temp_list)/len(shutter_temp_list)
#    colocation_avg = sum(colo_temp_list)/len(colo_temp_list)
#    del shutter_temp_list
#    del colo_temp_list
#
#    pause_period = ((colocation_avg ) + ((shutter_avg + (colocation_avg * 2)/3) * 3))/4
#    xaxis2 = xaxis2 + (i,)
#    print (pause_period/np.mean(execution_time_sec_shutter[j][i]))*10
#    yaxis2 = yaxis2 + ( (pause_period/np.mean(execution_time_sec_shutter[j][i]))*10  ,)
#
#print yaxis2
#print np.mean(yaxis2)
#
#del execution_time_shutter
#del execution_time_sec_shutter
#del avg_execution_time_shutter
#del dictList_phase_change
#del dictList_phase_change2
#
#execution_time_shutter = defaultdict(lambda  : defaultdict(list))
#execution_time_sec_shutter = defaultdict(lambda  : defaultdict(list))
#avg_execution_time_shutter = defaultdict(dict)
#dictList_phase_change = defaultdict(lambda  : defaultdict(list))
#dictList_phase_change2 = defaultdict(lambda  : defaultdict(list))
#std_execution_time = defaultdict(dict)
#
#def print_elapsed_time_shutter(time_shutter):
#    for j in colocationList:
#        for i in benchList:
#            print '%s ||||  %s'%(j,i)
#            print time_shutter[j][i]
#
#sep = 'u'
#for (b,a) in enumerate(fList5):
#    #print a
#    if a in colocationList:
#        index = a
#    else:
#        if a in benchList:
#            execution_time_shutter[index][a].append((fList5[b+4].split('system '))[1].split('elapsed')[0])
#
##print execution_time_shutter['colocating with mcf']['perlbench']
##print((s.split(start))[1].split(end)[0])
#
#for j in colocationList:
#    for i in benchList:
#        for k in execution_time_shutter[j][i]:
#            m,s = [float (var) for var in k.split(':')]
#            temp = m*60 + s
#            execution_time_sec_shutter[j][i].append(temp)
#
#
#for (b,a) in enumerate(fList6):
#    if a in colocationList:
#        index = a
#    else:
#        if a in benchList:
#            dictList_phase_change[index][a].append(fList6[b+1])
#            #print dictList_phase_change[j][i]
#            #print fList4[b+1]
#
#
#for a in xrange(0,len(runningList3),2):
#    j = runningList3[a+1]
#    i = runningList3[a]
#    for elem in dictList_phase_change[j][i]:
#        dictList_phase_change2[j][i].extend(elem.strip().split('\t'))
#        #print dictList_phase_change2[j][i]
#
#yaxis3 = ()
#yaxis_abs3 = ()
#error3 = ()
#xaxis3 = ()
#for a in xrange(0,len(runningList3),2):
#    j = runningList3[a+1]
#    i = runningList3[a]
#    print i,j
#    shutter_temp_list = []
#    colo_temp_list = []
#    #print dictList_phase_change2[j][i]
#    for (count,item) in enumerate(dictList_phase_change2[j][i]):
#        if count%2==1:
#            colo_temp_list.append(float(item))
#        if count%2==0:
#            shutter_temp_list.append(float(item))
#
#    shutter_avg = sum(shutter_temp_list)/len(shutter_temp_list)
#    colocation_avg = sum(colo_temp_list)/len(colo_temp_list)
#    del shutter_temp_list
#    del colo_temp_list
#
#    pause_period = ((colocation_avg ) + ((shutter_avg + (colocation_avg * 2)/3) * 3))/4
#    xaxis3 = xaxis3 + (i,)
#    print (pause_period/np.mean(execution_time_sec_shutter[j][i]))*10
#    yaxis3 = yaxis3 + ( (pause_period/np.mean(execution_time_sec_shutter[j][i]))*10  ,)
#
#print yaxis3
#print np.mean(yaxis3)


part1 = ()
part2 = ()
xaxistemp = ()
for (m,n) in enumerate(yaxis):
    if m < len(yaxis)/2:
        part1 = part1 + (n,)
    else:
        part2 = part2 + (n,)
print part1
print part2

for (m,n) in enumerate(xaxis):
    if m < len(xaxis)/2:
        xaxistemp = xaxistemp + (n,)
width = 0.25
x = np.arange(len(part1))
fig = plt.figure(figsize=(12, 5))
bar1 = plt.bar( x, part1, width, color="b", label='colocating with MILC, LIBQUANTUM, MCF (avg = %.2f)' %(np.mean(part1)))
bar2 = plt.bar( x+width, part2, width, color="m",  label='co-locating with NAMD,ASTAR,TONTO (avg = %.2f)' %(np.mean(part2)))
#bar1 = plt.bar( x, yaxis, width, color="g", label='Snapshot Shuttering (avg = %.2f)' %(np.mean(yaxis) ))
#bar2 = plt.bar( x+width, yaxis2, width, color="r", label='Precise Shuttering  (avg = %.2f)' %(np.mean(yaxis2)))
#bar3 = plt.bar( x+width+width, yaxis3, width, color="g", label=' colocating with sphinx3 (avg = %.1f)' %(np.mean(yaxis3)))
##bar3 = plt.bar( x+width+width, yaxis3, width, color="g", label='4 corunners (avg is %.1f)' %(np.mean(yaxis3) ))
##autolabel2(bar1)
##autolabel(bar2)
##autolabel2(bar3)
plt.ylabel( 'Percentage Overhead' )
plt.title('Overhead due to Snapshot Shuttering when co-locating with multiple co-runners')
plt.xticks(x + width/2.0, xaxistemp, rotation='30', size='12', ha='center')
plt.ylim(-5,15)
plt.xlim(-1,10)
plt.grid()
plt.legend(prop={'size':12})
plt.tight_layout()
plt.savefig('phase_chagnge_overheadmaybe.png', dpi=125)
