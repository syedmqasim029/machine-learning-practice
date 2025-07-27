from sklearn.module import Model
model = Model()
model.fit(X,y)
predictions = model.predict(X_new)
print(predictions)