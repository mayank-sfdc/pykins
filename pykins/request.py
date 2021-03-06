# Copyright 2020 Arie Bregman
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def build_url(url, url_portion):
    return urllib3.urljoin(url, 'api/json', url_portion)


def open_url(jenkins, url_portion):
    """Open given Jenkins URL."""
    return urllib3.urlopen(build_url(jenkins.url, url_portion)).read()
