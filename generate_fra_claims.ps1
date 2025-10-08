# FRA Claims Generator PowerShell Script

# Sample data arrays
$states = @(
    @{
        Name = "Madhya Pradesh"
        Code = "MP"
        Districts = @("Mandla", "Balaghat", "Seoni", "Chhindwara", "Betul", "Hoshangabad", "Dindori", "Shahdol", "Umaria", "Katni")
        Villages = @("Khairwani", "Bamhani", "Ghughri", "Kanha", "Mukki", "Sarhi", "Baihar", "Lalbarra", "Amarkantak", "Bandhavgarh")
        Coordinates = @(
            @{Lat=22.7196; Lon=80.5771}, @{Lat=21.8047; Lon=80.1807}, @{Lat=22.0796; Lon=79.9739}, @{Lat=22.0572; Lon=78.9389},
            @{Lat=21.9058; Lon=77.9065}, @{Lat=22.7679; Lon=77.7289}, @{Lat=22.9441; Lon=81.0820}, @{Lat=23.2967; Lon=81.3431},
            @{Lat=23.5290; Lon=80.8397}, @{Lat=23.8315; Lon=80.9061}
        )
    },
    @{
        Name = "Odisha"
        Code = "OD"
        Districts = @("Mayurbhanj", "Keonjhar", "Sundargarh", "Sambalpur", "Deogarh", "Angul", "Dhenkanal", "Kandhamal", "Rayagada", "Koraput")
        Villages = @("Similipal", "Barbil", "Rourkela", "Hirakud", "Tileibani", "Talcher", "Kamakhyanagar", "Phulbani", "Gunupur", "Jeypore")
        Coordinates = @(
            @{Lat=21.9270; Lon=86.7470}, @{Lat=21.6293; Lon=85.5895}, @{Lat=22.2604; Lon=84.8536}, @{Lat=21.4669; Lon=83.9812},
            @{Lat=21.5347; Lon=84.7338}, @{Lat=20.8397; Lon=85.0939}, @{Lat=20.6593; Lon=85.5955}, @{Lat=20.4781; Lon=84.2336},
            @{Lat=19.1626; Lon=83.4148}, @{Lat=18.8895; Lon=82.5678}
        )
    },
    @{
        Name = "Tripura"
        Code = "TR"
        Districts = @("West Tripura", "South Tripura", "Dhalai", "North Tripura", "Gomati", "Khowai", "Sepahijala", "Unakoti")
        Villages = @("Agartala", "Udaipur", "Ambassa", "Dharmanagar", "Sonamura", "Teliamura", "Bishalgarh", "Kumarghat")
        Coordinates = @(
            @{Lat=23.8315; Lon=91.2868}, @{Lat=23.5333; Lon=91.4789}, @{Lat=23.9333; Lon=91.8500}, @{Lat=24.3167; Lon=92.1667},
            @{Lat=23.4939; Lon=91.2814}, @{Lat=23.4500; Lon=91.4667}, @{Lat=23.6667; Lon=91.4167}, @{Lat=24.1167; Lon=92.0167}
        )
    },
    @{
        Name = "Telangana"
        Code = "TG"
        Districts = @("Adilabad", "Komaram Bheem", "Mancherial", "Nirmal", "Nizamabad", "Jagtial", "Peddapalli", "Jayashankar", "Mulugu", "Bhadradri")
        Villages = @("Kawal", "Jannaram", "Luxettipet", "Bhainsa", "Armoor", "Dharmapuri", "Manthani", "Eturnagaram", "Eturunagaram", "Kothagudem")
        Coordinates = @(
            @{Lat=19.6944; Lon=78.5311}, @{Lat=18.7333; Lon=79.4500}, @{Lat=18.8667; Lon=79.4500}, @{Lat=19.0833; Lon=78.3500},
            @{Lat=18.6725; Lon=78.0941}, @{Lat=18.7903; Lon=78.9242}, @{Lat=18.6127; Lon=79.3742}, @{Lat=18.3167; Lon=80.1000},
            @{Lat=18.1500; Lon=80.1667}, @{Lat=17.5500; Lon=80.6167}
        )
    }
)

