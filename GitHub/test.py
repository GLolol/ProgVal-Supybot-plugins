###
# Copyright (c) 2011, Valentin Lorentz
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

from supybot.test import *

class GitHubTestCase(PluginTestCase):
    plugins = ('GitHub', 'Config')
    def testAnnounceAdd(self):
        self.assertNotError('config supybot.plugins.GitHub.announces ""')
        self.assertNotError('github announce add #foo ProgVal Limnoria')
        self.assertResponse('config supybot.plugins.GitHub.announces',
                            'ProgVal/Limnoria | test | #foo')
        self.assertNotError('github announce add #bar ProgVal Supybot-plugins')
        self.assertResponse('config supybot.plugins.GitHub.announces',
                            'ProgVal/Limnoria | test | #foo || '
                            'ProgVal/Supybot-plugins | test | #bar')


    def testAnnounceRemove(self):
        self.assertNotError('config supybot.plugins.GitHub.announces '
                            'ProgVal/Limnoria | test | #foo || '
                            'ProgVal/Supybot-plugins | #bar')
        self.assertNotError('github announce remove #foo ProgVal Limnoria')
        self.assertResponse('config supybot.plugins.GitHub.announces',
                            'ProgVal/Supybot-plugins |  | #bar')
        self.assertNotError('github announce remove #bar '
                            'ProgVal Supybot-plugins')
        self.assertResponse('config supybot.plugins.GitHub.announces', ' ')

    def testAnnounceList(self):
        self.assertNotError('config supybot.plugins.GitHub.announces '
                            'abc/def | test | #foo || '
                            'abc/def | test | #bar || '
                            'def/ghi | test | #bar')
        self.assertRegexp('github announce list #foo', 'The following .*abc/def')
        self.assertRegexp('github announce list #bar', 'The following .*(abc/def.*def/ghi|def/ghi.*abc/def)')
        self.assertRegexp('github announce list #baz', 'No repositories')

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
