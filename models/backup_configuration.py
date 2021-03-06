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


class BackupConfiguration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BackupConfiguration - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'custom_s3_bucket': 'str',
            'custom_s3_bucket_region': 'str',
            'custom_s3_key': 'str',
            'custom_s3_secret': 'str',
            'url': 'str',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'type': 'type',
            'custom_s3_bucket': 'custom_s3_bucket',
            'custom_s3_bucket_region': 'custom_s3_bucket_region',
            'custom_s3_key': 'custom_s3_key',
            'custom_s3_secret': 'custom_s3_secret',
            'url': 'url',
            'can': 'can'
        }

        self._type = None
        self._custom_s3_bucket = None
        self._custom_s3_bucket_region = None
        self._custom_s3_key = None
        self._custom_s3_secret = None
        self._url = None
        self._can = None

    @property
    def type(self):
        """
        Gets the type of this BackupConfiguration.
        Type of backup: looker-s3 or custom-s3

        :return: The type of this BackupConfiguration.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this BackupConfiguration.
        Type of backup: looker-s3 or custom-s3

        :param type: The type of this BackupConfiguration.
        :type: str
        """
        self._type = type

    @property
    def custom_s3_bucket(self):
        """
        Gets the custom_s3_bucket of this BackupConfiguration.
        Name of bucket for custom-s3 backups

        :return: The custom_s3_bucket of this BackupConfiguration.
        :rtype: str
        """
        return self._custom_s3_bucket

    @custom_s3_bucket.setter
    def custom_s3_bucket(self, custom_s3_bucket):
        """
        Sets the custom_s3_bucket of this BackupConfiguration.
        Name of bucket for custom-s3 backups

        :param custom_s3_bucket: The custom_s3_bucket of this BackupConfiguration.
        :type: str
        """
        self._custom_s3_bucket = custom_s3_bucket

    @property
    def custom_s3_bucket_region(self):
        """
        Gets the custom_s3_bucket_region of this BackupConfiguration.
        Name of region where the bucket is located

        :return: The custom_s3_bucket_region of this BackupConfiguration.
        :rtype: str
        """
        return self._custom_s3_bucket_region

    @custom_s3_bucket_region.setter
    def custom_s3_bucket_region(self, custom_s3_bucket_region):
        """
        Sets the custom_s3_bucket_region of this BackupConfiguration.
        Name of region where the bucket is located

        :param custom_s3_bucket_region: The custom_s3_bucket_region of this BackupConfiguration.
        :type: str
        """
        self._custom_s3_bucket_region = custom_s3_bucket_region

    @property
    def custom_s3_key(self):
        """
        Gets the custom_s3_key of this BackupConfiguration.
        AWS S3 key used for custom-s3 backups

        :return: The custom_s3_key of this BackupConfiguration.
        :rtype: str
        """
        return self._custom_s3_key

    @custom_s3_key.setter
    def custom_s3_key(self, custom_s3_key):
        """
        Sets the custom_s3_key of this BackupConfiguration.
        AWS S3 key used for custom-s3 backups

        :param custom_s3_key: The custom_s3_key of this BackupConfiguration.
        :type: str
        """
        self._custom_s3_key = custom_s3_key

    @property
    def custom_s3_secret(self):
        """
        Gets the custom_s3_secret of this BackupConfiguration.
        AWS S3 secret used for custom-s3 backups

        :return: The custom_s3_secret of this BackupConfiguration.
        :rtype: str
        """
        return self._custom_s3_secret

    @custom_s3_secret.setter
    def custom_s3_secret(self, custom_s3_secret):
        """
        Sets the custom_s3_secret of this BackupConfiguration.
        AWS S3 secret used for custom-s3 backups

        :param custom_s3_secret: The custom_s3_secret of this BackupConfiguration.
        :type: str
        """
        self._custom_s3_secret = custom_s3_secret

    @property
    def url(self):
        """
        Gets the url of this BackupConfiguration.
        Link to get this item

        :return: The url of this BackupConfiguration.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this BackupConfiguration.
        Link to get this item

        :param url: The url of this BackupConfiguration.
        :type: str
        """
        self._url = url

    @property
    def can(self):
        """
        Gets the can of this BackupConfiguration.
        Operations the current user is able to perform on this object

        :return: The can of this BackupConfiguration.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this BackupConfiguration.
        Operations the current user is able to perform on this object

        :param can: The can of this BackupConfiguration.
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

