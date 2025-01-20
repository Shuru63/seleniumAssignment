import React from 'react'
import  { useState, useEffect } from 'react';
import Form from './Form';

const Page = () => {
    const [results, setResults] = useState([]);

  return (
    <div className="container">
    <h1 className="title">VPN Keyword Search Automation</h1>
    <Form setResults={setResults} />
    <ul className="results-list">
        {results.map((result, index) => (
            <li key={index} className="result-item">
                <span className="keyword">Keyword: {result.keyword}</span>, 
                <span className="country">Country: {result.vpn_country}</span>, 
                <span className="result">Result: {result.result}</span>
            </li>
        ))}
    </ul>
</div>

  )
}

export default Page
