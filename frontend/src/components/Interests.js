function Interests({list}) {
    return(
        <div className="component" id="interests">
              <h3>Genres</h3> 
              <div id="bubbles">
                {list.map((item) => (
                    <div id="bubble">{item}</div>
                ))}
              </div>
        </div>
    );
}
export default Interests;