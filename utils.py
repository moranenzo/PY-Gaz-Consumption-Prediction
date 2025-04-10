import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import shap
import plotly.graph_objects as go

# Initialize JS for SHAP plots
shap.initjs()

def plot_pred_vs_actual_plotly(dates, y_true, y_pred, title="Predictions vs Reality Over Time"):

    df_plot = pd.DataFrame({
        'date': dates,
        'y_true': y_true,
        'y_pred': y_pred
    })

    df_plot = df_plot.sort_values(by='date')
    fig = go.Figure()

    # actual
    fig.add_trace(go.Scatter(
        x=df_plot['date'],
        y=df_plot['y_true'],
        mode='markers+lines', 
        name='True values',
        marker=dict(size=5),
        line=dict(width=2)
    ))

    # predicted
    fig.add_trace(go.Scatter(
        x=df_plot['date'],
        y=df_plot['y_pred'],
        mode='markers+lines', 
        name='Predictions',
        marker=dict(size=5, symbol='x'), 
        line=dict(dash='dash', width=2) 
    ))

    # layout
    fig.update_layout(
        title=title,
        xaxis_title='Date',
        yaxis_title='Value',
        height=600,
        legend_title_text='Légende',
        hovermode="x unified"
    )

    fig.show()


def plot_shap_summary(model, X, feature_names, plot_type="bar"):
    try:
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(X)
        shap.summary_plot(shap_values, X, feature_names=feature_names, plot_type=plot_type, show=False)
        plt.title(f"SHAP Summary Plot ({plot_type})")
        plt.show()
    except Exception as e:
        print(f"Erreur lors de la génération du SHAP Summary Plot: {e}")

def plot_shap_waterfall(model, X, feature_names, instance_index=0):

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X) 
    expected_value = explainer.expected_value

    instance_shap = shap_values[instance_index]
    instance_features = X.iloc[[instance_index]]

    shap_explanation = shap.Explanation(
        values=instance_shap,
        base_values=expected_value,
        data=instance_features.values[0], 
        feature_names=feature_names
    )

    shap.waterfall_plot(shap_explanation, show=False)
    plt.show()


def plot_shap_dependence(model, X, feature_names, feature_name_or_index, interaction_index="auto"):

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)

    shap.dependence_plot(
        feature_name_or_index,
        shap_values,
        X,
        feature_names=feature_names,
        interaction_index=interaction_index,
        show=False
    )
    plt.title(f"SHAP Dependence Plot: {feature_name_or_index}")
    plt.show()
