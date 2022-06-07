# Importing libraries and functions we'll need

from random import choice
from collections import defaultdict
import matplotlib.pyplot as plt
from math import log


def make_microbiome(total=10000000,common=0.70,uncommon=0.25,rare=0.04,very_rare=0.004,\
    uber_rare=0.0004,most_rare=0.00001):
    microbiome = ['species1']*int(common*total)+\
      ['species2']*int(uncommon*total)+\
      ['species3']*int(rare*total)+\
      ['species4']*int(very_rare*total)+\
      ['species5']*int(very_rare*total)+\
      ['species6']*int(uber_rare*total)+\
      ['species7']*int(uber_rare*total)+\
      ['species8']*int(uber_rare*total)+\
      ['species9']*int(uber_rare*total)+\
      ['species10']*int(uber_rare*total)+\
      ['species11']*int(most_rare*total)
    return microbiome

def sample_microbiome(microbiome,depth):
    counts = defaultdict(int)
    for i in range(depth):
        read = (choice(microbiome)) 
        counts[read] += 1
    return counts

def obs_species(counts):
    return(len(counts))

def rarefaction_graph(x,y,outfile="rarefaction.png",fontsize=16,font="Arial"):
    ax =plt.subplot()
    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
        label.set_fontname(font)
        label.set_fontsize(fontsize) 

    x_axis_font = {'fontname':'Times New Roman', 'size':'12'}
    y_axis_font = {'fontname':'Times New Roman', 'size':'12'}
    
    plt.plot(x,y,c='yellow',linewidth=3.0)
        
    ax.spines['top'].set_color('pink') 
    ax.spines['right'].set_color('blue')
    
    ax.set_facecolor('purple')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.ylabel('Observed OTUs',**y_axis_font)
    plt.xlabel('Sampling Depth',**x_axis_font)
    plt.savefig(outfile)
    plt.show()

if __name__ == "__main__":
    microbiome = make_microbiome(total=1000000)
    graph_depths = [50,500,1000, 3000,50]
    sampling_depths = range(10,3010,10)
    x = []
    y = []
    iterations = 5
    title_font = {'fontname':'Times New Roman', 'size':'16', 'color':'black', 'weight':'normal',
              'verticalalignment':'bottom'} 

    for sampling_depth in sampling_depths: 
        curr_counts = []
        for i in range(iterations):
            microbiome_sample = sample_microbiome(microbiome,sampling_depth)
            curr_count = obs_species(microbiome_sample)
            curr_counts.append(curr_count)
        counts = sum(curr_counts)/len(curr_counts)
        x.append(sampling_depth)
        y.append(counts)
        plt.title("Rarefaction_%i"%sampling_depth,**title_font) 
        if sampling_depth in graph_depths:
            rarefaction_graph(x,y,outfile="rarefaction_%i"%sampling_depth)
