import networkx as nx

def create_graph_conll(conll):
    """
    Conll file format: http://sdp.delph-in.net/2014/data.html
    """
    
    def add_edges(graph, edges, preds):
        for i in edges:
            _from = i[0]
            _to = preds[i[1] - 1]
            _label = i[2]
            graph.add_edge(_from, _to, label=_label)
    
    graphs = []
    _graph = False
    _edges = []
    _preds = []
    
    if conll.readline() != '#SDP 2015\n':
        return False
    
    for line in conll.readlines():
        
        # new line
        if line[0] == '#':
            
            # add edges
            if (_graph):
                add_edges(_graph, _edges, _preds)
                _edges = []
                _preds = []
                
            _graph = nx.DiGraph()
            _info = {}
            graphs.append([_graph, _info])
        
        # each line of sentence
        # id, form, lemma, pos, top, pred, [as many args as preds]
        elif len(line) > 1:
            _current_graph = graphs[len(graphs) - 1]
            _words = line.replace('\n', '').split('\t')
            _id = int(_words[0])
            _form = _words[1]
            _lemma = _words[2]
            _pos = _words[3]
            _top = _words[4] == '+'
            _pred = _words[5] == '+'
            _frame = _words[6]
            _info[_id] = {
                'form': _form,
                'lemma': _lemma,
                'pos': _pos,
                'top': _top,
                'pred': _pred,
                'frame': _frame
            }
            
            # Storing predicates
            if _pred:
                _preds.append(_id)
                
            if _top:
                _graph.add_edge(_id, _id, label='TOP')
            
            _graph.add_node(_id)
            
            # Storing edges
            for i in range(7, len(_words[7:]) + 7):
                if _words[i] != '_':
                    _edges.append((_id, i-6, _words[i]))
    
    # cleanup on last sentence
    add_edges(_graph, _edges, _preds)
    return graphs


def full_analysis(gold, test, name):
    """
    Precision, recall, F-score for dependencies
    """
    found = 0
    found_labeled = 0
    
    gold_size = 0
    gold_size_labeled = 0
    
    test_size = 0
    test_size_labeled = 0
    
    for a, b in zip(gold, test):
        
        # graphs
        g_gold = a[0].edges()
        g_gold_labeled = a[0].edges(data='label')
        g_test = b[0].edges()
        g_test_labeled = b[0].edges(data='label')
        
        # sizes
        gold_size += len(g_gold)
        gold_size_labeled += len(g_gold_labeled)
        test_size += len(g_test)
        test_size_labeled += len(g_test_labeled)
        
        for edge in g_test:
            if edge in g_gold:
                found += 1
                
        for edge in g_test_labeled:
            if edge in g_gold_labeled:
                found_labeled += 1
                
    p = round(found / test_size, 4)
    r = round(found / gold_size, 4)
    f = round(2 * ((p * r) / (p + r)), 4)
    
    pl = round(found_labeled / test_size_labeled, 4)
    rl = round(found_labeled / gold_size_labeled, 4)
    fl = round(2 * ((pl * rl) / (pl + rl)), 4)
    
    print(name)
    print('--------------------------------------')
    print('{:<20} {:<20} {:<20} {:<20}'.format('Type', 'precision', 'recall', 'f-score'))
    print('{:<20} {:<20.4f}& {:<20.4f}& {:<20.4f}'.format('Unlabeled', round(p, 4), round(r, 4), round(f, 4)))
    print('{:<20} {:<20.4f}& {:<20.4f}& {:<20.4f}\n'.format('Labeled', round(pl, 4), round(rl, 4), round(fl, 4)))


def get_args(conll):
    args = []
    for line in conll.readlines():
        if line[0] != '#' and len(line) > 1:
            _words = line.replace('\n', '').split('\t')
            for i in range(7, len(_words[7:]) + 7):
                if _words[i] != '_':
                    if _words[i] not in args:
                        args.append(_words[i])
    return args


def get_pos(conll):
    pos = []
    for line in conll.readlines():
        if line[0] != '#' and len(line) > 1:
            _words = line.replace('\n', '').split('\t')
            p = _words[3]
            if p not in pos:
                pos.append(p)
    return pos

def get_frame(conll):
    pos = []
    for line in conll.readlines():
        if line[0] != '#' and len(line) > 1:
            _words = line.replace('\n', '').split('\t')
            p = _words[6]
            if p not in pos:
                pos.append(p)
    return pos