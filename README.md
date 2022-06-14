# Veld

[![PyPI version](https://badge.fury.io/py/Veld.svg)](https://pypi.org/project/Veld)
[![Build status](https://github.com/GjjvdBurg/Veld/workflows/build/badge.svg)](https://github.com/GjjvdBurg/Veld/actions)
[![Downloads](https://pepy.tech/badge/Veld)](https://pepy.tech/project/Veld)

Veld is a suite of command line applications for simple statistics on a data 
stream. It is a continuation of [cli 
stats](https://github.com/GjjvdBurg/cli_stats). Similar projects in this space 
include [st](https://github.com/nferraz/st) and 
[datamash](https://www.gnu.org/software/datamash/). What sets Veld apart from 
these projects is that it also has support for plotting.

## Installation

Veld is available on PyPI:

```
$ pip install veld
```

## Usage

Currently Veld includes the following commands:
```
usage: veld [-h] [-V] [--debug] command ...

Below are the available Veld commands. Use veld help <command>
to learn more about each command.

univariate statistics:
  sum        Sum the values in the data stream
  mean       Find the mean (average) of the values in the data stream
  mode       Find the mode of the values in the data stream
  median     Find the median of the values in the data stream
  stdev      Compute the standard deviation of the input stream
  variance   Compute the variance of the input stream
  quantile   Find the given quantile for the data in the stream

extreme values and counts:
  min        Find the minimum of the values in the data stream
  max        Find the maximum of the values in the data stream
  count      Count the number of values in the data stream

filtering values:
  lt         Keep only inputs that are less than a given threshold
  le         Keep only inputs that are less than or equal to a given threshold
  gt         Keep only inputs that are greater than a given threshold
  ge         Keep only inputs that are greater than or equal to a given threshold
  eq         Keep only inputs that equal a given value
  ne         Keep only inputs that are not equal to a given value

math operators:
  log        Compute the logarithm of the input stream
  round      Round the floating point values in the input stream
  cumsum     Compute the cumulative sum of the input stream

plotting:
  lines      Show line plots of the input data
  scatter    Show a scatterplot of two-dimensional data
  histogram  Plot a histogram of the values in the data stream
  barcount   Create a histogram with bars for all unique values in the stream

For more information about Veld, visit:
https://github.com/GjjvdBurg/Veld
```

For example:
```
$ seq 10 | veld sum
55

$ seq 10 | veld gt 5
6
7
8
9
10

$ seq 10 | veld mean
5.5

```

Documentation on all the commands can be found using:
```
$ man veld <command>
```
or
```
$ veld help <command>
```

## Notes

License: See the LICENSE file.

Author: [Gertjan van den Burg][gertjan].

Why "veld"? [Veld](https://en.wikipedia.org/wiki/Veld) is built on top of 
[wilderness](https://github.com/GjjvdBurg/wilderness), and it's short and 
didn't conflict with any tab completions I have :)

[gertjan]: https://gertjanvandenburg.com
