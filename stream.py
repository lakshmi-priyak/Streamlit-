import os
import streamlit as st
import pickle
import numpy as np

# Get the absolute path to the pickle file
pickle_file_path = os.path.join(os.getcwd(), 'sample.pkl')

# Check if the file exists
if os.path.exists(pickle_file_path):
    with open(pickle_file_path, 'rb') as f:
        model = pickle.load(f)
else:
    st.error("Error: pickle file 'sample.pkl' not found.")
    st.stop()

def predict_cancer(Age, TumorSize, EstrogenStatus, ProgesteroneStatus, RegionalNodeExamined, NStage, SixthStage, differentiate, RegionalNodPositive):
    input_data = np.array([[Age, TumorSize, EstrogenStatus, ProgesteroneStatus, RegionalNodeExamined, NStage, SixthStage, differentiate, RegionalNodPositive]]).astype(np.int16)
    prediction = model.predict_proba(input_data)
    pred = '{0:.{1}f}'.format(prediction[0][0], 2)
    return float(pred)

def main():
    st.title("Streamlit")
    html_temp = """
    <div style="background-color:black ;padding:10px">
    <h2 style="color:white;text-align:center;">Breast Cancer Prediction</h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)

    Age = st.text_input("Age", "Type Here")
    TumorSize = st.text_input("TumorSize", "Type Here")
    EstrogenStatus = st.text_input("EstrogenStatus", "Type Here")
    ProgesteroneStatus = st.text_input("ProgesteroneStatus", "Type Here")
    RegionalNodeExamined = st.text_input("RegionalNodeExamined", "Type Here")
    NStage = st.text_input("NStage", "Type Here")
    SixthStage = st.text_input("SixthStage", "Type Here")
    differentiate = st.text_input("differentiate", "Type Here")
    RegionalNodePositive = st.text_input("RegionalNodPositive", "Type Here")

    safe_html = """
       <div style="background-color:grey ;padding:10px">
       <h2 style="color:white;text-align:center;">The Patient is Alive</h2>
       </div>
    """

    danger_html = """
       <div style="background-color:grey ;padding:10px">
       <h2 style="color:white;text-align:center;">The Patient is Dead</h2>
       </div>
    """

    if st.button("Predict"):
        output = predict_cancer(Age, TumorSize, EstrogenStatus, ProgesteroneStatus, RegionalNodeExamined, NStage, SixthStage, differentiate, RegionalNodePositive)
        st.success("The probability of the patient diagnosed with cancer is {}".format(output))

        if output > 0.5:
            st.markdown(danger_html, unsafe_allow_html=True)
        else:
            st.markdown(safe_html, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
