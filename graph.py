# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 19:50:06 2020

@author: V.H.
"""

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


if __name__== '__main__':
    data = pd.read_csv(r'C:\Networkx\input_data3.csv')
    
    plt.figure(figsize=(30, 30))
    
    #create the graph
    g = nx.from_pandas_edgelist(data, 'FROM', 'TO')

    #layout for our nodes
    layout = nx.kamada_kawai_layout(g)
    #layout = nx.fruchterman_reingold_layout(g, iterations=1000)
    
    
    # Draw major nodes "FROM"
    clubs = list(data.FROM.unique())
    size = data.groupby(['FROM'], as_index=False).agg({'VALUE':'sum'})    
    club_size = [g.degree(club)*size.loc[size['FROM']==club, 'VALUE'].iloc[0] for club in clubs]
    
    nx.draw_networkx_nodes(g, layout, 
                           nodelist=clubs, 
                           node_size=club_size, 
                           node_color='lightblue')
    
    nx.draw_networkx_nodes(g, layout, 
                           nodelist=['AVG_PRICE_1GB'], 
                           node_size=20*size.loc[size['FROM']=='AVG_PRICE_1GB', 'VALUE'].iloc[0], 
                           node_color='gold')
    
    nx.draw_networkx_nodes(g, layout, 
                           nodelist=['EUROPE'], 
                           node_size=10*size.loc[size['FROM']=='EUROPE', 'VALUE'].iloc[0], 
                           node_color='tab:blue')
    nx.draw_networkx_nodes(g, layout, 
                           nodelist=['ASIA'], 
                           node_size=10*size.loc[size['FROM']=='ASIA', 'VALUE'].iloc[0], 
                           node_color='tab:orange')
    nx.draw_networkx_nodes(g, layout, 
                           nodelist=['AFRICA'], 
                           node_size=10*size.loc[size['FROM']=='AFRICA', 'VALUE'].iloc[0], 
                           node_color='tab:olive')
    nx.draw_networkx_nodes(g, layout, 
                           nodelist=['AMERICA'], 
                           node_size=10*size.loc[size['FROM']=='AMERICA', 'VALUE'].iloc[0], 
                           node_color='tab:green')                                           
    nx.draw_networkx_nodes(g, layout, 
                           nodelist=['CIS FORMER USSR'], 
                           node_size=10*size.loc[size['FROM']=='CIS FORMER USSR', 'VALUE'].iloc[0], 
                           node_color='tab:pink')  
    nx.draw_networkx_nodes(g, layout, 
                           nodelist=['OCEANIA'], 
                           node_size=10*size.loc[size['FROM']=='OCEANIA', 'VALUE'].iloc[0], 
                           node_color='tab:cyan')      
                                               

    # Draw minor nodes "TO"
    people = list(data.TO.unique())
    size2 = data.groupby(['TO'], as_index=False).agg({'VALUE':'sum'}) 
    nodesize = [size2.loc[size2['TO']==person, 'VALUE'].iloc[0] for person in people]
    
    nx.draw_networkx_nodes(g, layout, 
                           nodelist=people, 
                           node_color='lightgray', 
                           node_size=nodesize,
                           alpha=0.5)
    
    # EUROPE
    nx.draw_networkx_nodes(g, layout, 
                           nodelist=['BALTICS'], 
                           node_size=5*size2.loc[size2['TO']=='BALTICS', 'VALUE'].iloc[0], 
                           node_color='tab:blue')
    nx.draw_networkx_nodes(g, layout, 
                           nodelist=['EASTERN EUROPE'], 
                           node_size=5*size2.loc[size2['TO']=='EASTERN EUROPE', 'VALUE'].iloc[0], 
                           node_color='tab:blue')   
    nx.draw_networkx_nodes(g, layout, 
                           nodelist=['WESTERN EUROPE'], 
                           node_size=5*size2.loc[size2['TO']=='WESTERN EUROPE', 'VALUE'].iloc[0], 
                           node_color='tab:blue')   
        
    #ASIA
    nx.draw_networkx_nodes(g, layout, 
                           nodelist=['OTHERS'], 
                           node_size=5*size2.loc[size2['TO']=='OTHERS', 'VALUE'].iloc[0], 
                           node_color='tab:orange')   
    nx.draw_networkx_nodes(g, layout, 
                           nodelist=['NEAR EAST'], 
                           node_size=5*size2.loc[size2['TO']=='NEAR EAST', 'VALUE'].iloc[0], 
                           node_color='tab:orange')       

    #AFRICA
    nx.draw_networkx_nodes(g, layout, 
                           nodelist=['NORTHERN AFRICA'], 
                           node_size=5*size2.loc[size2['TO']=='NORTHERN AFRICA', 'VALUE'].iloc[0], 
                           node_color='tab:olive')      
    nx.draw_networkx_nodes(g, layout, 
                           nodelist=['SUB-SAHARAN AFRICA'], 
                           node_size=5*size2.loc[size2['TO']=='SUB-SAHARAN AFRICA', 'VALUE'].iloc[0], 
                           node_color='tab:olive')    


    #AMERICA
    nx.draw_networkx_nodes(g, layout, 
                           nodelist=['CARIBBEAN'], 
                           node_size=5*size2.loc[size2['TO']=='CARIBBEAN', 'VALUE'].iloc[0], 
                           node_color='tab:green')    
    nx.draw_networkx_nodes(g, layout, 
                           nodelist=['CENTRAL AMERICA'], 
                           node_size=5*size2.loc[size2['TO']=='CENTRAL AMERICA', 'VALUE'].iloc[0], 
                           node_color='tab:green')   
    nx.draw_networkx_nodes(g, layout, 
                           nodelist=['NORTHERN AMERICA'], 
                           node_size=5*size2.loc[size2['TO']=='NORTHERN AMERICA', 'VALUE'].iloc[0], 
                           node_color='tab:green')   
    nx.draw_networkx_nodes(g, layout, 
                           nodelist=['SOUTH AMERICA'], 
                           node_size=5*size2.loc[size2['TO']=='SOUTH AMERICA', 'VALUE'].iloc[0], 
                           node_color='tab:green')           
    


    # Draw EDGES
    nx.draw_networkx_edges(g, layout, 
                           width=1, 
                           edge_color="tab:gray")

    # Add LABELS
    nx.draw_networkx_labels(g, layout)        

    # Turn off the axis because I know you don't want it
    plt.axis('off')

    # Save the graph
    plt.savefig("output/graph04.png")
    plt.close()               
                          
                           
                        
    

    
    
    
    
