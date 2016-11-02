import networkx as nx


def singletons(gold, test):
    
    gold_size = 0
    test_size = 0
    found = 0
    
    for a, b in zip(gold, test):
        
        # graph data
        _gold_graph = a[0].edges()
        _gold_data = a[1]
        _gold_visited = []
        
        _test_graph = b[0].edges()
        _test_data = b[1]
        _test_visited = []
        
        # appending in-degree and out-degree
        for edge in _gold_graph:
            if edge[0] not in _gold_visited:
                _gold_visited.append(edge[0])
            if edge[1] not in _gold_visited:
                _gold_visited.append(edge[1])
        
        for edge in _test_graph:
            if edge[0] not in _test_visited:
                _test_visited.append(edge[0])
            if edge[1] not in _test_visited:
                _test_visited.append(edge[1])
            
        # finding dangling nodes
        for k, v in _gold_data.items():
            if k not in _gold_visited:
                gold_size += 1
                
        for k, v in _test_data.items():
            if k not in _test_visited:
                test_size += 1
                if k not in _gold_visited:
                    found += 1
                
    p = found / test_size
    r = found / gold_size
    f = 2 * ((p * r) / (p + r))
        
    
    print('{:<10} &{:<10} &{:<10} &{:<10} &{:<10} &{:<10}\\\\'.
                      format('Gold', 'Test', 'Match', 'Precision', 'Recall', 'F-score'))
    print('{:<10} &{:<10} &{:<10} &{:<10.4f} &{:<10.4f} &{:<10.4f}\\\\'.
                      format(gold_size, test_size, found, p, r, f))

    return (gold_size, test_size, found, p, r, f)           

def singletons_pos_frame(gold, test, pos=False, frame=False, sort=False):
    
    saved = []
    
    def check(current, pos_frame):
        
        gold_size = 0
        test_size = 0
        found = 0
        
        for a, b in zip(gold, test):

            # graph data
            _gold_graph = a[0].edges()
            _gold_data = a[1]
            _gold_visited = []

            _test_graph = b[0].edges()
            _test_data = b[1]
            _test_visited = []
            
            # appending in-degree and out-degree
            for edge in _gold_graph:
                if edge[0] not in _gold_visited:
                    _gold_visited.append(edge[0])
                if edge[1] not in _gold_visited:
                    _gold_visited.append(edge[1])

            for edge in _test_graph:
                if edge[0] not in _test_visited:
                    _test_visited.append(edge[0])
                if edge[1] not in _test_visited:
                    _test_visited.append(edge[1])

                    
            gold_node_pos_frame = []
            
            # finding dangling nodes
            for k, v in _gold_data.items():
                if k not in _gold_visited and v[pos_frame] == current:
                    gold_size += 1
                    gold_node_pos_frame.append((k, v[pos_frame]))

            for k, v in _test_data.items():
                if k not in _test_visited and v[pos_frame] == current:
                    test_size += 1
                    if k not in _gold_visited and (k, v[pos_frame]) in gold_node_pos_frame:
                        found += 1

        p = 0
        r = 0
        f = 0
        
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
        
        saved.append((current, gold_size, test_size, found, p, r, f))
            
        
    
    print('{:<20} &{:<10} &{:<10} &{:<10} &{:<10} &{:<10} &{:<10}\\\\'.
                          format('Pos/Frame', 'Gold', 'Test', 'Match', 'Precision', 'Recall', 'F-score'))
    
    if pos:
        for p in pos:
            check(p, 'pos')
            
    if frame:
        for f in frame:
            check(f, 'frame')
    
    if sort:
        saved = sorted(saved, key=lambda x: x[sort], reverse=True)
    
    for s in saved:
        print('{:<20} &{:<10} &{:<10} &{:<10} &{:<10.4f} &{:<10.4f} &{:<10.4f}\\\\'.
              format(s[0].replace('_', '\_'), s[1], s[2], s[3], s[4], s[5], s[6]))

    return saved
