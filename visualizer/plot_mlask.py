import pandas as pd
import matplotlib.pyplot as plt

def plot_mlask(path_input = '../_data/df_mlask_1700.csv',path_output = '../_data/plot_mlask_1700.png'):
    
    df = pd.read_csv(path_input)
    del df['Unnamed: 0']
    
    df.plot() 
    
    plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left', borderaxespad=1)
    plt.savefig(path_output, bbox_inches='tight')
    
if __name__ == '__main__':
    plot_mlask()