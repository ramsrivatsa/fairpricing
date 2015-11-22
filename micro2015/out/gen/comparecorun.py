from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

colocationListBaseline = [ 'colocating with perlbench', 'colocating with astar', 'colocating with povray', 'colocating with omnetpp', 'colocating with bzip2', 'colocating with libquantum', 'colocating with lbm', 'colocating with sphinx3', 'colocating with soplex' ]
runningList = [ 'mcf', 'colocating with bzip2', 'mcf', 'colocating with astar', 'mcf', 'colocating with soplex', 'mcf', 'colocating with lbm', 'mcf', 'colocating with libquantum' ]
benchListExperiments = ['mcf']
libquantum=1.09
def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.08*height, '%.2f'%float(height), size='17')

def autolabel2(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%.2f x'%float(height))

filename = 'shutter_cpi_5'
fList2 = [s.strip() for s in open('../../papergraphs/1.1intrograph/degradation/shutter_cpi_1000.txt').readlines()]

dictList_degradation_colocation = defaultdict(lambda  : defaultdict(list))

for (b,a) in enumerate(fList2):
    if a in colocationListBaseline:
        index = a
    else:
        if a in benchListExperiments:
            dictList_degradation_colocation[index][a].append(float(fList2[b+1]))

yaxis = ()
xaxis = ()
xaxis = xaxis + ('mcf solo',)
yaxis = yaxis + (1,)
#sorting the ground truth values
for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]
    xaxis = xaxis + ('mcf + \n' + j[16:],)
    #yaxis = yaxis + (np.mean(dictList_degradation_colocation[j][i])/np.mean(dictList_degradation_colocation['colocating with bzip2'][i]), )
    yaxis = yaxis + (np.mean(dictList_degradation_colocation[j][i])/2.75, ) 
   #print j,i,dictList_degradation_colocation[j][i]

width=0.5
x = np.arange(len(yaxis))
fig = plt.figure(figsize=(10, 5))
bar1 = plt.bar( x, yaxis, width, color="g", label='mcf with co-runners in the x-axis')
#bar2 = plt.bar( x+width, yaxis2, width, color="b", label='colocating with mcf  (avg = %.2f)' %(np.mean(yaxis_abs2)))
autolabel(bar1)
#autolabel(bar2)
plt.ylabel( 'Execution time \n normalized to mcf solo ',fontsize=20, multialignment='center')
plt.xticks(x + width/2.0, xaxis, rotation='30',  ha='center', size='18')
#x	plt.ylim(-0.1,4)
plt.yticks(np.arange(0,5),size='23')

plt.xlim(-0.5,6)
plt.grid()
plt.tight_layout()
#plt.legend(prop={'size':20})
#plt.savefig('comparecorun.png', dpi=150)
#plt.show()
#plt.close()
#plt.savefig('%s_error.png' %(filename), dpi=125)

import os as mars_awesome_os;
import matplotlib.pyplot as mars_awesome_plt;
mars_awesome_plt.savefig('comparecorun.eps', bbox_inches='tight');
mars_awesome_os.popen('epstopdf comparecorun.eps');
