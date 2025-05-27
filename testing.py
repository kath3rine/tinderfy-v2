import requests

access_token = "BQCvWKFCfthUyJN-wkZk-98CwCvSNpA8va6nYE3iROB9JqA7v3ytIdoEMyiV9y5G3TBP8ZXrxLHUy1mX-zHB9OIooeGs-4Wuco4sm5OgHYlzHG-WbE2wPmuPoTr1gcIhmA_CPxiH_gTCbzMbp-YfRqDfVI0cdh2GrW_jN1IzPCdfaB1BIV5VKsLTmPwmSaKweGxsjReaBCi0FSFMeTRwpZ-f8YAa6nLpnZ2zLrMRHRLddIcD61ao"  # Must be from authorization code flow
track_id = "11dFghVXANMlKmJXsNCbNl"  # Spotify's demo track

headers = {
    "Authorization": f"Bearer {access_token}"
}

url = f"https://api.spotify.com/v1/audio-features/{track_id}"
response = requests.get(url, headers=headers)

print("Status:", response.status_code)
print("Response:", response.text)
