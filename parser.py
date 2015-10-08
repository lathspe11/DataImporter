import argparse

print(dir(argparse.ArgumentParser))
argparse.ArgumentParser
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-s', action="store", dest="select", help='select string to use')
parser.add_argument('-o', action="store", dest="order", help='order string to use')
parser.add_argument('-f', action="store", dest="filter", help='filter string to use')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))