# Copyright (c) The btclib developers
# Distributed under the MIT software license, see the accompanying
# LICENSE file or https://opensource.org/license/mit for the full text.

r"""Core's `feature_cltv`, rewritten on this harness: btclib-node.

`feature_cltv_test.py` beside this module holds the bodies, run here
against the target rather than the oracle (rule 3 of issue
btclib-org/btclib#2220). `Capability.TEST_ACTIVATION_HEIGHT` is
declared per build, and `Capability.ACCEPT_NON_STANDARD` by none
(`btclib_node.py`'s own docstring has both), so the mempool body is a
counted skip; the log body also asks for `Capability.DEBUG_LOG`,
bitcoind's alone.

    export TF2_INTEGRATION=1 TF2_BTCLIB_NODE_PYTHON=<python>
    uv run pytest \
        tests/integration/feature_cltv_btclib_node_test.py
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.integration.feature_cltv_test import (
    a_version_3_block_is_logged_once_active,
    a_version_3_block_is_refused_once_active,
    cltv_activates_one_block_before_the_configured_height,
    cltv_failures_are_mined_until_the_configured_height,
    cltv_failures_are_refused_by_the_mempool,
    cltv_failures_are_refused_in_a_block,
)

if TYPE_CHECKING:
    from collections.abc import Callable

    from btclib_functional_tests.btclib_node import BtclibNodeAdapter
    from btclib_functional_tests.capability import SkipCounts

pytestmark = pytest.mark.integration


def test_cltv_activates_one_block_before_the_configured_height(
    btclib_node_cluster: Callable[[int], list[BtclibNodeAdapter]],
    skip_counts: SkipCounts,
) -> None:
    """The target: the body this module's docstring names, over btclib-node."""
    cltv_activates_one_block_before_the_configured_height(
        btclib_node_cluster, skip_counts
    )


def test_a_version_3_block_is_refused_once_active(
    btclib_node_cluster: Callable[[int], list[BtclibNodeAdapter]],
    skip_counts: SkipCounts,
) -> None:
    """The target: the body this module's docstring names, over btclib-node."""
    a_version_3_block_is_refused_once_active(btclib_node_cluster, skip_counts)


def test_a_version_3_block_is_logged_once_active(
    btclib_node_cluster: Callable[[int], list[BtclibNodeAdapter]],
    skip_counts: SkipCounts,
) -> None:
    """The target: the body this module's docstring names, over btclib-node."""
    a_version_3_block_is_logged_once_active(btclib_node_cluster, skip_counts)


def test_cltv_failures_are_mined_until_the_configured_height(
    btclib_node_cluster: Callable[[int], list[BtclibNodeAdapter]],
    skip_counts: SkipCounts,
) -> None:
    """The target: the body this module's docstring names, over btclib-node."""
    cltv_failures_are_mined_until_the_configured_height(
        btclib_node_cluster, skip_counts
    )


def test_cltv_failures_are_refused_by_the_mempool(
    btclib_node_cluster: Callable[[int], list[BtclibNodeAdapter]],
    skip_counts: SkipCounts,
) -> None:
    """The target: skipped on `Capability.ACCEPT_NON_STANDARD`."""
    cltv_failures_are_refused_by_the_mempool(btclib_node_cluster, skip_counts)


def test_cltv_failures_are_refused_in_a_block(
    btclib_node_cluster: Callable[[int], list[BtclibNodeAdapter]],
    skip_counts: SkipCounts,
) -> None:
    """The target: the block refusals, which ask for `Capability.MINE` alone."""
    cltv_failures_are_refused_in_a_block(btclib_node_cluster, skip_counts)
