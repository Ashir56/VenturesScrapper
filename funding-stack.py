import random
import time

import requests



def refreshing_tokens(refresh_token):

    print("refreshing tokens")
    url = "https://api.fundingstack.com/v3/sessions"
    payload = {}
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'cookie': '_ga=GA1.1.2073881975.1721048101; _hjSessionUser_3089276=eyJpZCI6IjAyZGYzMTA2LTA2NTItNTMxOC1iYjY4LWVmZTM0YmI5NTA2MiIsImNyZWF0ZWQiOjE3MjEwNDgxMDEyMDYsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_3089276=eyJpZCI6IjE1MjBlOGFkLTVhMzYtNGM4My1hM2FiLTU4MTFmNDM3NDIzZiIsImMiOjE3MjEwNDgxMDEyMDcsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; intercom-id-n2xmi9eu=1fe04c08-b871-4722-82bf-e26dab33539e; intercom-device-id-n2xmi9eu=f2b16a33-89b6-4730-9d96-b31a9909b37c; Domain=; cf_clearance=sRLqAIBuED0UGL4xlfONu.tEqs6gXfl58ilPCCSidAM-1721050098-1.0.1.1-T4.2yIyaNRcOL4.mXirStQEq3y.kXVYPByc9t_94fD8BbzN1uSjHv4ftxa7UfDSPuFXTA_FYFeCuamonb6X14A; ajs_anonymous_id=dc22fe49-ce1b-42f2-b4de-1c301f17ee4d; ajs_user_id=114707; intercom-session-n2xmi9eu=TVNoVXlmb3NvZllLM1BlSGJoS1dyamRtTElieHR4QUZLS3IrMVhTNXRPbHN1d1UwbVhNQUZnMjBGVlExcXEwdi0tL2dHRkUvR2pBYzJpTnY3QUF3TVRpUT09--4ebeb11f7dccea57f81ba045ccc70541dc506747; refreshToken='+ refresh_token +'; _ga_DSTED8KWBJ=GS1.1.1721048100.1.1.1721052274.0.0.0',
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
    url = "https://api.fundingstack.com/v3/accounts/78521/rounds/87507/investor_database?page=" + str(page)

    payload = {}
    headers = {
        'authority': 'api.fundingstack.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': '_ga=GA1.1.2073881975.1721048101; _hjSessionUser_3089276=eyJpZCI6IjAyZGYzMTA2LTA2NTItNTMxOC1iYjY4LWVmZTM0YmI5NTA2MiIsImNyZWF0ZWQiOjE3MjEwNDgxMDEyMDYsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_3089276=eyJpZCI6IjE1MjBlOGFkLTVhMzYtNGM4My1hM2FiLTU4MTFmNDM3NDIzZiIsImMiOjE3MjEwNDgxMDEyMDcsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; intercom-id-n2xmi9eu=1fe04c08-b871-4722-82bf-e26dab33539e; intercom-device-id-n2xmi9eu=f2b16a33-89b6-4730-9d96-b31a9909b37c; Domain=; cf_clearance=sRLqAIBuED0UGL4xlfONu.tEqs6gXfl58ilPCCSidAM-1721050098-1.0.1.1-T4.2yIyaNRcOL4.mXirStQEq3y.kXVYPByc9t_94fD8BbzN1uSjHv4ftxa7UfDSPuFXTA_FYFeCuamonb6X14A; ajs_anonymous_id=dc22fe49-ce1b-42f2-b4de-1c301f17ee4d; ajs_user_id=114707; intercom-session-n2xmi9eu=R0tnVG9COXFuSkNxdkFkUW5LeEpFV3JEZy9pTlFqb0RwWHl1VEJEMGRrUnJMTk5NQTc5cVp4Z2N5YVdleTJzRC0td1RVZGZRSnkySXIwWm5aRjExKzljUT09--e620dcf923d72fa4e82e109c79c68f579da45e14; accessToken='+access_token+'; refreshToken='+refresh_token+'; _ga_DSTED8KWBJ=GS1.1.1721048100.1.1.1721051333.0.0.0',
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


new_access_token = "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJhcGkuZnVuZGluZ3N0YWNrLmNvbSIsInN1YiI6MTE0NzA3LCJleHAiOjE3MjEwNTQzMzksImlhdCI6MTcyMTA1NDIxOSwianRpIjoiZjFiNmE0NTYtOTMwOS00N2U0LWFkOGMtOWRlOGUyYzcxZDM5IiwidXNlciI6eyJpZCI6MTE0NzA3LCJuYW1lIjpudWxsLCJlbWFpbCI6ImpvY2tlLm1hcnRlbGl1c0BhcXZjLmNvbSIsImFkbWluIjpmYWxzZX19.q7rYyRVT7nmlNBuUk_QEOGl5wvvP1Q8WQmrd8wHFBteJFBJPpb5QsHIQ77-HOGgM9mRY7CZxA0E_Lc5em8-i2gAPpXTDAkz4KGnnj96CONkq-ZdFsqV_ic6bQqWWpNDRn5Ey7NXOg1EUXv6-IC9vDpiaWNv9Cu1TFssM-PakzXRs2AW6L0BU6xfHhQvJNUFxLxH9uzno32y-axDo0Bn2MGN7DcfuhElUQxDUaqBbiaqx-jFjSB34FjK1JsfhzqVRm6baJ-m1j-ZlM4FCV7tlBtreq9MOJR-v7x2l1NAbitUfMOnda6CTBpx3ZV3-GS54vNzKEehClQ2VoqrEL8cmjQ"
new_refresh_token = "93de8e33068a34d40862d62185773acef628692b3047df1b29158e8693a337d3"


for i in range(1,11363):

    response = api_request(i, new_access_token, new_refresh_token)
    if response.status_code == 401:
        new_access_token, new_refresh_token = refreshing_tokens(new_refresh_token)
        response_again = api_request(i, new_access_token, new_refresh_token)
        if response_again.status_code == 401:
            break
    else:
        print("Scrapped page: " + str(i))

    wait = random.randint(20,30)
    print(f"waiting {wait}s")
    time.sleep(wait)
