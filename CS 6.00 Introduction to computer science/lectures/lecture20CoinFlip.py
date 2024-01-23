########## Lecture 20a lesson handout

from pylab import * # type: ignore
import random, math

def flipTrial(numFlips):
    heads, tails = 0, 0
    for i in range(0, numFlips):
        coin = random.randint(0, 1)
        if coin == 0:
            heads += 1
        else:
            tails += 1
    return heads, tails

def simFlips(numFlips, numTrials):
    diffs = []
    for i in range(0, numTrials):
        heads, tails = flipTrial(numFlips)
        diffs.append(abs(heads - tails))
    diffs = array(diffs)
    diffMean = sum(diffs)/len(diffs)
    diffPercent = (diffs/float(numFlips))*100
    percentMean = sum(diffPercent)/len(diffPercent)
    hist(diffs)
    axvline(diffMean, color = 'r', label = 'Mean')
    legend()
    titleString = str(numFlips) + ' Flips, ' + str(numTrials) + ' Trials'
    title(titleString)
    xlabel('Difference between heads and tails')
    ylabel('Number of trials')
    figure()
    plot(diffPercent)
    axhline(percentMean, color = 'r', label = 'Mean') # type: ignore
    legend()
    title(titleString)
    xlabel('Trial Number')
    ylabel('Percent Difference between heads and tails')

simFlips(100, 100)
# figure()
# simFlips(5000, 100)
# simFlips(3, 4000)
show()
