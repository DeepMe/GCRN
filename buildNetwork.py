#coding: utf-8
from __future__ import print_function
from __future__ import division
import networkx as nx
import time
import pandas as pd
import matplotlib.pyplot as plt


INTERVEL = 604800
START_DATE = '2004-04-23 00:00:00'
END_DATE = '2004-10-28 00:00:00'

HISTORY_EDGES = []

def timestamp_datetime(value):
    format = '%Y-%m-%d %H:%M:%S'
    value = time.localtime(value)
    dt = time.strftime(format, value)
    return dt


def datetime_timestamp(dt):
    time.strptime(dt, '%Y-%m-%d %H:%M:%S')
    s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
    return int(s)


if __name__ == "__main__":
    df = pd.read_table('C:/data/CollegeMsg.txt', header=None, delim_whitespace=True)
    currentTime = datetime_timestamp(START_DATE)
    count = 1

    numNodes = []
    numEdges = []

    while True:
        if currentTime > datetime_timestamp('2004-10-31 00:00:00'):
            break
        current_edges = df[df[2] < currentTime]
        current_edges = current_edges[current_edges[2] > (currentTime - 4*INTERVEL)]
        # current_edges.to_csv('C:/data/CollegeMsg/{}.csv'.format(timestamp_datetime(begin)[:10]), index=False, header=False)
        source = current_edges[0].tolist()
        target = current_edges[1].tolist()
        edge_list = [(source[i], target[i]) for i in range(len(source))]
        G = nx.DiGraph()
        G.add_edges_from(edge_list, nodetype=int)
        # nx.write_edgelist(G, 'C:/data/CollegeMsg/{}.edgelist'.format(timestamp_datetime(currentTime)[:10]))
        # nx.write_edgelist(G, 'C:/data/CollegeMsg/{}.edgelist'.format(count))

        currentTime += INTERVEL

        print("network {} build finished".format(count))
        count += 1
        numNodes.append(G.number_of_nodes())
        numEdges.append(G.number_of_edges())

    plt.subplot(121)
    plt.plot(range(len(numNodes)), numNodes, marker='.', color='r')
    plt.xlabel("time")
    plt.ylabel("number of nodes")
    plt.subplot(122)
    plt.plot(range(len(numEdges)), numEdges, marker='*', color='b')
    plt.xlabel("time")
    plt.ylabel("number of edges")
    plt.show()
