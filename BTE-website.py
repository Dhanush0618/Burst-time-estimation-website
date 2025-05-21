#To execute this program open cmd in same file directory(C:\Users\my\OneDrive\Desktop) and execute the command:
#                                                                               "python -m streamlit run app.py"
#In any other computer:
#   1. pip install streamlit(to create web)
#   2. pip install requests(handling url)
#   3. pip install streamlit_lottie(interactive animations)


from PIL import Image
from pathlib import Path
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import matplotlib.pyplot as plt

st.set_page_config(page_title="Burst Time Estimator", page_icon="🧑‍💻", layout="wide")

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    
lottie_coding = load_lottie("https://lottie.host/6dbbceae-dcb1-4090-96bb-a27fdc3780d9/z5M0BKqkDg.json")
lottie_code = load_lottie("https://lottie.host/83bc7e5b-04bb-430e-90de-0cd3e9bd9495/ery6ZcH6sH.json")
img_path = Path("image") / "sphn-image.png"
img_sphn = Image.open(img_path)
img_sphn = img_sphn.resize((10000,10000))

with st.container():
    col_1, col_2 = st.columns((1,10), gap="small")
    with col_1:
        st.image(img_sphn, width=None)
    with col_2:
        st.markdown(
            "<h4 style='text-align: center;'>Project Based Learning: Burst Time Estimation Using Streamlit.io</h4>",
        unsafe_allow_html=True)
        st.markdown(
            "<h1 style='text-align: center;'>Welcome to our Website 🙏</h1.",
            unsafe_allow_html=True)
    
with st.container():
    txt_col, gif_col = st.columns((2,1))
    with txt_col:
        st.subheader("We are using :red[streamlit/Python] to create a website for :red[Predicting] the burst time of processes")
        st.write("""There are many ways to predict the burst time of a process:""")
        st.write("1. Using the EXPONENTIAL AVERAGING method:")
        st.write("""Predict the burst time of the next process using the previuos burst time.   :cyan[**Formula is: e(t+1) = ( a * a[t-1] ) + ( (1-a) * e(t) )**]
                 \nwhere e(t) is the predicted burst time at time t, a(t) is the actual burst time at time t, and alpha is a smoothing factor (typically between 0 and 1).""")
        st.write("[Learn more about EXPONENTIAL AVERAGING >](https://www.scribd.com/presentation/834380705/Burst-Time-Prediction:~:text=Burst%20Time%20Prediction-,The%20document%20discusses%20Shortest%20Job%20First%20(SJF)%20scheduling%2C%20which,burst%20times%20using%20exponential%20averaging)")
        st.write("2. Using Machine Learning:")
        st.write("Machine learning offers a powerful approach to estimate the CPU burst time of processes, a crucial element for efficient CPU scheduling algorithms like SJF (Shortest Job First) and SRTF (Shortest Remaining Time First). By leveraging historical data and process attributes, ML models can predict burst times more accurately than traditional methods like exponential averaging. ")
        st.write("[Learn more about ML algorithms >](https://thegrenze.com/pages/servej.php?fn=326.pdf&name=Comparative%20Study%20on%20Calculating%20CPU%20Burst%20Timeusing%20Different%20Machine%20Learning%20Algorithms&id=1716&association=GRENZE&journal=GIJET&year=2023&volume=9&issue=1)")
        st.write("IMPORTANCE:")
        st.write("i)EFFICIENT CPU RESOURCE ALLOCATION:")
        st.write("Accurate burst time estimations allow scheduling algorithms to make better decisions about which processes to run first, leading to improved overall system performance.") 
        st.write("ii)REAL-TIME SCHEDULLING:")
        st.write("Real-time systems often require knowing the execution time of tasks beforehand to guarantee deadlines, making accurate burst time estimation essential.") 
        st.write("iii)PERFORMANCE IMPROVEMENT:")
        st.write("By predicting burst times, scheduling algorithms can minimize waiting time and turnaround time for processes, leading to a more responsive and efficient system.")
        st.write("##")
        st.write("TO KNOW MORE, [Click Here >](https://www.researchgate.net/publication/341481948_Revised_Formula_for_Estimating_CPU-Burst)")
        
    with gif_col:

        st.lottie(lottie_coding, height=700, key="coding_2")
                
        
with st.container():
    st.write("---")
    lt_col, rt_col = st.columns((2,1))
    with lt_col:
        st.header("The code for 'BURST TIME ESTIMATION' is:")
        code="""
            def estimate(act_bt,a,e_0):
                pred_bt=[e_0]
                for i in range(1,len(act_bt)):
                    prev_pred=pred_bt[-1]
                    pred=a*act_bt[i-1]+(1-a)*prev_pred
                    pred_bt.append(pred)
                return pred_bt

            act_bt=[]
            n=int(input("enter no. of processes: "))
            print("enter burst time of each process: ")
            for i in range(n):
                bt=float(input(f"Process {i+1}: "))
                act_bt.append(bt)

            e_0=float(input("enter the initial predicted burst time: "))
            a=float(input("enter smooothing factor (0<=a<=1): "))

            pred_bt=estimate(act_bt,a,e_0)

            print("\nProcess\tActual_BT Predicted_BT")
            print("-----------------------------------------")
            for i in range(n):
                print("P",i,"\t",act_bt[i],"\t    ",pred_bt[i],(" (Previous Prediction)" if i==0 else ""))"""
            
        st.code(code, language='python')

    with rt_col:
        st.lottie(lottie_code, height=900, key="coding")
        
with st.container():
    lft_col, rgt_col = st.columns((1,2))
    with lft_col:
        st.title("Burst Time Predictor (Exponential Averaging)")
        st.markdown("Formula: `e(t+1) = α × t + (1 - α) × e(t)`")
        
        act_burst = st.number_input("Actual Burst Time (t)", min_value=0.0, max_value=10.0, format="%.2f")
        prev_estimate = st.number_input("Previous Estimated Burst Time (e(t))", min_value=0.0, max_value=10.0, format="%.2f")
        alpha = st.slider("Alpha (α)", min_value=0.0, max_value=1.0, value=0.5, step=0.05)
        next_estimate = 0
        
        if st.button("Predict Next Burst Time"):
            next_estimate = alpha * act_burst + (1 - alpha) * prev_estimate
            st.success(f"Predicted Next Burst Time: {next_estimate:.2f}")
            st.balloons()
    with rgt_col:
        labels = ['Prev_BT (e(t))', 'Act_BT (t)', 'Pred_BT (e(t+1))']
        values = [prev_estimate, act_burst, next_estimate]

        fig, ax = plt.subplots(figsize = (6,3)) #6 is width and 3 is lenght
        bars = ax.bar(labels, values, color=['skyblue', 'orange', 'green'])
        ax.set_ylabel('Burst Time')
        ax.set_title('Burst Time Prediction Using Exponential Averaging')
        ax.bar_label(bars, fmt='%.2f')
        st.pyplot(fig)

with st.container():
    st.write("---")
    st.subheader("Presented by:\nDHANUSH KUMAR (23N81A67C6)")
    st.write("P.BHUVAN (24N85A6702)")
    st.write("BHASKER (23N81A6766)")
    st.write("B.KARTHIK (23N81A6772)")
    st.write("AKSHAY KUMAR (23N81A6770)")
    st.write("##")
    st.subheader("\u00A9 Group no.11. All rights are reserved.")

    
        

    
        

        
    
    
