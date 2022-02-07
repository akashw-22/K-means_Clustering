import matplotlib.pyplot as plt, random, numpy as np, csv, os

def getfile():

    files = os.listdir('csvfiles')
    print("select fileno..", files)
    file = "csvfiles/" + files[int(input())]
    return file


def getset(filename):

    set = []
    with open(filename ,'r') as csvfile:
        reader = list(csv.reader(csvfile, delimiter=','))
        for row, i in zip(reader, range(5000)):
            col = []
            #print(row)
            for el in row:
                if float(el):
                    col.append(el)
            #print(col)
            set.append([float(col[0]), float(col[1])])
    return set


def distance(x,y):
    return (x[0] - y[0])**2 + (x[1] - y[1])**2

def formcluster(centr, set):

    cluster = []
    for i in range(len(centr)):
        cluster.append([])
    for point in set:
        d = []
        for c in centr:
            d.append(distance(point, c))
        cluster[d.index(min(d))].append(point)
    return cluster

def kmeans(set, k):

    plt.ion()
    fig, ax = plt.subplots()
    ax.scatter([], [])
    centr = []
    centr = random.sample(set, k)

    print(centr)
    temp = []

    while True:
        cl = formcluster(centr, set)
        #print(cl)
        temp = []
        for i in cl:
            temp.append(list(np.mean(i, axis = 0)))

        if centr == temp:
            break
        else:
            centr = temp

        #print(centr)

        #fig.canvas.draw()
        #fig.canvas.flush_events()
        #plt.pause(0.1)
        #for i,j in zip(cl, ['red', 'blue', 'orange', 'green', 'violet', 'yellow']):
        #    for x,y in i:
        #        ax.scatter(x, y, s = 5, color = j)

        #for x,y in centr:
        #    ax.scatter(x, y, s=400, color = 'black', marker = 'X')


    #print(centr)

    for i,j in zip(cl, ['red', 'blue', 'orange', 'green', 'violet', 'yellow', 'indigo', 'lightgreen']):
        for x,y in i:
            ax.scatter(x, y, s = 25, color = j)

    for x,y in centr:
        ax.scatter(x, y, s=100, color = 'black', marker = 'X')


    plt.waitforbuttonpress()
    #fig.canvas.flush_events()
    #plt.pause(0.1)

    plt.show()

filename = getfile()
dataset = getset(filename)
#print(dataset)
print("Enter K value")
k = int(input())
kmeans(dataset,k)
