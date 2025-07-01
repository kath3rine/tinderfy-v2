import React from 'react'

function Header({name, pfp}) {
    return(
        <div className="component" id="header">
            <div id="name-container">
                <h1 id="name">{name}</h1>
            </div>
            
            <div id="pfp-container">
                <img id="pfp" src={pfp} />
            </div>
            
        </div>
        
    );
}
export default Header