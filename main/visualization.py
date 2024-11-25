import matplotlib.pyplot as plt
import numpy as np

def plot_results(results):
    print("Plotting results...")
    mae_values = [metrics["MAE"] for metrics in results.values()]
    rmse_values = [metrics["RMSE"] for metrics in results.values()]
    r2_values = [metrics["R2"] for metrics in results.values()]
    
    x_pos = np.arange(len(results))
    width = 0.25
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.bar(x_pos - width, mae_values, width, label="MAE", color='blue')
    ax.bar(x_pos, rmse_values, width, label="RMSE", color='green')
    ax.bar(x_pos + width, r2_values, width, label="R2", color='red')
    
    ax.set_xticks(x_pos)
    ax.set_xticklabels(results.keys())
    ax.set_xlabel("Model")
    ax.set_ylabel("Metric Value")
    ax.set_title("Model Comparison Metrics")
    ax.legend()
    
    plt.tight_layout()
    plt.show()
    print("Results plotted.")

def plot_feature_importance(feature_importance, feature_names):
    print("Plotting feature importance...")
    importance_array = feature_importance.toArray()
    
    feature_importance_pairs = list(zip(feature_names, importance_array))
    sorted_pairs = sorted(feature_importance_pairs, key=lambda x: x[1], reverse=True)
    sorted_features = [x[0] for x in sorted_pairs]
    sorted_importance = [x[1] for x in sorted_pairs]
    
    plt.figure(figsize=(12, 6))
    y_pos = np.arange(len(sorted_features))
    plt.barh(y_pos, sorted_importance, align='center')
    plt.yticks(y_pos, sorted_features)
    plt.xlabel('Feature Importance')
    plt.title('Random Forest Feature Importance')
    
    for i, v in enumerate(sorted_importance):
        plt.text(v, i, f'{v:.4f}', va='center')
    
    plt.tight_layout()
    plt.show()
    print("Feature importance plot completed.")
