import click
from cloaker import Cloaker


def main():
	cloaker = Cloaker()

	click.secho('test', fg='blue')


if __name__ == '__main__':
	main()