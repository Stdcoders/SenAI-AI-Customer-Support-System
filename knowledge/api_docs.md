# API Documentation

**Document ID:** API-001

**Version:** 2.5

**Last Updated:** June 2026

---

# Overview

This document describes SenAI public API capabilities, authentication requirements, versioning strategy, rate limits, and deprecation policy.

AI Agents must reference this document when responding to API-related inquiries.

---

# Base URL

https://api.senai.ai/v2

---

# Authentication

All requests require:

Authorization: Bearer <API_KEY>

API keys are generated from the Developer Dashboard.

AI Agents must never expose or generate API keys.

---

# API Versions

Supported:

v2

Deprecated:

v1

v1 remains available until December 31, 2026.

Migration to v2 is strongly recommended.

---

# Rate Limits

Starter

100 requests/minute

---

Standard

1000 requests/minute

---

Enterprise

Unlimited

Subject to fair usage policy.

---

# Common Headers

Required:

Authorization

Content-Type: application/json

Accept: application/json

Optional:

X-Request-ID

X-Correlation-ID

---

# Error Codes

200

Success

400

Invalid Request

401

Unauthorized

403

Forbidden

404

Resource Not Found

409

Conflict

422

Validation Error

429

Rate Limit Exceeded

500

Internal Server Error

---

# Pagination

Supported parameters:

limit

offset

cursor

Maximum limit:

100 records

---

# Breaking Changes in v2

* OAuth support
* Improved filtering
* Cursor pagination
* Enhanced webhook security
* Consistent JSON responses

---

# Webhooks

Retry Policy:

3 attempts

Exponential backoff

Timeout:

10 seconds

Failed deliveries appear in the Developer Dashboard.

---

# AI Agent Guidance

The AI Agent MAY:

* explain endpoints
* explain authentication
* explain rate limits
* explain version differences

The AI Agent MUST NOT:

* invent undocumented endpoints
* reveal secrets
* generate API keys
* guarantee backward compatibility

---

# Related Documents

pricing_policy.md

compliance_faq.md

sla_policy.md

---

End of Document
