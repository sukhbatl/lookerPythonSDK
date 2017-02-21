# coding: utf-8

"""
ContentMetadataApi.py
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


class ContentMetadataApi(object):
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

    def all_content_metadata_accesss(self, **kwargs):
        """
        Get All Content Metadata Accesss
        ### All content metadata access records for a content metadata item.\n

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.all_content_metadata_accesss(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int content_metadata_id: Id of content metadata
        :param str fields: Requested fields.
        :return: list[ContentMetaGroupUser]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_metadata_id', 'fields']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method all_content_metadata_accesss" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/content_metadata_access'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'content_metadata_id' in params:
            query_params['content_metadata_id'] = params['content_metadata_id']
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
                                            response_type='list[ContentMetaGroupUser]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def all_content_metadatas(self, **kwargs):
        """
        Get All Content Metadatas
        ### Get information about all content metadata in a space.\n

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.all_content_metadatas(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str fields: Requested fields.
        :param int parent_id: Parent space of content.
        :return: list[ContentMeta]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields', 'parent_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method all_content_metadatas" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/content_metadata'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'fields' in params:
            query_params['fields'] = params['fields']
        if 'parent_id' in params:
            query_params['parent_id'] = params['parent_id']

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
                                            response_type='list[ContentMeta]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def content_metadata(self, content_metadata_id, **kwargs):
        """
        Get Content Metadata
        ### Get information about an individual content metadata record.\n

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.content_metadata(content_metadata_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int content_metadata_id: Id of content metadata (required)
        :param str fields: Requested fields.
        :return: ContentMeta
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_metadata_id', 'fields']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method content_metadata" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'content_metadata_id' is set
        if ('content_metadata_id' not in params) or (params['content_metadata_id'] is None):
            raise ValueError("Missing the required parameter `content_metadata_id` when calling `content_metadata`")

        resource_path = '/content_metadata/{content_metadata_id}'.replace('{format}', 'json')
        path_params = {}
        if 'content_metadata_id' in params:
            path_params['content_metadata_id'] = params['content_metadata_id']

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
                                            response_type='ContentMeta',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def create_content_metadata_access(self, **kwargs):
        """
        Create Content Metadata Access
        ### Create content metadata access.\n

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_content_metadata_access(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ContentMetaGroupUser body: Content Metadata Access
        :return: ContentMetaGroupUser
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
                    " to method create_content_metadata_access" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/content_metadata_access'.replace('{format}', 'json')
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
                                            response_type='ContentMetaGroupUser',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_content_metadata_access(self, content_metadata_access_id, **kwargs):
        """
        Delete Content Metadata Access
        ### Remove content metadata access.\n

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_content_metadata_access(content_metadata_access_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int content_metadata_access_id: Id of content metadata access (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_metadata_access_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_content_metadata_access" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'content_metadata_access_id' is set
        if ('content_metadata_access_id' not in params) or (params['content_metadata_access_id'] is None):
            raise ValueError("Missing the required parameter `content_metadata_access_id` when calling `delete_content_metadata_access`")

        resource_path = '/content_metadata_access/{content_metadata_access_id}'.replace('{format}', 'json')
        path_params = {}
        if 'content_metadata_access_id' in params:
            path_params['content_metadata_access_id'] = params['content_metadata_access_id']

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

    def update_content_metadata(self, content_metadata_id, body, **kwargs):
        """
        Update Content Metadata
        ### Move a piece of content.\n

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_content_metadata(content_metadata_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int content_metadata_id: Id of content metadata (required)
        :param ContentMeta body: Content Metadata (required)
        :return: ContentMeta
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_metadata_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_content_metadata" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'content_metadata_id' is set
        if ('content_metadata_id' not in params) or (params['content_metadata_id'] is None):
            raise ValueError("Missing the required parameter `content_metadata_id` when calling `update_content_metadata`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_content_metadata`")

        resource_path = '/content_metadata/{content_metadata_id}'.replace('{format}', 'json')
        path_params = {}
        if 'content_metadata_id' in params:
            path_params['content_metadata_id'] = params['content_metadata_id']

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
                                            response_type='ContentMeta',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def update_content_metadata_access(self, content_metadata_access_id, body, **kwargs):
        """
        Update Content Metadata Access
        ### Update type of access for content metadata.\n

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_content_metadata_access(content_metadata_access_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int content_metadata_access_id: Id of content metadata access (required)
        :param ContentMetaGroupUser body: Content Metadata Access (required)
        :return: ContentMetaGroupUser
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_metadata_access_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_content_metadata_access" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'content_metadata_access_id' is set
        if ('content_metadata_access_id' not in params) or (params['content_metadata_access_id'] is None):
            raise ValueError("Missing the required parameter `content_metadata_access_id` when calling `update_content_metadata_access`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_content_metadata_access`")

        resource_path = '/content_metadata_access/{content_metadata_access_id}'.replace('{format}', 'json')
        path_params = {}
        if 'content_metadata_access_id' in params:
            path_params['content_metadata_access_id'] = params['content_metadata_access_id']

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

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ContentMetaGroupUser',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response