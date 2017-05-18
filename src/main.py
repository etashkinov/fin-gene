import quandl_dump as qd
import graph

df = qd.load_stock("WIKI/GOOGL")
print(df.tail())

graph.show(df, '2011-05-11')
