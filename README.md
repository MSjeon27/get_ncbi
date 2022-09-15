# get_ncbi

## Table of Contents
  * [Installation](#installation)
  * [Quick start](#quick-start)
  * [Instruction](#instruction)
  * [Features](#features)
  
## Installation

Download using pip via pypi.

```bash
$ pip install get_ncbi
```
(Mac/homebrew users may need to use ``pip3``)

## Quick start
```
$ get_ncbi 'genus species'
// -f 'format'    # type of format: geno, trans, prot, gff, gbk
// -o 'output file name'
```

## Instruction

This tool was devised for download the various information about the multiple representative species in 'just one command line'.

It is useful for biologist who want to analyze several representative species.

We provides the tool instruction with several cases.


### Case 1. multiple genomes
```
$ get_ncbi 'Saccharomyces cerevisiae' 'debaryomyces Hansenii' -f geno
```
This type of command downloads the genomic fasta files of 'Saccharomyces cerevisiae' and 'Debaryomyces hansenii', respectively.

In this case, following files will be saved in output directory:
- saccharomyces_cerevisiae_genomic.fna.gz
- debaryomyces_hansenii_genomic.fna.gz

The number of species can be infinite! and this tool doesn't consider the upper and lower case letters of species name.


### Case 2. multiple formats
```
$ get_ncbi 'Saccharomyces cerevisiae' -f geno prot
```
This type of command downloads the genomic and protein fasta files of 'Saccharomyces cerevisiae'.

It also provides multiple format options! (e.g. -f geno prot trans gff)


## Features
  * Python script to automatically download representative species informations from NCBI genome


## Large update log
get_ncbi 1.1.0
- When multiple file types were entered, it was modified to distinguish which file types were excluded from Not found. This provides information such as certain species provide genome files, but not protein files.