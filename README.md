# Beyond the Screen
**Accessible, guided digital-task support — student prototype**

Beyond the Screen is a small demonstration web app exploring how first-time smartphone users and people with limited digital literacy could receive clearer, step-by-step guidance for common digital tasks.

> **Prototype notice:** This is an educational concept demo. It does not connect to government services, submit forms, store user data, or provide official advice. The sample content is fictional and should be user-tested before real-world deployment.

## Features
- Simple, responsive interface with clear task cards.
- Step-by-step guidance for sample digital tasks.
- Sample task data stored locally in JSON.
- JSON endpoint at `/api/tasks`.
- Health endpoint at `/health`.
- Basic automated tests.

## Requirements
- Python 3.10+
- pip

## Setup
```bash
# 1. Create and enter a virtual environment (recommended)
python -m venv .venv

# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the app
python app.py
```
Open `http://127.0.0.1:5000` in your browser.

## Environment variables
No environment variables are required for this local demo. `.env.example` is included as a deployment reminder. Do not commit passwords, API keys, or personal data.

## Run tests
```bash
pip install pytest
pytest
```

## Project structure
```text
beyond-the-screen/
├── app.py
├── requirements.txt
├── .env.example
├── README.md
├── LICENSE
├── docs/
│   └── technical-design.md
├── sample_data/
│   └── tasks.json
├── static/
│   └── style.css
├── templates/
│   └── index.html
└── tests/
    └── test_app.py
```

## Architecture
See [`docs/technical-design.md`](docs/technical-design.md) for the architecture diagram, routes, data flow, limitations, and future work.

## Privacy and accessibility principles
- Sample data is fictional; no personal information is collected.
- Keep instructions short and plain-language.
- Provide keyboard-friendly controls and readable contrast.
- Test with intended users and local-language speakers before making impact claims.

## Roadmap
1. Conduct consent-based interviews with intended users.
2. Co-design and test instructions in relevant Indian languages.
3. Add text-size controls and optional audio guidance.
4. Evaluate task completion and user confidence with clear consent and privacy safeguards.

## License
Released under the MIT License. See [`LICENSE`](LICENSE).
