My personal collection of custom logcheck rules
===============================================

1) Check the repository into a location like::

      /etc/logcheck/custom.ignore.d

   Don't forget to set the permissions correctly. Usually, the group
   is set to the ``logcheck`` user, and nothing is world-readable::

     chown -R :logcheck /etc/logcheck/custom.ignore.d
     chmod -R o= /etc/logcheck/custom.ignore.d
     find /etc/logcheck/custom.ignore.d -type d | xargs chmod g+s
    
2) Run 

      /etc/logcheck/custom.ignore.d/sync.py
    
   This will link the custom rule files into the appropriate logcheck
   ignore directories.
    
   Note that by default it will assume to be located in a directory
   within a standard ``/etc/logcheck`` directory structure, and will
   sync the rules of the SYSTEM EVENTS layer into all report levels
   (workstation, server, paranoid).
