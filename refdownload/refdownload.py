"""This is a program to download reference fasta files from NCBI using their
accession number(s). The fasta file(s) will be either written to file or, in
the case of a single file, written to stdout.

Usage:

    python3 refdownload.py <accn1> [<accn2> ...] -o /path/to/save/files/

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
import xml.etree.ElementTree as ET
from refdownload import arguments  # todo: need to set project up as package


"""raw code to download
https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
root = ET.fromstring(response.text)
>>> root.tag
'eSearchResult'
>>> root.attribute
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'xml.etree.ElementTree.Element' object has no attribute 'attribute'
>>> root.attrib
{}
>>> for child in root:
...     print(child.tag, child.attrib)
...
Count {}
RetMax {}
RetStart {}
QueryKey {}
WebEnv {}
IdList {}
TranslationSet {}
QueryTranslation {}
>>> for child in root:
...     print(child.tag, child.text)
...
Count 1
RetMax 1
RetStart 0
QueryKey 1
WebEnv NCID_1_332496223_130.14.22.215_9001_1518688588_719535970_0MetA0_S_MegaStore_F_1
IdList

TranslationSet None
QueryTranslation None
# grab the below bit out of the <WebEnv> xml tags
web = "NCID_1_315897282_130.14.22.215_9001_1518599921_1103742014_0MetA0_S_MegaStore_F_1"
# grab the below bit out of the <QueryKey> xml tag (regex for digit)
key = 1
url2 = base + "efetch.fcgi?db=nuccore&query_key={}&WebEnv={}".format(key, web) + "&rettype=fasta&retmode=text"
fasta = requests.get(url2)
fasta.text

"""


def construct_esearch_url(accession_id: str) -> str:
    """Constructs an Esearch URL for a given accession number. This is used to
    fetch an XML file containing information required to get fasta.
    See https://www.ncbi.nlm.nih.gov/books/NBK25498/#chapter3.Application_2_Converting_access
    for more information.

    Args:
        accession_id: NCBI accession/version number for fasta of interest.

    Returns:
        An esearch URL to get XML metadata required for downloading fasta from
        NCBI.
    """
    base = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
    search = 'esearch.fcgi?db=nuccore&term={}&usehistory=y'.format(accession_id)
    return base + search


def esearch_request(accession_id: str) -> requests.Response:
    """Submits an esearch GET request for the XML metadata about the accession
    ID provided.

    Args:
        accession_id: NCBI accession/version number for fasta of interest.

    Returns:
        Response object of the esearch GET request.
    """
    esearch_url = construct_esearch_url(accession_id)
    esearch_response = requests.get(esearch_url)

    # raise error if bad response from request
    if not esearch_response.ok:
        esearch_response.raise_for_status()

    return esearch_response

def parse_esearch_XML(response: requests.Response) -> (str, str):
    """Takes a response from an esearch request and extracts the QueryKey and
    WebEnv parameters, which are required for fetching the fasta.

    Args:
        response: Response from esearch request. Text is XML.

    Returns:
        A tuple of strings with the values of (QueryKey, WebEnv)
    """



def main():
    """Main function to coordinate the running of the script"""
    args = arguments.generate_args(__doc__)


if __name__ == '__main__':
    main()
