#!/usr/bin/env bash

# Common functions for rebase modernization scripts
# Based on spec-kit patterns, adapted for legacy system modernization

set -e

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Function to get feature paths and variables
get_feature_paths() {
    local current_branch=""
    local has_git="false"
    local feature_dir=""
    
    # Check if we're in a git repository
    if git rev-parse --git-dir >/dev/null 2>&1; then
        has_git="true"
        current_branch=$(git branch --show-current 2>/dev/null || echo "main")
        
        # Extract feature name from branch (pattern: ###-feature-name)
        if [[ "$current_branch" =~ ^[0-9]+-(.+)$ ]]; then
            feature_dir="$REPO_ROOT/specs/$current_branch"
        else
            # If not on a feature branch, check for REBASE_FEATURE env var
            if [[ -n "$REBASE_FEATURE" ]]; then
                feature_dir="$REPO_ROOT/specs/$REBASE_FEATURE"
                current_branch="$REBASE_FEATURE"
            else
                # Default to main development
                feature_dir="$REPO_ROOT/specs/main-modernization"
                current_branch="main-modernization"
            fi
        fi
    else
        has_git="false"
        # Not a git repo, use REBASE_FEATURE env var or default
        if [[ -n "$REBASE_FEATURE" ]]; then
            feature_dir="$REPO_ROOT/specs/$REBASE_FEATURE"
            current_branch="$REBASE_FEATURE"
        else
            feature_dir="$REPO_ROOT/specs/main-modernization"
            current_branch="main-modernization"
        fi
    fi
    
    # Output variables that can be eval'd
    cat <<EOF
REPO_ROOT="$REPO_ROOT"
CURRENT_BRANCH="$current_branch"
HAS_GIT="$has_git"
FEATURE_DIR="$feature_dir"
DISCOVER_SPEC="$feature_dir/discover.md"
ASSESS_SPEC="$feature_dir/assess.md"
JUSTIFY_SPEC="$feature_dir/justify.md"
PLAN_SPEC="$feature_dir/plan.md"
CONSTITUTION="$feature_dir/constitution.md"
TASKS="$feature_dir/tasks.md"
RESEARCH="$feature_dir/research.md"
QUICKSTART="$feature_dir/quickstart.md"
CONTRACTS_DIR="$feature_dir/contracts"
MEMORY_CONSTITUTION="$REPO_ROOT/memory/constitution.md"
EOF
}

# Function to check if we're on a proper feature branch
check_feature_branch() {
    local branch="$1"
    local has_git="$2"
    
    if [[ "$has_git" == "true" ]]; then
        # In a git repo, check for proper branch naming
        if [[ ! "$branch" =~ ^[0-9]+-(.+)$ ]] && [[ "$branch" != "main-modernization" ]]; then
            echo "Warning: Not on a feature branch (pattern: ###-feature-name)"
            echo "Current branch: $branch"
            echo "Consider creating a feature branch or setting REBASE_FEATURE environment variable"
            return 1
        fi
    else
        # Not in git repo, just check for REBASE_FEATURE
        if [[ -z "$REBASE_FEATURE" ]] && [[ "$branch" == "main-modernization" ]]; then
            echo "Info: Using default modernization workspace: main-modernization"
            echo "Set REBASE_FEATURE environment variable to use a specific feature name"
        fi
    fi
    return 0
}

# Function to check if a file exists and report
check_file_exists() {
    local filepath="$1"
    local description="$2"
    
    if [[ -f "$filepath" ]]; then
        echo "  ✓ $description"
        return 0
    else
        echo "  ✗ $description"
        return 1
    fi
}

# Function to check if a directory has files
check_dir_has_files() {
    local dirpath="$1"
    local description="$2"
    
    if [[ -d "$dirpath" ]] && [[ -n "$(ls -A "$dirpath" 2>/dev/null)" ]]; then
        echo "  ✓ $description"
        return 0
    else
        echo "  ✗ $description"
        return 1
    fi
}

# Function to create directory if it doesn't exist
ensure_directory() {
    local dirpath="$1"
    if [[ ! -d "$dirpath" ]]; then
        mkdir -p "$dirpath"
        echo "Created directory: $dirpath"
    fi
}

#!/usr/bin/env bash

# Common functions for rebase modernization scripts
# Based on spec-kit patterns, adapted for legacy system modernization

set -e

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Define all available phases (compatible with bash 3.2+)
get_phase_description() {
    case "$1" in
        "discover") echo "Business Discovery & Context" ;;
        "assess") echo "Current System Audit" ;;
        "justify") echo "Risk + ROI Analysis (Go/No-Go Decision)" ;;
        "plan") echo "Future State Design & Roadmap" ;;
        *) echo "Unknown phase" ;;
    esac
}

# Define phase order for sequential workflows
get_phase_order() {
    echo "discover assess justify plan"
}

# Function to list all available phases
list_phases() {
    echo "Available modernization phases:"
    local phase_num=1
    local phases=($(get_phase_order))
    
    for phase in "${phases[@]}"; do
        local description=$(get_phase_description "$phase")
        local status=""
        
        # Check if phase file exists
        eval $(get_feature_paths)
        local phase_file="${FEATURE_DIR}/${phase}.md"
        if [[ -f "$phase_file" ]]; then
            status=" ✓"
        else
            status=" ○"
        fi
        
        echo "  ${phase_num}. ${status} /rebase.${phase} - ${description}"
        ((phase_num++))
    done
    echo ""
    echo "Legend: ✓ = completed, ○ = not started"
}

