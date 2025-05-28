function Header(props) {
    return(
        <div className="component" id="header">
            <h1>{props.name}</h1>
            <img id="pfp" src={props.pfp} />
        </div>
        
    );
}
export default Header