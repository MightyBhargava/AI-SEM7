import numpy as np

class NeuralNetwork:
    def __init__(self, layers, activation='sigmoid'):
        self.layers = layers
        self.activation = activation
        self.weights = []
        self.biases = []
        self.initialize_parameters()

    def initialize_parameters(self):
        np.random.seed(1)
        self.weights = [np.random.randn(self.layers[i], self.layers[i-1]) * np.sqrt(1 / self.layers[i-1])
                        for i in range(1, len(self.layers))]
        self.biases = [np.zeros((self.layers[i], 1)) for i in range(1, len(self.layers))]

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def relu(self, z):
        return np.maximum(0, z)

    def sigmoid_derivative(self, z):
        return self.sigmoid(z) * (1 - self.sigmoid(z))

    def relu_derivative(self, z):
        z[z <= 0] = 0
        z[z > 0] = 1
        return z

    def forward_propagation(self, X):
        A = X.T
        for i in range(len(self.layers) - 1):
            Z = np.dot(self.weights[i], A) + self.biases[i]
            if self.activation == 'sigmoid':
                A = self.sigmoid(Z)
            elif self.activation == 'relu':
                A = self.relu(Z)
        return A

# Example usage:
if __name__ == "__main__":
    # Initialize a neural network with 2 input neurons, 3 hidden neurons, and 1 output neuron
    layers = [2, 3, 1]
    nn = NeuralNetwork(layers, activation='sigmoid')

    # Example input
    X = np.array([[0.1, 0.2], [0.3, 0.4]])

    # Perform forward propagation
    predictions = nn.forward_propagation(X)
    print("Predictions:")
    print(predictions)
