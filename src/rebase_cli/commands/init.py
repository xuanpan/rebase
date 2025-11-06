# src/rebase_cli/commands/init.py
"""
Module for the 'rebase init' command.

Handles legacy system modernization project initialization:
- Creates modernization project structure in existing codebases (--here)
- Creates separate modernization projects for analysis
- Copies rebase templates and scripts from this repository
- Sets up AI assistant context for code modernization
- Initializes Git repository if needed
- Displays modernization workflow next steps
"""

import os
import shutil
import sys
from pathlib import Path
import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()

# AI assistant configuration for modernization workflows
AGENT_CONFIG = {
    "copilot": {
        "name": "GitHub Copilot", 
        "context_file": ".github/copilot-instructions.md",
        "description": "GitHub's AI pair programmer with excellent code modernization capabilities"
    },
    "claude": {
        "name": "Claude AI", 
        "context_file": "CLAUDE.md",
        "description": "Anthropic's Claude with strong architectural reasoning for legacy system analysis"
    },
    "cursor": {
        "name": "Cursor", 
        "context_file": ".cursor/rules/rebase-rules.md",
        "description": "AI-first code editor with excellent refactoring capabilities"
    },
    "windsurf": {
        "name": "Windsurf", 
        "context_file": ".windsurf/rules/rebase-rules.md",
        "description": "AI coding assistant focused on large-scale code transformations"
    },
}

app = typer.Typer(help="Rebase CLI commands for legacy system modernization")


def detect_legacy_system_type(project_path: Path) -> str:
    """Detect the type of legacy system based on project files."""
    if (project_path / "pom.xml").exists():
        return "Java/Maven"
    elif (project_path / "build.gradle").exists():
        return "Java/Gradle"
    elif (project_path / "package.json").exists():
        return "Node.js/JavaScript"
    elif (project_path / "requirements.txt").exists() or (project_path / "pyproject.toml").exists():
        return "Python"
    elif (project_path / "Gemfile").exists():
        return "Ruby"
    elif (project_path / "go.mod").exists():
        return "Go"
    elif (project_path / "Cargo.toml").exists():
        return "Rust"
    elif any(project_path.glob("*.csproj")) or any(project_path.glob("*.sln")):
        return ".NET/C#"
    elif (project_path / "composer.json").exists():
        return "PHP"
    else:
        return "Unknown/Custom"


def setup_rebase_structure(project_path: Path, ai_assistant: str):
    """Create the rebase directory structure in the target project."""
    rebase_dir = project_path / ".rebase"
    rebase_dir.mkdir(exist_ok=True)
    
    # Create subdirectories
    (rebase_dir / "templates").mkdir(exist_ok=True)
    (rebase_dir / "templates" / "commands").mkdir(exist_ok=True)
    (rebase_dir / "scripts").mkdir(exist_ok=True)
    (rebase_dir / "scripts" / "bash").mkdir(exist_ok=True)
    (rebase_dir / "scripts" / "powershell").mkdir(exist_ok=True)
    
    # Create other directories
    (project_path / "memory").mkdir(exist_ok=True)
    (project_path / "specs").mkdir(exist_ok=True)
    
    return rebase_dir


def copy_rebase_templates(project_path: Path, rebase_dir: Path):
    """Copy templates and scripts from the rebase repository to the project."""
    # Get the rebase repository root (3 levels up from this file)
    repo_root = Path(__file__).parent.parent.parent.parent
    
    # Copy templates
    templates_src = repo_root / "templates"
    if templates_src.exists():
        for template_file in templates_src.rglob("*"):
            if template_file.is_file():
                rel_path = template_file.relative_to(templates_src)
                dest_path = rebase_dir / "templates" / rel_path
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(template_file, dest_path)
    
    # Copy scripts
    scripts_src = repo_root / "scripts"
    if scripts_src.exists():
        for script_file in scripts_src.rglob("*"):
            if script_file.is_file():
                rel_path = script_file.relative_to(scripts_src)
                dest_path = rebase_dir / "scripts" / rel_path
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(script_file, dest_path)
                # Make scripts executable on Unix systems
                if dest_path.suffix == ".sh":
                    dest_path.chmod(0o755)


