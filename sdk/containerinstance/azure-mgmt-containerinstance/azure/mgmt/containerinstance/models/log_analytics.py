# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class LogAnalytics(Model):
    """Container group log analytics information.

    All required parameters must be populated in order to send to Azure.

    :param workspace_id: Required. The workspace id for log analytics
    :type workspace_id: str
    :param workspace_key: Required. The workspace key for log analytics
    :type workspace_key: str
    :param log_type: The log type to be used. Possible values include:
     'ContainerInsights', 'ContainerInstanceLogs'
    :type log_type: str or
     ~azure.mgmt.containerinstance.models.LogAnalyticsLogType
    :param metadata: Metadata for log analytics.
    :type metadata: dict[str, str]
    """

    _validation = {
        'workspace_id': {'required': True},
        'workspace_key': {'required': True},
    }

    _attribute_map = {
        'workspace_id': {'key': 'workspaceId', 'type': 'str'},
        'workspace_key': {'key': 'workspaceKey', 'type': 'str'},
        'log_type': {'key': 'logType', 'type': 'str'},
        'metadata': {'key': 'metadata', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(LogAnalytics, self).__init__(**kwargs)
        self.workspace_id = kwargs.get('workspace_id', None)
        self.workspace_key = kwargs.get('workspace_key', None)
        self.log_type = kwargs.get('log_type', None)
        self.metadata = kwargs.get('metadata', None)