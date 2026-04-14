# Package Sorter

[![CI](https://github.com/adambouras/package-sorter/actions/workflows/ci.yml/badge.svg)](https://github.com/adambouras/package-sorter/actions/workflows/ci.yml)

Robotic arm dispatch function for Smarter Technology's automation factory.  
Sorts packages into **STANDARD**, **SPECIAL**, or **REJECTED** stacks based on volume, dimensions, and mass.

## Rules

| Condition | Criteria |
|-----------|----------|
| **Bulky** | Volume ≥ 1,000,000 cm³ **or** any single dimension ≥ 150 cm |
| **Heavy** | Mass ≥ 20 kg |

| Stack | When |
|-------|------|
| STANDARD | Neither bulky nor heavy |
| SPECIAL | Bulky **or** heavy (but not both) |
| REJECTED | Bulky **and** heavy |

## Run in GitHub Codespaces (easiest)

1. Click the green **`<> Code`** button on the repo → **Codespaces** tab.
2. Click **"Create codespace on main"**.
3. Dependencies install automatically and the server starts.
4. A browser tab opens with the app — ready to use.

> If the app doesn't auto-start, open the Codespaces terminal and run `python run.py`, then click the **Ports** tab → globe icon on port **5000**.

## Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/adambouras/package-sorter.git
cd package-sorter

# 2. Create & activate a virtual environment
python3 -m venv .env
source .env/bin/activate      # macOS / Linux
# .env\Scripts\activate       # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python run.py
```

Then open **http://127.0.0.1:5000** in your browser.

## Run Tests

```bash
python -m pytest tests/ -v
```

## Project Structure

```
package-sorter/
├── .devcontainer/          # GitHub Codespaces config
├── .github/workflows/      # CI pipeline
├── package_sorter/          # Application package
│   ├── __init__.py          #   App factory (create_app)
│   ├── sort.py              #   Core sorting logic
│   └── routes.py            #   API & view routes
├── static/images/           # Static assets
├── templates/               # HTML templates
├── tests/                   # Test suite
│   ├── test_sort.py         #   Unit tests
│   └── test_api.py          #   Integration tests
├── run.py                   # Entry point
├── requirements.txt
└── README.md
```

## Usage (Python)

```python
from package_sorter.sort import sort

sort(10, 10, 10, 5)      # "STANDARD"
sort(200, 200, 200, 10)  # "SPECIAL"
sort(150, 150, 150, 25)  # "REJECTED"
```

## Frontend

The web UI lets you:

1. Enter package dimensions and mass, then click **Dispatch Package**.
2. See which stack the package is routed to (STANDARD / SPECIAL / REJECTED).
3. Adjust **Benchmark Thresholds** to customise the bulky/heavy rules.
4. **Clear Stacks** to reset.

## CI

GitHub Actions runs the test suite across Python 3.9–3.12 on every push and PR.
