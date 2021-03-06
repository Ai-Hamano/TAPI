# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server import util


class AdminStatePac(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, administrative_state: str=None, operational_state: str=None, lifecycle_state: str=None):  # noqa: E501
        """AdminStatePac - a model defined in Swagger

        :param administrative_state: The administrative_state of this AdminStatePac.  # noqa: E501
        :type administrative_state: str
        :param operational_state: The operational_state of this AdminStatePac.  # noqa: E501
        :type operational_state: str
        :param lifecycle_state: The lifecycle_state of this AdminStatePac.  # noqa: E501
        :type lifecycle_state: str
        """
        self.swagger_types = {
            'administrative_state': str,
            'operational_state': str,
            'lifecycle_state': str
        }

        self.attribute_map = {
            'administrative_state': 'administrative-state',
            'operational_state': 'operational-state',
            'lifecycle_state': 'lifecycle-state'
        }

        self._administrative_state = administrative_state
        self._operational_state = operational_state
        self._lifecycle_state = lifecycle_state

    @classmethod
    def from_dict(cls, dikt) -> 'AdminStatePac':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The admin-state-pac of this AdminStatePac.  # noqa: E501
        :rtype: AdminStatePac
        """
        return util.deserialize_model(dikt, cls)

    @property
    def administrative_state(self) -> str:
        """Gets the administrative_state of this AdminStatePac.


        :return: The administrative_state of this AdminStatePac.
        :rtype: str
        """
        return self._administrative_state

    @administrative_state.setter
    def administrative_state(self, administrative_state: str):
        """Sets the administrative_state of this AdminStatePac.


        :param administrative_state: The administrative_state of this AdminStatePac.
        :type administrative_state: str
        """
        allowed_values = ["LOCKED", "UNLOCKED"]  # noqa: E501
        if administrative_state not in allowed_values:
            raise ValueError(
                "Invalid value for `administrative_state` ({0}), must be one of {1}"
                .format(administrative_state, allowed_values)
            )

        self._administrative_state = administrative_state

    @property
    def operational_state(self) -> str:
        """Gets the operational_state of this AdminStatePac.


        :return: The operational_state of this AdminStatePac.
        :rtype: str
        """
        return self._operational_state

    @operational_state.setter
    def operational_state(self, operational_state: str):
        """Sets the operational_state of this AdminStatePac.


        :param operational_state: The operational_state of this AdminStatePac.
        :type operational_state: str
        """
        allowed_values = ["DISABLED", "ENABLED"]  # noqa: E501
        if operational_state not in allowed_values:
            raise ValueError(
                "Invalid value for `operational_state` ({0}), must be one of {1}"
                .format(operational_state, allowed_values)
            )

        self._operational_state = operational_state

    @property
    def lifecycle_state(self) -> str:
        """Gets the lifecycle_state of this AdminStatePac.


        :return: The lifecycle_state of this AdminStatePac.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state: str):
        """Sets the lifecycle_state of this AdminStatePac.


        :param lifecycle_state: The lifecycle_state of this AdminStatePac.
        :type lifecycle_state: str
        """
        allowed_values = ["PLANNED", "POTENTIAL_AVAILABLE", "POTENTIAL_BUSY", "INSTALLED", "PENDING_REMOVAL"]  # noqa: E501
        if lifecycle_state not in allowed_values:
            raise ValueError(
                "Invalid value for `lifecycle_state` ({0}), must be one of {1}"
                .format(lifecycle_state, allowed_values)
            )

        self._lifecycle_state = lifecycle_state
