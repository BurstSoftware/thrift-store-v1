import streamlit as st
import pandas as pd

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

# ====================== SANITIZED BUSINESS PLAN ======================
business_plan = """
**Comprehensive Business Plan**  
**[Thrift Store Name]**

**Sole Owner & Operator:** [Owner Name]  

**Launch:** 2027

### Executive Summary
[Thrift Store Name] is a high-volume, curated thrift and resale store. [Owner Name] is the 100% sole owner of the LLC and the only individual performing physical operations. All non-physical tasks are automated through 6 specialized virtual AI agents supported by Shopify as the central platform.

[Owner Name] will work an 8-hour workday, 7 days a week (56 hours per week) handling only physical tasks. The business capitalizes on strong tourism economy and resident base for high sales velocity in affordable secondhand goods priced $1–$5.

**Key Financials:**
- [Owner Name] annual salary: $250,000.
- Virtual AI agents + Shopify: $122,000 – $125,000.
- Rent, utilities & overhead: $80,000 – $140,000.
- Total Year 1 Expenses: $452,000 – $515,000.
- Sales Target: 5,000 items per week (250,000 items/year) at $3.50 average price = $875,000 Year 1 revenue.
- Projected Year 1 Net Profit: $360,000 – $423,000.

The lean owner-operated model with AI automation, donation-based inventory (near-zero COGS), and strong local/tourist demand positions the business for rapid profitability and scalability.

### Company Description
- Legal Structure: LLC owned 100% by [Owner Name].
- Mission: Offer quality, affordable secondhand treasures while promoting sustainability, reuse, and a fun coastal “treasure hunt” shopping experience.
- Unique Value Proposition: Daily fresh inventory, beach-themed curation, owner-managed quality control, hybrid in-store + online model via Shopify.

### Market Analysis
The area combines a stable resident base with strong tourism. High discretionary spending aligns perfectly with thrift store strengths. The national secondhand market continues expanding at 8–14% annually.

Target customers: Local families, retirees, budget-conscious residents, and tourists seeking vacation outfits, souvenirs, and home accents.

### Products and Services
**Top 20 Common High-Volume / High-Margin Staples:**  
1. Clothing (name-brand, vintage, denim)  
2. Shoes  
3. Books  
4. Furniture  
5. Housewares/Kitchenware  
6. Designer handbags & accessories  
7. Video games & electronics  
8. Picture frames & art  
9. Jewelry  
10. Lamps & lighting  
11. Vintage barware & glassware  
12. Tools & hardware  
13. Holiday decorations  
14. Children’s clothing & toys  
15. Vinyl records & media  
16. Home decor  
17. Sporting goods/outdoor gear  
18. Linens & textiles  
19. Small appliances  
20. LEGO & collectibles.

**Top 20 Trending Products (2026–2027 Focus):**  
1. Vintage denim & Y2K clothing  
2. Bold/ornate mirrors  
3. Midcentury modern furniture  
4. Chrome accents  
5. Natural fabrics  
6. Vintage lighting  
7. Crafting/sewing supplies  
8. ’90s/Y2K tech  
9. Athleisure & premium activewear  
10. Statement chairs  
11. Tactile wall art & figurines  
12. Vintage barware  
13. Leather jackets  
14. Designer labels  
15. Brass trinkets  
16. Compact furniture  
17. Brooches, tassels & poet-core accessories  
18. Wood & natural material goods  
19. Unique pottery & majolica  
20. Sustainable/eco-branded items.

**Special Focus:** Beach-themed decor, shells, vacation clothing, and outdoor gear.

**Services:** Item bundling, minor upcycling/repairs, seasonal events, and online shipping.

### Operations Plan
- Store Hours: 7 days/week, aligned with tourist traffic.  
- Daily Process: [Owner Name] handles all physical verification, validation, acceptance, sorting, and staging of donations.  
- Technology: Shopify POS and online store for real-time inventory sync.

**Daily Schedule (8 hours/day, 7 days/week):**  
Donation intake & physical processing, Merchandising & store displays, Customer assistance, Packing & shipping online orders, Quality control & closing procedures.

### Management and Organization
**Sole Owner:** [Owner Name] – full physical operations + strategic oversight.  
**Virtual AI Agents (6):** Handle all digital, administrative, and marketing tasks 24/7.

### Labor Cost Projections
[Owner Name]: $250,000/year fixed.

**Additional Employees Scaling:**
- Lean (AI only): $0  
- Minimum (14 employees): $728,000  
- Moderate (24 employees): $1,248,000  
- Full (34 employees): $1,768,000

### Risks & Opportunities
**Risks:** Inventory inconsistency, competition, economic sensitivity, owner workload, labor scaling.  
**Opportunities:** Tourism growth, sustainability boom, hybrid sales, upcycling, partnerships.

### Financial Projections (5 Years)
(Full table with revenue, category breakdown, expenses, and profit projections as previously provided)

**Startup Capital Required:** $85,000 – $125,000

**Recommendations & Next Steps** are included for bankers, lenders, and investors.
"""

# ====================== STREAMLIT APP ======================
st.set_page_config(page_title="[Thrift Store Name] Tools Hub", layout="wide")
st.title("🛍️ [Thrift Store Name] - Tools Dashboard")
st.caption("One centralized place to see what software tool is needed for every function in the business.")

# Sidebar Navigation
page = st.sidebar.selectbox(
    "Choose a Section",
    ["Home - Business Plan", "Inventory Tracking", "Product Pricing", 
     "Job & Task Management", "SOP & Daily Checklists", "Master Tools Overview"]
)

# ====================== PAGES ======================
if page == "Home - Business Plan":
    st.header("📋 Comprehensive Business Plan")
    st.markdown(business_plan, unsafe_allow_html=True)

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
st.markdown("**Recommended Stack**: **Square** (Main POS + Inventory) + Connecteam/Homebase (Team) + Process Street (SOPs)")
st.caption("Tools Dashboard for [Thrift Store Name]")
