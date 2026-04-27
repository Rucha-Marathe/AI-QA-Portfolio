# AI QA Portfolio: Testing & Monitoring Journey

This repository serves as a professional portfolio documenting the implementation of AI-powered quality assurance, including red teaming, RAG validation, and production observability.

## Why These Tools?
To be an effective AI QA professional, I have standardized my environment around industry-leading tools:

- **VS Code**: My integrated "Command Center" for code, terminals, and GitHub management.
- **Python**: The standard language for AI automation, API interaction, and data analysis.
- **Jupyter**: My "Scratchpad" for prototyping tests and visualizing LLM outputs instantly.
- **Git & GitHub**: My "Safety Net" for version control, collaboration, and showcasing my work to recruiters.
- **GitLens**: My "Time Machine" for debugging code changes and tracking authorship.

## Project Infrastructure & Setup
This project follows professional CI/CD and QA best practices to ensure reproducibility.

### 1. Development Environment
- **IDE**: VS Code (Python, GitLens, Jupyter extensions)
- **Git Config**: Configured `user.name` and `user.email` for identity tracking.

### 2. Isolated Workspace
I utilized Python’s `venv` to isolate dependencies, ensuring a clean environment.

**Command Used:**
```bash
python -m venv aiqa-env
```

### 3. Troubleshooting & Resolution
While setting up the virtual environment, I encountered a security restriction preventing script execution.

**Error**: `PSSecurityException` (Execution policy disabled).
**Screenshot of error:**
![Security Exception Error](images/image.jpg)

**Resolution Command:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

### 4. Core Dependencies
**Tools installed:**
```bash
pip install jupyter pytest
```

## Testing Milestones
- **Lesson 1**: Successfully automated safety logic validation using `pytest`.
- **Result**: 2/2 tests passed in the `test_ai_logic.py` suite.

---
*Maintained by: Rucha Marathe*