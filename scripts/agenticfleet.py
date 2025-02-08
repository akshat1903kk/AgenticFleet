#!/usr/bin/env python3
"""Entry point script for AgenticFleet."""

import os
import subprocess
import sys

# Add src directory to path
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.insert(0, src_dir)

def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: agenticfleet <command>")
        print("Commands:")
        print("  start         Start with OAuth enabled")
        print("  start no-oauth  Start without OAuth")
        sys.exit(1)

    command = sys.argv[1]

    if command == "start":
        # Check for no-oauth flag
        no_oauth = len(sys.argv) > 2 and sys.argv[2] == "no-oauth"
        # Set environment variables for OAuth
        if no_oauth:
            os.environ["OAUTH_CLIENT_ID"] = ""
            os.environ["OAUTH_CLIENT_SECRET"] = ""
            os.environ["OAUTH_REDIRECT_URI"] = ""
            os.environ["OAUTH_SCOPES"] = ""
            os.environ["OAUTH_AUTHORIZE_URL"] = ""
            os.environ["OAUTH_TOKEN_URL"] = ""
            os.environ["OAUTH_USER_INFO_URL"] = ""
            print("Starting AgenticFleet without OAuth...")
        else:
            print("Starting AgenticFleet with OAuth...")

        # Get the path to app.py
        app_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src", "agentic_fleet"))
        app_path = os.path.join(app_dir, "app.py")

        # Build and run chainlit command
        cmd = [
            "chainlit",
            "run",
            app_path,
            "--port",
            "8001"
        ]

        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running chainlit: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
