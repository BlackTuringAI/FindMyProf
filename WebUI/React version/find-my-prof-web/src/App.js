import './App.css';

function App() {
  return (
    <div className="App">
      <ToolBar />
      <MainContent />
      <Footer />
    </div>
  );
}

function ToolBar() {
  return (
    <nav>
      <h1 id="title">FindMyProf</h1>
      <div id="toolbar">
        <a id="Coming" class="toolbar-opt" href="{{ url_for('home') }}" >Home</a>
        <a id="About" class="toolbar-opt" href="{{ url_for('about') }}">About us</a>
        <a id="Company" class="toolbar-opt" href="{{ url_for('Company weblink') }}">Company weblink</a>
      </div>
    </nav>
  );
}

function MainContent() {
  return (
    <div id="main">
      <div id="upper-half">
        <ProfProfile />

        <div id="Me">Booker</div>
      </div>

      <div id="lower-half">
        <div id="Form">
            Form
        </div>
        <RankingBoard />
      </div>
    </div>
  );
}

function ProfProfile() {
  const url = "https://www.w3schools.com/howto/img_avatar.png";
  return (
    <div id="ProfProfile">
      <div id="Details">
        <p>Details</p>
      </div>
      <div id="Pic">
        <img id="ProfPic" src={url} alt="Avatar" />
      </div>
    </div>
  );
}

function RankingBoard() {
  const rankings = ['Rank 1', 'Rank 2', 'Rank 3', 'Rank 4', 'Rank 5']; // replace this with actual data

  return (
    <div id="Ranking-board">
      <ul>
        {rankings.map((ranking) => (
          <li>{ranking}</li>
        ))}
      </ul>
    </div>
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

export default App;

