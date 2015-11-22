from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

benchListBaseline = [ 'gcc', 'perlbench', 'leslie3d', 'povray', 'libquantum', 'astar', 'bzip2', 'milc', 'namd', 'calculix', 'h264ref', 'sphinx3', 'zeusmp', 'gobmk', 'hmmer', 'tonto', 'bwaves', 'gromacs', 'dealII', 'sjeng', 'lbm', 'xalancbmk', 'gamess', 'cactusADM', 'soplex', 'GemsFDTD', 'omnetpp', 'mcf' ]
benchListExperiments = [ 'gcc', 'perlbench', 'leslie3d', 'povray', 'libquantum', 'astar', 'bzip2', 'milc', 'namd', 'calculix', 'h264ref', 'sphinx3', 'zeusmp', 'gobmk', 'hmmer', 'tonto', 'bwaves', 'gromacs', 'dealII', 'sjeng', 'lbm', 'xalancbmk', 'gamess', 'cactusADM', 'soplex', 'GemsFDTD', 'omnetpp', 'mcf' ]
colocationListBaseline = [ 'colocating with lbm', 'colocating with povray', 'colocating with astar', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
colocationListExperiments = [ 'colocating with lbm', 'colocating with povray', 'colocating with perlbench', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
runningList2 = [  'perlbench', 'colocating with libquantum', 'mcf', 'colocating with libquantum', 'leslie3d', 'colocating with libquantum', 'povray', 'colocating with libquantum', 'libquantum', 'colocating with libquantum', 'astar', 'colocating with libquantum', 'bzip2', 'colocating with libquantum', 'milc', 'colocating with libquantum', 'namd', 'colocating with libquantum', 'calculix', 'colocating with libquantum', 'h264ref', 'colocating with libquantum', 'gobmk', 'colocating with libquantum', 'hmmer', 'colocating with libquantum', 'tonto', 'colocating with libquantum', 'sphinx3', 'colocating with libquantum', 'zeusmp', 'colocating with libquantum', 'bwaves', 'colocating with libquantum', 'gromacs', 'colocating with libquantum', 'dealII', 'colocating with libquantum', 'sjeng', 'colocating with libquantum', 'lbm', 'colocating with libquantum', 'xalancbmk', 'colocating with libquantum', 'gamess', 'colocating with libquantum', 'cactusADM', 'colocating with libquantum', 'soplex', 'colocating with libquantum', 'GemsFDTD', 'colocating with libquantum', 'omnetpp', 'colocating with libquantum' ]

siriusbenchListBaseline = [ 'gmm', 'dnn_asr', 'surf-fe', 'surf-fd', 'stem', 'regex', 'crf', 'img-imc', 'img-dig', 'img-face', 'nlp-pos', 'nlp-chk', 'nlp-ner']
siriusbenchListExperiments = [ 'gmm', 'dnn_asr', 'surf-fe', 'surf-fd', 'stem', 'regex', 'crf', 'img-imc', 'img-dig', 'img-face', 'nlp-pos', 'nlp-chk', 'nlp-ner']
siriuscolocationListBaseline = [ 'colocating with lbm', 'colocating with povray', 'colocating with astar', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
siriuscolocationListExperiments = [ 'colocating with lbm', 'colocating with povray', 'colocating with perlbench', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
siriusrunningList2 = [ 'gmm', 'colocating with libquantum', 'dnn_asr', 'colocating with libquantum', 'surf-fe', 'colocating with libquantum', 'surf-fd', 'colocating with libquantum', 'stem', 'colocating with libquantum', 'regex', 'colocating with libquantum', 'crf', 'colocating with libquantum', 'img-imc', 'colocating with libquantum', 'img-dig', 'colocating with libquantum', 'img-face', 'colocating with libquantum', 'nlp-pos', 'colocating with libquantum', 'nlp-chk', 'colocating with libquantum', 'nlp-ner' , 'colocating with libquantum']

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%.2f'%float(height))

def autolabel2(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%.2f'%float(height))

def add_line(ax, xpos, ypos):
    line = plt.Line2D([xpos, xpos], [ypos + .1, ypos - .5], transform=ax.transAxes, linewidth=2, color='black')
    line.set_clip_on(False)
    ax.add_line(line)

filename = 'shutter_cpi_10'

fList3= [s.strip() for s in open('../../papergraphs/accuracy/libquantumcorunner/priorwork/shutter_cpi_5.txt').readlines()]

fList4 = [s.strip() for s in open('../../papergraphs/accuracy/libquantumcorunner/singlevm/shutter_cpi_1000.txt').readlines()]
fList5 = [s.strip() for s in open('../../papergraphs/accuracy/libquantumcorunner/degradation/shutter_cpi_1000.txt').readlines()]
fList6 = [s.strip() for s in open('../../papergraphs/accuracy/libquantumcorunner/snapshot2/%s.txt' % filename).readlines()]
fList7 = [s.strip() for s in open('../../papergraphs/accuracy/libquantumcorunner/degradation3/shutter_cpi_1000.txt').readlines()]

fList8= [s.strip() for s in open('../../papergraphs/accuracy/libquantumcorunner/siriusdjinn/priorwork/shutter_cpi_4.txt').readlines()]

fList9 = [s.strip() for s in open('../../papergraphs/accuracy/libquantumcorunner/siriusdjinn/singlevm/shutter_cpi_1000.txt').readlines()]
fList10 = [s.strip() for s in open('../../papergraphs/accuracy/libquantumcorunner/siriusdjinn/degradation/shutter_cpi_1000.txt').readlines()]
fList11 = [s.strip() for s in open('../../papergraphs/accuracy/libquantumcorunner/siriusdjinn/snapshot/%s.txt' % filename).readlines()]

dictList_single_vm = defaultdict(list)
dictList_degradation_colocation = defaultdict(lambda  : defaultdict(list))
dictList_degradation_colocation2 = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter2 = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter3 = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter4 = defaultdict(lambda  : defaultdict(list))
plot_degradation = defaultdict(dict)
plot_degradation2 = defaultdict(dict)
plot_degradation_error = defaultdict(dict)
plot_degradation_error2 = defaultdict(dict)
plot_degradation_abs = defaultdict(dict)
plot_degradation_abs2 = defaultdict(dict)

for (b,a) in enumerate(fList4):
    if a in benchListBaseline:
        dictList_single_vm[a].append(fList4[b+1])

#SORTING LIST CONTAING VALUES OF SINGLE SPEC RUNS INSIDE VMs
for i in benchListBaseline:
    dictList_single_vm[i].sort()
    #print i,dictList_single_vm[i]

for (b,a) in enumerate(fList5):
    #print a
    if a in colocationListBaseline:
       #print a
       index = a
    else:
        if a in benchListExperiments:
            #print a
            dictList_degradation_colocation[index][a].append(fList5[b+1])

#sorting the ground truth values
for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]
    dictList_degradation_colocation[j][i].sort()
    #print j,i,dictList_degradation_colocation[j][i]

for (b,a) in enumerate(fList7):
    #print a
    if a in colocationListBaseline:
       #print a
       index = a
    else:
        if a in benchListExperiments:
            #print a
            dictList_degradation_colocation2[index][a].append(fList7[b+1])

#APPENDING DEGRADATION SHUTTER
for (b,a) in enumerate(fList6):
    if a in colocationListExperiments:
        index = a
    else:
        if a in benchListExperiments:
            dictList_degradation_shutter[index][a].append(fList6[b+1])

for (b,a) in enumerate(fList3):
    if a in colocationListExperiments:
        index = a
    else:
        if a in benchListExperiments:
            dictList_degradation_shutter3[index][a].append(fList3[b+1])

for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]
    #print i,j,dictList_degradation_shutter[j][i]
#APPENDING DEGRADATION SHUTTER2 as shutter and colocation values are tab separated
for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]
    for elem in dictList_degradation_shutter[j][i]:
        dictList_degradation_shutter2[j][i].extend(elem.strip().split('\t'))

    for elem in dictList_degradation_shutter3[j][i]:
        dictList_degradation_shutter4[j][i].extend(elem.strip().split('\t'))
    #print dictList_degradation_shutter2[j][i]

speclib_yaxis2 = ()
speclib_yaxis3 = ()
speclib_yaxis_abs2 = ()
speclib_yaxis_abs3 = ()
speclib_error2 = ()
speclib_error3 = ()
speclib_xaxis2 = ()
for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]
    #print i,j
    #print dictList_single_vm[i]
    #print dictList_degradation_colocation[j][i]
    #print dictList_degradation_shutter2[j][i]
    denominator1 = sum(float(n) for (m,n) in enumerate(dictList_single_vm[i]) if m!=0 and m!=len(dictList_single_vm[i])-1)/(len(dictList_single_vm[i])-2)
    numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_colocation[j][i]))/(len(dictList_degradation_colocation[j][i]))
    numerator10 = sum(float(n) for (m,n) in enumerate(dictList_degradation_colocation2[j][i]))/(len(dictList_degradation_colocation2[j][i]))
    shutter_temp_list = []
    shutter_temp_list2 = []
    colo_temp_list = []
    colo_temp_list2 = []
    degradation_temp_list = []
    degradation_temp_list2 = []
    error_temp_list = []
    error_temp_list2 = []
    #print numerator1
    #print denominator1
    for (count,item) in enumerate(dictList_degradation_shutter2[j][i]):
        if count%2==0:
            colo_temp_list.append(item)
        if count%2==1:
            shutter_temp_list.append(item)

    for (count,item) in enumerate(dictList_degradation_shutter4[j][i]):
        if count%2==0:
            colo_temp_list2.append(item)
        if count%2==1:
            shutter_temp_list2.append(item)

    for (count,item) in enumerate(shutter_temp_list):
        degradation_temp_list.append(abs((((float(shutter_temp_list[count])/float(colo_temp_list[count]))-(numerator1/denominator1))/(float(shutter_temp_list[count])/float(colo_temp_list[count])))*100))

    shutter_temp_list.sort()
    shutter_temp_list2.sort()
    colo_temp_list.sort()
    colo_temp_list2.sort()
    #print shutter_temp_list
    #print colo_temp_list
    #print dictList_degradation_shutter2[j][i]
    denominator2 = sum(float(n) for (m,n) in enumerate(shutter_temp_list) if m!=0 and m!=len(shutter_temp_list)-1 )/len(shutter_temp_list)
    numerator2 = sum(float(n) for (m,n) in enumerate(colo_temp_list) if m!=0 and m!=len(colo_temp_list)-1  )/len(colo_temp_list)
    for (m,n) in enumerate(shutter_temp_list):
        ratio=float(n)/float(colo_temp_list[m])
        error_temp_list.append(abs((((ratio)-(numerator10/denominator1))/(numerator10/denominator1))*100))
    plot_degradation_error[j][i]=np.std(error_temp_list)

    denominator3 = sum(float(n) for (m,n) in enumerate(shutter_temp_list2))/(len(shutter_temp_list2))
    numerator3 = sum(float(n) for (m,n) in enumerate(colo_temp_list2))/(len(colo_temp_list2))
    for (m,n) in enumerate(shutter_temp_list2):
        ratio=float(n)/float(colo_temp_list2[m])
        error_temp_list2.append(abs((((ratio)-(numerator3/denominator3))/(numerator1/denominator1))*100))
    plot_degradation_error2[j][i]=np.std(error_temp_list2)

    #print numerator2
    #print denominator2
    del shutter_temp_list
    del colo_temp_list
    del degradation_temp_list
    del shutter_temp_list2
    del colo_temp_list2
    del degradation_temp_list2
    plot_degradation[j][i] = (((numerator2/denominator2)-(numerator10/denominator1))/(numerator10/denominator1))*100
    plot_degradation_abs[j][i] = abs((((numerator2/denominator2)-(numerator10/denominator1))/(numerator10/denominator1))*100)
    plot_degradation2[j][i] = (((numerator3/denominator3)-(numerator1/denominator1))/(numerator1/denominator1))*100
    plot_degradation_abs2[j][i] = abs((((numerator3/denominator3)-(numerator1/denominator1))/(numerator1/denominator1))*100)
    #print j,i,plot_degradation[j][i]
    #print plot_degradation_error[j][i]
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    speclib_xaxis2 = speclib_xaxis2 + (i,)
    speclib_yaxis2 = speclib_yaxis2 + (plot_degradation[j][i],)
    speclib_yaxis3 = speclib_yaxis3 + (plot_degradation2[j][i],)
    speclib_yaxis_abs2 = speclib_yaxis_abs2 + (plot_degradation_abs[j][i],)
    speclib_yaxis_abs3 = speclib_yaxis_abs3 + (plot_degradation_abs2[j][i],)
    speclib_error2 = speclib_error2 + (plot_degradation_error[j][i],)
    speclib_error3 = speclib_error3 + (plot_degradation_error2[j][i],)
    #print numerator2,denominator2,numerator2/denominator2
    #print denominator2/numerator2
    #print j,i,plot_degradation[j][i]
            #print (((numerator2/denominator2)-(numerator1/denominator1))/(numerator2/denominator2))*100
