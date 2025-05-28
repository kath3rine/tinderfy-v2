function MyAnthem(props) {
    return(
        <div className="component" id="my-anthem">
            <h3>My album</h3>
            <div id="my-anthem-container">
                <img src={props.pfp} />
                <div id="my-anthem-text">
                    <h3>{props.name}</h3>
                    <p>{props.artist}</p>
                </div>
            </div>
        </div>
        
    );
}
export default MyAnthem