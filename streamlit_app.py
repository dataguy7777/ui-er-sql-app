import streamlit as st
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle

# Set the page configuration to use a wide layout
st.set_page_config(layout="wide")
st.title("Bank Database Schema Visualization")

# Define the bank database schema with tables and their relationships
# Tables:
#   CUSTOMERS (customer_id PK, name, email)
#   ACCOUNTS (account_id PK, customer_id FK->CUSTOMERS.customer_id, branch_id FK->BRANCHES.branch_id, balance)
#   BRANCHES (branch_id PK, branch_name, location)
#   TRANSACTIONS (transaction_id PK, account_id FK->ACCOUNTS.account_id, amount, tx_date)

# Define nodes representing each table
nodes = [
    {
        "data": {
            "id": 1,
            "label": "CUSTOMERS",
            "fields": "customer_id (PK)\nname\nemail"
        }
    },
    {
        "data": {
            "id": 2,
            "label": "ACCOUNTS",
            "fields": "account_id (PK)\ncustomer_id (FK->CUSTOMERS)\nbranch_id (FK->BRANCHES)\nbalance"
        }
    },
    {
        "data": {
            "id": 3,
            "label": "BRANCHES",
            "fields": "branch_id (PK)\nbranch_name\nlocation"
        }
    },
    {
        "data": {
            "id": 4,
            "label": "TRANSACTIONS",
            "fields": "transaction_id (PK)\naccount_id (FK->ACCOUNTS)\namount\ntx_date"
        }
    }
]

# Define edges representing foreign key relationships
edges = [
    {"data": {"id": 5, "label": "RELATION", "source": 2, "target": 1}},
    {"data": {"id": 6, "label": "RELATION", "source": 2, "target": 3}},
    {"data": {"id": 7, "label": "RELATION", "source": 4, "target": 2}}
]

# Combine nodes and edges into elements
elements = {
    "nodes": nodes,
    "edges": edges
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
# EdgeStyle(type, caption_attribute, directed)
edge_styles = [
    EdgeStyle("RELATION", "label", True)
]

# Render the link analysis visualization
st.subheader("Database Schema Graph")
st.write("Tables are represented as nodes with their fields. Edges represent foreign key relationships.")

# Display the link analysis component
st_link_analysis(
    elements=elements,
    layout="cose",          # 'cose' is a common layout; adjust if desired
    node_styles=node_styles,
    edge_styles=edge_styles,
    height=600,
    width=1000
)

# Provide detailed schema information below the graph
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
""")
