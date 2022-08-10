import argparse

# # Create the Parser
parser = argparse.ArgumentParser()

# # Add the Arguments
parser.add_argument('--foo')

# # Execute the parse_args() method
args = parser.parse_args(['--foo', 'BAR'])

# # Print the value(s) of the namespace
print(vars(args))
