import argparse
import sys
import json
import os

CONFIG_FILE = ".gitgroup.json"

class GitGroup:
    """A multiplex Git management tool (gitgroup)"""

    def __init__(self):
        if not os.path.exists(CONFIG_FILE):
            self.init()

    def init(self, args=None):
        """Initialize the .gitgroup.json file"""
        if not os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "w") as f:
                json.dump({"repositories": []}, f, indent=4)
            print("Initialized .gitgroup.json")
        else:
            print(".gitgroup.json already exists")

    def run(self, args):
        """Run a Git command on all repositories"""
        with open(CONFIG_FILE, "r") as f:
            data = json.load(f)

        git_command = " ".join(args.git_command)  # Convert list to command string

        if data["repositories"]:
            print("Executing Git command in repositories:")
            for repo in data["repositories"]:
                os.system(f"git --git-dir={repo}/.git --work-tree={repo} {git_command}")
        else:
            print("No repositories found.")

    def add(self, args):
        """Add repositories to the group"""
        if not args.repositories:
            print("Error: Please specify at least one repository to add.")
            return

        with open(CONFIG_FILE, "r") as f:
            data = json.load(f)

        data["repositories"].extend(args.repositories)
        data["repositories"] = list(set(data["repositories"]))  # Remove duplicates

        with open(CONFIG_FILE, "w") as f:
            json.dump(data, f, indent=4)

        print(f"Added: {', '.join(args.repositories)}")

    def rm(self, args):
        """Remove repositories from the group"""
        if not args.repositories:
            print("Error: Please specify at least one repository to remove.")
            return

        with open(CONFIG_FILE, "r") as f:
            data = json.load(f)

        removed = [repo for repo in args.repositories if repo in data["repositories"]]
        data["repositories"] = [repo for repo in data["repositories"] if repo not in args.repositories]

        with open(CONFIG_FILE, "w") as f:
            json.dump(data, f, indent=4)

        if removed:
            print(f"Removed: {', '.join(removed)}")
        else:
            print("Nothing to remove.")

    def ls(self, args=None):
        """List all repositories"""
        with open(CONFIG_FILE, "r") as f:
            data = json.load(f)

        if data["repositories"]:
            print("Repositories:")
            for repo in data["repositories"]:
                print(f"- {repo}")
        else:
            print("No repositories found.")

def main():
    parser = argparse.ArgumentParser(description="A multiplex Git management tool (gitgroup)")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add Command
    parser_add = subparsers.add_parser("add", help="Add repositories to the group")
    parser_add.add_argument("repositories", nargs="+", help="Repository paths to add")
    parser_add.set_defaults(func=GitGroup().add)

    # Remove Command
    parser_rm = subparsers.add_parser("rm", help="Remove repositories from the group")
    parser_rm.add_argument("repositories", nargs="+", help="Repository paths to remove")
    parser_rm.set_defaults(func=GitGroup().rm)

    # List Command
    parser_ls = subparsers.add_parser("ls", help="List all repositories in the group")
    parser_ls.set_defaults(func=GitGroup().ls)

    # Init Command
    parser_init = subparsers.add_parser("init", help="Initialize the .gitgroup.json file")
    parser_init.set_defaults(func=GitGroup().init)

    # Run Command
    parser_run = subparsers.add_parser("run", help="Execute Git commands in all repositories")
    parser_run.add_argument("git_command", nargs=argparse.REMAINDER, help="Git command to execute")
    parser_run.set_defaults(func=GitGroup().run)

    # Parse Arguments
    args = parser.parse_args()
    args.func(args)  # Call the appropriate function

if __name__ == "__main__":
    main()
