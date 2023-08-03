#!/usr/bin/env
import argparse
import sys
import via_voti
import via_elettori

def make_cli():
    parser = argparse.ArgumentParser(prog="senato", description="analizza i voti del senato italiano via Open Data")
    parser.add_argument("-m", "--method", type=str, default="voti", choices=["voti", "elettori"], help="calcola le percentuali via `voti` o `elettori`")
    parser.add_argument("-l", "--limit", type=int, default=65, help="limite soglia per le percentuali")
    parser.add_argument("file", type=str, default="senato.csv", help="file csv con i dati del senato")
    return parser

def parse_cli():
    return make_cli().parse_args(sys.argv[1:])

def main():
    config = parse_cli()
    if config.method == "voti":
        via_voti.workflow(config.file, config.limit)
    else:
        via_elettori.workflow(config.file, config.limit)

main()