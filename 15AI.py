import math

class DecisionTree:
    def entropy(self, data):
        labels = [row[-1] for row in data]
        return -sum((labels.count(label)/len(data)) * math.log2(labels.count(label)/len(data)) for label in set(labels))

    def information_gain(self, data, index):
        total_entropy = self.entropy(data)
        values = set(row[index] for row in data)
        weighted_entropy = sum((len([row for row in data if row[index] == value]) / len(data)) * self.entropy([row for row in data if row[index] == value]) for value in values)
        return total_entropy - weighted_entropy

    def best_split(self, data):
        return max(range(len(data[0]) - 1), key=lambda i: self.information_gain(data, i))

    def build_tree(self, data):
        if len(set([row[-1] for row in data])) == 1: return data[0][-1]
        if len(data[0]) == 1: return max(set([row[-1] for row in data]), key=[row[-1] for row in data].count)
        best_index = self.best_split(data)
        tree = {best_index: {}}
        for value in set(row[best_index] for row in data):
            subset = [row[:best_index] + row[best_index+1:] for row in data if row[best_index] == value]
            tree[best_index][value] = self.build_tree(subset)
        return tree

    def fit(self, data):
        self.tree = self.build_tree(data)

    def predict(self, row, tree=None):
        if tree is None: tree = self.tree
        if isinstance(tree, dict):
            feature_value = row[list(tree.keys())[0]]
            return self.predict(row, tree[list(tree.keys())[0]].get(feature_value))
        return tree

data = [
    [1, 'Sunny', 'High', 'No', 'No'],
    [2, 'Sunny', 'High', 'No', 'Yes'],
    [3, 'Overcast', 'High', 'No', 'Yes'],
    [4, 'Rain', 'Low', 'Yes', 'Yes'],
    [5, 'Rain', 'Low', 'Yes', 'No'],
    [6, 'Overcast', 'Low', 'Yes', 'Yes'],
    [7, 'Sunny', 'High', 'No', 'No'],
    [8, 'Sunny', 'Low', 'Yes', 'Yes'],
    [9, 'Rain', 'Low', 'Yes', 'Yes'],
    [10, 'Sunny', 'Low', 'No', 'Yes']
]

tree = DecisionTree()
tree.fit(data)
prediction = tree.predict([1, 'Sunny', 'High', 'No'])
print(f"Prediction: {prediction}")
