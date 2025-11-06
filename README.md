# Sales Agent

An agent which provides recommendations based on your choice and in price range, checks the product in the stock and checkout the products that you are intrested in

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

2. Create a virtual python environment in this repo
```bash
conda create -p venv python=3.12 -y
```

Any other method can also be used to create python environment.

3. Activate python environment
```bash
conda activate ./venv
```

4. Install `uv` in the environment if it is not present
```bash
pip install uv
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

- Recommend products based on your criteria such as minimum rating and minimum price
- Check whether the products are in stock or not
- Checkout the product if you are intrested to buy


## License

This project is licensed under the terms included in the LICENSE file.

## Author

Pranavi Sriya (pranavisriyavajha9@gmail.com)
