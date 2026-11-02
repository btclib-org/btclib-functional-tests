# Copyright (c) The btclib developers
# Distributed under the MIT software license, see the accompanying
# LICENSE file or https://opensource.org/license/mit for the full text.

"""Core's `feature_bip68_sequence`, rewritten on tf2's own harness: btclib-node.

`feature_bip68_sequence_test.py` beside this module is the body, run here
against the target rather than the oracle (rule 3 of issue
btclib-org/btclib#2220). It asks for `Capability.MINE` and
`Capability.TEST_ACTIVATION_HEIGHT`, each declared per build
(`btclib_node.py`'s own docstring says which).

    export TF2_INTEGRATION=1 TF2_BTCLIB_NODE_PYTHON=<python>
    uv run pytest tests/integration/feature_bip68_sequence_btclib_node_test.py
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.integration.feature_bip68_sequence_test import (
    mempool_enforces_bip68_before_consensus_does,
)

if TYPE_CHECKING:
    from collections.abc import Callable

    from btclib_functional_tests.btclib_node import BtclibNodeAdapter
    from btclib_functional_tests.capability import SkipCounts

pytestmark = pytest.mark.integration


def test_mempool_enforces_bip68_before_consensus_does(
    btclib_node_cluster: Callable[[int], list[BtclibNodeAdapter]],
    skip_counts: SkipCounts,
) -> None:
    """The target: the body this module's docstring names, over btclib-node."""
    mempool_enforces_bip68_before_consensus_does(btclib_node_cluster, skip_counts)
