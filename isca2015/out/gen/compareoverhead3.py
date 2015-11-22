from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt


benchList = [ 'milc', 'mcf', 'astar', 'lbm', 'libquantum' ]
benchList2 = [ 'milc', 'mcf', 'astar', 'lbm', 'libquantum' ]
#benchList2 = [ 'gcc', 'mcf', 'perlbench', 'astar', 'libquantum', 'povray', 'bzip2' ]
colocationList = [ 'colocating with libquantum' ]
colocationListBaseline = [ 'colocating with libquantum' ]
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


filename = 'execution_time_4'
fList1 = [s.strip() for s in open('../../papergraphs/3.compareprior/overhead/shuttering/prior_work_new/2_vm/%s.txt' % filename).readlines()]
fList2 = [s.strip() for s in open('../../papergraphs/3.compareprior/overhead/shuttering/2_degradation_ground_truth/execution_time_1000.txt').readlines()]
fList3 = [s.strip() for s in open('../../papergraphs/3.compareprior/overhead/shuttering/prior_work_new/3_vm/%s.txt' % filename).readlines()]
fList4 = [s.strip() for s in open('../../papergraphs/3.compareprior/overhead/shuttering/3_degradation_ground_truth/execution_time_1000.txt').readlines()]
fList5 = [s.strip() for s in open('../../papergraphs/3.compareprior/overhead/shuttering/prior_work_new/4_vm/%s.txt' % filename).readlines()]
fList6 = [s.strip() for s in open('../../papergraphs/3.compareprior/overhead/shuttering/degradation_ground_truth/execution_time_1000.txt').readlines()]
#print fList1


execution_time_shutter = defaultdict(lambda  : defaultdict(list))
execution_time_sec_shutter = defaultdict(lambda  : defaultdict(list))
avg_execution_time_shutter = defaultdict(dict)

execution_time_baseline = defaultdict(lambda  : defaultdict(list))
execution_time_sec_baseline = defaultdict(lambda  : defaultdict(list))
avg_execution_time_baseline = defaultdict(dict)

std_execution_time = defaultdict(dict)

def print_elapsed_time_shutter(time_shutter):
    for j in colocationList:
        for i in benchList:
            print '%s ||||  %s'%(j,i)
            print time_shutter[j][i]


def print_elapsed_time_baseline(time_baseline):
    for j in colocationListBaseline:
        for i in benchList:
            print '%s ||||  %s'%(j,i)
            print time_baseline[j][i]

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

for (b,a) in enumerate(fList2):
    if a in colocationListBaseline:
        #print a,'1'
        index = a
    else:
        if a in benchList:
            #print a,'2'
            #print index,a
            #execution_time2[index][a].append(fList2[b+4].split('u',1)[0])
            execution_time_baseline[index][a].append((fList2[b+4].split('system '))[1].split('elapsed')[0])

#print execution_time_baseline['colocating with mcf']['perlbench']
#### PRINT EXECUTION TIME IN MINUTES ###########
#print_elapsed_time_shutter(execution_time_shutter)
#print '***********************************************'
#print_elapsed_time_baseline(execution_time_baseline)

for j in colocationList:
    for i in benchList:
        for k in execution_time_shutter[j][i]:
            m,s = [float (var) for var in k.split(':')]
            temp = m*60 + s
            execution_time_sec_shutter[j][i].append(temp)

for j in colocationListBaseline:
    for i in benchList:
        for k in execution_time_baseline[j][i]:
            m,s = [float (var) for var in k.split(':')]
            temp = m*60 + s
            execution_time_sec_baseline[j][i].append(temp)


xaxis = ()
yaxis = ()
error = ()
xaxis2 = ()
yaxis2 = ()
error2 = ()
xaxis3 = ()
yaxis3 = ()
error3 = ()

for j in colocationList:
    for i in benchList:
        if len(execution_time_sec_shutter[j][i]) != 0:
            #print j,i
            temp_list = []
            for item in execution_time_sec_shutter[j][i]:
                temp_list.append(item)
            temp_list.sort()
            del temp_list[len(temp_list)-1]
            del temp_list[0]
            avg_execution_time_shutter[j][i] = np.mean(temp_list)
            del temp_list
            #print avg_execution_time_shutter[j][i]

#print '*************************'

for j in colocationListBaseline:
    for i in benchList:
        if len(execution_time_sec_baseline[j][i]) != 0:
            #print j,i
            avg_execution_time_baseline[j][i] = np.mean(execution_time_sec_baseline[j][i])
            #print avg_execution_time_baseline[j][i]

