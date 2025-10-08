// FRA Atlas Application JavaScript

// Enhanced FRA data with coordinates and claimant details
const fraData2023 = [
    {
        state: "Andhra Pradesh", 
        individualClaims: 284294, 
        communityClaims: 3294, 
        totalClaims: 287588, 
        individualTitles: 225826, 
        communityTitles: 1822, 
        totalTitles: 227648, 
        landArea: 980495,
        coordinates: [15.9129, 79.7400],
        recentClaimants: [
            {name: "Ravi Kumar", village: "Araku Valley", claimType: "Individual", landArea: 2.5, status: "Approved"},
            {name: "Tribal Community", village: "Paderu", claimType: "Community", landArea: 45.2, status: "Under Review"},
            {name: "Lakshmi Devi", village: "Chintapalli", claimType: "Individual", landArea: 1.8, status: "Approved"}
        ]
    },
    {
        state: "Assam", 
        individualClaims: 148965, 
        communityClaims: 6046, 
        totalClaims: 155011, 
        individualTitles: 57325, 
        communityTitles: 1477, 
        totalTitles: 58802, 
        landArea: 125000,
        coordinates: [26.2006, 92.9376],
        recentClaimants: [
            {name: "Bodo Community", village: "Kokrajhar", claimType: "Community", landArea: 78.5, status: "Approved"},
            {name: "Rani Sharma", village: "Jorhat", claimType: "Individual", landArea: 3.2, status: "Pending"},
            {name: "Tea Garden Workers", village: "Dibrugarh", claimType: "Community", landArea: 156.7, status: "Under Review"}
        ]
    },
    {
        state: "Bihar", 
        individualClaims: 8022, 
        communityClaims: 0, 
        totalClaims: 8022, 
        individualTitles: 121, 
        communityTitles: 0, 
        totalTitles: 121, 
        landArea: 5000,
        coordinates: [25.0961, 85.3131],
        recentClaimants: [
            {name: "Santhal Community", village: "Jamui", claimType: "Individual", landArea: 1.2, status: "Approved"},
            {name: "Ram Singh", village: "Kaimur", claimType: "Individual", landArea: 0.8, status: "Pending"}
        ]
    },
    {
        state: "Chhattisgarh", 
        individualClaims: 883938, 
        communityClaims: 53920, 
        totalClaims: 937858, 
        individualTitles: 475100, 
        communityTitles: 49241, 
        totalTitles: 524341, 
        landArea: 6090348.55,
        coordinates: [21.2787, 81.8661],
        recentClaimants: [
            {name: "Gond Tribal Community", village: "Bastar", claimType: "Community", landArea: 234.5, status: "Approved"},
            {name: "Sita Devi", village: "Dantewada", claimType: "Individual", landArea: 4.2, status: "Approved"},
            {name: "Korku Community", village: "Surguja", claimType: "Community", landArea: 189.3, status: "Under Review"}
        ]
    },
    {
        state: "Goa", 
        individualClaims: 9758, 
        communityClaims: 378, 
        totalClaims: 10136, 
        individualTitles: 472, 
        communityTitles: 13, 
        totalTitles: 485, 
        landArea: 902.53,
        coordinates: [15.2993, 74.1240],
        recentClaimants: [
            {name: "Fishing Community", village: "Canacona", claimType: "Community", landArea: 12.3, status: "Approved"},
            {name: "Maria Santos", village: "Sanguem", claimType: "Individual", landArea: 0.5, status: "Pending"}
        ]
    },
    {
        state: "Gujarat", 
        individualClaims: 182869, 
        communityClaims: 7187, 
        totalClaims: 190056, 
        individualTitles: 96559, 
        communityTitles: 4791, 
        totalTitles: 101350, 
        landArea: 1404189.01,
        coordinates: [23.0225, 72.5714],
        recentClaimants: [
            {name: "Bhil Community", village: "Dahod", claimType: "Community", landArea: 145.7, status: "Approved"},
            {name: "Kiran Patel", village: "Panchmahals", claimType: "Individual", landArea: 2.8, status: "Under Review"},
            {name: "Adivasi Collective", village: "Valsad", claimType: "Community", landArea: 98.4, status: "Approved"}
        ]
    },
    {
        state: "Himachal Pradesh", 
        individualClaims: 4880, 
        communityClaims: 466, 
        totalClaims: 5346, 
        individualTitles: 256, 
        communityTitles: 59, 
        totalTitles: 315, 
        landArea: 11231.66,
        coordinates: [31.1048, 77.1734],
        recentClaimants: [
            {name: "Mountain Community", village: "Kinnaur", claimType: "Community", landArea: 23.5, status: "Approved"},
            {name: "Devi Singh", village: "Lahaul Spiti", claimType: "Individual", landArea: 1.5, status: "Pending"}
        ]
    },
    {
        state: "Jharkhand", 
        individualClaims: 107032, 
        communityClaims: 3724, 
        totalClaims: 110756, 
        individualTitles: 59866, 
        communityTitles: 2104, 
        totalTitles: 61970, 
        landArea: 257154.83,
        coordinates: [23.6102, 85.2799],
        recentClaimants: [
            {name: "Santal Community", village: "Dumka", claimType: "Community", landArea: 67.8, status: "Approved"},
            {name: "Birsa Munda", village: "Khunti", claimType: "Individual", landArea: 3.4, status: "Approved"},
            {name: "Ho Tribal Group", village: "West Singhbhum", claimType: "Community", landArea: 123.6, status: "Under Review"}
        ]
    },
    {
        state: "Karnataka", 
        individualClaims: 288549, 
        communityClaims: 5940, 
        totalClaims: 294489, 
        individualTitles: 14981, 
        communityTitles: 1345, 
        totalTitles: 16326, 
        landArea: 56417.82,
        coordinates: [15.3173, 75.7139],
        recentClaimants: [
            {name: "Soliga Community", village: "Chamarajanagar", claimType: "Community", landArea: 89.2, status: "Approved"},
            {name: "Rajesh Kumar", village: "Kodagu", claimType: "Individual", landArea: 2.1, status: "Pending"},
            {name: "Tribal Collective", village: "Uttara Kannada", claimType: "Community", landArea: 156.8, status: "Under Review"}
        ]
    },
    {
        state: "Kerala", 
        individualClaims: 45678, 
        communityClaims: 2345, 
        totalClaims: 48023, 
        individualTitles: 23456, 
        communityTitles: 1234, 
        totalTitles: 24690, 
        landArea: 125000,
        coordinates: [10.8505, 76.2711],
        recentClaimants: [
            {name: "Adivasi Community", village: "Wayanad", claimType: "Community", landArea: 45.6, status: "Approved"},
            {name: "Ravi Nair", village: "Idukki", claimType: "Individual", landArea: 2.3, status: "Pending"}
        ]
    },
    {
        state: "Madhya Pradesh", 
        individualClaims: 567890, 
        communityClaims: 34567, 
        totalClaims: 602457, 
        individualTitles: 345678, 
        communityTitles: 23456, 
        totalTitles: 369134, 
        landArea: 2500000,
        coordinates: [22.9734, 78.6569],
        recentClaimants: [
            {name: "Gond Community", village: "Mandla", claimType: "Community", landArea: 234.5, status: "Approved"},
            {name: "Bhil Tribe", village: "Jhabua", claimType: "Community", landArea: 189.3, status: "Under Review"}
        ]
    },
    {
        state: "Maharashtra", 
        individualClaims: 234567, 
        communityClaims: 12345, 
        totalClaims: 246912, 
        individualTitles: 123456, 
        communityTitles: 6789, 
        totalTitles: 130245, 
        landArea: 890000,
        coordinates: [19.7515, 75.7139],
        recentClaimants: [
            {name: "Warli Community", village: "Thane", claimType: "Community", landArea: 67.8, status: "Approved"},
            {name: "Kokna Tribe", village: "Nashik", claimType: "Community", landArea: 45.2, status: "Pending"}
        ]
    },
    {
        state: "Odisha", 
        individualClaims: 456789, 
        communityClaims: 23456, 
        totalClaims: 480245, 
        individualTitles: 234567, 
        communityTitles: 12345, 
        totalTitles: 246912, 
        landArea: 1800000,
        coordinates: [20.9517, 85.0985],
        recentClaimants: [
            {name: "Kondh Community", village: "Kandhamal", claimType: "Community", landArea: 123.4, status: "Approved"},
            {name: "Santhal Tribe", village: "Mayurbhanj", claimType: "Community", landArea: 89.7, status: "Under Review"}
        ]
    }
];