def create_ai_context_file(project_path: Path, ai_assistant: str, project_name: str, system_type: str):
    """Create AI assistant context file for the modernization project."""
    agent_config = AGENT_CONFIG[ai_assistant]
    context_file_path = project_path / agent_config["context_file"]
    
    # Ensure parent directory exists
    context_file_path.parent.mkdir(parents=True, exist_ok=True)
    
    context_content = f"""# {project_name} - Legacy System Modernization

Auto-generated rebase context for {agent_config['name']}. Last updated: {Path(__file__).stat().st_mtime}

## Legacy System Information

**System Type**: {system_type}
**Project**: {project_name}
**Modernization Framework**: Rebase CLI (Business-Focused Approach)

## Available Rebase Commands

Use these slash commands to drive the business-focused modernization process:

### Core Modernization Workflow

| Command | Description | Template |
|---------|-------------|----------|
| `/rebase.discover` | Phase 1: Business Discovery & Context - understand business drivers and stakeholder needs | `.rebase/templates/commands/discover.md` |
| `/rebase.assess` | Phase 2: Current System Audit - technical analysis and business impact mapping | `.rebase/templates/commands/assess.md` |
| `/rebase.justify` | Phase 3: Risk + ROI Analysis - create business case with Go/No-Go decision | `.rebase/templates/commands/justify.md` |
| `/rebase.plan` | Phase 4: Future State Design & Roadmap - detailed implementation planning | `.rebase/templates/commands/plan.md` |

### Command Execution Pattern

Each command follows this pattern:
1. **Read the command template** from `.rebase/templates/commands/[command].md`
2. **Use the base template** from `.rebase/templates/[command]-template.md` 
3. **Generate the output** following the command template instructions
4. **Save results** to `.rebase/[command].md`

### Decision Gates

Each phase includes decision gates to ensure business value:

1. **After /rebase.discover**: Confirm business case exists
2. **After /rebase.assess**: Validate technical feasibility  
3. **After /rebase.justify**: **Go/No-Go Decision** - Approve investment
4. **After /rebase.plan**: Approve implementation approach

## Business-Focused Modernization Principles

**Business Value First**: Every decision traced to business outcomes
**Risk Management**: Incremental approaches over big-bang migrations  
**Evidence-Based**: Data-driven decisions with measurable success criteria
**ROI-Focused**: Clear financial justification for modernization investment

## Project Structure

```
{project_name}/
├── .rebase/                 # Rebase framework files
│   ├── discover.md         # Phase 1: Business discovery results (generated by /rebase.discover)
│   ├── assess.md           # Phase 2: Technical assessment (generated by /rebase.assess)
│   ├── justify.md          # Phase 3: Business case and ROI (generated by /rebase.justify)
│   ├── plan.md             # Phase 4: Implementation roadmap (generated by /rebase.plan)
│   ├── constitution.md     # Modernization principles and governance
│   └── templates/          # Rebase templates and command instructions
│       ├── discover-template.md    # Base template for business discovery
│       ├── assess-template.md      # Base template for technical assessment
│       ├── justify-template.md     # Base template for business case
│       ├── plan-template.md        # Base template for implementation plan
│       └── commands/               # Command execution instructions
│           ├── discover.md         # How to execute /rebase.discover
│           ├── assess.md           # How to execute /rebase.assess
│           ├── justify.md          # How to execute /rebase.justify
│           └── plan.md             # How to execute /rebase.plan
├── src/                    # Existing legacy source code
└── {agent_config['context_file']}  # This file - AI assistant context
```

## Legacy System Context

**Business Context**: {system_type} system requiring modernization
**Current State**: Analyze with `/rebase.assess` for technical details
**Modernization Goals**: Define with `/rebase.discover` for business objectives  
**Investment Decision**: Build with `/rebase.justify` for ROI and approval
**Implementation Strategy**: Design with `/rebase.plan` for execution roadmap

## Getting Started

The business-focused modernization process follows these steps:

1. **Business Discovery** (`/rebase.discover`)
   - Interview stakeholders and understand business drivers
   - Identify pain points and success criteria
   - Document strategic context and constraints

2. **Technical Assessment** (`/rebase.assess`) 
   - Audit current system architecture and code quality
   - Identify technical risks and bottlenecks
   - Map technical issues to business impact

3. **Business Justification** (`/rebase.justify`)
   - Calculate ROI and modernization benefits  
   - Assess risks of status quo vs. modernization
   - Create investment decision framework

4. **Implementation Planning** (`/rebase.plan`)
   - Design target architecture and migration strategy
   - Create detailed roadmap with phases and milestones
   - Plan resources, timeline, and risk mitigation

## Command Usage Instructions

When a user types a `/rebase.command`, you should:

1. **Read the command template** from `.rebase/templates/commands/[command].md`
2. **Follow the execution steps** outlined in the template
3. **Use the base template** from `.rebase/templates/[command]-template.md` as structure
4. **Generate comprehensive output** based on project context and user input
5. **Present results** in the format specified by the command template

## Success Criteria

**Business Success**: Measurable improvement in business metrics (revenue, cost, time-to-market)
**Technical Success**: Improved performance, reliability, maintainability, and security
**Project Success**: On-time, on-budget delivery with stakeholder satisfaction

---

**Note**: This file is maintained by the rebase CLI. Manual additions should be placed between the markers below.

<!-- MANUAL ADDITIONS START -->
<!-- Add your custom instructions here -->
<!-- MANUAL ADDITIONS END -->
"""
    
    with open(context_file_path, 'w') as f:
        f.write(context_content)
    
    return context_file_path


