#!/usr/bin/env python3
"""
Enhanced ADHIVAN Decision Support System (DSS) Module
Advanced Government Land Rights Management System with Real Data Integration

Based on:
- Ministry of Tribal Affairs (tribal.nic.in)
- State Land Records Portals (Telangana, MP, Odisha)
- Tribal Welfare Departments
- Forest Land Information Systems
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
    page_title="Enhanced ADHIVAN - FRA Decision Support System",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS for professional government styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #1e3c72 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    .metric-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
        border-left: 5px solid #2a5298;
        margin: 0.5rem 0;
    }
    .alert-box {
        background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%);
        border: 2px solid #ffc107;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 16px rgba(255,193,7,0.2);
    }
    .success-box {
        background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
        border: 2px solid #28a745;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 16px rgba(40,167,69,0.2);
    }
    .data-source-card {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        border: 2px solid #2196f3;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    .stButton > button {
        background: linear-gradient(135deg, #2a5298 0%, #1e3c72 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(30,60,114,0.3);
    }
    .tribal-info {
        background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%);
        border: 2px solid #9c27b0;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

class Enhanced_DSS_System:
    def __init__(self):
        self.real_data_sources = self.initialize_data_sources()
        self.enhanced_sample_data = self.generate_enhanced_sample_data()
        self.tribal_welfare_data = self.load_tribal_welfare_data()
        self.initialize_session_state()
    
    def initialize_session_state(self):
        """Initialize enhanced session state variables"""
        if 'processed_data' not in st.session_state:
            st.session_state.processed_data = None
        if 'selected_claim' not in st.session_state:
            st.session_state.selected_claim = None
        if 'data_source' not in st.session_state:
            st.session_state.data_source = 'enhanced_sample'
        if 'analysis_mode' not in st.session_state:
            st.session_state.analysis_mode = 'comprehensive'
    
    def initialize_data_sources(self):
        """Initialize real government data source configurations"""
        return {
            'telangana': {
                'name': 'Telangana Bhu Bharati Portal',
                'url': 'https://bhubharati.co.in',
                'type': 'Land Records',
                'features': ['Pattadar Passbooks', 'Cadastral Maps', 'Survey Numbers'],
                'status': 'Active',
                'api_available': False
            },
            'telangana_open': {
                'name': 'Telangana Open Data Portal',
                'url': 'https://data.telangana.gov.in',
                'type': 'Open Data',
                'features': ['GIS Layers', 'Statistical Data', 'Demographic Info'],
                'status': 'Active',
                'api_available': True
            },
            'mp_bhulekh': {
                'name': 'MP Bhulekh Portal',
                'url': 'https://mpbhulekh.gov.in',
                'type': 'Land Records',
                'features': ['Khata/Khasra', 'Land Maps', 'Ownership Details'],
                'status': 'Active',
                'api_available': False
            },
            'odisha_forest': {
                'name': 'Odisha FLI-DSS',
                'url': 'https://odishaforestgeodss.in',
                'type': 'Forest Land Information',
                'features': ['Forest Layers', 'ESZ Data', 'Protected Areas'],
                'status': 'Active',
                'api_available': True
            },
            'tribal_affairs': {
                'name': 'Ministry of Tribal Affairs',
                'url': 'https://tribal.nic.in',
                'type': 'Tribal Welfare',
                'features': ['Tribal Demographics', 'Welfare Schemes', 'FRA Guidelines'],
                'status': 'Active',
                'api_available': False
            }
        }
    
    def load_tribal_welfare_data(self):
        """Load comprehensive tribal welfare and demographic data"""
        return {
            'telangana_tribes': {
                'major_tribes': ['Gond', 'Koya', 'Chenchu', 'Yerukula', 'Lambada'],
                'population': 3200000,
                'districts': ['Adilabad', 'Khammam', 'Warangal', 'Mahbubnagar'],
                'welfare_dept': 'https://tgtribalwelfare.cgg.gov.in',
                'schemes': ['Girijan Cooperative Corporation', 'Tribal Sub Plan', 'ITDA Programs']
            },
            'madhya_pradesh_tribes': {
                'major_tribes': ['Bhil', 'Gond', 'Baiga', 'Sahariya', 'Korku'],
                'population': 15300000,
                'districts': ['Jhabua', 'Dhar', 'Mandla', 'Dindori', 'Barwani'],
                'welfare_dept': 'https://tribal.mp.gov.in',
                'schemes': ['Mukhyamantri Tribal Swavalamban Yojana', 'Van Dhan Vikas']
            },
            'odisha_tribes': {
                'major_tribes': ['Santhal', 'Koya', 'Saora', 'Oraon', 'Munda'],
                'population': 9600000,
                'districts': ['Mayurbhanj', 'Sundargarh', 'Kandhamal', 'Koraput'],
                'welfare_dept': 'https://stscarticle.odisha.gov.in',
                'schemes': ['Special Central Assistance', 'Tribal Development Cooperative']
            },
            'kerala_tribes': {
                'major_tribes': ['Paniya', 'Adiya', 'Kuruma', 'Kattunaikan', 'Irula'],
                'population': 485000,
                'districts': ['Wayanad', 'Idukki', 'Palakkad', 'Kozhikode'],
                'welfare_dept': 'https://stdd.kerala.gov.in',
                'schemes': ['Tribal Development Program', 'Forest Rights Implementation']
            }
        }   
 
    def generate_enhanced_sample_data(self):
        """Generate enhanced sample data based on real government sources"""
        np.random.seed(42)
        
        # Enhanced state and district mapping
        state_districts = {
            'Telangana': ['Adilabad', 'Khammam', 'Warangal', 'Mahbubnagar', 'Nizamabad'],
            'Madhya Pradesh': ['Jhabua', 'Dhar', 'Mandla', 'Dindori', 'Barwani'],
            'Odisha': ['Mayurbhanj', 'Sundargarh', 'Kandhamal', 'Koraput', 'Gajapati'],
            'Kerala': ['Wayanad', 'Idukki', 'Palakkad', 'Kozhikode', 'Thrissur']
        }
        
        # Enhanced tribal mapping by state
        state_tribes = {
            'Telangana': ['Gond', 'Koya', 'Chenchu', 'Yerukula', 'Lambada'],
            'Madhya Pradesh': ['Bhil', 'Gond', 'Baiga', 'Sahariya', 'Korku'],
            'Odisha': ['Santhal', 'Koya', 'Saora', 'Oraon', 'Munda'],
            'Kerala': ['Paniya', 'Adiya', 'Kuruma', 'Kattunaikan', 'Irula']
        }
        
        claim_types = [
            'Individual Forest Rights (IFR)', 
            'Community Forest Rights (CFR)', 
            'Community Rights (CR)',
            'Habitat Rights',
            'Grazing Rights',
            'NTFP Rights'
        ]
        
        land_types = [
            'Forest Land', 'Agricultural Land', 'Wasteland', 'Mixed Use',
            'Grazing Land', 'Water Bodies', 'Settlement Area'
        ]
        
        statuses = ['Approved', 'Pending', 'Under Review', 'Rejected', 'Disputed', 'Survey Required']
        
        # Generate coordinates for different states
        state_coords = {
            'Telangana': {'lat_range': (16.0, 19.5), 'lon_range': (77.0, 81.0)},
            'Madhya Pradesh': {'lat_range': (21.0, 26.5), 'lon_range': (74.0, 82.0)},
            'Odisha': {'lat_range': (17.5, 22.5), 'lon_range': (81.0, 87.5)},
            'Kerala': {'lat_range': (8.2, 12.8), 'lon_range': (74.8, 77.8)}
        }
        
        n_claims = 1000  # Increased sample size
        
        # Generate state distribution
        states = np.random.choice(list(state_districts.keys()), n_claims, p=[0.3, 0.3, 0.25, 0.15])
        
        data = []
        for i in range(n_claims):
            state = states[i]
            district = np.random.choice(state_districts[state])
            tribe = np.random.choice(state_tribes[state])
            
            # Generate coordinates based on state
            lat_range = state_coords[state]['lat_range']
            lon_range = state_coords[state]['lon_range']
            lat = np.random.uniform(lat_range[0], lat_range[1])
            lon = np.random.uniform(lon_range[0], lon_range[1])
            
            claim_data = {
                'claim_id': f'FRA{str(i+1).zfill(6)}',
                'state': state,
                'district': district,
                'tribe': tribe,
                'claim_type': np.random.choice(claim_types),
                'land_type': np.random.choice(land_types),
                'area_hectares': round(np.random.uniform(0.5, 25.0), 2),
                'status': np.random.choice(statuses, p=[0.35, 0.25, 0.15, 0.1, 0.1, 0.05]),
                'submission_date': pd.date_range('2018-01-01', '2024-12-01', periods=n_claims)[i],
                'latitude': round(lat, 6),
                'longitude': round(lon, 6),
                'population_benefited': np.random.randint(1, 75),
                'verification_officer': np.random.choice(['Officer A', 'Officer B', 'Officer C', 'Officer D', 'Officer E']),
                'priority_score': round(np.random.uniform(1, 10), 1),
                'survey_number': f'SY{np.random.randint(100, 9999)}',
                'village': f'Village_{np.random.randint(1, 100)}',
                'tehsil': f'Tehsil_{np.random.randint(1, 20)}',
                'forest_division': f'FD_{district}_{np.random.randint(1, 5)}',
                'gps_verified': np.random.choice([True, False], p=[0.7, 0.3]),
                'documents_complete': np.random.choice([True, False], p=[0.8, 0.2]),
                'community_consent': np.random.choice([True, False], p=[0.85, 0.15]),
                'environmental_clearance': np.random.choice([True, False, None], p=[0.6, 0.2, 0.2])
            }
            data.append(claim_data)
        
        df = pd.DataFrame(data)
        
        # Add approval dates for approved claims
        df['approval_date'] = df.apply(
            lambda x: x['submission_date'] + timedelta(days=np.random.randint(30, 730)) 
            if x['status'] == 'Approved' else None, axis=1
        )
        
        return df
    
    def create_enhanced_summary_insights(self, data):
        """Generate comprehensive enhanced data summary and insights"""
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
            'states_covered': data['state'].nunique(),
            'districts_covered': data['district'].nunique(),
            'tribes_involved': data['tribe'].nunique(),
            'gps_verified_rate': round((data['gps_verified'].sum() / total_claims) * 100, 1),
            'documents_complete_rate': round((data['documents_complete'].sum() / total_claims) * 100, 1),
            'community_consent_rate': round((data['community_consent'].sum() / total_claims) * 100, 1),
            'avg_processing_time': round(data[data['approval_date'].notna()].apply(
                lambda x: (x['approval_date'] - x['submission_date']).days, axis=1
            ).mean(), 0) if len(data[data['approval_date'].notna()]) > 0 else 0
        }
        
        return insights
    
    def create_decision_matrix(self, data):
        """Create decision support matrix for FRA claims"""
        decision_factors = []
        
        for _, claim in data.iterrows():
            factors = {
                'claim_id': claim['claim_id'],
                'priority_score': claim['priority_score'],
                'readiness_score': 0,
                'risk_score': 0,
                'recommendation': '',
                'action_required': []
            }
            
            # Calculate readiness score
            if claim['gps_verified']:
                factors['readiness_score'] += 2
            if claim['documents_complete']:
                factors['readiness_score'] += 2
            if claim['community_consent']:
                factors['readiness_score'] += 2
            if claim['environmental_clearance'] == True:
                factors['readiness_score'] += 2
            elif claim['environmental_clearance'] == False:
                factors['risk_score'] += 2
            
            # Calculate risk factors
            if claim['area_hectares'] > 15:
                factors['risk_score'] += 1
            if claim['population_benefited'] > 50:
                factors['risk_score'] += 1
            if not claim['gps_verified']:
                factors['risk_score'] += 2
                factors['action_required'].append('GPS Survey Required')
            if not claim['documents_complete']:
                factors['risk_score'] += 1
                factors['action_required'].append('Document Verification')
            if not claim['community_consent']:
                factors['risk_score'] += 3
                factors['action_required'].append('Community Consultation')
            
            # Generate recommendations
            if factors['readiness_score'] >= 6 and factors['risk_score'] <= 2:
                factors['recommendation'] = 'Fast Track Approval'
            elif factors['readiness_score'] >= 4 and factors['risk_score'] <= 4:
                factors['recommendation'] = 'Standard Processing'
            elif factors['risk_score'] > 4:
                factors['recommendation'] = 'Detailed Review Required'
            else:
                factors['recommendation'] = 'Additional Documentation Needed'
            
            decision_factors.append(factors)
        
        return pd.DataFrame(decision_factors)
    
    def create_enhanced_interactive_map(self, data):
        """Create enhanced interactive folium map with multi-state support"""
        # Calculate center point for multi-state data
        center_lat = data['latitude'].mean()
        center_lon = data['longitude'].mean()
        
        m = folium.Map(
            location=[center_lat, center_lon],
            zoom_start=6,
            tiles='OpenStreetMap'
        )
        
        # Enhanced color mapping
        color_map = {
            'Approved': 'green',
            'Pending': 'orange',
            'Under Review': 'blue',
            'Rejected': 'red',
            'Disputed': 'purple',
            'Survey Required': 'darkred'
        }
        
        # Add state-wise clustering
        from folium.plugins import MarkerCluster
        marker_cluster = MarkerCluster().add_to(m)
        
        # Add markers for each claim
        for idx, row in data.iterrows():
            popup_html = f"""
            <div style="width: 350px; font-family: Arial;">
                <h4 style="color: #2a5298;">🏛️ {row['claim_id']}</h4>
                <hr>
                <p><b>📍 Location:</b> {row['district']}, {row['state']}</p>
                <p><b>👥 Tribe:</b> {row['tribe']}</p>
                <p><b>📋 Type:</b> {row['claim_type']}</p>
                <p><b>🌍 Area:</b> {row['area_hectares']} hectares</p>
                <p><b>📊 Status:</b> <span style="color: {color_map.get(row['status'], 'gray')};">{row['status']}</span></p>
                <p><b>👨‍👩‍👧‍👦 Beneficiaries:</b> {row['population_benefited']}</p>
                <p><b>⭐ Priority:</b> {row['priority_score']}/10</p>
                <p><b>🗺️ Survey No:</b> {row['survey_number']}</p>
                <p><b>✅ GPS Verified:</b> {'Yes' if row['gps_verified'] else 'No'}</p>
                <p><b>📄 Documents:</b> {'Complete' if row['documents_complete'] else 'Incomplete'}</p>
            </div>
            """
            
            folium.CircleMarker(
                location=[row['latitude'], row['longitude']],
                radius=max(6, min(row['area_hectares'] / 2, 15)),
                popup=folium.Popup(popup_html, max_width=350),
                color=color_map.get(row['status'], 'gray'),
                fill=True,
                fillColor=color_map.get(row['status'], 'gray'),
                fillOpacity=0.7,
                weight=2
            ).add_to(marker_cluster)
        
        # Enhanced legend
        legend_html = '''
        <div style="position: fixed; 
                    bottom: 50px; left: 50px; width: 180px; height: 160px; 
                    background-color: white; border:2px solid grey; z-index:9999; 
                    font-size:12px; padding: 15px; border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <h4 style="margin-top: 0; color: #2a5298;">📊 Claim Status</h4>
        <p><i class="fa fa-circle" style="color:green"></i> Approved</p>
        <p><i class="fa fa-circle" style="color:orange"></i> Pending</p>
        <p><i class="fa fa-circle" style="color:blue"></i> Under Review</p>
        <p><i class="fa fa-circle" style="color:red"></i> Rejected</p>
        <p><i class="fa fa-circle" style="color:purple"></i> Disputed</p>
        <p><i class="fa fa-circle" style="color:darkred"></i> Survey Required</p>
        </div>
        '''
        m.get_root().html.add_child(folium.Element(legend_html))
        
        return m    

    def create_advanced_visualizations(self, data):
        """Create advanced data visualizations for decision making"""
        
        # 1. Multi-State Claims Distribution
        state