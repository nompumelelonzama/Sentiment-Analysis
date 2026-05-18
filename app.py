# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# import nltk
# from streamlit_option_menu import option_menu
# from datetime import datetime
# import numpy as np
# from wordcloud import WordCloud


# # Initialize NLTK VADER
# nltk.download('vader_lexicon', quiet=True)
# sid = SentimentIntensityAnalyzer()

# # --- 1. UI Configuration & Dark Serene Styling ---
# st.set_page_config(page_title="Sentient AI | Data Insights", layout="wide", page_icon="🌙")

# # Initialize Session State for History & Data
# if 'history' not in st.session_state:
#     st.session_state.history = []
# if 'analyzed_df' not in st.session_state:
#     st.session_state.analyzed_df = None

# # Custom CSS for Premium Dark Mode
# st.markdown("""
#     <style>
#     /* Dark Theme Core */
#     .stApp {
#         background-color: #0b0d11;
#         color: #e0e0e0;
#     }
#     [data-testid="stSidebar"] {
#         background-color: #12151c;
#         border-right: 1px solid #1f232d;
#     }
    
#     /* Professional Headers & Gradient Text */
#     h1, h2, h3 {
#         color: #a29bfe;
#         font-family: 'Inter', sans-serif;
#         font-weight: 700;
#     }
#     .hero-title {
#         font-size: 3rem;
#         background: linear-gradient(to right, #a29bfe, #6c5ce7);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         font-weight: 800;
#     }

#     /* Analyze Button Styling */
#     .stButton>button {
#         width: 100%;
#         border-radius: 12px;
#         background: linear-gradient(45deg, #6c5ce7, #a29bfe);
#         color: white;
#         border: none;
#         padding: 18px;
#         font-weight: bold;
#         transition: 0.4s;
#         box-shadow: 0 4px 20px rgba(108, 92, 231, 0.2);
#     }
#     .stButton>button:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 8px 25px rgba(108, 92, 231, 0.4);
#     }

#     /* Metric Cards Glassmorphism */
#     div[data-testid="stMetric"] {
#         background: rgba(28, 31, 43, 0.8);
#         border: 1px solid rgba(162, 155, 254, 0.2);
#         border-radius: 15px;
#         padding: 20px;
#     }

#     /* Report Card Styling */
#     .report-card {
#         background: rgba(22, 25, 34, 0.9);
#         border: 1px solid rgba(162, 155, 254, 0.15);
#         border-radius: 16px;
#         padding: 24px;
#         margin-bottom: 16px;
#     }
#     .stat-pill {
#         display: inline-block;
#         padding: 4px 14px;
#         border-radius: 20px;
#         font-size: 0.8rem;
#         font-weight: 600;
#         margin: 4px;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # --- 2. Sidebar Navigation & Logo ---
# with st.sidebar:
#     st.markdown("""
#         <div style="text-align: center; padding-bottom: 20px;">
#             <img src="https://cdn-icons-png.flaticon.com/512/2103/2103633.png" width="70" style="filter: invert(80%) sepia(20%) saturate(1000%) hue-rotate(220deg);">
#             <h2 style="color: #a29bfe; margin-top: 10px; letter-spacing: 2px;">SENTIENT AI</h2>
#             <p style="font-size: 0.7rem; color: #636e72;">PREMIUM INSIGHT ENGINE</p>
#         </div>
#     """, unsafe_allow_html=True)

#     selected_nav = option_menu(
#         menu_title=None,
#         options=["Home", "Dashboard", "History", "Data Explorer"],
#         icons=["house", "speedometer2", "clock-history", "table"],
#         menu_icon="cast",
#         default_index=0,
#         styles={
#             "container": {"padding": "0!important", "background-color": "transparent"},
#             "icon": {"color": "#a29bfe", "font-size": "18px"}, 
#             "nav-link": {"font-size": "15px", "text-align": "left", "margin":"5px", "color": "#a0a0a0"},
#             "nav-link-selected": {"background-color": "#6c5ce7", "color": "white"},
#         }
#     )

#     st.divider()
#     uploaded_file = st.file_uploader("Upload Dataset", type=["csv", "xlsx"])
    
#     if uploaded_file:
# # Optimized robust CSV/Excel reader
#         # if uploaded_file.name.endswith('csv'):
#         #     df_raw = pd.read_csv(
#         #         uploaded_file, 
#         #         on_bad_lines='skip',  # This ignores the line that causes the "saw 3" error
#         #         engine='python',      # The python engine is better at handling quotes/newlines
#         #         encoding='utf-8'      # Ensures special characters are read correctly
#         #     )
#      if uploaded_file:
#         # --- FIXED BLOCK START ---
#         if uploaded_file.name.endswith('csv'):
#             df_raw = pd.read_csv(uploaded_file, on_bad_lines='skip', engine='python')
        
#         else:
#             df_raw = pd.read_excel(uploaded_file)        
#         st.subheader("Analysis Scope")
#         analysis_mode = st.radio("Target Selection", ["Whole Dataset", "Specific Column"])
#         target_col = st.selectbox("Select Column:", df_raw.columns) if analysis_mode == "Specific Column" else df_raw.select_dtypes(include=['object']).columns[0]

#         st.subheader("Visual Studio")
#         chart_type = st.selectbox("Choose Graph Type", ["Donut Chart", "Bar Graph", "Line Graph (Trend)", "Histogram (Density)", "Combo Chart", "Pie Chart", "Heatmap","Scatter plot"])
#         accent_color = st.color_picker("Report Theme Color", "#a29bfe")

        

# # all_text = " ".join(df_raw[target_col].astype(str))

# # wordcloud = WordCloud(
# #     width=800,
# #     height=400,
# #     background_color='black',
# #     colormap='viridis'
# # ).generate(all_text)

# # fig_wc, ax = plt.subplots(figsize=(10,5))
# # ax.imshow(wordcloud, interpolation='bilinear')
# # ax.axis("off")

# # st.pyplot(fig_wc)

    

# # --- 3. Main Logic ---

# # --- PAGE: HOME ---
# if selected_nav == "Home":
#     st.markdown('<h1 class="hero-title">👋 Welcome to Sentient AI, the future of Data Interpretation.</h1>', unsafe_allow_html=True)
#     st.write("### Beautifully crafted sentiment analysis for the modern industry.")
#     st.image("https://images.unsplash.com/photo-1677442136019-21780ecad995?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80", use_container_width=True, caption="Powered by Sentient AI Deep Logic")


# # --- PAGE: DASHBOARD ---
# elif selected_nav == "Dashboard":
#     if not uploaded_file:
#         st.info("👋 Please upload a data file in the sidebar to begin your journey.")
#     else:
#         st.title("✨ Project Dashboard")
        
#         if st.button("🚀 GENERATE ANALYSIS & REPORT"):
#             with st.spinner("AI is interpreting your data..."):
#                 # Analysis Engine
#                 def get_scores(text):
#                     return sid.polarity_scores(str(text))['compound']

#                 def get_all_scores(text):
#                     scores = sid.polarity_scores(str(text))
#                     return scores['pos'], scores['neg'], scores['neu'], scores['compound']

#                 df_raw['Compound_Score'] = df_raw[target_col].apply(get_scores)
#                 df_raw[['Pos_Score', 'Neg_Score', 'Neu_Score', 'Compound_Score']] = df_raw[target_col].apply(
#                     lambda x: pd.Series(get_all_scores(x))
#                 )
#                 df_raw['Sentiment'] = df_raw['Compound_Score'].apply(lambda x: 'Positive' if x >= 0.05 else ('Negative' if x <= -0.05 else 'Neutral'))
#                 df_raw['Text_Length'] = df_raw[target_col].astype(str).apply(len)
#                 df_raw['Word_Count'] = df_raw[target_col].astype(str).apply(lambda x: len(x.split()))
#                 df_raw['Index'] = range(len(df_raw))
#                 st.session_state.analyzed_df = df_raw

#                 # Metrics
#                 total = len(df_raw)
#                 counts = df_raw['Sentiment'].value_counts()
#                 pos, neg, neu = counts.get('Positive', 0), counts.get('Negative', 0), counts.get('Neutral', 0)
#                 avg_score = df_raw['Compound_Score'].mean()
#                 std_score = df_raw['Compound_Score'].std()
#                 median_score = df_raw['Compound_Score'].median()

#                 m1, m2, m3, m4 = st.columns(4)
#                 m1.metric("Rows", total)
#                 m2.metric("Positive", f"{(pos/total*100):.1f}%", delta="High Approval")
#                 m3.metric("Negative", f"{(neg/total*100):.1f}%", delta="-Critical", delta_color="inverse")
#                 m4.metric("Neutral", f"{(neu/total*100):.1f}%")

#                 # Add to History
#                 st.session_state.history.append({
#                     "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
#                     "File": uploaded_file.name,
#                     "Column": target_col,
#                     "Result": f"Pos: {pos} | Neg: {neg}"
#                 })

#                 st.divider()

#                 # Dynamic Visuals — Primary Chart
#                 c1, c2 = st.columns([2, 1])
#                 with c1:
#                     st.subheader(f"Results: {chart_type}")
#                     color_map = {'Positive':'#00b894', 'Negative':'#ff7675', 'Neutral':'#74b9ff'}
                    
#                     if chart_type == "Donut Chart":
#                         fig = px.pie(df_raw, names='Sentiment', hole=0.6, color='Sentiment', color_discrete_map=color_map)
#                     elif chart_type == "Bar Graph":
#                         fig = px.bar(counts.reset_index(), x='Sentiment', y='count', color='Sentiment', color_discrete_map=color_map)
#                     elif chart_type == "Line Graph (Trend)":
#                         fig = px.line(df_raw, y='Compound_Score', title="Sentiment Fluency Across Data", markers=True)
#                         fig.update_traces(line_color=accent_color)
#                     else: # Histogram
#                         fig = px.histogram(df_raw, x='Compound_Score', nbins=20, color='Sentiment', color_discrete_map=color_map)
                    
#                     fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white", template="plotly_dark")
#                     st.plotly_chart(fig, use_container_width=True)

#                 with c2:
#                     st.subheader("AI Interpretation")
#                     status = "Favorable" if pos > neg else "Action Required"
#                     st.markdown(f"""
#                         <div style="background:#161922; padding:20px; border-radius:15px; border-left: 5px solid {accent_color};">
#                             <h4 style="color:{accent_color}">Status: {status}</h4>
#                             <p>Our AI has processed the <b>{target_col}</b> column. The emotional trajectory indicates a 
#                             { "strong positive bias" if pos > neg else "noticeable negative trend"}.</p>
#                             <hr style="opacity:0.1">
#                             <small>Data Source: {uploaded_file.name}</small>
#                         </div>
#                     """, unsafe_allow_html=True)

#                 # --- Statistics for Report ---
#                 st.divider()
#                 st.subheader("📊 Score Distribution by Sentiment Category")
#                 col_box1, col_box2 = st.columns([3, 2])

#                 with col_box1:
#                     fig_box = go.Figure()
#                     for sentiment, color in [('Positive', '#00b894'), ('Neutral', '#74b9ff'), ('Negative', '#ff7675')]:
#                         subset = df_raw[df_raw['Sentiment'] == sentiment]['Compound_Score']
#                         if len(subset) > 0:
#                             fig_box.add_trace(go.Box(
#                                 y=subset,
#                                 name=sentiment,
#                                 marker_color=color,
#                                 boxmean='sd',
#                                 line=dict(width=2),
#                             ))
#                     fig_box.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white", template="plotly_dark", height=420)
#                     st.plotly_chart(fig_box, use_container_width=True)

