# cicd-labs 🚀

A lightweight, automated CI/CD pipeline built for local development on Linux.

## Workflow
- Watcher: Monitors src/ for any file changes.
- CI: Runs flake8 to validate code quality.
- CD: Automatically deploys clean code to production/.
- Orchestrator: Kills old processes and restarts the app using subprocess.Popen.

## Structure
- scripts/cicd.py: The main automation engine.
- scripts/run.sh: Bash wrapper to execute production code.
- src/: Development environment.
- production/: Live environment.

## Usage
python3 scripts/cicd.py

## Features
- Asynchronous: Non-blocking process management.
- Logging: Real-time tracking in pipeline.log.
- Idempotency: Only syncs files if content differs.