for j in colocationList:
    for i in benchList2:
        if len(execution_time_sec_shutter[j][i]) != 0:
            if j == 'colocating with libquantum':
                yaxis = yaxis + ( abs(((avg_execution_time_shutter[j][i] - avg_execution_time_baseline[j][i])/avg_execution_time_baseline[j][i])*100), )
                temp = ( ((avg_execution_time_shutter[j][i] - avg_execution_time_baseline[j][i])/avg_execution_time_baseline[j][i])*100, )
                print j,i,( ((avg_execution_time_shutter[j][i] - avg_execution_time_baseline[j][i])/avg_execution_time_baseline[j][i])*100, )

for i in benchList:
    xaxis = xaxis +(i,)
width = 0.25       # the width of the bars


del execution_time_shutter
del execution_time_sec_shutter
del avg_execution_time_shutter
del execution_time_baseline
del execution_time_sec_baseline
del avg_execution_time_baseline
del std_execution_time


execution_time_shutter = defaultdict(lambda  : defaultdict(list))
execution_time_sec_shutter = defaultdict(lambda  : defaultdict(list))
avg_execution_time_shutter = defaultdict(dict)

execution_time_baseline = defaultdict(lambda  : defaultdict(list))
execution_time_sec_baseline = defaultdict(lambda  : defaultdict(list))
avg_execution_time_baseline = defaultdict(dict)

std_execution_time = defaultdict(dict)


sep = 'u'
for (b,a) in enumerate(fList3):
    #print a
    if a in colocationList:
        index = a
    else:
        if a in benchList:
            execution_time_shutter[index][a].append((fList3[b+4].split('system '))[1].split('elapsed')[0])

#print execution_time_shutter['colocating with mcf']['perlbench']
#print((s.split(start))[1].split(end)[0])

for (b,a) in enumerate(fList4):
    if a in colocationListBaseline:
        #print a,'1'
        index = a
    else:
        if a in benchList:
            #print a,'2'
            #print index,a
            #execution_time2[index][a].append(fList2[b+4].split('u',1)[0])
            execution_time_baseline[index][a].append((fList4[b+4].split('system '))[1].split('elapsed')[0])

#print execution_time_baseline['colocating with mcf']['perlbench']
#### PRINT EXECUTION TIME IN MINUTES ###########
#print_elapsed_time_shutter(execution_time_shutter)
#print '***********************************************'
#print_elapsed_time_baseline(execution_time_baseline)

for j in colocationList:
    for i in benchList:
        for k in execution_time_shutter[j][i]:
            m,s = [float (var) for var in k.split(':')]
            temp = m*60 + s
            execution_time_sec_shutter[j][i].append(temp)

for j in colocationListBaseline:
    for i in benchList:
        for k in execution_time_baseline[j][i]:
            m,s = [float (var) for var in k.split(':')]
            temp = m*60 + s
            execution_time_sec_baseline[j][i].append(temp)

for j in colocationList:
    for i in benchList:
        if len(execution_time_sec_shutter[j][i]) != 0:
            #print j,i
            temp_list = []
            for item in execution_time_sec_shutter[j][i]:
                temp_list.append(item)
            temp_list.sort()
            del temp_list[len(temp_list)-1]
            del temp_list[0]
            avg_execution_time_shutter[j][i] = np.mean(temp_list)
            del temp_list
            #print avg_execution_time_shutter[j][i]

#print '*************************'

for j in colocationListBaseline:
    for i in benchList:
        if len(execution_time_sec_baseline[j][i]) != 0:
            avg_execution_time_baseline[j][i] = np.min(execution_time_sec_baseline[j][i])

for j in colocationList:
    for i in benchList2:
        if len(execution_time_sec_shutter[j][i]) != 0:
            if j == 'colocating with libquantum':
                yaxis2 = yaxis2 + ( abs(((avg_execution_time_shutter[j][i] - avg_execution_time_baseline[j][i])/avg_execution_time_baseline[j][i])*100), )
                temp = ( ((avg_execution_time_shutter[j][i] - avg_execution_time_baseline[j][i])/avg_execution_time_baseline[j][i])*100, )
                print j,i,( abs(((avg_execution_time_shutter[j][i] - avg_execution_time_baseline[j][i])/avg_execution_time_baseline[j][i])*100), )


del execution_time_shutter
del execution_time_sec_shutter
del avg_execution_time_shutter
del execution_time_baseline
del execution_time_sec_baseline
del avg_execution_time_baseline
del std_execution_time


execution_time_shutter = defaultdict(lambda  : defaultdict(list))
execution_time_sec_shutter = defaultdict(lambda  : defaultdict(list))
avg_execution_time_shutter = defaultdict(dict)

execution_time_baseline = defaultdict(lambda  : defaultdict(list))
execution_time_sec_baseline = defaultdict(lambda  : defaultdict(list))
avg_execution_time_baseline = defaultdict(dict)

std_execution_time = defaultdict(dict)


