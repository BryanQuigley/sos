# This file is part of the sos project: https://github.com/sosreport/sos
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# version 2 of the GNU General Public License.
#
# See the LICENSE file in the source distribution for further information.


# This sosreport plugin is meant for sas adapters.
# This plugin logs inforamtion on each adapter it finds.

from sos.report.plugins import Plugin, RedHatPlugin, DebianPlugin, UbuntuPlugin


class arcconf(Plugin, RedHatPlugin, DebianPlugin, UbuntuPlugin):

    short_desc = 'arcconf Integrated RAID adapter information'

    plugin_name = "arcconf"
    commands = ("arcconf",)

    def setup(self):

        # get list of adapters
        self.add_cmd_output("arcconf getconfig 1")

# vim: et ts=4 sw=4
