# Copyright 2016 - Alcatel-Lucent
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,  software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND,  either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


from vitrage.datasources.driver_base import DriverBase
from vitrage import os_clients


class NeutronBase(DriverBase):
    def __init__(self, conf):
        super(NeutronBase, self).__init__()
        self._client = None
        self.conf = conf

    @property
    def client(self):
        if not self._client:
            self._client = os_clients.neutron_client(self.conf)
        return self._client
