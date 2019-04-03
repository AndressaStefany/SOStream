from math import exp
from utils import dist


def updateCluster(win_micro_cluster, vt, alpha, winner_neighborhood):
    win_micro_cluster['C'] = [(win_micro_cluster['n'] * (wi + vi)) / (win_micro_cluster['n'] + 1) for wi, vi in zip(win_micro_cluster['C'], vt)]
    win_micro_cluster['n'] += 1
    width_neighbor = win_micro_cluster['r'] ** 2
    for neighbor_micro_cluster in winner_neighborhood:
        influence = exp(-(dist(neighbor_micro_cluster['C'], win_micro_cluster['C'])/(2 * width_neighbor)))
        neighbor_micro_cluster['C'] = [a + alpha*influence*(b-a) for a, b in zip(neighbor_micro_cluster['C'], win_micro_cluster['C'])]