// Global variables
let map;
let currentLayer;
let infoPanel;

// Initialize the interactive map
function initializeMap() {
    try {
        // Initialize map centered on India
        map = L.map('map').setView([20.5937, 78.9629], 5);
        
        // Add OpenStreetMap tiles
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
        }).addTo(map);
        
        // Wait for claimant data to load, then add individual markers
        setTimeout(() => {
            if (window.FRAClaimants && window.FRAClaimants.length > 0) {
                addIndividualClaimantMarkers();
                console.log(`Added ${window.FRAClaimants.length} individual claimant markers`);
            } else {
                console.log('Claimant data not loaded, adding state markers as fallback');
                addStateMarkers();
            }
        }, 1000);
        
        // Show info panel
        infoPanel = document.getElementById('infoPanel');
        if (infoPanel) {
            infoPanel.style.display = 'block';
        }
        
        console.log('Map initialized successfully');
    } catch (error) {
        console.error('Error initializing map:', error);
    }
}

// Add individual claimant markers to the map
function addIndividualClaimantMarkers() {
    if (!window.FRAClaimants) return;
    
    console.log('Adding individual claimant markers...');
    
    window.FRAClaimants.forEach(claimant => {
        // Determine marker color based on claim status
        let color = '#95a5a6'; // Default gray
        switch(claimant.status) {
            case 'Approved':
                color = '#27ae60'; // Green
                break;
            case 'Under Review':
                color = '#f39c12'; // Orange
                break;
            case 'Pending':
                color = '#3498db'; // Blue
                break;
            case 'Rejected':
                color = '#e74c3c'; // Red
                break;
            case 'Documentation Required':
                color = '#9b59b6'; // Purple
                break;
        }
        
        // Determine marker size based on land area
        const landArea = parseFloat(claimant.landArea);
        const radius = Math.max(3, Math.min(8, landArea * 2)); // Size between 3-8 pixels
        
        // Create circle marker for each claimant
        const marker = L.circleMarker(claimant.coordinates, {
            radius: radius,
            fillColor: color,
            color: '#2c3e50',
            weight: 1,
            opacity: 0.8,
            fillOpacity: 0.6
        }).addTo(map);
        
        // Add hover events
        marker.on('mouseover', function() {
            showClaimantInfo(claimant);
            this.setStyle({
                weight: 3,
                fillOpacity: 0.9,
                radius: radius + 2
            });
        });
        
        marker.on('mouseout', function() {
            this.setStyle({
                weight: 1,
                fillOpacity: 0.6,
                radius: radius
            });
        });
        
        // Add click event for detailed view
        marker.on('click', function() {
            viewClaimantDetails(claimant.claimId);
        });
        
        // Add tooltip with claimant information
        marker.bindTooltip(`
            <div style="font-size: 12px;">
                <strong>${claimant.name}</strong><br>
                <strong>ID:</strong> ${claimant.claimId}<br>
                <strong>Tribe:</strong> ${claimant.tribe}<br>
                <strong>Village:</strong> ${claimant.village}<br>
                <strong>Land:</strong> ${claimant.landArea} ha<br>
                <strong>Status:</strong> ${claimant.status}<br>
                <strong>Type:</strong> ${claimant.claimType}
            </div>
        `, {
            permanent: false,
            direction: 'top',
            offset: [0, -10]
        });
    });
}

// Fallback function to add state markers if claimant data is not available
function addStateMarkers() {
    fraData2023.forEach(stateData => {
        const successRate = stateData.totalClaims > 0 ? (stateData.totalTitles / stateData.totalClaims * 100) : 0;
        
        // Determine color based on success rate
        let color = '#95a5a6'; // Default gray
        if (successRate > 70) color = '#27ae60'; // Green
        else if (successRate > 40) color = '#f39c12'; // Orange
        else if (successRate > 0) color = '#e74c3c'; // Red
        
        // Create circle marker
        const marker = L.circleMarker(stateData.coordinates, {
            radius: Math.sqrt(stateData.totalClaims / 10000) + 5,
            fillColor: color,
            color: '#2c3e50',
            weight: 2,
            opacity: 1,
            fillOpacity: 0.7
        }).addTo(map);
        
        // Add hover events
        marker.on('mouseover', function() {
            showStateInfo(stateData);
            this.setStyle({
                weight: 4,
                fillOpacity: 0.9
            });
        });
        
        marker.on('mouseout', function() {
            this.setStyle({
                weight: 2,
                fillOpacity: 0.7
            });
        });
        
        // Add click event for detailed view
        marker.on('click', function() {
            showDetailedStateInfo(stateData);
        });
        
        // Add tooltip
        marker.bindTooltip(`
            <strong>${stateData.state}</strong><br>
            Claims: ${formatNumber(stateData.totalClaims)}<br>
            Success Rate: ${successRate.toFixed(1)}%
        `, {
            permanent: false,
            direction: 'top'
        });
    });
}

