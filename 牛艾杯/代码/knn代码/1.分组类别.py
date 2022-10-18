from sklearn.neighbors import KNeighborsClassifier
x = [[1],[2],[10],[20]]
y = [0,0,1,1]
estimator = KNeighborsClassifier(n_neighbors=1)
estimator.fit(x,y)
ret = estimator.predict([[0]])
print(ret)
ret1 = estimator.predict([[1]])
print(ret1)