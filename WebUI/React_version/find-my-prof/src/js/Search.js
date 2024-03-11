import '../css/Search.css';

import {Header, Footer} from './basic'



function Search() {
    return (
        <div className="Search">
            <Header />
            <MainContent />
            <Footer />
        </div>
    );
}

function MainContent() {
    return (
        <div id="main">
			<div id="lower-half">
				<ProfProfile />
                <Form />
                <RankingBoard />
			</div>
		</div>
    );
}
  
function ProfProfile() {
    const url = "https://www.w3schools.com/howto/img_avatar.png";

    return (
        <div id="upper-half">
            <div id="Details">
                <p>Details</p>
            </div>

            <div id="Pic">
                <img src={url} alt="Avatar" />
            </div>

            <div id="Me">Booker</div>
        </div>
    );
}

function Form() {
    return (
        <form id="Form" action="/search/submit" method="post">
            <div>
                <dl>
                    <dt><label>Field of research: </label></dt>
                    <dd>
                        <span>Enter your desired field of research</span>
                        <input type="text" name="field-of-research" />
                    </dd>

                    <dt><label>Description: </label></dt>
                    <dd>
                        <span>Enter the description</span>
                        <input type="text" name="description" />
                    </dd>
                    
                    <dt><label>University: </label></dt>
                    <dd id="Uni-opt">
                        <span>Select your desired college</span>
                        <br />
                        <input id="HKU" type="checkbox" name="university" />
                        <label>HKU</label>
                        <input id="CUHK" type="checkbox" name="university" />
                        <label>CUHK</label>
                        <input id="UST" type="checkbox" name="university" />
                        <label>UST</label>
                    </dd>

                    <dt><label>Professor: </label></dt>
                    <dd>
                        <span>Enter the name of Prof</span>
                        <input id="Prof-name" type="text" name="prof-name" />
                    </dd>

                    <button id="Search-button" type="submit">Search</button>
                </dl>
            </div>
        </form>
    );
}
  
function RankingBoard() {
    const rankings = []; // replace this with actual data

    return (
        <div id="Ranking-board">
            <ul>
                <li>
                    <input type="radio" id="option1" name="option" />
                    <label for="option1">Option 1</label>
                    <span>100</span>
                </li>
                <li>
                    <input type="radio" id="option2" name="option" />
                    <label for="option2">Option 2</label>
                    <span>90</span>
                </li>
                <li>
                    <input type="radio" id="option3" name="option" />
                    <label for="option3">Option 3</label>
                    <span>80</span>
                </li>
            </ul>
        </div>
    );
}



export default Search