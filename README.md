# dmi
Kommandolinje program til download af vandstand gennem DMI's frie data API. Kan køres gennem fx anaconda eller miniconda prompt.


# Installation 
## Bruger oprettelse
For at downloade data skal en nøgle først laves hos DMI. Det gøres ved at følge linket: https://confluence.govcloud.dk/display/FDAPI/User+Creation#UserCreation-RegisterAsAUser1.RegisterasaUser 

Subscribe til oceanObs og gem nøglen i en .txt fil kaldet "dmiCODE.txt" i den mappe som programmet skal køres i. 

En liste over tidevandstationernes nr. kan findes her: https://confluence.govcloud.dk/pages/viewpage.action?pageId=30015718. Dette nummer bruges som input. 

Parametre kan ses her: https://confluence.govcloud.dk/pages/viewpage.action?pageId=30015716


## Installation
Python skal være installeret:
```sh
(base) $ git clone https://github.com/chris3759/dmi.git
(base) $ cd dmi 
(base) $ conda env create -f environment.yml
(base) $ conda activate dmi
(dmi) $ python -m pip install -e .
(dmi) $
```
Husk at lægge "dmiCODE.txt" i den mappe som programmet køres fra. 

# Kommando linje eksempler
Generel brug
```sh
Usage: dmi [OPTIONS] STATIONID

  Kommando linje program til download af tidevand

Options:
  -s, --start TEXT
  -e, --end TEXT
  -p, --parameterid TEXT
  --help                  Show this message and exit.
```
Parameter-ID angiver hvilken parameter der skal hentes fra stationen. Default er "Sea level relative to local zero for the station" (sealev_ln). Listen over parametre kan ses her: https://confluence.govcloud.dk/pages/viewpage.action?pageId=30015716

DMI har et maximum for hvor mange observationer der kan leveres. Denne limit er på 300000 observationer. Dvs. skal man hente mere end ca. 5 års data skal man bruge --start og --end kommandoerne for at hente data af flere omgange. 

### Seneste times vandstand ved stationen 32048 (Tejn)
```sh
(base) $ conda activate dmi
(dmi) $ dmi 32048
Antal observationer: x
...
Skrevet til: 32048.csv
```

### Data efter given start dato (fx 30. juni 2021) med dvr90 reference
```sh
(base) $ conda activate dmi
(dmi) $ dmi 32048 --start 2021-06-30 -p sealev_dvr
Antal observationer: x
...
Skrevet til: 32048.csv
```


### Data før slut dato (fx 30. juni 2021)
```sh
(base) $ conda activate dmi
(dmi) $ dmi 32048 -e 2021-06-30
Antal observationer: x
...
Skrevet til: 32048.csv
```

### Data mellem to datoer (fx start 30. juni 2021, end 24. december 2021)
```sh
(base) $ conda activate dmi
(dmi) $ dmi 32048 -s 2021-06-30 -e 2021-12-24
Antal observationer: x
...
Skrevet til: 32048.csv
```

