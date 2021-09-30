# Terminator by Chris Jones <cmsj@tenshu.net?
# GPL v2 only
"""phpstorm_url_handler.py - Plugin for PhpStorm URL handling"""
import re
import terminatorlib.plugin as plugin

# Every plugin you want Terminator to load *must* be listed in 'AVAILABLE'
AVAILABLE = ['PhpStormURLHandler']

class PhpStormURLHandler(plugin.URLHandler):
    """PhpStormURLHandler URL handler. If there is a URL that starts with phpstorm:, handle it appropriately"""
    capabilities = ['url_handler']
    handler_name = 'phpstorm_url'
    nameopen = "Open file and go to line in PhpStorm"
    namecopy: "Copy"
    match = '\\bphpstorm:\\/\\/(.*|.*\\n.*)\\&line=\\d+'

    def callback(self, url):
        return(url.replace(' ', '').replace('\n', ''))
