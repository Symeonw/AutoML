import numpy as np
import tensorflow as tf 
import matplotlib.pyplot as plt 

np.random.seed(42)
tf.random.set_seed(42)

n = 100
X = np.linspace(0,50,n)
y = np.linspace(0,50,n)
X += np.random.uniform(-10, 10, n)
y += np.random.uniform(-10, 10, n)

plt.scatter(X,y)

class LinearModel:
    def __init__(self):
        self.W = tf.Variable(13.0) # Weight #Can be any value as long as its not large
        self.b = tf.Variable(4.0)  # Bias #Can be any value as long as its not large

    def loss(self, y, y_pred):
        return tf.reduce_mean(tf.square(y - y_pred)) # Computes mean squared error
    
    def train(self, X, y, lr=0.0001, epochs=20, verbose=True):
        def train_step():
            with tf.GradientTape() as t:
                current_loss = self.loss(y, self.predict(X))

            dW, db = t.gradient(current_loss, [self.W, self.b])
            self.W.assign_sub(lr * dW)
            self.b.assign_sub(lr * db)

            return current_loss

        for epoch in range(epochs):
            current_loss = train_step()
            if verbose:
                print(f"Epoch {epoch}: Loss: {current_loss.numpy()}")

    def predict(self, X):
        return self.W * X + self.b

model = LinearModel()
model.train(X, y, epochs=40)
plt.scatter(X, y, label ="data")
plt.plot(X, model.predict(X), "r-", label="predicted")
plt.legend()
