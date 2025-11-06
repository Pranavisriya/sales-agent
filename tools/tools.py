import pandas as pd
from langchain.tools import tool

data=pd.read_csv('/Users/pranavisriya/Documents/untitled folder/sales_agent/data/products.csv')

@tool
def product_recommender(product_type:str, minimum_rating:float, price_range:int) -> str:
    """Recommends products based on product type, minimum rating, and price range.

    Args:
        product_type (str): The type of product to recommend.
        minimum_rating (float): The minimum rating of the product.
        price_range (int): The maximum price of the product.

    Returns:
        str: A list of recommended products in string format.
    """
    filtered = data[
        (data["product_type"].str.lower() == product_type.lower()) &
        (data["minimum_rating"] >= float(minimum_rating)) &
        (data["price"] <= float(price_range))
    ]

    if filtered.empty:
        return "[]"

    top5 = (
        filtered
        .sort_values(["minimum_rating", "price", "product_name"], ascending=[False, True, True])
        .loc[:, ["product_id", "product_name", "price", "minimum_rating"]]
        .head(5)
    )

    recommendations = top5.to_dict(orient="records")
    return str(recommendations)


@tool
def check_inventory(product_id: str) -> bool:
    """Checks the inventory for a specific product.

    Args:
        product_id (str): The id of the product to check.
        Returns:
            bool: The inventory status of the product.
    """
    product_id=product_id.upper()
    if product_id not in data['product_id'].values:
        return False
    inventory_count = data.loc[data['product_id'] == product_id, 'inventory'].values[0]
    if inventory_count > 0:
        return True
    else:
        return False
    
@tool
def check_out(product_id:str, quantity:int=1) -> str:
    """Processes the checkout for a specific product.

    Args:
        product_id (str): The id of the product to checkout.
        quantity (int): The quantity of the product to checkout.
    Returns:
        str: The checkout status of the product.
    """
    return f"Checked out product {product_id} successfully."