$communities = @{
    "Gond" = @("Ramesh Kumar", "Sunita", "Bharat Singh", "Kamala Devi", "Ravi Kumar", "Sita", "Mohan Lal", "Radha", "Suresh", "Parvati")
    "Baiga" = @("Dukhan", "Fulkumari", "Mangal Singh", "Chameli", "Budhan", "Sukhmati", "Raman", "Phoolmati", "Dhaniram", "Kamlesh")
    "Korku" = @("Shankar", "Rukhmani", "Ganesh", "Savitri", "Ramchandra", "Laxmi", "Vishnu", "Durga", "Krishna", "Saraswati")
    "Santhal" = @("Soma", "Phulmani", "Budhan", "Champa", "Mangal", "Sukri", "Jatra", "Dulari", "Sidhu", "Rukmani")
    "Koya" = @("Ramulu", "Lakshmi", "Venkat", "Sita", "Raju", "Kamala", "Naresh", "Padma", "Suresh", "Radha")
    "Chenchu" = @("Narasimha", "Yellamma", "Rama", "Sita", "Krishna", "Lakshmi", "Venkata", "Parvati", "Ravi", "Kamala")
}

$claimTypes = @(
    "Individual Forest Rights (IFR)",
    "Community Forest Rights (CFR)", 
    "Community Forest Resource Rights",
    "Traditional Forest Dweller Rights"
)

$documents = @(
    "Ration Card", "Voter ID Card", "Community Certificate", "Land Survey Records",
    "Revenue Records", "Patta Documents", "Settlement Records", "Forest Survey Records",
    "Genealogy Records", "Traditional Use Evidence"
)

$occupations = @(
    "collection of minor forest produce",
    "traditional agriculture and livestock",
    "honey collection and beekeeping",
    "medicinal plant collection",
    "bamboo and timber collection",
    "fishing in forest streams",
    "traditional handicrafts",
    "forest-based livelihood activities"
)

function Get-RandomDate {
    $start = Get-Date "2020-01-01"
    $end = Get-Date "2023-12-31"
    $randomTicks = Get-Random -Minimum $start.Ticks -Maximum $end.Ticks
    $randomDate = New-Object DateTime($randomTicks)
    return $randomDate.ToString("dd-MM-yyyy")
}

function Get-RandomSelection {
    param($Array, $Count = 1)
    if ($Count -eq 1) {
        return $Array | Get-Random
    } else {
        return $Array | Get-Random -Count $Count
    }
}

Write-Host "Generating 600 FRA claim documents..."

for ($i = 1; $i -le 600; $i++) {
    # Select random state
    $state = $states | Get-Random
    
    # Select random data from state
    $district = Get-RandomSelection $state.Districts
    $village = Get-RandomSelection $state.Villages
    $coord = Get-RandomSelection $state.Coordinates
    
    # Add random variation to coordinates
    $lat = $coord.Lat + (Get-Random -Minimum -0.05 -Maximum 0.05)
    $lon = $coord.Lon + (Get-Random -Minimum -0.05 -Maximum 0.05)
    
    # Select random community and name
    $communityName = $communities.Keys | Get-Random
    $firstName = Get-RandomSelection $communities[$communityName]
    
    # Generate other random data
    $claimType = Get-RandomSelection $claimTypes
    $area = [math]::Round((Get-Random -Minimum 0.5 -Maximum 5.0), 1)
    $appDate = Get-RandomDate
    $selectedDocs = Get-RandomSelection $documents (Get-Random -Minimum 3 -Maximum 6)
    $occupation = Get-RandomSelection $occupations
    $yearsResiding = Get-Random -Minimum 25 -Maximum 100
    $year = Get-Random -Minimum 2020 -Maximum 2023
    
    # Generate claim ID
    $claimId = "FRA/$year/$($state.Code)/$($i.ToString().PadLeft(5, '0'))"
    
    # Create document content
    $content = @"
Forest Rights Act Claim Application

Claim ID: $claimId
Applicant Name: $firstName $communityName
Tribe/Community: $communityName
Village: $village
District: $district
State: $($state.Name)
Coordinates: $($lat.ToString("F6"))°N, $($lon.ToString("F6"))°E
Type of Claim: $claimType
Land Area Claimed: $area hectares
Application Date: $appDate

Supporting Documents:
$($selectedDocs | ForEach-Object { "- $_" } | Out-String)
Additional Information:
The claimant has been residing in the forest area for over $yearsResiding years.
Traditional occupation includes $occupation.
The family has been dependent on forest resources for their livelihood.
Evidence of traditional use and occupation has been documented.
Community elders have verified the historical presence in the area.
"@

    # Create filename
    $filename = "fra_claims/FRA_Claim_$($i.ToString().PadLeft(3, '0'))_$($claimId.Replace('/', '_')).txt"
    
    # Write file
    $content | Out-File -FilePath $filename -Encoding UTF8
    
    if ($i % 50 -eq 0) {
        Write-Host "Generated $i documents..."
    }
}

Write-Host "Successfully generated 600 FRA claim documents in the 'fra_claims' folder!"