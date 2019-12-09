#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from mephisto.providers.mturk_sandbox.provider_type import PROVIDER_TYPE
from mephisto.providers.mturk.mturk_provider import MTurkProvider
from mephisto.providers.mturk_sandbox.sandbox_mturk_agent import SandboxMTurkAgent
from mephisto.providers.mturk_sandbox.sandbox_mturk_requester import (
    SandboxMTurkRequester,
)
from mephisto.providers.mturk_sandbox.sandbox_mturk_unit import SandboxMTurkUnit
from mephisto.providers.mturk_sandbox.sandbox_mturk_worker import SandboxMTurkWorker


from typing import ClassVar, Type, List, TYPE_CHECKING

if TYPE_CHECKING:
    from mephisto.data_model.assignment import Unit
    from mephisto.data_model.worker import Worker
    from mephisto.data_model.requester import Requester
    from mephisto.data_model.agent import Agent


class SandboxMTurkProvider(MTurkProvider):
    """
    Mock implementation of a CrowdProvider that stores everything
    in a local state in the class for use in tests.
    """

    PROVIDER_TYPE = PROVIDER_TYPE

    UnitClass: ClassVar[Type["Unit"]] = SandboxMTurkUnit

    RequesterClass: ClassVar[Type["Requester"]] = SandboxMTurkRequester

    WorkerClass: ClassVar[Type["Worker"]] = SandboxMTurkWorker

    AgentClass: ClassVar[Type["Agent"]] = SandboxMTurkAgent

    SUPPORTED_TASK_TYPES: ClassVar[List[str]] = [
        # TODO
    ]