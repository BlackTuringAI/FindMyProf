import '../css/basic.css';



function Header() {
    return (
        <header>
            <h1 id="title">Black Turing AI</h1>
            <nav id="toolbar">
                <a id="Home" href="http://127.0.0.1:5000">Home</a>
                <a id="News" href="">News</a>
                <a id="About" href="">About Us</a>

                <a href="http://127.0.0.1:5000/search">temp for search</a>
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