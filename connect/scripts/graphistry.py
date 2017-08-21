import pandas
import graphistry

edges = pandas.read_csv('facebook_combined', sep=' ', names=['src', 'dst'])
graphistry.bind(source='src', destination='dst').plot(edges)
