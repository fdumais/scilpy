#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import tempfile

from scilpy.io.fetcher import get_testing_files_dict, fetch_data, get_home

# If they already exist, this only takes 5 seconds (check md5sum)
fetch_data(get_testing_files_dict(), keys=['atlas.zip'])
tmp_dir = tempfile.TemporaryDirectory()


def test_help_option(script_runner):
    ret = script_runner.run('scil_dilate_labels.py', '--help')
    assert ret.success


def test_execution_atlas(script_runner):
    os.chdir(os.path.expanduser(tmp_dir.name))
    in_atlas = os.path.join(get_home(), 'atlas',
                            'atlas_freesurfer_v2_single_brainstem.nii.gz')
    ret = script_runner.run('scil_dilate_labels.py', in_atlas,
                            'atlas_freesurfer_v2_single_brainstem_dil.nii.gz',
                            '--processes', '1', '--distance', '2')
    assert ret.success
