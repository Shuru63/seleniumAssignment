import React from 'react'
import  { useState, useEffect } from 'react';
import PerformVPNSearch from './PerformVPNSearch';
const Form = ({ setResults }) => {
    const [keyword, setKeyword] = useState("");
        const [vpnCountry, setVpnCountry] = useState("");
    
        const handleSubmit = async (e) => {
            e.preventDefault();
            try {
                const response = await PerformVPNSearch(keyword, vpnCountry);
                setResults((prev) => [...prev, response.data]);
            } catch (error) {
                console.error("Error performing VPN search:", error);
            }
        };
  return (
    <div>
        <form onSubmit={handleSubmit} className="search-form">
    <input
        type="text"
        placeholder="Keyword"
        value={keyword}
        onChange={(e) => setKeyword(e.target.value)}
        className="input-field"
    />
    <input
        type="text"
        placeholder="VPN Country"
        value={vpnCountry}
        onChange={(e) => setVpnCountry(e.target.value)}
        className="input-field"
    />
    <button type="submit" className="submit-btn">Search</button>
</form>

    </div>
  )
}

export default Form
