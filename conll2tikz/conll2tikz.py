import networkx as nx
import sys

def create_graph_conll(conll, year=2015):
    """
    Conll file format: http://sdp.delph-in.net/2014/data.html
    """

    year = int(year)
    
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
            _info[_id] = {
                'form': _form,
                'lemma': _lemma,
                'pos': _pos,
                'top': _top,
                'pred': _pred,
            }

            if year == 2015:
                _frame = _words[6]
                _info[_id]['frame'] = _frame
            
            # Storing predicates
            if _pred:
                _preds.append(_id)
                
            if _top:
                _graph.add_edge(_id, _id, label='TOP')
            
            _graph.add_node(_id)
            
            # Storing edges
            start = 0
            if year == 2015:
                start = 7
            if year == 2014:
                start = 6
            for i in range(start, len(_words[start:]) + start):
                if _words[i] != '_':
                    _edges.append((_id, i-start-1, _words[i]))
    
    # cleanup on last sentence
    add_edges(_graph, _edges, _preds)

    for graph in graphs:
        edges = graph[0].edges(data='label')
        data = graph[1]
        root = ''
        for key, value in data.items():
            print(value['form'] + ' \\& ', end='')
            if value['top']:
                root = key
        print()
        for key, value in data.items():
            if 'frame' in value:
                print(value['frame'].replace('_', '\_') + ' \\& ', end='')
        print('\\\\')
        print('\deproot{{{}}}{{{}}}'.format(root, 'root'))
        for edge in edges:
            if edge[0] != edge[1]:
                label = edge[2].replace('_', '\_')
                dependent = edge[0]
                head = edge[1]
                print('\depedge{{{}}}{{{}}}{{{}}}'.format(head, dependent, label))
        
create_graph_conll(open(sys.argv[1]), sys.argv[2])