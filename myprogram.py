import argparse

# parser = argparse.ArgumentParser(
#     prog='PROG',
#     usage='%(prog)s [options -h -bar]',
#     description='A foo that bars',
#     epilog="And that's how you'd foo a bar")
# parser.add_argument('--foo', help='foo help')
# parser.add_argument('bar', nargs='+', help='bar help')
# args = parser.parse_args()

parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument('--parent', type=int)

foo_parser = argparse.ArgumentParser(parents=[parent_parser])
foo_parser.add_argument('foo')
foo_parser.parse_args(['--parent', '2', 'XXX'])


bar_parser = argparse.ArgumentParser(parents=[parent_parser])
bar_parser.add_argument('--bar')
bar_parser.parse_args(['--bar', 'YYY'])
