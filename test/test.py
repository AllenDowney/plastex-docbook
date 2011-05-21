#!/usr/bin/env python

import os
import subprocess
import shlex

root_dir = os.getcwd()

def runtest(version):
    tmpl_dirname = os.path.normpath(os.path.join(root_dir, '..', 'docbook%s' % version))
    os.environ['DocBookTEMPLATES'] = '%s:.:%s:' % (tmpl_dirname, os.environ.get('DocBookTEMPLATES', ''))

    cmd = 'plastex --renderer DocBook --dir test_db%s ' % version
    cmd += ' --filename result%s.xml test_document.tex' % version

    p = subprocess.Popen(shlex.split(cmd))
    p.wait()

if __name__ == '__main__':
    os.environ['PYTHONPATH'] = '%s:.:%s:' % (root_dir, os.environ.get('PYTHONPATH', ''))

    for version in ('45', '50'):
        runtest(version)
