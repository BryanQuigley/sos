# Copyright (C) Red Hat, Inc. 2019

# This file is part of the sos project: https://github.com/sosreport/sos
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# version 2 of the GNU General Public License.
#
# See the LICENSE file in the source distribution for further information.

from sos.policies.redhat import RedHatPolicy


class AmazonPolicy(RedHatPolicy):

    distro = "Amazon Linux"
    vendor = "Amazon"
    vendor_url = "https://aws.amazon.com"

    def __init__(self, sysroot=None, init=None, probe_runtime=True,
                 remote_exec=None):
        super(AmazonPolicy, self).__init__(sysroot=sysroot, init=init,
                                           probe_runtime=probe_runtime,
                                           remote_exec=remote_exec)


# vim: set et ts=4 sw=4 :
