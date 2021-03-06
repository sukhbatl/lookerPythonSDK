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


class CredentialsLDAP(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CredentialsLDAP - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'email': 'str',
            'ldap_id': 'str',
            'ldap_dn': 'str',
            'created_at': 'str',
            'logged_in_at': 'str',
            'is_disabled': 'bool',
            'type': 'str',
            'url': 'str',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'email': 'email',
            'ldap_id': 'ldap_id',
            'ldap_dn': 'ldap_dn',
            'created_at': 'created_at',
            'logged_in_at': 'logged_in_at',
            'is_disabled': 'is_disabled',
            'type': 'type',
            'url': 'url',
            'can': 'can'
        }

        self._email = None
        self._ldap_id = None
        self._ldap_dn = None
        self._created_at = None
        self._logged_in_at = None
        self._is_disabled = None
        self._type = None
        self._url = None
        self._can = None

    @property
    def email(self):
        """
        Gets the email of this CredentialsLDAP.
        EMail address

        :return: The email of this CredentialsLDAP.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this CredentialsLDAP.
        EMail address

        :param email: The email of this CredentialsLDAP.
        :type: str
        """
        self._email = email

    @property
    def ldap_id(self):
        """
        Gets the ldap_id of this CredentialsLDAP.
        LDAP Unique ID for this user

        :return: The ldap_id of this CredentialsLDAP.
        :rtype: str
        """
        return self._ldap_id

    @ldap_id.setter
    def ldap_id(self, ldap_id):
        """
        Sets the ldap_id of this CredentialsLDAP.
        LDAP Unique ID for this user

        :param ldap_id: The ldap_id of this CredentialsLDAP.
        :type: str
        """
        self._ldap_id = ldap_id

    @property
    def ldap_dn(self):
        """
        Gets the ldap_dn of this CredentialsLDAP.
        LDAP Distinguished name for this user (as-of the last login)

        :return: The ldap_dn of this CredentialsLDAP.
        :rtype: str
        """
        return self._ldap_dn

    @ldap_dn.setter
    def ldap_dn(self, ldap_dn):
        """
        Sets the ldap_dn of this CredentialsLDAP.
        LDAP Distinguished name for this user (as-of the last login)

        :param ldap_dn: The ldap_dn of this CredentialsLDAP.
        :type: str
        """
        self._ldap_dn = ldap_dn

    @property
    def created_at(self):
        """
        Gets the created_at of this CredentialsLDAP.
        Timestamp for the creation of this credential

        :return: The created_at of this CredentialsLDAP.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this CredentialsLDAP.
        Timestamp for the creation of this credential

        :param created_at: The created_at of this CredentialsLDAP.
        :type: str
        """
        self._created_at = created_at

    @property
    def logged_in_at(self):
        """
        Gets the logged_in_at of this CredentialsLDAP.
        Timestamp for most recent login using credential

        :return: The logged_in_at of this CredentialsLDAP.
        :rtype: str
        """
        return self._logged_in_at

    @logged_in_at.setter
    def logged_in_at(self, logged_in_at):
        """
        Sets the logged_in_at of this CredentialsLDAP.
        Timestamp for most recent login using credential

        :param logged_in_at: The logged_in_at of this CredentialsLDAP.
        :type: str
        """
        self._logged_in_at = logged_in_at

    @property
    def is_disabled(self):
        """
        Gets the is_disabled of this CredentialsLDAP.
        Has this credential been disabled?

        :return: The is_disabled of this CredentialsLDAP.
        :rtype: bool
        """
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled):
        """
        Sets the is_disabled of this CredentialsLDAP.
        Has this credential been disabled?

        :param is_disabled: The is_disabled of this CredentialsLDAP.
        :type: bool
        """
        self._is_disabled = is_disabled

    @property
    def type(self):
        """
        Gets the type of this CredentialsLDAP.
        Short name for the type of this kind of credential

        :return: The type of this CredentialsLDAP.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CredentialsLDAP.
        Short name for the type of this kind of credential

        :param type: The type of this CredentialsLDAP.
        :type: str
        """
        self._type = type

    @property
    def url(self):
        """
        Gets the url of this CredentialsLDAP.
        Link to get this item

        :return: The url of this CredentialsLDAP.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this CredentialsLDAP.
        Link to get this item

        :param url: The url of this CredentialsLDAP.
        :type: str
        """
        self._url = url

    @property
    def can(self):
        """
        Gets the can of this CredentialsLDAP.
        Operations the current user is able to perform on this object

        :return: The can of this CredentialsLDAP.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this CredentialsLDAP.
        Operations the current user is able to perform on this object

        :param can: The can of this CredentialsLDAP.
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

