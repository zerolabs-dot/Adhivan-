#!/usr/bin/env python3
"""
Decision Support System (DSS) Module - ADHIVAN
Government Land Rights Management System
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import folium
from streamlit_folium import st_folium
import json
import os
from datetime import datetime, timedelta
import base64
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="ADHIVAN - Decision Support System",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for government styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #2a5298;
    }
    .alert-box {
        background: #fff3cd;
        border: 1px solid #ffeaa7;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .success-box {
        background: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

class DSS_System:
    def __init__(self):
        self.sample_data = self.generate_sample_data()
        self.initialize_session_state()
    
    def initialize_session_state(self):
        """Initialize session state variables"""
        if 'processed_data' not in st.session_state:
            st.session_state.processed_data = None
        if 'selected_claim' not in st.session_state:
            st.session_state.selected_claim = None
    
    def generate_sample_data(self):
        """Generate comprehensive sample FRA claims data"""
        np.random.seed(42)
        
        districts = ['Wayanad', 'Idukki', 'Palakkad', 'Thrissur', 'Kozhikode']
        tribes = ['Paniya', 'Adiya', 'Kuruma', 'Kattunaikan', 'Irula']
        claim_types = ['Individual Forest Rights (IFR)', 'Community Forest Rights (CFR)', 'Community Rights (CR)']
        land_types = ['Forest Land', 'Agricultural Land', 'Wasteland', 'Mixed Use']
        statuses = ['Approved', 'Pending', 'Under Review', 'Rejected', 'Disputed']
        
        n_claims = 500
        
        data = {
            'claim_id': [f'FRA{str(i).zfill(6)}' for i in range(1, n_claims + 1)],
            'district': np.random.choice(districts, n_claims),
            'tribe': np.random.choice(tribes, n_claims),
            'claim_type': np.random.choice(claim_types, n_claims),
            'land_type': np.random.choice(land_types, n_claims),
            'area_hectares': np.random.uniform(0.5, 15.0, n_claims).round(2),
            'status': np.random.choice(statuses, n_claims, p=[0.4, 0.25, 0.15, 0.1, 0.1]),
            'submission_date': pd.date_range('2020-01-01', '2024-12-01', periods=n_claims),
            'latitude': np.random.uniform(8.2, 12.8, n_claims),
            'longitude': np.random.uniform(74.8, 77.8, n_claims),
            'population_benefited': np.random.randint(1, 50, n_claims),
            'verification_officer': np.random.choice(['Officer A', 'Officer B', 'Officer C', 'Officer D'], n_claims),
            'priority_score': np.random.uniform(1, 10, n_claims).round(1)
        }
        
        df = pd.DataFrame(data)
        df['approval_date'] = df.apply(lambda x: x['submission_date'] + timedelta(days=np.random.randint(30, 365)) 
                                     if x['status'] == 'Approved' else None, axis=1)
        
        return df
    
    def create_summary_insights(self, data):
        """Generate comprehensive data summary and insights"""
        total_claims = len(data)
        total_area = data['area_hectares'].sum()
        approved_claims = len(data[data['status'] == 'Approved'])
        pending_claims = len(data[data['status'] == 'Pending'])
        
        insights = {
            'total_claims': total_claims,
            'total_area': round(total_area, 2),
            'approved_claims': approved_claims,
            'pending_claims': pending_claims,
            'approval_rate': round((approved_claims / total_claims) * 100, 1),
            'avg_area_per_claim': round(data['area_hectares'].mean(), 2),
            'total_beneficiaries': data['population_benefited'].sum(),
            'districts_covered': data['district'].nunique(),
            'tribes_involved': data['tribe'].nunique()
        }
        
        return insights    

    def create_interactive_map(self, data):
        """Create interactive folium map with claim locations"""
        center_lat = data['latitude'].mean()
        center_lon = data['longitude'].mean()
        
        m = folium.Map(
            location=[center_lat, center_lon],
            zoom_start=8,
            tiles='OpenStreetMap'
        )
        
        color_map = {
            'Approved': 'green',
            'Pending': 'orange',
            'Under Review': 'blue',
            'Rejected': 'red',
            'Disputed': 'purple'
        }
        
        for idx, row in data.iterrows():
            popup_html = f"""
            <div style="width: 300px;">
                <h4>Claim ID: {row['claim_id']}</h4>
                <p><b>District:</b> {row['district']}</p>
                <p><b>Tribe:</b> {row['tribe']}</p>
                <p><b>Area:</b> {row['area_hectares']} hectares</p>
                <p><b>Status:</b> {row['status']}</p>
            </div>
            """
            
            folium.CircleMarker(
                location=[row['latitude'], row['longitude']],
                radius=max(5, row['area_hectares'] / 2),
                popup=folium.Popup(popup_html, max_width=300),
                color=color_map.get(row['status'], 'gray'),
                fill=True,
                fillColor=color_map.get(row['status'], 'gray'),
                fillOpacity=0.7,
                weight=2
            ).add_to(m)
        
        return m
    
    def create_visualizations(self, data):
        """Create comprehensive data visualizations"""
        
        # Claims by District
        district_counts = data['district'].value_counts()
        fig_district = px.bar(
            x=district_counts.index,
            y=district_counts.values,
            title="Claims Distribution by District",
            labels={'x': 'District', 'y': 'Number of Claims'},
            color=district_counts.values,
            color_continuous_scale='Blues'
        )
        
        # Status Distribution
        status_counts = data['status'].value_counts()
        fig_status = px.pie(
            values=status_counts.values,
            names=status_counts.index,
            title="Claims Status Distribution",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        
        return fig_district, fig_status
    
    def generate_patta_document(self, claim_data):
        """Generate official Patta document for download"""
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4)
        styles = getSampleStyleSheet()
        story = []
        
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=18,
            spaceAfter=30,
            alignment=1,
            textColor=colors.darkblue
        )
        
        story.append(Paragraph("GOVERNMENT OF KERALA", title_style))
        story.append(Paragraph("FOREST RIGHTS ACT - LAND PATTA", title_style))
        story.append(Spacer(1, 20))
        
        claim_details = [
            ['Claim ID:', claim_data['claim_id']],
            ['District:', claim_data['district']],
            ['Tribal Community:', claim_data['tribe']],
            ['Area (Hectares):', str(claim_data['area_hectares'])],
            ['Status:', claim_data['status']],
        ]
        
        table = Table(claim_details, colWidths=[2*inch, 3*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.white),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
        ]))
        
        story.append(table)
        story.append(Spacer(1, 30))
        story.append(Paragraph(f"Generated on: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}", styles['Normal']))
        
        doc.build(story)
        buffer.seek(0)
        return buffer
    
    def query_processor(self, query, data):
        """Process natural language queries about the data"""
        query = query.lower()
        results = []
        
        if 'total' in query and 'claim' in query:
            total = len(data)
            results.append(f"Total number of claims: {total}")
        
        if 'approved' in query:
            approved = len(data[data['status'] == 'Approved'])
            rate = (approved / len(data)) * 100
            results.append(f"Approved claims: {approved} ({rate:.1f}% approval rate)")
        
        if 'district' in query:
            district_stats = data['district'].value_counts()
            results.append("Claims by district:")
            for district, count in district_stats.items():
                results.append(f"  • {district}: {count} claims")
        
        if not results:
            results.append("I can help you with queries about claims, districts, and statistics.")
        
        return "\n".join(results)    

    def run_dashboard(self):
        """Main dashboard interface"""
        
        st.markdown("""
        <div class="main-header">
            <h1>🏛️ ADHIVAN - Decision Support System</h1>
            <p>Government Land Rights Management & Analytics Platform</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.sidebar.title("🔧 System Controls")
        
        if st.sidebar.button("🔄 Process Sample Data", type="primary"):
            with st.spinner("Processing FRA claims data..."):
                st.session_state.processed_data = self.sample_data
                st.sidebar.success("✅ Data processed successfully!")
        
        if st.session_state.processed_data is None:
            st.warning("⚠️ Please process the sample data first using the sidebar.")
            st.info("Click '🔄 Process Sample Data' in the sidebar to begin analysis.")
            return
        
        data = st.session_state.processed_data
        insights = self.create_summary_insights(data)
        
        tab1, tab2, tab3, tab4 = st.tabs([
            "📈 Dashboard", "🗺️ Interactive Map", "📊 Analytics", "🤖 Query Assistant"
        ])
        
        with tab1:
            st.header("📈 Executive Dashboard")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Total Claims", insights['total_claims'])
            
            with col2:
                st.metric("Approval Rate", f"{insights['approval_rate']}%")
            
            with col3:
                st.metric("Total Area", f"{insights['total_area']} Ha")
            
            with col4:
                st.metric("Beneficiaries", insights['total_beneficiaries'])
            
            if insights['pending_claims'] > 100:
                st.warning(f"⚠️ High Priority Alert: {insights['pending_claims']} pending claims need attention.")
            
            fig_district, fig_status = self.create_visualizations(data)
            
            col1, col2 = st.columns(2)
            with col1:
                st.plotly_chart(fig_status, use_container_width=True)
            with col2:
                st.plotly_chart(fig_district, use_container_width=True)
        
        with tab2:
            st.header("🗺️ Interactive Geospatial Map")
            st.info("💡 Hover over markers to see detailed claim information.")
            
            map_obj = self.create_interactive_map(data)
            map_data = st_folium(map_obj, width=1200, height=600)
            
            if map_data['last_object_clicked_popup']:
                st.subheader("📋 Selected Claim Details")
                selected_claim = data.iloc[0]  # Demo selection
                
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.write(f"**Claim ID:** {selected_claim['claim_id']}")
                    st.write(f"**District:** {selected_claim['district']}")
                    st.write(f"**Tribal Community:** {selected_claim['tribe']}")
                    st.write(f"**Area:** {selected_claim['area_hectares']} hectares")
                    st.write(f"**Status:** {selected_claim['status']}")
                
                with col2:
                    if st.button("📄 Download Patta Document", type="primary"):
                        patta_buffer = self.generate_patta_document(selected_claim)
                        st.download_button(
                            label="💾 Download PDF",
                            data=patta_buffer.getvalue(),
                            file_name=f"Patta_{selected_claim['claim_id']}.pdf",
                            mime="application/pdf"
                        )
                        st.success("✅ Patta document ready for download!")
        
        with tab3:
            st.header("📊 Advanced Analytics")
            
            fig_district, fig_status = self.create_visualizations(data)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.plotly_chart(fig_district, use_container_width=True)
                
                st.subheader("📈 Performance Metrics")
                avg_processing_time = np.random.randint(45, 120)
                st.metric("Avg Processing Time", f"{avg_processing_time} days")
                
                conflict_rate = np.random.uniform(5, 15)
                st.metric("Conflict Rate", f"{conflict_rate:.1f}%")
            
            with col2:
                st.plotly_chart(fig_status, use_container_width=True)
                
                st.subheader("📊 Summary Statistics")
                st.write(f"**Districts Covered:** {insights['districts_covered']}")
                st.write(f"**Tribes Involved:** {insights['tribes_involved']}")
                st.write(f"**Average Area per Claim:** {insights['avg_area_per_claim']} Ha")
        
        with tab4:
            st.header("🤖 Intelligent Query Assistant")
            st.info("💬 Ask questions about the FRA claims data in natural language.")
            
            query = st.text_input(
                "Enter your query:",
                placeholder="e.g., 'How many claims are approved?', 'Show me district-wise statistics'"
            )
            
            if st.button("🔍 Process Query") and query:
                with st.spinner("Processing your query..."):
                    response = self.query_processor(query, data)
                    st.markdown(f"""
                    <div class="success-box">
                        <h4>📊 Query Results:</h4>
                        <pre>{response}</pre>
                    </div>
                    """, unsafe_allow_html=True)
            
            st.subheader("💡 Sample Queries")
            sample_queries = [
                "How many total claims are there?",
                "What is the approval rate?",
                "Show me district-wise statistics"
            ]
            
            for i, sample in enumerate(sample_queries):
                if st.button(f"📝 {sample}", key=f"sample_{i}"):
                    response = self.query_processor(sample, data)
                    st.markdown(f"""
                    <div class="success-box">
                        <h4>📊 Query Results:</h4>
                        <pre>{response}</pre>
                    </div>
                    """, unsafe_allow_html=True)

def main():
    """Main application entry point"""
    dss = DSS_System()
    dss.run_dashboard()

if __name__ == "__main__":
    main()