// Show state information in the info panel
function showStateInfo(stateData) {
    const successRate = stateData.totalClaims > 0 ? (stateData.totalTitles / stateData.totalClaims * 100) : 0;
    
    const elements = {
        stateName: document.getElementById('stateName'),
        totalClaims: document.getElementById('totalClaims'),
        individualClaims: document.getElementById('individualClaims'),
        communityClaims: document.getElementById('communityClaims'),
        titlesDistributed: document.getElementById('titlesDistributed'),
        successRate: document.getElementById('successRate'),
        landArea: document.getElementById('landArea')
    };
    
    if (elements.stateName) elements.stateName.textContent = stateData.state;
    if (elements.totalClaims) elements.totalClaims.textContent = formatNumber(stateData.totalClaims);
    if (elements.individualClaims) elements.individualClaims.textContent = formatNumber(stateData.individualClaims);
    if (elements.communityClaims) elements.communityClaims.textContent = formatNumber(stateData.communityClaims);
    if (elements.titlesDistributed) elements.titlesDistributed.textContent = formatNumber(stateData.totalTitles);
    if (elements.successRate) elements.successRate.textContent = successRate.toFixed(1) + '%';
    if (elements.landArea) elements.landArea.textContent = formatNumber(stateData.landArea);
    
    // Show recent claimants from fabricated data
    const claimantsDiv = document.getElementById('recentClaimants');
    if (claimantsDiv) {
        claimantsDiv.innerHTML = '';
        
        // Get real claimants from fabricated data for this state
        if (window.FRAClaimants) {
            const stateClaimants = window.FRAClaimants
                .filter(c => c.state === stateData.state)
                .slice(0, 5); // Show first 5 claimants
            
            if (stateClaimants.length > 0) {
                stateClaimants.forEach(claimant => {
                    const claimantDiv = document.createElement('div');
                    claimantDiv.style.marginBottom = '0.5rem';
                    claimantDiv.style.padding = '0.5rem';
                    claimantDiv.style.background = '#f8f9fa';
                    claimantDiv.style.borderRadius = '4px';
                    claimantDiv.style.cursor = 'pointer';
                    claimantDiv.onclick = () => viewClaimantDetails(claimant.claimId);
                    claimantDiv.innerHTML = `
                        <strong>${claimant.name}</strong> - ${claimant.village}<br>
                        <small>${claimant.tribe} | ${claimant.landArea} ha | ${claimant.status}</small>
                    `;
                    claimantsDiv.appendChild(claimantDiv);
                });
            } else {
                claimantsDiv.innerHTML = '<em>No claimant data available for this state</em>';
            }
        } else if (stateData.recentClaimants && stateData.recentClaimants.length > 0) {
            // Fallback to original data
            stateData.recentClaimants.forEach(claimant => {
                const claimantDiv = document.createElement('div');
                claimantDiv.style.marginBottom = '0.5rem';
                claimantDiv.style.padding = '0.5rem';
                claimantDiv.style.background = '#f8f9fa';
                claimantDiv.style.borderRadius = '4px';
                claimantDiv.innerHTML = `
                    <strong>${claimant.name}</strong> - ${claimant.village}<br>
                    <small>${claimant.claimType} | ${claimant.landArea} acres | ${claimant.status}</small>
                `;
                claimantsDiv.appendChild(claimantDiv);
            });
        } else {
            claimantsDiv.innerHTML = '<em>Loading claimant data...</em>';
        }
    }
}

// Show individual claimant information in the info panel
function showClaimantInfo(claimant) {
    const elements = {
        stateName: document.getElementById('stateName'),
        totalClaims: document.getElementById('totalClaims'),
        individualClaims: document.getElementById('individualClaims'),
        communityClaims: document.getElementById('communityClaims'),
        titlesDistributed: document.getElementById('titlesDistributed'),
        successRate: document.getElementById('successRate'),
        landArea: document.getElementById('landArea')
    };
    
    // Update info panel with claimant details
    if (elements.stateName) elements.stateName.textContent = `${claimant.name} (${claimant.claimId})`;
    if (elements.totalClaims) elements.totalClaims.textContent = claimant.tribe;
    if (elements.individualClaims) elements.individualClaims.textContent = claimant.village;
    if (elements.communityClaims) elements.communityClaims.textContent = claimant.district;
    if (elements.titlesDistributed) elements.titlesDistributed.textContent = claimant.state;
    if (elements.successRate) elements.successRate.textContent = claimant.status;
    if (elements.landArea) elements.landArea.textContent = claimant.landArea + ' ha';
    
    // Update labels to match claimant data
    const labels = document.querySelectorAll('.info-label');
    if (labels.length >= 6) {
        labels[0].textContent = 'Tribe/Community';
        labels[1].textContent = 'Village';
        labels[2].textContent = 'District';
        labels[3].textContent = 'State';
        labels[4].textContent = 'Status';
        labels[5].textContent = 'Land Area';
    }
    
    // Show claimant details in recent claimants section
    const claimantsDiv = document.getElementById('recentClaimants');
    if (claimantsDiv) {
        claimantsDiv.innerHTML = `
            <div style="background: #f8f9fa; padding: 1rem; border-radius: 8px;">
                <h4 style="color: #2c3e50; margin-bottom: 0.5rem;">Claimant Details</h4>
                <p><strong>Claim Type:</strong> ${claimant.claimType}</p>
                <p><strong>Application Date:</strong> ${claimant.applicationDate}</p>
                <p><strong>Years in Area:</strong> ${claimant.yearsInArea} years</p>
                <p><strong>Traditional Occupation:</strong> ${claimant.occupation}</p>
                <p><strong>Coordinates:</strong> ${claimant.coordinates[0].toFixed(4)}°N, ${claimant.coordinates[1].toFixed(4)}°E</p>
                
                <div style="margin-top: 1rem;">
                    <strong>Supporting Documents:</strong><br>
                    <div style="display: flex; flex-wrap: wrap; gap: 0.25rem; margin-top: 0.5rem;">
                        ${claimant.documents.map(doc => `
                            <span style="background: #e9ecef; padding: 0.2rem 0.4rem; border-radius: 10px; font-size: 0.7rem;">
                                ${doc}
                            </span>
                        `).join('')}
                    </div>
                </div>
                
                <button onclick="viewClaimantDetails('${claimant.claimId}')" 
                        style="margin-top: 1rem; padding: 0.5rem 1rem; background: #27ae60; color: white; border: none; border-radius: 5px; cursor: pointer;">
                    <i class="fas fa-eye"></i> View Full Details
                </button>
            </div>
        `;
    }
}

// Show detailed state information
function showDetailedStateInfo(stateData) {
    alert(`Detailed information for ${stateData.state} would open here.\n\nThis could include:\n- District-wise breakdown\n- Historical trends\n- Detailed claimant lists\n- Land use patterns`);
}

// Update map view based on selected criteria
function updateMapView() {
    const viewType = document.getElementById('viewType');
    if (viewType) {
        console.log('Updating map view to:', viewType.value);
        // This function would update the map visualization based on the selected view type
    }
}

