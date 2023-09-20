import csv

with open('bus_stops.csv', 'r', encoding='windows-1251') as bs:
    fields = ['ID', 'Name', 'Longitude_WGS84', 'Latitude_WGS84', 'AdmArea', 'District', 
              'RouteNumbers', 'StationName', 'Direction', 'Pavilion', 'OperatingOrgName', 
              'EntryState', 'global_id', 'PlaceDescription', 'Works', 'geodata_center', 'geoarea']
    reader = csv.DictReader(bs, fields, delimiter=';')
    stops = []
    streets = []
    for row in reader:
        stops.append(row['ID'])
        streets.append(row['Name'])
    most_common_street = max(set(streets), key=streets.count)

    start_index = most_common_street.find('(')
    most_common_street = most_common_street[:start_index] 

    print('Количесвто остановок составляет:', len(stops))
    print('Больше всего остановок на:', most_common_street)
