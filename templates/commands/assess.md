# /rebase.assess Command Template

## Command Purpose
**Phase 2: Current System Audit** - Understand the "what" from a technical perspective

## When to Use
- After business discovery phase is complete
- When technical understanding is needed for ROI calculations
- Before creating modernization business case

## Prerequisites
- **discover.md** should be completed first
- Access to codebase and system documentation
- Technical team availability for assessment

## Execution Steps

### 1. Technology Stack Analysis
Analyze and document current technology:

**Code Analysis:**
- Programming languages and versions
- Frameworks and libraries in use
- Database technologies and versions
- Infrastructure and deployment methods

**Dependency Assessment:**
- Third-party library versions
- End-of-life components
- Security vulnerabilities
- License compliance issues

### 2. Architecture Review
Evaluate current system architecture:

**System Structure:**
- Monolithic vs. distributed architecture
- Component boundaries and relationships
- Data flow and integration patterns
- Scalability limitations

**Code Quality Assessment:**
- Technical debt hotspots
- Test coverage and quality
- Code complexity metrics
- Documentation completeness

### 3. Performance and Security Analysis
Assess non-functional aspects:

**Performance Issues:**
- Response time bottlenecks
- Scalability constraints
- Resource utilization problems
- Load handling limitations

**Security Concerns:**
- Known vulnerabilities
- Security best practices compliance
- Data protection measures
- Access control implementation

### 4. Business Impact Mapping
Connect technical issues to business impact:

**Technical Issue → Business Impact Matrix:**
```markdown
| Technical Issue | Business Impact | Severity | Cost of Inaction |
|----------------|----------------|----------|------------------|
| Slow API responses | Poor user experience | High | Lost customers |
| Outdated framework | Security vulnerabilities | Critical | Compliance risk |
| Manual deployment | Slow feature delivery | Medium | Competitive disadvantage |
```

### 5. Priority Assessment
Rank modernization areas by:
- Business impact severity
- Technical complexity
- Implementation effort
- Risk of current state

## Output Generation

Create comprehensive assessment document with:

### Current State Technical Report
- Technology stack inventory
- Architecture assessment summary
- Code quality metrics
- Performance benchmarks

### Risk Assessment
- Critical technical risks
- Security vulnerabilities
- Compliance gaps
- Operational risks

### Business Impact Analysis
- Technical constraints blocking business goals
- Cost of maintaining current state
- Productivity impact on development teams
- Customer/user experience issues

### Modernization Priority Matrix
```markdown
## High Impact, Low Effort (Quick Wins)
- [Issues that provide immediate value]

## High Impact, High Effort (Strategic)
- [Major modernization initiatives]

## Low Impact, Low Effort (Nice-to-Have)
- [Minor improvements]

## Low Impact, High Effort (Avoid)
- [Not recommended for modernization]
```

## Expected Outputs
- **assess.md** - Complete technical assessment
- Technology health scorecard
- Risk assessment matrix
- Business impact mapping
- Modernization priority recommendations

## Next Steps
Upon completion:
1. Review technical findings with development team
2. Validate business impact assessments
3. Proceed to **Phase 3: Justify** (`/rebase.justify`)

## Command Usage Notes
- Requires technical expertise for accurate assessment
- May need automated tools for code analysis
- Should involve multiple technical stakeholders
- Forms foundation for ROI calculations in justify phase