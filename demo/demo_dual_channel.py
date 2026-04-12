"""
DEMO ONLY - NOT THE REAL SYSTEM
--------------------------------
This is a simplified demonstration of selected concepts from a
dual-channel fail-closed enforcement architecture.

It does NOT contain:
- production enforcement logic
- cryptographic mechanisms
- continuous validation internals
- private implementation details
- operational deployment components

This file is provided for public demonstration purposes only.
"""

import json
from datetime import datetime


def channel_a_check(mode: str = "pass") -> dict:
    if mode == "fail":
        return {
            "input_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            "status": "VALIDATED",
        }
    return {
        "input_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        "status": "VALIDATED",
    }


def channel_b_check(mode: str = "pass") -> dict:
    if mode == "fail":
        return {
            "input_hash": "7f83b1657ff1fc53b92dc18148a1d65dfa135f8a1f5f8c3d5f8e6a2c3d4f5e6a",
            "status": "VALIDATED",
        }
    return {
        "input_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        "status": "VALIDATED",
    }


def build_demo_output(mode: str = "pass") -> dict:
    channel_a = channel_a_check(mode)
    channel_b = channel_b_check(mode)

    aligned = channel_a["input_hash"] == channel_b["input_hash"]

    if aligned:
        return {
            "demo_timestamp": datetime.utcnow().isoformat() + "Z",
            "system_version": "demo-only-v1",
            "validation_mode": "DUAL_CHANNEL_REQUIRED",
            "execution_policy": "FAIL_CLOSED",
            "validation_status": "VALIDATION_APPROVED",
            "channels": {
                "channel_a": channel_a,
                "channel_b": channel_b,
            },
            "evidence_bundle": {
                "bundle_id": "demo-bundle-001",
                "evidence_hash": "hash_of_channel_inputs_demo",
                "verification": "VALIDATION_CONFIRMED",
                "linked_channels": ["channel_a", "channel_b"],
            },
            "enforcement_result": "ALLOW",
            "note": (
                "This output demonstrates a validation-approved scenario under "
                "a fail-closed policy. It represents high-level system behavior "
                "only and does not include production enforcement logic or "
                "cryptographic mechanisms."
            ),
        }

    return {
        "demo_timestamp": datetime.utcnow().isoformat() + "Z",
        "system_version": "demo-only-v1",
        "validation_mode": "DUAL_CHANNEL_REQUIRED",
        "execution_policy": "FAIL_CLOSED",
        "validation_status": "VALIDATION_DENIED",
        "channels": {
            "channel_a": channel_a,
            "channel_b": channel_b,
        },
        "evidence_bundle": {
            "bundle_id": "demo-bundle-002",
            "evidence_hash": "hash_of_channel_inputs_demo",
            "verification": "VALIDATION_MISMATCH",
            "linked_channels": ["channel_a", "channel_b"],
            "mismatch_detected": True,
        },
        "enforcement_result": "DENY",
        "note": (
            "This output demonstrates a fail-closed denial scenario triggered "
            "by a validation mismatch. It represents high-level system behavior "
            "only and does not include production enforcement logic or "
            "cryptographic mechanisms."
        ),
    }


if __name__ == "__main__":
    print("Running dual-channel validation demo...\n")

    print("PASS scenario:")
    print(json.dumps(build_demo_output("pass"), indent=2))

    print("\nFAIL-CLOSED scenario:")
    print(json.dumps(build_demo_output("fail"), indent=2))
