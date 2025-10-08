// Chart functions for FRA Atlas Dashboard

function createIndividualRightsChart() {
    const canvas = document.getElementById('individualRightsChart');
    if (!canvas) {
        console.log('individualRightsChart canvas not found');
        return;
    }
    
    console.log('Creating individual rights chart...');
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    
    ctx.clearRect(0, 0, width, height);
    
    // Get top 8 states by individual claims
    const topStates = fraData2023
        .map(state => ({
            name: state.state.length > 8 ? state.state.substring(0, 8) + '...' : state.state,
            claims: state.individualClaims,
            titles: state.individualTitles
        }))
        .sort((a, b) => b.claims - a.claims)
        .slice(0, 8);
    
    const barWidth = (width - 60) / topStates.length - 8;
    const maxValue = Math.max(...topStates.map(s => Math.max(s.claims, s.titles)));
    
    if (maxValue === 0) return;
    
    topStates.forEach((state, index) => {
        const x = 30 + index * (barWidth + 8);
        
        // Draw claims bar
        const claimsHeight = (state.claims / maxValue) * (height - 80);
        const claimsY = height - claimsHeight - 40;
        ctx.fillStyle = '#f39c12';
        ctx.fillRect(x, claimsY, barWidth/2 - 2, claimsHeight);
        
        // Draw titles bar
        const titlesHeight = (state.titles / maxValue) * (height - 80);
        const titlesY = height - titlesHeight - 40;
        ctx.fillStyle = '#e74c3c';
        ctx.fillRect(x + barWidth/2 + 2, titlesY, barWidth/2 - 2, titlesHeight);
        
        // Draw state name
        ctx.fillStyle = '#2c3e50';
        ctx.font = '9px Arial';
        ctx.save();
        ctx.translate(x + barWidth/2, height - 25);
        ctx.rotate(-Math.PI/4);
        ctx.textAlign = 'right';
        ctx.fillText(state.name, 0, 0);
        ctx.restore();
    });
    
    console.log('Individual rights chart created successfully');
}

function createCommunityRightsChart() {
    const canvas = document.getElementById('communityRightsChart');
    if (!canvas) {
        console.log('communityRightsChart canvas not found');
        return;
    }
    
    console.log('Creating community rights chart...');
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    
    ctx.clearRect(0, 0, width, height);
    
    // Get top 8 states by community claims
    const topStates = fraData2023
        .map(state => ({
            name: state.state.length > 8 ? state.state.substring(0, 8) + '...' : state.state,
            claims: state.communityClaims,
            titles: state.communityTitles
        }))
        .sort((a, b) => b.claims - a.claims)
        .slice(0, 8);
    
    const barWidth = (width - 60) / topStates.length - 8;
    const maxValue = Math.max(...topStates.map(s => Math.max(s.claims, s.titles)));
    
    if (maxValue === 0) return;
    
    topStates.forEach((state, index) => {
        const x = 30 + index * (barWidth + 8);
        
        // Draw claims bar
        const claimsHeight = (state.claims / maxValue) * (height - 80);
        const claimsY = height - claimsHeight - 40;
        ctx.fillStyle = '#3498db';
        ctx.fillRect(x, claimsY, barWidth/2 - 2, claimsHeight);
        
        // Draw titles bar
        const titlesHeight = (state.titles / maxValue) * (height - 80);
        const titlesY = height - titlesHeight - 40;
        ctx.fillStyle = '#9b59b6';
        ctx.fillRect(x + barWidth/2 + 2, titlesY, barWidth/2 - 2, titlesHeight);
        
        // Draw state name
        ctx.fillStyle = '#2c3e50';
        ctx.font = '9px Arial';
        ctx.save();
        ctx.translate(x + barWidth/2, height - 25);
        ctx.rotate(-Math.PI/4);
        ctx.textAlign = 'right';
        ctx.fillText(state.name, 0, 0);
        ctx.restore();
    });
    
    console.log('Community rights chart created successfully');
}

