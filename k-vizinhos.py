import matematica as mat
from collections import Counter

def raw_majority_vote(labels):
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]
    return winner

def majority_vote(labels):
    """presume que as etiquetas sao ordenadas da mais proxima para a mais distante"""
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count 
                       for count in vote_counts.values()
                       if count == winner_count])
    
    if num_winners == 1:
        return winner                       # vencedor unico, entao o devolve
    else:
        return majority_vote(labels[:-1])   # tenta novamente sem o mais distante

def knn_classify(k, labeled_points, new_point):
    """ cada ponto rotulado deveria ser um par (point, label) """

    # organiza os pontos rotulados do mais proximo para o mais distante
    by_distance = sorted(labeled_points,
                         key = lambda (point, _): mat.distance(point, new_point))

    # encontra os rotulos para os k mais proximos
    k_nearest_labels = [label for _, label in by_distance[:k]]

    # e os deixa votar
    return majority_vote(k_nearest_labels)