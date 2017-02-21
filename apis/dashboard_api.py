# coding: utf-8

"""
DashboardApi.py
Copyright 2016 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DashboardApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def all_dashboards(self, **kwargs):
        """
        Get All Dashboards
        Get information about all dashboards.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.all_dashboards(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str fields: Requested fields.
        :return: list[DashboardBase]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method all_dashboards" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/dashboards'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'fields' in params:
            query_params['fields'] = params['fields']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[DashboardBase]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def create_dashboard(self, **kwargs):
        """
        Create Dashboard
        ### Create a dashboard with specified information.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_dashboard(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Dashboard body: Dashboard
        :return: Dashboard
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_dashboard" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/dashboards'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Dashboard',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def create_dashboard_prefetch(self, dashboard_id, **kwargs):
        """
        Create Dashboard Prefetch
        ### Create a prefetch for a dashboard with the specified information.\n

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_dashboard_prefetch(dashboard_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str dashboard_id: Id of dashboard (required)
        :param PrefetchDashboardRequest body: Parameters for prefetch request
        :return: PrefetchDashboardRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_dashboard_prefetch" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'dashboard_id' is set
        if ('dashboard_id' not in params) or (params['dashboard_id'] is None):
            raise ValueError("Missing the required parameter `dashboard_id` when calling `create_dashboard_prefetch`")

        resource_path = '/dashboards/{dashboard_id}/prefetch'.replace('{format}', 'json')
        path_params = {}
        if 'dashboard_id' in params:
            path_params['dashboard_id'] = params['dashboard_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PrefetchDashboardRequest',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def dashboard(self, dashboard_id, **kwargs):
        """
        Get Dashboard
        ### Get information about the dashboard with a specific id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.dashboard(dashboard_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str dashboard_id: Id of dashboard (required)
        :param str fields: Requested fields.
        :return: Dashboard
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard_id', 'fields']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dashboard" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'dashboard_id' is set
        if ('dashboard_id' not in params) or (params['dashboard_id'] is None):
            raise ValueError("Missing the required parameter `dashboard_id` when calling `dashboard`")

        resource_path = '/dashboards/{dashboard_id}'.replace('{format}', 'json')
        path_params = {}
        if 'dashboard_id' in params:
            path_params['dashboard_id'] = params['dashboard_id']

        query_params = {}
        if 'fields' in params:
            query_params['fields'] = params['fields']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Dashboard',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def dashboard_prefetch(self, dashboard_id, **kwargs):
        """
        Get Dashboard Prefetch
        ### Get a prefetch for a dashboard with the specified information.\n

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.dashboard_prefetch(dashboard_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str dashboard_id: Id of dashboard (required)
        :param list[PrefetchDashboardFilterValue] dashboard_filters: JSON encoded string of Dashboard filters that were applied to prefetch
        :return: PrefetchMapper
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard_id', 'dashboard_filters']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dashboard_prefetch" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'dashboard_id' is set
        if ('dashboard_id' not in params) or (params['dashboard_id'] is None):
            raise ValueError("Missing the required parameter `dashboard_id` when calling `dashboard_prefetch`")

        resource_path = '/dashboards/{dashboard_id}/prefetch'.replace('{format}', 'json')
        path_params = {}
        if 'dashboard_id' in params:
            path_params['dashboard_id'] = params['dashboard_id']

        query_params = {}
        if 'dashboard_filters' in params:
            query_params['dashboard_filters'] = params['dashboard_filters']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PrefetchMapper',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_dashboard(self, dashboard_id, **kwargs):
        """
        Delete Dashboard
        ### Delete the dashboard with a specific id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_dashboard(dashboard_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str dashboard_id: Id of dashboard (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_dashboard" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'dashboard_id' is set
        if ('dashboard_id' not in params) or (params['dashboard_id'] is None):
            raise ValueError("Missing the required parameter `dashboard_id` when calling `delete_dashboard`")

        resource_path = '/dashboards/{dashboard_id}'.replace('{format}', 'json')
        path_params = {}
        if 'dashboard_id' in params:
            path_params['dashboard_id'] = params['dashboard_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='str',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def search_dashboards(self, **kwargs):
        """
        Search Dashboards
        Get information about all dashboards.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.search_dashboards(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str fields: Requested fields.
        :param int page: Requested page.
        :param int per_page: Results per page.
        :param int limit: Number of results to return. (used with offset and takes priority over page and per_page)
        :param int offset: Number of results to skip before returning any. (used with limit and takes priority over page and per_page)
        :param str sorts: Fields to sort by.
        :param str title: Match Dashboard title.
        :param str description: Match Dashboard description.
        :param int content_favorite_id: Filter on a content favorite id.
        :param str space_id: Filter on a particular space.
        :param str creator_id: Filter on dashboards created by a particular user.
        :param str view_count: Filter on a particular value of view_count
        :return: list[Dashboard]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields', 'page', 'per_page', 'limit', 'offset', 'sorts', 'title', 'description', 'content_favorite_id', 'space_id', 'creator_id', 'view_count']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_dashboards" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/dashboards/search'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'fields' in params:
            query_params['fields'] = params['fields']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'sorts' in params:
            query_params['sorts'] = params['sorts']
        if 'title' in params:
            query_params['title'] = params['title']
        if 'description' in params:
            query_params['description'] = params['description']
        if 'content_favorite_id' in params:
            query_params['content_favorite_id'] = params['content_favorite_id']
        if 'space_id' in params:
            query_params['space_id'] = params['space_id']
        if 'creator_id' in params:
            query_params['creator_id'] = params['creator_id']
        if 'view_count' in params:
            query_params['view_count'] = params['view_count']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Dashboard]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def update_dashboard(self, dashboard_id, body, **kwargs):
        """
        Update Dashboard
        ### Update the dashboard with a specific id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_dashboard(dashboard_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str dashboard_id: Id of dashboard (required)
        :param Dashboard body: Dashboard (required)
        :return: Dashboard
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_dashboard" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'dashboard_id' is set
        if ('dashboard_id' not in params) or (params['dashboard_id'] is None):
            raise ValueError("Missing the required parameter `dashboard_id` when calling `update_dashboard`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_dashboard`")

        resource_path = '/dashboards/{dashboard_id}'.replace('{format}', 'json')
        path_params = {}
        if 'dashboard_id' in params:
            path_params['dashboard_id'] = params['dashboard_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Dashboard',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response