function createForestLandChart() {
    const canvas = document.getElementById('forestLandChart');
    if (!canvas) {
        console.log('forestLandChart canvas not found');
        return;
    }
    
    console.log('Creating forest land chart...');
    console.log('Canvas dimensions:', canvas.width, 'x', canvas.height);
    
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    
    ctx.clearRect(0, 0, width, height);
    
    // Get top 6 states by land area for better visibility
    const topStates = fraData2023
        .filter(state => state.landArea > 0) // Only states with land data
        .map(state => ({
            name: state.state.length > 8 ? state.state.substring(0, 8) + '...' : state.state,
            landArea: state.landArea / 100000 // Convert to lakh acres
        }))
        .sort((a, b) => b.landArea - a.landArea)
        .slice(0, 6);
    
    console.log('Top states for forest land chart:', topStates);
    
    if (topStates.length === 0) {
        console.log('No states with land data found');
        return;
    }
    
    const barWidth = Math.max(30, (width - 80) / topStates.length - 10);
    const maxValue = Math.max(...topStates.map(s => s.landArea));
    
    console.log('Max land area value:', maxValue);
    
    if (maxValue === 0) return;
    
    topStates.forEach((state, index) => {
        const x = 40 + index * (barWidth + 10);
        
        // Assume 70% IFR and 30% CFR for visualization
        const ifrLand = state.landArea * 0.7;
        const cfrLand = state.landArea * 0.3;
        
        // Draw IFR bar
        const ifrHeight = Math.max(5, (ifrLand / maxValue) * (height - 100));
        const ifrY = height - ifrHeight - 50;
        ctx.fillStyle = '#27ae60';
        ctx.fillRect(x, ifrY, barWidth/2 - 2, ifrHeight);
        
        // Draw CFR bar
        const cfrHeight = Math.max(5, (cfrLand / maxValue) * (height - 100));
        const cfrY = height - cfrHeight - 50;
        ctx.fillStyle = '#2980b9';
        ctx.fillRect(x + barWidth/2 + 2, cfrY, barWidth/2 - 2, cfrHeight);
        
        // Draw state name
        ctx.fillStyle = '#2c3e50';
        ctx.font = '10px Arial';
        ctx.save();
        ctx.translate(x + barWidth/2, height - 30);
        ctx.rotate(-Math.PI/4);
        ctx.textAlign = 'right';
        ctx.fillText(state.name, 0, 0);
        ctx.restore();
        
        // Draw value
        ctx.fillStyle = '#2c3e50';
        ctx.font = '9px Arial';
        ctx.textAlign = 'center';
        ctx.fillText(state.landArea.toFixed(1) + 'L', x + barWidth/2, ifrY - 8);
    });
    
    // Draw title
    ctx.fillStyle = '#2c3e50';
    ctx.font = 'bold 12px Arial';
    ctx.textAlign = 'left';
    ctx.fillText('Land Area (Lakh Acres)', 10, 20);
    
    console.log('Forest land chart created successfully');
}

function createClaimsStatusChart() {
    const canvas = document.getElementById('claimsStatusChart');
    if (!canvas) {
        console.log('claimsStatusChart canvas not found');
        return;
    }
    
    console.log('Creating claims status chart...');
    console.log('Canvas dimensions:', canvas.width, 'x', canvas.height);
    
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    
    ctx.clearRect(0, 0, width, height);
    
    const totalClaims = fraData2023.reduce((sum, state) => sum + state.totalClaims, 0);
    const totalTitles = fraData2023.reduce((sum, state) => sum + state.totalTitles, 0);
    const rejectedClaims = Math.floor(totalClaims * 0.12); // Assume 12% rejected
    const pendingClaims = Math.max(0, totalClaims - totalTitles - rejectedClaims);
    
    console.log('Claims data:', {
        totalClaims,
        totalTitles,
        rejectedClaims,
        pendingClaims
    });
    
    const centerX = width / 2;
    const centerY = height / 2 - 20; // Move up a bit
    const radius = Math.min(width, height) / 4;
    
    const total = totalClaims;
    let currentAngle = -Math.PI / 2; // Start from top
    
    // Draw Titles Distributed slice (largest)
    const titlesAngle = (totalTitles / total) * 2 * Math.PI;
    ctx.beginPath();
    ctx.moveTo(centerX, centerY);
    ctx.arc(centerX, centerY, radius, currentAngle, currentAngle + titlesAngle);
    ctx.closePath();
    ctx.fillStyle = '#27ae60'; // Green for approved
    ctx.fill();
    ctx.strokeStyle = '#fff';
    ctx.lineWidth = 3;
    ctx.stroke();
    currentAngle += titlesAngle;
    
    // Draw Pending Claims slice
    const pendingAngle = (pendingClaims / total) * 2 * Math.PI;
    if (pendingAngle > 0) {
        ctx.beginPath();
        ctx.moveTo(centerX, centerY);
        ctx.arc(centerX, centerY, radius, currentAngle, currentAngle + pendingAngle);
        ctx.closePath();
        ctx.fillStyle = '#f39c12'; // Orange for pending
        ctx.fill();
        ctx.strokeStyle = '#fff';
        ctx.lineWidth = 3;
        ctx.stroke();
        currentAngle += pendingAngle;
    }
    
    // Draw Rejected Claims slice
    const rejectedAngle = (rejectedClaims / total) * 2 * Math.PI;
    if (rejectedAngle > 0) {
        ctx.beginPath();
        ctx.moveTo(centerX, centerY);
        ctx.arc(centerX, centerY, radius, currentAngle, currentAngle + rejectedAngle);
        ctx.closePath();
        ctx.fillStyle = '#e74c3c'; // Red for rejected
        ctx.fill();
        ctx.strokeStyle = '#fff';
        ctx.lineWidth = 3;
        ctx.stroke();
    }
    
    // Draw center text
    ctx.fillStyle = '#2c3e50';
    ctx.font = 'bold 12px Arial';
    ctx.textAlign = 'center';
    ctx.fillText('Total Claims', centerX, centerY - 8);
    ctx.font = '11px Arial';
    ctx.fillText(formatNumber(totalClaims), centerX, centerY + 8);
    
    // Draw percentages
    const titlesPercent = ((totalTitles / total) * 100).toFixed(1);
    const pendingPercent = ((pendingClaims / total) * 100).toFixed(1);
    const rejectedPercent = ((rejectedClaims / total) * 100).toFixed(1);
    
    ctx.font = '9px Arial';
    ctx.fillText(`Approved: ${titlesPercent}%`, centerX, centerY + radius + 25);
    ctx.fillText(`Pending: ${pendingPercent}%`, centerX, centerY + radius + 38);
    ctx.fillText(`Rejected: ${rejectedPercent}%`, centerX, centerY + radius + 51);
    
    console.log('Claims status chart created successfully');
}

