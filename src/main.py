import quandl_dump as qd
import fracture
import graph
#('GOOGL', 'MSFT', 'TSLA', 'CSCO', 'TWTR', 'FB', 'GOOD', 'GLAD', 'FIX', 'NUE', 'XOMA','HELE')

companies = qd.get_stored()

for c in companies:
    result = fracture.get_point(c[1][['Adj. Close']])
    print(c[0], result)

    if result:
        graph.show(c[0], c[1], result)

# companies = qd.get_list("NASDAQ")
# qd.dump(companies)


