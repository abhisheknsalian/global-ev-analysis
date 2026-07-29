import plotly.express as px


# ==========================================================
# Common Plotly Layout
# ==========================================================
def apply_layout(fig, y_title, legend_title="Powertrain"):
    """
    Apply a consistent layout to all Plotly charts.
    """

    fig.update_layout(
        template="plotly_white",
        height=650,
        title_x=0.5,
        font=dict(size=14),
        legend_title=legend_title,
        xaxis_title="Year",
        yaxis_title=y_title,
        margin=dict(
            l=10,
            r=10,
            t=60,
            b=10
        )
    )

    fig.update_xaxes(
        showgrid=False,
        zeroline=False
    )

    fig.update_yaxes(
        showgrid=True,
        zeroline=False,
        tickformat=",.0s"
    )

    return fig


# ==========================================================
# Global EV Sales
# ==========================================================
def global_sales_chart(df):

    sales = df[
        (df["category"] == "Historical")
        & (df["parameter"] == "EV sales")
        & (df["mode"] == "Cars")
        & (df["region_country"] == "World")
        & (df["powertrain"].isin(["BEV", "PHEV"]))
    ]

    fig = px.line(
        sales,
        x="year",
        y="value",
        color="powertrain",
        markers=True,
        title="Global EV Sales (BEV vs PHEV)"
    )

    return apply_layout(fig, "EV Sales")


# ==========================================================
# Global EV Stock
# ==========================================================
def global_stock_chart(df):

    stock = df[
        (df["category"] == "Historical")
        & (df["parameter"] == "EV stock")
        & (df["mode"] == "Cars")
        & (df["region_country"] == "World")
        & (df["powertrain"].isin(["BEV", "PHEV"]))
    ]

    fig = px.area(
        stock,
        x="year",
        y="value",
        color="powertrain",
        title="Global EV Stock (BEV vs PHEV)"
    )

    return apply_layout(fig, "EV Stock")


# ==========================================================
# Top 10 BEV Sales (2024)
# ==========================================================
def top10_countries_chart(df):

    sales = df[
        (df["category"] == "Historical")
        & (df["parameter"] == "EV sales")
        & (df["powertrain"] == "BEV")
        & (df["year"] == 2024)
    ].copy()

    exclude = [
        "World",
        "Europe",
        "EU27",
        "Asia Pacific",
        "North America",
        "Central and South America",
        "Rest of the world",
        "Other"
    ]

    sales = sales[
        ~sales["region_country"].isin(exclude)
    ]

    top10 = (
        sales.sort_values("value", ascending=False)
        .head(10)
    )

    fig = px.bar(
        top10,
        x="value",
        y="region_country",
        orientation="h",
        color_discrete_sequence=["#1f77b4"],
        title="Top 10 Countries by BEV Sales (2024)"
    )

    fig.update_layout(
        template="plotly_white",
        height=650,
        title_x=0.5,
        xaxis_title="BEV Sales",
        yaxis_title="Country"
    )

    fig.update_yaxes(categoryorder="total ascending")

    return fig

# ==========================================================
# Choropleth Map
# ==========================================================
def choropleth_chart(df):

    data = df[
        (df["category"] == "Historical")
        & (df["parameter"] == "EV sales")
        & (df["powertrain"] == "BEV")
        & (df["year"] == 2024)
    ].copy()

    exclude = [
        "World",
        "Europe",
        "EU27",
        "Asia Pacific",
        "North America",
        "Central and South America",
        "Rest of the world",
        "Other"
    ]

    data = data[
        ~data["region_country"].isin(exclude)
    ]

    fig = px.choropleth(
        data,
        locations="region_country",
        locationmode="country names",
        color="value",
        hover_name="region_country",
        color_continuous_scale="Viridis",
        title="Global Distribution of BEV Sales (2024)"
    )

    fig.update_layout(
        template="plotly_white",
        height=800,
        title_x=0.5
    )

    fig.update_geos(
    showcountries=True,
    showcoastlines=True,
    fitbounds="locations"
    )

    return fig

