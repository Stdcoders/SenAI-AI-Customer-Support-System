# Service Level Agreement (SLA) Policy

**Document ID:** SLA-001

**Version:** 4.0

**Last Updated:** June 2026

---

# Overview

This document defines SenAI's uptime commitments, incident response procedures, customer communication standards, service credits, and Root Cause Analysis (RCA) obligations.

The AI Agent must reference this policy whenever handling outages, production incidents, support escalations, or legal complaints related to availability.

---

# Uptime Commitment

## Standard Plan

Guaranteed Uptime:

99.5%

---

## Enterprise Plan

Guaranteed Uptime:

99.9%

Measured monthly.

Scheduled maintenance windows are excluded from SLA calculations.

---

# Incident Severity Levels

## P0 - Critical

Examples:

* Complete platform outage
* Data loss
* Security breach
* Authentication failure affecting all customers

Target Initial Response:

15 minutes

Engineering engagement:

Immediate

Executive notification:

Required

---

## P1 - High

Examples:

* Major feature unavailable
* Significant API degradation

Target Response:

1 hour

---

## P2 - Medium

Examples:

* Partial functionality loss
* Performance degradation

Target Response:

4 hours

---

## P3 - Low

Examples:

* UI issues
* Minor bugs
* Documentation corrections

Target Response:

1 business day

---

# Root Cause Analysis

**Policy ID: RCA-001**

For every P0 incident:

* RCA delivered within 24 hours
* Timeline included
* Impact assessment included
* Corrective actions documented
* Prevention measures documented

The AI agent may communicate that an RCA will be delivered but must never generate technical RCA details.

---

# SLA Credit Policy

**Policy ID: SLA-CREDIT-001**

Enterprise customers may qualify for service credits.

Monthly Availability | Credit

99.9%+ → No Credit

99.0%–99.89% → 10%

98.0%–98.99% → 25%

Below 98.0% → 50%

Credits are applied to future invoices and are not cash refunds.

The AI agent must never calculate custom credits outside this policy.

---

# Legal Escalation

If an email contains:

* legal review
* cease and desist
* attorney
* lawsuit
* breach of contract

the AI agent must:

1. Flag Legal
2. Escalate to Human
3. Generate holding response
4. Notify Customer Success Director

Automatic replies are prohibited.

---

# Communication Standards

During active incidents:

The AI agent may:

* acknowledge the issue
* confirm investigation
* provide status page links
* reference SLA commitments

The AI agent must not:

* speculate on causes
* assign blame
* promise resolution times
* disclose confidential information

---

# Enterprise Renewal Protection

If an Enterprise customer has:

* active renewal
* open outage
* legal escalation

the AI agent must prioritize:

Critical

and immediately escalate to:

Customer Success Director

Engineering Lead

Legal Team

---

# Agent Guidance

The AI agent MAY:

* explain SLA commitments
* explain incident severity
* reference RCA timelines
* reference published service credit policy

The AI agent MUST NOT:

* invent SLA terms
* negotiate credits
* approve refunds
* publish technical RCA findings

---

# Related Documents

pricing_policy.md

refund_policy.md

escalation_matrix.md

---

End of Document
