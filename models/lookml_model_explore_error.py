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


class LookmlModelExploreError(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        LookmlModelExploreError - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'message': 'str',
            'details': 'str',
            'error_pos': 'str',
            'field_error': 'bool',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'message': 'message',
            'details': 'details',
            'error_pos': 'error_pos',
            'field_error': 'field_error',
            'can': 'can'
        }

        self._message = None
        self._details = None
        self._error_pos = None
        self._field_error = None
        self._can = None

    @property
    def message(self):
        """
        Gets the message of this LookmlModelExploreError.
        Error Message

        :return: The message of this LookmlModelExploreError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this LookmlModelExploreError.
        Error Message

        :param message: The message of this LookmlModelExploreError.
        :type: str
        """
        self._message = message

    @property
    def details(self):
        """
        Gets the details of this LookmlModelExploreError.
        Details

        :return: The details of this LookmlModelExploreError.
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this LookmlModelExploreError.
        Details

        :param details: The details of this LookmlModelExploreError.
        :type: str
        """
        self._details = details

    @property
    def error_pos(self):
        """
        Gets the error_pos of this LookmlModelExploreError.
        Error source location

        :return: The error_pos of this LookmlModelExploreError.
        :rtype: str
        """
        return self._error_pos

    @error_pos.setter
    def error_pos(self, error_pos):
        """
        Sets the error_pos of this LookmlModelExploreError.
        Error source location

        :param error_pos: The error_pos of this LookmlModelExploreError.
        :type: str
        """
        self._error_pos = error_pos

    @property
    def field_error(self):
        """
        Gets the field_error of this LookmlModelExploreError.
        Is this a field error

        :return: The field_error of this LookmlModelExploreError.
        :rtype: bool
        """
        return self._field_error

    @field_error.setter
    def field_error(self, field_error):
        """
        Sets the field_error of this LookmlModelExploreError.
        Is this a field error

        :param field_error: The field_error of this LookmlModelExploreError.
        :type: bool
        """
        self._field_error = field_error

    @property
    def can(self):
        """
        Gets the can of this LookmlModelExploreError.
        Operations the current user is able to perform on this object

        :return: The can of this LookmlModelExploreError.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this LookmlModelExploreError.
        Operations the current user is able to perform on this object

        :param can: The can of this LookmlModelExploreError.
        :type: dict(str, bool)
        """
        self._can = can

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

