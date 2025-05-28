function Interests(props) {
    return(
        <div className="component" id="interests">
              <h3>{props.title}</h3> 
              <div id="bubbles">
                {props.list.map((item) => (
                    <div id="bubble">{item}</div>
                ))}
              </div>
        </div>
    );
}
export default Interests;