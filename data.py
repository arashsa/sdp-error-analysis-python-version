from functions import create_graph_conll, full_analysis, get_args, get_pos, get_frame

class Data:
    def __init__(self):
        # test data
        self.dm = create_graph_conll(open('2015/test/en.id.dm.sdp'))
        self.dm_ood = create_graph_conll(open('2015/test/en.ood.dm.sdp'))
        self.psd = create_graph_conll(open('2015/test/en.id.psd.sdp'))
        self.psd_ood = create_graph_conll(open('2015/test/en.ood.psd.sdp'))
        
        # arguments
        self.dm_args = get_args(open('2015/test/en.id.dm.sdp'))
        self.dm_ood_args = get_args(open('2015/test/en.ood.dm.sdp'))
        self.psd_args = get_args(open('2015/test/en.id.psd.sdp'))
        self.psd_ood_args = get_args(open('2015/test/en.ood.psd.sdp'))

        # pos
        self.dm_pos = get_pos(open('2015/test/en.id.dm.sdp'))
        self.psd_pos = get_pos(open('2015/test/en.id.psd.sdp'))

        # frame
        self.dm_frame = get_frame(open('2015/test/en.id.dm.sdp'))
        self.psd_frame = get_frame(open('2015/test/en.id.psd.sdp'))

        # Lisbon
        self.lisbon_dm_closed = create_graph_conll(open('2015/submissions/Lisbon/en.id.closed.dm.1.sdp'))
        self.lisbon_dm_open = create_graph_conll(open('2015/submissions/Lisbon/en.id.open.dm.1.sdp'))
        self.lisbon_dm_closed_ood = create_graph_conll(open('2015/submissions/Lisbon/en.ood.closed.dm.1.sdp'))
        self.lisbon_dm_open_ood = create_graph_conll(open('2015/submissions/Lisbon/en.ood.open.dm.1.sdp'))
        self.lisbon_psd_closed = create_graph_conll(open('2015/submissions/Lisbon/en.id.closed.psd.1.sdp'))
        self.lisbon_psd_open = create_graph_conll(open('2015/submissions/Lisbon/en.id.open.psd.1.sdp'))
        self.lisbon_psd_closed_ood = create_graph_conll(open('2015/submissions/Lisbon/en.ood.closed.psd.1.sdp'))
        self.lisbon_psd_open_ood = create_graph_conll(open('2015/submissions/Lisbon/en.ood.open.psd.1.sdp'))

        # Peking
        self.peking_dm_closed = create_graph_conll(open('2015/submissions/Peking/en.id.closed.dm.1.sdp'))
        self.peking_dm_closed_2 = create_graph_conll(open('2015/submissions/Peking/en.id.closed.dm.2.sdp'))
        self.peking_dm_closed_ood = create_graph_conll(open('2015/submissions/Peking/en.ood.closed.dm.1.sdp'))
        self.peking_dm_closed_ood_2 = create_graph_conll(open('2015/submissions/Peking/en.ood.closed.dm.2.sdp'))

        self.peking_psd_closed = create_graph_conll(open('2015/submissions/Peking/en.id.closed.psd.1.sdp'))
        self.peking_psd_closed_2 = create_graph_conll(open('2015/submissions/Peking/en.id.closed.psd.2.sdp'))
        self.peking_psd_closed_ood = create_graph_conll(open('2015/submissions/Peking/en.ood.closed.psd.1.sdp'))
        self.peking_psd_closed_ood_2 = create_graph_conll(open('2015/submissions/Peking/en.ood.closed.psd.2.sdp'))

        # Turku
        self.turku_dm_gold = create_graph_conll(open('2015/submissions/Turku/en.id.gold.dm.1.sdp'))
        self.turku_dm_gold_2 = create_graph_conll(open('2015/submissions/Turku/en.id.gold.dm.2.sdp'))
        self.turku_dm_open = create_graph_conll(open('2015/submissions/Turku/en.id.open.dm.1.sdp'))
        self.turku_dm_open_2 = create_graph_conll(open('2015/submissions/Turku/en.id.open.dm.2.sdp'))
        self.turku_dm_gold_ood = create_graph_conll(open('2015/submissions/Turku/en.ood.gold.dm.1.sdp'))
        self.turku_dm_gold_ood_2 = create_graph_conll(open('2015/submissions/Turku/en.ood.gold.dm.2.sdp'))
        self.turku_dm_open_ood = create_graph_conll(open('2015/submissions/Turku/en.ood.open.dm.1.sdp'))
        self.turku_dm_open_ood_2 = create_graph_conll(open('2015/submissions/Turku/en.ood.open.dm.2.sdp'))

        self.turku_psd_gold = create_graph_conll(open('2015/submissions/Turku/en.id.gold.psd.1.sdp'))
        self.turku_psd_gold_2 = create_graph_conll(open('2015/submissions/Turku/en.id.gold.psd.2.sdp'))
        self.turku_psd_open = create_graph_conll(open('2015/submissions/Turku/en.id.open.psd.1.sdp'))
        self.turku_psd_open_2 = create_graph_conll(open('2015/submissions/Turku/en.id.open.psd.2.sdp'))
        self.turku_psd_gold_ood = create_graph_conll(open('2015/submissions/Turku/en.ood.gold.psd.1.sdp'))
        self.turku_psd_gold_ood_2 = create_graph_conll(open('2015/submissions/Turku/en.ood.gold.psd.2.sdp'))
        self.turku_psd_open_ood = create_graph_conll(open('2015/submissions/Turku/en.ood.open.psd.1.sdp'))
        self.turku_psd_open_ood_2 = create_graph_conll(open('2015/submissions/Turku/en.ood.open.psd.2.sdp'))