import random
import time
import os
import json

import requests


# def append_to_json_file(new_data, file_path='investors_data.json'):
#     if os.path.exists(file_path):
#         with open(file_path, 'r') as json_file:
#             if json_file:
#                 existing_data = json.load(json_file)
#         existing_data.extend(new_data)
#     else:
#         existing_data = new_data
#
#     # Save updated data back to the file
#     with open(file_path, 'w') as json_file:
#         json.dump(existing_data, json_file, indent=4)
#
#     print(f"Data has been appended to {file_path}")


def append_to_json_file(new_data, file_path='investors_filtered_data2(1288).json'):
    # Check if the file exists
    if os.path.exists(file_path):
        # Load existing data from the file
        try:
            with open(file_path, 'r') as json_file:
                existing_data = json.load(json_file)
        except json.JSONDecodeError:
            existing_data = []
    else:
        # If file doesn't exist, initialize with an empty list
        existing_data = []

    # Append new data to the existing data
    existing_data.extend(new_data)

    # Save updated data back to the file
    with open(file_path, 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)

    print(f"Data has been appended to {file_path}")


def refreshing_tokens(refresh_token):
    print("refreshing tokens")
    url = "https://api.fundingstack.com/v3/sessions"
    payload = {}
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'cookie': '_ga=GA1.1.2073881975.1721048101; _hjSessionUser_3089276=eyJpZCI6IjAyZGYzMTA2LTA2NTItNTMxOC1iYjY4LWVmZTM0YmI5NTA2MiIsImNyZWF0ZWQiOjE3MjEwNDgxMDEyMDYsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_3089276=eyJpZCI6IjE1MjBlOGFkLTVhMzYtNGM4My1hM2FiLTU4MTFmNDM3NDIzZiIsImMiOjE3MjEwNDgxMDEyMDcsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; intercom-id-n2xmi9eu=1fe04c08-b871-4722-82bf-e26dab33539e; intercom-device-id-n2xmi9eu=f2b16a33-89b6-4730-9d96-b31a9909b37c; Domain=; cf_clearance=sRLqAIBuED0UGL4xlfONu.tEqs6gXfl58ilPCCSidAM-1721050098-1.0.1.1-T4.2yIyaNRcOL4.mXirStQEq3y.kXVYPByc9t_94fD8BbzN1uSjHv4ftxa7UfDSPuFXTA_FYFeCuamonb6X14A; ajs_anonymous_id=dc22fe49-ce1b-42f2-b4de-1c301f17ee4d; ajs_user_id=114707; intercom-session-n2xmi9eu=TVNoVXlmb3NvZllLM1BlSGJoS1dyamRtTElieHR4QUZLS3IrMVhTNXRPbHN1d1UwbVhNQUZnMjBGVlExcXEwdi0tL2dHRkUvR2pBYzJpTnY3QUF3TVRpUT09--4ebeb11f7dccea57f81ba045ccc70541dc506747; refreshToken=' + refresh_token + '; _ga_DSTED8KWBJ=GS1.1.1721048100.1.1.1721052274.0.0.0',
        'origin': 'https://www.fundingstack.com',
        'priority': 'u=1, i',
        'referer': 'https://www.fundingstack.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'x-csrf-protected': 'true'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    access_token = response.cookies.get("accessToken")
    refresh_token = response.cookies.get("refreshToken")

    if response.status_code == 200:
        print("tokens refreshed")
        return access_token, refresh_token

    return "", ""


