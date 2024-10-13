import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from .src.data_management import download_dataframe_as_csv  # Correct relative import
from .src.machine_learning.predictive_analysis import (
    load_model_and_predict,
    resize_input_image,
    plot_predictions_probabilities
)

def page_mildew_detector_body():
    st.info(
        "The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew."
    )

    st.write(
        "Here you can download a set of mildew or healthy leaves for live prediction. "
        "You can download the images from [here](https://github.com/Luisg882/mildew-detection-in-cherry-leafs/tree/main/inputs/mildew_detection_in_cherry_leaves/cherry-leaves)"

    )
    st.write("---")

    images_buffer = st.file_uploader(
        'Upload leaf image. You may select more than one.',
        type='png', 
        accept_multiple_files=True
    )
   
    if images_buffer:
        df_report = pd.DataFrame([])  # Initialize the DataFrame outside the loop
        for image in images_buffer:
            img_pil = Image.open(image)
            st.info(f"Leaf Image: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(img_pil, caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height")

            version = 'v1'  # Make sure to define version here
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(resized_img, version=version)
            plot_predictions_probabilities(pred_proba, pred_class)

            df_report = df_report.append({"Name": image.name, 'Result': pred_class}, ignore_index=True)
        
        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(df_report), unsafe_allow_html=True)
