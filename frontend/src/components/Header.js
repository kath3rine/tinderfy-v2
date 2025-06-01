function Header(props) {
    return(
        <div className="component" id="header">
            <div id="name-container">
                <h1 id="name">{props.name}</h1>
            </div>
            
            <div id="pfp-container">
                <img id="pfp" src={props.pfp} />
            </div>
            
        </div>
        
    );
}
export default Header