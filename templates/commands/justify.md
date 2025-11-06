# /rebase.justify Command Template

## Command Purpose
**Phase 3: Risk + ROI Analysis / Business Case** - Answer the "why now" question and secure approval

## When to Use
- After discovery and assessment phases are complete
- When seeking investment approval for modernization
- To make Go/No-Go decision on modernization initiative

## Prerequisites
- **discover.md** completed with business context
- **assess.md** completed with technical analysis
- Financial data for current system costs
- Budget parameters for modernization investment

## Execution Steps

### 1. Cost Analysis Framework

**Current System Costs (Annual):**
Calculate total cost of maintaining status quo:

```markdown
## Current System Costs
- Infrastructure/hosting: $______
- Maintenance/support: $______  
- Development velocity impact: $______
- Downtime/reliability costs: $______
- Security/compliance costs: $______
- Opportunity cost (delayed features): $______
- **Total Annual Cost: $______**
```

**Modernization Investment:**
Estimate one-time modernization costs:

```markdown
## Modernization Investment
- Development resources: $______
- Infrastructure migration: $______
- Training/knowledge transfer: $______
- Third-party tools/services: $______
- Risk mitigation (20% contingency): $______
- **Total Investment: $______**
```

### 2. Benefits Quantification

**Quantitative Benefits (Annual):**
Calculate measurable improvements:

```markdown
## Annual Benefits
- Reduced infrastructure costs: $______
- Improved development velocity: $______
- Decreased maintenance burden: $______
- Enhanced reliability value: $______
- Performance improvements: $______
- Faster time-to-market: $______
- **Total Annual Benefits: $______**
```

**Qualitative Benefits:**
Document non-quantified value:
- Improved developer experience
- Enhanced security posture
- Better scalability for growth
- Competitive advantage
- Risk reduction

### 3. ROI Calculations

**Financial Projections (3-Year):**
```markdown
| Year | Current Cost | Investment | Benefits | Net Impact |
|------|-------------|------------|----------|------------|
| 1    | $______     | $______    | $______  | $______    |
| 2    | $______     | $______    | $______  | $______    |
| 3    | $______     | $______    | $______  | $______    |
| Total| $______     | $______    | $______  | $______    |
```

**Key Metrics:**
- **ROI Percentage:** (Total Benefits - Investment) / Investment × 100
- **Payback Period:** Investment / Annual Benefits (in months)
- **Net Present Value:** Total benefits minus total investment

### 4. Risk Assessment

**Risks of NOT Modernizing:**
- Security vulnerabilities and compliance failures
- Inability to scale with business growth
- Developer productivity decline
- Competitive disadvantage
- Escalating maintenance costs

**Risks of Modernizing:**
- Project execution risks (delays, budget overruns)
- Technical risks (migration issues, performance)
- Business disruption during transition
- Team capacity and skill gaps

### 5. Go/No-Go Decision Framework

**Go Criteria (must meet all):**
- [ ] ROI ≥ 15% within 3 years
- [ ] Payback period ≤ 24 months
- [ ] Strategic alignment confirmed
- [ ] Resources and budget available
- [ ] Executive sponsorship secured
- [ ] Technical feasibility validated

**No-Go Triggers (any one stops initiative):**
- [ ] Negative or insufficient ROI
- [ ] Unacceptable risk profile
- [ ] Lack of strategic alignment
- [ ] Insufficient resources/budget
- [ ] Missing executive support
- [ ] Technical infeasibility

## Output Generation

### Business Case Document
Create comprehensive justification:

**Executive Summary:**
- Problem statement and urgency
- Proposed solution overview
- Financial case (ROI, payback, NPV)
- Risk assessment summary
- Recommendation with rationale

**Detailed Analysis:**
- Current state costs and limitations
- Modernization benefits and timeline
- Investment requirements and phasing
- Risk mitigation strategies
- Success criteria and measurement

### Decision-Ready Presentation
Structure for stakeholder approval:

```markdown
## Slide Structure
1. Current State Challenges
2. Modernization Opportunity  
3. Financial Analysis (ROI)
4. Risk Assessment
5. Implementation Options
6. Recommendation & Next Steps
```

### Go/No-Go Recommendation
Based on criteria assessment:

```markdown
## Decision: GO / NO-GO

**Rationale:**
[Clear explanation of recommendation based on criteria]

**If GO:**
- Business case meets all criteria
- Acceptable risk profile with mitigation
- Recommend proceeding to Phase 4 (Plan)

**If NO-GO:**
- Criteria not met: [list failing criteria]
- Alternative recommendations: [defer, smaller scope, etc.]
- Re-evaluation timeline: [when to revisit]
```

## Expected Outputs
- **justify.md** - Complete business case document
- ROI analysis with financial projections
- Risk assessment matrix
- Go/No-Go decision with rationale
- Executive presentation deck

## Next Steps

### If GO Decision:
1. Secure budget and resource allocation
2. Obtain formal stakeholder approval
3. Proceed to **Phase 4: Plan** (`/rebase.plan`)

### If NO-GO Decision:
1. Document decision rationale
2. Address failing criteria if possible
3. Set timeline for re-evaluation
4. Consider alternative approaches

## Command Usage Notes
- Requires accurate financial data for credible analysis
- Should involve finance/business stakeholders
- Critical decision point - thorough analysis essential
- Forms basis for all subsequent modernization work