// Filter map markers based on status and state
function filterMapMarkers() {
    const statusFilter = document.getElementById('statusFilter')?.value || '';
    const stateFilter = document.getElementById('mapStateFilter')?.value || '';
    
    if (!map || !window.FRAClaimants) return;
    
    // Clear existing markers
    map.eachLayer(layer => {
        if (layer instanceof L.CircleMarker) {
            map.removeLayer(layer);
        }
    });
    
    // Filter claimants based on selected criteria
    const filteredClaimants = window.FRAClaimants.filter(claimant => {
        const matchesStatus = !statusFilter || claimant.status === statusFilter;
        const matchesState = !stateFilter || claimant.state === stateFilter;
        return matchesStatus && matchesState;
    });
    
    console.log(`Showing ${filteredClaimants.length} claimants on map`);
    
    // Add filtered markers
    filteredClaimants.forEach(claimant => {
        // Determine marker color based on claim status
        let color = '#95a5a6'; // Default gray
        switch(claimant.status) {
            case 'Approved':
                color = '#27ae60'; // Green
                break;
            case 'Under Review':
                color = '#f39c12'; // Orange
                break;
            case 'Pending':
                color = '#3498db'; // Blue
                break;
            case 'Rejected':
                color = '#e74c3c'; // Red
                break;
            case 'Documentation Required':
                color = '#9b59b6'; // Purple
                break;
        }
        
        // Determine marker size based on land area
        const landArea = parseFloat(claimant.landArea);
        const radius = Math.max(3, Math.min(8, landArea * 2)); // Size between 3-8 pixels
        
        // Create circle marker for each claimant
        const marker = L.circleMarker(claimant.coordinates, {
            radius: radius,
            fillColor: color,
            color: '#2c3e50',
            weight: 1,
            opacity: 0.8,
            fillOpacity: 0.6
        }).addTo(map);
        
        // Add hover events
        marker.on('mouseover', function() {
            showClaimantInfo(claimant);
            this.setStyle({
                weight: 3,
                fillOpacity: 0.9,
                radius: radius + 2
            });
        });
        
        marker.on('mouseout', function() {
            this.setStyle({
                weight: 1,
                fillOpacity: 0.6,
                radius: radius
            });
        });
        
        // Add click event for detailed view
        marker.on('click', function() {
            viewClaimantDetails(claimant.claimId);
        });
        
        // Add tooltip with claimant information
        marker.bindTooltip(`
            <div style="font-size: 12px;">
                <strong>${claimant.name}</strong><br>
                <strong>ID:</strong> ${claimant.claimId}<br>
                <strong>Tribe:</strong> ${claimant.tribe}<br>
                <strong>Village:</strong> ${claimant.village}<br>
                <strong>Land:</strong> ${claimant.landArea} ha<br>
                <strong>Status:</strong> ${claimant.status}<br>
                <strong>Type:</strong> ${claimant.claimType}
            </div>
        `, {
            permanent: false,
            direction: 'top',
            offset: [0, -10]
        });
    });
    
    // Update info panel with filter summary
    const infoPanel = document.getElementById('infoPanel');
    if (infoPanel && filteredClaimants.length > 0) {
        const summary = `Showing ${filteredClaimants.length} claimants`;
        document.getElementById('stateName').textContent = summary;
    }
}

// Navigation functions
function showPage(pageId) {
    // Hide all pages
    const pages = document.querySelectorAll('.page');
    pages.forEach(page => page.classList.remove('active'));
    
    // Show selected page
    const targetPage = document.getElementById(pageId);
    if (targetPage) {
        targetPage.classList.add('active');
    }
    
    // Update navigation - find the clicked link
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => link.classList.remove('active'));
    
    // Find and activate the correct nav link
    const activeLink = document.querySelector(`[onclick="showPage('${pageId}')"]`);
    if (activeLink) {
        activeLink.classList.add('active');
    }
    
    // Load page-specific data
    switch(pageId) {
        case 'atlas':
            setTimeout(() => {
                if (!map) {
                    initializeMap();
                }
                loadNationalStats();
            }, 100);
            break;
        case 'dashboard':
            console.log('Switching to dashboard page...');
            setTimeout(() => {
                loadDashboardData();
                // Debug: Check if canvas elements exist
                console.log('Canvas elements check:');
                console.log('individualRightsChart:', document.getElementById('individualRightsChart'));
                console.log('communityRightsChart:', document.getElementById('communityRightsChart'));
                console.log('forestLandChart:', document.getElementById('forestLandChart'));
                console.log('claimsStatusChart:', document.getElementById('claimsStatusChart'));
            }, 200);
            break;
        case 'claims':
            loadClaimsData();
            break;
        case 'titles':
            loadTitlesData();
            break;
        case 'claimants':
            loadClaimantsPage();
            break;
    }
}

// Load national statistics
function loadNationalStats() {
    const totalStates = fraData2023.length;
    const totalClaims = fraData2023.reduce((sum, state) => sum + state.totalClaims, 0);
    const totalTitles = fraData2023.reduce((sum, state) => sum + state.totalTitles, 0);
    const totalLand = fraData2023.reduce((sum, state) => sum + state.landArea, 0);
    
    const elements = {
        nationalTotalStates: document.getElementById('nationalTotalStates'),
        nationalTotalClaims: document.getElementById('nationalTotalClaims'),
        nationalTotalTitles: document.getElementById('nationalTotalTitles'),
        nationalTotalLand: document.getElementById('nationalTotalLand')
    };
    
    if (elements.nationalTotalStates) elements.nationalTotalStates.textContent = totalStates;
    if (elements.nationalTotalClaims) elements.nationalTotalClaims.textContent = formatNumber(totalClaims);
    if (elements.nationalTotalTitles) elements.nationalTotalTitles.textContent = formatNumber(totalTitles);
    if (elements.nationalTotalLand) elements.nationalTotalLand.textContent = formatNumber(Math.round(totalLand / 1000000)) + 'M';
}

// Dashboard functions
function updateDashboard() {
    const dashboardType = document.getElementById('dashboardType');
    if (dashboardType) {
        console.log('Updating dashboard to:', dashboardType.value);
        showDashboardLoading();
        
        // Simulate loading time
        setTimeout(() => {
            hideDashboardLoading();
            loadDashboardCharts();
        }, 1500);
    }
}

function refreshDashboard() {
    showDashboardLoading();
    
    // Simulate refresh
    setTimeout(() => {
        hideDashboardLoading();
        updateDashboardStats();
        
        // Force refresh charts
        if (typeof forceRefreshCharts === 'function') {
            forceRefreshCharts();
        } else {
            loadDashboardCharts();
        }
    }, 1000);
}

function showDashboardLoading() {
    const loading = document.getElementById('dashboardLoading');
    if (loading) {
        loading.style.display = 'flex';
    }
}

function hideDashboardLoading() {
    const loading = document.getElementById('dashboardLoading');
    if (loading) {
        loading.style.display = 'none';
    }
}

