import imageio
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.animation as animation
from IPython.display import display, HTML
from matplotlib.patches import Ellipse
from IPython.display import Image
from matplotlib.animation import FuncAnimation

class PlayAnimation:
    def __init__(self, df, gameId, playId):
        self.play_data = df[(df['gameId'] == gameId) &
                            (df['playId'] == playId)]
        self.possession_team = self.play_data['possessionTeam'].iloc[0]

    def plot_play(self):
        fig, ax = plt.subplots(figsize=(12, 5.33))
        plt.xlim(0, 120)
        plt.ylim(0, 53.3)
        plt.title('Play Visualization')
        plt.xlabel('X')
        plt.ylabel('Y')

        def update(frame):
            ax.clear()
            plt.xlim(0, 120)
            plt.ylim(0, 53.3)
            plt.title('Play Visualization')
            plt.xlabel('X')
            plt.ylabel('Y')
            current_frame = self.play_data[self.play_data['frameId'] == frame]
            for idx, row in current_frame.iterrows():
                if row['team'] == 'football':
                    football = Ellipse(
                        (row['x'], row['y']), width=1, height=0.6, edgecolor='brown', facecolor='brown')
                    ax.add_patch(football)
                else:
                    color = 'blue' if row['team'] == self.possession_team else 'red'
                    ax.scatter(row['x'], row['y'], c=color)

        ani = animation.FuncAnimation(
            fig, update, frames=self.play_data['frameId'].nunique(), interval=100, repeat=False)
        ani.save('play_animation.gif', writer='imagemagick')
        # Close the figure to prevent it from displaying in the notebook
        plt.close(fig)
        display(Image(filename='play_animation.gif'))
