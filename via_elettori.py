#!/usr/bin/env python3
from csvutils import read_senato

def extract_tuples(rows):
    return [extract_tuple(row) for row in rows]

def extract_tuple(row):
    collegio = (row[0], row[1])
    comune = row[2]
    lista = row[-2]
    voti = row[-1]
    elettori = row[3]
    return (collegio, lista, voti, elettori, comune)

def extract_shares(rows):
    voti_collegi = {}
    totale_collegi = {}
    comuni_collegi = {}
    for entry in extract_tuples(rows):
        (collegio, lista, voti, elettori, comune) = entry
        if collegio not in voti_collegi:
            voti_collegi[collegio] = {}
            totale_collegi[collegio] = 0
            comuni_collegi[collegio] = []
        if lista not in voti_collegi[collegio]:
            voti_collegi[collegio][lista] = 0
        if comune not in comuni_collegi[collegio]:
            comuni_collegi[collegio].append(comune)
            totale_collegi[collegio] += elettori
        voti_collegi[collegio][lista] += voti
    return (voti_collegi, totale_collegi)

def analize_shares(collegi):
    (voti_collegi, totale_collegi) = collegi
    percentuali_collegi = {}
    for collegio in voti_collegi:
        if collegio not in percentuali_collegi:
            percentuali_collegi[collegio] = {}
        totale = totale_collegi[collegio]
        for lista in voti_collegi[collegio]:
            voti = voti_collegi[collegio][lista]
            percentuali_collegi[collegio][lista] = voti / totale
    return (voti_collegi, totale_collegi, percentuali_collegi)

def find_maxes(collegi, limit = 65):
    (voti_collegi, totale_collegi, percentuali_collegi) = collegi
    entries = []
    for collegio in percentuali_collegi:
        for lista in percentuali_collegi[collegio]:
            percentuale = percentuali_collegi[collegio][lista] * 100
            if percentuale >= limit:
                entries.append((collegio, lista, percentuale))
    return entries


def workflow(filepath: str, limit: int):
    senato = read_senato(filepath)
    collegi = extract_shares(senato)
    result = analize_shares(collegi)
    maxes = find_maxes(result, limit)
    for entry in maxes:
        print(entry)