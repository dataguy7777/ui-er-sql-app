import streamlit as st
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle

st.set_page_config(layout="wide")
st.title("Bank Database Schema Visualization")

# Hypothetical Bank Database Schema:
# Tables:
#   CUSTOMERS (customer_id PK, name, email)
#   ACCOUNTS (account_id PK, customer_id FK->CUSTOMERS.customer_id, branch_id FK->BRANCHES.branch_id, balance)
#   BRANCHES (branch_id PK, branch_name, location)
#   TRANSACTIONS (transaction_id PK, account_id FK->ACCOUNTS.account_id, amount, tx_date)

# Represent tables as nodes
nodes = [
    {
        "id": 1,
        "type": "CUSTOMERS",
        "name": "CUSTOMERS",
        "fields": "customer_id (PK)\nname\nemail"
    },
    {
        "id": 2,
        "type": "ACCOUNTS",
        "name": "ACCOUNTS",
        "fields": "account_id (PK)\ncustomer_id (FK->CUSTOMERS)\nbranch_id (FK->BRANCHES)\nbalance"
    },
    {
        "id": 3,
        "type": "BRANCHES",
        "name": "BRANCHES",
        "fields": "branch_id (PK)\nbranch_name\nlocation"
    },
    {
        "id": 4,
        "type": "TRANSACTIONS",
        "name": "TRANSACTIONS",
        "fields": "transaction_id (PK)\naccount_id (FK->ACCOUNTS)\namount\ntx_date"
    }
]

# Edges represent foreign key relationships
# Direction: From referencing table to referenced table
edges = [
    {"id": 5, "type": "RELATION", "source": 2, "target": 1, "label": "ACCOUNTS->CUSTOMERS"},
    {"id": 6, "type": "RELATION", "source": 2, "target": 3, "label": "ACCOUNTS->BRANCHES"},
    {"id": 7, "type": "RELATION", "source": 4, "target": 2, "label": "TRANSACTIONS->ACCOUNTS"}
]

elements = {
    "nodes": nodes,
    "edges": edges
}

# Define node styles for each table type
node_styles = [
    NodeStyle(node_type="CUSTOMERS", color="#FF7F3E", caption="fields", shape="box"),
    NodeStyle(node_type="ACCOUNTS", color="#2A629A", caption="fields", shape="box"),
    NodeStyle(node_type="BRANCHES", color="#78C850", caption="fields", shape="box"),
    NodeStyle(node_type="TRANSACTIONS", color="#F0C674", caption="fields", shape="box")
]

# Define edge style for relationships
edge_styles = [
    EdgeStyle(edge_type="RELATION", caption='label', directed=True)
]

st.subheader("Database Schema Graph")
st.write("Tables are represented as nodes with their fields. Edges represent foreign key relationships.")

st_link_analysis(
    elements,
    layout="cose",          # 'cose' is a common layout. Adjust if desired.
    node_styles=node_styles,
    edge_styles=edge_styles,
    height=600,
    width=1000
)

st.markdown("""
**Schema Details:**

**CUSTOMERS**  
- `customer_id (PK)`: Unique identifier for each customer  
- `name`: Customer full name  
- `email`: Contact email address

**ACCOUNTS**  
- `account_id (PK)`: Unique identifier for each account  
- `customer_id (FK->CUSTOMERS)`: Links an account to its owner  
- `branch_id (FK->BRANCHES)`: Links an account to the branch where it was opened  
- `balance`: Current balance of the account

**BRANCHES**  
- `branch_id (PK)`: Unique identifier for each branch  
- `branch_name`: Name of the branch  
- `location`: Geographical location of the branch

**TRANSACTIONS**  
- `transaction_id (PK)`: Unique identifier for each transaction  
- `account_id (FK->ACCOUNTS)`: The account affected by the transaction  
- `amount`: Amount of money involved in the transaction  
- `tx_date`: Date/time of the transaction
""")
