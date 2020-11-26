import os
from ING2YNAB.ING2YNAB import Ing2YNAB
import os

from ING2YNAB.ING2YNAB import Ing2YNAB

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='input file, default transactions.csv', type=str, nargs='?',
                        default=os.path.join(os.getcwd(), "transactions.csv"))
    parser.add_argument('-o', '--output', help='output file, default ING.csv', type=str, nargs='?',
                        default=os.path.join(os.getcwd(), "ING.csv"))
    args = parser.parse_args()
    print(args)

    converter = Ing2YNAB(args.input, args.output)
    converter.read()
    converter.write()
