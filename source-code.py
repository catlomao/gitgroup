import argparse
import sys
import json
import os

CONFIG_FILE = ".gitgroup.json"

class GitGroup:
    # >> A multiplex Git management tool (gitgroup) << made by catlomao
    # please dont steal, give credit!!!

    def __init__(self):
        if not os.path.exists(CONFIG_FILE):
            self.init()

    def init(self, *args):
        if not os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "w") as f:
                json.dump({"repositories": []}, f, indent=4)
            print("Initialized .gitgroup.json")
        else:
            print(".gitgroup.json already exists")

    def run(self, *args):
        with open(CONFIG_FILE, "r") as f:
            data = json.load(f)
        git = " ".join(args)
        if data["repositories"]:
            print("Repositories:")
            for repo in data["repositories"]:
                os.system(f"git --git-dir={repo}/.git --work-tree={repo} {git}")
        else:
            print("No repositories found.")

    def add(self, *args):
        if not args:
            print("Error: Please give a repository name to add.")
            return
        
        with open(CONFIG_FILE, "r") as f:
            data = json.load(f)

        data["repositories"].extend(args)
        data["repositories"] = list(set(data["repositories"]))  # Remove duplicates

        with open(CONFIG_FILE, "w") as f:
            json.dump(data, f, indent=4)

        print(f"Added: {', '.join(args)}")

    def rm(self, *args):
        if not args:
            print("Error: Please give a repository name to remove.")
            return

        with open(CONFIG_FILE, "r") as f:
            data = json.load(f)

        removed = [repo for repo in args if repo in data["repositories"]]
        data["repositories"] = [repo for repo in data["repositories"] if repo not in args]

        with open(CONFIG_FILE, "w") as f:
            json.dump(data, f, indent=4)

        if removed:
            print(f"Removed: {', '.join(removed)}")
        else:
            print("Nothing to remove....?")

    def ls(self, *args):
        with open(CONFIG_FILE, "r") as f:
            data = json.load(f)

        if data["repositories"]:
            print("Repositories:")
            for repo in data["repositories"]:
                print(f"- {repo}")
        else:
            print("No repositories found.")

    def execute(self, command, *args):
        if hasattr(self, command):
            getattr(self, command)(*args)
        else:
            print(f"Error: Unknown command '{command}'")
            sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="A multiplex Git management tool (gitgroup)")
    parser.add_argument("add", type=str, help="adds repo to group")
    parser.add_argument("rm", type=str, help="removes a repo from group")
    parser.add_argument("ls", type=str, help="list all repos in group")
    parser.add_argument("init", type=str, help="initializes the current folder (.gitgroup.json)")
    parser.add_argument("run", type=str, help="executes git commands for each repo EXAMPLE <gitgroup run <git command like status or push whatever> >")

    args = parser.parse_args()

    gitgroup = GitGroup()
    gitgroup.execute(args.command, *args.arguments)

if __name__ == "__main__":
    main()
