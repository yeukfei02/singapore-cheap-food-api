import requests


def find_address_handler(request):
    print(f"request.args = {request.args}")

    response = {
        "message": "find_address",
        "result": {}
    }

    if request.args:
        search_value = request.args.get("searchValue")
        print(f"search_value = {search_value}")

        one_map_api_result = one_map_api(search_value)

        if one_map_api_result:
            response = {
                "message": "find_address",
                "result": one_map_api_result
            }

    headers = {
        "Access-Control-Allow-Origin": "*"
    }

    return (response, 200, headers)


def get_cheap_food_handler(request):
    print(f"request.args = {request.args}")

    get_budget_meal_result = get_budget_meal_api()

    response = {
        "message": "get_cheap_food",
        "result": get_budget_meal_result
    }

    headers = {
        "Access-Control-Allow-Origin": "*"
    }

    return (response, 200, headers)


def one_map_api(search_value):
    result = None

    try:
        root_url = "https://www.onemap.gov.sg/api/common/elastic/search"

        params = {
            "searchVal": search_value,
            "returnGeom": "Y",
            "getAddrDetails": "Y",
            "pageNum": "1"
        }

        response = requests.get(root_url, params=params)
        print(f"response = {response}")

        response_json = response.json()
        print(f"response_json = {response_json}")

        if response_json:
            formatted_results = []

            if response_json["results"]:
                for item in response_json["results"]:
                    data = {
                        "searchVal": item["SEARCHVAL"],
                        "blkNo": item["BLK_NO"],
                        "roadName": item["ROAD_NAME"],
                        "building": item["BUILDING"],
                        "address": item["ADDRESS"],
                        "postal": item["POSTAL"],
                        "X": item["X"],
                        "Y": item["Y"],
                        "latitude": item["LATITUDE"],
                        "longitude": item["LONGITUDE"]
                    }
                    formatted_results.append(data)

            data = {
                "found": response_json["found"],
                "totalNumPages": response_json["totalNumPages"],
                "pageNum": response_json["pageNum"],
                "results": formatted_results
            }

            result = data
    except Exception as e:
        print(f"one_map_api error = {e}")

    return result


def get_budget_meal_api():
    result = None

    try:
        root_url = "https://www.gowhere.gov.sg/budgetmeal/data/data.json"

        response = requests.get(root_url)
        print(f"response = {response}")

        response_json = response.json()
        print(f"response_json = {response_json}")

        if response_json:
            formatted_data = []

            if response_json["data"]:
                for item in response_json["data"]:
                    data = {
                        "address": item["address"],
                        "postalCode": item["postalCode"],
                        "name": item["name"],
                        "description": item["description"],
                        "lat": item["LAT"],
                        "lon": item["LON"],
                        "filters": item["filters"]
                    }
                    formatted_data.append(data)

            data = {
                "lastUpdated": response_json["lastUpdated"],
                "data": formatted_data
            }

            result = data
    except Exception as e:
        print(f"get_budget_meal_api error = {e}")

    return result
