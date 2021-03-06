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


class Timezone(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Timezone - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'value': 'str',
            'label': 'str',
            'group': 'str',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'value': 'value',
            'label': 'label',
            'group': 'group',
            'can': 'can'
        }

        self._value = None
        self._label = None
        self._group = None
        self._can = None

    @property
    def value(self):
        """
        Gets the value of this Timezone.
        Timezone

        :return: The value of this Timezone.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Timezone.
        Timezone

        :param value: The value of this Timezone.
        :type: str
        """
        self._value = value

    @property
    def label(self):
        """
        Gets the label of this Timezone.
        Description of timezone

        :return: The label of this Timezone.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this Timezone.
        Description of timezone

        :param label: The label of this Timezone.
        :type: str
        """
        self._label = label

    @property
    def group(self):
        """
        Gets the group of this Timezone.
        Timezone group (e.g Common, Other, etc.)

        :return: The group of this Timezone.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this Timezone.
        Timezone group (e.g Common, Other, etc.)

        :param group: The group of this Timezone.
        :type: str
        """
        self._group = group

    @property
    def can(self):
        """
        Gets the can of this Timezone.
        Operations the current user is able to perform on this object

        :return: The can of this Timezone.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this Timezone.
        Operations the current user is able to perform on this object

        :param can: The can of this Timezone.
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

