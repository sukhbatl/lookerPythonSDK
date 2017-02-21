# coding: utf-8

"""
ScheduledPlanApi.py
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


class ScheduledPlanApi(object):
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

    def all_scheduled_plans(self, **kwargs):
        """
        Get All Scheduled Plans
        ### List all scheduled plans which belong to the requesting user

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.all_scheduled_plans(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_id: User Id (default is requesting user if not specified)
        :return: list[ScheduledPlan]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method all_scheduled_plans" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/scheduled_plans'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'user_id' in params:
            query_params['user_id'] = params['user_id']

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
                                            response_type='list[ScheduledPlan]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def create_scheduled_plan(self, **kwargs):
        """
        Create Scheduled Plan
        ### Schedule a Look or Dashboard by creating a scheduled plan. Admins can create scheduled plans on behalf of other users by specifying a user Id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_scheduled_plan(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ScheduledPlan body: Scheduled Plan
        :return: ScheduledPlan
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
                    " to method create_scheduled_plan" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/scheduled_plans'.replace('{format}', 'json')
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
                                            response_type='ScheduledPlan',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_scheduled_plan(self, scheduled_plan_id, **kwargs):
        """
        Delete Scheduled Plan
        ### Delete the scheduled plan with the specified id. Admins can delete other users' Scheduled Plans.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_scheduled_plan(scheduled_plan_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int scheduled_plan_id: Scheduled Plan Id (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scheduled_plan_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_scheduled_plan" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'scheduled_plan_id' is set
        if ('scheduled_plan_id' not in params) or (params['scheduled_plan_id'] is None):
            raise ValueError("Missing the required parameter `scheduled_plan_id` when calling `delete_scheduled_plan`")

        resource_path = '/scheduled_plans/{scheduled_plan_id}'.replace('{format}', 'json')
        path_params = {}
        if 'scheduled_plan_id' in params:
            path_params['scheduled_plan_id'] = params['scheduled_plan_id']

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

    def scheduled_plan(self, scheduled_plan_id, **kwargs):
        """
        Get Scheduled Plan
        ### Get information about a scheduled plan. Admins can fetch information about other users' Scheduled Plans.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.scheduled_plan(scheduled_plan_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int scheduled_plan_id: Scheduled Plan Id (required)
        :return: ScheduledPlan
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scheduled_plan_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scheduled_plan" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'scheduled_plan_id' is set
        if ('scheduled_plan_id' not in params) or (params['scheduled_plan_id'] is None):
            raise ValueError("Missing the required parameter `scheduled_plan_id` when calling `scheduled_plan`")

        resource_path = '/scheduled_plans/{scheduled_plan_id}'.replace('{format}', 'json')
        path_params = {}
        if 'scheduled_plan_id' in params:
            path_params['scheduled_plan_id'] = params['scheduled_plan_id']

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

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ScheduledPlan',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def scheduled_plan_run_once(self, **kwargs):
        """
        Create Scheduled Plan
        ### Schedule a Look or Dashboard to run once _now_ with a scheduled plan (can be useful for testing a Scheduled Plan). Admins can create scheduled plans on behalf of other users by specifying a user Id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.scheduled_plan_run_once(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ScheduledPlan body: Scheduled Plan
        :return: ScheduledPlan
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
                    " to method scheduled_plan_run_once" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/scheduled_plans/run_once'.replace('{format}', 'json')
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
                                            response_type='ScheduledPlan',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def scheduled_plans_for_dashboard(self, dashboard_id, **kwargs):
        """
        Scheduled Plans for Dashboard
        ### Get scheduled plans by using a dashboard id for the requesting user or a specified user Id (with :see_schedules permission)

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.scheduled_plans_for_dashboard(dashboard_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int dashboard_id: Dashboard Id (required)
        :param int user_id: User Id (default is requesting user if not specified)
        :return: list[ScheduledPlan]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard_id', 'user_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scheduled_plans_for_dashboard" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'dashboard_id' is set
        if ('dashboard_id' not in params) or (params['dashboard_id'] is None):
            raise ValueError("Missing the required parameter `dashboard_id` when calling `scheduled_plans_for_dashboard`")

        resource_path = '/scheduled_plans/dashboard/{dashboard_id}'.replace('{format}', 'json')
        path_params = {}
        if 'dashboard_id' in params:
            path_params['dashboard_id'] = params['dashboard_id']

        query_params = {}
        if 'user_id' in params:
            query_params['user_id'] = params['user_id']

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
                                            response_type='list[ScheduledPlan]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def scheduled_plans_for_look(self, look_id, **kwargs):
        """
        Scheduled Plans for Look
        ### Get scheduled plans by using a look id for the requesting user or a specified user Id (with :see_schedules permission)

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.scheduled_plans_for_look(look_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int look_id: Look Id (required)
        :param int user_id: User Id (default is requesting user if not specified)
        :return: list[ScheduledPlan]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['look_id', 'user_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scheduled_plans_for_look" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'look_id' is set
        if ('look_id' not in params) or (params['look_id'] is None):
            raise ValueError("Missing the required parameter `look_id` when calling `scheduled_plans_for_look`")

        resource_path = '/scheduled_plans/look/{look_id}'.replace('{format}', 'json')
        path_params = {}
        if 'look_id' in params:
            path_params['look_id'] = params['look_id']

        query_params = {}
        if 'user_id' in params:
            query_params['user_id'] = params['user_id']

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
                                            response_type='list[ScheduledPlan]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def scheduled_plans_for_lookml_dashboard(self, lookml_dashboard_id, **kwargs):
        """
        Scheduled Plans for LookML Dashboard
        ### Get scheduled plans by using a LookML dashboard id for the requesting user or a specified user Id (with :see_schedules permission)

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.scheduled_plans_for_lookml_dashboard(lookml_dashboard_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int lookml_dashboard_id: LookML Dashboard Id (required)
        :param int user_id: User Id (default is requesting user if not specified)
        :return: list[ScheduledPlan]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['lookml_dashboard_id', 'user_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scheduled_plans_for_lookml_dashboard" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'lookml_dashboard_id' is set
        if ('lookml_dashboard_id' not in params) or (params['lookml_dashboard_id'] is None):
            raise ValueError("Missing the required parameter `lookml_dashboard_id` when calling `scheduled_plans_for_lookml_dashboard`")

        resource_path = '/scheduled_plans/lookml_dashboard/{lookml_dashboard_id}'.replace('{format}', 'json')
        path_params = {}
        if 'lookml_dashboard_id' in params:
            path_params['lookml_dashboard_id'] = params['lookml_dashboard_id']

        query_params = {}
        if 'user_id' in params:
            query_params['user_id'] = params['user_id']

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
                                            response_type='list[ScheduledPlan]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def scheduled_plans_for_space(self, space_id, **kwargs):
        """
        Scheduled Plans for Space
        ### Get scheduled plans by using a space id for the requesting user

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.scheduled_plans_for_space(space_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int space_id: Space Id (required)
        :return: list[ScheduledPlan]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scheduled_plans_for_space" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'space_id' is set
        if ('space_id' not in params) or (params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `scheduled_plans_for_space`")

        resource_path = '/scheduled_plans/space/{space_id}'.replace('{format}', 'json')
        path_params = {}
        if 'space_id' in params:
            path_params['space_id'] = params['space_id']

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

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[ScheduledPlan]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def update_scheduled_plan(self, scheduled_plan_id, body, **kwargs):
        """
        Update Scheduled Plan
        ### Update the scheduled plan with the specified id. Admins can update other users' Scheduled Plans.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_scheduled_plan(scheduled_plan_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int scheduled_plan_id: Scheduled Plan Id (required)
        :param ScheduledPlan body: Scheduled Plan (required)
        :return: ScheduledPlan
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scheduled_plan_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_scheduled_plan" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'scheduled_plan_id' is set
        if ('scheduled_plan_id' not in params) or (params['scheduled_plan_id'] is None):
            raise ValueError("Missing the required parameter `scheduled_plan_id` when calling `update_scheduled_plan`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_scheduled_plan`")

        resource_path = '/scheduled_plans/{scheduled_plan_id}'.replace('{format}', 'json')
        path_params = {}
        if 'scheduled_plan_id' in params:
            path_params['scheduled_plan_id'] = params['scheduled_plan_id']

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
                                            response_type='ScheduledPlan',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