# ==========================================================
# Bubble Chart
# ==========================================================
def bubble_chart(df):

    sales = df[
        (df["parameter"] == "EV sales")
        & (df["powertrain"] == "BEV")
        & (df["year"] == 2024)
    ][["region_country", "value"]].rename(columns={"value": "Sales"})

    stock = df[
        (df["parameter"] == "EV stock")
        & (df["powertrain"] == "BEV")
        & (df["year"] == 2024)
    ][["region_country", "value"]].rename(columns={"value": "Stock"})

    bubble = sales.merge(stock, on="region_country")

    exclude = [
        "World",
        "Europe",
        "EU27",
        "Asia Pacific",
        "North America",
        "Central and South America",
        "Rest of the world",
        "Other"
    ]

    bubble = bubble[
        ~bubble["region_country"].isin(exclude)
    ]

    fig = px.scatter(
        bubble,
        x="Sales",
        y="Stock",
        size="Stock",
        color="Sales",
        hover_name="region_country",
        color_continuous_scale="Viridis",
        title="BEV Sales vs EV Stock (2024)"
    )

    fig.update_layout(
        template="plotly_white",
        height=650,
        title_x=0.5
    )

    return fig

# ==========================================================
# Heatmap
# ==========================================================
def heatmap_chart(df):

    data = df[
        (df["category"] == "Historical") &
        (df["parameter"] == "EV sales") &
        (df["powertrain"] == "BEV") &
        (df["year"] >= 2015)
    ].copy()

    exclude = [
        "World",
        "Europe",
        "EU27",
        "Asia Pacific",
        "North America",
        "Central and South America",
        "Rest of the world",
        "Other"
    ]

    data = data[
        ~data["region_country"].isin(exclude)
    ]

    top10 = (
        data.groupby("region_country")["value"]
        .sum()
        .nlargest(10)
        .index
    )

    data = data[
        data["region_country"].isin(top10)
    ]

    heatmap = data.pivot_table(
        index="region_country",
        columns="year",
        values="value",
        aggfunc="sum"
    )

    fig = px.imshow(
        heatmap,
        text_auto=".2s",
        color_continuous_scale="YlOrRd",
        aspect="auto",
        title="BEV Sales Across Leading Markets (2015–2024)"
    )

    fig.update_layout(
        template="plotly_white",
        height=650,
        title_x=0.5
    )

    return fig

# ==========================================================
# Market Share Treemap
# ==========================================================
def treemap_chart(df):

    data = df[
        (df["category"] == "Historical") &
        (df["parameter"] == "EV sales") &
        (df["powertrain"] == "BEV") &
        (df["year"] == 2024)
    ].copy()

    exclude = [
        "World",
        "Europe",
        "EU27",
        "North America",
        "Central and South America",
        "Asia Pacific",
        "Rest of the world",
        "Other"
    ]

    data = data[
        ~data["region_country"].isin(exclude)
    ]

    europe = [
        "Germany","France","United Kingdom","Norway","Netherlands",
        "Sweden","Italy","Spain","Austria","Belgium","Denmark",
        "Finland","Switzerland","Portugal","Poland","Ireland",
        "Czech Republic","Slovakia","Hungary","Luxembourg","Iceland"
    ]

    asia = [
        "China","Japan","Korea","India","Indonesia","Thailand",
        "Malaysia","Singapore","Viet Nam","Chinese Taipei",
        "Israel","Türkiye"
    ]

    north_america = ["USA","Canada","Mexico"]
    oceania = ["Australia","New Zealand"]

    def region(country):
        if country in europe:
            return "Europe"
        elif country in asia:
            return "Asia"
        elif country in north_america:
            return "North America"
        elif country in oceania:
            return "Oceania"
        return "Other"

    data["Region"] = data["region_country"].apply(region)

    fig = px.treemap(
        data,
        path=["Region", "region_country"],
        values="value",
        color="value",
        color_continuous_scale="Viridis",
        title="Regional Distribution of BEV Sales (2024)"
    )

    fig.update_layout(
        template="plotly_white",
        height=700,
        title_x=0.5
    )

    return fig