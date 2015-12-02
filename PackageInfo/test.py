# -*- Encoding: utf-8 -*-
###
# Copyright (c) 2008-2010 Terence Simpson
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of version 2 of the GNU General Public License as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
###

from supybot.test import *

class PackageInfoTestCase(PluginTestCase):
    plugins = ('PackageInfo',)
    cleanConfDir = True
    cleanDataDir = False

    def testBase(self):
        self.assertRegexp('info gstreamer1.0-libav',
                r'gstreamer1.0-libav \(source: gst-libav1.0\)')
        self.assertRegexp('info rjegegjierigj', 'does not exist')
        self.assertRegexp('find irssi', 'Found: .*irssi-dev')
        self.assertRegexp('depends supybot', 'python')


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
