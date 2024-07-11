datalist=["Bhopal","Indore","Leh","Srinagar",
          "Jammu","Kangra-Gaggal","Kullu",
          "Shimla","Ludhiana","Chandigrah","Dehradun",
          "Bathinda","Hindon","Delhi","Patnagar","Safdarjung",
          "Bikaner","Agra","Jaipur","Jaisalmer","Jodhpur","Lucknow",
          "Kishangarh Gwalior","Kanpur","Gorakhpur","CoochBehar",
          "Udaipur","Prayagraj","Varanasi","Patna","Gaya",
          "Khajuraho","Satna","Durgapur","Bhuj","Kandla",
          "Jabalpur","Jamnagar","Rajkot","Vadodara","Porbandar","Keshod",
          "Bhavnagar","Surat","Jalgaon","Nashik","Gandhinagar",
          "Aurangabad","Mumbai","Shirdi","Nagpur","Nanded",
          "Juhu","Pune","Div","Kolhapur","Hyderabad","Belagavi",
          "Vijayawada","Belagavi","Hubli","Goa","KAdapa",
          "Bengaluru","Tirupati","Mysore","Chennai","Kannur",
          "Puducherry","Salem","Kozhikode","Coimbatore","Kochi",
          "Tiruchiralli","Thanjavur","Madurai",
          "Thiruvananthapura","Thoothukudi","Kadapa",
          "Raipur","Nagpur","Jabalpur","Satna","Patana",
          "Ranchi","Jamshedpur","Lucknow","Ranchi","Jharsuguda",
          "Visakhapatnam","Rajahmundry","Bhuvneswer","Kolkata",
          "Gangtok","Bagdogra","Guwahati","Shillong","Silchar",
          "Agartala","Agartala","Lengpui","Imphal",
          "Dimapur","Jorhat","Lilabari","Passighat",
          "Dibrugrah","Tezu","Ahmedabad"
          ]
datalist1=[]
for s in datalist:
    datalist1.append(s.lower())
    
    
datelist=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

monthlist=["January","February","March","April","May","june","July","Augest","September","Octomber","Nivember","December"]
    
# print(datalist1)


#           "Juhu","Pune","Div","Kolhapur","Hyderabad","Belagavi",
#           "Vijayawada","Belagavi","Hubli","Goa","KAdapa",
#           "Bengaluru","Tirupati","Mysore","Chennai","Kannur",

apikeys1=[23.291124,22.728090,34.143233,34.002317,32.681156,32.165169,31.825407,31.085943,30.850658,30.668108,30.195274,30.271674,28.705237,29.033694,28.583698,
          28.055768,27.162085,26.829112,26.870836,26.264585,26.761921,26.589638,26.409782,26.746580,26.329915,24.639582,25.430424,25.448320,25.599584,24.749051,
          24.810633,24.571242,23.618041,23.275660,23.109917,23.183197,22.460881,22.309073,22.333855,21.647892,21.318210,21.753941,21.121259,20.961632,20.113238,
          19.963796,19.867962,19.097353,19.692892,21.177035,19.183536,]
apikeys2=[77.335670,75.804204,77.554237,74.762488,74.842260,76.260181,77.472878,77.066105,75.956378,76.786035,78.192176,74.745860,77.342336,79.469030,77.211172,
          73.196316,77.970820,75.805664,70.855922,73.050593,80.885766,74.817085,80.409494,83.442908,89.469959,73.890818,81.471249,82.856953,85.085679,84.943779,
          79.912506,80.854105,87.240207,69.663998,70.104276,80.057008,70.015910,70.782321,73.226678,69.661041,70.267115,72.183477,72.742006,75.619148,73.893802,
          73.807493,75.395819,72.874745,74.394217,79.107196,77.334778,]
# print(datalist[len(apikeys1)])
def datacheck(a,b):
    if a in datalist and b in datalist:
        lst1=[]
        lst2=[]
        i=0
        j=0
        for s in datalist:
            if s==a:
                lst1.append(apikeys1[i])
                lst2.append(apikeys2[i])
                break
            else:
                i=i+1
        for s in datalist:
            if s==b:
                lst1.append(apikeys1[j])
                lst2.append(apikeys2[j])
                break
            else:
                j=j+1
        return lst1,lst2
    else:
        return False
    