#print np.mean(yaxis2)


#width=0.25
#x = np.arange(len(yaxis2))
#fig = plt.figure(figsize=(28, 5))
##bar1 = plt.bar( x, yaxis, width, color="r", label='colocating with libquatum (avg = %.2f)' %(np.mean(yaxis_abs)))
#bar1 = plt.bar( x, yaxis_abs3, width, color="k", yerr=error3, label='Shuttering (mean: %.2f)' %(np.mean(yaxis_abs3)))
#bar2 = plt.bar( x+width, yaxis_abs2, width, color="lightgrey", yerr=error2, label='Snapshot (mean: %.2f)' %(np.mean(yaxis_abs2)))
##bar3 = plt.bar( x+width+width, yaxis3, width, color="g", label='colocating with sphinx  (avg = %.2f)' %(np.mean(yaxis_abs3)))
##autolabel(bar1)
##autolabel(bar2)
#plt.ylabel( 'Estimation error (%)' ,fontsize='25')
##plt.title('Error in predicting degradation when co-locating with libquantum')
#plt.xticks(x + width/2.0, xaxis2, rotation='30', size='23',  ha='center', va='top')
##plt.yticks((-0.5,0,1,2,3,4),('','0','1','2','3','4'),size='23')
#plt.yticks((0,10,20,30,40,50),('0','10','20','30','40',' '),size='25')
#plt.ylim(0,50)
#plt.xlim(-1,26)
#plt.grid()
#plt.tight_layout()
#plt.legend(loc=9, ncol=2, prop={'size':28})
##plt.savefig('%s_maybefinal_error.png' %(filename), dpi=125)


## ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

del dictList_single_vm
del dictList_degradation_colocation
del dictList_degradation_shutter
del dictList_degradation_shutter2
del dictList_degradation_shutter3
del dictList_degradation_shutter4
del plot_degradation
del plot_degradation2
del plot_degradation_error
del plot_degradation_error2
del plot_degradation_abs
del plot_degradation_abs2

dictList_single_vm = defaultdict(list)
dictList_degradation_colocation = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter2 = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter3 = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter4 = defaultdict(lambda  : defaultdict(list))
plot_degradation = defaultdict(dict)
plot_degradation2 = defaultdict(dict)
plot_degradation_error = defaultdict(dict)
plot_degradation_error2 = defaultdict(dict)
plot_degradation_abs = defaultdict(dict)
plot_degradation_abs2 = defaultdict(dict)

for (b,a) in enumerate(fList9):
    if a in siriusbenchListBaseline:
        dictList_single_vm[a].append(fList9[b+1])

#SORTING LIST CONTAING VALUES OF SINGLE SPEC RUNS INSIDE VMs
for i in siriusbenchListBaseline:
    dictList_single_vm[i].sort()
    #print i,dictList_single_vm[i]

for (b,a) in enumerate(fList10):
    #print a
    if a in siriuscolocationListBaseline:
       #print a
       index = a
    else:
        if a in siriusbenchListExperiments:
            #print a
            dictList_degradation_colocation[index][a].append(fList10[b+1])

#sorting the ground truth values
for a in xrange(0,len(siriusrunningList2),2):
    j = siriusrunningList2[a+1]
    i = siriusrunningList2[a]
    #print i,j
    dictList_degradation_colocation[j][i].sort()
    #print j,i,dictList_degradation_colocation[j][i]

#for a in xrange(0,len(runningList),2):
#    j = runningList[a+1]
#    i = runningList[a]
#    numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_colocation[j][i]) if m!=0 and m!=len(dictList_degradation_colocation[j][i])-1)/(len(dictList_degradation_colocation[j][i])-2)
#    print numerator1
#    #print dictList_degradation_colocation[runningList[a+1]][runningList[a]]
#    #print numerator1

#APPENDING DEGRADATION SHUTTER
for (b,a) in enumerate(fList11):
    #print a
    if a in siriuscolocationListExperiments:
        index = a
    else:
        if a in siriusbenchListExperiments:
            dictList_degradation_shutter[index][a].append(fList11[b+1])

for (b,a) in enumerate(fList8):
    if a in siriuscolocationListExperiments:
        index = a
    else:
        if a in siriusbenchListExperiments:
            dictList_degradation_shutter3[index][a].append(fList8[b+1])

for a in xrange(0,len(siriusrunningList2),2):
    j = siriusrunningList2[a+1]
    i = siriusrunningList2[a]
    #print i,j,dictList_degradation_shutter[j][i]
#APPENDING DEGRADATION SHUTTER2 as shutter and colocation values are tab separated
for a in xrange(0,len(siriusrunningList2),2):
    j = siriusrunningList2[a+1]
    i = siriusrunningList2[a]
    for elem in dictList_degradation_shutter[j][i]:
        dictList_degradation_shutter2[j][i].extend(elem.strip().split('\t'))

    for elem in dictList_degradation_shutter3[j][i]:
        dictList_degradation_shutter4[j][i].extend(elem.strip().split('\t'))
    #print dictList_degradation_shutter2[j][i]


lib_xaxis2 = ()
lib_yaxis2 = ()
lib_yaxis3 = ()
lib_yaxis_abs2 = ()
lib_yaxis_abs3 = ()
lib_error2 = ()
lib_error3 = ()

