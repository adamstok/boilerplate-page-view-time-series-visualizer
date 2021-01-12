import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'])

# Clean data
df = df[(df['value'] >= df['value'].max() * 0.025)
        & (df['value'] <= df['value'] * 0.975)]


def draw_line_plot():
    # Draw line plot

    fig = plt.plot(df['date'], df['value'])

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([(df['date'].dt.year), (df['date'].dt.month)])[
        'value'].mean()
    df_bar = df_bar.unstack()

    # Draw bar plot

    fig = df_bar.plot(kind='bar', figsize=(20, 15), legend=True)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2)

    ax1 = sns.boxplot(x=df['date'].dt.year, y=df['value'])
    ax2 = sns.boxplot(x=df_box['date'].dt.month, y=df_box['value'])

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
