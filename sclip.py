#!/usr/bin/env python

import clipboard
import sys

clipboard.copy( "".join(sys.stdin.readlines())  )  
