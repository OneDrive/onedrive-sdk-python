import requests
import json


class ResourceDiscoveryRequest(object):
    def __init__(self):
        self._method = 'GET'
        self._discovery_service_url = 'https://api.office.com/discovery/v2.0/me/services'

    def get_service_info(self, access_token):
        """Send request to discovery service. Return ServiceInfo
        for valid services.

        Args:
            access_token (str): A valid access token for resource
                'https://api.office.com/discovery/'

        Returns:
            List of :class:`ServiceInfo<onedrivesdk.helpers.resource_discovery.ServiceInfo>`:
                ServiceInfo for each service that the caller can access. NOTE: values that
                do not provide access to OneDrive for Business will be excluded (i.e. must have
                capability = 'MyFiles' and service_api_version = 'v2.0'
        """
        headers = {'Authorization': 'Bearer ' + access_token}
        response = json.loads(requests.get(self._discovery_service_url, headers=headers).text)
        service_info_list = [ServiceInfo(x) for x in response['value']]
        trimmed_service_info_list = [si for si in service_info_list
                                     if si.capability == 'MyFiles' and si.service_api_version == 'v2.0']
        return trimmed_service_info_list


class ServiceInfo(object):
    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    def __str__(self):
        return 'serviceResourceId: {}\nserviceEndpointUri: {}'\
            .format(self.service_resource_id, self.service_endpoint_uri)

    def _prop_dict_get(self, prop):
        if prop in self._prop_dict:
            return self._prop_dict[prop]
        else:
            return None

    def _prop_dict_set(self, prop, val):
        self._prop_dict[prop] = val

    @property
    def capability(self):
        return self._prop_dict_get('capability')

    @capability.setter
    def capability(self, value):
        self._prop_dict_set('capability', value)

    @property
    def service_id(self):
        return self._prop_dict_get('serviceId')

    @service_id.setter
    def service_id(self, value):
        self._prop_dict_set('serviceId', value)

    @property
    def service_name(self):
        return self._prop_dict_get('serviceName')

    @service_name.setter
    def service_name(self, value):
        self._prop_dict_set('serviceName', value)

    @property
    def service_endpoint_uri(self):
        return self._prop_dict_get('serviceEndpointUri')

    @service_endpoint_uri.setter
    def service_endpoint_uri(self, value):
        self._prop_dict_set('serviceEndpointUri', value)

    @property
    def service_resource_id(self):
        return self._prop_dict_get('serviceResourceId')

    @service_resource_id.setter
    def service_resource_id(self, value):
        self._prop_dict_set('serviceResourceId', value)

    @property
    def service_api_version(self):
        return self._prop_dict_get('serviceApiVersion')

    @service_api_version.setter
    def service_api_version(self, value):
        self._prop_dict_set('serviceApiVersion', value)
