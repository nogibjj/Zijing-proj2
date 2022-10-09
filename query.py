#!/usr/bin/env python

import click
import pandas as pd

# build a click group
@click.group()
def cli():
    pass


# build a click command
@cli.command()
def describe():
    # load the data and print the description
    df = pd.read_csv('ds_salaries.csv')
    print(df.describe())

@click.command()
@click.option("--n", default=5, help="Most N paid job, default 5")
def query_most_N(n):
    """Find N most pay job"""
    df = pd.read_csv('ds_salaries.csv')
    print(df.nlargest(n, 'salary').job_title)


# run the command
if __name__ == "__main__":
    cli.add_command(query_most_N)
    cli.add_command(describe)
    cli()
