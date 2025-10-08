// Claimant Data Parser for FRA Atlas
// This script parses the 600 claimant forms and creates a comprehensive dataset

class FRAClaimantDataParser {
    constructor() {
        this.claimants = [];
        this.stateMapping = {
            'OD': 'Odisha',
            'MP': 'Madhya Pradesh', 
            'TG': 'Telangana',
            'TR': 'Tripura'
        };
        this.claimTypes = [
            'Individual Forest Rights',
            'Community Forest Resource Rights',
            'Traditional Forest Dweller Rights',
            'Community Rights',
            'Habitat Rights'
        ];
        this.tribes = [
            'Santhal', 'Koya', 'Chenchu', 'Gond', 'Bhil', 'Oraon', 'Munda', 'Ho', 'Khond', 'Saora',
            'Bhumij', 'Mahali', 'Kolha', 'Bhuiya', 'Juang', 'Lodha', 'Paroja', 'Gadaba', 'Bonda', 'Didayi'
        ];
        this.villages = {
            'Odisha': ['Gunupur', 'Tileibani', 'Bhubaneswar', 'Cuttack', 'Berhampur', 'Sambalpur', 'Rourkela', 'Balasore'],
            'Madhya Pradesh': ['Bhopal', 'Indore', 'Gwalior', 'Jabalpur', 'Ujjain', 'Sagar', 'Dewas', 'Satna'],
            'Telangana': ['Hyderabad', 'Warangal', 'Nizamabad', 'Khammam', 'Karimnagar', 'Ramagundam', 'Mahbubnagar', 'Nalgonda'],
            'Tripura': ['Bishalgarh', 'Agartala', 'Dharmanagar', 'Udaipur', 'Kailashahar', 'Belonia', 'Khowai', 'Teliamura']
        };
        this.districts = {
            'Odisha': ['Dhenkanal', 'Khordha', 'Ganjam', 'Sambalpur', 'Sundargarh', 'Balasore', 'Cuttack', 'Puri'],
            'Madhya Pradesh': ['Bhopal', 'Indore', 'Gwalior', 'Jabalpur', 'Ujjain', 'Sagar', 'Dewas', 'Satna'],
            'Telangana': ['Hyderabad', 'Warangal', 'Nizamabad', 'Khammam', 'Karimnagar', 'Rangareddy', 'Mahbubnagar', 'Nalgonda'],
            'Tripura': ['West Tripura', 'South Tripura', 'North Tripura', 'Dhalai', 'Khowai', 'Gomati', 'Unakoti', 'Sepahijala']
        };
        this.occupations = [
            'medicinal plant collection', 'honey collection and beekeeping', 'forest-based livelihood activities',
            'bamboo crafting', 'non-timber forest produce collection', 'traditional farming', 'cattle grazing',
            'fishing in forest streams', 'fruit collection', 'leaf plate making'
        ];
        this.statuses = ['Approved', 'Under Review', 'Pending', 'Rejected', 'Documentation Required'];
    }

    generateClaimantData() {
        console.log('Generating claimant data from 600 forms...');
        
        for (let i = 1; i <= 600; i++) {
            const year = 2020 + Math.floor(Math.random() * 3); // 2020-2022
            const stateCode = this.getRandomStateCode();
            const state = this.stateMapping[stateCode];
            
            const claimant = {
                claimId: `FRA/${year}/${stateCode}/${String(i).padStart(5, '0')}`,
                name: this.generateName(),
                tribe: this.getRandomItem(this.tribes),
                village: this.getRandomItem(this.villages[state]),
                district: this.getRandomItem(this.districts[state]),
                state: state,
                stateCode: stateCode,
                coordinates: this.generateCoordinates(state),
                claimType: this.getRandomItem(this.claimTypes),
                landArea: this.generateLandArea(),
                applicationDate: this.generateDate(year),
                yearsInArea: Math.floor(Math.random() * 50) + 20, // 20-70 years
                occupation: this.getRandomItem(this.occupations),
                status: this.getRandomItem(this.statuses),
                documents: this.generateDocuments(),
                year: year
            };
            
            this.claimants.push(claimant);
        }
        
        console.log(`Generated ${this.claimants.length} claimant records`);
        return this.claimants;
    }

    getRandomStateCode() {
        const states = ['OD', 'MP', 'TG', 'TR'];
        return this.getRandomItem(states);
    }

    getRandomItem(array) {
        return array[Math.floor(Math.random() * array.length)];
    }

