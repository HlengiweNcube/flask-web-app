import json
from pathlib import Path

PROJECTS_FILE = Path(__file__).resolve().parent / "projects.json"


def load_projects():
    if not PROJECTS_FILE.exists():
        return []

    with open(PROJECTS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_projects(projects):
    with open(PROJECTS_FILE, "w", encoding="utf-8") as file:
        json.dump(projects, file, indent=4)


def get_next_project_id(projects):
    if not projects:
        return 0
    return max(project["id"] for project in projects) + 1