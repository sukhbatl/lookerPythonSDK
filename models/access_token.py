# coding: utf-8

"""
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

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class AccessToken(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AccessToken - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'access_token': 'str',
            'token_type': 'str',
            'expires_in': 'int'
        }

        self.attribute_map = {
            'access_token': 'access_token',
            'token_type': 'token_type',
            'expires_in': 'expires_in'
        }

        self._access_token = None
        self._token_type = None
        self._expires_in = None

    @property
    def access_token(self):
        """
        Gets the access_token of this AccessToken.
        Access Token used for API calls

        :return: The access_token of this AccessToken.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """
        Sets the access_token of this AccessToken.
        Access Token used for API calls

        :param access_token: The access_token of this AccessToken.
        :type: str
        """
        self._access_token = access_token

    @property
    def token_type(self):
        """
        Gets the token_type of this AccessToken.
        Type of Token

        :return: The token_type of this AccessToken.
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """
        Sets the token_type of this AccessToken.
        Type of Token

        :param token_type: The token_type of this AccessToken.
        :type: str
        """
        self._token_type = token_type

    @property
    def expires_in(self):
        """
        Gets the expires_in of this AccessToken.
        Number of seconds before the token expires

        :return: The expires_in of this AccessToken.
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """
        Sets the expires_in of this AccessToken.
        Number of seconds before the token expires

        :param expires_in: The expires_in of this AccessToken.
        :type: int
        """
        self._expires_in = expires_in

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

