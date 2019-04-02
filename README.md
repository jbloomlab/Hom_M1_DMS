# Analysis of influenza M1 deep mutational scanning

## Overview
Nancy Hom performed deep mutational scanning of the PR8 M1 gene in the context of the X-31 virus. 
This directory contains an analysis of the data by Lauren Gentles in the [Bloom lab](https://research.fhcrc.org/bloom/en.html).

The analysis is performed by the Jupyter notebook [analysis_notebook.ipynb](analysis_notebook.ipynb).
There is a separate script, [scripts/pymol_neff_color.py](scripts/pymol_neff_color.py) for making a `pymol` image.

## Input files
The following input files are in the [./data/](./data/) subdirectory:

* [PR8-M1.fasta](./data/PR8-M1.fasta): The PR8 M1 coding sequence as found in the Bloom lab plasmid pHW198-M.

* [M1_human_PR8_prealignment_fasta.fa](./data/M1_human_PR8_prealignment_fasta.fa): an alignment of human M1 coding sequences from [Machkovech et al, Journal of Virology, 2015](https://www.ncbi.nlm.nih.gov/pubmed/26311880).

* [Wu_relative_fitness.csv](./data/Wu_relative_fitness.csv) are the "relative fitness" values reported by [Wu et al, BMC Genomics, 2016](https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-015-2358-7) from their deep mutational scanning of M1. These are taken from the supplementary Excel file provided with that paper.

* [1EA3.pdb](./data/1EA3.pdb) is the crystal structure of the PR8 M1 protein. 

* [1EA3_monomer.pdb](./data/1EA3_monomer.pdb) is just one monomer (chain A) manually extracted from [1EA3.pdb](./data/1EA3.pdb).

* [1EA3_monomer.dssp](./data/1EA3_monomer.dssp) is the result of manually running [dssp](http://swift.cmbi.ru.nl/gv/dssp/) on [1EA3_monomer.pdb](./data/1EA3_monomer.pdb).

## Results
For a summary of the results, look at the Jupyter notebook [analysis_notebook.ipynb](analysis_notebook.ipynb).

Major results files are in the [./results/](results) subdirectory.
These include:

 - The [./results/codoncounts/](results/codoncounts) subdirectory has the counts of each codon mutation at each position for each sample in the `*_codoncounts.csv` files.

 - The [./results/prefs/](results/prefs) subdirectory has the amino-acid preferences calculated from the codon counts. The files of most relevance are likely to be [./results/prefs/summary_avgprefs.csv](results/prefs/summary_avgprefs.csv), which contains the amino-acid preferences from the experiments prior to re-scaling.
