import React from 'react'
import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api";
const PerformVPNSearch = (keyword, vpnCountry) => {
    return axios.post(`${API_URL}/vpn-search/`, { keyword, vpn_country: vpnCountry });
}

export default PerformVPNSearch
