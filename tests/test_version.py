#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of jupyter-samples.
# https://github.com/garaemon/jupyter-samples

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2017, garaemon <garaemon@gmail.com>

from preggy import expect

from jupyter_samples import __version__
from tests.base import TestCase


class VersionTestCase(TestCase):
    def test_has_proper_version(self):
        expect(__version__).to_equal('0.1.0')
