from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import time
import argparse, os

def main():

    curtm = time.strftime("%Y%m%d-%H%M%S")

    parser = argparse.ArgumentParser(description=("Automatically download representative species informations from NCBI genome"))
    parser.add_argument('splist', metavar='s', nargs='+', help="Target species list")
    parser.add_argument('-f', '--format', default='geno', nargs='+', help='Format for download (geno, trans, prot, gff, gbk)')
    parser.add_argument('-o', '--out', metavar='o', default=f'{curtm}_NCBIgenome', help="Out directory")
    args = parser.parse_args()

    # Check the existence of output directory
    cur_dir = os.getcwd()

    try:
        os.makedirs(args.out)
        os.chdir(args.out)
    except OSError:
        print(f'The output directory with same name \'{args.out}\' already exists!')
        quit()

    # Set baseUrl
    baseUrl = 'https://www.ncbi.nlm.nih.gov/genome/?term='

    # Generate total search Url list
    urldict = dict()
    for sp in args.splist:
        spformat = sp.lower().replace(' ', '+')
        # quote_plus : 크롤링에서 사용할 수 있는 ASCII code로 변환
        f_url = baseUrl + quote_plus(spformat)
        urldict[f_url] = spformat.replace('+', '_')

    # Set not founded list
    not_founded = []

    # Analyze the Url address for crawling
    linkdict = dict()
    for url in urldict:
        html = urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        shifttags = soup.select('span.shifted>a[href]')
        # Pass the search which not founded
        if len(shifttags) == 0:
            not_founded.append(urldict[url])
            continue
        datafiles = []
        for i in shifttags:
            href = i.attrs['href']
            if href.endswith('.gz'):
                datafiles.append(href)
        spname = urldict[url]
        # Append links to link directory
        linkdict[spname] = datafiles

    # Set type directory
    ftype = {
        'geno' : 'genomic.fna',
        'trans' : 'rna.fna',
        'prot' : 'protein.faa',
        'gff' : 'genomic.gff',
        'gbk' : 'genomic.gbff'
    }

    # Download function
    def linkdown(sp, lk, type):
        for f in lk:
            if type in f:
                print(f'wget {f}')
                os.system(f'wget {f}')
                old_fname = os.path.basename(f)
                new_fname = f'{sp}_{type}.gz'
                os.rename(old_fname, new_fname)

    # Download target files
    for sp in linkdict:
        for f in args.format:
            linkdown(sp, linkdict[sp], ftype[f])

    if os.path.isfile('Not_founded.txt'):
        print('\nWarning: Previous \'Not_founded.txt\' file has been removed!\n')

    with open('Not_founded.txt', 'w') as nf:
        for n in not_founded:
            nf.write(n + '\n')

    os.chdir(cur_dir)