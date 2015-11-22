from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt



benchList = [ 'gcc', 'perlbench', 'leslie3d', 'povray', 'libquantum', 'astar', 'bzip2', 'milc', 'namd', 'calculix', 'h264ref', 'sphinx3', 'zeusmp', 'gobmk', 'hmmer', 'tonto', 'bwaves', 'gromacs', 'dealII', 'sjeng', 'lbm', 'xalancbmk', 'gamess', 'soplex', 'GemsFDTD', 'omnetpp', 'mcf', 'cactusADM' ]

colocationList = [ 'colocating with libquantum', 'colocating with mcf',  'colocating with sphinx3']
colocationListBaseline = [ 'colocating with libquantum', 'colocating with mcf', 'colocating with sphinx3' ]


runningList = [  'perlbench', 'colocating with libquantum', 'mcf', 'colocating with libquantum', 'leslie3d', 'colocating with libquantum', 'povray', 'colocating with libquantum', 'libquantum', 'colocating with libquantum', 'astar', 'colocating with libquantum', 'bzip2', 'colocating with libquantum', 'milc', 'colocating with libquantum', 'namd', 'colocating with libquantum', 'calculix', 'colocating with libquantum', 'h264ref', 'colocating with libquantum', 'gobmk', 'colocating with libquantum', 'hmmer', 'colocating with libquantum', 'tonto', 'colocating with libquantum', 'sphinx3', 'colocating with libquantum', 'zeusmp', 'colocating with libquantum', 'bwaves', 'colocating with libquantum', 'gromacs', 'colocating with libquantum', 'dealII', 'colocating with libquantum', 'sjeng', 'colocating with libquantum', 'lbm', 'colocating with libquantum', 'xalancbmk', 'colocating with libquantum', 'gamess', 'colocating with libquantum', 'soplex', 'colocating with libquantum', 'cactusADM', 'colocating with libquantum', 'GemsFDTD', 'colocating with libquantum', 'omnetpp', 'colocating with libquantum' ]