function updateDashboardStats() {
    const totalStates = fraData2023.length;
    const totalClaims = fraData2023.reduce((sum, state) => sum + state.totalClaims, 0);
    const totalTitles = fraData2023.reduce((sum, state) => sum + state.totalTitles, 0);
    const totalLand = fraData2023.reduce((sum, state) => sum + state.landArea, 0);
    const successRate = totalClaims > 0 ? (totalTitles / totalClaims * 100) : 0;
    
    const elements = {
        dashboardClaims: document.getElementById('dashboardClaims'),
        dashboardTitles: document.getElementById('dashboardTitles'),
        dashboardSuccess: document.getElementById('dashboardSuccess'),
        dashboardLand: document.getElementById('dashboardLand')
    };
    
    if (elements.dashboardClaims) elements.dashboardClaims.textContent = formatNumber(totalClaims);
    if (elements.dashboardTitles) elements.dashboardTitles.textContent = formatNumber(totalTitles);
    if (elements.dashboardSuccess) elements.dashboardSuccess.textContent = successRate.toFixed(1) + '%';
    if (elements.dashboardLand) elements.dashboardLand.textContent = formatNumber(Math.round(totalLand / 1000000)) + 'M';
}

function loadDashboardCharts() {
    console.log('Loading dashboard charts...');
    setTimeout(() => {
        createIndividualRightsChart();
        createCommunityRightsChart();
        createForestLandChart();
        createClaimsStatusChart();
    }, 100);
}

function createStateProgressChart() {
    const canvas = document.getElementById('stateProgressChart');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    
    ctx.clearRect(0, 0, width, height);
    
    const topStates = fraData2023
        .map(state => ({
            name: state.state.length > 10 ? state.state.substring(0, 10) + '...' : state.state,
            successRate: state.totalClaims > 0 ? (state.totalTitles / state.totalClaims * 100) : 0
        }))
        .sort((a, b) => b.successRate - a.successRate)
        .slice(0, 8);
    
    const barWidth = width / topStates.length - 10;
    const maxRate = Math.max(...topStates.map(s => s.successRate));
    
    topStates.forEach((state, index) => {
        const barHeight = (state.successRate / maxRate) * (height - 60);
        const x = index * (barWidth + 10) + 5;
        const y = height - barHeight - 30;
        
        ctx.fillStyle = '#27ae60';
        ctx.fillRect(x, y, barWidth, barHeight);
        
        ctx.fillStyle = '#2c3e50';
        ctx.font = '10px Arial';
        ctx.save();
        ctx.translate(x + barWidth/2, height - 5);
        ctx.rotate(-Math.PI/4);
        ctx.textAlign = 'right';
        ctx.fillText(state.name, 0, 0);
        ctx.restore();
        
        ctx.fillStyle = '#2c3e50';
        ctx.font = '10px Arial';
        ctx.textAlign = 'center';
        ctx.fillText(state.successRate.toFixed(1) + '%', x + barWidth/2, y - 5);
    });
}

function createMonthlyTrendsChart() {
    const canvas = document.getElementById('monthlyTrendsChart');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    
    ctx.clearRect(0, 0, width, height);
    
    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    const data = [45, 52, 48, 61, 55, 67, 73, 69, 78, 82, 76, 85];
    
    const maxValue = Math.max(...data);
    const stepX = width / (months.length - 1);
    const stepY = (height - 40) / maxValue;
    
    // Draw line
    ctx.beginPath();
    ctx.strokeStyle = '#27ae60';
    ctx.lineWidth = 3;
    
    data.forEach((value, index) => {
        const x = index * stepX;
        const y = height - 20 - (value * stepY);
        
        if (index === 0) {
            ctx.moveTo(x, y);
        } else {
            ctx.lineTo(x, y);
        }
        
        // Draw points
        ctx.fillStyle = '#27ae60';
        ctx.beginPath();
        ctx.arc(x, y, 4, 0, 2 * Math.PI);
        ctx.fill();
        
        // Draw labels
        ctx.fillStyle = '#2c3e50';
        ctx.font = '10px Arial';
        ctx.textAlign = 'center';
        ctx.fillText(months[index], x, height - 5);
        ctx.fillText(value + '%', x, y - 10);
    });
    
    ctx.stroke();
}

function createClaimTypesChart() {
    const canvas = document.getElementById('claimTypesChart');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    
    ctx.clearRect(0, 0, width, height);
    
    const totalIndividual = fraData2023.reduce((sum, state) => sum + state.individualClaims, 0);
    const totalCommunity = fraData2023.reduce((sum, state) => sum + state.communityClaims, 0);
    const total = totalIndividual + totalCommunity;
    
    const individualPercent = (totalIndividual / total) * 100;
    const communityPercent = (totalCommunity / total) * 100;
    
    const centerX = width / 2;
    const centerY = height / 2;
    const radius = Math.min(width, height) / 3;
    
    // Draw Individual Claims slice
    ctx.beginPath();
    ctx.moveTo(centerX, centerY);
    ctx.arc(centerX, centerY, radius, 0, (individualPercent / 100) * 2 * Math.PI);
    ctx.closePath();
    ctx.fillStyle = '#27ae60';
    ctx.fill();
    
    // Draw Community Claims slice
    ctx.beginPath();
    ctx.moveTo(centerX, centerY);
    ctx.arc(centerX, centerY, radius, (individualPercent / 100) * 2 * Math.PI, 2 * Math.PI);
    ctx.closePath();
    ctx.fillStyle = '#2ecc71';
    ctx.fill();
    
    // Draw labels
    ctx.fillStyle = '#2c3e50';
    ctx.font = '12px Arial';
    ctx.textAlign = 'center';
    ctx.fillText(`Individual: ${individualPercent.toFixed(1)}%`, centerX, centerY + radius + 20);
    ctx.fillText(`Community: ${communityPercent.toFixed(1)}%`, centerX, centerY + radius + 35);
}

// Dashboard functions
function loadDashboardData() {
    console.log('Loading dashboard data...');
    const totalStates = fraData2023.length;
    const totalClaims = fraData2023.reduce((sum, state) => sum + state.totalClaims, 0);
    const totalTitles = fraData2023.reduce((sum, state) => sum + state.totalTitles, 0);
    const totalLand = fraData2023.reduce((sum, state) => sum + state.landArea, 0);
    
    const elements = {
        dashTotalStates: document.getElementById('dashTotalStates'),
        dashTotalClaims: document.getElementById('dashTotalClaims'),
        dashTotalTitles: document.getElementById('dashTotalTitles'),
        dashTotalLand: document.getElementById('dashTotalLand')
    };
    
    if (elements.dashTotalStates) elements.dashTotalStates.textContent = totalStates;
    if (elements.dashTotalClaims) elements.dashTotalClaims.textContent = formatNumber(totalClaims);
    if (elements.dashTotalTitles) elements.dashTotalTitles.textContent = formatNumber(totalTitles);
    if (elements.dashTotalLand) elements.dashTotalLand.textContent = formatNumber(Math.round(totalLand / 1000000)) + 'M';
    
    updateDashboardStats();
    
    // Load charts with a delay to ensure DOM is ready
    setTimeout(() => {
        loadDashboardCharts();
    }, 500);
}

