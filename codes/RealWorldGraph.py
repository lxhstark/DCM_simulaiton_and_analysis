import networkx as nx
import pandas as pd
import scipy.stats as st

from codes.AnalysisToolFunction import test_shortpath_marginal_2, d_tolist

data = pd.read_csv('/Users/leah/summer_2017/DCM_simulation_and_analysis/output_data/wiki_vote/wiki-Vote.txt', header=3, sep='\t')
data.columns=['FromNodeId', 'ToNodeId']
edges = []
l = len(data.FromNodeId)
for i in range(0, l):
    edges.append((data.FromNodeId[i], data.ToNodeId[i]))

graph = nx.DiGraph()
graph.add_edges_from(edges)


result = test_shortpath_marginal_2(graph, 200)

#din = d_tolist(graph.in_degree())
#dout = d_tolist(graph.out_degree())

corr, p = st.pearsonr(din, dout)

# dict

#pr = nx.pagerank(graph)
#bc = nx.betweenness_centrality_source(graph)
