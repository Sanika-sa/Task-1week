import numpy as np
import matplotlib.pyplot as plt

# 1. Generate Synthetic Dataset (Simulating pattern/digit features)
np.random.seed(42)
N = 300  # number of points per class
D = 2   # dimensionality
K = 3   # number of classes
X = np.zeros((N * K, D))
y = np.zeros(N * K, dtype='uint8')

for j in range(K):
    ix = range(N * j, N * (j + 1))
    r = np.linspace(0.0, 1, N)  # radius
    t = np.linspace(j * 4, (j + 1) * 4, N) + np.random.randn(N) * 0.2  # theta
    X[ix] = np.c_[r * np.sin(t), r * np.cos(t)]
    y[ix] = j

X = X.T
Y = np.zeros((K, N * K))
Y[y, np.arange(N * K)] = 1

# 2. Initialize Network Parameters
input_size = D
hidden_size = 64
output_size = K

# Weights and biases
W1 = np.random.randn(hidden_size, input_size) * 0.01
b1 = np.zeros((hidden_size, 1))
W2 = np.random.randn(output_size, hidden_size) * 0.01
b2 = np.zeros((output_size, 1))

# Hyperparameters
learning_rate = 0.5
epochs = 1000
num_examples = X.shape[1]

loss_history = []
accuracy_history = []

# 3. Training Loop
for epoch in range(epochs):
    # --- Forward Propagation ---
    Z1 = np.dot(W1, X) + b1
    A1 = np.maximum(0, Z1)  # ReLU activation
    Z2 = np.dot(W2, A1) + b2
    
    # Softmax activation
    exp_scores = np.exp(Z2 - np.max(Z2, axis=0, keepdims=True))
    probs = exp_scores / np.sum(exp_scores, axis=0, keepdims=True)
    
    
    core_loss = -np.sum(Y * np.log(probs + 1e-9)) / num_examples
    loss_history.append(core_loss)
    
    preds = np.argmax(probs, axis=0)
    accuracy = np.mean(preds == y) * 100
    accuracy_history.append(accuracy)
    
    # --- Backpropagation ---
    dZ2 = probs - Y
    dW2 = np.dot(dZ2, A1.T) / num_examples
    db2 = np.sum(dZ2, axis=1, keepdims=True) / num_examples
    
    dA1 = np.dot(W2.T, dZ2)
    dZ1 = dA1 * (Z1 > 0)  
    dW1 = np.dot(dZ1, X.T) / num_examples
    db1 = np.sum(dZ1, axis=1, keepdims=True) / num_examples
    
    
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2
    
    if epoch % 100 == 0:
        print(f"Epoch {epoch}/{epochs} - Loss: {core_loss:.4f} - Accuracy: {accuracy:.2f}%")

plt.figure(figsize=(12, 5))


plt.subplot(1, 2, 1)
plt.plot(loss_history, color='red', linewidth=2)
plt.title("Training Loss over Epochs")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.grid(True)


plt.subplot(1, 2, 2)
plt.plot(accuracy_history, color='green', linewidth=2)
plt.title("Training Accuracy over Epochs")
plt.xlabel("Epochs")
plt.ylabel("Accuracy (%)")
plt.grid(True)

plt.tight_layout()
plt.show()