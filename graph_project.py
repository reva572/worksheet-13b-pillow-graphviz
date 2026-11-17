
import graphviz

dot = graphviz.Digraph(comment='My First Graph')

dot.attr(rankdir='LR')

dot.node('A', 'Start')
dot.node('B', 'Process')
dot.node('C', 'End')

dot.edge('A', 'Z')
dot.edge('B', 'C')

dot.render('my_first_graph', format='png', cleanup=True)

print("Graph created successfully!")

