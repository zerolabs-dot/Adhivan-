#!/usr/bin/env python3
"""
ADHIVAN Decision Support System - Flask Web Application
Government Land Rights Management System
"""

from flask import Flask, render_template, jsonify, request, send_file
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.utils
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
import folium

app = Flask(__name__)

class ADHIVANSystem:
    def __init__(self):
        self.data = None
        self.processed = False
        
    def generate_sample_data(self):
        """Generate comprehensive sample data for FRA claims"""
        np.random.seed(42)
        
        # Indian states with significant tribal populations
        states = ['Telangana', 'Madhya Pradesh', 'Odisha', 'Jharkhand', 'Chhattisgarh', 
                 'Maharashtra', 'Rajasthan', 'Gujarat', 'Andhra Pradesh', 'West Bengal']
        
        # Tribal communities
        tribal_communities = ['Gond', 'Santhal', 'Bhil', 'Oraon', 'Munda', 'Ho', 'Khond', 
                            'Baiga', 'Korku', 'Sahariya', 'Meena', 'Garasia']
        
        # Generate 500 sample claims
        n_claims = 500
        
        data = {
            'claim_id': [f'FRA{str(i+1).zfill(6)}' for i in range(n_claims)],
            'applicant_name': [f'Applicant_{i+1}' for i in range(n_claims)],
            'state': np.random.choice(states, n_claims),
            'district': [f'District_{np.random.randint(1, 31)}' for _ in range(n_claims)],
            'village': [f'Village_{np.random.randint(1, 101)}' for _ in range(n_claims)],
            'tribal_community': np.random.choice(tribal_communities, n_claims),
            'land_area_acres': np.round(np.random.exponential(2.5, n_claims), 2),
            'claim_type': np.random.choice(['Individual', 'Community', 'Community Forest Resource'], 
                                         n_claims, p=[0.6, 0.3, 0.1]),
            'submission_date': [datetime.now() - timedelta(days=np.random.randint(1, 1095)) 
                              for _ in range(n_claims)],
            'status': np.random.choice(['Pending', 'Under Review', 'Approved', 'Rejected', 'Requires Additional Info'], 
                                     n_claims, p=[0.25, 0.20, 0.35, 0.15, 0.05]),
            'latitude': np.random.uniform(8.0, 37.0, n_claims),
            'longitude': np.random.uniform(68.0, 97.0, n_claims),
            'forest_type': np.random.choice(['Dense Forest', 'Open Forest', 'Scrub Land', 'Grassland'], n_claims),
            'survey_number': [f'SY{np.random.randint(1, 1000)}' for _ in range(n_claims)],
            'gps_coordinates': [f"{lat:.6f}, {lon:.6f}" for lat, lon in 
                              zip(np.random.uniform(8.0, 37.0, n_claims), 
                                  np.random.uniform(68.0, 97.0, n_claims))],
            'family_size': np.random.randint(2, 12, n_claims),
            'occupation': np.random.choice(['Agriculture', 'Forest Produce Collection', 'Animal Husbandry', 
                                         'Daily Labor', 'Traditional Crafts'], n_claims),
            'annual_income': np.random.randint(15000, 150000, n_claims),
            'documents_submitted': np.random.choice(['Complete', 'Incomplete', 'Under Verification'], 
                                                  n_claims, p=[0.6, 0.25, 0.15]),
            'processing_time_days': np.random.randint(30, 730, n_claims),
            'officer_assigned': [f'Officer_{np.random.randint(1, 51)}' for _ in range(n_claims)],
            'priority_level': np.random.choice(['High', 'Medium', 'Low'], n_claims, p=[0.2, 0.5, 0.3])
        }
        
        self.data = pd.DataFrame(data)
        self.processed = True
        return self.data
    
    def get_dashboard_metrics(self):
        """Calculate key dashboard metrics"""
        if not self.processed:
            return {}
            
        total_claims = len(self.data)
        approved_claims = len(self.data[self.data['status'] == 'Approved'])
        pending_claims = len(self.data[self.data['status'] == 'Pending'])
        total_land_area = self.data['land_area_acres'].sum()
        avg_processing_time = self.data['processing_time_days'].mean()
        
        return {
            'total_claims': total_claims,
            'approved_claims': approved_claims,
            'pending_claims': pending_claims,
            'approval_rate': round((approved_claims / total_claims) * 100, 1),
            'total_land_area': round(total_land_area, 2),
            'avg_processing_time': round(avg_processing_time, 1)
        }
    
    def create_status_chart(self):
        """Create status distribution chart"""
        if not self.processed:
            return None
            
        status_counts = self.data['status'].value_counts()
        
        fig = px.pie(
            values=status_counts.values,
            names=status_counts.index,
            title="Claim Status Distribution",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        
        fig.update_layout(
            title_font_size=16,
            font=dict(size=12),
            showlegend=True
        )
        
        return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    def create_state_chart(self):
        """Create state-wise distribution chart"""
        if not self.processed:
            return None
            
        state_counts = self.data['state'].value_counts().head(10)
        
        fig = px.bar(
            x=state_counts.index,
            y=state_counts.values,
            title="Top 10 States by Claim Count",
            labels={'x': 'State', 'y': 'Number of Claims'},
            color=state_counts.values,
            color_continuous_scale='Blues'
        )
        
        fig.update_layout(
            title_font_size=16,
            font=dict(size=12),
            xaxis_tickangle=-45
        )
        
        return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    def create_map(self):
        """Create interactive map with claim locations"""
        if not self.processed:
            return None
            
        # Create base map centered on India
        m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)
        
        # Color mapping for status
        status_colors = {
            'Approved': 'green',
            'Pending': 'orange',
            'Under Review': 'blue',
            'Rejected': 'red',
            'Requires Additional Info': 'purple'
        }
        
        # Add markers for each claim
        for idx, row in self.data.iterrows():
            folium.CircleMarker(
                location=[row['latitude'], row['longitude']],
                radius=5,
                popup=f"""
                <b>Claim ID:</b> {row['claim_id']}<br>
                <b>Applicant:</b> {row['applicant_name']}<br>
                <b>State:</b> {row['state']}<br>
                <b>District:</b> {row['district']}<br>
                <b>Status:</b> {row['status']}<br>
                <b>Land Area:</b> {row['land_area_acres']} acres<br>
                <b>Community:</b> {row['tribal_community']}
                """,
                color=status_colors.get(row['status'], 'gray'),
                fill=True,
                fillColor=status_colors.get(row['status'], 'gray'),
                fillOpacity=0.7
            ).add_to(m)
        
        # Add legend
        legend_html = '''
        <div style="position: fixed; 
                    bottom: 50px; left: 50px; width: 150px; height: 120px; 
                    background-color: white; border:2px solid grey; z-index:9999; 
                    font-size:14px; padding: 10px">
        <p><b>Claim Status</b></p>
        <p><i class="fa fa-circle" style="color:green"></i> Approved</p>
        <p><i class="fa fa-circle" style="color:orange"></i> Pending</p>
        <p><i class="fa fa-circle" style="color:blue"></i> Under Review</p>
        <p><i class="fa fa-circle" style="color:red"></i> Rejected</p>
        </div>
        '''
        m.get_root().html.add_child(folium.Element(legend_html))
        
        return m._repr_html_()

