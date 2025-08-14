import matplotlib.pyplot as plt
import pandas as pd

def plot_top_dues(data, top_n=5):
    df = pd.DataFrame(data)
    df = df.sort_values("due_amount", ascending=False).head(top_n)
    plt.figure(figsize=(6,4))
    plt.bar(df["name"], df["due_amount"])
    plt.xticks(rotation=45)
    plt.ylabel("Due Amount")
    plt.title(f"Top {top_n} Customers by Due")
    return plt
