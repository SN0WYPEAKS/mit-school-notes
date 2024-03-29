########## Lecture 21 lesson handout
import pylab

def getSpringData(fname):
    springData = open(fname, 'r')
    distances = []
    forces = []
    for line in springData:
        if line[0] == '#':
            continue
        line = line[:-1]
        elems = line.rsplit(':')
        distances.append(float(elems[0]))
        forces.append(float(elems[1]))
    return pylab.array(distances), pylab.array(forces)

distances, forces = getSpringData('springData.txt')
pylab.scatter(distances, forces)
pylab.xlabel('Distance (Meters)')
pylab.ylabel('|Force| (Newtons)')
pylab.title('Force vs. Distance for Spring')

# k, b = pylab.polyfit(distances, forces, 1)
# yVals = k*distances + b
# pylab.plot(distances, yVals, c = 'r', linewidth = 2)
# pylab.title('Force vs. Distance, k = ' + str(k))

pylab.show()
