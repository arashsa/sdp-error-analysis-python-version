import networkx as nx

def predicate_argument_pos(gold, test, pos_frame, pos_frame_type, predicate_argument=1, sort=0):
    '''
    Checking predicate or argument pos.
    predicate_argument = 0 is argument
    predicate_argument = 1 is predicate and/or argument
    '''
    
    if predicate_argument == 0:
        print('arguments')
    elif predicate_argument == 1:
        print('predicates')
    
    # test
    count = 0
    
    gold_size = 0
    test_size = 0
    found = 0
    
    saved = []
    
    print('{:<20} &{:<10} &{:<10} &{:<10} &{:<10} &{:<10}\\\\'
          .format('Pos/frame', 'Gold', 'Test', 'Precision', 'Recall', 'F-score'))
    
    for p_f in pos_frame_type:
        
        gold_size = 0
        test_size = 0
        p = 0
        r = 0
        f = 0
        found = 0
    
        for a, b in zip(gold, test):

            # graph data
            gold_graph = a[0].edges()
            gold_data = a[1]
            gold_visited = []

            test_graph = b[0].edges()
            test_data = b[1]
            test_visited = []

            # get predicates or arguments
            for edge in gold_graph:
                if edge[predicate_argument] not in gold_visited and gold_data[edge[predicate_argument]][pos_frame] == p_f:
                    gold_visited.append(edge[predicate_argument])

            for edge in test_graph:
                if edge[predicate_argument] not in test_visited and test_data[edge[predicate_argument]][pos_frame] == p_f:
                    test_visited.append(edge[predicate_argument])

            # counts
            gold_size += len(gold_visited)
            test_size += len(test_visited)

            for i in test_visited:
                if i in gold_visited and test_data[i][pos_frame] == gold_data[i][pos_frame]:
                    found += 1
                
            try:
                p = found / test_size
            except ZeroDivisionError:
                pass

            try:
                r = found / gold_size
            except ZeroDivisionError:
                pass

            try:
                f = 2 * ((p * r) / (p + r))
            except ZeroDivisionError:
                pass
        
        saved.append((p_f, gold_size, test_size, p, r, f))
        
    saved = sorted(saved, key=lambda x: x[sort], reverse=True)

    for s in saved:
        if s[1] > 8:
            print('{:<20} &{:<10} &{:<10} &{:<10.4f} &{:<10.4f} &{:<10.4f}\\\\'
                  .format(s[0].replace('_', '\_'), s[1], s[2], s[3], s[4], s[5]))
    print()


def frame_pos(gold, test, pos_frame, pos_frame_type, sort=0):
    '''
    Frame POS for graph
    '''
    
    # for testing
    count = 0
    
    saved = []
    
    print('{:<20} &{:<10} &{:<10} &{:<10} &{:<10} &{:<10}'
          .format('Pos/frame', 'Gold', 'Test', 'Match', 'Precision', 'Recall', 'F-score'))
    
    for p_f in pos_frame_type:
        
        gold_size = 0
        test_size = 0
        p = 0
        r = 0
        f = 0
        found = 0
    
        for a, b in zip(gold, test):

            # graph data
            gold_graph = a[0].edges()
            gold_data = a[1]
            gold_visited = []

            test_graph = b[0].edges()
            test_data = b[1]
            test_visited = []

            # get predicates or arguments
            for edge in gold_graph:
                if edge not in gold_visited \
                and (gold_data[edge[0]][pos_frame] == p_f or gold_data[edge[1]][pos_frame] == p_f):
                    gold_visited.append(edge[0])
                    gold_visited.append(edge[1])

            for edge in test_graph:
                if edge not in test_visited \
                and (test_data[edge[0]][pos_frame] == p_f or test_data[edge[1]][pos_frame] == p_f):
                    test_visited.append(edge[0])
                    test_visited.append(edge[1])

            # counts
            gold_size += len(gold_visited)
            test_size += len(test_visited)

            for i in test_visited:
                if i in gold_visited and test_data[i][pos_frame] == gold_data[i][pos_frame]:
                    found += 1
                
            try:
                p = found / test_size
            except ZeroDivisionError:
                pass

            try:
                r = found / gold_size
            except ZeroDivisionError:
                pass

            try:
                f = 2 * ((p * r) / (p + r))
            except ZeroDivisionError:
                pass
        
        saved.append((p_f, gold_size, test_size, found, p, r, f))
        
    saved = sorted(saved, key=lambda x: x[sort], reverse=True)

    for s in saved:
        if s[1] > 8:
            print('{:<20} &{:<10} &{:<10} &{:<10.4f} &{:<10.4f} &{:<10.4f}'
                  .format(s[0], s[1], s[2], s[3], s[4], s[5]), s[6])
    print()
    return saved
                
                