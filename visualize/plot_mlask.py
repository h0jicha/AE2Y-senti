import pandas as pd
import matplotlib.pyplot as plt

def plot_mlask(path_input = '../_data/df_mlask.csv',path_output = '../_data/plot_mlask.png'):
    
    df = pd.read_csv(path_input)
    
    df.plot() 
    
    plt.savefig(path_output)
    
if __name__ == '__main__':
    plot_mlask()