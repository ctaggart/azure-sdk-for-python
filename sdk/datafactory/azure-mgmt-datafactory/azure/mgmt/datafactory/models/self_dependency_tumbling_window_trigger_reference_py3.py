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

from .dependency_reference_py3 import DependencyReference


class SelfDependencyTumblingWindowTriggerReference(DependencyReference):
    """Self referenced tumbling window trigger dependency.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :param offset: Required. Timespan applied to the start time of a tumbling
     window when evaluating dependency.
    :type offset: str
    :param size: The size of the window when evaluating the dependency. If
     undefined the frequency of the tumbling window will be used.
    :type size: str
    """

    _validation = {
        'type': {'required': True},
        'offset': {'required': True, 'max_length': 15, 'min_length': 8, 'pattern': r'((\d+)\.)?(\d\d):(60|([0-5][0-9])):(60|([0-5][0-9]))'},
        'size': {'max_length': 15, 'min_length': 8, 'pattern': r'((\d+)\.)?(\d\d):(60|([0-5][0-9])):(60|([0-5][0-9]))'},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'offset': {'key': 'offset', 'type': 'str'},
        'size': {'key': 'size', 'type': 'str'},
    }

    def __init__(self, *, offset: str, size: str=None, **kwargs) -> None:
        super(SelfDependencyTumblingWindowTriggerReference, self).__init__(**kwargs)
        self.offset = offset
        self.size = size
        self.type = 'SelfDependencyTumblingWindowTriggerReference'