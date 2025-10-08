import random
import os
from datetime import datetime, timedelta

# Sample data for different states
states_data = {
    "Madhya Pradesh": {
        "districts": ["Mandla", "Balaghat", "Seoni", "Chhindwara", "Betul", "Hoshangabad", "Dindori", "Shahdol", "Umaria", "Katni"],
        "villages": ["Khairwani", "Bamhani", "Ghughri", "Kanha", "Mukki", "Sarhi", "Baihar", "Lalbarra", "Amarkantak", "Bandhavgarh"],
        "coordinates": [
            (22.7196, 80.5771), (21.8047, 80.1807), (22.0796, 79.9739), (22.0572, 78.9389),
            (21.9058, 77.9065), (22.7679, 77.7289), (22.9441, 81.0820), (23.2967, 81.3431),
            (23.5290, 80.8397), (23.8315, 80.9061)
        ]
    },
    "Odisha": {
        "districts": ["Mayurbhanj", "Keonjhar", "Sundargarh", "Sambalpur", "Deogarh", "Angul", "Dhenkanal", "Kandhamal", "Rayagada", "Koraput"],
        "villages": ["Similipal", "Barbil", "Rourkela", "Hirakud", "Tileibani", "Talcher", "Kamakhyanagar", "Phulbani", "Gunupur", "Jeypore"],
        "coordinates": [
            (21.9270, 86.7470), (21.6293, 85.5895), (22.2604, 84.8536), (21.4669, 83.9812),
            (21.5347, 84.7338), (20.8397, 85.0939), (20.6593, 85.5955), (20.4781, 84.2336),
            (19.1626, 83.4148), (18.8895, 82.5678)
        ]
    },
    "Tripura": {
        "districts": ["West Tripura", "South Tripura", "Dhalai", "North Tripura", "Gomati", "Khowai", "Sepahijala", "Unakoti"],
        "villages": ["Agartala", "Udaipur", "Ambassa", "Dharmanagar", "Sonamura", "Teliamura", "Bishalgarh", "Kumarghat"],
        "coordinates": [
            (23.8315, 91.2868), (23.5333, 91.4789), (23.9333, 91.8500), (24.3167, 92.1667),
            (23.4939, 91.2814), (23.4500, 91.4667), (23.6667, 91.4167), (24.1167, 92.0167)
        ]
    },
    "Telangana": {
        "districts": ["Adilabad", "Komaram Bheem", "Mancherial", "Nirmal", "Nizamabad", "Jagtial", "Peddapalli", "Jayashankar", "Mulugu", "Bhadradri"],
        "villages": ["Kawal", "Jannaram", "Luxettipet", "Bhainsa", "Armoor", "Dharmapuri", "Manthani", "Eturnagaram", "Eturunagaram", "Kothagudem"],
        "coordinates": [
            (19.6944, 78.5311), (18.7333, 79.4500), (18.8667, 79.4500), (19.0833, 78.3500),
            (18.6725, 78.0941), (18.7903, 78.9242), (18.6127, 79.3742), (18.3167, 80.1000),
            (18.1500, 80.1667), (17.5500, 80.6167)
        ]
    }
}

# Sample names for different communities
names_data = {
    "Gond": ["Ramesh Kumar", "Sunita", "Bharat Singh", "Kamala Devi", "Ravi Kumar", "Sita", "Mohan Lal", "Radha", "Suresh", "Parvati"],
    "Baiga": ["Dukhan", "Fulkumari", "Mangal Singh", "Chameli", "Budhan", "Sukhmati", "Raman", "Phoolmati", "Dhaniram", "Kamlesh"],
    "Korku": ["Shankar", "Rukhmani", "Ganesh", "Savitri", "Ramchandra", "Laxmi", "Vishnu", "Durga", "Krishna", "Saraswati"],
    "Santhal": ["Soma", "Phulmani", "Budhan", "Champa", "Mangal", "Sukri", "Jatra", "Dulari", "Sidhu", "Rukmani"],
    "Koya": ["Ramulu", "Lakshmi", "Venkat", "Sita", "Raju", "Kamala", "Naresh", "Padma", "Suresh", "Radha"],
    "Chenchu": ["Narasimha", "Yellamma", "Rama", "Sita", "Krishna", "Lakshmi", "Venkata", "Parvati", "Ravi", "Kamala"]
}