@app.command()
def init(
    project_name: str = typer.Argument(
        None, help="Name for modernization project directory (use '.' or --here for current directory)"
    ),
    ai_assistant: str = typer.Option(
        "copilot", "--ai", help=f"AI assistant to use: {', '.join(AGENT_CONFIG.keys())}"
    ),
    here: bool = typer.Option(False, "--here", help="Initialize in current directory (recommended for existing codebases)"),
):
    """
    Initialize a legacy system modernization project with Rebase.

    This command sets up the necessary structure for modernizing existing codebases:
    
    For EXISTING CODEBASES (recommended):
    - Run from within your legacy project: `rebase init --here --ai claude`
    - Adds modernization structure to your existing codebase
    - Preserves all existing code and files
    
    For SEPARATE MODERNIZATION PROJECTS:
    - Create dedicated modernization project: `rebase init legacy-app-modernization --ai copilot`
    - Useful for analysis and planning before touching the legacy system
    """
    # Determine target directory and project name
    if project_name == ".":
        here = True
        project_name = None

    if here and project_name:
        console.print("[red]Error:[/red] Cannot specify both project name and --here")
        raise typer.Exit(1)

    if not here and not project_name:
        console.print("[red]Error:[/red] Must specify project name or use --here")
        raise typer.Exit(1)

    # Validate AI assistant
    if ai_assistant not in AGENT_CONFIG:
        console.print(
            f"[red]Error:[/red] Invalid AI assistant '{ai_assistant}'. "
            f"Choose from: {', '.join(AGENT_CONFIG.keys())}"
        )
        raise typer.Exit(1)

    # Resolve target path
    if here:
        project_path = Path.cwd()
        project_name = project_path.name
        existing_items = list(project_path.iterdir())
        
        # Check if this is already a rebase project
        if (project_path / ".rebase").exists():
            console.print(
                Panel(
                    "[yellow]Warning:[/yellow] This directory already has rebase initialized (.rebase/ exists).\n"
                    "Continuing will update templates and scripts to the latest version.",
                    border_style="yellow",
                )
            )
            if not typer.confirm("Do you want to continue and update rebase?"):
                console.print("[yellow]Operation cancelled[/yellow]")
                raise typer.Exit(0)
        elif existing_items:
            # Detect legacy system type
            system_type = detect_legacy_system_type(project_path)
            console.print(
                Panel(
                    f"[cyan]Legacy System Detected:[/cyan] {system_type}\n\n"
                    f"Current directory contains {len(existing_items)} items. Rebase will add modernization "
                    "structure without modifying your existing code.",
                    border_style="cyan",
                )
            )
            if not typer.confirm("Initialize rebase modernization framework here?"):
                console.print("[yellow]Operation cancelled[/yellow]")
                raise typer.Exit(0)
    else:
        project_path = Path(project_name).resolve()
        if project_path.exists():
            console.print(
                Panel(
                    f"[red]Error:[/red] Directory '{project_name}' already exists. "
                    "Use --here to initialize in an existing directory, or choose a different name.",
                    border_style="red",
                )
            )
            raise typer.Exit(1)
        
        # Create new directory for modernization project
        project_path.mkdir(parents=True)

    # Detect or set system type
    system_type = detect_legacy_system_type(project_path) if here else "New Modernization Project"

    # Display project setup info
    setup_table = Table.grid(padding=1)
    setup_table.add_column(style="cyan", justify="right")
    setup_table.add_column(style="green")
    
    setup_table.add_row("Project:", project_name)
    setup_table.add_row("Target Path:", str(project_path))
    setup_table.add_row("System Type:", system_type)
    setup_table.add_row("AI Assistant:", AGENT_CONFIG[ai_assistant]["name"])
    setup_table.add_row("Mode:", "Brownfield (existing code)" if here else "Greenfield (new project)")

    console.print(
        Panel(
            setup_table,
            title="[cyan]Rebase Modernization Setup[/cyan]",
            border_style="cyan",
        )
    )

    try:
        # Set up rebase structure
        console.print("[cyan]Setting up rebase structure...[/cyan]")
        rebase_dir = setup_rebase_structure(project_path, ai_assistant)
        
        # Copy templates and scripts
        console.print("[cyan]Copying modernization templates and scripts...[/cyan]")
        copy_rebase_templates(project_path, rebase_dir)
        
        # Create AI assistant context file
        console.print(f"[cyan]Creating {AGENT_CONFIG[ai_assistant]['name']} context file...[/cyan]")
        context_file = create_ai_context_file(project_path, ai_assistant, project_name, system_type)
        
        # Initialize Git if not already a git repo and not --here
        if not here and not (project_path / ".git").exists():
            console.print("[cyan]Initializing Git repository...[/cyan]")
            os.system(f"cd '{project_path}' && git init")
            
            # Create .gitignore
            gitignore_content = """# Rebase working files
.rebase/cache/
specs/*/temp/
memory/temp/

# OS files
.DS_Store
Thumbs.db

# IDE files
.vscode/
.idea/
*.swp
*.swo

# Temporary files
*.tmp
*.temp
"""
            with open(project_path / ".gitignore", "w") as f:
                f.write(gitignore_content)

        console.print(f"[green]✓ Rebase modernization framework initialized successfully![/green]")

        # Display next steps
        next_steps = []
        if not here:
            next_steps.append(f"1. Navigate to your project: [cyan]cd {project_path}[/cyan]")
            next_steps.append(f"2. Open your AI assistant ({AGENT_CONFIG[ai_assistant]['name']}) in this directory")
        else:
            next_steps.append(f"1. Open your AI assistant ({AGENT_CONFIG[ai_assistant]['name']}) in this directory")
        
        next_steps.extend([
            "2. Start the business-focused modernization workflow:",
            "   [cyan]/rebase.discover[/cyan] - Phase 1: Business Discovery & Context",
            "   [cyan]/rebase.assess[/cyan] - Phase 2: Current System Audit",
            "   [cyan]/rebase.justify[/cyan] - Phase 3: Risk + ROI Analysis (Go/No-Go Decision)",
            "   [cyan]/rebase.plan[/cyan] - Phase 4: Future State Design & Roadmap",
            "",
            "3. Each phase includes decision gates to ensure business value",
            "   Focus on ROI, risk management, and measurable outcomes"
        ])

        console.print(
            Panel(
                "\n".join(next_steps),
                title="[green]Next Steps - Legacy System Modernization[/green]",
                border_style="green",
            )
        )
        
        # Show context file location
        console.print(f"\n[dim]AI context file created: {context_file.relative_to(project_path)}[/dim]")

    except Exception as e:
        console.print(f"[red]Error during initialization: {e}[/red]")
        raise typer.Exit(1)

