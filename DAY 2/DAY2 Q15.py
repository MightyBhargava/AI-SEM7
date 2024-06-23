import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier, plot_tree

# Generating synthetic data
X, y = make_classification(n_samples=100, n_features=2, n_classes=2, n_redundant=0, random_state=42)

# Training a Decision Tree classifier
clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X, y)

# Plotting the decision boundary
plt.figure(figsize=(10, 6))
plot_tree(clf, filled=True, rounded=True, class_names=['Class 0', 'Class 1'], feature_names=['Feature 1', 'Feature 2'])
plt.title('Decision Tree Classifier')
plt.show()
