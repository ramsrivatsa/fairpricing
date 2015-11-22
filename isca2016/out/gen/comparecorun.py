from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

colocationListBaseline = [ 'colocating with perlbench', 'colocating with astar', 'colocating with povray', 'colocating with omnetpp', 'colocating with bzip2', 'colocating with libquantum', 'colocating with lbm', 'colocating with sphinx3', 'colocating with soplex' ]
#runningList = [ 'mcf', 'colocating with bzip2', 'mcf', 'colocating with astar', 'mcf', 'colocating with soplex', 'mcf', 'colocating with lbm', 'mcf', 'colocating with libquantum' ]
runningList1 = [ 'libquantum', 'colocating with povray', 'libquantum', 'colocating with libquantum']
runningList2 = [ 'lbm', 'colocating with povray', 'lbm', 'colocating with libquantum']
runningList3 = [  'soplex', 'colocating with povray', 'soplex', 'colocating with libquantum']
runningList4 = [ 'gmm', 'colocating with povray', 'gmm', 'colocating with libquantum']
runningList5 = [   'crf', 'colocating with povray', 'crf', 'colocating with libquantum']
runningList6 = [  'nlp-pos', 'colocating with povray', 'nlp-pos', 'colocating with libquantum']
benchListExperiments = ['lbm', 'libquantum', 'soplex']
benchListExperiments2 = ['gmm', 'crf', 'nlp-pos']
benchListExperiments3 = ['lbm', 'libquantum', 'soplex', 'speech', 'crf', 'NLP']
xlabels = ['Speech\nRecognition', 'Question\nAnswer', 'Natural\nLanguage\nProcessing', 'lbm', 'libquantum', 'soplex' ]
gmm=0.74
crf=0.55
nlp_pos=0.45
libquantum=0.59
lbm=0.95
soplex=1.3
def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()-rect.get_width()/2., 1.1*height, '%.2fx'%float(height), size='15')

def autolabel2(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x(), 1.05*height, '%.2fx'%float(height), size='15')

filename = 'shutter_cpi_5'
fList2 = [s.strip() for s in open('../../papergraphs/1.1intrograph/degradation/spec.txt').readlines()]
fList3 = [s.strip() for s in open('../../papergraphs/1.1intrograph/degradation/sirius.txt').readlines()]

dictList_degradation_colocation = defaultdict(lambda  : defaultdict(list))
dictList_degradation_colocation_sirius = defaultdict(lambda  : defaultdict(list))

labels = ['0x', '1x', '2x', '3x', '4x']

for (b,a) in enumerate(fList2):
    if a in colocationListBaseline:
        index = a
    else:
        if a in benchListExperiments:
            dictList_degradation_colocation[index][a].append(float(fList2[b+1]))

for (b,a) in enumerate(fList3):
    if a in colocationListBaseline:
        index = a
    else:
        if a in benchListExperiments2:
            dictList_degradation_colocation_sirius[index][a].append(float(fList3[b+1]))

yaxis = ()
yaxis2 = ()
xaxis = ()
#xaxis = xaxis + ('solo app',)
#yaxis = yaxis + (1,)
#yaxis2= yaxis2 + (1,)
#sorting the ground truth values
for a in xrange(0,len(runningList1),2):
    j = runningList1[a+1]
    i = runningList1[a]
    #yaxis = yaxis + (np.mean(dictList_degradation_colocation[j][i])/np.mean(dictList_degradation_colocation['colocating with bzip2'][i]), )
    yaxis = yaxis + (np.mean(dictList_degradation_colocation[j][i])/libquantum, )
for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]
    #yaxis = yaxis + (np.mean(dictList_degradation_colocation[j][i])/np.mean(dictList_degradation_colocation['colocating with bzip2'][i]), )
    yaxis = yaxis + (np.mean(dictList_degradation_colocation[j][i])/lbm, )
for a in xrange(0,len(runningList3),2):
    j = runningList3[a+1]
    i = runningList3[a]
    #yaxis = yaxis + (np.mean(dictList_degradation_colocation[j][i])/np.mean(dictList_degradation_colocation['colocating with bzip2'][i]), )
    yaxis = yaxis + (np.mean(dictList_degradation_colocation[j][i])/soplex, )

for a in xrange(0,len(runningList4),2):
    j = runningList4[a+1]
    i = runningList4[a]
    yaxis2= yaxis2 + (np.mean(dictList_degradation_colocation_sirius[j][i])/gmm, )
    #print j,i,dictList_degradation_colocation_sirius[j][i]

for a in xrange(0,len(runningList5),2):
    j = runningList5[a+1]
    i = runningList5[a]
    yaxis2= yaxis2 + (np.mean(dictList_degradation_colocation_sirius[j][i])/crf, )
    #print j,i,dictList_degradation_colocation_sirius[j][i]

for a in xrange(0,len(runningList6),2):
    j = runningList6[a+1]
    i = runningList6[a]
    yaxis2= yaxis2 + (np.mean(dictList_degradation_colocation_sirius[j][i])/nlp_pos, )
    #print j,i,dictList_degradation_colocation_sirius[j][i]
#print yaxis,yaxis2


yaxis_povray = ()
yaxis_libquantum = ()

for (count,item) in enumerate(yaxis2):
    if count%2 == 0:
        yaxis_povray = yaxis_povray + (item , )
    else:
        yaxis_libquantum = yaxis_libquantum + (item, )

for (count,item) in enumerate(yaxis):
    if count%2 == 0:
        yaxis_povray = yaxis_povray + (item , )
    else:
        yaxis_libquantum = yaxis_libquantum + (item, )


#print yaxis_povray, yaxis_libquantum



width=0.25
x = np.arange(len(yaxis))
fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(111)
bar1 = ax1.bar( x, yaxis_povray, width, color="y", label='co-running with povray')
ax2 = ax1.twinx()
bar2 = ax2.bar( x+width, yaxis_libquantum, width, color="r", label='co-running with libquantum')
autolabel(bar1)
ax1.set_xlim(0,6)
ax1.set_ylim(0,4)
ax1.set_yticklabels(('', '', '1x','', '2x', '', '3x', '', '4x', '') , size='18')
ax2.set_ylim(0,4)
ax2.set_yticklabels(('', '', '$1000','', '$2000', '', '$3000', '', '$4000', '') , size='18')
ax1.set_xticklabels(xlabels,  ha='left', rotation='0', size='16')
autolabel2(bar2)
ax1.legend(prop={'size':17}, loc=2)
ax2.legend(prop={'size':17}, loc=1)
plt.tight_layout()
plt.grid()

import os as mars_awesome_os;
import matplotlib.pyplot as mars_awesome_plt;
mars_awesome_plt.savefig('comparecorun.eps', bbox_inches='tight');
mars_awesome_os.popen('epstopdf comparecorun.eps');
