# Edict Release Review Checklist

## Purpose

This document is a compact review checklist for deciding whether the current
`Edict` package surface is still in `Draft`, has reached `Candidate`, or is
coherent enough to treat as `Release-Ready` in the current release-prep sense.

It is a review aid, not an updater spec.

## Fast Review

Answer these questions in order:

1. Does a real managed payload example exist?
2. Is package-to-instance mapping explicit?
3. Are managed ownership and managed-vs-local boundaries explicit?
4. Are compatibility categories documented clearly enough for later updater
   work?
5. Is local overlay, live state, and instance-support material still outside
   the package payload?
6. Is release-support positioning clear enough that release notes and migration
   notes are not being silently mixed into installed payload by default?

## Current Stage Heuristic

Treat the package surface as `Draft` if one or more of these are true:

- the payload is still only conceptual
- ownership is still unstable
- mapping to `.raiden/edict/` is still implicit
- the package boundary still depends on unresolved cleanup

Treat the package surface as `Candidate` if all of these are true:

- a real payload example exists
- package-to-instance mapping is explicit
- managed-vs-local separation is mostly clear
- remaining questions are mainly about release confidence, compatibility, or
  transition support

Treat the package surface as `Release-Ready` for current canon only if all of
these are true:

- the payload example is real and coherent
- managed ownership is explicit
- mapping to `.raiden/edict/` is explicit
- compatibility categories are documented
- release-support positioning is explicit enough to avoid mixing transition
  notes into installed payload by default
- no obvious local-only material has leaked into the package surface

## What This Checklist Does Not Approve Yet

Even if the review passes, it does not mean RAIDEN has settled:

- manifest schema
- release artifact format
- version comparison semantics
- migration-record schema
- rollback behavior
- updater command behavior

Those remain intentionally deferred.
