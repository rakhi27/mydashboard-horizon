# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from horizon import views
from restclient import RESTClient

class IndexView(views.APIView):
    # A very simple class-based view...
    template_name = 'mydashboard/mypanel/index.html'

    def get_data(self, request, context, *args, **kwargs):
        # Add data to the context here...
        restObj = RESTClient('admin', 'admin')
        restODLurl = 'http://172.17.78.59:8080/restconf/operational/network-topology:network-topology/'
        #response = restObj.get(restODLurl)
        context["jsonResponse"] = {'name':'rakesh'}#response.content 
        return context
