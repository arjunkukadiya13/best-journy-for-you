datalist=["Bhopal","Indore","Leh","Srinagar",
          "Jammu","Kangra-Gaggal","Kullu",
          "Shimla","Ludhiana","Chandigrah","Dehradun",
          "Bathinda","Hindon","Delhi","Patnagar","Safdarjung",
          "Bikaner","Agra","Jaipur","Jaisalmer","Jodhpur","Lucknow",
          "Kishangarh Gwalior","Kanpur","GOrakhpur","CoochBehar",
          "Udaipur","Prayagraj","Varanasi","Patana","Gaya",
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
          "Ranchi","Jamshedpur"
          ]
def datacheck(a,b):
    if a in datalist and b in datalist:
        return True
    else:
        return False