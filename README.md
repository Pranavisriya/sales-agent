# Sales Agent

An agent that recommends products within your budget and preferences, checks real-time stock status, and helps you proceed to checkout—all in one flow.

## Prerequisites

- Python 3.12 or higher
- uv
- API keys for:
  - Groq


## Installation

1. Clone the repository:
```bash
git clone https://github.com/Pranavisriya/sales-agent.git
cd sales-agent
```

2. Install `uv` in the environment if it is not present
```bash
pip install uv
```

3. Create a virtual python environment in this repo
```bash
uv init
uv venv -p 3.12
```

Any other method can also be used to create python environment.

4. Activate python environment
```bash
source .venv/bin/activate
```


5. Install dependencies using uv:
```bash
uv add -r requirements.txt
```

6. Create a `.env` file in the project root with your API keys:
```
GROQ_API_KEY=your_groqapi_key
```

## Usage

Run the fastapi and frontend:
```bash
uvicorn backend:app --reload --port 8000
streamlit run frontend.py
```


## Features

- Smart recommendations: Filter by your chosen criteria (e.g., minimum rating, price range).
- Inventory checks: Verify whether items are in stock before you decide.
- Guided checkout: Seamlessly proceed to purchase the products you’re interested in.


## License

This project is licensed under the terms included in the LICENSE file.

## Author

Pranavi Sriya (pranavisriyavajha9@gmail.com)