siriusbenchList = [ 'gmm', 'dnn_asr', 'surf-fe', 'surf-fd', 'stem', 'regex', 'crf', 'img-imc', 'img-dig', 'img-face', 'nlp-pos', 'nlp-chk', 'nlp-ner']
siriuscolocationList = [ 'colocating with lbm', 'colocating with povray', 'colocating with astar', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
siriusrunningList = [ 'gmm', 'colocating with libquantum', 'dnn_asr', 'colocating with libquantum', 'surf-fe', 'colocating with libquantum', 'surf-fd', 'colocating with libquantum', 'stem', 'colocating with libquantum', 'regex', 'colocating with libquantum', 'crf', 'colocating with libquantum', 'img-imc', 'colocating with libquantum', 'img-dig', 'colocating with libquantum', 'img-face', 'colocating with libquantum', 'nlp-pos', 'colocating with libquantum', 'nlp-chk', 'colocating with libquantum', 'nlp-ner' , 'colocating with libquantum']

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


def add_line(ax, xpos, ypos):
    line = plt.Line2D([xpos, xpos], [ypos + .1, ypos - .5], transform=ax.transAxes, linewidth=2, color='black')
    line.set_clip_on(False)
    ax.add_line(line)

filename = 'execution_time_1000'
fList1 = [s.strip() for s in open('../../papergraphs/accuracy/libquantumcorunner/degradation2/%s.txt' % filename).readlines()]  #degradation
fList2 = [s.strip() for s in open('../../papergraphs/accuracy/libquantumcorunner/snapshot/phase_change_5.txt').readlines()]
fList3 = [s.strip() for s in open('../../papergraphs/accuracy/libquantumcorunner/priorwork/execution_time_5.txt').readlines()] #prior work


fList4 = [s.strip() for s in open('../../papergraphs/accuracy/libquantumcorunner/siriusdjinn/degradation/newval/%s.txt' % filename).readlines()]  #degradation
fList5 = [s.strip() for s in open('../../papergraphs/accuracy/libquantumcorunner/siriusdjinn/snapshot/phase_change_10.txt').readlines()]
fList6 = [s.strip() for s in open('../../papergraphs/accuracy/libquantumcorunner/siriusdjinn/priorwork/execution_time_4.txt').readlines()] #prior work

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

libyaxis = ()
libyaxis2= ()
libyaxis_abs = ()
liberror = ()
libxaxis = ()
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
    libxaxis = libxaxis + (i,)
    #print (pause_period/np.mean(execution_time_sec_shutter[j][i]))*10
    libyaxis = libyaxis + ( (pause_period/np.mean(execution_time_sec_shutter[j][i]))*7.5  ,)
    libyaxis2 = libyaxis2 + ( (((np.mean(execution_time_sec_shutter2[j][i])/np.mean(execution_time_sec_shutter[j][i])) - 1)*100), )
    print np.mean(execution_time_sec_shutter2[j][i])
    print np.mean(execution_time_sec_shutter[j][i])
    #print '---------------------'

#print yaxis2
#print np.mean(yaxis)


#width = 0.25
#x = np.arange(len(yaxis))
#fig = plt.figure(figsize=(28, 5))
#bar2 = plt.bar( x, yaxis2, width, color="k", label='Shuttering  (mean: %.2f)' %(np.mean(yaxis2)))
#bar1 = plt.bar( x+width, yaxis, width, color="lightgrey", label='Snapshot (mean: %.2f)' %(np.mean(yaxis) ))
#
#
#plt.ylabel( 'Execution time \n overhead (%)',fontsize='23' )
##plt.title('Overhead due to Prediction of degradation while co-running with LIBQUANTUM')
#plt.xticks(x + width/2.0, xaxis, rotation='30', size='23', ha='center')
##plt.yticks((-5,0,10,20,30,40,50,60),('','0','10','20','30','40','50','60'),size='25')
#plt.yticks((0,5,10,15),('0','5','10','15'),size='25')
##plt.yticks(np.arange(-10, 60, 10),size='25')
#plt.xlim(-1,26)
#plt.grid()
#plt.legend(loc=9, ncol=2, prop={'size':28})
##leg.get_frame().set_alpha(0.1)
#plt.tight_layout()
#plt.savefig('phase_chagnge_overheadmaybe.png', dpi=125)

#### ----------------------------------------------------------------------------------------------------------------------------------


#fList3 = [s.strip() for s in open('experiment_libquantum/phase_changes_5.txt').readlines()]
##fList3 = [s.strip() for s in open('../../papergraphs/2.fullspec/overhead/experiment_mcf/%s.txt' % filename).readlines()]
##fList4 = [s.strip() for s in open('../../papergraphs/2.fullspec/overhead/experiment_mcf/phase_changes_5.txt').readlines()]
##fList5 = [s.strip() for s in open('../../papergraphs/2.fullspec/overhead/experiment_sphinx3/%s.txt' % filename).readlines()]
##fList6 = [s.strip() for s in open('../../papergraphs/2.fullspec/overhead/experiment_sphinx3/phase_changes_5.txt').readlines()]
#print fList1

del execution_time_shutter
del execution_time_sec_shutter
del avg_execution_time_shutter
del execution_time_shutter2
del execution_time_sec_shutter2
del avg_execution_time_shutter2
del dictList_phase_change
del dictList_phase_change2

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
    for j in siriuscolocationList:
        for i in siriusbenchList:
            print '%s ||||  %s'%(j,i)
            print time_shutter[j][i]


sep = 'u'
for (b,a) in enumerate(fList4):
    print a
    if a in siriuscolocationList:
        index = a
    else:
        if a in siriusbenchList:
            execution_time_shutter[index][a].append((fList4[b+4].split('system '))[1].split('elapsed')[0])

#print execution_time_shutter['colocating with mcf']['perlbench']
#print((s.split(start))[1].split(end)[0])

for j in siriuscolocationList:
    for i in siriusbenchList:
        #print i
        for k in execution_time_shutter[j][i]:
            try:
                m,s = [float (var) for var in k.split(':')]
                temp = m*60 + s
            except:
                h,m,s = [float (var) for var in k.split(':')]
                temp = h*3600 + m*60 + s

            execution_time_sec_shutter[j][i].append(temp)

for (b,a) in enumerate(fList6):
    print a
    if a in siriuscolocationList:
        index = a
    else:
        if a in siriusbenchList:
            #print index
            #print a
            execution_time_shutter2[index][a].append((fList6[b+4].split('system '))[1].split('elapsed')[0])

#print execution_time_shutter['colocating with mcf']['perlbench']
#print((s.split(start))[1].split(end)[0])

for j in siriuscolocationList:
    for i in siriusbenchList:
        for k in execution_time_shutter2[j][i]:
            #print k
            m,s = [float (var) for var in k.split(':')]
            temp = m*60 + s
            execution_time_sec_shutter2[j][i].append(temp)

for (b,a) in enumerate(fList5):
    if a in siriuscolocationList:
        index = a
    else:
        if a in siriusbenchList:
            dictList_phase_change[index][a].append(fList5[b+1])

for a in xrange(0,len(siriusrunningList),2):
    j = siriusrunningList[a+1]
    i = siriusrunningList[a]
    #print j,i
    for elem in dictList_phase_change[j][i]:
        dictList_phase_change2[j][i].extend(elem.strip().split('\t'))
    #print dictList_phase_change2[j][i]

libsiri_yaxis = ()
libsiri_yaxis2= ()
libsiri_yaxis_abs = ()
libsiri_error = ()
libsiri_xaxis = ()
#print dictList_phase_change2['colocating with mcf']['perlbench']
for a in xrange(0,len(siriusrunningList),2):
    j = siriusrunningList[a+1]
    i = siriusrunningList[a]
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
    libsiri_xaxis = libsiri_xaxis + (i,)
    #print (pause_period/np.mean(execution_time_sec_shutter[j][i]))*10
    libsiri_yaxis = libsiri_yaxis + ( (pause_period/np.mean(execution_time_sec_shutter[j][i]))*10  ,)
    libsiri_yaxis2 = libsiri_yaxis2 + ( abs(((np.mean(execution_time_sec_shutter2[j][i])/np.mean(execution_time_sec_shutter[j][i])) - 1)*100), )
    #print np.mean(execution_time_sec_shutter2[j][i])
    #print np.mean(execution_time_sec_shutter[j][i])
    #print '---------------------'

#print xaxis
#print yaxis
#print yaxis2
#print np.mean(yaxis)

benchList = [ 'gcc', 'perlbench', 'leslie3d', 'povray', 'libquantum', 'astar', 'bzip2', 'milc', 'namd', 'calculix', 'h264ref', 'sphinx3', 'zeusmp', 'gobmk', 'hmmer', 'tonto', 'bwaves', 'gromacs', 'dealII', 'sjeng', 'lbm', 'xalancbmk', 'gamess', 'soplex', 'GemsFDTD', 'omnetpp', 'mcf', 'cactusADM' ]

colocationList = [ 'colocating with libquantum', 'colocating with mcf',  'colocating with sphinx3']
colocationListBaseline = [ 'colocating with libquantum', 'colocating with mcf', 'colocating with sphinx3' ]


runningList = [  'perlbench', 'colocating with mcf', 'mcf', 'colocating with mcf', 'leslie3d', 'colocating with mcf', 'povray', 'colocating with mcf', 'libquantum', 'colocating with mcf', 'astar', 'colocating with mcf', 'bzip2', 'colocating with mcf', 'milc', 'colocating with mcf', 'namd', 'colocating with mcf', 'calculix', 'colocating with mcf', 'h264ref', 'colocating with mcf', 'gobmk', 'colocating with mcf', 'hmmer', 'colocating with mcf', 'tonto', 'colocating with mcf', 'sphinx3', 'colocating with mcf', 'zeusmp', 'colocating with mcf', 'bwaves', 'colocating with mcf', 'gromacs', 'colocating with mcf', 'dealII', 'colocating with mcf', 'sjeng', 'colocating with mcf', 'lbm', 'colocating with mcf', 'xalancbmk', 'colocating with mcf', 'gamess', 'colocating with mcf', 'cactusADM', 'colocating with mcf', 'soplex', 'colocating with mcf', 'GemsFDTD', 'colocating with mcf', 'omnetpp', 'colocating with mcf' ]

siriusbenchList = [ 'gmm', 'dnn_asr', 'surf-fe', 'surf-fd', 'stem', 'regex', 'crf', 'img-imc', 'img-dig', 'img-face', 'nlp-pos', 'nlp-chk', 'nlp-ner']
siriuscolocationList = [ 'colocating with lbm', 'colocating with povray', 'colocating with astar', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
siriusrunningList = [ 'gmm', 'colocating with mcf', 'dnn_asr', 'colocating with mcf', 'surf-fe', 'colocating with mcf', 'surf-fd', 'colocating with mcf', 'stem', 'colocating with mcf', 'regex', 'colocating with mcf', 'crf', 'colocating with mcf', 'img-imc', 'colocating with mcf', 'img-dig', 'colocating with mcf', 'img-face', 'colocating with mcf', 'nlp-pos', 'colocating with mcf', 'nlp-chk', 'colocating with mcf', 'nlp-ner' , 'colocating with mcf']

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

def add_line(ax, xpos, ypos):
    line = plt.Line2D([xpos, xpos], [ypos + .1, ypos - .5], transform=ax.transAxes, linewidth=2, color='black')
    line.set_clip_on(False)
    ax.add_line(line)


filename = 'execution_time_1000'
fList1 = [s.strip() for s in open('../../papergraphs/accuracy/mcfcorunner/degradation/%s.txt' % filename).readlines()]  #degradation
fList2 = [s.strip() for s in open('../../papergraphs/accuracy/mcfcorunner/snapshot/phase_change_70.txt').readlines()]
fList3 = [s.strip() for s in open('../../papergraphs/accuracy/mcfcorunner/priorwork/execution_time_5.txt').readlines()] #prior work

fList4 = [s.strip() for s in open('../../papergraphs/accuracy/mcfcorunner/siriusdjinn/degradation/%s.txt' % filename).readlines()]  #degradation
fList5 = [s.strip() for s in open('../../papergraphs/accuracy/mcfcorunner/siriusdjinn/snapshot/phase_change_75.txt').readlines()]
fList6 = [s.strip() for s in open('../../papergraphs/accuracy/mcfcorunner/siriusdjinn/priorwork/execution_time_4.txt').readlines()] #prior work


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

mcfyaxis = ()
mcfyaxis2= ()
mcfyaxis_abs = ()
mcferror = ()
mcfxaxis = ()
#print dictList_phase_change2['colocating with mcf']['perlbench']
for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]
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
    mcfxaxis = mcfxaxis + (i,)
    #print (pause_period/np.mean(execution_time_sec_shutter[j][i]))*10
    mcfyaxis = mcfyaxis + ( (pause_period/np.mean(execution_time_sec_shutter[j][i]))*7.5  ,)
    mcfyaxis2 = mcfyaxis2 + ( abs(((np.mean(execution_time_sec_shutter2[j][i])/np.mean(execution_time_sec_shutter[j][i])) - 1)*100), )
    #print '---------------------'

#print yaxis2
#print np.mean(yaxis)


#width = 0.25
#x = np.arange(len(yaxis))
#fig = plt.figure(figsize=(28, 5))
#bar2 = plt.bar( x, yaxis2, width, color="k", label='Shuttering  (mean: %.2f)' %(np.mean(yaxis2)))
#bar1 = plt.bar( x+width, yaxis, width, color="lightgrey", label='Snapshot (mean: %.2f)' %(np.mean(yaxis) ))

#plt.ylabel( 'Execution time \n overhead(%)',fontsize=23)
##plt.title('Overhead due to Prediction of degradation while co-running with MCF')
#plt.xticks(x + width/2.0, xaxis, rotation='30', size='23', ha='center')
##plt.yticks((-5,0,10,20,30,40,50,60),('','0','10','20','30','40','50','60'),size='25')
#plt.yticks((0,5,10,15),('0','5','10','15'),size='25')
#plt.xlim(-1,27)
#plt.grid()
#plt.legend(loc=9, ncol=2, prop={'size':28})
#plt.tight_layout()
##plt.savefig('phase_chagnge_overheadmaybe.png', dpi=125)

del execution_time_shutter
del execution_time_sec_shutter
del avg_execution_time_shutter
del execution_time_shutter2
del execution_time_sec_shutter2
del avg_execution_time_shutter2
del dictList_phase_change
del dictList_phase_change2

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
    for j in siriuscolocationList:
        for i in siriusbenchList:
            print '%s ||||  %s'%(j,i)
            print time_shutter[j][i]


sep = 'u'
for (b,a) in enumerate(fList4):
    #print a
    if a in siriuscolocationList:
        index = a
    else:
        if a in siriusbenchList:
            execution_time_shutter[index][a].append((fList4[b+4].split('system '))[1].split('elapsed')[0])

#print execution_time_shutter['colocating with mcf']['perlbench']
#print((s.split(start))[1].split(end)[0])

for j in siriuscolocationList:
    for i in siriusbenchList:
        #print i
        for k in execution_time_shutter[j][i]:
            try:
                m,s = [float (var) for var in k.split(':')]
                temp = m*60 + s
            except:
                h,m,s = [float (var) for var in k.split(':')]
                temp = h*3600 + m*60 + s

            execution_time_sec_shutter[j][i].append(temp)

#print fList6
for (b,a) in enumerate(fList6):
    #print a
    if a in siriuscolocationList:
        index = a
    else:
        if a in siriusbenchList:
            #print index
            #print a
            #print fList6[b+4]
            execution_time_shutter2[index][a].append((fList6[b+4].split('system '))[1].split('elapsed')[0])

#print execution_time_shutter['colocating with mcf']['perlbench']
#print((s.split(start))[1].split(end)[0])

for j in siriuscolocationList:
    for i in siriusbenchList:
        for k in execution_time_shutter2[j][i]:
            #print k
            m,s = [float (var) for var in k.split(':')]
            temp = m*60 + s
            execution_time_sec_shutter2[j][i].append(temp)

for (b,a) in enumerate(fList5):
    if a in siriuscolocationList:
        index = a
    else:
        if a in siriusbenchList:
            dictList_phase_change[index][a].append(fList5[b+1])

for a in xrange(0,len(siriusrunningList),2):
    j = siriusrunningList[a+1]
    i = siriusrunningList[a]
    #print j,i
    for elem in dictList_phase_change[j][i]:
        dictList_phase_change2[j][i].extend(elem.strip().split('\t'))
    #print dictList_phase_change2[j][i]

mcfsiri_yaxis = ()
mcfsiri_yaxis2= ()
mcfsiri_yaxis_abs = ()
mcfsiri_error = ()
mcfsiri_xaxis = ()
#print dictList_phase_change2['colocating with mcf']['perlbench']
for a in xrange(0,len(siriusrunningList),2):
    j = siriusrunningList[a+1]
    i = siriusrunningList[a]
    print j,i
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
    mcfsiri_xaxis = mcfsiri_xaxis + (i,)
    #print (pause_period/np.mean(execution_time_sec_shutter[j][i]))*10
    mcfsiri_yaxis = mcfsiri_yaxis + ( (pause_period/np.mean(execution_time_sec_shutter[j][i]))*10  ,)
    mcfsiri_yaxis2 = mcfsiri_yaxis2 + ( abs(((np.mean(execution_time_sec_shutter2[j][i])/np.mean(execution_time_sec_shutter[j][i])) - 1)*100), )
    print execution_time_sec_shutter2[j][i]
    print execution_time_sec_shutter[j][i]
    #print np.mean(execution_time_sec_shutter2[j][i])
    #print np.mean(execution_time_sec_shutter[j][i])
    #print '---------------------'

#print xaxis
#print yaxis
#print yaxis2
#print np.mean(yaxis)

benchList = [ 'gcc', 'perlbench', 'leslie3d', 'povray', 'libquantum', 'astar', 'bzip2', 'milc', 'namd', 'calculix', 'h264ref', 'sphinx3', 'zeusmp', 'gobmk', 'hmmer', 'tonto', 'bwaves', 'gromacs', 'dealII', 'sjeng', 'lbm', 'xalancbmk', 'gamess', 'soplex', 'GemsFDTD', 'omnetpp', 'mcf', 'cactusADM' ]
colocationList = [ 'colocating with libquantum', 'colocating with mcf',  'colocating with milc']
colocationListBaseline = [ 'colocating with libquantum', 'colocating with mcf', 'colocating with milc' ]

runningList = [  'perlbench', 'colocating with milc', 'mcf', 'colocating with milc', 'leslie3d', 'colocating with milc', 'povray', 'colocating with milc', 'libquantum', 'colocating with milc', 'astar', 'colocating with milc', 'bzip2', 'colocating with milc', 'milc', 'colocating with milc', 'namd', 'colocating with milc', 'calculix', 'colocating with milc', 'h264ref', 'colocating with milc', 'gobmk', 'colocating with milc', 'hmmer', 'colocating with milc', 'tonto', 'colocating with milc', 'sphinx3', 'colocating with milc', 'zeusmp', 'colocating with milc', 'bwaves', 'colocating with milc', 'gromacs', 'colocating with milc', 'dealII', 'colocating with milc', 'sjeng', 'colocating with milc', 'lbm', 'colocating with milc', 'xalancbmk', 'colocating with milc', 'gamess', 'colocating with milc', 'cactusADM', 'colocating with milc', 'soplex', 'colocating with milc', 'GemsFDTD', 'colocating with milc', 'omnetpp', 'colocating with milc' ]

siriusbenchList = [ 'gmm', 'dnn_asr', 'surf-fe', 'surf-fd', 'stem', 'regex', 'crf', 'img-imc', 'img-dig', 'img-face', 'nlp-pos', 'nlp-chk', 'nlp-ner']
siriuscolocationList = [ 'colocating with milc', 'colocating with povray', 'colocating with astar', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
siriusrunningList = [ 'gmm', 'colocating with milc', 'dnn_asr', 'colocating with milc', 'surf-fe', 'colocating with milc', 'surf-fd', 'colocating with milc', 'stem', 'colocating with milc', 'regex', 'colocating with milc', 'crf', 'colocating with milc', 'img-imc', 'colocating with milc', 'img-dig', 'colocating with milc', 'img-face', 'colocating with milc', 'nlp-pos', 'colocating with milc', 'nlp-chk', 'colocating with milc', 'nlp-ner' , 'colocating with milc']
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

def add_line(ax, xpos, ypos):
    line = plt.Line2D([xpos, xpos], [ypos + .1, ypos - .5], transform=ax.transAxes, linewidth=2, color='black')
    line.set_clip_on(False)
    ax.add_line(line)

filename = 'execution_time_1000'
fList1 = [s.strip() for s in open('../../papergraphs/accuracy/milccorunner/degradation/%s.txt' % filename).readlines()]  #degradation
fList2 = [s.strip() for s in open('../../papergraphs/accuracy/milccorunner/snapshot/phase_change_70.txt').readlines()]
fList3 = [s.strip() for s in open('../../papergraphs/accuracy/milccorunner/priorwork/execution_time_5.txt').readlines()] #prior work

fList4 = [s.strip() for s in open('../../papergraphs/accuracy/milccorunner/siriusdjinn/degradation/%s.txt' % filename).readlines()]  #degradation
fList5 = [s.strip() for s in open('../../papergraphs/accuracy/milccorunner/siriusdjinn/snapshot/phase_change_75.txt').readlines()]
fList6 = [s.strip() for s in open('../../papergraphs/accuracy/milccorunner/siriusdjinn/priorwork/execution_time_4.txt').readlines()] #prior work

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

milcyaxis = ()
milcyaxis2= ()
milcyaxis_abs = ()
milcerror = ()
milcxaxis = ()
#print dictList_phase_change2['colocating with mcf']['perlbench']
for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]
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
    milcxaxis = milcxaxis + (i,)
    #print (pause_period/np.mean(execution_time_sec_shutter[j][i]))*10
    milcyaxis = milcyaxis + ( (pause_period/np.mean(execution_time_sec_shutter[j][i]))*7.5  ,)
    milcyaxis2 = milcyaxis2 + ( abs(((np.mean(execution_time_sec_shutter2[j][i])/np.mean(execution_time_sec_shutter[j][i])) - 1)*100), )
    #print '---------------------'

#print yaxis2
#print np.mean(yaxis)


#width = 0.25
#x = np.arange(len(yaxis))
#fig = plt.figure(figsize=(28, 5))
#bar2 = plt.bar( x, yaxis2, width, color="k", label='Shuttering  (mean: %.2f)' %(np.mean(yaxis2)))
#bar1 = plt.bar( x+width, yaxis, width, color="lightgrey", label='Snapshot (mean: %.2f)' %(np.mean(yaxis) ))
##bar3 = plt.bar( x+width+width, yaxis3, width, color="g", label=' colocating with sphinx3 (avg = %.1f)' %(np.mean(yaxis3)))
###bar3 = plt.bar( x+width+width, yaxis3, width, color="g", label='4 corunners (avg is %.1f)' %(np.mean(yaxis3) ))
###autolabel2(bar1)
###autolabel(bar2)
###autolabel2(bar3)
#plt.ylabel( 'Execution time \n overhead(%)',fontsize=23)
##plt.title('Overhead due to Prediction of degradation while co-running with milc')
#plt.xticks(x + width/2.0, xaxis, rotation='30', size='23', ha='center')
##plt.yticks((-5,0,10,20,30,40,50,60),('','0','10','20','30','40','50','60'),size='25')
#plt.yticks((0,5,10,15),('0','5','10','15'),size='25')
#plt.xlim(-1,27)
#plt.grid()
#plt.legend(loc=9, ncol=2, prop={'size':28})
#plt.tight_layout()
##plt.savefig('phase_chagnge_overheadmaybe.png', dpi=125)

del execution_time_shutter
del execution_time_sec_shutter
del avg_execution_time_shutter
del execution_time_shutter2
del execution_time_sec_shutter2
del avg_execution_time_shutter2
del dictList_phase_change
del dictList_phase_change2

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
    for j in siriuscolocationList:
        for i in siriusbenchList:
            print '%s ||||  %s'%(j,i)
            print time_shutter[j][i]


sep = 'u'
for (b,a) in enumerate(fList4):
    #print a
    if a in siriuscolocationList:
        index = a
    else:
        if a in siriusbenchList:
            execution_time_shutter[index][a].append((fList4[b+4].split('system '))[1].split('elapsed')[0])

#print execution_time_shutter['colocating with mcf']['perlbench']
#print((s.split(start))[1].split(end)[0])

for j in siriuscolocationList:
    for i in siriusbenchList:
        #print i
        for k in execution_time_shutter[j][i]:
            try:
                m,s = [float (var) for var in k.split(':')]
                temp = m*60 + s
            except:
                h,m,s = [float (var) for var in k.split(':')]
                temp = h*3600 + m*60 + s

            execution_time_sec_shutter[j][i].append(temp)

#print fList6
for (b,a) in enumerate(fList6):
    #print a
    if a in siriuscolocationList:
        index = a
    else:
        if a in siriusbenchList:
            print index
            print a
            print fList6[b+4]
            execution_time_shutter2[index][a].append((fList6[b+4].split('system '))[1].split('elapsed')[0])

#print execution_time_shutter['colocating with mcf']['perlbench']
#print((s.split(start))[1].split(end)[0])

for j in siriuscolocationList:
    for i in siriusbenchList:
        for k in execution_time_shutter2[j][i]:
            #print k
            m,s = [float (var) for var in k.split(':')]
            temp = m*60 + s
            execution_time_sec_shutter2[j][i].append(temp)

for (b,a) in enumerate(fList5):
    if a in siriuscolocationList:
        index = a
    else:
        if a in siriusbenchList:
            dictList_phase_change[index][a].append(fList5[b+1])

for a in xrange(0,len(siriusrunningList),2):
    j = siriusrunningList[a+1]
    i = siriusrunningList[a]
    #print j,i
    for elem in dictList_phase_change[j][i]:
        dictList_phase_change2[j][i].extend(elem.strip().split('\t'))
    #print dictList_phase_change2[j][i]

milcsiri_yaxis = ()
milcsiri_yaxis2= ()
milcsiri_yaxis_abs = ()
milcsiri_error = ()
milcsiri_xaxis = ()
#print dictList_phase_change2['colocating with mcf']['perlbench']
for a in xrange(0,len(siriusrunningList),2):
    j = siriusrunningList[a+1]
    i = siriusrunningList[a]
    print j,i
    #print dictList_phase_change2[j][i]
    shutter_temp_list = []
    colo_temp_list = []
    for (count,item) in enumerate(dictList_phase_change2[j][i]):
        if count%2==1:
            colo_temp_list.append(float(item))
        if count%2==0:
            shutter_temp_list.append(float(item))
    #print shutter_temp_list
    #print colo_temp_list
    shutter_avg = sum(shutter_temp_list)/len(shutter_temp_list)
    colocation_avg = sum(colo_temp_list)/len(colo_temp_list)
    del shutter_temp_list
    del colo_temp_list

    pause_period = ((colocation_avg ) + ((shutter_avg + (colocation_avg * 2)/3) * 3))/4
    milcsiri_xaxis = milcsiri_xaxis + (i,)
    #print (pause_period/np.mean(execution_time_sec_shutter[j][i]))*10
    milcsiri_yaxis = milcsiri_yaxis + ( (pause_period/np.mean(execution_time_sec_shutter[j][i]))*10  ,)
    milcsiri_yaxis2 = milcsiri_yaxis2 + ( abs(((np.mean(execution_time_sec_shutter2[j][i])/np.mean(execution_time_sec_shutter[j][i])) - 1)*100), )
    print execution_time_sec_shutter2[j][i]
    print execution_time_sec_shutter[j][i]
    #print np.mean(execution_time_sec_shutter2[j][i])
    #print np.mean(execution_time_sec_shutter[j][i])
    #print '---------------------'

#print xaxis
#print yaxis
#print yaxis2
#print np.mean(yaxis)

benchList = [ 'gcc', 'perlbench', 'leslie3d', 'povray', 'libquantum', 'astar', 'bzip2', 'milc', 'namd', 'calculix', 'h264ref', 'sphinx3', 'zeusmp', 'gobmk', 'hmmer', 'tonto', 'bwaves', 'gromacs', 'dealII', 'sjeng', 'lbm', 'xalancbmk', 'gamess', 'soplex', 'GemsFDTD', 'omnetpp', 'mcf', 'cactusADM' ]

colocationList = [ 'colocating with libquantum', 'colocating with mcf',  'colocating with milc']
colocationListBaseline = [ 'colocating with libquantum', 'colocating with mcf', 'colocating with milc' ]

runningList = [  'perlbench', 'colocating with milc', 'mcf', 'colocating with milc', 'leslie3d', 'colocating with milc', 'povray', 'colocating with milc', 'libquantum', 'colocating with milc', 'astar', 'colocating with milc', 'bzip2', 'colocating with milc', 'milc', 'colocating with milc', 'namd', 'colocating with milc', 'calculix', 'colocating with milc', 'h264ref', 'colocating with milc', 'gobmk', 'colocating with milc', 'hmmer', 'colocating with milc', 'tonto', 'colocating with milc', 'sphinx3', 'colocating with milc', 'zeusmp', 'colocating with milc',    'bwaves', 'colocating with milc', 'gromacs', 'colocating with milc', 'dealII', 'colocating with milc', 'sjeng', 'colocating with milc', 'lbm', 'colocating with milc', 'xalancbmk', 'colocating with milc', 'gamess', 'colocating with milc', 'cactusADM', 'colocating with milc', 'soplex', 'colocating with milc', 'GemsFDTD', 'colocating with milc', 'omnetpp', 'colocating with milc' ]
runningList2 = [  'leslie3d', 'colocating with milc', 'milc', 'colocating with milc', 'namd', 'colocating with milc', 'calculix', 'colocating with milc', 'gobmk', 'colocating with milc', 'hmmer', 'colocating with milc', 'tonto', 'colocating with milc', 'sphinx3', 'colocating with milc', 'zeusmp', 'colocating with milc', 'bwaves', 'colocating with milc', 'gromacs', 'colocating with milc', 'dealII', 'colocating with milc', 'sjeng', 'colocating with milc', 'gamess', 'colocating with milc', 'cactusADM', 'colocating with milc', 'soplex', 'colocating with milc', 'GemsFDTD', 'colocating with milc' ]
runningList3 = [  'perlbench', 'colocating with milc', 'mcf', 'colocating with milc', 'povray', 'colocating with milc', 'libquantum', 'colocating with milc', 'astar', 'colocating with milc', 'bzip2', 'colocating with milc', 'h264ref', 'colocating with milc',  'lbm', 'colocating with milc', 'xalancbmk', 'colocating with milc', 'omnetpp', 'colocating with milc' ]

siriusbenchList = [ 'gmm', 'dnn_asr', 'surf-fe', 'surf-fd', 'stem', 'regex', 'crf', 'img-imc', 'img-dig', 'img-face', 'nlp-pos', 'nlp-chk', 'nlp-ner']
siriuscolocationList = [ 'colocating with lbm', 'colocating with povray', 'colocating with astar', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
siriusrunningList = [ 'gmm', 'colocating with libquantum', 'dnn_asr', 'colocating with libquantum', 'surf-fe', 'colocating with libquantum', 'surf-fd', 'colocating with libquantum', 'stem', 'colocating with libquantum', 'regex', 'colocating with libquantum', 'crf', 'colocating with libquantum', 'img-imc', 'colocating with libquantum', 'img-dig', 'colocating with libquantum', 'img-face', 'colocating with libquantum', 'nlp-pos', 'colocating with libquantum', 'nlp-chk', 'colocating with libquantum', 'nlp-ner' , 'colocating with libquantum']

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

def add_line(ax, xpos, ypos):
    line = plt.Line2D([xpos, xpos], [ypos + .1, ypos - .5], transform=ax.transAxes, linewidth=2, color='black')
    line.set_clip_on(False)
    ax.add_line(line)


filename = 'execution_time_1000'
fList1 = [s.strip() for s in open('../../papergraphs/mixcorunner/degradation/%s.txt' % filename).readlines()]  #degradation
fList2 = [s.strip() for s in open('../../papergraphs/mixcorunner/snapshot/phase_change_10.txt').readlines()]
fList3 = [s.strip() for s in open('../../papergraphs/mixcorunner/priorwork/execution_time_4.txt').readlines()] #prior work
fList4 = [s.strip() for s in open('../../papergraphs/mixcorunner/degradation/execution_time_100.txt').readlines()]  #degradation

fList7 = [s.strip() for s in open('../../papergraphs/mixcorunner/siriusdjinn/degradation/%s.txt' % filename).readlines()]  #degradation
fList5 = [s.strip() for s in open('../../papergraphs/mixcorunner/siriusdjinn/snapshot/phase_change_75.txt').readlines()]
fList6 = [s.strip() for s in open('../../papergraphs/mixcorunner/siriusdjinn/priorwork/execution_time_4.txt').readlines()] #prior work

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

mixyaxis = ()
mixyaxis2= ()
mixyaxis_abs = ()
mixerror = ()
mixxaxis = ()
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
    mixxaxis = mixxaxis + (i,)
    mixyaxis = mixyaxis + ( overhead_snapshot[j][i]  ,)
    mixyaxis2 = mixyaxis2 + ( overhead_shutter[j][i], )

#print yaxis
#print yaxis2


#width = 0.25
#x = np.arange(len(yaxis))
#fig = plt.figure(figsize=(28, 5))
#bar2 = plt.bar( x, yaxis2, width, color="k", label='Shuttering  (mean: %.2f)' %(np.mean(yaxis2)))
#bar1 = plt.bar( x+width, yaxis, width, color="lightgrey", label='Snapshot (mean: %.2f)' %(np.mean(yaxis) ))
##bar3 = plt.bar( x+width+width, yaxis3, width, color="g", label=' colocating with sphinx3 (avg = %.1f)' %(np.mean(yaxis3)))
###bar3 = plt.bar( x+width+width, yaxis3, width, color="g", label='4 corunners (avg is %.1f)' %(np.mean(yaxis3) ))
###autolabel2(bar1)
###autolabel(bar2)
###autolabel2(bar3)
#plt.ylabel( 'Execution time \n overhead(%)',fontsize=23)
##plt.title('Overhead due to Prediction of degradation while co-running with milc')
#plt.xticks(x + width/2.0, xaxis, rotation='30', size='23', ha='center')
##plt.yticks((-5,0,10,20,30,40,50,60),('','0','10','20','30','40','50','60'),size='25')
#plt.yticks((0,5,10,15),('0','5','10','15'),size='25')
#plt.xlim(-1,27)
#plt.grid()
#plt.legend(loc=9, ncol=2, prop={'size':28})
#plt.tight_layout()
##plt.savefig('milc_overhead.pdf', dpi=125)

del execution_time_shutter
del execution_time_sec_shutter
del avg_execution_time_shutter
del execution_time_shutter2
del execution_time_sec_shutter2
del avg_execution_time_shutter2
del dictList_phase_change
del dictList_phase_change2

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
    for j in siriuscolocationList:
        for i in siriusbenchList:
            print '%s ||||  %s'%(j,i)
            print time_shutter[j][i]


sep = 'u'
for (b,a) in enumerate(fList7):
    #print a
    if a in siriuscolocationList:
        index = a
    else:
        if a in siriusbenchList:
            #print a
            #print fList7[b+4]
            execution_time_shutter[index][a].append((fList7[b+4].split('system '))[1].split('elapsed')[0])

#print execution_time_shutter['colocating with mcf']['perlbench']
#print((s.split(start))[1].split(end)[0])

for j in siriuscolocationList:
    for i in siriusbenchList:
        #print i
        for k in execution_time_shutter[j][i]:
            try:
                m,s = [float (var) for var in k.split(':')]
                temp = m*60 + s
            except:
                h,m,s = [float (var) for var in k.split(':')]
                temp = h*3600 + m*60 + s

            execution_time_sec_shutter[j][i].append(temp)

for (b,a) in enumerate(fList6):
    #print a
    if a in siriuscolocationList:
        index = a
    else:
        if a in siriusbenchList:
            #print index
            #print a
            execution_time_shutter2[index][a].append((fList6[b+4].split('system '))[1].split('elapsed')[0])

#print execution_time_shutter['colocating with mcf']['perlbench']
#print((s.split(start))[1].split(end)[0])

for j in siriuscolocationList:
    for i in siriusbenchList:
        for k in execution_time_shutter2[j][i]:
            #print k
            m,s = [float (var) for var in k.split(':')]
            temp = m*60 + s
            execution_time_sec_shutter2[j][i].append(temp)

for (b,a) in enumerate(fList5):
    if a in siriuscolocationList:
        index = a
    else:
        if a in siriusbenchList:
            dictList_phase_change[index][a].append(fList5[b+1])

mixsiri_yaxis = ()
mixsiri_yaxis2= ()
mixsiri_yaxis_abs = ()
mixsiri_error = ()
mixsiri_xaxis = ()
for a in xrange(0,len(siriusrunningList),2):
    j = siriusrunningList[a+1]
    i = siriusrunningList[a]
    #print j,i
    for elem in dictList_phase_change[j][i]:
        dictList_phase_change2[j][i].extend(elem.strip().split('\t'))
    #print dictList_phase_change2[j][i]

#print dictList_phase_change2['colocating with mcf']['perlbench']
for a in xrange(0,len(siriusrunningList),2):
    j = siriusrunningList[a+1]
    i = siriusrunningList[a]
    print j,i
    #print dictList_phase_change2[j][i]
    #print i,j
    shutter_temp_list = []
    colo_temp_list = []
    for (count,item) in enumerate(dictList_phase_change2[j][i]):
        if count%2==1:
            colo_temp_list.append(float(item))
        if count%2==0:
            shutter_temp_list.append(float(item))
    print shutter_temp_list
    print colo_temp_list
    shutter_avg = sum(shutter_temp_list)/len(shutter_temp_list)
    colocation_avg = sum(colo_temp_list)/len(colo_temp_list)
    del shutter_temp_list
    del colo_temp_list

    pause_period = ((colocation_avg ) + ((shutter_avg + (colocation_avg * 2)/3) * 3))/4
    mixsiri_xaxis = mixsiri_xaxis + (i,)
    #print (pause_period/np.mean(execution_time_sec_shutter[j][i]))*10
    mixsiri_yaxis = mixsiri_yaxis + ( (pause_period/np.mean(execution_time_sec_shutter[j][i]))*10  ,)
    mixsiri_yaxis2 = mixsiri_yaxis2 + ( abs(((np.mean(execution_time_sec_shutter2[j][i])/np.mean(execution_time_sec_shutter[j][i])) - 1)*100), )
    #print np.mean(execution_time_sec_shutter2[j][i])
    #print np.mean(execution_time_sec_shutter[j][i])
    #print '---------------------'

#print xaxis
#print yaxis
#print yaxis2
#print np.mean(yaxis)



width = 0.15
x = np.arange(len(mixyaxis))
fig = plt.figure(figsize=(23, 5))
ax = fig.add_subplot(1,1,1)
#bar2 = plt.bar( x, libsiri_yaxis2, width, color="r", label='libquantum (avg = %.2f)' %(np.mean(libsiri_yaxis2)))
bar1 = plt.bar( x, libyaxis, width, color="y", label='libquantum (avg = %.2f)' %(np.mean(libyaxis) ))
bar2 = plt.bar( x+width, mcfyaxis, width, color="r", label='mcf (avg = %.2f)' %(np.mean(mcfyaxis) ))
bar4 = plt.bar( x+width+width, milcyaxis, width, color="b", label='milc (avg = %.2f)' %(np.mean(milcyaxis) ))
bar4 = plt.bar( x+width+width+width, mixyaxis, width, color="g", label='mix (avg = %.2f)' %(np.mean(mixyaxis) ))
#ly = len(mixyaxis2)
#add_line(ax, 0 * 1, -.1)
#add_line(ax, 1 * 1.0, -.1)
#add_line(ax, 1 * 0.55, -.1)
#add_line(ax, 1 * 0.845, -.1)
#bar3 = plt.bar( x+width+width, yaxis3, width, color="g", label=' colocating with sphinx3 (avg = %.1f)' %(np.mean(yaxis3)))
##bar3 = plt.bar( x+width+width, yaxis3, width, color="g", label='4 corunners (avg is %.1f)' %(np.mean(yaxis3) ))
##autolabel2(bar1)
##autolabel(bar2)
##autolabel2(bar3)
plt.ylabel( 'Execution time \n overhead(%)', fontsize='19' )
#plt.title('Overhead due to Prediction of degradation while co-running with LIBQUANTUM')
plt.xticks(x + width/2.0, mixxaxis, rotation='90', size='18', ha='center')
plt.ylim(0,20)
plt.xlim(-1,26)
plt.yticks(np.arange(0,25,5),size='20')
plt.grid()
plt.legend(loc=1, ncol=4, prop={'size':18})
plt.tight_layout()
#plt.savefig('overheadlibquantum.pdf', dpi=125)

#ax.text(10, -10, r'SPEC 2006', fontsize=20)
#ax.text(3, -10, r'Sirius Suite', fontsize=20)
#ax.text(8, -10, r'DjiNN & Tonic', fontsize=20)

import os as mars_awesome_os;
import matplotlib.pyplot as mars_awesome_plt;
mars_awesome_plt.savefig('spec-overhead.eps', bbox_inches='tight');
mars_awesome_os.popen('epstopdf spec-overhead.eps');