function loadDashboardCharts() {
    console.log('Loading dashboard charts...');
    
    // Check if all canvas elements exist
    const canvasIds = ['individualRightsChart', 'communityRightsChart', 'forestLandChart', 'claimsStatusChart'];
    const missingCanvas = [];
    
    canvasIds.forEach(id => {
        const canvas = document.getElementById(id);
        if (!canvas) {
            missingCanvas.push(id);
        } else {
            console.log(`Found canvas: ${id} (${canvas.width}x${canvas.height})`);
        }
    });
    
    if (missingCanvas.length > 0) {
        console.error('Missing canvas elements:', missingCanvas);
    }
    
    setTimeout(() => {
        console.log('Creating individual rights chart...');
        createIndividualRightsChart();
        
        setTimeout(() => {
            console.log('Creating community rights chart...');
            createCommunityRightsChart();
        }, 100);
        
        setTimeout(() => {
            console.log('Creating forest land chart...');
            createForestLandChart();
        }, 200);
        
        setTimeout(() => {
            console.log('Creating claims status chart...');
            createClaimsStatusChart();
        }, 300);
        
    }, 200);
}

// Force refresh all charts
function forceRefreshCharts() {
    console.log('Force refreshing all charts...');
    
    // Clear all canvases first
    const canvasIds = ['individualRightsChart', 'communityRightsChart', 'forestLandChart', 'claimsStatusChart'];
    canvasIds.forEach(id => {
        const canvas = document.getElementById(id);
        if (canvas) {
            const ctx = canvas.getContext('2d');
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // Draw a test rectangle to verify canvas is working
            ctx.fillStyle = '#f0f0f0';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = '#333';
            ctx.font = '12px Arial';
            ctx.textAlign = 'center';
            ctx.fillText('Loading...', canvas.width/2, canvas.height/2);
        }
    });
    
    // Reload charts after a delay
    setTimeout(() => {
        loadDashboardCharts();
    }, 500);
}

// Utility function for formatting numbers
function formatNumber(num) {
    if (num >= 1000000) {
        return (num / 1000000).toFixed(1) + 'M';
    } else if (num >= 1000) {
        return (num / 1000).toFixed(1) + 'K';
    }
    return num.toLocaleString();
}

// Test function to manually trigger charts
function testCharts() {
    console.log('=== TESTING CHARTS ===');
    
    // Check if fraData2023 exists
    if (typeof fraData2023 === 'undefined') {
        console.error('fraData2023 is not defined!');
        return;
    }
    
    console.log('fraData2023 length:', fraData2023.length);
    
    // Test each canvas
    const canvasIds = ['individualRightsChart', 'communityRightsChart', 'forestLandChart', 'claimsStatusChart'];
    
    canvasIds.forEach(id => {
        const canvas = document.getElementById(id);
        if (canvas) {
            console.log(`Canvas ${id}: ${canvas.width}x${canvas.height}, visible: ${canvas.offsetWidth > 0}`);
            
            // Draw a test pattern
            const ctx = canvas.getContext('2d');
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // Test pattern
            ctx.fillStyle = '#f0f0f0';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            ctx.fillStyle = '#27ae60';
            ctx.fillRect(10, 10, 50, 50);
            
            ctx.fillStyle = '#e74c3c';
            ctx.fillRect(70, 10, 50, 50);
            
            ctx.fillStyle = '#3498db';
            ctx.fillRect(130, 10, 50, 50);
            
            ctx.fillStyle = '#2c3e50';
            ctx.font = '14px Arial';
            ctx.textAlign = 'center';
            ctx.fillText(`${id} - TEST`, canvas.width/2, canvas.height/2);
            
        } else {
            console.error(`Canvas ${id} not found!`);
        }
    });
    
    // Now try to create actual charts
    setTimeout(() => {
        console.log('Creating actual charts...');
        createIndividualRightsChart();
        createCommunityRightsChart();
        createForestLandChart();
        createClaimsStatusChart();
    }, 1000);
}

// Make functions globally available
window.forceRefreshCharts = forceRefreshCharts;
window.testCharts = testCharts;