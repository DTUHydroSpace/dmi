"""
Kommandolinje program
 
"""


from typing import Iterable

import click
import requests
import json
import pandas as pd
import numpy as np
import dmi


@click.command()
@click.argument('stationid',type=int)
@click.option('--start','-s',default='',type=str)
@click.option('--end','-e',default='',type=str)

def main(stationid,start,end):
    """ Kommando linjo program til download af tidevand """
    with open('dmiCODE.txt') as f:
        key = f.readlines()
    if start == '' and end == '':
        url = (f"https://dmigw.govcloud.dk/v2/oceanObs/collections/observation/"
                f"items?period=latest-hour&stationId={stationid}"
                f"&api-key={key[0]}")
        
    elif start == '':
        url = (f"https://dmigw.govcloud.dk/v2/oceanObs/collections/observation/"
                f"items?datetime=../{end}T00:00:00+02:00&stationId={stationid}"
                f"&api-key={key[0]}")
    
    elif end == '':
        url = (f"https://dmigw.govcloud.dk/v2/oceanObs/collections/observation/"
                f"items?datetime={start}T00:00:00%2B02:00/..&stationId={stationid}"
                f"&api-key={key[0]}")

    else:
        url = (f"https://dmigw.govcloud.dk/v2/oceanObs/collections/observation/"
                f"items?datetime={start}T00:00:00Z/{end}T00:00:00Z&stationId={stationid}"
                f"&api-key={key[0]}")


    data = requests.get(url)
    jdat = data.json()
    jdat = json.dumps(jdat)
    jdat = data.json()
    f = jdat["features"]
    if len(f) == 0:
        click.echo(f"Ingen observationer fundet...")
    else:
        ####
        # Laver tabel med data. 
        table = []
        t_idx = []
        for i,_ in enumerate(f):
            t = f[i]["properties"]["observed"] 
            if t in t_idx:
                val = f[i]["properties"]["value"]
                x = f[i]["properties"]["parameterId"]
                table[t_idx.index(t)][parameter(x)] = f[i]["properties"]["value"]
            else:
                t_idx.append(t)
                val = f[i]["properties"]["value"]
                x = f[i]["properties"]["parameterId"]
                table.append([0]*5)
                table[t_idx.index(t)][0] = t
                table[t_idx.index(t)][parameter(x)] = f[i]["properties"]["value"]
        
        df = pd.DataFrame(table)
        click.echo(f"Antal observationer: {len(t_idx)}")
        click.echo(f"...")
        df.columns = ['Time','sealev_dvr','sealev_ln','sea_reg','tw']
        df.to_csv(f'{stationid}.csv',index=False)
        click.echo(f"Skrevet til: {stationid}.csv")


    
def parameter(x):
    return {
        'sealev_dvr': 1,
        'sealev_ln': 2,
        'sea_reg': 3,
        'tw': 4
    }.get(x,5)  # 5 is return default, if no input

if __name__=='__main__':
    main()