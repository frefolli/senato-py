I dati del senato del repository sono prelevati (e corretti in caso di errori ortografici, ex: ROMA IV -> ROMA V), dal sito ufficiale di Eligendo del Ministero dell'Interno.

# Esempio

`python -m main -h`

```
usage: senato [-h] [-m {voti,elettori}] [-l LIMIT] file

analizza i voti del senato italiano via Open Data

positional arguments:
  file                  file csv con i dati del senato

options:
  -h, --help            show this help message and exit
  -m {voti,elettori}, --method {voti,elettori}
                        calcola le percentuali via `voti` o `elettori`
  -l LIMIT, --limit LIMIT
                        limite soglia per le percentuali
```

Il limite e' impostato di default a 65 (= 65%).
Il metodo di default e' Voti.

## Metodo via Elettori

La percentuale di soglia e' calcolata tramite il rapporto voti_nel_collegio / aventi_diritto_nel_collegio.

## Metodo via Voti

La percentuale di soglia e' calcolata tramite il rapporto voti_nel_collegio / votanti.