function createProgressChart() {
    const canvas = document.getElementById('progressChart');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    
    ctx.clearRect(0, 0, width, height);
    
    const topStates = fraData2023
        .map(state => ({
            name: state.state,
            successRate: state.totalClaims > 0 ? (state.totalTitles / state.totalClaims * 100) : 0
        }))
        .sort((a, b) => b.successRate - a.successRate)
        .slice(0, 10);
    
    const barWidth = width / topStates.length - 10;
    const maxRate = Math.max(...topStates.map(s => s.successRate));
    
    topStates.forEach((state, index) => {
        const barHeight = (state.successRate / maxRate) * (height - 60);
        const x = index * (barWidth + 10) + 5;
        const y = height - barHeight - 30;
        
        ctx.fillStyle = '#27ae60';
        ctx.fillRect(x, y, barWidth, barHeight);
        
        ctx.fillStyle = '#2c3e50';
        ctx.font = '10px Arial';
        ctx.save();
        ctx.translate(x + barWidth/2, height - 5);
        ctx.rotate(-Math.PI/4);
        ctx.textAlign = 'right';
        ctx.fillText(state.name, 0, 0);
        ctx.restore();
        
        ctx.fillStyle = '#2c3e50';
        ctx.font = '12px Arial';
        ctx.textAlign = 'center';
        ctx.fillText(state.successRate.toFixed(1) + '%', x + barWidth/2, y - 5);
    });
    
    ctx.fillStyle = '#2c3e50';
    ctx.font = 'bold 16px Arial';
    ctx.textAlign = 'center';
    ctx.fillText('Top 10 States by Success Rate (%)', width/2, 20);
}

// Claims analysis functions
function loadClaimsData() {
    const tableBody = document.getElementById('claimsTableBody');
    if (!tableBody) return;
    
    tableBody.innerHTML = '';
    
    fraData2023.forEach(state => {
        const successRate = state.totalClaims > 0 ? (state.totalTitles / state.totalClaims * 100) : 0;
        
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${state.state}</td>
            <td>${formatNumber(state.individualClaims)}</td>
            <td>${formatNumber(state.communityClaims)}</td>
            <td>${formatNumber(state.totalClaims)}</td>
            <td>${successRate.toFixed(1)}%</td>
        `;
        tableBody.appendChild(row);
    });
    
    const searchBox = document.getElementById('claimsSearch');
    if (searchBox) {
        searchBox.addEventListener('input', function() {
            filterTable('claimsTable', this.value);
        });
    }
}

// Titles distribution functions
function loadTitlesData() {
    const tableBody = document.getElementById('titlesTableBody');
    if (!tableBody) return;
    
    tableBody.innerHTML = '';
    
    fraData2023.forEach(state => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${state.state}</td>
            <td>${formatNumber(state.individualTitles)}</td>
            <td>${formatNumber(state.communityTitles)}</td>
            <td>${formatNumber(state.totalTitles)}</td>
            <td>${formatNumber(state.landArea)}</td>
        `;
        tableBody.appendChild(row);
    });
    
    const searchBox = document.getElementById('titlesSearch');
    if (searchBox) {
        searchBox.addEventListener('input', function() {
            filterTable('titlesTable', this.value);
        });
    }
}

// Utility functions
function formatNumber(num) {
    if (num >= 1000000) {
        return (num / 1000000).toFixed(1) + 'M';
    } else if (num >= 1000) {
        return (num / 1000).toFixed(1) + 'K';
    }
    return num.toLocaleString();
}

function filterTable(tableId, searchTerm) {
    const table = document.getElementById(tableId);
    if (!table) return;
    
    const rows = table.getElementsByTagName('tr');
    
    for (let i = 1; i < rows.length; i++) {
        const row = rows[i];
        const stateName = row.cells[0].textContent.toLowerCase();
        
        if (stateName.includes(searchTerm.toLowerCase())) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    }
}

function animateVisitorCounter() {
    const counter = document.getElementById('visitorCount');
    if (!counter) return;
    
    let count = 570770;
    
    setInterval(() => {
        count += Math.floor(Math.random() * 5) + 1;
        counter.textContent = count.toLocaleString();
    }, 30000);
}

// Initialize application
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded, initializing application...');
    
    loadNationalStats();
    animateVisitorCounter();
    
    // Initialize map after a short delay to ensure DOM is ready
    setTimeout(() => {
        initializeMap();
    }, 500);
    
    // Add smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
});

// Prevent back button navigation
function DisableBackButton() {
    window.history.forward();
}

DisableBackButton();
window.addEventListener('load', DisableBackButton);
window.addEventListener('pageshow', function(evt) { 
    if (evt.persisted) DisableBackButton();
});

// Download functions for reports
function downloadAnnualReport() {
    showDownloadProgress('Annual Report 2023');
    
    // Create a sample PDF content
    const pdfContent = generateAnnualReportData();
    downloadFile(pdfContent, 'FRA_Annual_Report_2023.pdf', 'application/pdf');
    
    addToDownloadHistory('Annual Report 2023', 'PDF', '2.4 MB');
}

function downloadStateData() {
    showDownloadProgress('State-wise Data');
    
    // Generate CSV content from fraData2023
    const csvContent = generateStateDataCSV();
    downloadFile(csvContent, 'FRA_State_Data_2023.csv', 'text/csv');
    
    addToDownloadHistory('State-wise Data', 'CSV', '1.8 MB');
}

function downloadAnalytics() {
    showDownloadProgress('Analytics Dashboard');
    
    // Generate analytics report
    const analyticsContent = generateAnalyticsReport();
    downloadFile(analyticsContent, 'FRA_Analytics_Dashboard_2023.pdf', 'application/pdf');
    
    addToDownloadHistory('Analytics Dashboard', 'PDF', '3.2 MB');
}

function downloadGISData() {
    showDownloadProgress('GIS Data Package');
    
    // Generate GIS data package
    const gisContent = generateGISData();
    downloadFile(gisContent, 'FRA_GIS_Data_Package.zip', 'application/zip');
    
    addToDownloadHistory('GIS Data Package', 'ZIP', '15.6 MB');
}

function downloadRawData() {
    showDownloadProgress('Raw Data CSV');
    
    // Generate raw CSV data
    const rawContent = generateRawDataCSV();
    downloadFile(rawContent, 'FRA_Raw_Data_2023.csv', 'text/csv');
    
    addToDownloadHistory('Raw Data CSV', 'CSV', '890 KB');
}

function downloadPresentation() {
    showDownloadProgress('Presentation Template');
    
    // Generate presentation template
    const presentationContent = generatePresentationTemplate();
    downloadFile(presentationContent, 'FRA_Presentation_Template.pptx', 'application/vnd.openxmlformats-officedocument.presentationml.presentation');
    
    addToDownloadHistory('Presentation Template', 'PPTX', '4.1 MB');
}

