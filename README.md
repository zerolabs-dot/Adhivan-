# ADHIVAN - Decision Support System (DSS)

A comprehensive Government Land Rights Management System for analyzing FRA (Forest Rights Act) claims with interactive geospatial visualization and intelligent analytics.

## 🚀 Features

- **Interactive Dashboard**: Real-time analytics and key performance indicators
- **Geospatial Mapping**: Interactive maps with claim locations and detailed hover information
- **Smart Analytics**: Comprehensive data visualization and trend analysis
- **Query Assistant**: Natural language processing for data queries
- **Document Generation**: Automated Patta document creation and download
- **Professional Reports**: Detailed reporting with export capabilities

## 📋 Requirements

- Python 3.8 or higher
- Required packages (see requirements.txt)

## 🛠️ Installation

1. **Clone or download the project files**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run dss_system.py
   ```

4. **Access the application:**
   - Open your web browser
   - Navigate to `http://localhost:8501`

## 📊 Usage

### Getting Started
1. **Process Sample Data**: Click "🔄 Process Sample Data" in the sidebar
2. **Explore Dashboard**: View key metrics and summary statistics
3. **Interactive Map**: Hover over markers for claim details, click to download Patta documents
4. **Analytics**: Explore comprehensive data visualizations
5. **Query Assistant**: Ask natural language questions about the data
6. **Reports**: Generate and export detailed reports

### Sample Queries
- "How many total claims are there?"
- "What is the approval rate?"
- "Show me district-wise statistics"
- "Which tribal communities have the most claims?"
- "What is the total land area?"

### Map Features
- **Hover**: View claim summary information
- **Click**: Access detailed claim information
- **Download**: Generate and download official Patta documents
- **Legend**: Color-coded status indicators

## 📁 Project Structure

```
├── dss_system.py              # Main application file
├── requirements.txt           # Python dependencies
├── sample_documents/          # Sample data folder
│   ├── README.md             # Documentation
│   ├── claim_data.json       # Sample claim data
│   ├── geospatial_boundaries.json  # Boundary data
│   └── tribal_demographics.json    # Demographic data
└── README.md                 # This file
```

## 🎯 Key Components

### Dashboard Features
- **Executive Summary**: Key metrics and performance indicators
- **Status Overview**: Claims distribution by status
- **Geographic Analysis**: District-wise claim distribution
- **Alert System**: High-priority notifications

### Interactive Map
- **Real-time Visualization**: Live claim locations
- **Detailed Popups**: Comprehensive claim information
- **Status Color Coding**: Visual status indicators
- **Document Download**: Direct Patta generation

### Analytics Engine
- **Temporal Analysis**: Submission and approval trends
- **Spatial Analysis**: Geographic distribution patterns
- **Performance Metrics**: Processing times and accuracy
- **Predictive Insights**: Conflict zone identification

### Query Assistant
- **Natural Language Processing**: Plain English queries
- **Intelligent Responses**: Contextual data analysis
- **Sample Queries**: Pre-built query examples
- **Real-time Results**: Instant data insights

## 🔧 Customization

The system can be customized for different regions or requirements:

1. **Data Sources**: Modify the `generate_sample_data()` method
2. **Visualizations**: Update chart configurations in `create_visualizations()`
3. **Map Styling**: Customize the `create_interactive_map()` method
4. **Query Patterns**: Extend the `query_processor()` method
5. **Document Templates**: Modify the `generate_patta_document()` method

## 📈 Performance

- **Data Processing**: Handles 500+ claims efficiently
- **Map Rendering**: Optimized for large datasets
- **Report Generation**: Sub-30 second standard reports
- **Query Response**: Real-time natural language processing

## 🛡️ Security

- Government-grade security considerations
- Data validation and sanitization
- Secure document generation
- Access control ready architecture

## 🤝 Support

For technical support or feature requests, please refer to the system documentation or contact the development team.

## 📄 License

This system is developed for government use and follows applicable data protection and security guidelines.

---

**ADHIVAN Decision Support System** - Empowering data-driven land rights decisions for better governance.