# Veld

Veld is a suite of command line applications for simple statistics on a data 
stream. It is a continuation of [cli 
stats](https://github.com/GjjvdBurg/cli_stats). Similar projects in this space 
include [st](https://github.com/nferraz/st) and 
[datamash](https://www.gnu.org/software/datamash/).

## Installation

Veld is available on PyPI:

```
$ pip install veld
```

## Usage

Currently Veld includes the following commands:
```
usage: veld [-h] [-V] [--debug] command ...

Below are the available Veld commands

extreme values and counts:
  min    Find the minimum ofthe values in the data stream
  max    Find the maximum of the values in the data stream
  count  Count the number of values in the data stream

univariate statistics:
  sum    Sum the values in the data stream
  mean   Find the mean (average) of the values in the data stream
  mode   Find the mode of the values in the data stream

```

Documentation on all the commands can be found using:
```
$ man veld <command>
```

## Notes

License: See the LICENSE file.

Author: [Gertjan van den Burg][gertjan].

Why "veld"? [Veld](https://en.wikipedia.org/wiki/Veld) is built on top of 
[wilderness](https://github.com/GjjvdBurg/wilderness), and it's short and 
didn't conflict with any tab completions I have :)

[gertjan]: https://gertjanvandenburg.com
