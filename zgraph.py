import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix

# Data from your training logs
binary_metrics = {
    'Black and white': 0.0479,
    'Cotton leaves': 0.0479,
    'Cotton plant disease': 0.0419,
    'HOG brighter': 0.0479,
    'HOG_data': 0.0479,
    'Main dataset-1': 0.0478,
    'Main dataset-2': 0.0476
}

multi_class_metrics = {
    'Black and white': 0.9249,
    'Cotton leaves': 0.9626,
    'Cotton plant disease': 0.3978,
    'HOG brighter': 0.5969,
    'HOG_data': 0.6640,
    'Main dataset-1': 0.9596,
    'Main dataset-2': 0.9260
}

# 1. Performance Comparison Chart
def plot_performance_comparison():
    plt.figure(figsize=(12, 6))
    df = pd.DataFrame({
        'Binary Classification': binary_metrics.values(),
        'Multi-Class Classification': multi_class_metrics.values()
    }, index=binary_metrics.keys())
    
    df.plot(kind='bar', rot=45)
    plt.title('Model Performance Comparison Across Datasets')
    plt.ylabel('Weighted F1 Score')
    plt.ylim(0, 1.1)
    plt.tight_layout()
    plt.show()

# 2. Training History Plots
def plot_training_history():
    history = {
        'loss': [1.4603, 0.9088, 0.6802, 0.5816, 0.4994],
        'val_loss': [0.9223, 0.4714, 0.3335, 0.2762, 0.2519],
        'accuracy': [0.4315, 0.6758, 0.7679, 0.8006, 0.8262],
        'val_accuracy': [0.6667, 0.8161, 0.8882, 0.9018, 0.9175]
    }
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Loss plot
    ax1.plot(history['loss'], label='Training Loss')
    ax1.plot(history['val_loss'], label='Validation Loss')
    ax1.set_title('Training and Validation Loss')
    ax1.set_xlabel('Epochs')
    ax1.set_ylabel('Loss')
    ax1.legend()
    
    # Accuracy plot
    ax2.plot(history['accuracy'], label='Training Accuracy')
    ax2.plot(history['val_accuracy'], label='Validation Accuracy')
    ax2.set_title('Training and Validation Accuracy')
    ax2.set_xlabel('Epochs')
    ax2.set_ylabel('Accuracy')
    ax2.legend()
    
    plt.tight_layout()
    plt.show()

# 3. Confusion Matrix Visualization
def plot_confusion_matrix():
    # Simulated confusion matrix for demonstration purposes
    cm = np.array([
        [50, 2, 1, 0, 0, 1],
        [3, 45, 2, 0, 1, 1],
        [0, 1, 48, 2, 1, 1],
        [0, 0, 2, 47, 2, 3],
        [1, 1, 2, 3, 45, 3],
        [0, 1, 2, 2, 2, 48]
    ])
    
    classes = ['Aphids', 'Army worm', 'Bacterial Blight', 'Powdery Mildew', 'Target spot', 'Healthy']
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=classes, yticklabels=classes)
    plt.title('Confusion Matrix')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.show()

# 4. Classification Report Table
def classification_report_table():
    report = {
        'Aphids': {'precision': 0.86, 'recall': 0.91, 'f1-score': 0.89, 'support': 160},
        'Army worm': {'precision': 0.99, 'recall': 0.94, 'f1-score': 0.96, 'support': 160},
        'Bacterial Blight': {'precision': 0.90, 'recall': 0.88, 'f1-score': 0.89, 'support': 160},
        'Powdery Mildew': {'precision': 0.87, 'recall': 0.85, 'f1-score': 0.86, 'support': 160},
        'Target spot': {'precision': 0.91, 'recall': 0.93, 'f1-score': 0.92, 'support': 160},
        'Healthy': {'precision': 0.94, 'recall': 0.97, 'f1-score': 0.95, 'support': 157},
        'macro avg': {'precision': 0.91, 'recall': 0.91, 'f1-score': 0.91, 'support': 957},
        'weighted avg': {'precision': 0.91, 'recall': 0.91, 'f1-score': 0.91, 'support': 957}
    }
    
    df = pd.DataFrame(report).transpose()
    df = df.round(2)
    print(df.to_string())  # Use print instead of display() for non-Jupyter environments

# 5. Metric Distribution Plot
def plot_metric_distribution():
    metrics = list(binary_metrics.values()) + list(multi_class_metrics.values())
    labels = ['Binary']*len(binary_metrics) + ['Multi-Class']*len(multi_class_metrics)
    
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=labels, y=metrics)
    plt.title('F1 Score Distribution by Model Type')
    plt.ylabel('Weighted F1 Score')
    plt.show()

# Run all the visualizations
plot_performance_comparison()
plot_training_history()
plot_confusion_matrix()
classification_report_table()
plot_metric_distribution()