# Initialize the system
dss_system = ADHIVANSystem()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_data')
def process_data():
    """Process sample data and return success status"""
    dss_system.generate_sample_data()
    return jsonify({'status': 'success', 'message': 'Sample data processed successfully!'})

@app.route('/dashboard_data')
def dashboard_data():
    """Get dashboard metrics and charts"""
    if not dss_system.processed:
        return jsonify({'error': 'Data not processed yet'})
    
    metrics = dss_system.get_dashboard_metrics()
    status_chart = dss_system.create_status_chart()
    state_chart = dss_system.create_state_chart()
    
    return jsonify({
        'metrics': metrics,
        'status_chart': status_chart,
        'state_chart': state_chart
    })

@app.route('/map')
def get_map():
    """Get interactive map"""
    if not dss_system.processed:
        return jsonify({'error': 'Data not processed yet'})
    
    map_html = dss_system.create_map()
    return jsonify({'map_html': map_html})

@app.route('/query', methods=['POST'])
def process_query():
    """Process natural language queries"""
    if not dss_system.processed:
        return jsonify({'error': 'Data not processed yet'})
    
    query = request.json.get('query', '').lower()
    
    # Simple query processing
    if 'total claims' in query or 'how many claims' in query:
        total = len(dss_system.data)
        return jsonify({'response': f'There are {total} total claims in the system.'})
    
    elif 'approval rate' in query:
        metrics = dss_system.get_dashboard_metrics()
        return jsonify({'response': f'The current approval rate is {metrics["approval_rate"]}%.'})
    
    elif 'pending' in query:
        pending = len(dss_system.data[dss_system.data['status'] == 'Pending'])
        return jsonify({'response': f'There are {pending} pending claims.'})
    
    elif 'approved' in query:
        approved = len(dss_system.data[dss_system.data['status'] == 'Approved'])
        return jsonify({'response': f'There are {approved} approved claims.'})
    
    elif 'land area' in query or 'total area' in query:
        total_area = dss_system.data['land_area_acres'].sum()
        return jsonify({'response': f'The total land area across all claims is {total_area:.2f} acres.'})
    
    elif 'district' in query:
        district_stats = dss_system.data['district'].value_counts().head(5)
        top_districts = ', '.join([f"{dist} ({count} claims)" for dist, count in district_stats.items()])
        return jsonify({'response': f'Top districts by claim count: {top_districts}'})
    
    elif 'tribal' in query or 'community' in query:
        tribal_stats = dss_system.data['tribal_community'].value_counts().head(5)
        top_communities = ', '.join([f"{comm} ({count} claims)" for comm, count in tribal_stats.items()])
        return jsonify({'response': f'Top tribal communities by claim count: {top_communities}'})
    
    else:
        return jsonify({'response': 'I can help you with queries about total claims, approval rates, pending claims, land area, districts, and tribal communities. Please try asking about these topics.'})

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)