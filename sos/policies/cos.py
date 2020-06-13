# Copyright (C) Red Hat, Inc. 2020

# This file is part of the sos project: https://github.com/sosreport/sos
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# version 2 of the GNU General Public License.
#
# See the LICENSE file in the source distribution for further information.

from sos.report.plugins import CosPlugin
from sos.policies import LinuxPolicy


class CosPolicy(LinuxPolicy):
    distro = "Container-Optimized OS"
    vendor = "Google Cloud Platform"
    vendor_url = "https://cloud.google.com/container-optimized-os/"
    valid_subclasses = [CosPlugin]
    PATH = "/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin"

# vim: set et ts=4 sw=4 :
