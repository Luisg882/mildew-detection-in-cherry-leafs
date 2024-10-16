import streamlit as st
from app_pages.multipage import MultiPage


# load pages scripts
from app_pages.page_ml_performance import page_ml_performance_body
from app_pages.page_project_summary import page_project_sumary_body
from app_pages.page_leaves_visualizer import page_leaves_visualizer_body
from app_pages.page_mildew_detector import page_mildew_detector_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body



app = MultiPage(app_name="Mildew Detector in Cherry Leaves")  # Create an instance of the app


# Add your app pages here using .add_page()

app.add_page("Project Summary", page_project_sumary_body)
app.add_page("Leaves Visualizer", page_leaves_visualizer_body)
app.add_page("Mildew Detector", page_mildew_detector_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("Machine Learning Performance", page_ml_performance_body)



app.run()