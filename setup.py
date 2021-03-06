# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
# Copyright 2010 Anso Labs, LLC
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import glob
import os
import sys

from setuptools import setup, find_packages

srcdir = os.path.join(os.path.dirname(sys.argv[0]), 'src')

setup(name='nova',
      version='0.3.0',
      description='None Other, Vaguely Awesome',
      author='nova-core',
      author_email='nova-core@googlegroups.com',
      url='http://novacc.org/',
      packages = find_packages(),

     )
