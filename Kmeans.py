import matplotlib.pyplot as plt, random, numpy as np, csv, os

def getfile():

    files = os.listdir('csvfiles')
    print("select fileno..", files)
    file = "csvfiles/" + files[int(input())]
    return file


def getset(filename, d):

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

            cor = []
            for k in range(d):
                cor.append(float(col[k]))
            set.append(cor)
    #print(set)
    return set


def distance(x,y):

    dis = 0

    for i in range(len(x)):
        dis += (x[i] - y[i])**2

    #print(dis)
    return dis

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
    #centr = random.sample(set, k)
    centr = set[:k]

    #print(centr)
    temp = []

    while True:
        cl = formcluster(centr, set)
        #print(cl)
        temp = []
        for i in cl:
            #print(len(i))
            if len(i) == 0:
                temp.append(centr[cl.index(i)])
                #print("hit")
            else:
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


    print(centr)

    color = ['red', 'blue', 'orange', 'green', 'violet', 'yellow', 'indigo', 'lightgreen']

    if len(set[0]) == 2:
        for j,i in enumerate(cl):
            for x,y in i:
                ax.scatter(x, y, s = 25, color = color[j%8])


        for x,y in centr:
            ax.scatter(x, y, s=100, color = 'black', marker = 'X')


        plt.waitforbuttonpress()

        plt.show()

filename = getfile()
#print(dataset)
print("Enter K value")
k = int(input())
print("Enter Dimension")
dim = int(input())
dataset = getset(filename, dim)
kmeans(dataset,k)