#                 with col_box2:
#                     st.markdown(f"""
#                         <div style="background:#161922; padding:20px; border-radius:15px; border-left: 5px solid #74b9ff; margin-top: 10px;">
#                             <h4 style="color:#74b9ff;">📐 Statistical Summary</h4>
#                             <p><b>Mean Score:</b> {avg_score:.4f}</p>
#                             <p><b>Median Score:</b> {median_score:.4f}</p>
#                             <p><b>Std Deviation:</b> {std_score:.4f}</p>
#                         </div>
#                     """, unsafe_allow_html=True)

#                 # =============================================
#                 # --- THE DETAILED INSIGHT REPORT ---
#                 # =============================================
#                 st.divider()
#                 st.header("📄 Executive Insight Report")

#                 # FIX: Pre-calculate the formatted averages to avoid the ValueError inside the f-string
#                 avg_pos_fmt = f"{df_raw[df_raw['Sentiment']=='Positive']['Compound_Score'].mean():.4f}" if pos > 0 else 'N/A'
#                 avg_neg_fmt = f"{df_raw[df_raw['Sentiment']=='Negative']['Compound_Score'].mean():.4f}" if neg > 0 else 'N/A'
#                 avg_neu_fmt = f"{df_raw[df_raw['Sentiment']=='Neutral']['Compound_Score'].mean():.4f}" if neu > 0 else 'N/A'

#                 st.markdown(f"""
#                     <div class="report-card">
#                         <h3 style="color:#a29bfe; margin-bottom: 16px;">🗂️ 1. Dataset Overview</h3>
#                         <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px;">
#                             <div><p style="color:#636e72; font-size:0.8rem; margin-bottom:2px;">SOURCE FILE</p><p style="font-weight:600;">{uploaded_file.name}</p></div>
#                             <div><p style="color:#636e72; font-size:0.8rem; margin-bottom:2px;">ANALYSIS COLUMN</p><p style="font-weight:600;">{target_col}</p></div>
#                             <div><p style="color:#636e72; font-size:0.8rem; margin-bottom:2px;">GENERATED AT</p><p style="font-weight:600;">{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p></div>
#                         </div>
#                     </div>
#                 """, unsafe_allow_html=True)

#                 overall_sentiment = "POSITIVE" if pos > neg and pos > neu else ("NEGATIVE" if neg > pos and neg > neu else "NEUTRAL")
#                 overall_color = "#00b894" if overall_sentiment == "POSITIVE" else ("#ff7675" if overall_sentiment == "NEGATIVE" else "#74b9ff")
                
#                 st.markdown(f"""
#                     <div class="report-card">
#                         <h3 style="color:#a29bfe; margin-bottom: 16px;">🎯 2. Sentiment Classification Results</h3>
#                         <div style="margin-bottom: 20px;">
#                             <span style="font-size:1rem; color:#636e72;">Overall Dataset Sentiment: </span>
#                             <span style="font-size:1.3rem; font-weight:800; color:{overall_color};">● {overall_sentiment}</span>
#                         </div>
#                         <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; text-align: center;">
#                             <div style="background: rgba(0,184,148,0.1); border: 1px solid rgba(0,184,148,0.3); border-radius:12px; padding: 20px;">
#                                 <p style="font-size: 2.2rem; font-weight: 800; color: #00b894; margin:0;">{pos:,}</p>
#                                 <p style="color: #00b894; font-weight: 600; margin:4px 0;">POSITIVE</p>
#                                 <p style="color:#636e72; font-size:0.85rem;">{(pos/total*100):.2f}% of total</p>
#                                 <p style="color:#636e72; font-size:0.8rem;">Avg Score: {avg_pos_fmt}</p>
#                             </div>
#                             <div style="background: rgba(255,118,117,0.1); border: 1px solid rgba(255,118,117,0.3); border-radius:12px; padding: 20px;">
#                                 <p style="font-size: 2.2rem; font-weight: 800; color: #ff7675; margin:0;">{neg:,}</p>
#                                 <p style="color: #ff7675; font-weight: 600; margin:4px 0;">NEGATIVE</p>
#                                 <p style="color:#636e72; font-size:0.85rem;">{(neg/total*100):.2f}% of total</p>
#                                 <p style="color:#636e72; font-size:0.8rem;">Avg Score: {avg_neg_fmt}</p>
#                             </div>
#                             <div style="background: rgba(116,185,255,0.1); border: 1px solid rgba(116,185,255,0.3); border-radius:12px; padding: 20px;">
#                                 <p style="font-size: 2.2rem; font-weight: 800; color: #74b9ff; margin:0;">{neu:,}</p>
#                                 <p style="color: #74b9ff; font-weight: 600; margin:4px 0;">NEUTRAL</p>
#                                 <p style="color:#636e72; font-size:0.85rem;">{(neu/total*100):.2f}% of total</p>
#                                 <p style="color:#636e72; font-size:0.8rem;">Avg Score: {avg_neu_fmt}</p>
#                             </div>
#                         </div>
#                     </div>
#                 """, unsafe_allow_html=True)

#                 # --- Statistics Deep Dive ---
#                 skewness = df_raw['Compound_Score'].skew()
#                 st.markdown(f"""
#                     <div class="report-card">
#                         <h3 style="color:#a29bfe; margin-bottom: 16px;">📐 3. Statistical Deep Dive</h3>
#                         <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px;">
#                             <div>
#                                 <p style="color:#a0a0a0;">Mean: {avg_score:.6f}</p>
#                                 <p style="color:#a0a0a0;">Median: {median_score:.6f}</p>
#                                 <p style="color:#a0a0a0;">Std Deviation: {std_score:.6f}</p>
#                                 <p style="color:#a0a0a0;">Skewness: {skewness:.4f}</p>
#                             </div>
#                         </div>
#                     </div>
#                 """, unsafe_allow_html=True)

#                 # --- Downloadable Text Report ---
#                 st.divider()
#                 st.subheader("📥 Export Report")
#                 report_text = f"SENTIENT AI REPORT\nFile: {uploaded_file.name}\nOverall: {overall_sentiment}\nPos: {pos}, Neg: {neg}, Neu: {neu}"
#                 col_btn1, col_btn2 = st.columns(2)
#                 col_btn1.download_button("📥 Download Full Text Report", report_text, "sentient_report.txt")
#                 col_btn2.download_button("📊 Export Analyzed Data (CSV)", df_raw.to_csv(index=False), "analyzed_sentiments.csv")

# # --- PAGE: HISTORY ---
# elif selected_nav == "History":
#     st.title("🕒 Analysis History")
#     if not st.session_state.history:
#         st.info("No analysis logs found for this session.")
#     else:
#         st.table(pd.DataFrame(st.session_state.history))
#         if st.button("🗑️ Clear History"):
#             st.session_state.history = []
#             st.rerun()

# # --- PAGE: DATA EXPLORER ---
# elif selected_nav == "Data Explorer":
#     st.title("📂 Data Explorer")
#     if st.session_state.analyzed_df is not None:
#         st.dataframe(st.session_state.analyzed_df, use_container_width=True)
#     elif uploaded_file:
#         st.dataframe(df_raw, use_container_width=True)
#     else:
#         st.info("Upload a file to explore the raw contents here.")



import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from streamlit_option_menu import option_menu
from datetime import datetime
import numpy as np

# Initialize NLTK VADER
nltk.download('vader_lexicon', quiet=True)
sid = SentimentIntensityAnalyzer()

# --- Multi-Language Dictionary ---
LANGS = {
    "English": {
        "home": "Home", 
        "dash": "Dashboard", 
        "hist": "History", 
        "expl": "Data Explorer",
        "welcome": "👋 Welcome to Sentient AI, the future of Data Interpretation.",
        "sub": "Beautifully crafted sentiment analysis for the modern industry.",
        "upload": "Upload Dataset", 
        "scope": "Analysis Scope", 
        "target": "Target Selection",
        "btn": "🚀 GENERATE ANALYSIS & REPORT", 
        "stat": "Status", 
        "report": "Executive Insight Report",
        "pos": "Positive", 
        "neg": "Negative", 
        "neu": "Neutral", 
        "rows": "Total Rows"
    },
    "French": {
        "home": "Accueil", 
        "dash": "Tableau de bord", 
        "hist": "Historique", 
        "expl": "Explorateur",
        "welcome": "👋 Bienvenue sur Sentient AI, l'avenir de l'interprétation des données.",
        "sub": "Analyse de sentiment magnifiquement conçue pour l'industrie moderne.",
        "upload": "Télécharger l'ensemble de données", 
        "scope": "Portée de l'analyse", 
        "target": "Sélection de la cible",
        "btn": "🚀 GÉNÉRER L'ANALYSE ET LE RAPPORT", 
        "stat": "Statut", 
        "report": "Rapport d'analyse exécutif",
        "pos": "Positif", 
        "neg": "Négatif", 
        "neu": "Neutre", 
        "rows": "Nombre total de lignes"
    },
    "Spanish": {
        "home": "Inicio", 
        "dash": "Panel", 
        "hist": "Historial", 
        "expl": "Explorador",
        "welcome": "👋 Bienvenido a Sentient AI, el futuro de la interpretación de datos.",
        "sub": "Análisis de sentimientos bellamente diseñado para la industria moderna.",
        "upload": "Subir base de datos", 
        "scope": "Alcance del análisis", 
        "target": "Selección de objetivo",
        "btn": "🚀 GENERAR ANÁLISIS E INFORME", 
        "stat": "Estado", 
        "report": "Informe de Perspectiva Ejecutiva",
        "pos": "Positivo", 
        "neg": "Negativo", 
        "neu": "Neutral", 
        "rows": "Filas totales"
    }
}

# --- UI Configuration & Styling ---
st.set_page_config(page_title="Sentient AI | Data Insights", layout="wide", page_icon="🌙")

if 'history' not in st.session_state: 
    st.session_state.history = []
if 'analyzed_df' not in st.session_state: 
    st.session_state.analyzed_df = None

