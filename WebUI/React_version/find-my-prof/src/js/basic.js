import '../css/basic.css';
import { Link } from 'react-router-dom';


function Header() {
    return (
        <header>
            <h1 id="title">Black Turing AI</h1>
            <nav id="toolbar">
                <Link id="Home" to="/home">Home</Link>
                <Link id="News" to="/news">News</Link>
                <Link id="About" to="/about">About Us</Link>

                <Link to="/search">temp for search</Link>
            </nav>
        </header>
    );
}

function Footer() {
    return (
        <footer>
            <p>{">Black Turing AI - FindMyProf"}</p>   {/* uses JS string here so special symbol ">" can be used */}
            <p>© 2024 Black Turing AI. All rights reserved.</p>
        </footer>
    );
}



export { Header, Footer };