from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt


benchList = [ 'gcc', 'perlbench', 'leslie3d', 'povray', 'libquantum', 'astar', 'bzip2', 'milc', 'namd', 'calculix', 'h264ref', 'sphinx3', 'zeusmp', 'gobmk', 'hmmer', 'tonto', 'bwaves', 'gromacs', 'dealII', 'sjeng', 'lbm', 'xalancbmk', 'gamess', 'soplex', 'GemsFDTD', 'omnetpp', 'mcf', 'cactusADM' ]

colocationList = [ 'colocating with libquantum', 'colocating with mcf',  'colocating with sphinx3']
colocationListBaseline = [ 'colocating with libquantum', 'colocating with mcf', 'colocating with sphinx3' ]


runningList = [  'perlbench', 'colocating with libquantum', 'mcf', 'colocating with libquantum', 'leslie3d', 'colocating with libquantum', 'povray', 'colocating with libquantum', 'libquantum', 'colocating with libquantum', 'astar', 'colocating with libquantum', 'milc', 'colocating with libquantum', 'namd', 'colocating with libquantum', 'calculix', 'colocating with libquantum', 'h264ref', 'colocating with libquantum', 'gobmk', 'colocating with libquantum', 'hmmer', 'colocating with libquantum', 'tonto', 'colocating with libquantum', 'sphinx3', 'colocating with libquantum', 'zeusmp', 'colocating with libquantum', 'bwaves', 'colocating with libquantum', 'gromacs', 'colocating with libquantum', 'dealII', 'colocating with libquantum', 'sjeng', 'colocating with libquantum', 'lbm', 'colocating with libquantum', 'xalancbmk', 'colocating with libquantum', 'gamess', 'colocating with libquantum', 'cactusADM', 'colocating with libquantum', 'soplex', 'colocating with libquantum', 'omnetpp', 'colocating with libquantum' ]

siriusbenchList = [ 'gmm', 'dnn_asr', 'surf-fe', 'surf-fd', 'stem', 'regex', 'crf', 'img-imc', 'img-dig', 'img-face', 'nlp-pos', 'nlp-chk', 'nlp-ner']
siriuscolocationList = [ 'colocating with lbm', 'colocating with povray', 'colocating with astar', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with libquantum' ]
siriusrunningList = [ 'gmm', 'colocating with libquantum', 'surf-fe', 'colocating with libquantum', 'surf-fd', 'colocating with libquantum', 'stem', 'colocating with libquantum', 'regex', 'colocating with libquantum', 'crf', 'colocating with libquantum', 'img-imc', 'colocating with libquantum', 'img-dig', 'colocating with libquantum', 'img-face', 'colocating with libquantum', 'nlp-pos', 'colocating with libquantum', 'nlp-chk', 'colocating with libquantum', 'nlp-ner' , 'colocating with libquantum']

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
fList1 = [s.strip() for s in open('../../papergraphs/scalability/libquantumcorunner/spec/degradation/%s.txt' % filename).readlines()]  #degradation
fList2 = [s.strip() for s in open('../../papergraphs/scalability/libquantumcorunner/spec/snapshot/phase_change_10.txt').readlines()]
fList3 = [s.strip() for s in open('../../papergraphs/scalability/libquantumcorunner/spec/priorwork/execution_time_4.txt').readlines()] #prior work

fList4 = [s.strip() for s in open('../../papergraphs/scalability/libquantumcorunner/siriusdjinn/degradation/%s.txt' % filename).readlines()]  #degradation
fList5 = [s.strip() for s in open('../../papergraphs/scalability/libquantumcorunner/siriusdjinn/snapshot/phase_change_10.txt').readlines()]
fList6 = [s.strip() for s in open('../../papergraphs/scalability/libquantumcorunner/siriusdjinn/priorwork/execution_time_4.txt').readlines()] #prior work

yaxis = ()
yaxis2= ()
yaxis_abs = ()
error = ()
xaxis = ()
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
    print a
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
    xaxis = xaxis + (i,)
    #print (pause_period/np.mean(execution_time_sec_shutter[j][i]))*10
    yaxis = yaxis + ( (pause_period/np.mean(execution_time_sec_shutter[j][i]))*10  ,)
    yaxis2 = yaxis2 + ( abs(((np.mean(execution_time_sec_shutter2[j][i])/np.mean(execution_time_sec_shutter[j][i])) - 1)*100), )
    print execution_time_sec_shutter2[j][i]
    print execution_time_sec_shutter[j][i]
    #print np.mean(execution_time_sec_shutter2[j][i])
    #print np.mean(execution_time_sec_shutter[j][i])
    #print '---------------------'

#print xaxis
#print yaxis
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
            try:
                m,s = [float (var) for var in k.split(':')]
                temp = m*60 + s
            except:
                h,m,s = [float (var) for var in k.split(':')]
                temp = h*3600 + m*60 + s
            #print k
            execution_time_sec_shutter2[j][i].append(temp)

for (b,a) in enumerate(fList2):
    #print a
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
    xaxis = xaxis + (i,)
    #print (pause_period/np.mean(execution_time_sec_shutter[j][i]))*10
    yaxis = yaxis + ( (pause_period/np.mean(execution_time_sec_shutter[j][i]))*7.5  ,)
    yaxis2 = yaxis2 + ( abs(((np.mean(execution_time_sec_shutter2[j][i])/np.mean(execution_time_sec_shutter[j][i])) - 1)*100), )
    #print '---------------------'

#print yaxis2
#print np.mean(yaxis)

width = 0.25
x = np.arange(len(yaxis))
fig = plt.figure(figsize=(25, 5))
ax = fig.add_subplot(1,1,1)
bar2 = plt.bar( x, yaxis2, width, color="r", label='Shuttering  (avg = %.2f)' %(np.mean(yaxis2)))
bar1 = plt.bar( x+width, yaxis, width, color="y", label='Snapshot(avg = %.2f)' %(np.mean(yaxis) ))
ly = len(yaxis2)
add_line(ax, 0 * 1, -.1)
add_line(ax, 1 * 1.0, -.1)
add_line(ax, 1 * 0.175, -.1)
add_line(ax, 1 * 0.335, -.1)
#bar3 = plt.bar( x+width+width, yaxis3, width, color="g", label=' colocating with sphinx3 (avg = %.1f)' %(np.mean(yaxis3)))
##bar3 = plt.bar( x+width+width, yaxis3, width, color="g", label='4 corunners (avg is %.1f)' %(np.mean(yaxis3) ))
##autolabel2(bar1)
##autolabel(bar2)
##autolabel2(bar3)
plt.ylabel( 'Execution time \n overhead(%)', fontsize='19' )
#plt.title('Overhead due to Prediction of degradation while co-running with LIBQUANTUM')
plt.xticks(x + width/2.0, xaxis, rotation='90', size='18', ha='center')
plt.ylim(0,50)
plt.xlim(-1,37)
plt.yticks(np.arange(0,55,10),size='20')
plt.grid()
plt.legend(loc=1, ncol=2, prop={'size':18})
plt.tight_layout()
#plt.savefig('overheadlibquantum.pdf', dpi=125)
ax.text(24, -25, r'SPEC 2006', fontsize=20)
ax.text(1, -25, r'Sirius Suite', fontsize=20)
ax.text(7, -25, r'DjiNN & Tonic', fontsize=20)

import os as mars_awesome_os;
import matplotlib.pyplot as mars_awesome_plt;
mars_awesome_plt.savefig('overhead-comparison.eps', bbox_inches='tight');
mars_awesome_os.popen('epstopdf overhead-comparison.eps');
