#!/usr/bin/python
fname = raw_input('file name:')
print
try:
  fobj = open(fname,'r')
  for eachline in fobj:
    print eachline
  except IOEror,e:
    print 'file open error:',e
fobj.close()
