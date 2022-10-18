from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
iris = load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris.data,iris.target,test_size=0.2,random_state=22)
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)
estimator = KNeighborsClassifier(n_neighbors=5)
estimator.fit(x_train, y_train)
y_pre = estimator.predict(x_test)
print("预测值是:\n", y_pre)
print("预测值和真实值得对比是:\n",y_pre==y_test)
score = estimator.score(x_test,y_test)
print("准确率为:\n", score)