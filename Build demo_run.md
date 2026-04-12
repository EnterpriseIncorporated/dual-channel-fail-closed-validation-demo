# Demo Run – Dual-Channel Consensus Outputs

This document describes the demonstration-only outputs included in this repository.  
They illustrate how a dual-channel, fail-closed consensus posture behaves in a **PASS** and **FAIL-CLOSED** scenario, without exposing production logic, cryptographic workflows, or enforcement mechanisms.

---

## 1. Demo location

The public demonstration of the system is located in the `demo/` directory:

- `example_output.json` — PASS scenario (consensus reached)
- `fail_output.json` — FAIL-CLOSED scenario (consensus denied)

These files are **representative outputs only** and do not contain implementation details.

---

## 2. PASS scenario – `example_output.json`

In the PASS case, both channels align and consensus is reached.

**Key properties:**

- **consensus_mode:** `DUAL_CHANNEL_REQUIRED`
- **execution_policy:** `FAIL_CLOSED`
- **consensus_status:** `CONSENSUS_REACHED`
- **channels:** both channels present and aligned
- **enforcement_result:** represented as an allow/continue posture in the demo

This demonstrates the **normal path** where dual-channel agreement is achieved under a fail-closed policy.

---

## 3. FAIL-CLOSED scenario – `fail_output.json`

In the FAIL-CLOSED case, the channels are both validated but do **not** match, and consensus is denied.

**Key properties:**

- **consensus_mode:** `DUAL_CHANNEL_REQUIRED`
- **execution_policy:** `FAIL_CLOSED`
- **consensus_status:** `CONSENSUS_DENIED`
- **channels:** both `VALIDATED`, but with mismatched `input_hash` values
- **evidence_bundle.verification:** `CONSENSUS_FAILED`
- **evidence_bundle.mismatch_detected:** `true`
- **enforcement_result:** `DENY`

This demonstrates the **denial path**, where the system remains fail-closed when channel agreement is not achieved.

---

## 4. Conceptual behavior (high-level only)

At a high level, the demo illustrates the following conceptual behavior:

1. **Dual-channel requirement:**  
   Two independent channels must agree for consensus to be considered valid.

2. **Validation before comparison:**  
   Each channel is represented as individually validated before any comparison is shown in the demo.

3. **Consensus decision:**  
   - If both channels align → `CONSENSUS_REACHED` (PASS demo)  
   - If channels mismatch → `CONSENSUS_DENIED` (FAIL-CLOSED demo)

4. **Fail-closed posture:**  
   When in doubt, or when mismatch is detected, the system posture is **deny** rather than **allow**.

These behaviors are shown at a **representational** level only.

---

## 5. Scope and limitations of the demo

These demo outputs:

- **Do show:**
  - Dual-channel requirement as a concept
  - PASS vs FAIL-CLOSED outcomes
  - Presence of an evidence bundle structure
  - High-level consensus status and enforcement posture

- **Do not show:**
  - Production enforcement logic
  - Actual consensus engine internals
  - Real cryptographic workflows or key management
  - Transport, session, or token lifecycle control
  - Any implementation details of the underlying system

They are intended for **illustration and discussion**, not as a reference implementation.

---

## 6. Intended use

These demo files are provided to:

- Give reviewers a concrete sense of system behavior
- Support architecture, evaluation, and security-focused discussions
- Serve as a stable reference point for PASS and FAIL-CLOSED outcomes
- Preserve a clear boundary between **public demonstration** and **private implementation**

For evaluation, architecture discussions, or deeper technical review, these outputs should be treated as **representative artifacts**, not as a full description of the system.
