# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server import util


class GetNodeEdgePointDetailsRPCInputSchema(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, topology_id_or_name: str=None, node_id_or_name: str=None, ep_id_or_name: str=None):  # noqa: E501
        """GetNodeEdgePointDetailsRPCInputSchema - a model defined in Swagger

        :param topology_id_or_name: The topology_id_or_name of this GetNodeEdgePointDetailsRPCInputSchema.  # noqa: E501
        :type topology_id_or_name: str
        :param node_id_or_name: The node_id_or_name of this GetNodeEdgePointDetailsRPCInputSchema.  # noqa: E501
        :type node_id_or_name: str
        :param ep_id_or_name: The ep_id_or_name of this GetNodeEdgePointDetailsRPCInputSchema.  # noqa: E501
        :type ep_id_or_name: str
        """
        self.swagger_types = {
            'topology_id_or_name': str,
            'node_id_or_name': str,
            'ep_id_or_name': str
        }

        self.attribute_map = {
            'topology_id_or_name': 'topology-id-or-name',
            'node_id_or_name': 'node-id-or-name',
            'ep_id_or_name': 'ep-id-or-name'
        }

        self._topology_id_or_name = topology_id_or_name
        self._node_id_or_name = node_id_or_name
        self._ep_id_or_name = ep_id_or_name

    @classmethod
    def from_dict(cls, dikt) -> 'GetNodeEdgePointDetailsRPCInputSchema':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The get-node-edge-point-detailsRPC_input_schema of this GetNodeEdgePointDetailsRPCInputSchema.  # noqa: E501
        :rtype: GetNodeEdgePointDetailsRPCInputSchema
        """
        return util.deserialize_model(dikt, cls)

    @property
    def topology_id_or_name(self) -> str:
        """Gets the topology_id_or_name of this GetNodeEdgePointDetailsRPCInputSchema.


        :return: The topology_id_or_name of this GetNodeEdgePointDetailsRPCInputSchema.
        :rtype: str
        """
        return self._topology_id_or_name

    @topology_id_or_name.setter
    def topology_id_or_name(self, topology_id_or_name: str):
        """Sets the topology_id_or_name of this GetNodeEdgePointDetailsRPCInputSchema.


        :param topology_id_or_name: The topology_id_or_name of this GetNodeEdgePointDetailsRPCInputSchema.
        :type topology_id_or_name: str
        """

        self._topology_id_or_name = topology_id_or_name

    @property
    def node_id_or_name(self) -> str:
        """Gets the node_id_or_name of this GetNodeEdgePointDetailsRPCInputSchema.


        :return: The node_id_or_name of this GetNodeEdgePointDetailsRPCInputSchema.
        :rtype: str
        """
        return self._node_id_or_name

    @node_id_or_name.setter
    def node_id_or_name(self, node_id_or_name: str):
        """Sets the node_id_or_name of this GetNodeEdgePointDetailsRPCInputSchema.


        :param node_id_or_name: The node_id_or_name of this GetNodeEdgePointDetailsRPCInputSchema.
        :type node_id_or_name: str
        """

        self._node_id_or_name = node_id_or_name

    @property
    def ep_id_or_name(self) -> str:
        """Gets the ep_id_or_name of this GetNodeEdgePointDetailsRPCInputSchema.


        :return: The ep_id_or_name of this GetNodeEdgePointDetailsRPCInputSchema.
        :rtype: str
        """
        return self._ep_id_or_name

    @ep_id_or_name.setter
    def ep_id_or_name(self, ep_id_or_name: str):
        """Sets the ep_id_or_name of this GetNodeEdgePointDetailsRPCInputSchema.


        :param ep_id_or_name: The ep_id_or_name of this GetNodeEdgePointDetailsRPCInputSchema.
        :type ep_id_or_name: str
        """

        self._ep_id_or_name = ep_id_or_name
