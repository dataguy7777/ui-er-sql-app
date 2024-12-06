import streamlit as st
import networkx as nx
from pyvis.network import Network
from streamlit.components.v1 import components
import tempfile

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
        "id": "CUSTOMERS",
        "label": "CUSTOMERS",
        "title": "customer_id (PK)\nname\email",
        "group": "CUSTOMERS"
    },
    {
        "id": "ACCOUNTS",
        "label": "ACCOUNTS",
        "title": "account_id (PK)\ncustomer_id (FK->CUSTOMERS)\nbranch_id (FK->BRANCHES)\nbalance",
        "group": "ACCOUNTS"
    },
    {
        "id": "BRANCHES",
        "label": "BRANCHES",
        "title": "branch_id (PK)\nbranch_name\nlocation",
        "group": "BRANCHES"
    },
    {
        "id": "TRANSACTIONS",
        "label": "TRANSACTIONS",
        "title": "transaction_id (PK)\naccount_id (FK->ACCOUNTS)\namount\ntx_date",
        "group": "TRANSACTIONS"
    }
]

# Define edges representing foreign key relationships
edges = [
    {"from": "ACCOUNTS", "to": "CUSTOMERS", "label": "customer_id (FK)"},
    {"from": "ACCOUNTS", "to": "BRANCHES", "label": "branch_id (FK)"},
    {"from": "TRANSACTIONS", "to": "ACCOUNTS", "label": "account_id (FK)"}
]

# Create a NetworkX graph
G = nx.DiGraph()

# Add nodes to the graph
for node in nodes:
    G.add_node(node["id"], label=node["label"], title=node["title"], group=node["group"])

# Add edges to the graph
for edge in edges:
    G.add_edge(edge["from"], edge["to"], label=edge["label"])

# Create a PyVis network
net = Network(height='600px', width='100%', directed=True, bgcolor='#ffffff', font_color='black')

# Set the physics layout of the network
net.barnes_hut()

# Convert the NetworkX graph to PyVis
net.from_nx(G)

# Customize the nodes based on their group (table type)
colors = {
    "CUSTOMERS": "#FF7F3E",
    "ACCOUNTS": "#2A629A",
    "BRANCHES": "#78C850",
    "TRANSACTIONS": "#F0C674"
}

for node in net.nodes:
    node["color"] = colors.get(node["group"], "#D3D3D3")  # Default color if group not found
    node["shape"] = "box"
    node["font"]["size"] = 14
    node["font"]["color"] = "#000000"

# Customize the edges
for edge in net.edges:
    edge["color"] = "#0078d4"
    edge["arrows"] = "to"
    edge["font"] = {"align": "middle"}

# Generate the HTML for the network
with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html') as tmp_file:
    net.save_graph(tmp_file.name)
    net_path = tmp_file.name

# Display the network graph in Streamlit
components.html(open(net_path, 'r').read(), height=600, width=1000, scrolling=True)

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

**Relationships:**
- **ACCOUNTS → CUSTOMERS**: Each account is linked to a customer.
- **ACCOUNTS → BRANCHES**: Each account is associated with a branch.
- **TRANSACTIONS → ACCOUNTS**: Each transaction is tied to an account.

**Usage:**
- **Interactive Graph**: Click and drag nodes to explore relationships.
- **Tooltips**: Hover over nodes and edges to see detailed information.
""")
