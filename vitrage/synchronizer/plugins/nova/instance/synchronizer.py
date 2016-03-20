# Copyright 2016 - Alcatel-Lucent
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,  software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND,  either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from vitrage.synchronizer.plugins.nova.base import NovaBase


class InstanceSynchronizer(NovaBase):

    @staticmethod
    def filter_instances(instances):
        instances_res = []
        for instance in instances:
            instances_res.append(instance.__dict__)
        return instances_res

    def get_all(self, sync_mode):
        return self.make_pickleable(
            self.filter_instances(self.client.servers.list()),
            self.NOVA_INSTANCE,
            sync_mode,
            ['manager'])

    def get_changes(self, sync_mode):
        pass