sep = 'u'
for (b,a) in enumerate(fList5):
    #print a
    if a in colocationList:
        index = a
    else:
        if a in benchList:
            execution_time_shutter[index][a].append((fList5[b+4].split('system '))[1].split('elapsed')[0])

#print execution_time_shutter['colocating with mcf']['perlbench']
#print((s.split(start))[1].split(end)[0])

for (b,a) in enumerate(fList6):
    if a in colocationListBaseline:
        #print a,'1'
        index = a
    else:
        if a in benchList:
            #print a,'2'
            #print index,a
            #execution_time2[index][a].append(fList2[b+4].split('u',1)[0])
            execution_time_baseline[index][a].append((fList6[b+4].split('system '))[1].split('elapsed')[0])

#print execution_time_baseline['colocating with mcf']['perlbench']
#### PRINT EXECUTION TIME IN MINUTES ###########
#print_elapsed_time_shutter(execution_time_shutter)
#print '***********************************************'
#print_elapsed_time_baseline(execution_time_baseline)

for j in colocationList:
    for i in benchList:
        for k in execution_time_shutter[j][i]:
            m,s = [float (var) for var in k.split(':')]
            temp = m*60 + s
            execution_time_sec_shutter[j][i].append(temp)

for j in colocationListBaseline:
    for i in benchList:
        for k in execution_time_baseline[j][i]:
            m,s = [float (var) for var in k.split(':')]
            temp = m*60 + s
            execution_time_sec_baseline[j][i].append(temp)

for j in colocationList:
    for i in benchList:
        if len(execution_time_sec_shutter[j][i]) != 0:
            #print j,i
            temp_list = []
            for item in execution_time_sec_shutter[j][i]:
                temp_list.append(item)
            temp_list.sort()
            del temp_list[len(temp_list)-1]
            del temp_list[0]
            avg_execution_time_shutter[j][i] = np.mean(temp_list)
            del temp_list
            #print avg_execution_time_shutter[j][i]

#print '*************************'

for j in colocationListBaseline:
    for i in benchList:
        if len(execution_time_sec_baseline[j][i]) != 0:
            avg_execution_time_baseline[j][i] = np.min(execution_time_sec_baseline[j][i])

for j in colocationList:
    for i in benchList2:
        if len(execution_time_sec_shutter[j][i]) != 0:
            if j == 'colocating with libquantum':
                yaxis3 = yaxis3 + ( abs(((avg_execution_time_shutter[j][i] - avg_execution_time_baseline[j][i])/avg_execution_time_baseline[j][i])*100), )
                temp = ( ((avg_execution_time_shutter[j][i] - avg_execution_time_baseline[j][i])/avg_execution_time_baseline[j][i])*100, )
                print j,i,( abs(((avg_execution_time_shutter[j][i] - avg_execution_time_baseline[j][i])/avg_execution_time_baseline[j][i])*100), )

#rects = plt.bar(np.arange(len(yaxis)), yaxis, width, color='r', label='blah')
#plt.xticks( np.arange(len(yaxis)) + width/2.0, xaxis, rotation='45' )
#autolabel(rects)
#plt.ylabel('Percentage')
#plt.title('Percentage Degradation in the execution time due to shuttering mechanism \n for colocation time 2s shutter time 15ms')
#plt.savefig('error.png', dpi=120, bbox_inches='tight')

#print np.mean(yaxis3)

x = np.arange(len(yaxis))
fig = plt.figure(figsize=(10, 5))
bar1 = plt.bar( x, yaxis, width, color="r", label='2 corunners (avg is %.1f) ' %(np.mean(yaxis) ))
bar2 = plt.bar( x+width, yaxis2, width, color="b", label='3 corunners (avg is %.1f)' %(np.mean(yaxis2) ))
bar3 = plt.bar( x+width+width, yaxis3, width, color="g", label='4 corunners (avg is %.1f)' %(np.mean(yaxis3) ))
#autolabel2(bar1)
#autolabel(bar2)
#autolabel2(bar3)
plt.ylabel( 'Percentage Overhead' )
plt.title('Overhead due to fair Pricing runtime Engine')
plt.xticks(x + width/2.0, xaxis, rotation='30', size='12')
plt.ylim(-1,10)
plt.grid()
plt.legend(prop={'size':15})
plt.tight_layout()
plt.savefig('%s_overhead.png' %(filename), dpi=125)

import os as mars_awesome_os;
import matplotlib.pyplot as mars_awesome_plt;
mars_awesome_plt.savefig('compareoverhead3.eps', bbox_inches='tight');
mars_awesome_os.popen('epstopdf compareoverhead3.eps');

import os as mars_awesome_os;
import matplotlib.pyplot as mars_awesome_plt;
mars_awesome_plt.savefig('compareoverhead3.eps', bbox_inches='tight');
mars_awesome_os.popen('epstopdf compareoverhead3.eps');