for a in xrange(0,len(siriusrunningList2),2):
    j = siriusrunningList2[a+1]
    i = siriusrunningList2[a]
    #print i,j
    #print i
    #print dictList_single_vm[i]
    #print dictList_degradation_colocation[j][i]
    #print dictList_degradation_shutter2[j][i]
    denominator1 = sum(float(n) for (m,n) in enumerate(dictList_single_vm[i]) if m!=0 and m!=len(dictList_single_vm[i])-1)/(len(dictList_single_vm[i])-2)
    numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_colocation[j][i]))/(len(dictList_degradation_colocation[j][i]))
    shutter_temp_list = []
    shutter_temp_list2 = []
    colo_temp_list = []
    colo_temp_list2 = []
    degradation_temp_list = []
    degradation_temp_list2 = []
    error_temp_list = []
    error_temp_list2 = []
    #print numerator1
    #print denominator1
    for (count,item) in enumerate(dictList_degradation_shutter2[j][i]):
        if count%2==0:
            colo_temp_list.append(item)
        if count%2==1:
            shutter_temp_list.append(item)

    for (count,item) in enumerate(dictList_degradation_shutter4[j][i]):
        if count%2==0:
            colo_temp_list2.append(item)
        if count%2==1:
            shutter_temp_list2.append(item)

    for (count,item) in enumerate(shutter_temp_list):
        degradation_temp_list.append(abs((((float(shutter_temp_list[count])/float(colo_temp_list[count]))-(numerator1/denominator1))/(float(shutter_temp_list[count])/float(colo_temp_list[count])))*100))

    shutter_temp_list.sort()
    shutter_temp_list2.sort()
    colo_temp_list.sort()
    colo_temp_list2.sort()
    #print shutter_temp_list
    #print colo_temp_list
    #print dictList_degradation_shutter2[j][i]
    denominator2 = sum(float(n) for (m,n) in enumerate(shutter_temp_list) if m!=0 and m!=len(dictList_single_vm[i])-1)/(len(dictList_single_vm[i])-2)/len(shutter_temp_list)
    numerator2 = sum(float(n) for (m,n) in enumerate(colo_temp_list) if m!=0 and m!=len(dictList_single_vm[i])-1)/(len(dictList_single_vm[i])-2 )/len(colo_temp_list)
    for (m,n) in enumerate(shutter_temp_list):
        ratio=float(n)/float(colo_temp_list[m])
        error_temp_list.append(abs((((ratio)-(numerator1/denominator1))/(numerator1/denominator1))*100))
    plot_degradation_error[j][i]=np.std(error_temp_list)

    denominator3 = sum(float(n) for (m,n) in enumerate(shutter_temp_list2))/(len(shutter_temp_list2))
    numerator3 = sum(float(n) for (m,n) in enumerate(colo_temp_list2))/(len(colo_temp_list2))
    for (m,n) in enumerate(shutter_temp_list2):
        ratio=float(n)/float(colo_temp_list2[m])
        error_temp_list2.append(abs((((ratio)-(numerator3/denominator3))/(numerator1/denominator1))*100))
    plot_degradation_error2[j][i]=np.std(error_temp_list2)

    #print numerator2
    #print denominator2
    del shutter_temp_list
    del colo_temp_list
    del degradation_temp_list
    del shutter_temp_list2
    del colo_temp_list2
    del degradation_temp_list2
    plot_degradation[j][i] = (((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100
    plot_degradation_abs[j][i] = abs((((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100)
    plot_degradation2[j][i] = (((numerator3/denominator3)-(numerator1/denominator1))/(numerator1/denominator1))*100
    plot_degradation_abs2[j][i] = abs((((numerator3/denominator3)-(numerator1/denominator1))/(numerator1/denominator1))*100)
    #print j,i,plot_degradation[j][i]
    #print plot_degradation_error[j][i]
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    lib_xaxis2 = lib_xaxis2 + (i,)
    lib_yaxis2 = lib_yaxis2 + (plot_degradation[j][i],)
    lib_yaxis3 = lib_yaxis3 + (plot_degradation2[j][i],)
    lib_yaxis_abs2 = lib_yaxis_abs2 + (plot_degradation_abs[j][i],)
    lib_yaxis_abs3 = lib_yaxis_abs3 + (plot_degradation_abs2[j][i],)
    lib_error2 = lib_error2 + (plot_degradation_error[j][i],)
    lib_error3 = lib_error3 + (plot_degradation_error2[j][i],)
    #print numerator2,denominator2,numerator2/denominator2
    #print denominator2/numerator2
    #print j,i,plot_degradation[j][i],plot_degradation2[j][i]
            #print (((numerator2/denominator2)-(numerator1/denominator1))/(numerator2/denominator2))*100
#print np.mean(yaxis2)


############### MCF STARTING #######################
benchListBaseline = [ 'gcc', 'perlbench', 'leslie3d', 'povray', 'libquantum', 'astar', 'bzip2', 'milc', 'namd', 'calculix', 'h264ref', 'sphinx3', 'zeusmp', 'gobmk', 'hmmer', 'tonto', 'bwaves', 'gromacs', 'dealII', 'sjeng', 'lbm', 'xalancbmk', 'gamess', 'cactusADM', 'soplex', 'GemsFDTD', 'omnetpp', 'mcf' ]
benchListExperiments = [ 'gcc', 'perlbench', 'leslie3d', 'povray', 'libquantum', 'astar', 'bzip2', 'milc', 'namd', 'calculix', 'h264ref', 'sphinx3', 'zeusmp', 'gobmk', 'hmmer', 'tonto', 'bwaves', 'gromacs', 'dealII', 'sjeng', 'lbm', 'xalancbmk', 'gamess', 'cactusADM', 'soplex', 'GemsFDTD', 'omnetpp', 'mcf' ]
colocationListBaseline = [ 'colocating with lbm', 'colocating with povray', 'colocating with astar', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
colocationListExperiments = [ 'colocating with lbm', 'colocating with povray', 'colocating with perlbench', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]

runningList2 = [  'perlbench', 'colocating with mcf', 'mcf', 'colocating with mcf', 'leslie3d', 'colocating with mcf', 'povray', 'colocating with mcf', 'libquantum', 'colocating with mcf', 'astar', 'colocating with mcf', 'bzip2', 'colocating with mcf', 'milc', 'colocating with mcf', 'namd', 'colocating with mcf', 'calculix', 'colocating with mcf', 'h264ref', 'colocating with mcf', 'gobmk', 'colocating with mcf', 'hmmer', 'colocating with mcf', 'tonto', 'colocating with mcf', 'sphinx3', 'colocating with mcf', 'zeusmp', 'colocating with mcf', 'bwaves', 'colocating with mcf', 'gromacs', 'colocating with mcf', 'dealII', 'colocating with mcf', 'sjeng', 'colocating with mcf', 'lbm', 'colocating with mcf', 'xalancbmk', 'colocating with mcf', 'gamess', 'colocating with mcf', 'cactusADM', 'colocating with mcf', 'soplex', 'colocating with mcf', 'GemsFDTD', 'colocating with mcf', 'omnetpp', 'colocating with mcf' ]
siriusbenchListBaseline = [ 'gmm', 'dnn_asr', 'surf-fe', 'surf-fd', 'stem', 'regex', 'crf', 'img-imc', 'img-dig', 'img-face', 'nlp-pos', 'nlp-chk', 'nlp-ner']
siriusbenchListExperiments = [ 'gmm', 'dnn_asr', 'surf-fe', 'surf-fd', 'stem', 'regex', 'crf', 'img-imc', 'img-dig', 'img-face', 'nlp-pos', 'nlp-chk', 'nlp-ner']
siriuscolocationListBaseline = [ 'colocating with lbm', 'colocating with povray', 'colocating with astar', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
siriuscolocationListExperiments = [ 'colocating with lbm', 'colocating with povray', 'colocating with perlbench', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
siriusrunningList2 = [ 'gmm', 'colocating with mcf', 'dnn_asr', 'colocating with mcf', 'surf-fe', 'colocating with mcf', 'surf-fd', 'colocating with mcf', 'stem', 'colocating with mcf', 'regex', 'colocating with mcf', 'crf', 'colocating with mcf', 'img-imc', 'colocating with mcf', 'img-dig', 'colocating with mcf', 'img-face', 'colocating with mcf', 'nlp-pos', 'colocating with mcf', 'nlp-chk', 'colocating with mcf', 'nlp-ner' , 'colocating with mcf']

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%.2f'%float(height))

def autolabel2(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%.2f'%float(height))

def add_line(ax, xpos, ypos):
    line = plt.Line2D([xpos, xpos], [ypos + .1, ypos - .5], transform=ax.transAxes, linewidth=2, color='black')
    line.set_clip_on(False)
    ax.add_line(line)


filename = 'shutter_cpi_70'

fList3= [s.strip() for s in open('../../papergraphs/accuracy/mcfcorunner/priorwork/shutter_cpi_5.txt').readlines()]

fList4 = [s.strip() for s in open('../../papergraphs/accuracy/mcfcorunner/singlevm/shutter_cpi_1000.txt').readlines()]
fList5 = [s.strip() for s in open('../../papergraphs/accuracy/mcfcorunner/degradation/shutter_cpi_1000.txt').readlines()]
fList6 = [s.strip() for s in open('../../papergraphs/accuracy/mcfcorunner/snapshot/%s.txt' % filename).readlines()]


fList8= [s.strip() for s in open('../../papergraphs/accuracy/mcfcorunner/siriusdjinn/priorwork/shutter_cpi_4.txt').readlines()]

fList9 = [s.strip() for s in open('../../papergraphs/accuracy/mcfcorunner/siriusdjinn/singlevm/shutter_cpi_1000.txt').readlines()]
fList10 = [s.strip() for s in open('../../papergraphs/accuracy/mcfcorunner/siriusdjinn/degradation/shutter_cpi_1000.txt').readlines()]
fList11 = [s.strip() for s in open('../../papergraphs/accuracy/mcfcorunner/siriusdjinn/snapshot/shutter_cpi_75.txt').readlines()]

dictList_single_vm = defaultdict(list)
dictList_degradation_colocation = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter2 = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter3 = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter4 = defaultdict(lambda  : defaultdict(list))
plot_degradation = defaultdict(dict)
plot_degradation2 = defaultdict(dict)
plot_degradation_error = defaultdict(dict)
plot_degradation_error2 = defaultdict(dict)
plot_degradation_abs = defaultdict(dict)
plot_degradation_abs2 = defaultdict(dict)

for (b,a) in enumerate(fList4):
    if a in benchListBaseline:
        dictList_single_vm[a].append(fList4[b+1])

#SORTING LIST CONTAING VALUES OF SINGLE SPEC RUNS INSIDE VMs
for i in benchListBaseline:
    dictList_single_vm[i].sort()
    #print i,dictList_single_vm[i]

for (b,a) in enumerate(fList5):
    #print a
    if a in colocationListBaseline:
       #print a
       index = a
    else:
        if a in benchListExperiments:
            #print a
            dictList_degradation_colocation[index][a].append(fList5[b+1])

#sorting the ground truth values
for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]
    dictList_degradation_colocation[j][i].sort()
    #print j,i,dictList_degradation_colocation[j][i]


#APPENDING DEGRADATION SHUTTER
for (b,a) in enumerate(fList6):
    if a in colocationListExperiments:
        index = a
    else:
        if a in benchListExperiments:
            dictList_degradation_shutter[index][a].append(fList6[b+1])

for (b,a) in enumerate(fList3):
    if a in colocationListExperiments:
        index = a
    else:
        if a in benchListExperiments:
            dictList_degradation_shutter3[index][a].append(fList3[b+1])

for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]
    #print i,j,dictList_degradation_shutter[j][i]
#APPENDING DEGRADATION SHUTTER2 as shutter and colocation values are tab separated
for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]
    for elem in dictList_degradation_shutter[j][i]:
        dictList_degradation_shutter2[j][i].extend(elem.strip().split('\t'))

    for elem in dictList_degradation_shutter3[j][i]:
        dictList_degradation_shutter4[j][i].extend(elem.strip().split('\t'))
    #print dictList_degradation_shutter2[j][i]

specmcf_yaxis2 = ()
specmcf_yaxis3 = ()
specmcf_yaxis_abs2 = ()
specmcf_yaxis_abs3 = ()
specmcf_error2 = ()
specmcf_error3 = ()
specmcf_xaxis2 = ()
for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]
    #print i,j
    #print dictList_single_vm[i]
    #print dictList_degradation_colocation[j][i]
    #print dictList_degradation_shutter2[j][i]
    denominator1 = sum(float(n) for (m,n) in enumerate(dictList_single_vm[i]) if m!=0 and m!=len(dictList_single_vm[i])-1)/(len(dictList_single_vm[i])-2)
    numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_colocation[j][i]))/(len(dictList_degradation_colocation[j][i]))
    shutter_temp_list = []
    shutter_temp_list2 = []
    colo_temp_list = []
    colo_temp_list2 = []
    degradation_temp_list = []
    degradation_temp_list2 = []
    error_temp_list = []
    error_temp_list2 = []
    #print numerator1
    #print denominator1
    for (count,item) in enumerate(dictList_degradation_shutter2[j][i]):
        if count%2==0:
            colo_temp_list.append(item)
        if count%2==1:
            shutter_temp_list.append(item)

    for (count,item) in enumerate(dictList_degradation_shutter4[j][i]):
        if count%2==0:
            colo_temp_list2.append(item)
        if count%2==1:
            shutter_temp_list2.append(item)

    for (count,item) in enumerate(shutter_temp_list):
        degradation_temp_list.append(abs((((float(shutter_temp_list[count])/float(colo_temp_list[count]))-(numerator1/denominator1))/(float(shutter_temp_list[count])/float(colo_temp_list[count])))*100))

    shutter_temp_list.sort()
    shutter_temp_list2.sort()
    colo_temp_list.sort()
    colo_temp_list2.sort()
    #print shutter_temp_list
    #print colo_temp_list
    #print dictList_degradation_shutter2[j][i]
    denominator2 = sum(float(n) for (m,n) in enumerate(shutter_temp_list) if m!=0 and m!=len(shutter_temp_list)-1)/(len(shutter_temp_list)-2)
    numerator2 = sum(float(n) for (m,n) in enumerate(colo_temp_list) if m!=0 and m!=len(colo_temp_list)-1)/(len(colo_temp_list)-2)
    #denominator2 = sum(float(n) for (m,n) in enumerate(shutter_temp_list))/len(shutter_temp_list)
    #numerator2 = sum(float(n) for (m,n) in enumerate(colo_temp_list))/len(colo_temp_list)
    for (m,n) in enumerate(shutter_temp_list):
        ratio=float(n)/float(colo_temp_list[m])
        error_temp_list.append(abs((((ratio)-(numerator1/denominator1))/(numerator1/denominator1))*100))
    plot_degradation_error[j][i]=np.std(error_temp_list)

    denominator3 = sum(float(n) for (m,n) in enumerate(shutter_temp_list2))/(len(shutter_temp_list2))
    numerator3 = sum(float(n) for (m,n) in enumerate(colo_temp_list2))/(len(colo_temp_list2))
    for (m,n) in enumerate(shutter_temp_list2):
        ratio=float(n)/float(colo_temp_list2[m])
        error_temp_list2.append(abs((((ratio)-(numerator3/denominator3))/(numerator1/denominator1))*100))
    plot_degradation_error2[j][i]=np.std(error_temp_list2)

    #print numerator2
    #print denominator2
    del shutter_temp_list
    del colo_temp_list
    del degradation_temp_list
    del shutter_temp_list2
    del colo_temp_list2
    del degradation_temp_list2
    plot_degradation[j][i] = (((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100
    plot_degradation_abs[j][i] = abs((((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100)
    plot_degradation2[j][i] = (((numerator3/denominator3)-(numerator1/denominator1))/(numerator1/denominator1))*100
    plot_degradation_abs2[j][i] = abs((((numerator3/denominator3)-(numerator1/denominator1))/(numerator1/denominator1))*100)
    #print j,i,plot_degradation[j][i]
    #print plot_degradation_error[j][i]
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    specmcf_xaxis2 = specmcf_xaxis2 + (i,)
    specmcf_yaxis2 = specmcf_yaxis2 + (plot_degradation[j][i],)
    specmcf_yaxis3 = specmcf_yaxis3 + (plot_degradation2[j][i],)
    specmcf_yaxis_abs2 = specmcf_yaxis_abs2 + (plot_degradation_abs[j][i],)
    specmcf_yaxis_abs3 = specmcf_yaxis_abs3 + (plot_degradation_abs2[j][i],)
    specmcf_error2 = specmcf_error2 + (plot_degradation_error[j][i],)
    specmcf_error3 = specmcf_error3 + (plot_degradation_error2[j][i],)


#width=0.25
#x = np.arange(len(yaxis2))
#fig = plt.figure(figsize=(28, 5))
##bar1 = plt.bar( x, yaxis, width, color="r", label='colocating with libquatum (avg = %.2f)' %(np.mean(yaxis_abs)))
#bar1 = plt.bar( x, yaxis_abs3, width, color="k", yerr=error3, label='Shuttering (mean: %.2f)' %(np.mean(yaxis_abs3)))
#bar2 = plt.bar( x+width, yaxis_abs2, width, color="lightgrey", yerr=error2, label='Snapshot (mean: %.2f)' %(np.mean(yaxis_abs2)))
##bar3 = plt.bar( x+width+width, yaxis3, width, color="g", label='colocating with sphinx  (avg = %.2f)' %(np.mean(yaxis_abs3)))
##autolabel(bar1)
##autolabel(bar2)
#plt.ylabel( 'Estimation error(%)' ,fontsize='25')
##plt.title('Error in predicting degradation when co-locating with mcf')
#plt.xticks(x + width/2.0, xaxis2, rotation='30', size='23',  ha='center', va='top')
#plt.yticks(np.arange(0,50,10),size='25')
#plt.ylim(0,40)
#plt.xlim(-1,27)
#plt.grid()
#plt.tight_layout()
#plt.legend(loc=9, ncol=2, prop={'size':28})
##plt.savefig('%s_maybefinal_error.png' %(filename), dpi=125)

del dictList_single_vm
del dictList_degradation_colocation
del dictList_degradation_shutter
del dictList_degradation_shutter2
del dictList_degradation_shutter3
del dictList_degradation_shutter4
del plot_degradation
del plot_degradation2
del plot_degradation_error
del plot_degradation_error2
del plot_degradation_abs
del plot_degradation_abs2

dictList_single_vm = defaultdict(list)
dictList_degradation_colocation = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter2 = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter3 = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter4 = defaultdict(lambda  : defaultdict(list))
plot_degradation = defaultdict(dict)
plot_degradation2 = defaultdict(dict)
plot_degradation_error = defaultdict(dict)
plot_degradation_error2 = defaultdict(dict)
plot_degradation_abs = defaultdict(dict)
plot_degradation_abs2 = defaultdict(dict)

for (b,a) in enumerate(fList9):
    if a in siriusbenchListBaseline:
        dictList_single_vm[a].append(fList9[b+1])

#SORTING LIST CONTAING VALUES OF SINGLE SPEC RUNS INSIDE VMs
for i in siriusbenchListBaseline:
    dictList_single_vm[i].sort()
    #print i,dictList_single_vm[i]

for (b,a) in enumerate(fList10):
    #print a
    if a in siriuscolocationListBaseline:
       #print a
       index = a
    else:
        if a in siriusbenchListExperiments:
            #print a
            dictList_degradation_colocation[index][a].append(fList10[b+1])

#sorting the ground truth values
for a in xrange(0,len(siriusrunningList2),2):
    j = siriusrunningList2[a+1]
    i = siriusrunningList2[a]
    #print i,j
    dictList_degradation_colocation[j][i].sort()
    #print j,i,dictList_degradation_colocation[j][i]

#for a in xrange(0,len(runningList),2):
#    j = runningList[a+1]
#    i = runningList[a]
#    numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_colocation[j][i]) if m!=0 and m!=len(dictList_degradation_colocation[j][i])-1)/(len(dictList_degradation_colocation[j][i])-2)
#    print numerator1
#    #print dictList_degradation_colocation[runningList[a+1]][runningList[a]]
#    #print numerator1

#APPENDING DEGRADATION SHUTTER
for (b,a) in enumerate(fList11):
    #print a
    if a in siriuscolocationListExperiments:
        index = a
    else:
        if a in siriusbenchListExperiments:
            dictList_degradation_shutter[index][a].append(fList11[b+1])

for (b,a) in enumerate(fList8):
    if a in siriuscolocationListExperiments:
        index = a
    else:
        if a in siriusbenchListExperiments:
            dictList_degradation_shutter3[index][a].append(fList8[b+1])

for a in xrange(0,len(siriusrunningList2),2):
    j = siriusrunningList2[a+1]
    i = siriusrunningList2[a]
    #print i,j,dictList_degradation_shutter[j][i]
#APPENDING DEGRADATION SHUTTER2 as shutter and colocation values are tab separated
for a in xrange(0,len(siriusrunningList2),2):
    j = siriusrunningList2[a+1]
    i = siriusrunningList2[a]
    for elem in dictList_degradation_shutter[j][i]:
        dictList_degradation_shutter2[j][i].extend(elem.strip().split('\t'))

    for elem in dictList_degradation_shutter3[j][i]:
        dictList_degradation_shutter4[j][i].extend(elem.strip().split('\t'))
    #print dictList_degradation_shutter2[j][i]

mcf_xaxis2 = ()
mcf_yaxis2 = ()
mcf_yaxis3 = ()
mcf_yaxis_abs2 = ()
mcf_yaxis_abs3 = ()
mcf_error2 = ()
mcf_error3 = ()
for a in xrange(0,len(siriusrunningList2),2):
    j = siriusrunningList2[a+1]
    i = siriusrunningList2[a]
    #print i,j
    #print i
    #print dictList_single_vm[i]
    #print dictList_degradation_colocation[j][i]
    #print dictList_degradation_shutter2[j][i]
    denominator1 = sum(float(n) for (m,n) in enumerate(dictList_single_vm[i]) if m!=0 and m!=len(dictList_single_vm[i])-1)/(len(dictList_single_vm[i])-2)
    numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_colocation[j][i]))/(len(dictList_degradation_colocation[j][i]))
    shutter_temp_list = []
    shutter_temp_list2 = []
    colo_temp_list = []
    colo_temp_list2 = []
    degradation_temp_list = []
    degradation_temp_list2 = []
    error_temp_list = []
    error_temp_list2 = []
    #print numerator1
    #print denominator1
    for (count,item) in enumerate(dictList_degradation_shutter2[j][i]):
        if count%2==0:
            colo_temp_list.append(item)
        if count%2==1:
            shutter_temp_list.append(item)

    for (count,item) in enumerate(dictList_degradation_shutter4[j][i]):
        if count%2==0:
            colo_temp_list2.append(item)
        if count%2==1:
            shutter_temp_list2.append(item)

    for (count,item) in enumerate(shutter_temp_list):
        degradation_temp_list.append(abs((((float(shutter_temp_list[count])/float(colo_temp_list[count]))-(numerator1/denominator1))/(float(shutter_temp_list[count])/float(colo_temp_list[count])))*100))

    shutter_temp_list.sort()
    shutter_temp_list2.sort()
    colo_temp_list.sort()
    colo_temp_list2.sort()
    #print shutter_temp_list
    #print colo_temp_list
    #print dictList_degradation_shutter2[j][i]
    denominator2 = sum(float(n) for (m,n) in enumerate(shutter_temp_list) if m!=0 and m!=len(dictList_single_vm[i])-1)/(len(dictList_single_vm[i])-2)/len(shutter_temp_list)
    numerator2 = sum(float(n) for (m,n) in enumerate(colo_temp_list) if m!=0 and m!=len(dictList_single_vm[i])-1)/(len(dictList_single_vm[i])-2 )/len(colo_temp_list)
    for (m,n) in enumerate(shutter_temp_list):
        ratio=float(n)/float(colo_temp_list[m])
        error_temp_list.append(abs((((ratio)-(numerator1/denominator1))/(numerator1/denominator1))*100))
    plot_degradation_error[j][i]=np.std(error_temp_list)

    denominator3 = sum(float(n) for (m,n) in enumerate(shutter_temp_list2))/(len(shutter_temp_list2))
    numerator3 = sum(float(n) for (m,n) in enumerate(colo_temp_list2))/(len(colo_temp_list2))
    for (m,n) in enumerate(shutter_temp_list2):
        ratio=float(n)/float(colo_temp_list2[m])
        error_temp_list2.append(abs((((ratio)-(numerator3/denominator3))/(numerator1/denominator1))*100))
    plot_degradation_error2[j][i]=np.std(error_temp_list2)

    #print numerator2
    #print denominator2
    del shutter_temp_list
    del colo_temp_list
    del degradation_temp_list
    del shutter_temp_list2
    del colo_temp_list2
    del degradation_temp_list2
    plot_degradation[j][i] = (((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100
    plot_degradation_abs[j][i] = abs((((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100)
    plot_degradation2[j][i] = (((numerator3/denominator3)-(numerator1/denominator1))/(numerator1/denominator1))*100
    plot_degradation_abs2[j][i] = abs((((numerator3/denominator3)-(numerator1/denominator1))/(numerator1/denominator1))*100)
    #print j,i,plot_degradation[j][i]
    #print plot_degradation_error[j][i]
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    mcf_xaxis2 = mcf_xaxis2 + (i,)
    mcf_yaxis2 = mcf_yaxis2 + (plot_degradation[j][i],)
    mcf_yaxis3 = mcf_yaxis3 + (plot_degradation2[j][i],)
    mcf_yaxis_abs2 = mcf_yaxis_abs2 + (plot_degradation_abs[j][i],)
    mcf_yaxis_abs3 = mcf_yaxis_abs3 + (plot_degradation_abs2[j][i],)
    mcf_error2 = mcf_error2 + (plot_degradation_error[j][i],)
    mcf_error3 = mcf_error3 + (plot_degradation_error2[j][i],)
    #print numerator2,denominator2,numerator2/denominator2
    #print denominator2/numerator2
    print j,i,plot_degradation[j][i],plot_degradation2[j][i]
            #print (((numerator2/denominator2)-(numerator1/denominator1))/(numerator2/denominator2))*100
#print np.mean(yaxis2)

benchListBaseline = [ 'gcc', 'perlbench', 'leslie3d', 'povray', 'libquantum', 'astar', 'bzip2', 'milc', 'namd', 'calculix', 'h264ref', 'sphinx3', 'zeusmp', 'gobmk', 'hmmer', 'tonto', 'bwaves', 'gromacs', 'dealII', 'sjeng', 'lbm', 'xalancbmk', 'gamess', 'cactusADM', 'soplex', 'GemsFDTD', 'omnetpp', 'mcf' ]
benchListExperiments = [ 'gcc', 'perlbench', 'leslie3d', 'povray', 'libquantum', 'astar', 'bzip2', 'milc', 'namd', 'calculix', 'h264ref', 'sphinx3', 'zeusmp', 'gobmk', 'hmmer', 'tonto', 'bwaves', 'gromacs', 'dealII', 'sjeng', 'lbm', 'xalancbmk', 'gamess', 'cactusADM', 'soplex', 'GemsFDTD', 'omnetpp', 'mcf' ]
colocationListBaseline = [ 'colocating with lbm', 'colocating with povray', 'colocating with milc', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
colocationListExperiments = [ 'colocating with lbm', 'colocating with povray', 'colocating with milc', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]

runningList2 = [  'perlbench', 'colocating with milc', 'mcf', 'colocating with milc', 'leslie3d', 'colocating with milc', 'povray', 'colocating with milc', 'libquantum', 'colocating with milc', 'astar', 'colocating with milc', 'bzip2', 'colocating with milc', 'milc', 'colocating with milc', 'namd', 'colocating with milc', 'calculix', 'colocating with milc', 'h264ref', 'colocating with milc', 'gobmk', 'colocating with milc', 'hmmer', 'colocating with milc', 'tonto', 'colocating with milc', 'sphinx3', 'colocating with milc', 'zeusmp', 'colocating with milc', 'bwaves', 'colocating with milc', 'gromacs', 'colocating with milc', 'dealII', 'colocating with milc', 'sjeng', 'colocating with milc', 'lbm', 'colocating with milc', 'xalancbmk', 'colocating with milc', 'gamess', 'colocating with milc', 'cactusADM', 'colocating with milc', 'soplex', 'colocating with milc', 'GemsFDTD', 'colocating with milc', 'omnetpp', 'colocating with milc' ]

siriusbenchListBaseline = [ 'gmm', 'dnn_asr', 'surf-fe', 'surf-fd', 'stem', 'regex', 'crf', 'img-imc', 'img-dig', 'img-face', 'nlp-pos', 'nlp-chk', 'nlp-ner']
siriusbenchListExperiments = [ 'gmm', 'dnn_asr', 'surf-fe', 'surf-fd', 'stem', 'regex', 'crf', 'img-imc', 'img-dig', 'img-face', 'nlp-pos', 'nlp-chk', 'nlp-ner']
siriuscolocationListBaseline = [ 'colocating with lbm', 'colocating with povray', 'colocating with astar', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
siriuscolocationListExperiments = [ 'colocating with lbm', 'colocating with povray', 'colocating with perlbench', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
siriusrunningList2 = [ 'gmm', 'colocating with milc', 'dnn_asr', 'colocating with milc', 'surf-fe', 'colocating with milc', 'surf-fd', 'colocating with milc', 'stem', 'colocating with milc', 'regex', 'colocating with milc', 'crf', 'colocating with milc', 'img-imc', 'colocating with milc', 'img-dig', 'colocating with milc', 'img-face', 'colocating with milc', 'nlp-pos', 'colocating with milc', 'nlp-chk', 'colocating with milc', 'nlp-ner' , 'colocating with milc']


def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%.2f'%float(height))

def autolabel2(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%.2f'%float(height))

def add_line(ax, xpos, ypos):
    line = plt.Line2D([xpos, xpos], [ypos + .1, ypos - .5], transform=ax.transAxes, linewidth=2, color='black')
    line.set_clip_on(False)
    ax.add_line(line)


filename = 'shutter_cpi_70'
#fList = [s.strip() for s in open('../../papergraphs/2.fullspec/accuracy/libquantumcorunner/single_vm_ground_truth/shutter_cpi_1000.txt').readlines()]
#fList2 = [s.strip() for s in open('../../papergraphs/2.fullspec/accuracy/libquantumcorunner/degradation_ground_truth/shutter_cpi_1000.txt').readlines()]
#fList3 = [s.strip() for s in open('../../papergraphs/2.fullspec/accuracy/libquantumcorunner/experiment_1/%s.txt' % filename).readlines()]
fList3= [s.strip() for s in open('../../papergraphs/accuracy/milccorunner/priorwork/shutter_cpi_5.txt').readlines()]

fList4 = [s.strip() for s in open('../../papergraphs/accuracy/milccorunner/singlevm/shutter_cpi_1000.txt').readlines()]
fList5 = [s.strip() for s in open('../../papergraphs/accuracy/milccorunner/degradation/shutter_cpi_1000.txt').readlines()]
fList6 = [s.strip() for s in open('../../papergraphs/accuracy/milccorunner/snapshot/%s.txt' % filename).readlines()]

fList8= [s.strip() for s in open('../../papergraphs/accuracy/milccorunner/siriusdjinn/priorwork/shutter_cpi_4.txt').readlines()]

fList9 = [s.strip() for s in open('../../papergraphs/accuracy/libquantumcorunner/siriusdjinn/singlevm/shutter_cpi_1000.txt').readlines()]
fList10 = [s.strip() for s in open('../../papergraphs/accuracy/milccorunner/siriusdjinn/degradation/shutter_cpi_1000.txt').readlines()]
fList11 = [s.strip() for s in open('../../papergraphs/accuracy/milccorunner/siriusdjinn/snapshot/shutter_cpi_75.txt').readlines()]


dictList_single_vm = defaultdict(list)
dictList_degradation_colocation = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter2 = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter3 = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter4 = defaultdict(lambda  : defaultdict(list))
plot_degradation = defaultdict(dict)
plot_degradation2 = defaultdict(dict)
plot_degradation_error = defaultdict(dict)
plot_degradation_error2 = defaultdict(dict)
plot_degradation_abs = defaultdict(dict)
plot_degradation_abs2 = defaultdict(dict)

for (b,a) in enumerate(fList4):
    if a in benchListBaseline:
        dictList_single_vm[a].append(fList4[b+1])

#SORTING LIST CONTAING VALUES OF SINGLE SPEC RUNS INSIDE VMs
for i in benchListBaseline:
    dictList_single_vm[i].sort()
    #print i,dictList_single_vm[i]

for (b,a) in enumerate(fList5):
    #print a
    if a in colocationListBaseline:
       #print a
       index = a
    else:
        if a in benchListExperiments:
            #print a
            dictList_degradation_colocation[index][a].append(fList5[b+1])

#sorting the ground truth values
for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]
    dictList_degradation_colocation[j][i].sort()
    #print j,i,dictList_degradation_colocation[j][i]



#APPENDING DEGRADATION SHUTTER
for (b,a) in enumerate(fList6):
    if a in colocationListExperiments:
        index = a
    else:
        if a in benchListExperiments:
            dictList_degradation_shutter[index][a].append(fList6[b+1])

for (b,a) in enumerate(fList3):
    if a in colocationListExperiments:
        index = a
    else:
        if a in benchListExperiments:
            dictList_degradation_shutter3[index][a].append(fList3[b+1])

for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]
    #print i,j,dictList_degradation_shutter[j][i]
#APPENDING DEGRADATION SHUTTER2 as shutter and colocation values are tab separated
for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]
    for elem in dictList_degradation_shutter[j][i]:
        dictList_degradation_shutter2[j][i].extend(elem.strip().split('\t'))

    for elem in dictList_degradation_shutter3[j][i]:
        dictList_degradation_shutter4[j][i].extend(elem.strip().split('\t'))
    #print dictList_degradation_shutter2[j][i]

specmilc_yaxis2 = ()
specmilc_yaxis3 = ()
specmilc_yaxis_abs2 = ()
specmilc_yaxis_abs3 = ()
specmilc_error2 = ()
specmilc_error3 = ()
specmilc_xaxis2 = ()
for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]
    #print i,j
    #print dictList_single_vm[i]
    #print dictList_degradation_colocation[j][i]
    #print dictList_degradation_shutter2[j][i]
    denominator1 = sum(float(n) for (m,n) in enumerate(dictList_single_vm[i]) if m!=0 and m!=len(dictList_single_vm[i])-1)/(len(dictList_single_vm[i])-2)
    numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_colocation[j][i]))/(len(dictList_degradation_colocation[j][i]))
    shutter_temp_list = []
    shutter_temp_list2 = []
    colo_temp_list = []
    colo_temp_list2 = []
    degradation_temp_list = []
    degradation_temp_list2 = []
    error_temp_list = []
    error_temp_list2 = []
    #print numerator1
    #print denominator1
    for (count,item) in enumerate(dictList_degradation_shutter2[j][i]):
        if count%2==0:
            colo_temp_list.append(item)
        if count%2==1:
            shutter_temp_list.append(item)

    for (count,item) in enumerate(dictList_degradation_shutter4[j][i]):
        if count%2==0:
            colo_temp_list2.append(item)
        if count%2==1:
            shutter_temp_list2.append(item)

    for (count,item) in enumerate(shutter_temp_list):
        degradation_temp_list.append(abs((((float(shutter_temp_list[count])/float(colo_temp_list[count]))-(numerator1/denominator1))/(float(shutter_temp_list[count])/float(colo_temp_list[count])))*100))

    shutter_temp_list.sort()
    shutter_temp_list2.sort()
    colo_temp_list.sort()
    colo_temp_list2.sort()
    #print shutter_temp_list
    #print colo_temp_list
    #print dictList_degradation_shutter2[j][i]
    denominator2 = sum(float(n) for (m,n) in enumerate(shutter_temp_list) if m!=0 and m!=len(shutter_temp_list)-1)/(len(shutter_temp_list)-2)
    numerator2 = sum(float(n) for (m,n) in enumerate(colo_temp_list) if m!=0 and m!=len(colo_temp_list)-1)/(len(colo_temp_list)-2)
    for (m,n) in enumerate(shutter_temp_list):
        ratio=float(n)/float(colo_temp_list[m])
        error_temp_list.append(abs((((ratio)-(numerator1/denominator1))/(numerator1/denominator1))*100))
    plot_degradation_error[j][i]=np.std(error_temp_list)

    denominator3 = sum(float(n) for (m,n) in enumerate(shutter_temp_list2))/(len(shutter_temp_list2))
    numerator3 = sum(float(n) for (m,n) in enumerate(colo_temp_list2))/(len(colo_temp_list2))
    for (m,n) in enumerate(shutter_temp_list2):
        ratio=float(n)/float(colo_temp_list2[m])
        error_temp_list2.append(abs((((ratio)-(numerator3/denominator3))/(numerator1/denominator1))*100))
    plot_degradation_error2[j][i]=np.std(error_temp_list2)

    #print numerator2
    #print denominator2
    del shutter_temp_list
    del colo_temp_list
    del degradation_temp_list
    del shutter_temp_list2
    del colo_temp_list2
    del degradation_temp_list2
    plot_degradation[j][i] = (((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100
    plot_degradation_abs[j][i] = abs((((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100)
    plot_degradation2[j][i] = (((numerator3/denominator3)-(numerator1/denominator1))/(numerator1/denominator1))*100
    plot_degradation_abs2[j][i] = abs((((numerator3/denominator3)-(numerator1/denominator1))/(numerator1/denominator1))*100)
    #print j,i,plot_degradation[j][i]
    #print plot_degradation_error[j][i]
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    specmilc_xaxis2 = specmilc_xaxis2 + (i,)
    specmilc_yaxis2 = specmilc_yaxis2 + (plot_degradation[j][i],)
    specmilc_yaxis3 = specmilc_yaxis3 + (plot_degradation2[j][i],)
    specmilc_yaxis_abs2 = specmilc_yaxis_abs2 + (plot_degradation_abs[j][i],)
    specmilc_yaxis_abs3 = specmilc_yaxis_abs3 + (plot_degradation_abs2[j][i],)
    specmilc_error2 = specmilc_error2 + (plot_degradation_error[j][i],)
    specmilc_error3 = specmilc_error3 + (plot_degradation_error2[j][i],)


#width=0.25
#x = np.arange(len(yaxis2))
#fig = plt.figure(figsize=(28, 5))
##bar1 = plt.bar( x, yaxis, width, color="r", label='colocating with libquatum (avg = %.2f)' %(np.mean(yaxis_abs)))
#bar1 = plt.bar( x, yaxis_abs3, width, color="k", yerr=error3, label='Shuttering (mean: %.2f)' %(np.mean(yaxis_abs3)))
#bar2 = plt.bar( x+width, yaxis_abs2, width, color="lightgrey", yerr=error2, label='Snapshot (mean: %.2f)' %(np.mean(yaxis_abs2)))
#
#plt.ylabel( 'Estimation error (%)',fontsize='25' )
##plt.title('Error in predicting degradation when co-locating with milc')
#plt.xticks(x + width/2.0, xaxis2, rotation='30', size='23',  ha='center', va='top')
#plt.yticks(np.arange(0,50,10),size='25')
#plt.ylim(0,50)
#plt.xlim(-1,27)
#plt.grid()
#plt.tight_layout()
#plt.legend(loc=9, ncol=2, prop={'size':28})
##plt.savefig('milc_accuracy.pdf', dpi=125)

del dictList_single_vm
del dictList_degradation_colocation
del dictList_degradation_shutter
del dictList_degradation_shutter2
del dictList_degradation_shutter3
del dictList_degradation_shutter4
del plot_degradation
del plot_degradation2
del plot_degradation_error
del plot_degradation_error2
del plot_degradation_abs
del plot_degradation_abs2

dictList_single_vm = defaultdict(list)
dictList_degradation_colocation = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter2 = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter3 = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter4 = defaultdict(lambda  : defaultdict(list))
plot_degradation = defaultdict(dict)
plot_degradation2 = defaultdict(dict)
plot_degradation_error = defaultdict(dict)
plot_degradation_error2 = defaultdict(dict)
plot_degradation_abs = defaultdict(dict)
plot_degradation_abs2 = defaultdict(dict)

for (b,a) in enumerate(fList9):
    if a in siriusbenchListBaseline:
        dictList_single_vm[a].append(fList9[b+1])

#SORTING LIST CONTAING VALUES OF SINGLE SPEC RUNS INSIDE VMs
for i in siriusbenchListBaseline:
    dictList_single_vm[i].sort()
    #print i,dictList_single_vm[i]

for (b,a) in enumerate(fList10):
    #print a
    if a in siriuscolocationListBaseline:
       #print a
       index = a
    else:
        if a in siriusbenchListExperiments:
            #print a
            dictList_degradation_colocation[index][a].append(fList10[b+1])

#sorting the ground truth values
for a in xrange(0,len(siriusrunningList2),2):
    j = siriusrunningList2[a+1]
    i = siriusrunningList2[a]
    #print i,j
    dictList_degradation_colocation[j][i].sort()
    #print j,i,dictList_degradation_colocation[j][i]

#for a in xrange(0,len(runningList),2):
#    j = runningList[a+1]
#    i = runningList[a]
#    numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_colocation[j][i]) if m!=0 and m!=len(dictList_degradation_colocation[j][i])-1)/(len(dictList_degradation_colocation[j][i])-2)
#    print numerator1
#    #print dictList_degradation_colocation[runningList[a+1]][runningList[a]]
#    #print numerator1

#APPENDING DEGRADATION SHUTTER
for (b,a) in enumerate(fList11):
    #print a
    if a in siriuscolocationListExperiments:
        index = a
    else:
        if a in siriusbenchListExperiments:
            dictList_degradation_shutter[index][a].append(fList11[b+1])

for (b,a) in enumerate(fList8):
    if a in siriuscolocationListExperiments:
        index = a
    else:
        if a in siriusbenchListExperiments:
            dictList_degradation_shutter3[index][a].append(fList8[b+1])

for a in xrange(0,len(siriusrunningList2),2):
    j = siriusrunningList2[a+1]
    i = siriusrunningList2[a]
    #print i,j,dictList_degradation_shutter[j][i]
#APPENDING DEGRADATION SHUTTER2 as shutter and colocation values are tab separated
for a in xrange(0,len(siriusrunningList2),2):
    j = siriusrunningList2[a+1]
    i = siriusrunningList2[a]
    for elem in dictList_degradation_shutter[j][i]:
        dictList_degradation_shutter2[j][i].extend(elem.strip().split('\t'))

    for elem in dictList_degradation_shutter3[j][i]:
        dictList_degradation_shutter4[j][i].extend(elem.strip().split('\t'))
    #print dictList_degradation_shutter2[j][i]

milc_xaxis2 = ()
milc_yaxis2 = ()
milc_yaxis3 = ()
milc_yaxis_abs2 = ()
milc_yaxis_abs3 = ()
milc_error2 = ()
milc_error3 = ()
for a in xrange(0,len(siriusrunningList2),2):
    j = siriusrunningList2[a+1]
    i = siriusrunningList2[a]
    print i,j
    #print i
    #print dictList_single_vm[i]
    print dictList_degradation_colocation[j][i]
    #print dictList_degradation_shutter2[j][i]
    denominator1 = sum(float(n) for (m,n) in enumerate(dictList_single_vm[i]) if m!=0 and m!=len(dictList_single_vm[i])-1)/(len(dictList_single_vm[i])-2)
    numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_colocation[j][i]))/(len(dictList_degradation_colocation[j][i]))
    shutter_temp_list = []
    shutter_temp_list2 = []
    colo_temp_list = []
    colo_temp_list2 = []
    degradation_temp_list = []
    degradation_temp_list2 = []
    error_temp_list = []
    error_temp_list2 = []
    #print numerator1
    #print denominator1
    for (count,item) in enumerate(dictList_degradation_shutter2[j][i]):
        if count%2==0:
            colo_temp_list.append(item)
        if count%2==1:
            shutter_temp_list.append(item)

    for (count,item) in enumerate(dictList_degradation_shutter4[j][i]):
        if count%2==0:
            colo_temp_list2.append(item)
        if count%2==1:
            shutter_temp_list2.append(item)

    for (count,item) in enumerate(shutter_temp_list):
        degradation_temp_list.append(abs((((float(shutter_temp_list[count])/float(colo_temp_list[count]))-(numerator1/denominator1))/(float(shutter_temp_list[count])/float(colo_temp_list[count])))*100))

    shutter_temp_list.sort()
    shutter_temp_list2.sort()
    colo_temp_list.sort()
    colo_temp_list2.sort()
    #print shutter_temp_list
    #print colo_temp_list
    #print dictList_degradation_shutter2[j][i]
    denominator2 = sum(float(n) for (m,n) in enumerate(shutter_temp_list) if m!=0 and m!=len(dictList_single_vm[i])-1)/(len(dictList_single_vm[i])-2)/len(shutter_temp_list)
    numerator2 = sum(float(n) for (m,n) in enumerate(colo_temp_list) if m!=0 and m!=len(dictList_single_vm[i])-1)/(len(dictList_single_vm[i])-2 )/len(colo_temp_list)
    for (m,n) in enumerate(shutter_temp_list):
        ratio=float(n)/float(colo_temp_list[m])
        error_temp_list.append(abs((((ratio)-(numerator1/denominator1))/(numerator1/denominator1))*100))
    plot_degradation_error[j][i]=np.std(error_temp_list)

    denominator3 = sum(float(n) for (m,n) in enumerate(shutter_temp_list2))/(len(shutter_temp_list2))
    numerator3 = sum(float(n) for (m,n) in enumerate(colo_temp_list2))/(len(colo_temp_list2))
    for (m,n) in enumerate(shutter_temp_list2):
        ratio=float(n)/float(colo_temp_list2[m])
        error_temp_list2.append(abs((((ratio)-(numerator3/denominator3))/(numerator1/denominator1))*100))
    plot_degradation_error2[j][i]=np.std(error_temp_list2)

    #print numerator2
    #print denominator2
    del shutter_temp_list
    del colo_temp_list
    del degradation_temp_list
    del shutter_temp_list2
    del colo_temp_list2
    del degradation_temp_list2
    plot_degradation[j][i] = (((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100
    plot_degradation_abs[j][i] = abs((((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100)
    plot_degradation2[j][i] = (((numerator3/denominator3)-(numerator1/denominator1))/(numerator1/denominator1))*100
    plot_degradation_abs2[j][i] = abs((((numerator3/denominator3)-(numerator1/denominator1))/(numerator1/denominator1))*100)
    #print j,i,plot_degradation[j][i]
    #print plot_degradation_error[j][i]
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    milc_xaxis2 = milc_xaxis2 + (i,)
    milc_yaxis2 = milc_yaxis2 + (plot_degradation[j][i],)
    milc_yaxis3 = milc_yaxis3 + (plot_degradation2[j][i],)
    milc_yaxis_abs2 = milc_yaxis_abs2 + (plot_degradation_abs[j][i],)
    milc_yaxis_abs3 = milc_yaxis_abs3 + (plot_degradation_abs2[j][i],)
    milc_error2 = milc_error2 + (plot_degradation_error[j][i],)
    milc_error3 = milc_error3 + (plot_degradation_error2[j][i],)
    #print numerator2,denominator2,numerator2/denominator2
    #print denominator2/numerator2
    print j,i,plot_degradation[j][i],plot_degradation2[j][i]
            #print (((numerator2/denominator2)-(numerator1/denominator1))/(numerator2/denominator2))*100
#print np.mean(yaxis2)

benchListBaseline = [ 'gcc', 'perlbench', 'leslie3d', 'povray', 'libquantum', 'astar', 'bzip2', 'milc', 'namd', 'calculix', 'h264ref', 'sphinx3', 'zeusmp', 'gobmk', 'hmmer', 'tonto', 'bwaves', 'gromacs', 'dealII', 'sjeng', 'lbm', 'xalancbmk', 'gamess', 'cactusADM', 'soplex', 'GemsFDTD', 'omnetpp', 'mcf' ]
benchListExperiments = [ 'gcc', 'perlbench', 'leslie3d', 'povray', 'libquantum', 'astar', 'bzip2', 'milc', 'namd', 'calculix', 'h264ref', 'sphinx3', 'zeusmp', 'gobmk', 'hmmer', 'tonto', 'bwaves', 'gromacs', 'dealII', 'sjeng', 'lbm', 'xalancbmk', 'gamess', 'cactusADM', 'soplex', 'GemsFDTD', 'omnetpp', 'mcf' ]
colocationListBaseline = [ 'colocating with lbm', 'colocating with milc', 'colocating with astar', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
colocationListExperiments = [ 'colocating with lbm', 'colocating with milc', 'colocating with perlbench', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
runningList = [  'perlbench', 'colocating with milc', 'mcf', 'colocating with milc', 'leslie3d', 'colocating with milc', 'povray', 'colocating with milc', 'libquantum', 'colocating with milc', 'astar', 'colocating with milc', 'bzip2', 'colocating with milc', 'milc', 'colocating with milc', 'namd', 'colocating with milc', 'calculix', 'colocating with milc', 'h264ref', 'colocating with milc', 'gobmk', 'colocating with milc', 'hmmer', 'colocating with milc', 'tonto', 'colocating with milc', 'sphinx3', 'colocating with milc', 'zeusmp', 'colocating with milc', 'bwaves', 'colocating with milc', 'gromacs', 'colocating with milc', 'dealII', 'colocating with milc', 'sjeng', 'colocating with milc', 'lbm', 'colocating with milc', 'xalancbmk', 'colocating with milc', 'gamess', 'colocating with milc', 'cactusADM', 'colocating with milc', 'soplex', 'colocating with milc', 'GemsFDTD', 'colocating with milc', 'omnetpp', 'colocating with milc' ]
runningList2 = [  'leslie3d', 'colocating with milc', 'zeusmp', 'colocating with milc', 'milc', 'colocating with milc', 'namd', 'colocating with milc', 'calculix', 'colocating with milc', 'gobmk', 'colocating with milc', 'hmmer', 'colocating with milc', 'tonto', 'colocating with milc', 'sphinx3', 'colocating with milc', 'bwaves', 'colocating with milc', 'gromacs', 'colocating with milc', 'dealII', 'colocating with milc', 'sjeng', 'colocating with milc', 'gamess', 'colocating with milc', 'cactusADM', 'colocating with milc', 'soplex', 'colocating with milc', 'GemsFDTD', 'colocating with milc' ]
runningList3 = [  'perlbench', 'colocating with milc', 'mcf', 'colocating with milc', 'povray', 'colocating with milc', 'libquantum', 'colocating with milc', 'astar', 'colocating with milc', 'bzip2', 'colocating with milc', 'h264ref', 'colocating with milc',  'lbm', 'colocating with milc', 'xalancbmk', 'colocating with milc', 'omnetpp', 'colocating with milc' ]

siriusbenchListBaseline = [ 'gmm', 'dnn_asr', 'surf-fe', 'surf-fd', 'stem', 'regex', 'crf', 'img-imc', 'img-dig', 'img-face', 'nlp-pos', 'nlp-chk', 'nlp-ner']
siriusbenchListExperiments = [ 'gmm', 'dnn_asr', 'surf-fe', 'surf-fd', 'stem', 'regex', 'crf', 'img-imc', 'img-dig', 'img-face', 'nlp-pos', 'nlp-chk', 'nlp-ner']
siriuscolocationListBaseline = [ 'colocating with lbm', 'colocating with povray', 'colocating with astar', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
siriuscolocationListExperiments = [ 'colocating with lbm', 'colocating with povray', 'colocating with perlbench', 'colocating with astar', 'colocating with libquantum', 'colocating with povray', 'colocating with omnetpp', 'colocating with mcf' ]
siriusrunningList2 = [ 'gmm', 'colocating with libquantum', 'dnn_asr', 'colocating with libquantum', 'surf-fe', 'colocating with libquantum', 'surf-fd', 'colocating with libquantum', 'stem', 'colocating with libquantum', 'regex', 'colocating with libquantum', 'crf', 'colocating with libquantum', 'img-imc', 'colocating with libquantum', 'img-dig', 'colocating with libquantum', 'img-face', 'colocating with libquantum', 'nlp-pos', 'colocating with libquantum', 'nlp-chk', 'colocating with libquantum', 'nlp-ner' , 'colocating with libquantum']

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%.2f'%float(height))

def autolabel2(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%.2f'%float(height))

def add_line(ax, xpos, ypos):
    line = plt.Line2D([xpos, xpos], [ypos + .1, ypos - .5], transform=ax.transAxes, linewidth=2, color='black')
    line.set_clip_on(False)
    ax.add_line(line)

filename = 'shutter_cpi_10'

fList3= [s.strip() for s in open('../../papergraphs/mixcorunner/priorwork/shutter_cpi_4.txt').readlines()]

fList4 = [s.strip() for s in open('../../papergraphs/mixcorunner/singlevm/shutter_cpi_1000.txt').readlines()]
fList5 = [s.strip() for s in open('../../papergraphs/mixcorunner/degradation/shutter_cpi_1000.txt').readlines()]
fList6 = [s.strip() for s in open('../../papergraphs/mixcorunner/snapshot/%s.txt' % filename).readlines()]
fList7 = [s.strip() for s in open('../../papergraphs/mixcorunner/degradation/shutter_cpi_100.txt').readlines()]

fList8= [s.strip() for s in open('../../papergraphs/mixcorunner/siriusdjinn/priorwork/shutter_cpi_4.txt').readlines()]

fList9 = [s.strip() for s in open('../../papergraphs/accuracy/libquantumcorunner/siriusdjinn/singlevm/shutter_cpi_1000.txt').readlines()]
fList10 = [s.strip() for s in open('../../papergraphs/mixcorunner/siriusdjinn/degradation/shutter_cpi_1000.txt').readlines()]
fList11 = [s.strip() for s in open('../../papergraphs/mixcorunner/siriusdjinn/snapshot/shutter_cpi_75.txt').readlines()]

dictList_single_vm = defaultdict(list)
dictList_degradation_colocation = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter2 = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter3 = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter4 = defaultdict(lambda  : defaultdict(list))
plot_degradation = defaultdict(dict)
plot_degradation2 = defaultdict(dict)
plot_degradation_error = defaultdict(dict)
plot_degradation_error2 = defaultdict(dict)
plot_degradation_abs = defaultdict(dict)
plot_degradation_abs2 = defaultdict(dict)

for (b,a) in enumerate(fList4):
    if a in benchListBaseline:
        dictList_single_vm[a].append(fList4[b+1])

#SORTING LIST CONTAING VALUES OF SINGLE SPEC RUNS INSIDE VMs
for i in benchListBaseline:
    dictList_single_vm[i].sort()
    #print i,dictList_single_vm[i]

for (b,a) in enumerate(fList5):
    #print a
    if a in colocationListBaseline:
       #print a
       index = a
    else:
        if a in benchListExperiments:
            #print a
            dictList_degradation_colocation[index][a].append(fList5[b+1])

#sorting the ground truth values
for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]
    dictList_degradation_colocation[j][i].sort()
    #print j,i,dictList_degradation_colocation[j][i]


#APPENDING DEGRADATION SHUTTER
for (b,a) in enumerate(fList6):
    if a in colocationListExperiments:
        index = a
    else:
        if a in benchListExperiments:
            dictList_degradation_shutter[index][a].append(fList6[b+1])

for (b,a) in enumerate(fList3):
    if a in colocationListExperiments:
        index = a
    else:
        if a in benchListExperiments:
            dictList_degradation_shutter3[index][a].append(fList3[b+1])

for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]
    #print i,j,dictList_degradation_shutter[j][i]
#APPENDING DEGRADATION SHUTTER2 as shutter and colocation values are tab separated
for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]
    for elem in dictList_degradation_shutter[j][i]:
        dictList_degradation_shutter2[j][i].extend(elem.strip().split('\t'))

    for elem in dictList_degradation_shutter3[j][i]:
        dictList_degradation_shutter4[j][i].extend(elem.strip().split('\t'))
    #print dictList_degradation_shutter2[j][i]

specmix_yaxis2 = ()
specmix_yaxis3 = ()
specmix_yaxis_abs2 = ()
specmix_yaxis_abs3 = ()
specmix_error2 = ()
specmix_error3 = ()
specmix_xaxis2 = ()
for a in xrange(0,len(runningList2),2):
    j = runningList2[a+1]
    i = runningList2[a]
    #print i,j
    #print dictList_single_vm[i]
    #print dictList_degradation_colocation[j][i]
    #print dictList_degradation_shutter2[j][i]
    denominator1 = sum(float(n) for (m,n) in enumerate(dictList_single_vm[i]) if m!=0 and m!=len(dictList_single_vm[i])-1)/(len(dictList_single_vm[i])-2)
    numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_colocation[j][i]))/(len(dictList_degradation_colocation[j][i]))
    shutter_temp_list = []
    shutter_temp_list2 = []
    colo_temp_list = []
    colo_temp_list2 = []
    degradation_temp_list = []
    degradation_temp_list2 = []
    error_temp_list = []
    error_temp_list2 = []
    #print numerator1
    #print denominator1
    for (count,item) in enumerate(dictList_degradation_shutter2[j][i]):
        if count%2==0:
            colo_temp_list.append(item)
        if count%2==1:
            shutter_temp_list.append(item)

    for (count,item) in enumerate(dictList_degradation_shutter4[j][i]):
        if count%2==0:
            colo_temp_list2.append(item)
        if count%2==1:
            shutter_temp_list2.append(item)

    for (count,item) in enumerate(shutter_temp_list):
        degradation_temp_list.append(abs((((float(shutter_temp_list[count])/float(colo_temp_list[count]))-(numerator1/denominator1))/(float(shutter_temp_list[count])/float(colo_temp_list[count])))*100))

    shutter_temp_list.sort()
    shutter_temp_list2.sort()
    colo_temp_list.sort()
    colo_temp_list2.sort()
    #print shutter_temp_list
    #print colo_temp_list
    #print dictList_degradation_shutter2[j][i]
    denominator2 = sum(float(n) for (m,n) in enumerate(shutter_temp_list))/len(shutter_temp_list)
    numerator2 = sum(float(n) for (m,n) in enumerate(colo_temp_list))/len(colo_temp_list)
    for (m,n) in enumerate(shutter_temp_list):
        ratio=float(n)/float(colo_temp_list[m])
        error_temp_list.append(abs((((ratio)-(numerator1/denominator1))/(numerator1/denominator1))*100))
    plot_degradation_error[j][i]=np.std(error_temp_list)

    denominator3 = sum(float(n) for (m,n) in enumerate(shutter_temp_list2))/(len(shutter_temp_list2))
    numerator3 = sum(float(n) for (m,n) in enumerate(colo_temp_list2))/(len(colo_temp_list2))
    for (m,n) in enumerate(shutter_temp_list2):
        ratio=float(n)/float(colo_temp_list2[m])
        error_temp_list2.append(abs((((ratio)-(numerator3/denominator3))/(numerator1/denominator1))*100))
    plot_degradation_error2[j][i]=np.std(error_temp_list2)

    #print numerator2
    #print denominator2
    del shutter_temp_list
    del colo_temp_list
    del degradation_temp_list
    del shutter_temp_list2
    del colo_temp_list2
    del degradation_temp_list2
    plot_degradation[j][i] = (((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100
    plot_degradation_abs[j][i] = abs((((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100)
    plot_degradation2[j][i] = (((numerator3/denominator3)-(numerator1/denominator1))/(numerator1/denominator1))*100
    plot_degradation_abs2[j][i] = abs((((numerator3/denominator3)-(numerator1/denominator1))/(numerator1/denominator1))*100)
    #print j,i,plot_degradation[j][i]
    #print plot_degradation_error[j][i]
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    #xaxis2 = xaxis2 + (i,)
    #yaxis2 = yaxis2 + (plot_degradation[j][i],)
    #yaxis3 = yaxis3 + (plot_degradation2[j][i],)
    #yaxis_abs2 = yaxis_abs2 + (plot_degradation_abs[j][i],)
    #yaxis_abs3 = yaxis_abs3 + (plot_degradation_abs2[j][i],)
    #error2 = error2 + (plot_degradation_error[j][i],)
    #error3 = error3 + (plot_degradation_error2[j][i],)
    #print numerator2,denominator2,numerator2/denominator2
    #print denominator2/numerator2
    #print j,i,plot_degradation[j][i]
            #print (((numerator2/denominator2)-(numerator1/denominator1))/(numerator2/denominator2))*100
#print np.mean(yaxis2)


del dictList_degradation_colocation
dictList_degradation_colocation = defaultdict(lambda  : defaultdict(list))

for (b,a) in enumerate(fList5):
    #print a
    if a in colocationListBaseline:
       #print a
       index = a
    else:
        if a in benchListExperiments:
            #print index,a
            dictList_degradation_colocation[index][a].append(fList5[b+1])
            #print dictList_degradation_colocation[index][a]

#sorting the ground truth values
for a in xrange(0,len(runningList3),2):
    j = runningList3[a+1]
    i = runningList3[a]
    dictList_degradation_colocation[j][i].sort()
    #print j,i,dictList_degradation_colocation[j][i]


for a in xrange(0,len(runningList3),2):
    j = runningList3[a+1]
    i = runningList3[a]
    #print i,j
    #print dictList_single_vm[i]
    #print dictList_degradation_colocation[j][i]
    #print dictList_degradation_shutter2[j][i]
    denominator1 = sum(float(n) for (m,n) in enumerate(dictList_single_vm[i]) if m!=0 and m!=len(dictList_single_vm[i])-1)/(len(dictList_single_vm[i])-2)
    numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_colocation[j][i]))/(len(dictList_degradation_colocation[j][i]))
    shutter_temp_list = []
    shutter_temp_list2 = []
    colo_temp_list = []
    colo_temp_list2 = []
    degradation_temp_list = []
    degradation_temp_list2 = []
    error_temp_list = []
    error_temp_list2 = []
    #print numerator1
    #print denominator1
    #for (count,item) in enumerate(dictList_degradation_shutter2[j][i]):
    #    if count%2==0:
    #        colo_temp_list.append(item)
    #    if count%2==1:
    #        shutter_temp_list.append(item)

    for (count,item) in enumerate(dictList_degradation_shutter4[j][i]):
        if count%2==0:
            colo_temp_list2.append(item)
        if count%2==1:
            shutter_temp_list2.append(item)

    #for (count,item) in enumerate(shutter_temp_list):
    #    degradation_temp_list.append(abs((((float(shutter_temp_list[count])/float(colo_temp_list[count]))-(numerator1/denominator1))/(float(shutter_temp_list[count])/float(colo_temp_list[count])))*100))

    #shutter_temp_list.sort()
    shutter_temp_list2.sort()
    #colo_temp_list.sort()
    colo_temp_list2.sort()

    denominator3 = sum(float(n) for (m,n) in enumerate(shutter_temp_list2))/(len(shutter_temp_list2))
    numerator3 = sum(float(n) for (m,n) in enumerate(colo_temp_list2))/(len(colo_temp_list2))
    for (m,n) in enumerate(shutter_temp_list2):
        ratio=float(n)/float(colo_temp_list2[m])
        error_temp_list2.append(abs((((ratio)-(numerator3/denominator3))/(numerator1/denominator1))*100))
    plot_degradation_error2[j][i]=np.std(error_temp_list2)

    #print numerator2
    #print denominator2
    #del shutter_temp_list
    #del colo_temp_list
    #del degradation_temp_list
    del shutter_temp_list2
    del colo_temp_list2
    del degradation_temp_list2
    #plot_degradation[j][i] = (((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100
    #plot_degradation_abs[j][i] = abs((((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100)
    plot_degradation2[j][i] = (((numerator3/denominator3)-(numerator1/denominator1))/(numerator1/denominator1))*100
    plot_degradation_abs2[j][i] = abs((((numerator3/denominator3)-(numerator1/denominator1))/(numerator1/denominator1))*100)
    #print j,i,plot_degradation[j][i]
    #print plot_degradation_error[j][i]
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    #xaxis2 = xaxis2 + (i,)
    #yaxis2 = yaxis2 + (plot_degradation[j][i],)
    #yaxis3 = yaxis3 + (plot_degradation2[j][i],)
    #yaxis_abs2 = yaxis_abs2 + (plot_degradation_abs[j][i],)
    #yaxis_abs3 = yaxis_abs3 + (plot_degradation_abs2[j][i],)
    #error2 = error2 + (plot_degradation_error[j][i],)
    #error3 = error3 + (plot_degradation_error2[j][i],)
    #print numerator2,denominator2,numerator2/denominator2
    #print denominator2/numerator2
    #print j,i,plot_degradation[j][i]
            #print (((numerator2/denominator2)-(numerator1/denominator1))/(numerator2/denominator2))*100

del dictList_degradation_colocation
dictList_degradation_colocation = defaultdict(lambda  : defaultdict(list))

for (b,a) in enumerate(fList7):
    #print a
    if a in colocationListBaseline:
       #print a
       index = a
    else:
        if a in benchListExperiments:
            #print index,a
            dictList_degradation_colocation[index][a].append(fList7[b+1])
            #print dictList_degradation_colocation[index][a]

#sorting the ground truth values
for a in xrange(0,len(runningList3),2):
    j = runningList3[a+1]
    i = runningList3[a]
    dictList_degradation_colocation[j][i].sort()
    #print j,i,dictList_degradation_colocation[j][i]


for a in xrange(0,len(runningList3),2):
    j = runningList3[a+1]
    i = runningList3[a]
    print i,j
    #print dictList_single_vm[i]
    #print dictList_degradation_colocation[j][i]
    #print dictList_degradation_shutter2[j][i]
    denominator1 = sum(float(n) for (m,n) in enumerate(dictList_single_vm[i]) if m!=0 and m!=len(dictList_single_vm[i])-1)/(len(dictList_single_vm[i])-2)
    numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_colocation[j][i]))/(len(dictList_degradation_colocation[j][i]))
    shutter_temp_list = []
    shutter_temp_list2 = []
    colo_temp_list = []
    colo_temp_list2 = []
    degradation_temp_list = []
    degradation_temp_list2 = []
    error_temp_list = []
    error_temp_list2 = []
    #print numerator1
    #print denominator1
    for (count,item) in enumerate(dictList_degradation_shutter2[j][i]):
        if count%2==0:
            colo_temp_list.append(item)
        if count%2==1:
            shutter_temp_list.append(item)

    #for (count,item) in enumerate(dictList_degradation_shutter4[j][i]):
    #    if count%2==0:
    #        colo_temp_list2.append(item)
    #    if count%2==1:
    #        shutter_temp_list2.append(item)

    #for (count,item) in enumerate(shutter_temp_list):
    #    degradation_temp_list.append(abs((((float(shutter_temp_list[count])/float(colo_temp_list[count]))-(numerator1/denominator1))/(float(shutter_temp_list[count])/float(colo_temp_list[count])))*100))

    shutter_temp_list.sort()
    #shutter_temp_list2.sort()
    colo_temp_list.sort()
    #colo_temp_list2.sort()
    #print shutter_temp_list
    #print colo_temp_list
    #print dictList_degradation_shutter2[j][i]
    denominator2 = sum(float(n) for (m,n) in enumerate(shutter_temp_list))/len(shutter_temp_list)
    numerator2 = sum(float(n) for (m,n) in enumerate(colo_temp_list))/len(colo_temp_list)
    for (m,n) in enumerate(shutter_temp_list):
        ratio=float(n)/float(colo_temp_list[m])
        error_temp_list.append(abs((((ratio)-(numerator1/denominator1))/(numerator1/denominator1))*100))
    plot_degradation_error[j][i]=np.std(error_temp_list)

    #denominator3 = sum(float(n) for (m,n) in enumerate(shutter_temp_list2))/(len(shutter_temp_list2))
    #numerator3 = sum(float(n) for (m,n) in enumerate(colo_temp_list2))/(len(colo_temp_list2))
    #for (m,n) in enumerate(shutter_temp_list2):
    #    ratio=float(n)/float(colo_temp_list2[m])
    #    error_temp_list2.append(abs((((ratio)-(numerator3/denominator3))/(numerator1/denominator1))*100))
    #plot_degradation_error2[j][i]=np.std(error_temp_list2)

    #print numerator2
    #print denominator2
    del shutter_temp_list
    del colo_temp_list
    del degradation_temp_list
    #del shutter_temp_list2
    #del colo_temp_list2
    #del degradation_temp_list2
    plot_degradation[j][i] = (((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100
    plot_degradation_abs[j][i] = abs((((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100)
    #plot_degradation2[j][i] = (((numerator3/denominator3)-(numerator1/denominator1))/(numerator1/denominator1))*100
    #plot_degradation_abs2[j][i] = abs((((numerator3/denominator3)-(numerator1/denominator1))/(numerator1/denominator1))*100)
    #print j,i,plot_degradation[j][i]
    #print plot_degradation_error[j][i]
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    #xaxis2 = xaxis2 + (i,)
    #yaxis2 = yaxis2 + (plot_degradation[j][i],)
    #yaxis3 = yaxis3 + (plot_degradation2[j][i],)
    #yaxis_abs2 = yaxis_abs2 + (plot_degradation_abs[j][i],)
    #yaxis_abs3 = yaxis_abs3 + (plot_degradation_abs2[j][i],)
    #error2 = error2 + (plot_degradation_error[j][i],)
    #error3 = error3 + (plot_degradation_error2[j][i],)
    #print numerator2,denominator2,numerator2/denominator2
    #print denominator2/numerator2
    #print j,i,plot_degradation[j][i]
            #print (((numerator2/denominator2)-(numerator1/denominator1))/(numerator2/denominator2))*100

for a in xrange(0,len(runningList),2):
    j = runningList[a+1]
    i = runningList[a]
    specmix_xaxis2 = specmix_xaxis2 + (i,)
    specmix_yaxis2 = specmix_yaxis2 + (plot_degradation[j][i],)
    specmix_yaxis3 = specmix_yaxis3 + (plot_degradation2[j][i],)
    specmix_yaxis_abs2 = specmix_yaxis_abs2 + (plot_degradation_abs[j][i],)
    specmix_yaxis_abs3 = specmix_yaxis_abs3 + (plot_degradation_abs2[j][i],)
    specmix_error2 = specmix_error2 + (plot_degradation_error[j][i],)
    specmix_error3 = specmix_error3 + (plot_degradation_error2[j][i],)


#width=0.25
#x = np.arange(len(yaxis2))
#fig = plt.figure(figsize=(28, 5))
##bar1 = plt.bar( x, yaxis, width, color="r", label='colocating with libquatum (avg = %.2f)' %(np.mean(yaxis_abs)))
#bar1 = plt.bar( x, yaxis_abs3, width, color="k", yerr=error3, label='Shuttering (mean: %.2f)' %(np.mean(yaxis_abs3)))
#bar2 = plt.bar( x+width, yaxis_abs2, width, color="lightgrey", yerr=error2, label='Snapshot (mean: %.2f)' %(np.mean(yaxis_abs2)))
##bar3 = plt.bar( x+width+width, yaxis3, width, color="g", label='colocating with sphinx  (avg = %.2f)' %(np.mean(yaxis_abs3)))
##autolabel(bar1)
##autolabel(bar2)
#plt.ylabel( 'Estimation error (%)' ,fontsize='25')
##plt.title('Error in predicting degradation when co-locating with libquantum')
#plt.xticks(x + width/2.0, xaxis2, rotation='30', size='23',  ha='center', va='top')
##plt.yticks((-0.5,0,1,2,3,4),('','0','1','2','3','4'),size='23')
#plt.yticks(np.arange(0,50,10),size='25')
#plt.ylim(0,40)
#plt.xlim(-1,26)
#plt.grid()
#plt.tight_layout()
#plt.legend(loc=9, ncol=2, prop={'size':28})
##plt.savefig('mix_error.pdf', dpi=125)


del dictList_single_vm
del dictList_degradation_colocation
del dictList_degradation_shutter
del dictList_degradation_shutter2
del dictList_degradation_shutter3
del dictList_degradation_shutter4
del plot_degradation
del plot_degradation2
del plot_degradation_error
del plot_degradation_error2
del plot_degradation_abs
del plot_degradation_abs2

dictList_single_vm = defaultdict(list)
dictList_degradation_colocation = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter2 = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter3 = defaultdict(lambda  : defaultdict(list))
dictList_degradation_shutter4 = defaultdict(lambda  : defaultdict(list))
plot_degradation = defaultdict(dict)
plot_degradation2 = defaultdict(dict)
plot_degradation_error = defaultdict(dict)
plot_degradation_error2 = defaultdict(dict)
plot_degradation_abs = defaultdict(dict)
plot_degradation_abs2 = defaultdict(dict)

for (b,a) in enumerate(fList9):
    if a in siriusbenchListBaseline:
        dictList_single_vm[a].append(fList9[b+1])

#SORTING LIST CONTAING VALUES OF SINGLE SPEC RUNS INSIDE VMs
for i in siriusbenchListBaseline:
    dictList_single_vm[i].sort()
    #print i,dictList_single_vm[i]

for (b,a) in enumerate(fList10):
    #print a
    if a in siriuscolocationListBaseline:
       #print a
       index = a
    else:
        if a in siriusbenchListExperiments:
            #print a
            dictList_degradation_colocation[index][a].append(fList10[b+1])

#sorting the ground truth values
for a in xrange(0,len(siriusrunningList2),2):
    j = siriusrunningList2[a+1]
    i = siriusrunningList2[a]
    #print i,j
    dictList_degradation_colocation[j][i].sort()
    #print j,i,dictList_degradation_colocation[j][i]

#for a in xrange(0,len(runningList),2):
#    j = runningList[a+1]
#    i = runningList[a]
#    numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_colocation[j][i]) if m!=0 and m!=len(dictList_degradation_colocation[j][i])-1)/(len(dictList_degradation_colocation[j][i])-2)
#    print numerator1
#    #print dictList_degradation_colocation[runningList[a+1]][runningList[a]]
#    #print numerator1

#APPENDING DEGRADATION SHUTTER
for (b,a) in enumerate(fList11):
    #print a
    if a in siriuscolocationListExperiments:
        index = a
    else:
        if a in siriusbenchListExperiments:
            dictList_degradation_shutter[index][a].append(fList11[b+1])

for (b,a) in enumerate(fList8):
    if a in siriuscolocationListExperiments:
        index = a
    else:
        if a in siriusbenchListExperiments:
            dictList_degradation_shutter3[index][a].append(fList8[b+1])

for a in xrange(0,len(siriusrunningList2),2):
    j = siriusrunningList2[a+1]
    i = siriusrunningList2[a]
    #print i,j,dictList_degradation_shutter[j][i]
    #print i,j
#APPENDING DEGRADATION SHUTTER2 as shutter and colocation values are tab separated
for a in xrange(0,len(siriusrunningList2),2):
    j = siriusrunningList2[a+1]
    i = siriusrunningList2[a]
    #print i,j
    for elem in dictList_degradation_shutter[j][i]:
        dictList_degradation_shutter2[j][i].extend(elem.strip().split('\t'))
        #print dictList_degradation_shutter2[j][i]

    for elem in dictList_degradation_shutter3[j][i]:
        dictList_degradation_shutter4[j][i].extend(elem.strip().split('\t'))
    #print dictList_degradation_shutter2[j][i]

mix_xaxis2 = ()
mix_yaxis2 = ()
mix_yaxis3 = ()
mix_yaxis_abs2 = ()
mix_yaxis_abs3 = ()
mix_error2 = ()
mix_error3 = ()
for a in xrange(0,len(siriusrunningList2),2):
    j = siriusrunningList2[a+1]
    i = siriusrunningList2[a]
    #print i,j
    #print i
    #print dictList_single_vm[i]
    #print dictList_degradation_colocation[j][i]
    #print dictList_degradation_shutter2[j][i]
    denominator1 = sum(float(n) for (m,n) in enumerate(dictList_single_vm[i]) if m!=0 and m!=len(dictList_single_vm[i])-1)/(len(dictList_single_vm[i])-2)
    numerator1 = sum(float(n) for (m,n) in enumerate(dictList_degradation_colocation[j][i]))/(len(dictList_degradation_colocation[j][i]))
    shutter_temp_list = []
    shutter_temp_list2 = []
    colo_temp_list = []
    colo_temp_list2 = []
    degradation_temp_list = []
    degradation_temp_list2 = []
    error_temp_list = []
    error_temp_list2 = []
    #print numerator1
    #print denominator1
    for (count,item) in enumerate(dictList_degradation_shutter2[j][i]):
        if count%2==0:
            colo_temp_list.append(item)
        if count%2==1:
            shutter_temp_list.append(item)

    for (count,item) in enumerate(dictList_degradation_shutter4[j][i]):
        if count%2==0:
            colo_temp_list2.append(item)
        if count%2==1:
            shutter_temp_list2.append(item)

    #print '1 %s' %shutter_temp_list
    #print colo_temp_list
    for (count,item) in enumerate(shutter_temp_list):
        degradation_temp_list.append(abs((((float(shutter_temp_list[count])/float(colo_temp_list[count]))-(numerator1/denominator1))/(float(shutter_temp_list[count])/float(colo_temp_list[count])))*100))

    shutter_temp_list.sort()
    shutter_temp_list2.sort()
    colo_temp_list.sort()
    colo_temp_list2.sort()
    #print shutter_temp_list
    #print colo_temp_list
    #print dictList_degradation_shutter2[j][i]
    denominator2 = sum(float(n) for (m,n) in enumerate(shutter_temp_list))/len(shutter_temp_list)
    numerator2 = sum(float(n) for (m,n) in enumerate(colo_temp_list))/len(colo_temp_list)
    for (m,n) in enumerate(shutter_temp_list):
        ratio=float(n)/float(colo_temp_list[m])
        error_temp_list.append(abs((((ratio)-(numerator1/denominator1))/(numerator1/denominator1))*100))
    plot_degradation_error[j][i]=np.std(error_temp_list)

    denominator3 = sum(float(n) for (m,n) in enumerate(shutter_temp_list2))/(len(shutter_temp_list2))
    numerator3 = sum(float(n) for (m,n) in enumerate(colo_temp_list2))/(len(colo_temp_list2))
    for (m,n) in enumerate(shutter_temp_list2):
        ratio=float(n)/float(colo_temp_list2[m])
        error_temp_list2.append(abs((((ratio)-(numerator3/denominator3))/(numerator1/denominator1))*100))
    plot_degradation_error2[j][i]=np.std(error_temp_list2)

    #print numerator2
    #print denominator2
    del shutter_temp_list
    del colo_temp_list
    del degradation_temp_list
    del shutter_temp_list2
    del colo_temp_list2
    del degradation_temp_list2
    plot_degradation[j][i] = (((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100
    plot_degradation_abs[j][i] = abs((((numerator2/denominator2)-(numerator1/denominator1))/(numerator1/denominator1))*100)
    plot_degradation2[j][i] = (((numerator3/denominator3)-(numerator1/denominator1))/(numerator1/denominator1))*100
    plot_degradation_abs2[j][i] = abs((((numerator3/denominator3)-(numerator1/denominator1))/(numerator1/denominator1))*100)
    #print j,i,plot_degradation[j][i]
    #print plot_degradation_error[j][i]
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    #xaxis = xaxis + ('%s \n %s' %(i,j[16:]),)
    mix_xaxis2 = mix_xaxis2 + (i,)
    mix_yaxis2 = mix_yaxis2 + (plot_degradation[j][i],)
    mix_yaxis3 = mix_yaxis3 + (plot_degradation2[j][i],)
    mix_yaxis_abs2 = mix_yaxis_abs2 + (plot_degradation_abs[j][i],)
    mix_yaxis_abs3 = mix_yaxis_abs3 + (plot_degradation_abs2[j][i],)
    mix_error2 = mix_error2 + (plot_degradation_error[j][i],)
    mix_error3 = mix_error3 + (plot_degradation_error2[j][i],)
    #print numerator2,denominator2,numerator2/denominator2
    #print denominator2/numerator2
    print j,i,plot_degradation[j][i],plot_degradation2[j][i]
            #print (((numerator2/denominator2)-(numerator1/denominator1))/(numerator2/denominator2))*100
#print np.mean(yaxis2)




width=0.15
x = np.arange(len(speclib_yaxis2))
fig = plt.figure(figsize=(23, 5))
fig.subplots_adjust(bottom=0.5)
ax = fig.add_subplot(1,1,1)
#bar1 = plt.bar( x, yaxis, width, color="r", label='colocating with libquatum (avg = %.2f)' %(np.mean(yaxis_abs)))
#bar1 = plt.bar( x, lib_yaxis_abs3, width, color="r", yerr=lib_error3, label='Shuttering (avg = %.2f)' %(np.mean(lib_yaxis_abs3)))
bar2 = plt.bar( x, speclib_yaxis_abs2, width, color="y", yerr=speclib_error2, label='libquantum (avg = %.2f)' %(np.mean(speclib_yaxis_abs2)))
bar3 = plt.bar( x+width, specmcf_yaxis_abs2, width, color="r", yerr=specmcf_error2, label='mcf (avg = %.2f)' %(np.mean(specmcf_yaxis_abs2)))
bar4 = plt.bar( x+width+width, specmilc_yaxis_abs2, width, color="b", yerr=specmilc_error2, label='milc (avg = %.2f)' %(np.mean(specmilc_yaxis_abs2)))
bar5 = plt.bar( x+width+width+width, specmix_yaxis_abs2, width, color="g", yerr=specmilc_error2, label='mix (avg = %.2f)' %(np.mean(specmix_yaxis_abs2)))
#ly = len(lib_yaxis_abs3)
#add_line(ax, 0 * 1.0, -.1)
#add_line(ax, 1 * 1.0, -.1)
#add_line(ax, 1 * 0.675, -.1)
#add_line(ax, 1 * 0.845, -.1)
#scale = 40./ly
#scale = 27./ly
#for pos in xrange(ly + 1):
#    print pos
#    print scale
#    add_line(ax, pos * scale, -.1)
#scale = 34./ly
#for pos in xrange(ly + 1):
#    add_line(ax, pos * scale, -.1)
#bar3 = plt.bar( x+width+width, yaxis3, width, color="g", label='colocating with sphinx  (avg = %.2f)' %(np.mean(yaxis_abs3)))
#autolabel(bar1)
#autolabel(bar2)
plt.ylabel( 'Estimation error (%)', fontsize='19' )
#plt.title('Error in predicting degradation when co-locating with libquantum')
plt.xticks(x + width/2.0, speclib_xaxis2, rotation='90', size='18',  ha='center', va='top')
plt.yticks(np.arange(0,50,10),size='20')
plt.ylim(0,50)
plt.xlim(-0.2,26)
plt.grid()
plt.tight_layout()
plt.legend(loc=1, ncol=4, prop={'size':18})
#plt.savefig('accuracylibquantum.pdf', dpi=125)
#ax.text(5, -23, r'SPEC 2006', fontsize=20)
#ax.text(4, -23, r'Sirius Suite', fontsize=20)
#ax.text(10, -23, r'DjiNN & Tonic', fontsize=20)

import os as mars_awesome_os;
import matplotlib.pyplot as mars_awesome_plt;
mars_awesome_plt.savefig('spec-accuracy.eps', bbox_inches='tight');
mars_awesome_os.popen('epstopdf spec-accuracy.eps');
