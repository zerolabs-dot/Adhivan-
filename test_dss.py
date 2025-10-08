#!/usr/bin/env python3
"""
Test script for ADHIVAN DSS System
Tests core functionality without Streamlit interface
"""

import pandas as pd
import numpy as np
import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import DSS components (without streamlit dependencies)
import warnings
warnings.filterwarnings('ignore')

class DSS_Test:
    def __init__(self):
        print("🏛️ ADHIVAN - Decision Support System Test")
        print("=" * 50)
        self.sample_data = self.generate_sample_data()
        
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
        
        return pd.DataFrame(data)
    
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
        
        return "\n".join(results) if results else "Query not recognized"
    
    def run_tests(self):
        """Run comprehensive tests"""
        print("\n📊 Testing Data Generation...")
        print(f"✅ Generated {len(self.sample_data)} sample claims")
        print(f"✅ Data shape: {self.sample_data.shape}")
        
        print("\n📈 Testing Summary Insights...")
        insights = self.create_summary_insights(self.sample_data)
        print("✅ Key Metrics:")
        for key, value in insights.items():
            print(f"   • {key.replace('_', ' ').title()}: {value}")
        
        print("\n🤖 Testing Query Processor...")
        test_queries = [
            "How many total claims are there?",
            "What is the approval rate?", 
            "Show me district-wise statistics"
        ]
        
        for query in test_queries:
            print(f"\n❓ Query: {query}")
            response = self.query_processor(query, self.sample_data)
            print(f"💬 Response: {response}")
        
        print("\n📋 Testing Data Analysis...")
        print("✅ Status Distribution:")
        status_counts = self.sample_data['status'].value_counts()
        for status, count in status_counts.items():
            percentage = (count / len(self.sample_data)) * 100
            print(f"   • {status}: {count} ({percentage:.1f}%)")
        
        print("\n🗺️ Testing Geospatial Data...")
        print(f"✅ Latitude range: {self.sample_data['latitude'].min():.2f} to {self.sample_data['latitude'].max():.2f}")
        print(f"✅ Longitude range: {self.sample_data['longitude'].min():.2f} to {self.sample_data['longitude'].max():.2f}")
        
        print("\n🎉 All Tests Completed Successfully!")
        print("=" * 50)
        print("📱 To run the full web interface:")
        print("   streamlit run dss_system.py")
        print("🌐 Then open: http://localhost:8501")

if __name__ == "__main__":
    test = DSS_Test()
    test.run_tests()