function showDownloadProgress(fileName) {
    // Create a temporary notification
    const notification = document.createElement('div');
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: #27ae60;
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        z-index: 10000;
        animation: slideIn 0.3s ease-out;
    `;
    notification.innerHTML = `
        <i class="fas fa-download"></i> Downloading ${fileName}...
    `;
    
    document.body.appendChild(notification);
    
    // Remove notification after 3 seconds
    setTimeout(() => {
        notification.remove();
    }, 3000);
}

function downloadFile(content, filename, mimeType) {
    const blob = new Blob([content], { type: mimeType });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
}

function generateStateDataCSV() {
    let csv = 'State,Individual Claims,Community Claims,Total Claims,Individual Titles,Community Titles,Total Titles,Land Area (Acres),Success Rate\n';
    
    fraData2023.forEach(state => {
        const successRate = state.totalClaims > 0 ? (state.totalTitles / state.totalClaims * 100).toFixed(2) : '0.00';
        csv += `"${state.state}",${state.individualClaims},${state.communityClaims},${state.totalClaims},${state.individualTitles},${state.communityTitles},${state.totalTitles},${state.landArea},${successRate}%\n`;
    });
    
    return csv;
}

function generateRawDataCSV() {
    let csv = 'State,Latitude,Longitude,Individual Claims,Community Claims,Total Claims,Individual Titles,Community Titles,Total Titles,Land Area,Recent Claimants\n';
    
    fraData2023.forEach(state => {
        const claimants = state.recentClaimants ? state.recentClaimants.map(c => `${c.name} (${c.village})`).join('; ') : '';
        csv += `"${state.state}",${state.coordinates[0]},${state.coordinates[1]},${state.individualClaims},${state.communityClaims},${state.totalClaims},${state.individualTitles},${state.communityTitles},${state.totalTitles},${state.landArea},"${claimants}"\n`;
    });
    
    return csv;
}

function generateAnnualReportData() {
    const totalClaims = fraData2023.reduce((sum, state) => sum + state.totalClaims, 0);
    const totalTitles = fraData2023.reduce((sum, state) => sum + state.totalTitles, 0);
    const totalLand = fraData2023.reduce((sum, state) => sum + state.landArea, 0);
    const successRate = totalClaims > 0 ? (totalTitles / totalClaims * 100).toFixed(2) : '0.00';
    
    return `Forest Rights Act - Annual Report 2023
    
EXECUTIVE SUMMARY
================
Total States Covered: ${fraData2023.length}
Total Claims Received: ${totalClaims.toLocaleString()}
Total Titles Distributed: ${totalTitles.toLocaleString()}
Overall Success Rate: ${successRate}%
Total Land Allocated: ${totalLand.toLocaleString()} acres

STATE-WISE PERFORMANCE
=====================
${fraData2023.map(state => {
    const rate = state.totalClaims > 0 ? (state.totalTitles / state.totalClaims * 100).toFixed(1) : '0.0';
    return `${state.state}: ${state.totalTitles.toLocaleString()} titles (${rate}% success rate)`;
}).join('\n')}

Generated on: ${new Date().toLocaleDateString()}
Source: Ministry of Tribal Affairs, Government of India`;
}

function generateAnalyticsReport() {
    return `FRA Analytics Dashboard Report 2023
    
This report contains comprehensive analytics and visualizations of Forest Rights Act implementation across India.

Key Metrics:
- Implementation progress by state
- Monthly trends analysis
- Claim type distribution
- Success rate comparisons

Generated on: ${new Date().toLocaleDateString()}`;
}

function generateGISData() {
    return `GIS Data Package for FRA Implementation

This package contains:
- State boundary shapefiles
- Claim location points
- Land allocation polygons
- Metadata and documentation

Coordinate System: WGS84
Format: ESRI Shapefile, KML
Generated on: ${new Date().toLocaleDateString()}`;
}

function generatePresentationTemplate() {
    return `PowerPoint Presentation Template - FRA Implementation 2023

Slides included:
1. Executive Summary
2. National Overview
3. State-wise Performance
4. Key Achievements
5. Challenges and Recommendations

Generated on: ${new Date().toLocaleDateString()}`;
}

function addToDownloadHistory(fileName, fileType, fileSize) {
    const historyDiv = document.getElementById('downloadHistory');
    if (!historyDiv) return;
    
    // Remove "No downloads yet" message if it exists
    if (historyDiv.innerHTML.includes('No downloads yet')) {
        historyDiv.innerHTML = '';
    }
    
    const downloadItem = document.createElement('div');
    downloadItem.style.cssText = 'padding: 0.5rem; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; align-items: center;';
    downloadItem.innerHTML = `
        <span><i class="fas fa-file"></i> ${fileName} (${fileType})</span>
        <div>
            <small style="color: #666; margin-right: 1rem;">${fileSize}</small>
            <small style="color: #666;">${new Date().toLocaleString()}</small>
        </div>
    `;
    
    // Add to top of history
    historyDiv.insertBefore(downloadItem, historyDiv.firstChild);
    
    // Keep only last 5 downloads
    while (historyDiv.children.length > 5) {
        historyDiv.removeChild(historyDiv.lastChild);
    }
}

// Export functions for global access
window.showPage = showPage;
window.updateMapView = updateMapView;
window.updateDashboard = updateDashboard;
window.refreshDashboard = refreshDashboard;
window.downloadAnnualReport = downloadAnnualReport;
window.downloadStateData = downloadStateData;
window.downloadAnalytics = downloadAnalytics;
window.downloadGISData = downloadGISData;
window.downloadRawData = downloadRawData;
window.downloadPresentation = downloadPresentation;

// Claimants page functionality
let currentPage = 1;
let itemsPerPage = 20;
let filteredClaimants = [];

function loadClaimantsPage() {
    console.log('Loading claimants page...');
    
    // Wait for claimant data to be loaded
    setTimeout(() => {
        if (window.FRAClaimants) {
            filteredClaimants = [...window.FRAClaimants];
            updateClaimantsSummary();
            displayClaimants();
            setupClaimantsFilters();
        } else {
            console.error('Claimant data not loaded yet');
        }
    }, 500);
}

function updateClaimantsSummary() {
    if (!window.FRAClaimantData) return;
    
    const data = window.FRAClaimantData;
    const totalClaimants = data.metadata.totalClaimants;
    const approved = window.FRAClaimants.filter(c => c.status === 'Approved').length;
    const pending = window.FRAClaimants.filter(c => c.status === 'Pending' || c.status === 'Under Review').length;
    const totalLand = window.FRAClaimants.reduce((sum, c) => sum + parseFloat(c.landArea), 0);
    
    document.getElementById('totalClaimants').textContent = totalClaimants;
    document.getElementById('approvedClaimants').textContent = approved;
    document.getElementById('pendingClaimants').textContent = pending;
    document.getElementById('totalLandClaimed').textContent = totalLand.toFixed(1);
}

function displayClaimants() {
    const tableBody = document.getElementById('claimantsTableBody');
    if (!tableBody) return;
    
    tableBody.innerHTML = '';
    
    const startIndex = (currentPage - 1) * itemsPerPage;
    const endIndex = startIndex + itemsPerPage;
    const pageClaimants = filteredClaimants.slice(startIndex, endIndex);
    
    pageClaimants.forEach(claimant => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${claimant.claimId}</td>
            <td>${claimant.name}</td>
            <td>${claimant.tribe}</td>
            <td>${claimant.village}</td>
            <td>${claimant.district}</td>
            <td>${claimant.state}</td>
            <td>${claimant.landArea}</td>
            <td>${claimant.claimType}</td>
            <td><span class="status-badge status-${claimant.status.toLowerCase().replace(' ', '-')}">${claimant.status}</span></td>
            <td>
                <button onclick="viewClaimantDetails('${claimant.claimId}')" 
                        style="padding: 0.25rem 0.5rem; background: #27ae60; color: white; border: none; border-radius: 3px; cursor: pointer; font-size: 0.8rem;">
                    <i class="fas fa-eye"></i> View
                </button>
            </td>
        `;
        tableBody.appendChild(row);
    });
    
    updatePagination();
}

