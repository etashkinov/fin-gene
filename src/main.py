import quandl_dump as qd
import fracture
import graph

# GOOGL
# MSFT
# TSLA
df = qd.get("WIKI/CSCO")
result = fracture.get_point(df[['Adj. Close']])
print(result)
graph.show(df, result)

