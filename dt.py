from collections import Counter
import numpy as np

# Function to calculate entropy
def calculate_entropy(labels):
    label_counts = Counter(labels)
    total_count = len(labels)
    
    entropy = 0.0
    for count in label_counts.values():
        probability = count / total_count
        if probability > 0:
            entropy -= probability * np.log2(probability)
    
    return entropy

# Function to calculate information gain
def calculate_information_gain(parent_labels, left_child_labels, right_child_labels):
    # Calculate entropy before split (parent node entropy)
    parent_entropy = calculate_entropy(parent_labels)
    
    # Calculate entropy after split (weighted average of child entropies)
    total_count = len(parent_labels)
    left_count = len(left_child_labels)
    right_count = len(right_child_labels)

    left_entropy = calculate_entropy(left_child_labels)
    right_entropy = calculate_entropy(right_child_labels)

    weighted_child_entropy = (left_count / total_count) * left_entropy + (right_count / total_count) * right_entropy

    # Calculate information gain
    info_gain = parent_entropy - weighted_child_entropy
    return info_gain

# Example dataset
labels = ['yes', 'no', 'yes', 'yes', 'no']
left_child_labels = ['yes', 'yes']
right_child_labels = ['no', 'yes', 'no']

# Calculate Information Gain
info_gain = calculate_information_gain(labels, left_child_labels, right_child_labels)
print(f"Information Gain: {info_gain:.4f}")
