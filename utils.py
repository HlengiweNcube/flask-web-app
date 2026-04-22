# utils.py

def get_project(projects, project_id):
    return next((p for p in projects if p["id"] == project_id), None)


def create_project(projects, title, description, image, live_url):
    new_id = max([p["id"] for p in projects], default=0) + 1

    new_project = {
        "id": new_id,
        "title": title,
        "description": description,
        "image": image,
        "live_url": live_url
    }

    projects.append(new_project)
    return new_project