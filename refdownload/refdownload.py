"""This is a program to download reference fasta files from NCBI using their
accession number(s). The fasta file(s) will be either written to file or, in
the case of a single file, written to stdout.

Usage:

    python3 refdownload.py <acc_num1> [<acc_num2> ...] -o /path/to/save/files/

Files are saved as `acc_num.fa`.

Examples:
    # download M. bovis reference to stdout
    python3 refdownload.py NC_002945.4

    # download M. bovis and E. coli references
    python3 refdownload.py NC_002945.4 U00096.3 -o Data/References/

Notes:
    If multiple accession IDs are given, but --output_dir is not specified,
    output_dir will default to the current working directory.

Please see the GitHub page for more information
https://github.com/mbhall88/refdownload/

Contributors:
Michael Hall (https://github.com/mbhall88)
"""
import requests
import arguments


"""raw code to download
import requests
acc = "NC_002945.4"
base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
url = base + "esearch.fcgi?db=nuccore&term={}&usehistory=y".format(acc)
result = requests.get(url)
result.text
# grab the below bit out of the <WebEnv> xml tags
web = "NCID_1_315897282_130.14.22.215_9001_1518599921_1103742014_0MetA0_S_MegaStore_F_1"
# grab the below bit out of the <QueryKey> xml tag (regex for digit)
key = 1
url2 = base + "efetch.fcgi?db=nuccore&query_key={}&WebEnv={}".format(key, web) + "&rettype=fasta&retmode=text"
fasta = requests.get(url2)
fasta.text

"""

def main():
    """Main function to coordinate the running of the script"""
    args = arguments.generate_args(__doc__)


if __name__ == '__main__':
    main()
