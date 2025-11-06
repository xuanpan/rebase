# /rebase.plan Command Template

## Command Purpose
**Phase 4: Future State Design & Roadmap** - Define the "how" to reach the desired state

## When to Use
- After successful Go decision from justify phase
- When detailed implementation planning is needed
- Before beginning modernization execution

## Prerequisites
- **discover.md**, **assess.md**, **justify.md** completed
- Go decision approved with budget allocation
- Stakeholder approval for modernization initiative
- Technical and business teams identified

## Execution Steps

### 1. Future State Architecture Design

**Technology Stack Selection:**
Based on assessment results and business requirements:

```markdown
## Target Technology Stack
- **Programming Language:** [Choice with rationale]
- **Framework:** [Choice with rationale]  
- **Database:** [Choice with rationale]
- **Cloud Platform:** [Choice with rationale]
- **Container Technology:** [Choice with rationale]

## Technology Selection Criteria
- Business requirements alignment
- Team skills and learning curve
- Community support and ecosystem
- Long-term viability
- Total cost of ownership
- Integration capabilities
```

**Architecture Principles:**
Define guiding principles for modern system:
- Scalability and performance requirements
- Security and compliance standards
- Maintainability and developer experience
- Integration and API design
- Data architecture and migration strategy

### 2. Migration Strategy Selection

**Approach Options Analysis:**

**Option A: Strangler Fig Pattern**
- Incremental replacement of components
- Maintain functionality throughout migration
- Lower risk, longer timeline

**Option B: Parallel Run Migration**  
- New system developed alongside existing
- Gradual traffic migration with validation
- Medium risk, medium timeline

**Option C: Big Bang Migration**
- Complete replacement in single release
- Higher risk, shorter timeline

**Recommended Approach:**
```markdown
## Selected Strategy: [Choice]

**Rationale:**
- Business risk tolerance: [Assessment]
- Technical complexity: [Assessment]  
- Resource constraints: [Assessment]
- Timeline requirements: [Assessment]
```

### 3. Phased Implementation Roadmap

**Phase Breakdown:**
Create detailed timeline with milestones:

```markdown
## Phase 1: Foundation (Months 1-X)
**Objectives:**
- Infrastructure setup and CI/CD
- Development environment preparation
- Team training and onboarding
- Core platform components

**Deliverables:**
- [Specific deliverables]

**Success Criteria:**
- [Measurable success criteria]

## Phase 2: Core Migration (Months X-Y)
**Objectives:**
- Primary business logic migration
- Data layer modernization
- API development and testing

## Phase 3: Integration & Optimization (Months Y-Z)
**Objectives:**
- System integration and testing
- Performance optimization
- User training and adoption
```

### 4. Resource Planning

**Team Composition:**
Define required team structure:

```markdown
## Development Team
- Technical Lead: X FTE
- Senior Developers: X FTE
- Mid-level Developers: X FTE
- UI/UX Designers: X FTE
- DevOps Engineers: X FTE
- QA Engineers: X FTE

## Business Team  
- Product Manager: X FTE
- Business Analysts: X FTE
- Change Management: X FTE

## Total Investment
- Monthly team cost: $X
- Total project cost: $X
- External contractors: $X
```

**Skills and Training:**
- Required competencies assessment
- Training plans for new technologies
- Knowledge transfer from legacy system
- External consulting needs

### 5. Risk Management Strategy

**Risk Mitigation Plans:**
For each identified risk, define mitigation:

```markdown
## Technical Risks
- **Data Migration Risk:** [Mitigation strategy]
- **Performance Risk:** [Mitigation strategy]
- **Integration Risk:** [Mitigation strategy]

## Business Risks  
- **User Adoption Risk:** [Mitigation strategy]
- **Timeline Risk:** [Mitigation strategy]
- **Budget Risk:** [Mitigation strategy]
```

**Rollback Procedures:**
- Data backup and recovery plans
- System rollback capabilities
- Communication procedures for issues
- Decision criteria for rollback

### 6. Success Measurement Framework

**Key Performance Indicators:**

```markdown
## Technical KPIs
- System performance (response time, throughput)
- Reliability (uptime, error rates)
- Development velocity (features per sprint)
- Code quality metrics

## Business KPIs
- User satisfaction scores
- Feature delivery speed  
- Operational cost reduction
- Revenue/business metric improvements

## Project KPIs
- Timeline adherence
- Budget compliance
- Scope delivery
- Risk mitigation effectiveness
```

**Measurement Baseline:**
Document current state metrics for comparison

## Output Generation

Create comprehensive implementation plan:

### Modernization Roadmap
- Visual timeline with phases and milestones
- Resource allocation schedule
- Dependency mapping
- Risk mitigation checkpoints

### Technical Implementation Plan
- Architecture specifications
- Migration procedures
- Testing strategies  
- Deployment plans

### Project Management Framework
- Governance structure
- Communication plans
- Change management approach
- Progress reporting mechanisms

## Expected Outputs
- **plan.md** - Complete implementation plan
- Detailed project roadmap with timeline
- Resource allocation and budget breakdown
- Risk management and mitigation strategies
- Success criteria and measurement framework

## Next Steps
Upon completion:
1. Final stakeholder review and approval
2. Project governance establishment
3. Team assembly and onboarding
4. Begin Phase 1 (Foundation) implementation

## Command Usage Notes
- Requires input from technical and business stakeholders
- Should align with approved business case from justify phase
- Forms basis for project execution and governance
- May require iterations based on stakeholder feedback
- Critical for setting realistic expectations and accountability