st.markdown("""
    <style>
    .stApp { background-color: #0b0d11; color: #e0e0e0; }
    [data-testid="stSidebar"] { background-color: #12151c; border-right: 1px solid #1f232d; }
    h1, h2, h3 { color: #a29bfe; font-family: 'Inter', sans-serif; font-weight: 700; }
    .hero-title { font-size: 3rem; background: linear-gradient(to right, #a29bfe, #6c5ce7); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 800; }
    .stButton>button { width: 100%; border-radius: 12px; background: linear-gradient(45deg, #6c5ce7, #a29bfe); color: white; border: none; padding: 18px; font-weight: bold; transition: all 0.3s ease; cursor: pointer; }
    .stButton>button:hover { background: linear-gradient(45deg, #5a4bcf, #8b7ee8); transform: translateY(-2px); box-shadow: 0 8px 20px rgba(108, 92, 231, 0.4); }
    .stButton>button:active { transform: translateY(0px); }
    div[data-testid="stMetric"] { background: rgba(28, 31, 43, 0.8); border: 1px solid rgba(162, 155, 254, 0.2); border-radius: 15px; padding: 20px; }
    .report-card { background: rgba(22, 25, 34, 0.9); border: 1px solid rgba(162, 155, 254, 0.15); border-radius: 16px; padding: 24px; margin-bottom: 16px; }
    
    /* Sentiment Card Styling */
    .sentiment-card {
        background: rgba(28, 31, 43, 0.9);
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        border: 1px solid rgba(162, 155, 254, 0.2);
        transition: transform 0.3s ease;
    }
    .sentiment-card:hover {
        transform: translateY(-5px);
        border-color: rgba(162, 155, 254, 0.5);
    }
    .sentiment-emoji {
        font-size: 48px;
        margin-bottom: 10px;
    }
    .sentiment-count {
        font-size: 36px;
        font-weight: 800;
        margin: 10px 0;
    }
    .sentiment-percent {
        font-size: 20px;
        color: #a29bfe;
        font-weight: 600;
    }
    .sentiment-label {
        font-size: 18px;
        color: #888;
        margin-top: 10px;
    }
    .positive { color: #00b894; }
    .negative { color: #ff7675; }
    .neutral { color: #74b9ff; }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.markdown('<div style="text-align: center;"><img src="https://cdn-icons-png.flaticon.com/512/2103/2103633.png" width="70" style="filter: invert(80%);"><h2>SENTIENT AI</h2></div>', unsafe_allow_html=True)
    lang_choice = st.selectbox("🌐 Language", ["English", "French", "Spanish"])
    curr_lang = LANGS[lang_choice]

    selected_nav = option_menu(None, [curr_lang["home"], curr_lang["dash"], curr_lang["hist"], curr_lang["expl"]], 
        icons=["house", "speedometer2", "clock-history", "table"], 
        default_index=0, 
        styles={"nav-link-selected": {"background-color": "#6c5ce7"}})

    st.divider()
    uploaded_file = st.file_uploader(curr_lang["upload"], type=["csv", "xlsx"])
    
    if uploaded_file:
        if uploaded_file.name.endswith('csv'):
            df_raw = pd.read_csv(uploaded_file, on_bad_lines='skip', engine='python')
        else:
            df_raw = pd.read_excel(uploaded_file)
        
        st.subheader(curr_lang["scope"])
        analysis_mode = st.radio(curr_lang["target"], ["Whole Dataset", "Specific Column"])
        
        if analysis_mode == "Specific Column":
            target_col = st.selectbox("Select Column:", df_raw.columns)
        else:
            target_col = df_raw.select_dtypes(include=['object']).columns[0]
        
        st.subheader("Visual Studio")
        chart_type = st.selectbox("Graph Type", ["Donut Chart", "Bar Graph", "Scatter Plot", "Heatmap", "Combo Graph", "Histogram (Density)"])
        accent_color = st.color_picker("Theme Color", "#a29bfe")

# --- Main Logic ---
if selected_nav == curr_lang["home"]:
    st.markdown(f'<h1 class="hero-title">{curr_lang["welcome"]}</h1>', unsafe_allow_html=True)
    st.write(f"### {curr_lang['sub']}")
    st.image("https://images.unsplash.com/photo-1677442136019-21780ecad995?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80", use_container_width=True)

elif selected_nav == curr_lang["dash"]:
    if not uploaded_file:
        st.info("👋 Please upload a data file in the sidebar to begin your journey.")
    else:
        st.title(f"✨ {curr_lang['dash']}")
        
        if st.button(curr_lang["btn"]):
            with st.spinner("AI is interpreting your data..."):
                # Sentiment Analysis Engine
                def get_all_scores(text):
                    s = sid.polarity_scores(str(text))
                    return s['pos'], s['neg'], s['neu'], s['compound']

                df_raw[['Pos_Score', 'Neg_Score', 'Neu_Score', 'Compound_Score']] = df_raw[target_col].apply(lambda x: pd.Series(get_all_scores(x)))
                df_raw['Sentiment'] = df_raw['Compound_Score'].apply(lambda x: 'Positive' if x >= 0.05 else ('Negative' if x <= -0.05 else 'Neutral'))
                df_raw['Index'] = range(len(df_raw))
                st.session_state.analyzed_df = df_raw

                total = len(df_raw)
                counts = df_raw['Sentiment'].value_counts()
                pos = counts.get('Positive', 0)
                neg = counts.get('Negative', 0)
                neu = counts.get('Neutral', 0)
                avg_score = df_raw['Compound_Score'].mean()

                # Dashboard Top Row Metrics
                m1, m2, m3, m4 = st.columns(4)
                m1.metric(curr_lang["rows"], total)
                m2.metric(curr_lang["pos"], f"{(pos/total*100):.1f}%")
                m3.metric(curr_lang["neg"], f"{(neg/total*100):.1f}%")
                m4.metric("Avg Score", f"{avg_score:.2f}")

                st.divider()

                # Sentiment Classification Results as Cards
                st.subheader("📊 Sentiment Classification Results")
                
                card_col1, card_col2, card_col3 = st.columns(3)
                
                with card_col1:
                    st.markdown(f"""
                        <div class="sentiment-card">
                            <div class="sentiment-emoji">😊</div>
                            <div class="sentiment-count positive">{pos:,}</div>
                            <div class="sentiment-percent">{(pos/total*100):.1f}%</div>
                            <div class="sentiment-label">POSITIVE</div>
                        </div>
                    """, unsafe_allow_html=True)
                
                with card_col2:
                    st.markdown(f"""
                        <div class="sentiment-card">
                            <div class="sentiment-emoji">😞</div>
                            <div class="sentiment-count negative">{neg:,}</div>
                            <div class="sentiment-percent">{(neg/total*100):.1f}%</div>
                            <div class="sentiment-label">NEGATIVE</div>
                        </div>
                    """, unsafe_allow_html=True)
                
                with card_col3:
                    st.markdown(f"""
                        <div class="sentiment-card">
                            <div class="sentiment-emoji">😐</div>
                            <div class="sentiment-count neutral">{neu:,}</div>
                            <div class="sentiment-percent">{(neu/total*100):.1f}%</div>
                            <div class="sentiment-label">NEUTRAL</div>
                        </div>
                    """, unsafe_allow_html=True)

                st.divider()

                # Score Distribution by Sentiment Category as Graph
                st.subheader("📈 Score Distribution by Sentiment Category")
                
                fig_dist = px.box(df_raw, x='Sentiment', y='Compound_Score', color='Sentiment',
                                  color_discrete_map={'Positive':'#00b894', 'Negative':'#ff7675', 'Neutral':'#74b9ff'},
                                  title="Compound Score Distribution by Sentiment Category")
                fig_dist.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
                                       font_color="white", template="plotly_dark", height=500)
                st.plotly_chart(fig_dist, use_container_width=True)
                
                st.divider()

                # Visualization Dashboard
                st.subheader("🎨 Visualization Dashboard")
                c1, c2 = st.columns([2, 1])
                
                with c1:
                    color_map = {'Positive':'#00b894', 'Negative':'#ff7675', 'Neutral':'#74b9ff'}
                    
                    if chart_type == "Donut Chart":
                        fig = px.pie(df_raw, names='Sentiment', hole=0.6, color='Sentiment', color_discrete_map=color_map)
                    elif chart_type == "Bar Graph":
                        fig = px.bar(counts.reset_index(), x='Sentiment', y='count', color='Sentiment', color_discrete_map=color_map)
                    elif chart_type == "Scatter Plot":
                        fig = px.scatter(df_raw, x='Index', y='Compound_Score', color='Sentiment', 
                                        color_discrete_map=color_map, title="Sentiment Distribution per Record")
                    elif chart_type == "Heatmap":
                        corr = df_raw[['Pos_Score', 'Neg_Score', 'Neu_Score', 'Compound_Score']].corr()
                        fig = px.imshow(corr, text_auto=True, aspect="auto", color_continuous_scale='RdBu_r', 
                                       title="Metric Correlation Heatmap")
                    elif chart_type == "Combo Graph":
                        fig = go.Figure()
                        fig.add_trace(go.Bar(x=counts.index, y=counts.values, name="Counts", marker_color="#6c5ce7"))
                        fig.add_trace(go.Scatter(x=counts.index, y=counts.values, mode='lines+markers', 
                                                name="Trend", line=dict(color="#00b894", width=4)))
                    else:
                        fig = px.histogram(df_raw, x='Compound_Score', nbins=20, color='Sentiment', 
                                          color_discrete_map=color_map)
                    
                    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
                                     font_color="white", template="plotly_dark", height=450)
                    st.plotly_chart(fig, use_container_width=True)

                with c2:
                    st.subheader("🤖 AI Interpretation")
                    status = "Favorable ✅" if pos > neg else "Action Required ⚠️"
                    st.markdown(f"""
                        <div style="background:#161922; padding:20px; border-radius:15px; border-left: 5px solid {accent_color};">
                            <h4 style="color:{accent_color}">Status: {status}</h4>
                            <p>Our AI analysis of <b>{target_col}</b> indicates a <b>{"positive" if pos > neg else "negative"}</b> bias in the dataset.</p>
                            <hr style="opacity:0.2">
                            <small>📊 {pos} positive | {neg} negative | {neu} neutral</small>
                        </div>
                    """, unsafe_allow_html=True)

                st.divider()

                # Executive Summary as Markdown
                st.subheader("📄 Executive Summary")
                
                avg_pos = df_raw[df_raw['Sentiment']=='Positive']['Compound_Score'].mean() if pos > 0 else 0
                avg_neg = df_raw[df_raw['Sentiment']=='Negative']['Compound_Score'].mean() if neg > 0 else 0
                
                md_report = f"""
## 📑 Sentiment Analysis Report

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  
**File:** `{uploaded_file.name}`  
**Analyzed Column:** `{target_col}`  

---



### 🎯 Classification Breakdown

| Category | Count | Percentage |
|:---|---|---:|
| Positive 😊 | {pos:,} | {pos/total*100:.2f}% |
| Negative 😞 | {neg:,} | {neg/total*100:.2f}% |
| Neutral 😐 | {neu:,} | {neu/total*100:.2f}% |

---

### 💡 Strategic Recommendations

#### 1. SENTIMENT OPTIMIZATION STRATEGY
   • Focus on addressing the {neg} negative entries ({neg/total*100:.1f}%) to improve brand perception
   • Leverage the {pos} positive testimonials ({pos/total*100:.1f}%) for marketing campaigns
   • Target the {neu} neutral users ({neu/total*100:.1f}%) with engagement activities

#### 2. OPERATIONAL ACTIONS
   • Implement feedback loops for negative responses within 24 hours
   • Create case studies from top positive feedback examples
   • Deploy automated surveys for neutral responses to gather more data

#### 3. MONITORING & MEASUREMENT
   • Set up weekly sentiment tracking dashboard
   • Establish baseline metrics for future comparison
   • Create alert thresholds for negative sentiment spikes

#### 4. LONG-TERM RECOMMENDATIONS
   • Integrate sentiment analysis into product development cycle
   • Train customer-facing teams on sentiment response protocols
   • Develop automated reporting system for stakeholders

---


"""
                
                st.markdown(f'<div class="report-card">{md_report}</div>', unsafe_allow_html=True)

                # Export Section
                st.divider()
                st.subheader("📥 Export Results")
                col_ex1, col_ex2 = st.columns(2)
                
                col_ex1.download_button(
                    label="💾 Download Executive Report (.txt)",
                    data=md_report,
                    file_name=f"sentient_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                    mime="text/markdown",
                    use_container_width=True
                )
                
                csv_data = df_raw.to_csv(index=False).encode('utf-8')
                col_ex2.download_button(
                    label="📊 Download Analyzed Data (.csv)",
                    data=csv_data,
                    file_name=f"analyzed_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv",
                    use_container_width=True
                )
                
                # Add to history
                st.session_state.history.append({
                    "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "File": uploaded_file.name,
                    "Column": target_col,
                    "Positive": f"{pos} ({pos/total*100:.1f}%)",
                    "Negative": f"{neg} ({neg/total*100:.1f}%)",
                    "Neutral": f"{neu} ({neu/total*100:.1f}%)"
                })

elif selected_nav == curr_lang["hist"]:
    st.title("🕒 Session History")
    if len(st.session_state.history) > 0:
        history_df = pd.DataFrame(st.session_state.history)
        st.dataframe(history_df, use_container_width=True)
        if st.button("🗑️ Clear History"):
            st.session_state.history = []
            st.rerun()
    else:
        st.info("No analysis logs found for this session. Run an analysis to see history here.")

elif selected_nav == curr_lang["expl"]:
    st.title("📂 Data Explorer")
    if st.session_state.analyzed_df is not None:
        st.dataframe(st.session_state.analyzed_df, use_container_width=True)
        csv_data = st.session_state.analyzed_df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Current Data as CSV", csv_data, "current_analysis_data.csv", "text/csv")
    elif uploaded_file:
        st.dataframe(df_raw, use_container_width=True)
    else:
        st.info("Upload data to explore or run an analysis first.")

# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# import nltk
# from streamlit_option_menu import option_menu
# from datetime import datetime
# import numpy as np
# from wordcloud import WordCloud


# # Initialize NLTK VADER
# nltk.download('vader_lexicon', quiet=True)
# sid = SentimentIntensityAnalyzer()

# # ─────────────────────────────────────────────
# # MULTI-LANGUAGE DICTIONARY
# # ─────────────────────────────────────────────
# LANG = {
#     "English": {
#         "nav": ["Home", "Dashboard", "History", "Data Explorer"],
#         "upload": "Upload Dataset",
#         "scope": "Analysis Scope",
#         "target": "Target Selection",
#         "whole": "Whole Dataset",
#         "specific": "Specific Column",
#         "sel_col": "Select Column:",
#         "visual": "Visual Studio",
#         "graph": "Choose Graph Type",
#         "color": "Report Theme Color",
#         "hero": "👋 Welcome to Sentient AI, the future of Data Interpretation.",
#         "sub": "### Beautifully crafted sentiment analysis for the modern industry.",
#         "caption": "Powered by Sentient AI Deep Logic",
#         "upload_prompt": "👋 Please upload a data file in the sidebar to begin your journey.",
#         "dash_title": "✨ Project Dashboard",
#         "gen_btn": "🚀 GENERATE ANALYSIS & REPORT",
#         "spinner": "AI is interpreting your data...",
#         "rows": "Rows", "pos": "Positive", "neg": "Negative", "neu": "Neutral",
#         "approval": "High Approval", "critical": "-Critical",
#         "results": "Results:",
#         "ai_interp": "AI Interpretation",
#         "favorable": "Favorable", "action": "Action Required",
#         "pos_bias": "strong positive bias", "neg_trend": "noticeable negative trend",
#         "data_src": "Data Source:",
#         "box_title": "📊 Score Distribution by Sentiment Category",
#         "stat_sum": "📐 Statistical Summary",
#         "mean": "Mean Score", "median": "Median Score", "std": "Std Deviation",
#         "report_hdr": "📄 Executive Insight Report",
#         "sec1": "🗂️ 1. Dataset Overview",
#         "src_file": "SOURCE FILE", "ana_col": "ANALYSIS COLUMN", "gen_at": "GENERATED AT",
#         "total_rec": "TOTAL RECORDS", "total_col": "TOTAL COLUMNS", "engine": "ENGINE",
#         "sec2": "🎯 2. Sentiment Classification Results",
#         "overall_lbl": "Overall Dataset Sentiment:",
#         "sec3": "📐 3. Statistical Deep Dive",
#         "score_stats": "COMPOUND SCORE STATISTICS",
#         "min": "Min Score", "max": "Max Score",
#         "q1": "Q1 (25th pct)", "q3": "Q3 (75th pct)", "iqr": "IQR",
#         "skew": "Skewness", "kurt": "Kurtosis",
#         "intensity": "INTENSITY BANDS",
#         "str_pos": "Strongly Positive (≥0.5):",
#         "str_neg": "Strongly Negative (≤−0.5):",
#         "mod_band": "Moderate Band (−0.5 to 0.5):",
#         "entries": "entries",
#         "left_skew": "⚠️ Left-skewed distribution — more negative outliers present.",
#         "right_skew": "⚠️ Right-skewed distribution — more positive outliers present.",
#         "sym": "✅ Distribution is approximately symmetric.",
#         "sec4": "📝 4. Text Complexity Analysis",
#         "avg_w": "Avg Words / Entry", "max_w": "Max Words", "min_w": "Min Words", "tot_w": "Total Words",
#         "sec5": "💡 5. AI-Powered Recommendations",
#         "rec1_title": "🔴 High Negative Sentiment Detected",
#         "rec1_body": "% of entries are negative. Investigate root causes and implement targeted improvement strategies.",
#         "rec2_title": "🟡 High Neutral Volume",
#         "rec2_body": "% neutral. Convert neutral sentiment to positive through improved engagement.",
#         "rec3_title": "🟢 Strong Positive Performance",
#         "rec3_body": "% positive. Strategy is working — maintain engagement and explore expansion.",
#         "rec4_title": "📊 Skewed Distribution",
#         "rec4_body": "Consider segmenting analysis by subgroup for deeper insights.",
#         "rec5_title": "✅ Balanced Sentiment Profile",
#         "rec5_body": "Balanced distribution detected. Continue monitoring trends over time.",
#         "export_hdr": "📥 Export Report",
#         "dl_report": "📥 Download Full Text Report",
#         "dl_csv": "📊 Export Analyzed Data (CSV)",
#         "hist_title": "🕒 Analysis History",
#         "no_hist": "No analysis logs found for this session.",
#         "clr_hist": "🗑️ Clear History",
#         "exp_title": "📂 Data Explorer",
#         "exp_prompt": "Upload a file to explore the raw contents here.",
#         "lang_label": "🌐 Language",
#     },
#     "French 🇫🇷": {
#         "nav": ["Accueil", "Tableau de bord", "Historique", "Explorateur"],
#         "upload": "Télécharger un fichier",
#         "scope": "Portée de l'analyse",
#         "target": "Sélection de cible",
#         "whole": "Jeu de données entier",
#         "specific": "Colonne spécifique",
#         "sel_col": "Sélectionner une colonne :",
#         "visual": "Studio visuel",
#         "graph": "Type de graphique",
#         "color": "Couleur du rapport",
#         "hero": "👋 Bienvenue sur Sentient AI, l'avenir de l'interprétation des données.",
#         "sub": "### Analyse de sentiment élégante pour l'industrie moderne.",
#         "caption": "Propulsé par Sentient AI Deep Logic",
#         "upload_prompt": "👋 Veuillez télécharger un fichier dans la barre latérale pour commencer.",
#         "dash_title": "✨ Tableau de bord du projet",
#         "gen_btn": "🚀 GÉNÉRER L'ANALYSE ET LE RAPPORT",
#         "spinner": "L'IA interprète vos données...",
#         "rows": "Lignes", "pos": "Positif", "neg": "Négatif", "neu": "Neutre",
#         "approval": "Haute approbation", "critical": "-Critique",
#         "results": "Résultats :",
#         "ai_interp": "Interprétation IA",
#         "favorable": "Favorable", "action": "Action requise",
#         "pos_bias": "forte tendance positive", "neg_trend": "tendance négative notable",
#         "data_src": "Source de données :",
#         "box_title": "📊 Distribution des scores par catégorie",
#         "stat_sum": "📐 Résumé statistique",
#         "mean": "Score moyen", "median": "Score médian", "std": "Écart-type",
#         "report_hdr": "📄 Rapport d'analyse exécutif",
#         "sec1": "🗂️ 1. Aperçu du jeu de données",
#         "src_file": "FICHIER SOURCE", "ana_col": "COLONNE ANALYSÉE", "gen_at": "GÉNÉRÉ LE",
#         "total_rec": "TOTAL ENREGISTREMENTS", "total_col": "TOTAL COLONNES", "engine": "MOTEUR",
#         "sec2": "🎯 2. Résultats de classification des sentiments",
#         "overall_lbl": "Sentiment général :",
#         "sec3": "📐 3. Analyse statistique approfondie",
#         "score_stats": "STATISTIQUES DU SCORE",
#         "min": "Score min", "max": "Score max",
#         "q1": "Q1 (25e pct)", "q3": "Q3 (75e pct)", "iqr": "IQR",
#         "skew": "Asymétrie", "kurt": "Kurtosis",
#         "intensity": "BANDES D'INTENSITÉ",
#         "str_pos": "Fortement positif (≥0.5) :",
#         "str_neg": "Fortement négatif (≤−0.5) :",
#         "mod_band": "Bande modérée (−0.5 à 0.5) :",
#         "entries": "entrées",
#         "left_skew": "⚠️ Distribution asymétrique à gauche — plus d'anomalies négatives.",
#         "right_skew": "⚠️ Distribution asymétrique à droite — plus d'anomalies positives.",
#         "sym": "✅ Distribution approximativement symétrique.",
#         "sec4": "📝 4. Analyse de la complexité du texte",
#         "avg_w": "Mots moy. / Entrée", "max_w": "Mots max", "min_w": "Mots min", "tot_w": "Total mots",
#         "sec5": "💡 5. Recommandations IA",
#         "rec1_title": "🔴 Sentiment négatif élevé détecté",
#         "rec1_body": "% des entrées sont négatives. Investiguer les causes profondes.",
#         "rec2_title": "🟡 Volume neutre élevé",
#         "rec2_body": "% neutre. Convertir le sentiment neutre en positif.",
#         "rec3_title": "🟢 Excellente performance positive",
#         "rec3_body": "% positif. Maintenir l'engagement et explorer l'expansion.",
#         "rec4_title": "📊 Distribution asymétrique",
#         "rec4_body": "Envisager de segmenter l'analyse par sous-groupe.",
#         "rec5_title": "✅ Profil de sentiment équilibré",
#         "rec5_body": "Distribution équilibrée. Continuer à surveiller les tendances.",
#         "export_hdr": "📥 Exporter le rapport",
#         "dl_report": "📥 Télécharger le rapport",
#         "dl_csv": "📊 Exporter les données (CSV)",
#         "hist_title": "🕒 Historique des analyses",
#         "no_hist": "Aucun journal d'analyse pour cette session.",
#         "clr_hist": "🗑️ Effacer l'historique",
#         "exp_title": "📂 Explorateur de données",
#         "exp_prompt": "Téléchargez un fichier pour explorer son contenu ici.",
#         "lang_label": "🌐 Langue",
#     },
#     "Spanish 🇪🇸": {
#         "nav": ["Inicio", "Panel", "Historial", "Explorador"],
#         "upload": "Cargar conjunto de datos",
#         "scope": "Alcance del análisis",
#         "target": "Selección de objetivo",
#         "whole": "Todo el conjunto de datos",
#         "specific": "Columna específica",
#         "sel_col": "Seleccionar columna:",
#         "visual": "Estudio visual",
#         "graph": "Tipo de gráfico",
#         "color": "Color del tema",
#         "hero": "👋 Bienvenido a Sentient AI, el futuro de la interpretación de datos.",
#         "sub": "### Análisis de sentimiento diseñado para la industria moderna.",
#         "caption": "Impulsado por Sentient AI Deep Logic",
#         "upload_prompt": "👋 Por favor cargue un archivo en la barra lateral para comenzar.",
#         "dash_title": "✨ Panel del proyecto",
#         "gen_btn": "🚀 GENERAR ANÁLISIS E INFORME",
#         "spinner": "La IA está interpretando sus datos...",
#         "rows": "Filas", "pos": "Positivo", "neg": "Negativo", "neu": "Neutro",
#         "approval": "Alta aprobación", "critical": "-Crítico",
#         "results": "Resultados:",
#         "ai_interp": "Interpretación IA",
#         "favorable": "Favorable", "action": "Acción requerida",
#         "pos_bias": "fuerte sesgo positivo", "neg_trend": "tendencia negativa notable",
#         "data_src": "Fuente de datos:",
#         "box_title": "📊 Distribución de puntuaciones por categoría",
#         "stat_sum": "📐 Resumen estadístico",
#         "mean": "Puntuación media", "median": "Puntuación mediana", "std": "Desviación estándar",
#         "report_hdr": "📄 Informe ejecutivo de análisis",
#         "sec1": "🗂️ 1. Descripción general del conjunto de datos",
#         "src_file": "ARCHIVO FUENTE", "ana_col": "COLUMNA ANALIZADA", "gen_at": "GENERADO EL",
#         "total_rec": "TOTAL REGISTROS", "total_col": "TOTAL COLUMNAS", "engine": "MOTOR",
#         "sec2": "🎯 2. Resultados de clasificación de sentimientos",
#         "overall_lbl": "Sentimiento general del conjunto de datos:",
#         "sec3": "📐 3. Análisis estadístico detallado",
#         "score_stats": "ESTADÍSTICAS DE PUNTUACIÓN",
#         "min": "Puntuación mín", "max": "Puntuación máx",
#         "q1": "Q1 (percentil 25)", "q3": "Q3 (percentil 75)", "iqr": "IQR",
#         "skew": "Asimetría", "kurt": "Curtosis",
#         "intensity": "BANDAS DE INTENSIDAD",
#         "str_pos": "Fuertemente positivo (≥0.5):",
#         "str_neg": "Fuertemente negativo (≤−0.5):",
#         "mod_band": "Banda moderada (−0.5 a 0.5):",
#         "entries": "entradas",
#         "left_skew": "⚠️ Distribución sesgada a la izquierda — más valores atípicos negativos.",
#         "right_skew": "⚠️ Distribución sesgada a la derecha — más valores atípicos positivos.",
#         "sym": "✅ Distribución aproximadamente simétrica.",
#         "sec4": "📝 4. Análisis de complejidad del texto",
#         "avg_w": "Palabras prom. / Entrada", "max_w": "Palabras máx", "min_w": "Palabras mín", "tot_w": "Total palabras",
#         "sec5": "💡 5. Recomendaciones de IA",
#         "rec1_title": "🔴 Alto sentimiento negativo detectado",
#         "rec1_body": "% de entradas son negativas. Investigar causas raíz.",
#         "rec2_title": "🟡 Alto volumen neutro",
#         "rec2_body": "% neutre. Convertir sentimiento neutro en positivo.",
#         "rec3_title": "🟢 Fuerte desempeño positivo",
#         "rec3_body": "% positivo. Mantener el compromiso y explorar la expansión.",
#         "rec4_title": "📊 Distribución sesgada",
#         "rec4_body": "Considere segmentar el análisis por subgrupo.",
#         "rec5_title": "✅ Perfil de sentimiento equilibrado",
#         "rec5_body": "Distribución equilibrada. Seguir monitoreando las tendencias.",
#         "export_hdr": "📥 Exportar informe",
#         "dl_report": "📥 Descargar informe completo",
#         "dl_csv": "📊 Exportar datos analizados (CSV)",
#         "hist_title": "🕒 Historial de análisis",
#         "no_hist": "No se encontraron registros de análisis para esta sesión.",
#         "clr_hist": "🗑️ Borrar historial",
#         "exp_title": "📂 Explorador de datos",
#         "exp_prompt": "Cargue un archivo para explorar el contenido aquí.",
#         "lang_label": "🌐 Idioma",
#     },
#     "German 🇩🇪": {
#         "nav": ["Startseite", "Dashboard", "Verlauf", "Daten-Explorer"],
#         "upload": "Datensatz hochladen",
#         "scope": "Analysebereich",
#         "target": "Zielauswahl",
#         "whole": "Gesamter Datensatz",
#         "specific": "Bestimmte Spalte",
#         "sel_col": "Spalte auswählen:",
#         "visual": "Visuelles Studio",
#         "graph": "Diagrammtyp",
#         "color": "Berichtsfarbe",
#         "hero": "👋 Willkommen bei Sentient AI, der Zukunft der Dateninterpretation.",
#         "sub": "### Stimmungsanalyse für die moderne Industrie.",
#         "caption": "Angetrieben von Sentient AI Deep Logic",
#         "upload_prompt": "👋 Bitte laden Sie eine Datei in der Seitenleiste hoch.",
#         "dash_title": "✨ Projekt-Dashboard",
#         "gen_btn": "🚀 ANALYSE & BERICHT ERSTELLEN",
#         "spinner": "KI interpretiert Ihre Daten...",
#         "rows": "Zeilen", "pos": "Positiv", "neg": "Negativ", "neu": "Neutral",
#         "approval": "Hohe Zustimmung", "critical": "-Kritisch",
#         "results": "Ergebnisse:",
#         "ai_interp": "KI-Interpretation",
#         "favorable": "Günstig", "action": "Handlung erforderlich",
#         "pos_bias": "starke positive Tendenz", "neg_trend": "negativer Trend",
#         "data_src": "Datenquelle:",
#         "box_title": "📊 Score-Verteilung nach Stimmungskategorie",
#         "stat_sum": "📐 Statistische Zusammenfassung",
#         "mean": "Mittlerer Score", "median": "Medianer Score", "std": "Standardabweichung",
#         "report_hdr": "📄 Führungsbericht",
#         "sec1": "🗂️ 1. Datensatz-Übersicht",
#         "src_file": "QUELLDATEI", "ana_col": "ANALYSIERTE SPALTE", "gen_at": "ERSTELLT AM",
#         "total_rec": "DATENSÄTZE GESAMT", "total_col": "SPALTEN GESAMT", "engine": "ENGINE",
#         "sec2": "🎯 2. Stimmungsklassifizierungsergebnisse",
#         "overall_lbl": "Gesamtstimmung des Datensatzes:",
#         "sec3": "📐 3. Statistische Tiefenanalyse",
#         "score_stats": "SCORE-STATISTIKEN",
#         "min": "Min-Score", "max": "Max-Score",
#         "q1": "Q1 (25. Perzentil)", "q3": "Q3 (75. Perzentil)", "iqr": "IQR",
#         "skew": "Schiefe", "kurt": "Kurtosis",
#         "intensity": "INTENSITÄTSBÄNDER",
#         "str_pos": "Stark positiv (≥0.5):",
#         "str_neg": "Stark negativ (≤−0.5):",
#         "mod_band": "Moderates Band (−0.5 bis 0.5):",
#         "entries": "Einträge",
#         "left_skew": "⚠️ Linksschiefe Verteilung — mehr negative Ausreißer.",
#         "right_skew": "⚠️ Rechtsschiefe Verteilung — mehr positive Ausreißer.",
#         "sym": "✅ Verteilung ist annähernd symmetrisch.",
#         "sec4": "📝 4. Textkomplexitätsanalyse",
#         "avg_w": "Ø Wörter / Eintrag", "max_w": "Max Wörter", "min_w": "Min Wörter", "tot_w": "Wörter gesamt",
#         "sec5": "💡 5. KI-Empfehlungen",
#         "rec1_title": "🔴 Hohe negative Stimmung erkannt",
#         "rec1_body": "% der Einträge sind negativ. Ursachen untersuchen.",
#         "rec2_title": "🟡 Hohes neutrales Volumen",
#         "rec2_body": "% neutral. Neutrale Stimmung in positive umwandeln.",
#         "rec3_title": "🟢 Starke positive Leistung",
#         "rec3_body": "% positiv. Engagement aufrechterhalten und Expansion erkunden.",
#         "rec4_title": "📊 Schiefe Verteilung",
#         "rec4_body": "Analyse nach Untergruppen segmentieren.",
#         "rec5_title": "✅ Ausgeglichenes Stimmungsprofil",
#         "rec5_body": "Ausgeglichene Verteilung. Trends weiter beobachten.",
#         "export_hdr": "📥 Bericht exportieren",
#         "dl_report": "📥 Vollständigen Bericht herunterladen",
#         "dl_csv": "📊 Analysierte Daten exportieren (CSV)",
#         "hist_title": "🕒 Analyseverlauf",
#         "no_hist": "Keine Analyseprotokolle für diese Sitzung.",
#         "clr_hist": "🗑️ Verlauf löschen",
#         "exp_title": "📂 Daten-Explorer",
#         "exp_prompt": "Laden Sie eine Datei hoch, um deren Inhalt hier zu erkunden.",
#         "lang_label": "🌐 Sprache",
#     },
#     "Portuguese 🇧🇷": {
#         "nav": ["Início", "Painel", "Histórico", "Explorador"],
#         "upload": "Carregar conjunto de dados",
#         "scope": "Escopo da análise",
#         "target": "Seleção de alvo",
#         "whole": "Todo o conjunto de datos",
#         "specific": "Coluna específica",
#         "sel_col": "Selecionar coluna:",
#         "visual": "Estúdio visual",
#         "graph": "Tipo de gráfico",
#         "color": "Cor do tema",
#         "hero": "👋 Bem-vindo ao Sentient AI, o futuro da interpretação de dados.",
#         "sub": "### Análise de sentimento para a indústria moderna.",
#         "caption": "Impulsionado pelo Sentient AI Deep Logic",
#         "upload_prompt": "👋 Por favor carregue um ficheiro na barra lateral para começar.",
#         "dash_title": "✨ Painel do projeto",
#         "gen_btn": "🚀 GERAR ANÁLISE E RELATÓRIO",
#         "spinner": "A IA está a interpretar os seus dados...",
#         "rows": "Linhas", "pos": "Positivo", "neg": "Negativo", "neu": "Neutro",
#         "approval": "Alta aprovação", "critical": "-Crítico",
#         "results": "Resultados:",
#         "ai_interp": "Interpretação IA",
#         "favorable": "Favorável", "action": "Ação necessária",
#         "pos_bias": "forte tendência positiva", "neg_trend": "tendência negativa notável",
#         "data_src": "Fonte de dados:",
#         "box_title": "📊 Distribuição de pontuações por categoria",
#         "stat_sum": "📐 Resumo estatístico",
#         "mean": "Pontuação média", "median": "Pontuação mediana", "std": "Desvio padrão",
#         "report_hdr": "📄 Relatório executivo",
#         "sec1": "🗂️ 1. Visão geral do conjunto de dados",
#         "src_file": "FICHEIRO FONTE", "ana_col": "COLUNA ANALISADA", "gen_at": "GERADO EM",
#         "total_rec": "TOTAL REGISTOS", "total_col": "TOTAL COLUNAS", "engine": "MOTOR",
#         "sec2": "🎯 2. Resultados da classificação de sentimentos",
#         "overall_lbl": "Sentimento geral do conjunto de dados:",
#         "sec3": "📐 3. Análise estatística detalhada",
#         "score_stats": "ESTATÍSTICAS DE PUNTUAÇÃO",
#         "min": "Pontuação mín", "max": "Pontuação máx",
#         "q1": "Q1 (percentil 25)", "q3": "Q3 (percentil 75)", "iqr": "IQR",
#         "skew": "Assimetria", "kurt": "Curtose",
#         "intensity": "BANDAS DE INTENSIDADE",
#         "str_pos": "Fortemente positivo (≥0.5):",
#         "str_neg": "Fortemente negativo (≤−0.5):",
#         "mod_band": "Banda moderada (−0.5 a 0.5):",
#         "entries": "entradas",
#         "left_skew": "⚠️ Distribuição assimétrica à esquerda — mais valores atípicos negativos.",
#         "right_skew": "⚠️ Distribuição assimétrica à direita — mais valores atípicos positivos.",
#         "sym": "✅ Distribuição aproximadamente simétrica.",
#         "sec4": "📝 4. Análise de complexidade do texto",
#         "avg_w": "Palavras méd. / Entrada", "max_w": "Palavras máx", "min_w": "Palavras mín", "tot_w": "Total palavras",
#         "sec5": "💡 5. Recomendações de IA",
#         "rec1_title": "🔴 Alto sentimento negativo detectado",
#         "rec1_body": "% das entradas são negativas. Investigar causas raiz.",
#         "rec2_title": "🟡 Alto volume neutro",
#         "rec2_body": "% neutro. Converter sentimento neutro em positivo.",
#         "rec3_title": "🟢 Forte desempenho positivo",
#         "rec3_body": "% positivo. Manter o envolvimento e explorar a expansão.",
#         "rec4_title": "📊 Distribuição assimétrica",
#         "rec4_body": "Considere segmentar a análise por subgrupo.",
#         "rec5_title": "✅ Perfil de sentimento equilibrado",
#         "rec5_body": "Distribuição equilibrada. Continue monitorando as tendências.",
#         "export_hdr": "📥 Exportar relatório",
#         "dl_report": "📥 Descarregar relatório completo",
#         "dl_csv": "📊 Exportar dados analisados (CSV)",
#         "hist_title": "🕒 Histórico de análises",
#         "no_hist": "Nenhum registo de análise encontrado para esta sessão.",
#         "clr_hist": "🗑️ Limpar histórico",
#         "exp_title": "📂 Explorador de dados",
#         "exp_prompt": "Carregue um ficheiro para explorar o conteúdo aqui.",
#         "lang_label": "🌐 Idioma",
#     },
# }

# # --- 1. UI Configuration & Dark Serene Styling ---
# st.set_page_config(page_title="Sentient AI | Data Insights", layout="wide", page_icon="🌙")

# # Initialize Session State for History & Data
# if 'history' not in st.session_state:
#     st.session_state.history = []
# if 'analyzed_df' not in st.session_state:
#     st.session_state.analyzed_df = None
# if 'lang' not in st.session_state:
#     st.session_state.lang = "English"

# # Custom CSS for Premium Dark Mode
# st.markdown("""
#     <style>
#     /* Dark Theme Core */
#     .stApp {
#         background-color: #0b0d11;
#         color: #e0e0e0;
#     }
#     [data-testid="stSidebar"] {
#         background-color: #12151c;
#         border-right: 1px solid #1f232d;
#     }
    
#     /* Professional Headers & Gradient Text */
#     h1, h2, h3 {
#         color: #a29bfe;
#         font-family: 'Inter', sans-serif;
#         font-weight: 700;
#     }
#     .hero-title {
#         font-size: 3rem;
#         background: linear-gradient(to right, #a29bfe, #6c5ce7);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         font-weight: 800;
#     }

#     /* Analyze Button Styling */
#     .stButton>button {
#         width: 100%;
#         border-radius: 12px;
#         background: linear-gradient(45deg, #6c5ce7, #a29bfe);
#         color: white;
#         border: none;
#         padding: 18px;
#         font-weight: bold;
#         transition: 0.4s;
#         box-shadow: 0 4px 20px rgba(108, 92, 231, 0.2);
#     }
#     .stButton>button:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 8px 25px rgba(108, 92, 231, 0.4);
#     }

#     /* Metric Cards Glassmorphism */
#     div[data-testid="stMetric"] {
#         background: rgba(28, 31, 43, 0.8);
#         border: 1px solid rgba(162, 155, 254, 0.2);
#         border-radius: 15px;
#         padding: 20px;
#     }

#     /* Report Card Styling */
#     .report-card {
#         background: rgba(22, 25, 34, 0.9);
#         border: 1px solid rgba(162, 155, 254, 0.15);
#         border-radius: 16px;
#         padding: 24px;
#         margin-bottom: 16px;
#     }
#     .stat-pill {
#         display: inline-block;
#         padding: 4px 14px;
#         border-radius: 20px;
#         font-size: 0.8rem;
#         font-weight: 600;
#         margin: 4px;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # --- 2. Sidebar Navigation & Logo ---
# with st.sidebar:
#     st.markdown("""
#         <div style="text-align: center; padding-bottom: 20px;">
#             <img src="https://cdn-icons-png.flaticon.com/512/2103/2103633.png" width="70" style="filter: invert(80%) sepia(20%) saturate(1000%) hue-rotate(220deg);">
#             <h2 style="color: #a29bfe; margin-top: 10px; letter-spacing: 2px;">SENTIENT AI</h2>
#             <p style="font-size: 0.7rem; color: #636e72;">PREMIUM INSIGHT ENGINE</p>
#         </div>
#     """, unsafe_allow_html=True)

#     # ── Language selector ──────────────────────────
#     chosen_lang = st.selectbox(
#         "🌐 Language / Langue / Idioma / Sprache",
#         list(LANG.keys()),
#         index=list(LANG.keys()).index(st.session_state.lang),
#         key="lang_picker"
#     )
#     st.session_state.lang = chosen_lang
#     T = LANG[chosen_lang]          # T is the active translation dict
#     # ──────────────────────────────────────────────

#     selected_nav = option_menu(
#         menu_title=None,
#         options=T["nav"],
#         icons=["house", "speedometer2", "clock-history", "table"],
#         menu_icon="cast",
#         default_index=0,
#         styles={
#             "container": {"padding": "0!important", "background-color": "transparent"},
#             "icon": {"color": "#a29bfe", "font-size": "18px"}, 
#             "nav-link": {"font-size": "15px", "text-align": "left", "margin":"5px", "color": "#a0a0a0"},
#             "nav-link-selected": {"background-color": "#6c5ce7", "color": "white"},
#         }
#     )

#     st.divider()
#     uploaded_file = st.file_uploader(T["upload"], type=["csv", "xlsx"])
    
#     if uploaded_file:
#         if uploaded_file.name.endswith('csv'):
#             df_raw = pd.read_csv(uploaded_file, on_bad_lines='skip', engine='python')
#         else:
#             df_raw = pd.read_excel(uploaded_file)

#         st.subheader(T["scope"])
#         analysis_mode = st.radio(T["target"], [T["whole"], T["specific"]])
#         target_col = st.selectbox(T["sel_col"], df_raw.columns) if analysis_mode == T["specific"] else df_raw.select_dtypes(include=['object']).columns[0]

#         st.subheader(T["visual"])
#         chart_type = st.selectbox(T["graph"], ["Donut Chart", "Bar Graph", "Line Graph (Trend)", "Histogram (Density)", "Combo Chart", "Pie Chart", "Heatmap", "Scatter plot"])
#         accent_color = st.color_picker(T["color"], "#a29bfe")

# # --- 3. Main Logic ---

# if selected_nav == T["nav"][0]:
#     st.markdown(f'<h1 class="hero-title">{T["hero"]}</h1>', unsafe_allow_html=True)
#     st.write(T["sub"])
#     st.image(
#         "https://images.unsplash.com/photo-1677442136019-21780ecad995?ixlib=rb-4.0.3&auto=format&fit=crop&w=1600&q=80",
#         use_container_width=True,
#         caption=T["caption"]
#     )

# elif selected_nav == T["nav"][1]:
#     if not uploaded_file:
#         st.info(T["upload_prompt"])
#     else:
#         st.title(T["dash_title"])
        
#         if st.button(T["gen_btn"]):
#             with st.spinner(T["spinner"]):
#                 def get_scores(text):
#                     return sid.polarity_scores(str(text))['compound']

#                 def get_all_scores(text):
#                     scores = sid.polarity_scores(str(text))
#                     return scores['pos'], scores['neg'], scores['neu'], scores['compound']

#                 df_raw['Compound_Score'] = df_raw[target_col].apply(get_scores)
#                 df_raw[['Pos_Score', 'Neg_Score', 'Neu_Score', 'Compound_Score']] = df_raw[target_col].apply(
#                     lambda x: pd.Series(get_all_scores(x))
#                 )
#                 df_raw['Sentiment'] = df_raw['Compound_Score'].apply(lambda x: 'Positive' if x >= 0.05 else ('Negative' if x <= -0.05 else 'Neutral'))
#                 df_raw['Text_Length'] = df_raw[target_col].astype(str).apply(len)
#                 df_raw['Word_Count'] = df_raw[target_col].astype(str).apply(lambda x: len(x.split()))
#                 df_raw['Index'] = range(len(df_raw))
#                 st.session_state.analyzed_df = df_raw

#                 total = len(df_raw)
#                 counts = df_raw['Sentiment'].value_counts()
#                 pos, neg, neu = counts.get('Positive', 0), counts.get('Negative', 0), counts.get('Neutral', 0)
#                 avg_score   = df_raw['Compound_Score'].mean()
#                 std_score   = df_raw['Compound_Score'].std()
#                 median_score = df_raw['Compound_Score'].median()
#                 skewness    = df_raw['Compound_Score'].skew()
#                 kurtosis_val = df_raw['Compound_Score'].kurtosis()
#                 q1          = df_raw['Compound_Score'].quantile(0.25)
#                 q3          = df_raw['Compound_Score'].quantile(0.75)
#                 iqr         = q3 - q1
#                 high_pos    = (df_raw['Compound_Score'] >= 0.5).sum()
#                 high_neg    = (df_raw['Compound_Score'] <= -0.5).sum()

#                 # Extra Metrics for Detailed Report
#                 variance = df_raw['Compound_Score'].var()
#                 lean_pos = ((df_raw['Compound_Score'] > 0) & (df_raw['Compound_Score'] < 0.05)).sum()
#                 lean_neg = ((df_raw['Compound_Score'] < 0) & (df_raw['Compound_Score'] > -0.05)).sum()
#                 true_neu = (df_raw['Compound_Score'] == 0).sum()
#                 polarity_index = df_raw['Compound_Score'].abs().mean()

#                 m1, m2, m3, m4 = st.columns(4)
#                 m1.metric(T["rows"], total)
#                 m2.metric(T["pos"], f"{(pos/total*100):.1f}%", delta=T["approval"])
#                 m3.metric(T["neg"], f"{(neg/total*100):.1f}%", delta=T["critical"], delta_color="inverse")
#                 m4.metric(T["neu"], f"{(neu/total*100):.1f}%")

#                 st.session_state.history.append({
#                     "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
#                     "File": uploaded_file.name,
#                     "Column": target_col,
#                     "Result": f"Pos: {pos} | Neg: {neg}"
#                 })

#                 st.divider()

#                 c1, c2 = st.columns([2, 1])
#                 with c1:
#                     st.subheader(f"{T['results']} {chart_type}")
#                     color_map = {'Positive':'#00b894', 'Negative':'#ff7675', 'Neutral':'#74b9ff'}
                    
#                     if chart_type == "Donut Chart":
#                         fig = px.pie(df_raw, names='Sentiment', hole=0.6, color='Sentiment', color_discrete_map=color_map)
#                     elif chart_type == "Bar Graph":
#                         fig = px.bar(counts.reset_index(), x='Sentiment', y='count', color='Sentiment', color_discrete_map=color_map)
#                     elif chart_type == "Line Graph (Trend)":
#                         fig = px.line(df_raw, y='Compound_Score', title="Sentiment Fluency Across Data", markers=True)
#                         fig.update_traces(line_color=accent_color)
#                     elif chart_type == "Histogram (Density)":
#                         fig = px.histogram(df_raw, x='Compound_Score', nbins=20, color='Sentiment', color_discrete_map=color_map)
#                     elif chart_type == "Combo Chart":
#                         fig = go.Figure()
#                         fig.add_trace(go.Bar(x=counts.index, y=counts.values, name='Count', marker_color=[color_map.get(s, '#a29bfe') for s in counts.index]))
#                         fig.add_trace(go.Scatter(x=counts.index, y=counts.values, mode='lines+markers', name='Trend', line=dict(color=accent_color, width=3)))
#                     elif chart_type == "Pie Chart":
#                         fig = px.pie(df_raw, names='Sentiment', color='Sentiment', color_discrete_map=color_map)
#                     elif chart_type == "Heatmap":
#                         heat_data = df_raw[['Pos_Score', 'Neg_Score', 'Neu_Score', 'Compound_Score']].corr()
#                         fig = px.imshow(heat_data, text_auto=True, color_continuous_scale='RdBu_r', title="Score Correlation Heatmap")
#                     elif chart_type == "Scatter plot":
#                         fig = px.scatter(df_raw, x='Index', y='Compound_Score', color='Sentiment', color_discrete_map=color_map, opacity=0.7, title="Sentiment Score per Record")
#                     else:
#                         fig = px.histogram(df_raw, x='Compound_Score', nbins=20, color='Sentiment', color_discrete_map=color_map)
                    
#                     fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white", template="plotly_dark")
#                     st.plotly_chart(fig, use_container_width=True)

#                 with c2:
#                     st.subheader(T["ai_interp"])
#                     status = T["favorable"] if pos > neg else T["action"]
#                     st.markdown(f"""
#                         <div style="background:#161922; padding:20px; border-radius:15px; border-left: 5px solid {accent_color};">
#                             <h4 style="color:{accent_color}">Status: {status}</h4>
#                             <p>Our AI has processed the <b>{target_col}</b> column. The emotional trajectory indicates a 
#                             { T["pos_bias"] if pos > neg else T["neg_trend"]}.</p>
#                             <hr style="opacity:0.1">
#                             <small>{T["data_src"]} {uploaded_file.name}</small>
#                         </div>
#                     """, unsafe_allow_html=True)

#                 st.divider()
#                 st.subheader(T["box_title"])
#                 col_box1, col_box2 = st.columns([3, 2])

#                 with col_box1:
#                     fig_box = go.Figure()
#                     for sentiment, color in [('Positive', '#00b894'), ('Neutral', '#74b9ff'), ('Negative', '#ff7675')]:
#                         subset = df_raw[df_raw['Sentiment'] == sentiment]['Compound_Score']
#                         if len(subset) > 0:
#                             fig_box.add_trace(go.Box(y=subset, name=sentiment, marker_color=color, boxmean='sd', line=dict(width=2)))
#                     fig_box.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white", template="plotly_dark", height=420)
#                     st.plotly_chart(fig_box, use_container_width=True)

#                 with col_box2:
#                     st.markdown(f"""
#                         <div style="background:#161922; padding:20px; border-radius:15px; border-left: 5px solid #74b9ff; margin-top: 10px;">
#                             <h4 style="color:#74b9ff;">{T["stat_sum"]}</h4>
#                             <p><b>{T["mean"]}:</b> {avg_score:.4f}</p>
#                             <p><b>{T["median"]}:</b> {median_score:.4f}</p>
#                             <p><b>{T["std"]}:</b> {std_score:.4f}</p>
#                             <p><b>{T["min"]}:</b> {df_raw['Compound_Score'].min():.4f}</p>
#                             <p><b>{T["max"]}:</b> {df_raw['Compound_Score'].max():.4f}</p>
#                             <p><b>{T["skew"]}:</b> {skewness:.4f}</p>
#                             <p><b>{T["kurt"]}:</b> {kurtosis_val:.4f}</p>
#                         </div>
#                     """, unsafe_allow_html=True)

#                 # =========================================================================
#                 # --- ENHANCED DETAILED EXECUTIVE INSIGHT REPORT ---
#                 # =========================================================================
#                 st.divider()
#                 st.header(T["report_hdr"])

#                 avg_pos_fmt = f"{df_raw[df_raw['Sentiment']=='Positive']['Compound_Score'].mean():.4f}" if pos > 0 else 'N/A'
#                 avg_neg_fmt = f"{df_raw[df_raw['Sentiment']=='Negative']['Compound_Score'].mean():.4f}" if neg > 0 else 'N/A'
#                 avg_neu_fmt = f"{df_raw[df_raw['Sentiment']=='Neutral']['Compound_Score'].mean():.4f}" if neu > 0 else 'N/A'

#                 # ── Section 1: Detailed Dataset Integrity ───────────────
#                 st.markdown(f"""
#                     <div class="report-card">
#                         <h3 style="color:#a29bfe; margin-bottom: 16px;">{T["sec1"]}</h3>
#                         <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; margin-bottom: 20px;">
#                             <div><p style="color:#636e72; font-size:0.8rem; margin-bottom:2px;">{T["src_file"]}</p><p style="font-weight:600;">{uploaded_file.name}</p></div>
#                             <div><p style="color:#636e72; font-size:0.8rem; margin-bottom:2px;">{T["ana_col"]}</p><p style="font-weight:600;">{target_col}</p></div>
#                             <div><p style="color:#636e72; font-size:0.8rem; margin-bottom:2px;">{T["gen_at"]}</p><p style="font-weight:600;">{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p></div>
#                         </div>
#                         <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 16px; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 15px;">
#                             <div><p style="color:#636e72; font-size:0.75rem;">TOTAL RECORDS</p><p style="font-size:1.1rem; font-weight:700;">{total:,}</p></div>
#                             <div><p style="color:#636e72; font-size:0.75rem;">NULL / EMPTY</p><p style="font-size:1.1rem; font-weight:700;">{df_raw[target_col].isna().sum()}</p></div>
#                             <div><p style="color:#636e72; font-size:0.75rem;">UNIQUE ENTRIES</p><p style="font-size:1.1rem; font-weight:700;">{df_raw[target_col].nunique():,}</p></div>
#                             <div><p style="color:#636e72; font-size:0.75rem;">POLARITY DENSITY</p><p style="font-size:1.1rem; font-weight:700;">{polarity_index:.4f}</p></div>
#                         </div>
#                     </div>
#                 """, unsafe_allow_html=True)

#                 # ── Section 2: Advanced Sentiment Results ──────────────
#                 overall_sentiment = "POSITIVE" if pos > neg and pos > neu else ("NEGATIVE" if neg > pos and neg > neu else "NEUTRAL")
#                 overall_color = "#00b894" if overall_sentiment == "POSITIVE" else ("#ff7675" if overall_sentiment == "NEGATIVE" else "#74b9ff")

#                 st.markdown(f"""
#                     <div class="report-card">
#                         <h3 style="color:#a29bfe; margin-bottom: 16px;">{T["sec2"]}</h3>
#                         <div style="margin-bottom: 25px;">
#                             <span style="font-size:1rem; color:#636e72;">{T["overall_lbl"]} </span>
#                             <span style="font-size:1.5rem; font-weight:800; color:{overall_color};">● {overall_sentiment}</span>
#                         </div>
#                         <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; text-align: center; margin-bottom:20px;">
#                             <div style="background: rgba(0,184,148,0.05); border: 1px solid rgba(0,184,148,0.2); border-radius:12px; padding: 20px;">
#                                 <p style="font-size: 2rem; font-weight: 800; color: #00b894; margin:0;">{pos:,}</p>
#                                 <p style="color: #00b894; font-weight: 600; margin:4px 0;">POSITIVE</p>
#                                 <p style="color:#636e72; font-size:0.8rem;">Avg Score: {avg_pos_fmt}</p>
#                             </div>
#                             <div style="background: rgba(255,118,117,0.05); border: 1px solid rgba(255,118,117,0.2); border-radius:12px; padding: 20px;">
#                                 <p style="font-size: 2rem; font-weight: 800; color: #ff7675; margin:0;">{neg:,}</p>
#                                 <p style="color: #ff7675; font-weight: 600; margin:4px 0;">NEGATIVE</p>
#                                 <p style="color:#636e72; font-size:0.8rem;">Avg Score: {avg_neg_fmt}</p>
#                             </div>
#                             <div style="background: rgba(116,185,255,0.05); border: 1px solid rgba(116,185,255,0.2); border-radius:12px; padding: 20px;">
#                                 <p style="font-size: 2rem; font-weight: 800; color: #74b9ff; margin:0;">{neu:,}</p>
#                                 <p style="color: #74b9ff; font-weight: 600; margin:4px 0;">NEUTRAL</p>
#                                 <p style="color:#636e72; font-size:0.8rem;">Avg Score: {avg_neu_fmt}</p>
#                             </div>
#                         </div>
#                         <div style="background: rgba(255,255,255,0.02); padding: 15px; border-radius: 10px;">
#                             <p style="color:#636e72; font-size:0.85rem; font-weight:600; margin-bottom:10px;">NEUTRAL BAND BREAKDOWN (LEAN ANALYSIS)</p>
#                             <div style="display: flex; justify-content: space-between;">
#                                 <span>Lean Positive (0.01 to 0.04): <b>{lean_pos}</b></span>
#                                 <span>Absolute Neutral (0.00): <b>{true_neu}</b></span>
#                                 <span>Lean Negative (-0.01 to -0.04): <b>{lean_neg}</b></span>
#                             </div>
#                         </div>
#                     </div>
#                 """, unsafe_allow_html=True)

#                 # ── Section 3: Detailed Statistical Deep Dive ──────────
#                 skew_note = T["left_skew"] if skewness < -0.5 else (T["right_skew"] if skewness > 0.5 else T["sym"])
#                 st.markdown(f"""
#                     <div class="report-card">
#                         <h3 style="color:#a29bfe; margin-bottom: 16px;">{T["sec3"]}</h3>
#                         <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px;">
#                             <div>
#                                 <p style="color:#636e72; font-size:0.85rem; font-weight:600; letter-spacing:1px; margin-bottom:10px;">{T["score_stats"]}</p>
#                                 <table style="width:100%; border-collapse:collapse;">
#                                     <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 0; color:#a0a0a0;">{T["mean"]}</td><td style="padding:8px 0; font-weight:600; text-align:right;">{avg_score:.6f}</td></tr>
#                                     <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 0; color:#a0a0a0;">{T["median"]}</td><td style="padding:8px 0; font-weight:600; text-align:right;">{median_score:.6f}</td></tr>
#                                     <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 0; color:#a0a0a0;">{T["std"]}</td><td style="padding:8px 0; font-weight:600; text-align:right;">{std_score:.6f}</td></tr>
#                                     <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 0; color:#a0a0a0;">Variance</td><td style="padding:8px 0; font-weight:600; text-align:right;">{variance:.6f}</td></tr>
#                                     <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 0; color:#a0a0a0;">{T["iqr"]}</td><td style="padding:8px 0; font-weight:600; text-align:right;">{iqr:.6f}</td></tr>
#                                     <tr style="border-bottom:1px solid rgba(255,255,255,0.05);"><td style="padding:8px 0; color:#a0a0a0;">{T["skew"]}</td><td style="padding:8px 0; font-weight:600; text-align:right;">{skewness:.4f}</td></tr>
#                                     <tr><td style="padding:8px 0; color:#a0a0a0;">{T["kurt"]}</td><td style="padding:8px 0; font-weight:600; text-align:right;">{kurtosis_val:.4f}</td></tr>
#                                 </table>
#                             </div>
#                             <div>
#                                 <p style="color:#636e72; font-size:0.85rem; font-weight:600; letter-spacing:1px; margin-bottom:10px;">{T["intensity"]}</p>
#                                 <div style="background:rgba(0,184,148,0.1); border-radius:10px; padding:14px; margin-bottom:10px;">
#                                     <p style="color:#00b894; margin:0; font-weight:700;">{T["str_pos"]} {high_pos:,} {T["entries"]} ({(high_pos/total*100):.1f}%)</p>
#                                     <small style="color:#00b894; opacity:0.8;">Highly favorable sentiment markers identified.</small>
#                                 </div>
#                                 <div style="background:rgba(255,118,117,0.1); border-radius:10px; padding:14px; margin-bottom:10px;">
#                                     <p style="color:#ff7675; margin:0; font-weight:700;">{T["str_neg"]} {high_neg:,} {T["entries"]} ({(high_neg/total*100):.1f}%)</p>
#                                     <small style="color:#ff7675; opacity:0.8;">Critical negative clusters requiring immediate audit.</small>
#                                 </div>
#                                 <div style="background:rgba(162,155,254,0.1); border-radius:10px; padding:14px; margin-bottom:10px;">
#                                     <p style="color:#a29bfe; margin:0; font-weight:700;">{T["mod_band"]} {total-high_pos-high_neg:,} {T["entries"]} ({((total-high_pos-high_neg)/total*100):.1f}%)</p>
#                                     <small style="color:#a29bfe; opacity:0.8;">Balanced moderate responses (Score -0.5 to 0.5).</small>
#                                 </div>
#                                 <p style="color:#636e72; font-size:0.8rem; margin-top:10px;">{skew_note}</p>
#                             </div>
#                         </div>
#                     </div>
#                 """, unsafe_allow_html=True)

#                 # ── Section 4: Text Complexity ─────────────────
#                 st.markdown(f"""
#                     <div class="report-card">
#                         <h3 style="color:#a29bfe; margin-bottom: 16px;">{T["sec4"]}</h3>
#                         <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 16px; text-align: center;">
#                             <div style="background:rgba(162,155,254,0.08); border-radius:10px; padding:16px;">
#                                 <p style="font-size:1.6rem; font-weight:800; color:#a29bfe; margin:0;">{df_raw['Word_Count'].mean():.1f}</p>
#                                 <p style="color:#636e72; font-size:0.8rem; margin:4px 0;">{T["avg_w"]}</p>
#                             </div>
#                             <div style="background:rgba(162,155,254,0.08); border-radius:10px; padding:16px;">
#                                 <p style="font-size:1.6rem; font-weight:800; color:#a29bfe; margin:0;">{df_raw['Word_Count'].max()}</p>
#                                 <p style="color:#636e72; font-size:0.8rem; margin:4px 0;">{T["max_w"]}</p>
#                             </div>
#                             <div style="background:rgba(162,155,254,0.08); border-radius:10px; padding:16px;">
#                                 <p style="font-size:1.6rem; font-weight:800; color:#a29bfe; margin:0;">{df_raw['Word_Count'].min()}</p>
#                                 <p style="color:#636e72; font-size:0.8rem; margin:4px 0;">{T["min_w"]}</p>
#                             </div>
#                             <div style="background:rgba(162,155,254,0.08); border-radius:10px; padding:16px;">
#                                 <p style="font-size:1.6rem; font-weight:800; color:#a29bfe; margin:0;">{df_raw['Word_Count'].sum():,}</p>
#                                 <p style="color:#636e72; font-size:0.8rem; margin:4px 0;">{T["tot_w"]}</p>
#                             </div>
#                         </div>
#                         <div style="margin-top:20px; padding: 15px; background: rgba(255,255,255,0.02); border-radius:10px;">
#                             <p style="color:#636e72; font-size:0.85rem; font-weight:600;">LINGUISTIC MARKERS</p>
#                             <p>Average Entry Length: <b>{df_raw['Text_Length'].mean():.0f}</b> characters per record.</p>
#                             <p>Vocabulary Density: <b>{df_raw['Word_Count'].nunique() / df_raw['Word_Count'].sum():.4f}</b> (Unique Word Ratio).</p>
#                         </div>
#                     </div>
#                 """, unsafe_allow_html=True)

#                 # ── Section 5: AI Recommendations ─────────────
#                 pos_pct = pos / total * 100
#                 neg_pct = neg / total * 100
#                 neu_pct = neu / total * 100
#                 recs = []
#                 if neg_pct > 30:
#                     recs.append((T["rec1_title"], f"{neg_pct:.1f}% {T['rec1_body']}"))
#                 if neu_pct > 50:
#                     recs.append((T["rec2_title"], f"{neu_pct:.1f}% {T['rec2_body']}"))
#                 if pos_pct > 60:
#                     recs.append((T["rec3_title"], f"{pos_pct:.1f}% {T['rec3_body']}"))
#                 if abs(skewness) > 1:
#                     recs.append((T["rec4_title"], f"{T['skew']}: {skewness:.2f}. {T['rec4_body']}"))
#                 if not recs:
#                     recs.append((T["rec5_title"], T["rec5_body"]))

#                 rec_html = "".join([f"""
#                     <div style="padding:14px; border-left:4px solid rgba(162,155,254,0.5); margin-bottom:12px; background:rgba(162,155,254,0.05); border-radius:0 10px 10px 0;">
#                         <p style="font-weight:700; margin:0 0 6px 0;">{r[0]}</p>
#                         <p style="color:#a0a0a0; margin:0; font-size:0.9rem;">{r[1]}</p>
#                     </div>
#                 """ for r in recs])

#                 st.markdown(f"""
#                     <div class="report-card">
#                         <h3 style="color:#a29bfe; margin-bottom: 16px;">{T["sec5"]}</h3>
#                         {rec_html}
#                     </div>
#                 """, unsafe_allow_html=True)

#                 st.divider()
#                 st.subheader(T["export_hdr"])
#                 report_text = f"""SENTIENT AI — DETAILED EXECUTIVE INSIGHT REPORT
# {'='*60}
# Generated : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
# File      : {uploaded_file.name}
# Column    : {target_col}
# Engine    : VADER NLP v3 | Language: {chosen_lang}

# {'='*60}
# 1. DATASET INTEGRITY & OVERVIEW
# {'='*60}
# Total Records   : {total:,}
# Unique Entries  : {df_raw[target_col].nunique():,}
# Null/Empty      : {df_raw[target_col].isna().sum()}
# Polarity Density: {polarity_index:.4f}

# {'='*60}
# 2. SENTIMENT CLASSIFICATION (ADVANCED)
# {'='*60}
# Overall Sentiment : {overall_sentiment}
# Positive : {pos:,} ({pos/total*100:.2f}%) | Avg Score: {avg_pos_fmt}
# Negative : {neg:,} ({neg/total*100:.2f}%) | Avg Score: {avg_neg_fmt}
# Neutral  : {neu:,} ({neu/total*100:.2f}%) | Avg Score: {avg_neu_fmt}

# LEAN ANALYSIS (Within Neutral Band):
# Lean Positive (0.01 - 0.04) : {lean_pos}
# Absolute Neutral (0.00)     : {true_neu}
# Lean Negative (-0.01 - -0.04): {lean_neg}

# {'='*60}
# 3. STATISTICAL DEEP DIVE
# {'='*60}
# Mean            : {avg_score:.6f}
# Median          : {median_score:.6f}
# Std Deviation   : {std_score:.6f}
# Variance        : {variance:.6f}
# IQR             : {iqr:.6f}
# Skewness        : {skewness:.4f}
# Kurtosis        : {kurtosis_val:.4f}

# INTENSITY BANDS:
# Strongly Positive (>=0.5) : {high_pos:,} ({(high_pos/total*100):.1f}%)
# Strongly Negative (<=-0.5): {high_neg:,} ({(high_neg/total*100):.1f}%)
# Moderate (-0.5 to 0.5)    : {total-high_pos-high_neg:,} ({(total-high_pos-high_neg)/total*100:.1f}%)

# {'='*60}
# 4. TEXT COMPLEXITY & LINGUISTICS
# {'='*60}
# Avg Words / Entry   : {df_raw['Word_Count'].mean():.1f}
# Max Words           : {df_raw['Word_Count'].max()}
# Total Words Analyzed: {df_raw['Word_Count'].sum():,}
# Avg Entry Chars     : {df_raw['Text_Length'].mean():.0f}

# {'='*60}
# 5. AI-POWERED RECOMMENDATIONS
# {'='*60}
# {chr(10).join([f"• {r[0]}: {r[1]}" for r in recs])}

# {'='*60}
# END OF REPORT — SENTIENT AI PREMIUM INSIGHT ENGINE
# """
#                 col_btn1, col_btn2 = st.columns(2)
#                 col_btn1.download_button(T["dl_report"], report_text, "sentient_report_detailed.txt")
#                 col_btn2.download_button(T["dl_csv"], df_raw.to_csv(index=False), "analyzed_sentiments.csv")

# elif selected_nav == T["nav"][2]:
#     st.title(T["hist_title"])
#     if not st.session_state.history:
#         st.info(T["no_hist"])
#     else:
#         st.table(pd.DataFrame(st.session_state.history))
#         if st.button(T["clr_hist"]):
#             st.session_state.history = []
#             st.rerun()

# elif selected_nav == T["nav"][3]:
#     st.title(T["exp_title"])
#     if st.session_state.analyzed_df is not None:
#         st.dataframe(st.session_state.analyzed_df, use_container_width=True)
#     elif uploaded_file:
#         st.dataframe(df_raw, use_container_width=True)
#     else:
#         st.info(T["exp_prompt"])