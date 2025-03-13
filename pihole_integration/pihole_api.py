"""
Pi-hole API Integration Module (REAL)

This module provides functions to interact with the Pi-hole API.

It uses the 'requests' library to make API calls and retrieves
real-time data from a Pi-hole instance.

Future enhancements:
- Implement robust error handling and retry mechanisms for API calls.
- Securely manage Pi-hole API token (e.g., using secrets management).
- Add more Pi-hole API functionalities (e.g., whitelist management, query logs).
"""

import streamlit as st
import requests

PIHOLE_API_URL = st.secrets["pihole_api"]["url"]  # Get from Streamlit secrets
PIHOLE_API_TOKEN = st.secrets["pihole_api"]["token"] # Get from Streamlit secrets


def get_pihole_status_from_api():
    """Fetches Pi-hole status from the API and returns it."""
    try:
        response = requests.get(PIHOLE_API_URL + "?status", params={'auth': PIHOLE_API_TOKEN})
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        return data.get("status", "unknown").lower()  # "enabled" or "disabled"
    except requests.exceptions.RequestException as e:
        return f"api_error: {e}"  # Indicate API error in status

def format_pihole_status_response(pihole_status):
    """Formats Pi-hole status for display in the UI."""
    if "api_error" in pihole_status:
        return f"<b>Pi-hole Status:</b> Error communicating with Pi-hole API. Check API URL and token.\nDetails: {pihole_status}"
    else:
        return f"<b>Pi-hole Status:</b> {pihole_status.upper()}"


def enable_pihole_api():
    """Calls the Pi-hole API to enable Pi-hole."""
    try:
        response = requests.get(PIHOLE_API_URL + "?enable", params={'auth': PIHOLE_API_TOKEN})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {e}"}

def disable_pihole_api():
    """Calls the Pi-hole API to disable Pi-hole."""
    try:
        response = requests.get(PIHOLE_API_URL + "?disable", params={'auth': PIHOLE_API_TOKEN, 'time': 30}) # Disable for 30 seconds as example
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {e}"}

def format_pihole_enable_disable_response(api_response, action):
    """Formats the Pi-hole enable/disable API response for UI display."""
    if "error" in api_response:
        return f"Failed to {action} Pi-hole: {api_response['error']}"
    else:
        return f"Pi-hole {action}d."


def get_pihole_summary_api():
    """Fetches Pi-hole summary data from the API."""
    try:
        response = requests.get(PIHOLE_API_URL + "?summary", params={'auth': PIHOLE_API_TOKEN})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {e}"}

def format_pihole_summary_response(summary_data):
    """Formats Pi-hole summary data for display in the UI."""
    if "error" in summary_data:
        return f"Error fetching Pi-hole summary: {summary_data['error']}"
    else:
        summary_response = "<b>Pi-hole Summary:</b>\n"
        summary_response += f"- Total Queries: {summary_data['dns_queries_today']}\n"
        summary_response += f"- Queries Blocked: {summary_data['ads_blocked_today']} ({summary_data['ads_percentage_today']}%)\n"
        summary_response += f"- Domains on Adlists: {summary_data['domains_being_blocked']}\n"
        return summary_response


def get_pihole_top_domains_blocked_api():
    """Fetches top blocked domains data from the Pi-hole API."""
    try:
        response = requests.get(PIHOLE_API_URL + "?topDomainsBlocked&getQueryTypes", params={'auth': PIHOLE_API_TOKEN}) # Added getQueryTypes
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {e}"}

def format_pihole_top_blocked_response(top_blocked_data):
    """Formats top blocked domains data for display in the UI."""
    top_blocked_response = ""
    if "error" in top_blocked_data:
        top_blocked_response = f"Error fetching top blocked domains: {top_blocked_data['error']}"
    elif not top_blocked_data or not top_blocked_data.get('top_domains_blocked'): # Handle empty or missing data
        top_blocked_response = "No top blocked domains data available."
    else:
        top_blocked_response = "<b>Top Blocked Domains:</b>\n"
        for domain, count in top_blocked_data['top_domains_blocked'].items():
            top_blocked_response += f"- {domain}: {count} blocks\n"
    return top_blocked_response


def add_pihole_blacklist_api(domain):
    """Calls the Pi-hole API to add a domain to the blacklist."""
    try:
        response = requests.get(PIHOLE_API_URL + f"?blacklist&domain={domain}", params={'auth': PIHOLE_API_TOKEN})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {e}"}

def remove_pihole_blacklist_api(domain):
    """Calls the Pi-hole API to remove a domain from the blacklist."""
    try:
        response = requests.get(PIHOLE_API_URL + f"?blacklist_delete&domain={domain}", params={'auth': PIHOLE_API_TOKEN})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {e}"}

def add_pihole_blacklist_display(prompt): # Basic display function, can be improved
    """Extracts domain from prompt and calls blacklist API, returns display response."""
    domain_to_blacklist = prompt.split("blacklist domain add")[-1].strip() #Very basic extraction
    if domain_to_blacklist:
        api_response = add_pihole_blacklist_api(domain_to_blacklist)
        if "error" in api_response:
            return f"Failed to blacklist domain: {api_response['error']}"
        else:
            return f"Domain '{domain_to_blacklist}' added to blacklist."
    else:
        return "Please specify a domain to blacklist (e.g., 'blacklist domain add example.com')."

def remove_pihole_blacklist_display(prompt): # Basic display function, can be improved
    """Extracts domain from prompt and calls unblacklist API, returns display response."""
    domain_to_unblacklist = prompt.split("blacklist domain remove")[-1].strip() #Basic extraction
    if domain_to_unblacklist:
        api_response = remove_pihole_blacklist_api(domain_to_unblacklist)
        if "error" in api_response:
            return f"Failed to remove domain from blacklist: {api_response['error']}"
        else:
            return f"Domain '{domain_to_unblacklist}' removed from blacklist."
    else:
        return "Please specify a domain to remove from blacklist (e.g., 'blacklist domain remove example.com')."