def api_request(page, access_token, refresh_token):
    print("Scrapping page: " + str(page))
    # url = "https://api.fundingstack.com/v3/accounts/78521/rounds/87507/investor_database?page=" + str(page)

    url = "https://api.fundingstack.com/v3/accounts/78521/rounds/87507/investor_database?page=" +str(page) + "&type=ew%2Cfo%2Cf%2Ca%2Cfof%2Clp%2Cii%2Ctr%2Ccvc%2Cria%2Cvc&industry=224%2C1713%2C438%2C3683%2C4507%2C1824%2C4514%2C20%2C19%2C43%2C4411%2C375%2C4494%2C606%2C1894%2C2005%2C743%2C163%2C447%2C1897%2C1281%2C698%2C504%2C180%2C502%2C499%2C503%2C454%2C249%2C143%2C1166%2C4048%2C556%2C4454%2C4383%2C557%2C555%2C460%2C189%2C1118%2C878%2C333%2C1037%2C199%2C3612%2C800%2C2807%2C610%2C919%2C390%2C292%2C807%2C233%2C877%2C3749%2C3958%2C4491%2C2017%2C4398%2C1768%2C48%2C542%2C496%2C56%2C971%2C61%2C494%2C495%2C55%2C1935%2C4387%2C4413%2C45%2C62%2C540%2C8%2C46%2C490%2C47%2C4073%2C4409%2C779%2C4384%2C879%2C68%2C1088%2C4487%2C201%2C198%2C197%2C1200%2C1913%2C120%2C4397%2C1034%2C4520%2C705%2C301%2C467%2C280%2C278%2C1910%2C2808&stage_focus=1%2C2%2C3%2C4"

    payload = {}
    headers = {
        'authority': 'api.fundingstack.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': '_ga=GA1.1.2073881975.1721048101; _hjSessionUser_3089276=eyJpZCI6IjAyZGYzMTA2LTA2NTItNTMxOC1iYjY4LWVmZTM0YmI5NTA2MiIsImNyZWF0ZWQiOjE3MjEwNDgxMDEyMDYsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_3089276=eyJpZCI6IjE1MjBlOGFkLTVhMzYtNGM4My1hM2FiLTU4MTFmNDM3NDIzZiIsImMiOjE3MjEwNDgxMDEyMDcsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; intercom-id-n2xmi9eu=1fe04c08-b871-4722-82bf-e26dab33539e; intercom-device-id-n2xmi9eu=f2b16a33-89b6-4730-9d96-b31a9909b37c; Domain=; cf_clearance=sRLqAIBuED0UGL4xlfONu.tEqs6gXfl58ilPCCSidAM-1721050098-1.0.1.1-T4.2yIyaNRcOL4.mXirStQEq3y.kXVYPByc9t_94fD8BbzN1uSjHv4ftxa7UfDSPuFXTA_FYFeCuamonb6X14A; ajs_anonymous_id=dc22fe49-ce1b-42f2-b4de-1c301f17ee4d; ajs_user_id=114707; intercom-session-n2xmi9eu=R0tnVG9COXFuSkNxdkFkUW5LeEpFV3JEZy9pTlFqb0RwWHl1VEJEMGRrUnJMTk5NQTc5cVp4Z2N5YVdleTJzRC0td1RVZGZRSnkySXIwWm5aRjExKzljUT09--e620dcf923d72fa4e82e109c79c68f579da45e14; accessToken=' + access_token + '; refreshToken=' + refresh_token + '; _ga_DSTED8KWBJ=GS1.1.1721048100.1.1.1721051333.0.0.0',
        'if-none-match': 'W/"32b1c4de0e96f7cd96849cac20457681"',
        'origin': 'https://www.fundingstack.com',
        'priority': 'u=1, i',
        'referer': 'https://www.fundingstack.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'x-csrf-protected': 'true'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response)
    print(response.text)
    return response
    # print("Scrapped page: " + str(i))


new_access_token = "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJhcGkuZnVuZGluZ3N0YWNrLmNvbSIsInN1YiI6MTE0NzA3LCJleHAiOjE3MjE3NDA4NDksImlhdCI6MTcyMTc0MDcyOSwianRpIjoiMGViZmQ3OTMtOTcwYi00ZThlLTgwYzUtYzM3YzVhZjNmZThlIiwidXNlciI6eyJpZCI6MTE0NzA3LCJuYW1lIjpudWxsLCJlbWFpbCI6ImpvY2tlLm1hcnRlbGl1c0BhcXZjLmNvbSIsImFkbWluIjpmYWxzZX19.OEmn420y2i9GJcDmHFw9iTkRZA3pqeYikwZR_ViPE_yF4OPgCRTuIRGKZoYZk-SrWJLnITNz7dV6eDjsVGQ9s2KGLWMxJor_cVBIF4SpIxSkgHd1XZiubJeIxmvjuDkRoh-x0sBA992tJMgSb4Wp_GvuQx6iJxPL3wepko5uxMLKba19s40NfEaSRh9LO-1Z_D6YoD0EJ7f7HDjKyhDVV5B7OQdPx5GCnByc9E4R2Jau2m_x6chfVZ5_4SxsQE3VWk2kuoVFjC7zWpjlhgDqWup7x8FG0G0ecGhpT2wdx6EcpX6va7a9HcsnA0bf2GSt9-SL-1ejDVoPcULDWOkKOA"
new_refresh_token = "38fff24c67af37ad191d0cd1a781122df7268537e4508392696ab548a02e5427"

for i in range(1565, 1570):

    response = api_request(i, new_access_token, new_refresh_token)
    if response.status_code == 401:
        new_access_token, new_refresh_token = refreshing_tokens(new_refresh_token)
        response_again = api_request(i, new_access_token, new_refresh_token)
        if response_again.status_code == 401:
            break
        elif response_again.status_code == 200:
            text_data = json.loads(response_again.text)
            data = text_data["data"]["response_object"]["investors"]
            append_to_json_file(data)
        else:
            break
    elif response.status_code == 200:
        text_data = json.loads(response.text)
        data = text_data["data"]["response_object"]["investors"]
        append_to_json_file(data)

    else:
        print("Scrapped page: " + str(i))
        break

    wait = random.randint(10, 15)
    print(f"waiting {wait}s")
    time.sleep(wait)
