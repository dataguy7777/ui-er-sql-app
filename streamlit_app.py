import streamlit as st
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle

# Set the page configuration to use a wide layout
st.set_page_config(layout="wide")
st.title("Bank Database Schema Visualization")

# Define nodes representing each table
elements = {
    "nodes": [
        {
            "data": {
                "id": "CUSTOMERS",
                "label": "CUSTOMERS",
                "fields": "customer_id (PK)\nname\nemail"
            }
        },
        {
            "data": {
                "id": "ACCOUNTS",
                "label": "ACCOUNTS",
                "fields": "account_id (PK)\ncustomer_id (FK->CUSTOMERS)\nbranch_id (FK->BRANCHES)\nbalance"
            }
        },
        {
            "data": {
                "id": "BRANCHES",
                "label": "BRANCHES",
                "fields": "branch_id (PK)\nbranch_name\nlocation"
            }
        },
        {
            "data": {
                "id": "TRANSACTIONS",
                "label": "TRANSACTIONS",
                "fields": "transaction_id (PK)\naccount_id (FK->ACCOUNTS)\namount\ntx_date"
            }
        }
    ],
    "edges": [
        {"data": {"id": "e1", "label": "ACCOUNTS->CUSTOMERS", "source": "ACCOUNTS", "target": "CUSTOMERS"}},
        {"data": {"id": "e2", "label": "ACCOUNTS->BRANCHES", "source": "ACCOUNTS", "target": "BRANCHES"}},
        {"data": {"id": "e3", "label": "TRANSACTIONS->ACCOUNTS", "source": "TRANSACTIONS", "target": "ACCOUNTS"}}
    ]
}

# Define node styles using positional arguments
# NodeStyle(type, color, caption_attribute, shape)
node_styles = [
    NodeStyle("CUSTOMERS", "#FF7F3E", "fields", "box"),
    NodeStyle("ACCOUNTS", "#2A629A", "fields", "box"),
    NodeStyle("BRANCHES", "#78C850", "fields", "box"),
    NodeStyle("TRANSACTIONS", "#F0C674", "fields", "box")
]

# Define edge styles using positional arguments
# EdgeStyle(type, color, caption_attribute, directed)
edge_styles = [
    EdgeStyle("RELATION", "#808080", "label", True),
    EdgeStyle("RELATION", "#808080", "label", True),
    EdgeStyle("RELATION", "#808080", "label", True)
]

# Define layout settings
layout = {"name": "cose", "animate": "end", "nodeDimensionsIncludeLabels": False}

st.subheader("Bank Database Schema Graph")
st.write("Tables are represented as nodes with their fields. Edges represent foreign key relationships.")

# Attempt to render the link analysis visualization
try:
    st_link_analysis(
        elements=elements,
        layout=layout,
        node_styles=node_styles,
        edge_styles=edge_styles,
        key="bank_schema"
    )
except TypeError as te:
    st.error(f"TypeError encountered: {te}")
except AttributeError as ae:
    st.error(f"AttributeError encountered: {ae}")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")

st.markdown("""
**Schema Details:**

### **CUSTOMERS**
- `customer_id (PK)`: Unique identifier for each customer  
- `name`: Customer's full name  
- `email`: Contact email address  

### **ACCOUNTS**
- `account_id (PK)`: Unique identifier for each account  
- `customer_id (FK->CUSTOMERS)`: Links an account to its owner  
- `branch_id (FK->BRANCHES)`: Links an account to the branch where it was opened  
- `balance`: Current balance of the account  

### **BRANCHES**
- `branch_id (PK)`: Unique identifier for each branch  
- `branch_name`: Name of the branch  
- `location`: Geographical location of the branch  

### **TRANSACTIONS**
- `transaction_id (PK)`: Unique identifier for each transaction  
- `account_id (FK->ACCOUNTS)`: The account affected by the transaction  
- `amount`: Amount of money involved in the transaction  
- `tx_date`: Date/time of the transaction  

**Relationships:**
- **ACCOUNTS → CUSTOMERS**: Each account is linked to a customer.
- **ACCOUNTS → BRANCHES**: Each account is associated with a branch.
- **TRANSACTIONS → ACCOUNTS**: Each transaction is tied to an account.

**Usage:**
- **Interactive Graph**: Click and drag nodes to explore relationships.
- **Tooltips**: Hover over nodes and edges to see detailed information.
""")
