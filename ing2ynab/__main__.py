import os
import argparse
import os

from ing2ynab.Ing2ynab import Ing2ynab

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='input file, default transactions.csv', type=str, nargs='?',
                        default=os.path.join(os.getcwd(), "transactions.csv"))
    parser.add_argument('-o', '--output', help='output file, default ING.csv', type=str, nargs='?',
                        default=os.path.join(os.getcwd(), "ING.csv"))
    args = parser.parse_args()
    print("Converting file: " + args.input)

    converter = Ing2ynab.fromfilename(args.input)
    converter.convert()
    converter.to_csv(args.output)
