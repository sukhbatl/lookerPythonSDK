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


class Session(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Session - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'ip_address': 'str',
            'browser': 'str',
            'operating_system': 'str',
            'city': 'str',
            'state': 'str',
            'country': 'str',
            'credentials_type': 'str',
            'extended_at': 'str',
            'extended_count': 'int',
            'sudo_user_id': 'int',
            'created_at': 'str',
            'expires_at': 'str',
            'url': 'str',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'id': 'id',
            'ip_address': 'ip_address',
            'browser': 'browser',
            'operating_system': 'operating_system',
            'city': 'city',
            'state': 'state',
            'country': 'country',
            'credentials_type': 'credentials_type',
            'extended_at': 'extended_at',
            'extended_count': 'extended_count',
            'sudo_user_id': 'sudo_user_id',
            'created_at': 'created_at',
            'expires_at': 'expires_at',
            'url': 'url',
            'can': 'can'
        }

        self._id = None
        self._ip_address = None
        self._browser = None
        self._operating_system = None
        self._city = None
        self._state = None
        self._country = None
        self._credentials_type = None
        self._extended_at = None
        self._extended_count = None
        self._sudo_user_id = None
        self._created_at = None
        self._expires_at = None
        self._url = None
        self._can = None

    @property
    def id(self):
        """
        Gets the id of this Session.
        Unique Id

        :return: The id of this Session.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Session.
        Unique Id

        :param id: The id of this Session.
        :type: int
        """
        self._id = id

    @property
    def ip_address(self):
        """
        Gets the ip_address of this Session.
        IP address of user when this session was initiated

        :return: The ip_address of this Session.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this Session.
        IP address of user when this session was initiated

        :param ip_address: The ip_address of this Session.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def browser(self):
        """
        Gets the browser of this Session.
        User's browser type

        :return: The browser of this Session.
        :rtype: str
        """
        return self._browser

    @browser.setter
    def browser(self, browser):
        """
        Sets the browser of this Session.
        User's browser type

        :param browser: The browser of this Session.
        :type: str
        """
        self._browser = browser

    @property
    def operating_system(self):
        """
        Gets the operating_system of this Session.
        User's Operating System

        :return: The operating_system of this Session.
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """
        Sets the operating_system of this Session.
        User's Operating System

        :param operating_system: The operating_system of this Session.
        :type: str
        """
        self._operating_system = operating_system

    @property
    def city(self):
        """
        Gets the city of this Session.
        City component of user location (derived from IP address)

        :return: The city of this Session.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this Session.
        City component of user location (derived from IP address)

        :param city: The city of this Session.
        :type: str
        """
        self._city = city

    @property
    def state(self):
        """
        Gets the state of this Session.
        State component of user location (derived from IP address)

        :return: The state of this Session.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Session.
        State component of user location (derived from IP address)

        :param state: The state of this Session.
        :type: str
        """
        self._state = state

    @property
    def country(self):
        """
        Gets the country of this Session.
        Country component of user location (derived from IP address)

        :return: The country of this Session.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Session.
        Country component of user location (derived from IP address)

        :param country: The country of this Session.
        :type: str
        """
        self._country = country

    @property
    def credentials_type(self):
        """
        Gets the credentials_type of this Session.
        Type of credentials used for logging in this session

        :return: The credentials_type of this Session.
        :rtype: str
        """
        return self._credentials_type

    @credentials_type.setter
    def credentials_type(self, credentials_type):
        """
        Sets the credentials_type of this Session.
        Type of credentials used for logging in this session

        :param credentials_type: The credentials_type of this Session.
        :type: str
        """
        self._credentials_type = credentials_type

    @property
    def extended_at(self):
        """
        Gets the extended_at of this Session.
        Time when this session was last extended by the user

        :return: The extended_at of this Session.
        :rtype: str
        """
        return self._extended_at

    @extended_at.setter
    def extended_at(self, extended_at):
        """
        Sets the extended_at of this Session.
        Time when this session was last extended by the user

        :param extended_at: The extended_at of this Session.
        :type: str
        """
        self._extended_at = extended_at

    @property
    def extended_count(self):
        """
        Gets the extended_count of this Session.
        Number of times this session was extended

        :return: The extended_count of this Session.
        :rtype: int
        """
        return self._extended_count

    @extended_count.setter
    def extended_count(self, extended_count):
        """
        Sets the extended_count of this Session.
        Number of times this session was extended

        :param extended_count: The extended_count of this Session.
        :type: int
        """
        self._extended_count = extended_count

    @property
    def sudo_user_id(self):
        """
        Gets the sudo_user_id of this Session.
        Actual user in the case when this session represents one user sudo'ing as another

        :return: The sudo_user_id of this Session.
        :rtype: int
        """
        return self._sudo_user_id

    @sudo_user_id.setter
    def sudo_user_id(self, sudo_user_id):
        """
        Sets the sudo_user_id of this Session.
        Actual user in the case when this session represents one user sudo'ing as another

        :param sudo_user_id: The sudo_user_id of this Session.
        :type: int
        """
        self._sudo_user_id = sudo_user_id

    @property
    def created_at(self):
        """
        Gets the created_at of this Session.
        Time when this session was initiated

        :return: The created_at of this Session.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Session.
        Time when this session was initiated

        :param created_at: The created_at of this Session.
        :type: str
        """
        self._created_at = created_at

    @property
    def expires_at(self):
        """
        Gets the expires_at of this Session.
        Time when this session will expire

        :return: The expires_at of this Session.
        :rtype: str
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """
        Sets the expires_at of this Session.
        Time when this session will expire

        :param expires_at: The expires_at of this Session.
        :type: str
        """
        self._expires_at = expires_at

    @property
    def url(self):
        """
        Gets the url of this Session.
        Link to get this item

        :return: The url of this Session.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this Session.
        Link to get this item

        :param url: The url of this Session.
        :type: str
        """
        self._url = url

    @property
    def can(self):
        """
        Gets the can of this Session.
        Operations the current user is able to perform on this object

        :return: The can of this Session.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this Session.
        Operations the current user is able to perform on this object

        :param can: The can of this Session.
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
