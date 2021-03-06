#!/usr/bin/env python

from os import walk, symlink as ln
from os.path import dirname, join, normpath as np, exists, islink, abspath


our_dir = np(dirname(__file__))
logcheck_dir = np(join(our_dir, '../'))


def install_dir(source_dir, target_dir):
    for root, dirs, files in walk(source_dir):
        for filename in files:
            s = np(join(source_dir, filename))
            t = np(join(target_dir, 'local-%s'%filename))

            if exists(t):                
                print "%8s %s" % ("[exists]", t)
                if not islink(t):
                    print "%s%s" % (" "*9, "Cannot override the file at this location.")
            else:
                # TODO: it would be much nicer we we could create
                # a proper relative link. It should be able to handle
                # two arbitrary paths though.
                ln(np(abspath(s)), t)
                print "%8s %s" % ("[mklink]", t)


# install system level rules
source_dir = join(our_dir, 'ignore.d')
for td in ('server', 'workstation', 'paranoid'):
    target_dir = join(logcheck_dir, 'ignore.d.%s'%td)
    install_dir(source_dir, target_dir)

# installation violation ignores
install_dir(join(our_dir, 'violations.ignore.d'), 
            join(logcheck_dir, 'violations.ignore.d'))