# Function to validate prerequisites for rebase commands
validate_prerequisites() {
    # Parse named phase arguments
    local required_phases=()
    
    # Handle both old style (positional booleans) and new style (named phases)
    if [[ "$1" =~ ^(true|false)$ ]]; then
        # Old style: convert positional booleans to phase names
        [[ "$1" == "true" ]] && required_phases+=("discover")
        [[ "$2" == "true" ]] && required_phases+=("assess")
        [[ "$3" == "true" ]] && required_phases+=("justify")
        [[ "$4" == "true" ]] && required_phases+=("plan")
    else
        # New style: named phases
        required_phases=("$@")
    fi
    
    # Load feature paths
    eval $(get_feature_paths)
    
    echo "Checking prerequisites..."
    echo "Feature directory: $FEATURE_DIR"
    
    local all_good=true
    local missing_phases=()
    
    # Check each required phase
    for phase in "${required_phases[@]}"; do
        # Validate phase exists
        local description=$(get_phase_description "$phase")
        if [[ "$description" == "Unknown phase" ]]; then
            echo "  ✗ Unknown phase: $phase"
            all_good=false
            continue
        fi
        
        local phase_file="${FEATURE_DIR}/${phase}.md"
        
        if ! check_file_exists "$phase_file" "Phase: $phase ($description)"; then
            all_good=false
            missing_phases+=("$phase")
        fi
    done
    
    # Optional files (don't fail if missing)
    check_file_exists "$RESEARCH" "Research documentation (research.md)" || true
    check_file_exists "$QUICKSTART" "Quickstart guide (quickstart.md)" || true
    check_dir_has_files "$CONTRACTS_DIR" "API contracts (contracts/)" || true
    check_file_exists "$CONSTITUTION" "Modernization constitution (constitution.md)" || true
    check_file_exists "$MEMORY_CONSTITUTION" "Global constitution (memory/constitution.md)" || true
    
    if [[ "$all_good" != "true" ]]; then
        echo ""
        echo "Missing required prerequisites. Please run the appropriate commands:"
        for phase in "${missing_phases[@]}"; do
            local description=$(get_phase_description "$phase")
            echo "  /rebase.${phase} - ${description}"
        done
        return 1
    fi
    
    return 0
}

# Function to output JSON for consumption by commands
output_json() {
    eval $(get_feature_paths)
    
    local available_docs=""
    local docs=()
    
    # Check all known phases
    local phases=($(get_phase_order))
    for phase in "${phases[@]}"; do
        local phase_file="${FEATURE_DIR}/${phase}.md"
        [[ -f "$phase_file" ]] && docs+=("${phase}.md")
    done
    
    # Check other standard files
    [[ -f "$CONSTITUTION" ]] && docs+=("constitution.md")
    [[ -f "$TASKS" ]] && docs+=("tasks.md")
    [[ -f "$RESEARCH" ]] && docs+=("research.md")
    [[ -f "$QUICKSTART" ]] && docs+=("quickstart.md")
    [[ -d "$CONTRACTS_DIR" ]] && [[ -n "$(ls -A "$CONTRACTS_DIR" 2>/dev/null)" ]] && docs+=("contracts/")
    [[ -f "$MEMORY_CONSTITUTION" ]] && docs+=("memory/constitution.md")
    
    # Join array elements with commas
    local IFS=','
    available_docs="${docs[*]}"
    
    cat <<EOF
{
    "REPO_ROOT": "$REPO_ROOT",
    "CURRENT_BRANCH": "$CURRENT_BRANCH", 
    "HAS_GIT": "$HAS_GIT",
    "FEATURE_DIR": "$FEATURE_DIR",
    "DISCOVER_SPEC": "$DISCOVER_SPEC",
    "ASSESS_SPEC": "$ASSESS_SPEC",
    "JUSTIFY_SPEC": "$JUSTIFY_SPEC",
    "PLAN_SPEC": "$PLAN_SPEC",
    "CONSTITUTION": "$CONSTITUTION",
    "TASKS": "$TASKS",
    "RESEARCH": "$RESEARCH",
    "QUICKSTART": "$QUICKSTART",
    "CONTRACTS_DIR": "$CONTRACTS_DIR",
    "MEMORY_CONSTITUTION": "$MEMORY_CONSTITUTION",
    "AVAILABLE_DOCS": ["$available_docs"]
}
EOF
}

# Main function for standalone execution
main() {
    case "${1:-}" in
        --json)
            output_json
            ;;
        --phases)
            list_phases
            ;;
        --validate)
            shift  # Remove --validate argument
            validate_prerequisites "$@"
            ;;
        --help|-h)
            echo "Usage: $0 [--json|--phases|--validate <phases...>|--help]"
            echo "  --json                    Output environment variables as JSON"
            echo "  --phases                  List all available modernization phases"
            echo "  --validate <phases...>    Validate prerequisites for specific phases"
            echo "                           Examples:"
            echo "                             --validate discover assess"
            echo "                             --validate discover assess justify plan"
            echo "                             --validate true true false false  (legacy format)"
            echo "  --help                    Show this help message"
            ;;
        *)
            eval $(get_feature_paths)
            echo "Rebase modernization environment:"
            echo "  Repository: $REPO_ROOT"
            echo "  Current branch: $CURRENT_BRANCH"
            echo "  Git repository: $HAS_GIT"
            echo "  Feature directory: $FEATURE_DIR"
            echo ""
            echo "Use --phases to see available modernization phases"
            ;;
    esac
}

# Run main if script is executed directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi