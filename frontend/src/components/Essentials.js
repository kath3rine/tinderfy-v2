function Essentials({list}) {
    return(
        <div>
              favorite artists: 
              {list.map((item) => (
                <li>{item}</li>
              ))}
        </div>
    );
}
export default Essentials;