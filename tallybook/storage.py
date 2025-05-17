from pathlib import Path
import json
import os

data_file = Path.home() / "Documents/projects/tallybook/tallybook/tally_data.json"
#data_file = Path.home() / "Documents" / "projects" / "tallybook" / "tallybook" / "tally_data.json"


def load_data():
    if data_file.exists():
        with open(data_file) as f:
            return json.load(f)
    else:
        return {}

def save_data(data):
    with open(data_file, "w") as f:
        json.dump(data, f, indent=2)