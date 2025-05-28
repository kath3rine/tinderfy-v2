function Basics(props) {
    return(
        <div className="component" id="basics">
                <h3>Recommendations</h3>
                <div className="basic-item" id={`${props.track == "None" ? "artist-no-track-rec" : "artist-track-rec"}`}>
                    <p className="basic-title">Artist</p>
                    <p className="basic-text">{props.artist}</p>
                </div>
                <div className="basic-item" id={`${props.track == "None" ? "no-track-rec" : "track-rec"}`}>
                    <p className="basic-title">Song</p>
                    <p className="basic-text">{props.track}</p>
                </div>
            </div>
    );
}
export default Basics;