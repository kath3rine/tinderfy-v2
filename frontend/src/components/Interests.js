function Interests({list}) {
    return(
        <div>
              favorite genres: 
              {list.map((item) => (
                <li>{item}</li>
              ))}
        </div>
    );
}
export default Interests;