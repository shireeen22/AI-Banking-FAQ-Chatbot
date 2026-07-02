import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

def graph_feed():
    df = pd.read_csv("feedback.csv")
    return df["feedback"].value_counts()

def quest_graph():
    df = pd.read_csv("feedback.csv")
    return df["question"].value_counts().head(5)