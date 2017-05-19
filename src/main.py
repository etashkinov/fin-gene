import quandl_dump as qd
import fracture
import graph

companies = ('GOOGL', 'MSFT', 'TSLA', 'CSCO', 'TWTR', 'FB')

df = qd.get("WIKI/" + companies[3])
result = fracture.get_point(df[['Adj. Close']])
print(result)
graph.show(df, result)

