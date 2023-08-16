/**
Challenge: Complete the Navbar to match the design

Hint: use the Figma file for the most accurate peek at the design
(colors, sizes, fonts, etc.)
*/

import React from "react"

export default function Navbar() {
    return (
        <div id = "navbar">
        <img src="./images/react-icon-small.png" />
        <strong><p style={{color: '#00D8FF', margin: '4px'}} id="rf">ReactFacts</p></strong>
        <p id="reactc">React Course - Project 1</p>
        </div>
        
        
        
    )
    
}