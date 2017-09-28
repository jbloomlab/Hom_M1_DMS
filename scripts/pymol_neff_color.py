"""
Colors M1 residues by number of effective amino acids.

It is intended to be run in the PyMOL terminal as::

    run pymol_analysis.py

Lauren Gentles, September-27-2017


To dos:

-remove the second monomer
"""
import pymol
from pymol import cmd

# Input variables
structure = '1EA3' # name of structure
n_eff_input_f = './results/prefs/neff_and_prefs.csv'

# Fetch and display structure
cmd.delete('all')
cmd.fetch(structure)
cmd.hide('everything')
cmd.select('monomer', 'chain A')
cmd.bg_color('white')
cmd.show('cartoon', 'monomer')

# Read in neff values
neffs = {}
with open(n_eff_input_f) as f:
	lines = f.readlines()[1:]
	for line in lines:
		line_elements = line.strip().split(',')
		site = int(line_elements[0])
		neff = float(line_elements[-1])
		neffs[site] = neff

# Determine the min and max entropy to set the range of the color scale
min_neff = min(neffs.values())
max_neff = max(neffs.values())

# Change each residue's B factor to its entropy value
for site in neffs:
	cmd.alter("resi %d" %site, "b = %g" % neffs[site])

# Color the structure by B-factor values
cmd.spectrum('b', 'yellow_red', structure, minimum=min_neff, maximum=max_neff)

# set up view
cmd.set_view (
    '-0.722045004,   -0.058464222,   -0.689368665, '
    '0.598552346,    0.446926057,   -0.664827526, '
    '0.346962959,   -0.892658830,   -0.287708551, '
    '0.000000000,    0.000000000, -119.305297852, '
    '16.283113480,   28.784046173,   25.007221222, '
    '91.323577881,  147.287002563,  -20.000000000')

cmd.select('none')

cmd.ray(1600, 1200)
cmd.png('./results/prefs/structure_by_neff.png')
