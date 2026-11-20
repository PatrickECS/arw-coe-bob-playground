# Arrow EMEA AI & Platform CoE – Project Process & Governance

## Purpose

This document defines the process for requesting and using resources in the Arrow EMEA AI & Platform CoE / Experience Center.

The CoE supports real customer and partner opportunities where technical validation, enablement, testing, integration, or a proof of concept is required.

The environment is not intended for private research or general sandbox usage.

---

# 1. What We Need Before Starting

Every project must have a clear business and technical purpose.

Before resources can be allocated, we need:

### Business Information

- Customer or partner name
- Country / region
- Business opportunity
- Account Manager or Arrow contact
- Business Development Manager (BDM), where applicable
- Local Arrow Solution Engineer
- Primary technical contact
- Expected business or technical outcome

### Technical Information

- Description of the use case
- What needs to be tested or validated
- Required technologies
- Required infrastructure
- Compute requirements
- GPU requirements, if applicable
- Storage requirements
- Networking requirements
- Required platforms or software
- Number of users requiring access
- Expected project duration
- Preferred start date
- Any vendor involvement or technical dependencies

The request must be detailed enough for the CoE team to understand what resources are required and whether the project can be supported.

---

# 2. Qualification

Before the project starts, a qualification discussion is required.

The purpose is to understand:

- What the customer or partner wants to achieve
- What needs to be validated
- Whether the CoE environment can support the requirement
- What infrastructure is required
- What technical support is required
- How much capacity is needed
- When the environment is required
- How long the project is expected to run
- What a successful outcome looks like

If the CoE cannot support the requested configuration or timeframe, an alternative architecture, resource plan, or schedule should be discussed.

---

# 3. Business Approval

CoE resources are not allocated automatically.

The project must be connected to a valid business opportunity and have appropriate Arrow business ownership.

The relevant BDM, Account Manager, or Arrow contact should confirm the business context and why CoE resources are required.

Resources should be prioritized for projects where technical validation can help progress a real customer or partner opportunity.

---

# 4. CoE Approval

The CoE team makes the final decision on whether the requested environment can be provided.

Approval depends primarily on:

### Infrastructure Fit

Do we have the required infrastructure, capacity, licenses, platforms, and technical support?

### Resource Availability

Can the requested resources be provided during the required timeframe without negatively affecting existing projects?

### Technical Readiness

Is the requesting team ready to work with the environment?

If additional knowledge or preparation is required, an enablement session can be arranged before the project starts.

### Business Relevance

Is there a clear customer, partner, technical, or business outcome associated with the project?

Only after these points are clear should infrastructure be reserved.

---

# 5. Environment Planning

After approval, the CoE team and the responsible Solution Engineer define what must be prepared.

This can include:

- Compute
- GPU resources
- Storage
- Networking
- OpenShift / Kubernetes
- OpenShift AI
- Virtualization
- AI infrastructure
- Vendor software
- Accounts
- VPN connectivity
- Permissions
- Project-specific namespaces or environments

Only the resources required for the approved project should be allocated.

---

# 6. User Onboarding

Access is personal and must not be shared.

For every user requiring access, the necessary onboarding information must be provided.

The user is then provided with:

- Personal account
- GlobalProtect VPN access, when required
- Access to the relevant environment
- Project-specific permissions

Users should only receive access to the resources required for their project.

Administrator or elevated access should only be provided when technically necessary.

---

# 7. Infrastructure Handover

Before active project work starts, the environment should be handed over to the responsible technical team.

During the handover we verify:

- Users can connect
- VPN access works
- Required accounts are available
- Required platforms are reachable
- Required permissions are working
- Infrastructure is available
- Project responsibilities are clear
- Important limitations are understood

Technical problems with the environment should ideally be identified during the handover rather than after the project has started.

---

# 8. Active Project Phase

Once the handover is complete, the customer, partner, vendor, and Arrow technical teams can perform the agreed work.

This can include:

- Proof of concept
- Technical validation
- Architecture validation
- Integration testing
- AI workload testing
- Performance testing
- Platform testing
- Customer demonstrations
- Technical enablement
- Solution development

The environment should be used for the agreed project purpose.

Significant changes to the infrastructure requirements should be discussed with the CoE team.

---

# 9. Project Sync

For active or longer-running projects, regular short syncs should be held.

The purpose is to understand:

- Current status
- Progress
- Technical blockers
- Infrastructure problems
- Resource utilization
- Changes in requirements
- Additional resources required
- Whether the timeline is still realistic

These meetings should remain short and operational.

The CoE team does not need detailed project management information. The important point is understanding whether the environment is being used effectively and whether technical support or infrastructure changes are required.

---

# 10. Standard Project Duration

The standard allocation period is approximately **one month**.

Resources should not remain allocated indefinitely.

If more time is required, the project can be extended.

An extension should be discussed before the existing allocation expires and should explain:

- Current project status
- Why additional time is required
- What work remains
- How much additional time is required
- Whether the same infrastructure is still required

Multiple extensions are possible when justified.

---

# 11. Inactive Projects

The CoE is shared infrastructure and unused resources should be returned to the available capacity pool.

If an environment remains inactive for approximately **7 consecutive days**, the CoE team may review the environment.

Depending on the infrastructure, resources may be:

- Scaled down
- Suspended
- Released
- Decommissioned

Projects can be reactivated when there is a valid requirement and capacity is available.

---

# 12. Project Completion / Recap

At the end of the project, a short recap should be completed.

We want to understand:

- What was tested
- What was achieved
- Whether the validation was successful
- What technical challenges were discovered
- What value the CoE provided
- What the next step is
- Whether the opportunity is progressing
- Whether additional validation is required

The purpose is not administrative reporting.

The objective is to understand the value of the environment and make successful work reusable across EMEA.

---

# 13. Sharing the Result

Successful projects should, where possible, be documented.

This can be:

- Short technical summary
- Show & Tell session
- Demo
- Video
- One-page summary
- Reference use case
- Blog or internal article
- Customer or partner success story
- LinkedIn post when appropriate

Sensitive customer or partner information must only be shared with the appropriate approval.

The goal is to turn successful technical validation into reusable knowledge for other Arrow teams, partners, and customers.

---

# 14. Project Closure

Once the project is complete and no extension is required:

- User access can be reviewed or removed
- Project-specific environments can be decommissioned
- Reserved compute and GPU resources can be released
- Storage can be cleaned up or archived where required
- Temporary accounts and permissions can be removed
- Infrastructure becomes available for new projects

Nothing should be deleted before confirming whether project data, configurations, documentation, or results need to be retained.

---

# Process Summary

**Request → Qualification → Business Approval → CoE Approval → Environment Planning → User Onboarding → Infrastructure Handover → Active Project → Regular Sync → Recap → Extension or Closure**

The overall principle is simple:

**We first understand the opportunity and requirements, then approve and allocate the right resources, support the technical validation, review the result, and finally release the resources for the next project.**
