"""This holds the command line arguments creation function for the script"""
import argparse
import os


def generate_args(doc):
    """Generates the argparse arguments for the program

    Returns:
        argparse.Namespace: an object holding attributes and return it.
    """
    parser = argparse.ArgumentParser(description=doc,
                                     formatter_class=
                                     argparse.RawTextHelpFormatter)

    parser.add_argument('-o', '--output_dir',
                        help="Directory to save fasta files to. The filename " 
                        "will be the accession number followed by .fa",
                        type=str,
                        default='-')

    parser.add_argument('accession',
                        metavar='accn',
                        type=str,
                        nargs='+',
                        help='Accession/Version ID. e.g NC_002945.4')

    args = parser.parse_args()

    # if there are more than accession id given and stdout is still set as
    # output path, change output path to current working directory.
    if len(args.accession) > 1 and args.output_dir == '-':
        args.output_dir = os.getcwd()

    return args