# Generate claim ID
def generate_claim_id(state_code, year, serial):
    return f"FRA/{year}/{state_code}/{serial:05d}"

# Get state code
def get_state_code(state):
    codes = {"Madhya Pradesh": "MP", "Odisha": "OD", "Tripura": "TR", "Telangana": "TG"}
    return codes[state]

# Generate random date
def generate_random_date():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2023, 12, 31)
    time_between = end_date - start_date
    days_between = time_between.days
    random_days = random.randrange(days_between)
    return (start_date + timedelta(days=random_days)).strftime("%d-%m-%Y")

# Generate FRA claim document
def generate_fra_claim(serial_no):
    state = random.choice(list(states_data.keys()))
    state_data = states_data[state]
    
    district = random.choice(state_data["districts"])
    village = random.choice(state_data["villages"])
    lat, lon = random.choice(state_data["coordinates"])
    
    # Add some random variation to coordinates (within ~5km radius)
    lat += random.uniform(-0.05, 0.05)
    lon += random.uniform(-0.05, 0.05)
    
    community = random.choice(list(names_data.keys()))
    name = random.choice(names_data[community])
    
    claim_types = [
        "Individual Forest Rights (IFR)",
        "Community Forest Rights (CFR)", 
        "Community Forest Resource Rights",
        "Traditional Forest Dweller Rights"
    ]
    
    documents = [
        "Ration Card", "Voter ID Card", "Community Certificate", "Land Survey Records",
        "Revenue Records", "Patta Documents", "Settlement Records", "Forest Survey Records",
        "Genealogy Records", "Traditional Use Evidence"
    ]
    
    occupations = [
        "collection of minor forest produce",
        "traditional agriculture and livestock",
        "honey collection and beekeeping",
        "medicinal plant collection",
        "bamboo and timber collection",
        "fishing in forest streams",
        "traditional handicrafts",
        "forest-based livelihood activities"
    ]
    
    claim_id = generate_claim_id(get_state_code(state), random.randint(2020, 2023), serial_no)
    claim_type = random.choice(claim_types)
    area = round(random.uniform(0.5, 5.0), 1)
    app_date = generate_random_date()
    selected_docs = random.sample(documents, random.randint(3, 6))
    occupation = random.choice(occupations)
    years_residing = random.randint(25, 100)
    
    content = f"""Forest Rights Act Claim Application

Claim ID: {claim_id}
Applicant Name: {name} {community}
Tribe/Community: {community}
Village: {village}
District: {district}
State: {state}
Coordinates: {lat:.6f}°N, {lon:.6f}°E
Type of Claim: {claim_type}
Land Area Claimed: {area} hectares
Application Date: {app_date}

Supporting Documents:
{chr(10).join([f"- {doc}" for doc in selected_docs])}

Additional Information:
The claimant has been residing in the forest area for over {years_residing} years.
Traditional occupation includes {occupation}.
The family has been dependent on forest resources for their livelihood.
Evidence of traditional use and occupation has been documented.
Community elders have verified the historical presence in the area."""

    return content, claim_id

# Create directory for FRA claims
if not os.path.exists("fra_claims"):
    os.makedirs("fra_claims")

print("Generating 600 FRA claim documents...")

for i in range(1, 601):
    content, claim_id = generate_fra_claim(i)
    filename = f"fra_claims/FRA_Claim_{i:03d}_{claim_id.replace('/', '_')}.txt"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    if i % 50 == 0:
        print(f"Generated {i} documents...")

print("Successfully generated 600 FRA claim documents in the 'fra_claims' folder!")