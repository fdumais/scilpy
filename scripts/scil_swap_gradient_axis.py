#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Flip one or more axes of the gradient sampling matrix. It will be saved in
the same format as input gradient sampling file.
"""
import argparse
import os

from scilpy.io.utils import (add_overwrite_arg, assert_inputs_exist,
                             assert_outputs_exist)
from scilpy.utils.bvec_bval_tools import (swap_dipy_gradient_axis,
                                          swap_mrtrix_gradient_axis)
from scilpy.utils.util import str_to_index


def _build_arg_parser():
    p = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                description=__doc__)

    p.add_argument('gradient_sampling_file',
                   help='Path to gradient sampling file.')

    p.add_argument('swapped_sampling_file',
                   help='Path to the swapped gradient sampling file.')

    p.add_argument('axes', metavar='dimension',
                   choices=['x', 'y', 'z'], nargs='+',
                   help='The axes you want to swap. eg: to swap the x '
                        'and y axes use: x y.')

    add_overwrite_arg(p)

    return p


def main():
    parser = _build_arg_parser()
    args = parser.parse_args()

    assert_inputs_exist(parser, args.gradient_sampling_file)
    assert_outputs_exist(parser, args, args.swapped_sampling_file)

    indices = [str_to_index(axis) for axis in list(args.axes)]

    _, ext = os.path.splitext(args.gradient_sampling_file)

    if ext == '.b':
        swap_mrtrix_gradient_axis(args.gradient_sampling_file,
                                  args.swapped_sampling_file,
                                  indices)
    else:
        swap_dipy_gradient_axis(args.gradient_sampling_file,
                                args.swapped_sampling_file,
                                indices)


if __name__ == "__main__":
    main()
