# dmi
Kommandolinje program til download af vandstand gennem DMI's frie data API. 


# Installation 
## Bruger oprettelse
For at downloade data skal en nøgle først laves hos DMI. Det gøres ved at følge linket: https://confluence.govcloud.dk/display/FDAPI/User+Creation#UserCreation-RegisterAsAUser1.RegisterasaUser 

Subscribe til oceanObs og gem nøglen i en .txt fil kaldet "dmiCODE.txt" i den mappe som programmet skal køres i. 

En liste over tidevandstationernes nr. kan findes her: https://confluence.govcloud.dk/pages/viewpage.action?pageId=30015718

Parametre fra stationerne kan ses her: https://confluence.govcloud.dk/pages/viewpage.action?pageId=30015716


## Installation
Hav python og conda installeret:
```sh
(base) $ git clone https://github.com/chris3759/dmi.git
(base) $ cd dmi 
(base) $ git chechout 0.1.0
(base) $ conda env create -f environment.yml
(base) $ conda activate dmi
(dmi) $ python -m pip install -e .
(dmi) $
```


# Kommando linje eksempler
Generel brug
```sh
Usage: dmi [OPTIONS] STATIONID

  Kommando linje program til download af tidevand

Options:
  -s, --start TEXT
  -e, --end TEXT
  --help            Show this message and exit.
```
### Seneste times vandstand ved stationen 32048 (Tejn)
```sh
(base) $ conda activate dmi
(dmi) $ dmi 32048
Antal observationer: x
...
Skrevet til: 32048.csv
```

### Data efter start_dato (fx 30. juni 2021)
```sh
(base) $ conda activate dmi
(dmi) $ dmi 32048 --start 2021-06-30
Antal observationer: x
...
Skrevet til: 32048.csv
```


### Data hentet før end_dato (fx 30. juni 2021)
```sh
(base) $ conda activate dmi
(dmi) $ dmi 32048 --end 2021-06-30
Antal observationer: x
...
Skrevet til: 32048.csv
```

### Data mellem to datoer (fx start 30. juni 2021, end 24. december 2021)
```sh
(base) $ conda activate dmi
(dmi) $ dmi 32048 -s 2021-06-30 -e 2021-12-24
Antal observationer: 250
...
Skrevet til: 32048.csv
```

