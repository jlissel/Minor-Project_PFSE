import streamlit as st
import plotly.graph_objects as go
import my_app_module as sam

st.header("Bending Moment of a Glulam Beam over a Length Range")

st.sidebar.subheader("Results Parameters")
min_length = st.sidebar.number_input("Minimum beam length (mm)", value=100)
max_length = st.sidebar.number_input("Maximum beam length (mm)", value=10000)
interval = st.sidebar.number_input("Length step interval (mm)", value=100)
length = st.sidebar.number_input("Length (mm)", value=5000)
b = st.sidebar.number_input("Width (mm)", value = 315)
d = st.sidebar.number_input("Depth (mm)", value = 720)
fb = st.sidebar.number_input("Specified bending strength (MPa)", value = 30.6)

# K Factors
st.sidebar.subheader("K Factors")
kD = st.sidebar.number_input("Load Duration Factor, kD", value=1.0)
kH = st.sidebar.number_input("System Factor, kH", value=1.0)
ksb = st.sidebar.number_input("Service Condition Factor, ksb", value=1.0)
kT = st.sidebar.number_input("Treatment Factor, kT", value=1.0)
kx = st.sidebar.number_input("Curvature Factor, kx", value=1.0)
kL = st.sidebar.number_input("Lateral Stability Factor, kL", value=1.0)

# Calculation of "resistance lines"
results = sam.bending_capacity_vs_length(
    min_length,
    max_length,
    interval,
    length,
    b,
    d,
    fb,
    kD,
    kH,
    ksb,
    kT,
    kx,
    kL,
)

length_input = st.number_input(label="Length", min_value=min_length, max_value=max_length)

# Calculation of individual point for plot marker and example calculations
example_latex, factored_load = sam.calc_mr_at_given_length(
    length, 
    b, 
    d, 
    fb,
    1.0, 
    1.0, 
    1.0,
    1.0,
    1,0,
    1,0,
    )

fig = go.Figure()

# Plot lines
fig.add_trace(
    go.Scatter(
    x=results["Glulam Beam"][1], 
    y=results["Glulam Beam"][0],
    line={"color": "red"},
    name="Glulam Beam"
    )
)

fig.add_trace(
    go.Scatter(
        y=[length_input],
        x=[factored_load],
        name="Example Calculation: Glulam Beam"
    )
)

fig.layout.title.text = "Factored moment resistance of glulam beam"
fig.layout.xaxis.title = "Factored moment resistance, Knm"
fig.layout.yaxis.title = "Length of beam, mm"


st.plotly_chart(fig)

calc_expander_a = st.expander(label="Sample Calculation, Glulam Beam")
with calc_expander_a:
    for calc in example_latex:
        st.latex(
            calc
        )