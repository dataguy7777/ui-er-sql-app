import streamlit as st
from st_link_analysis import st_link_analysis

st.set_page_config(layout="wide")
st.title("Linked Cubes Visualization")

# Define cubes as nodes
nodes = [
    {"id": "Cube_AssetBackedSecurity", "label": "Asset backed security (BIRD_ABS_ELDM)"},
    {"id": "Cube_SecurityExchange", "label": "Security and exchange tradable derivative (BIRD_SCRTY_EXCHNG_TRDBL_DRVTV_EIL)"},
    {"id": "Cube_OtherFramework", "label": "Some matching cube from other Framework"}
]

# Define edges
edges = [
    {"source": "Cube_AssetBackedSecurity", "target": "Cube_SecurityExchange"},
    {"source": "Cube_SecurityExchange", "target": "Cube_OtherFramework"}
]

# Try using dictionaries for styles if NodeStyle and EdgeStyle classes cause errors
node_style = {
    "color": "#f0f0f0",
    "border_color": "#666666",
    "shape": "box",
    "font_color": "#000000",
    "font_size": 12
}

edge_style = {
    "color": "#0078d4",
    "width": 2,
    "directed": False
}

st.subheader("Cubes Network")
st.write("This network graph shows multiple cubes and their links.")

# Pass the dictionaries directly
st_link_analysis(nodes, edges, node_style=node_style, edge_style=edge_style, height=600, width=1000)

st.markdown("""
**Cube Details:**

- **Cube: Asset backed security (BIRD_ABS_ELDM)**
  - Description: A debt security with underlying assets.
  - Maintained by: SDD team (ECB)
  - Type of cube: ELDM - Uncommon cube type
  - Version: 1 (01.07.2023 - 31.12.9999)

- **Cube: Security and exchange tradable derivative (BIRD_SCRTY_EXCHNG_TRDBL_DRVTV_EIL)**
  - Forward engineered from: Asset backed security (BIRD_ABS_ELDM)
  
- **Cube: OtherFramework Cube**
  - Represents a cube from another framework or domain linking to SecurityExchange cube.
""")
