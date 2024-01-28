import argparse

def add(args):
    result = sum(args.numbers)
    print(f"The sum of {', '.join(map(str, args.numbers))} is: {result}")

def subtract(args):
    result = args.numbers[0] - sum(args.numbers[1:])
    print(f"The difference between {args.numbers[0]} and {', '.join(map(str, args.numbers[1:]))} is: {result}")

def multiply(args):
    result = 1
    for num in args.numbers:
        result *= num
    print(f"The product of {', '.join(map(str, args.numbers))} is: {result}")

def divide(args):
    if 0 in args.numbers[1:]:
        print("Error: Division by zero is not allowed.")
    else:
        result = args.numbers[0] / args.numbers[1]
        print(f"The division of {args.numbers[0]} by {args.numbers[1]} is: {result}")

parser = argparse.ArgumentParser(description="Command-Line Calculator")

subparsers = parser.add_subparsers(title="Operations", dest="operation")

# Subparser for the "add" command
add_parser = subparsers.add_parser("add", help="Perform addition")
add_parser.add_argument("numbers", metavar="N", type=float, nargs="+", help="Numbers to add")
add_parser.set_defaults(func=add)

# Subparser for the "subtract" command
subtract_parser = subparsers.add_parser("subtract", help="Perform subtraction")
subtract_parser.add_argument("numbers", metavar="N", type=float, nargs="+", help="Numbers to subtract")
subtract_parser.set_defaults(func=subtract)

# Subparser for the "multiply" command
multiply_parser = subparsers.add_parser("multiply", help="Perform multiplication")
multiply_parser.add_argument("numbers", metavar="N", type=float, nargs="+", help="Numbers to multiply")
multiply_parser.set_defaults(func=multiply)

# Subparser for the "divide" command
divide_parser = subparsers.add_parser("divide", help="Perform division")
divide_parser.add_argument("numbers", metavar="N", type=float, nargs="+", help="Numbers to divide")
divide_parser.set_defaults(func=divide)

args = parser.parse_args()
if hasattr(args, "func"):
    args.func(args)
else:
    parser.print_help()