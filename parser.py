import argparse

def parser_arguments():
    '''
    Manage the input from the terminal.
    :return: parser
    '''
    parser = argparse.ArgumentParser(description='')

    parser.add_argument('-source_dir', required=False, 
                        metavar="/path/to/OID/dataset/folder/",
                        help='Directory of the OID dataset folder')
    parser.add_argument('-target_dir', required=False,
                        metavar="/path/to/framework/dataset/folder/",
                        help="Directory of the framework dataset folder")
    parser.add_argument('-class_file', required=False, 
                        metavar="/path/to/OID/class/file",
                        help='Path to the classes text file')
    parser.add_argument('-classes', required=False, nargs='+', 
                        metavar="list of classes",
                        help="Sequence of 'strings' of the wanted classes")

    return parser.parse_args()
