import os
import subprocess
import shlex

dirname = os.getcwd()
tmpl_dirname = os.path.join(dirname,'..','docbook45')
os.environ['PYTHONPATH'] = '%s:.:%s:' % (dirname, os.environ.get('PYTHONPATH',''))
os.environ['DocBookTEMPLATES'] = '%s:.:%s:' % (tmpl_dirname, os.environ.get('DocBookTEMPLATES',''))
print os.environ['DocBookTEMPLATES']
cmd = 'plastex --renderer DocBook --filename test.xml test_document.tex'
print 'hey'
print shlex.split(cmd)
p = subprocess.Popen(shlex.split(cmd))
p.wait()

  