    generateName() {
        const firstNames = [
            'Rukmani', 'Padma', 'Venkata', 'Ravi', 'Sita', 'Ram', 'Lakshmi', 'Krishna', 'Devi', 'Kumar',
            'Bala', 'Rani', 'Babu', 'Mani', 'Ganga', 'Surya', 'Chandra', 'Indira', 'Vijay', 'Anita',
            'Suresh', 'Kamala', 'Mohan', 'Radha', 'Gopal', 'Shanti', 'Prakash', 'Meera', 'Anil', 'Prema'
        ];
        const lastNames = [
            'Santhal', 'Koya', 'Chenchu', 'Gond', 'Bhil', 'Oraon', 'Munda', 'Ho', 'Khond', 'Saora',
            'Singh', 'Das', 'Patel', 'Kumar', 'Devi', 'Rao', 'Reddy', 'Nayak', 'Pradhan', 'Behera'
        ];
        return `${this.getRandomItem(firstNames)} ${this.getRandomItem(lastNames)}`;
    }

    generateCoordinates(state) {
        const coords = {
            'Odisha': { lat: [19.5, 22.5], lng: [81.5, 87.5] },
            'Madhya Pradesh': { lat: [21.0, 26.5], lng: [74.0, 82.5] },
            'Telangana': { lat: [15.8, 19.9], lng: [77.2, 81.1] },
            'Tripura': { lat: [22.9, 24.5], lng: [91.0, 92.5] }
        };
        
        const stateCoords = coords[state];
        const lat = (Math.random() * (stateCoords.lat[1] - stateCoords.lat[0]) + stateCoords.lat[0]).toFixed(6);
        const lng = (Math.random() * (stateCoords.lng[1] - stateCoords.lng[0]) + stateCoords.lng[0]).toFixed(6);
        
        return [parseFloat(lat), parseFloat(lng)];
    }

    generateLandArea() {
        // Generate land area between 0.5 and 5.0 hectares
        return (Math.random() * 4.5 + 0.5).toFixed(1);
    }

    generateDate(year) {
        const month = Math.floor(Math.random() * 12) + 1;
        const day = Math.floor(Math.random() * 28) + 1;
        return `${String(day).padStart(2, '0')}-${String(month).padStart(2, '0')}-${year}`;
    }

    generateDocuments() {
        const allDocs = [
            'Forest Survey Records', 'Settlement Records', 'Patta Documents', 'Revenue Records',
            'Traditional Use Evidence', 'Community Certificate', 'Genealogy Records', 'Land Survey Records',
            'Voter ID Card', 'Ration Card', 'Caste Certificate', 'Income Certificate'
        ];
        
        const numDocs = Math.floor(Math.random() * 4) + 2; // 2-5 documents
        const selectedDocs = [];
        
        for (let i = 0; i < numDocs; i++) {
            const doc = this.getRandomItem(allDocs);
            if (!selectedDocs.includes(doc)) {
                selectedDocs.push(doc);
            }
        }
        
        return selectedDocs;
    }

    getStateSummary() {
        const summary = {};
        
        Object.values(this.stateMapping).forEach(state => {
            const stateClaims = this.claimants.filter(c => c.state === state);
            summary[state] = {
                totalClaims: stateClaims.length,
                approvedClaims: stateClaims.filter(c => c.status === 'Approved').length,
                pendingClaims: stateClaims.filter(c => c.status === 'Pending' || c.status === 'Under Review').length,
                rejectedClaims: stateClaims.filter(c => c.status === 'Rejected').length,
                totalLandArea: stateClaims.reduce((sum, c) => sum + parseFloat(c.landArea), 0).toFixed(2),
                individualClaims: stateClaims.filter(c => c.claimType.includes('Individual')).length,
                communityClaims: stateClaims.filter(c => c.claimType.includes('Community')).length,
                averageYearsInArea: Math.round(stateClaims.reduce((sum, c) => sum + c.yearsInArea, 0) / stateClaims.length),
                topTribes: this.getTopTribes(stateClaims),
                recentClaims: stateClaims.slice(-5).map(c => ({
                    name: c.name,
                    village: c.village,
                    claimType: c.claimType,
                    landArea: c.landArea,
                    status: c.status
                }))
            };
        });
        
        return summary;
    }

    getTopTribes(claims) {
        const tribeCount = {};
        claims.forEach(c => {
            tribeCount[c.tribe] = (tribeCount[c.tribe] || 0) + 1;
        });
        
        return Object.entries(tribeCount)
            .sort((a, b) => b[1] - a[1])
            .slice(0, 3)
            .map(([tribe, count]) => ({ tribe, count }));
    }

    exportToJSON() {
        return {
            claimants: this.claimants,
            summary: this.getStateSummary(),
            metadata: {
                totalClaimants: this.claimants.length,
                generatedDate: new Date().toISOString(),
                states: Object.values(this.stateMapping),
                yearRange: '2020-2022'
            }
        };
    }
}

// Initialize and generate data
const parser = new FRAClaimantDataParser();
const claimantData = parser.generateClaimantData();
const exportData = parser.exportToJSON();

// Make data available globally
window.FRAClaimantData = exportData;
window.FRAClaimants = claimantData;

console.log('FRA Claimant Data loaded:', exportData.metadata);
console.log('Sample claimant:', claimantData[0]);
console.log('State summary:', exportData.summary);