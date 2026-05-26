import streamlit as st
import pandas as pd
from io import StringIO

# ====================== DATA SETUP ======================
# Inventory Tracking
inventory_data = {
    "Category": [
        "Clothing and Accessories", "Shoes and Footwear", "Furniture and Home Decor",
        "Housewares Kitchenware Barware", "Books Vinyl Media LEGO",
        "Electronics Games Small Appliances", "Jewelry Tools Sporting Goods",
        "Childrens Items Holiday Linens", "Overall Recommendation"
    ],
    "Recommended Tools": [
        "Square POS Square Inventory", "Square POS Square Inventory",
        "Square POS Square Inventory + Notes", "Square POS Square Inventory",
        "Square POS Square Inventory", "Square POS Square Inventory",
        "Square POS Square Inventory", "Square POS Square Inventory",
        "Square POS + Square Inventory"
    ],
    "Key Features": [
        "Sizes colors styles brands condition photos", "Size tracking pair matching condition",
        "Large item tracking dimensions photos location", "Bulk tracking condition notes",
        "Condition notes search tags", "Testing notes serial numbers condition",
        "Detailed condition photo tracking", "Age seasonal tagging safety notes",
        "Real-time sync payments inventory"
    ],
    "Best For": [
        "All scales - Primary recommendation", "High-volume intake",
        "Scaled operations", "Daily donations",
        "High-turnover categories", "Higher-value items",
        "Premium niche items", "Seasonal peaks",
        "Lean to full scale"
    ]
}

# Pricing Tools
pricing_data = {
    "Tool Platform": ["Square Pricing", "Square Inventory Rules", "Square Promotions", "Manual Square Adjustments"],
    "Features": [
        "Square built-in pricing rules category pricing",
        "Automated markdowns by age or category",
        "Discounts bundles color rotation promotions",
        "Quick price changes based on demand"
    ],
    "Integration": ["Native to Square"] * 4,
    "Automation Level": ["High", "High", "High", "Medium"]
}

# Job & Task Management
job_tools_data = {
    "Tool": ["Square Team Management", "Connecteam", "Deputy", "Homebase", "When I Work"],
    "Best For": [
        "Staff scheduling and time tracking",
        "Task checklists and advanced scheduling",
        "Full labor management",
        "Payroll and daily tasks",
        "Mobile scheduling"
    ],
    "Key Features": [
        "Time clock scheduling basic tasks",
        "Checklists role access time tracking",
        "Scheduling compliance payroll",
        "Daily checklists time tracking",
        "Shift swaps notifications"
    ],
    "Pricing approx": [
        "Included with Square",
        "Free tier + 29 per month",
        "5 per user per month",
        "Free + 24 per location",
        "2.50 per user per month"
    ]
}

# SOP & Checklists
sop_data = {
    "Tool": ["Process Street", "SweetProcess", "Tango or Scribe", "Notion or Trainual", "Manifestly Checklists"],
    "Best For": [
        "Interactive checklists",
        "SOP and training",
        "Video checklists",
        "Central SOP hub",
        "Recurring workflows"
    ],
    "Key Features": [
        "Recurring tasks role-based SOPs",
        "Step-by-step guides",
        "Screen recording to checklist",
        "Knowledge base and training",
        "Automated reminders"
    ],
    "Use Case in Thrift Store": [
        "Daily sorter merchandiser cashier checklists",
        "Role-specific training for 14-34 staff",
        "Packing shipping and intake processes",
        "Owner and associate training",
        "Morning intake and end-of-day procedures"
    ]
}

# Master List
master_data = {
    "Category": [
        "Inventory Tracking", "Inventory Tracking", "Pricing", "Pricing",
        "Job and Task Management", "Job and Task Management", "Job and Task Management",
        "SOP and Checklists", "SOP and Checklists", "SOP and Checklists"
    ],
    "Tool Name": [
        "Square POS + Square Inventory", "Square Inventory", "Square Pricing Tools",
        "Square Promotions", "Square Team Management", "Connecteam", "Homebase",
        "Process Street", "SweetProcess", "Tango Scribe"
    ],
    "Primary Use": [
        "Core inventory and sales", "Thrift item tracking", "Dynamic pricing",
        "Discount management", "Staff time and basic tasks", "Advanced task management",
        "Daily checklists and payroll", "Interactive daily checklists",
        "SOP documentation", "Video SOPs"
    ],
    "Key Features": [
        "Real-time sync payments inventory", "Condition notes category tags",
        "Category rules markdowns", "Bundles and rotations",
        "Time clock scheduling", "Checklists and assignments",
        "Task lists time tracking", "Role-based workflows",
        "Training and procedures", "Quick process creation"
    ],
    "Recommended For": [
        "Lean start - Primary recommendation", "High volume donations",
        "All categories", "Daily pricing management",
        "All staff levels", "14-34 staff scaling",
        "Small to medium team", "Sorter Merchandiser Cashier",
        "All associate roles", "Shipping and intake training"
    ]
}

# ====================== STREAMLIT APP ======================
st.set_page_config(page_title="Fantastic Finds Tools Hub", layout="wide")
st.title("🛍️ Fantastic Finds Thrift Store - Tools Dashboard")
st.markdown("**Gulf Shores, Alabama** | Owned by Nathan Rossow | 2027 Launch")
st.caption("One centralized place to see what software tool is needed for every function in the business.")

# Sidebar Navigation
page = st.sidebar.selectbox(
    "Choose a Section",
    ["Home", "Inventory Tracking", "Product Pricing", "Job & Task Management", 
     "SOP & Daily Checklists", "Master Tools Overview"]
)

# ====================== PAGES ======================
if page == "Home":
    st.header("Welcome to the Tools Hub")
    st.write("""
    This app shows exactly which tools are recommended for **Fantastic Finds Thrift Store**.
    
    Nathan handles all physical work. Square is the main system for inventory, sales, and basic team management.
    Use the sidebar to explore each area of the business.
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Core System", "Square POS + Inventory")
    with col2:
        st.metric("Primary Focus", "Lean + Scalable")
    with col3:
        st.metric("Owner Schedule", "8 hrs/day, 7 days/week")

elif page == "Inventory Tracking":
    st.header("📦 Inventory Tracking by Product Category")
    df = pd.DataFrame(inventory_data)
    st.dataframe(df, use_container_width=True, hide_index=True)

elif page == "Product Pricing":
    st.header("💰 Product Pricing Tools")
    df = pd.DataFrame(pricing_data)
    st.dataframe(df, use_container_width=True, hide_index=True)

elif page == "Job & Task Management":
    st.header("👥 Job Assignment & Team Management")
    df = pd.DataFrame(job_tools_data)
    st.dataframe(df, use_container_width=True, hide_index=True)

elif page == "SOP & Daily Checklists":
    st.header("✅ SOPs & Daily Checklists")
    df = pd.DataFrame(sop_data)
    st.dataframe(df, use_container_width=True, hide_index=True)

elif page == "Master Tools Overview":
    st.header("🔄 Master Tools List")
    df = pd.DataFrame(master_data)
    st.dataframe(df, use_container_width=True, hide_index=True)

# Footer
st.divider()
st.markdown("**Recommended Stack for Fantastic Finds**: **Square** (Main POS + Inventory) + Connecteam/Homebase (Team) + Process Street (SOPs)")
st.caption("Built for Nathan Rossow's thrift store business plan")
