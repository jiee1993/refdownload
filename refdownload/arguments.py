"""This holds the command line arguments creation function for the script"""
import argparse
import os


class FullPaths(argparse.Action):
    """Expand user- and relative-paths"""
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest,
                os.path.abspath(os.path.expanduser(values)))


class FullPathsList(argparse.Action):
    """Expand user- and relative-paths"""
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest,
                [os.path.abspath(os.path.expanduser(value))
                 for value in values])


def generate_args(doc):
    """Generates the argparse arguments for the program

    Returns:
        argparse.Namespace: an object holding attributes and return it.
    """
    parser = argparse.ArgumentParser(description=doc)
    parser.add_argument(
        "-o", "--output_dir",
        action=FullPathsList,
        help="""Directory to save fasta files to. The filename will be the 
        accession number followed by .fa""",
        type=str,
        required=True)

    parser.add_argument('accession',
                        metavar='N',
                        type=str,
                        nargs='+',
                        help='Accession/Version ID. e.g NC_002945.4')

    parser.add_argument(
        "-o", "--output",
        action=FullPaths,
        help="""Filename to write fast5 paths to. If nothing is entered,
            it will write the paths to STDOUT.""",
        default=None)

    return parser.parse_args()