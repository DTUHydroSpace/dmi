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
@click.option('--parameterid','-p',default='sealev_ln',type=str)

def main(stationid,start,end,parameterid):
    """ Kommando linje program til download af tidevand """
    with open('dmiCODE.txt') as f:
        key = f.readlines()
    if start == '' and end == '':
        url = (f"https://dmigw.govcloud.dk/v2/oceanObs/collections/observation/"
                f"items?period=latest-hour&stationId={stationid}&parameterId={parameterid}"
                f"&api-key={key[0]}")
        
    elif start == '':
        url = (f"https://dmigw.govcloud.dk/v2/oceanObs/collections/observation/"
                f"items?datetime=../{end}T00:00:00+02:00&stationId={stationid}&limit=300000"
                f"&parameterId={parameterid}&api-key={key[0]}")
                
    
    elif end == '':
        url = (f"https://dmigw.govcloud.dk/v2/oceanObs/collections/observation/"
                f"items?datetime={start}T00:00:00%2B02:00/..&stationId={stationid}&limit=300000"
                f"&parameterId={parameterid}&api-key={key[0]}")

    else:
        url = (f"https://dmigw.govcloud.dk/v2/oceanObs/collections/observation/"
                f"items?datetime={start}T00:00:00Z/{end}T00:00:00Z&stationId={stationid}&limit=300000"
                f"&parameterId={parameterid}&api-key={key[0]}")

    click.echo("Request sendt til dmi \n...")
    data = requests.get(url)
    click.echo("request modtaget")
    jdat = data.json()
    jdat = json.dumps(jdat)
    jdat = data.json()

    try: 
        ft = jdat["features"]
    except:
        click.echo("Fejl, tjek input... \nSvar fra request:")
        click.echo(f"{jdat}")
        return

    if len(ft) == 0:
        click.echo(f"Ingen observationer fundet...")
    else:
        table = []
        for i,_ in enumerate(ft):
            table.append(['nan']*2)
            table[i][0] = "'"+str(ft[i]["properties"]["observed"])+"'"
            table[i][1] = ft[i]["properties"]["value"]
        
        df = pd.DataFrame(table)
        click.echo(f"Antal observationer: {len(ft)}")
        if len(ft)==300000:
            click.echo(f"dmi's limit for observationer er nået. Lav en ny request med de manglende data, ved brug af --start og --end kommandoerne")
        df.columns = ['%Time',f'{parameterid}']
        df.to_csv(f'{stationid}.csv',index=False)
        click.echo(f"Skrevet til: {stationid}.csv")

if __name__=='__main__':
    main()
