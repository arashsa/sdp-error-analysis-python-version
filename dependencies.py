import networkx as nx


def dependencies_by_type(types, gold, test, sort=False):
    """
    Precision, recall, F-score for dependencies
    """

    print('Dependencies by type')
    print('{:<18} &{:<10} &{:<10} &{:<10} &{:<10} &{:<10} &{:<10}'.
          format('Type', 'Gold', 'Test', 'Match', 'Precision', 'Recall', 'F-score'))

    saved = []

    for _type in types:
        
        found = 0
        gold_size = 0
        test_size = 0
        dependencies_total_gold = 0
        dependencies_total_test = 0
            
        for a, b in zip(gold, test):
        
            # graphs
            _gold = a[0].edges(data='label')
            _test = b[0].edges(data='label')
        
            # sizes
            for edge in _gold:
                dependencies_total_gold += 1
                _current_type = edge[2]
                if _current_type == _type:
                    gold_size += 1
                    
                    
            for edge in _test:
                dependencies_total_test += 1
                _current_type = edge[2]
                if _current_type == _type:
                    test_size += 1
                    
            for edge in _test:
                _current_type = edge[2]
                if edge in _gold and _current_type == _type:
                    found += 1
               
        p = 0 if test_size == 0 else found / test_size
        r = 0 if gold_size == 0 else found / gold_size
        if found > 0:
            f = 2 * ((p * r) / (p + r))
        else:
            f = 0
            
        if not sort and sort != 0:
            print('{:<18} &{:<10} &{:<10} &{:<10} &{:<10.4f} &{:<10.4f} &{:<10.4f}\\\\'
                  .format(_type, gold_size, test_size, found, round(p, 4), round(r, 4), round(f, 4)))
        else:
            saved.append((_type, gold_size, test_size, found, p, r, f))
    
    # For plotting
    make_table_type = []
    make_table_gold_size = []
    make_table_test_size = []
    make_table_match = []

    make_table_p = []
    make_table_r = []
    make_table_f = []
    
    if sort or sort == 0:
        sorted_list = sorted(saved, key=lambda x: x[sort], reverse=True)
        
        dep_count = 0
        for el in sorted_list:
            dep_count += 1
            print('{:<18} &{:<10} &{:<10} &{:<10} &{:<10.4f} &{:<10.4f} &{:<10.4f}\\\\'.
                  format(el[0].replace('_', '\_'), el[1], el[2], el[3], round(el[4], 4), round(el[5], 4), round(el[6], 4)))

            make_table_type.append(el[0])
            make_table_gold_size.append(el[1])
            make_table_test_size.append(el[2])
            make_table_match.append(el[3])

            make_table_p.append(round(el[4], 4))
            make_table_r.append(round(el[5], 4))
            make_table_f.append(round(el[6], 4))
            
    print('\nTotal number of dependencies gold: {}'.format(dependencies_total_gold))
    print('Total number of dependencies test: {}'.format(dependencies_total_test))
    print('Types: {}\n\n'.format(dep_count))

    return((make_table_type, make_table_gold_size, make_table_test_size, make_table_match, make_table_p, make_table_r, make_table_f))


def dependencies_by_length(gold, test, arg=False):
    """
    Precision, recall, F-score for dependencies by length
    """
    
    longest_g = 0
    longest_t = 0

    return_length = []
    return_gold = []
    return_pred = []
    return_match = []
    return_p = []
    return_r = []
    return_f = []
    
    if arg:
        print('Dependencies by length and specific type')
        print('{:<8} &{:<18} &{:<10} &{:<10} &{:<10} &{:<10} &{:<10} &{:<10}\\\\'.
              format('Length', 'Type', 'Gold', 'Test', 'Match', 'Precision', 'Recall', 'F-score'))
    else:
        print('Dependencies by length')
        print('{:<8} &{:<10} &{:<10} &{:<10} &{:<10} &{:<10} &{:<10}\\\\'.
              format('Length', 'Gold', 'Test', 'Match', 'Precision', 'Recall', 'F-score'))

    found = 0
    gold_size = 0
    test_size = 0

    for length in range(1, 100):
        
        for a, b in zip(gold, test):

            # graphs
            _gold = a[0].edges(data='label')
            _test = b[0].edges(data='label')

            # counting sizes
            for edge in _gold:
                start_end = sorted([edge[0], edge[1]])
                _len = start_end[1] - start_end[0]
                if _len > longest_g:
                    longest_g = _len
                if _len == length:
                    gold_size += 1

            for edge in _test:
                start_end = sorted([edge[0], edge[1]])
                _len = start_end[1] - start_end[0]
                if _len > longest_t:
                    longest_t = _len
                if _len == length:
                    if edge in _gold:
                        found += 1
                    test_size += 1
        
        if length % 3 == 0 and length != 0:
            p = 0 if test_size == 0 else found / test_size
            r = 0 if gold_size == 0 else found / gold_size
            if found > 0:
                f = 2 * ((p * r) / (p + r))
            else:
                f = 0
                
            if gold_size > 0:
                if arg:
                    print('{:<8} &{:<18} &{:<10} &{:<10} &{:<10} &{:<10.4f} &{:<10.4f} &{:<10.4f}\\\\'.
                        format(length-1, arg, gold_size, test_size, found, p, r, f))
                else:
                    print('{:<8} &{:<10} &{:<10} &{:<10} &{:<10.4f} &{:<10.4f} &{:<10.4f}\\\\'.
                        format(length, gold_size, test_size, found, p, r, f))

            return_length.append(length)
            return_gold.append(gold_size)
            return_pred.append(test_size)
            return_match.append(found)
            return_p.append(p)
            return_r.append(r)
            return_f.append(f)
            
            found = 0
            gold_size = 0
            test_size = 0
                

    print('Longest dependency in gold: {}'.format(longest_g))
    print('Longest dependency in test: {}'.format(longest_t))
    print()

    return((return_length, return_gold, return_pred, return_match, return_p, return_r, return_f))


def dependencies_by_sentence_length(gold, test):
    """
    Precision, recall, F-score for dependencies by length
    """

    results = []
    found = 0
    gold_size = 0
    test_size = 0

    # len(range(1, 51)) == 50
    for length in range(1, 61):
        
        for a, b in zip(gold, test):

            # graphs
            _gold = a[0].edges(data='label')
            _test = b[0].edges(data='label')
            sentence_length = len(a[1])

            # sentence length match
            if (sentence_length == length):
                gold_size += len(_gold)
                test_size += len(_test)
                for edge in _test:
                    if edge in _gold:
                        found += 1

        if length % 10 == 0:         
            p = 0 if test_size == 0 else found / test_size
            r = 0 if gold_size == 0 else found / gold_size
            if found > 0:
                f = 2 * ((p * r) / (p + r))
            else:
                f = 0
            results.append([p, r, f])

            found = 0
            gold_size = 0
            test_size = 0

    return results



                

def sentence_lengths(gold):
    """
    Returns sentence length, and average length
    """
    dependencies = [[] for a in range(56)]
    for length in range(56):
        for a in gold:
            if len(a[1]) == length:
                dependencies[length].append(a)
    sentences = [len(a) for a in dependencies]
    count = 0
    s = 0
    for a in gold:
        s += len(a[1])
        count += 1
    average = s / count
    return (sentences, average)
