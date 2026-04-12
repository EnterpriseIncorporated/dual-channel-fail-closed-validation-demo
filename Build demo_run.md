Demo Run – Dual-Channel Validation Outputs

This document describes the demonstration-only outputs included in this repository.
They illustrate how a dual-channel, fail-closed validation and enforcement model behaves in PASS and FAIL-CLOSED scenarios, without exposing production logic, cryptographic workflows, or enforcement mechanisms.

⸻

1. Demo location

The public demonstration of the system is located in the demo/ directory:
	•	example_output.json — PASS scenario (validation approved)
	•	fail_output.json — FAIL-CLOSED scenario (validation denied)

These files are representative outputs only and do not contain implementation details.

⸻

2. PASS scenario – example_output.json

In the PASS case, both channels align and validation is approved.

Key properties:
	•	validation_mode: DUAL_CHANNEL_REQUIRED
	•	execution_policy: FAIL_CLOSED
	•	validation_status: VALIDATION_APPROVED
	•	channels: both channels present and aligned
	•	enforcement_result: ALLOW

This demonstrates the normal path where dual-channel agreement satisfies validation under a fail-closed policy.

⸻

3. FAIL-CLOSED scenario – fail_output.json

In the FAIL-CLOSED case, the channels are both validated but do not match, and validation is denied.

Key properties:
	•	validation_mode: DUAL_CHANNEL_REQUIRED
	•	execution_policy: FAIL_CLOSED
	•	validation_status: VALIDATION_DENIED
	•	channels: both VALIDATED, but with mismatched input_hash values
	•	evidence_bundle.verification: VALIDATION_MISMATCH
	•	evidence_bundle.mismatch_detected: true
	•	enforcement_result: DENY

This demonstrates the denial path, where the system remains fail-closed when channel agreement is not achieved.

⸻

4. Conceptual behavior (high-level only)

At a high level, the demo illustrates the following conceptual behavior:
	1.	Dual-channel requirement
Two independent validation paths must agree before execution is permitted.
	2.	Validation before comparison
Each channel is represented as independently validated before comparison is performed.
	3.	Validation decision
	•	If both channels align → VALIDATION_APPROVED (PASS demo)
	•	If channels mismatch → VALIDATION_DENIED (FAIL-CLOSED demo)
	4.	Fail-closed posture
When mismatch or uncertainty occurs, the system defaults to deny rather than allow.

These behaviors are shown at a representational level only.

⸻

5. Scope and limitations of the demo

These demo outputs:

Do show:
	•	Dual-channel validation as a concept
	•	PASS vs FAIL-CLOSED enforcement outcomes
	•	Evidence bundle structure
	•	High-level validation and enforcement states

Do not show:
	•	Production enforcement logic
	•	Validation engine internals
	•	Real cryptographic workflows or key management
	•	Transport, session, or token lifecycle control
	•	Any implementation details of the underlying system

They are intended for illustration and discussion, not as a reference implementation.

⸻

6. Intended use

These demo files are provided to:
	•	Give reviewers a concrete sense of system behavior
	•	Support architecture, evaluation, and security-focused discussions
	•	Serve as a stable reference point for PASS and FAIL-CLOSED outcomes
	•	Maintain a clear boundary between public demonstration and private implementation

For evaluation or technical review, these outputs should be treated as representative artifacts, not as a complete system description.