function updatePagination() {
    const totalPages = Math.ceil(filteredClaimants.length / itemsPerPage);
    document.getElementById('pageInfo').textContent = `Page ${currentPage} of ${totalPages}`;
    
    document.getElementById('prevPage').disabled = currentPage === 1;
    document.getElementById('nextPage').disabled = currentPage === totalPages;
}

function changePage(direction) {
    const totalPages = Math.ceil(filteredClaimants.length / itemsPerPage);
    const newPage = currentPage + direction;
    
    if (newPage >= 1 && newPage <= totalPages) {
        currentPage = newPage;
        displayClaimants();
    }
}

function setupClaimantsFilters() {
    const searchInput = document.getElementById('claimantSearch');
    const stateFilter = document.getElementById('stateFilter');
    const statusFilter = document.getElementById('statusFilter');
    const claimTypeFilter = document.getElementById('claimTypeFilter');
    
    [searchInput, stateFilter, statusFilter, claimTypeFilter].forEach(element => {
        if (element) {
            element.addEventListener('change', applyFilters);
            element.addEventListener('input', applyFilters);
        }
    });
}

function applyFilters() {
    const searchTerm = document.getElementById('claimantSearch').value.toLowerCase();
    const stateFilter = document.getElementById('stateFilter').value;
    const statusFilter = document.getElementById('statusFilter').value;
    const claimTypeFilter = document.getElementById('claimTypeFilter').value;
    
    filteredClaimants = window.FRAClaimants.filter(claimant => {
        const matchesSearch = !searchTerm || 
            claimant.name.toLowerCase().includes(searchTerm) ||
            claimant.village.toLowerCase().includes(searchTerm) ||
            claimant.tribe.toLowerCase().includes(searchTerm);
            
        const matchesState = !stateFilter || claimant.state === stateFilter;
        const matchesStatus = !statusFilter || claimant.status === statusFilter;
        const matchesClaimType = !claimTypeFilter || claimant.claimType.includes(claimTypeFilter);
        
        return matchesSearch && matchesState && matchesStatus && matchesClaimType;
    });
    
    currentPage = 1;
    displayClaimants();
}

function viewClaimantDetails(claimId) {
    const claimant = window.FRAClaimants.find(c => c.claimId === claimId);
    if (!claimant) return;
    
    const modal = document.getElementById('claimantModal');
    const modalTitle = document.getElementById('modalTitle');
    const modalContent = document.getElementById('modalContent');
    
    modalTitle.textContent = `${claimant.name} - ${claimant.claimId}`;
    
    modalContent.innerHTML = `
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
            <div>
                <h4 style="color: #27ae60; margin-bottom: 0.5rem;">Personal Information</h4>
                <p><strong>Name:</strong> ${claimant.name}</p>
                <p><strong>Tribe/Community:</strong> ${claimant.tribe}</p>
                <p><strong>Years in Area:</strong> ${claimant.yearsInArea} years</p>
                <p><strong>Traditional Occupation:</strong> ${claimant.occupation}</p>
            </div>
            <div>
                <h4 style="color: #27ae60; margin-bottom: 0.5rem;">Location Details</h4>
                <p><strong>Village:</strong> ${claimant.village}</p>
                <p><strong>District:</strong> ${claimant.district}</p>
                <p><strong>State:</strong> ${claimant.state}</p>
                <p><strong>Coordinates:</strong> ${claimant.coordinates[0]}°N, ${claimant.coordinates[1]}°E</p>
            </div>
        </div>
        
        <div style="margin-top: 1.5rem;">
            <h4 style="color: #27ae60; margin-bottom: 0.5rem;">Claim Information</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                <div>
                    <p><strong>Claim Type:</strong> ${claimant.claimType}</p>
                    <p><strong>Land Area:</strong> ${claimant.landArea} hectares</p>
                    <p><strong>Application Date:</strong> ${claimant.applicationDate}</p>
                </div>
                <div>
                    <p><strong>Status:</strong> <span class="status-badge status-${claimant.status.toLowerCase().replace(' ', '-')}">${claimant.status}</span></p>
                    <p><strong>Year:</strong> ${claimant.year}</p>
                </div>
            </div>
        </div>
        
        <div style="margin-top: 1.5rem;">
            <h4 style="color: #27ae60; margin-bottom: 0.5rem;">Supporting Documents</h4>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
                ${claimant.documents.map(doc => `
                    <span style="background: #f0f0f0; padding: 0.25rem 0.5rem; border-radius: 15px; font-size: 0.8rem;">
                        <i class="fas fa-file-alt"></i> ${doc}
                    </span>
                `).join('')}
            </div>
        </div>
        
        <div style="margin-top: 1.5rem; padding: 1rem; background: #f8f9fa; border-radius: 8px;">
            <h4 style="color: #27ae60; margin-bottom: 0.5rem;">Additional Information</h4>
            <p>The claimant has been residing in the forest area for over ${claimant.yearsInArea} years. 
            Traditional occupation includes ${claimant.occupation}. The family has been dependent on forest 
            resources for their livelihood. Evidence of traditional use and occupation has been documented. 
            Community elders have verified the historical presence in the area.</p>
        </div>
    `;
    
    modal.style.display = 'flex';
}

function closeClaimantModal() {
    document.getElementById('claimantModal').style.display = 'none';
}

// Add CSS for status badges
const statusStyles = document.createElement('style');
statusStyles.textContent = `
    .status-badge {
        padding: 0.25rem 0.5rem;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: bold;
        text-transform: uppercase;
    }
    .status-approved { background: #d4edda; color: #155724; }
    .status-under-review { background: #fff3cd; color: #856404; }
    .status-pending { background: #cce5ff; color: #004085; }
    .status-rejected { background: #f8d7da; color: #721c24; }
    .status-documentation-required { background: #e2e3e5; color: #383d41; }
`;
document.head.appendChild(statusStyles);

// Export claimants functions
window.changePage = changePage;
window.viewClaimantDetails = viewClaimantDetails;
window.closeClaimantModal = closeClaimantModal;
window.filterMapMarkers = filterMapMarkers;