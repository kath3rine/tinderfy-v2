function Header(props) {
    return(
        <div>
            <p>{props.name}</p>
            <img src={props.pfp} />
        </div>
        
    );
}
export default Header