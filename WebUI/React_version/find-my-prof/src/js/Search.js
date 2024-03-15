import styles from '../css/Search.module.css';

import {Header, Footer} from './basic'



function Search() {
    return (
        <div className={styles.Search}>
            <Header />
            <MainContent />
            <Footer />
        </div>
    );
}

function MainContent() {
    return (
        <div id={styles.main}>
            <div id={styles.upper_half}>
                <ProfDetails />
                <ProfPic />
                <Me />
            </div>
			<div id={styles.lower_half}>
                <Form />
                <RankingBoard />
			</div>
		</div>
    );
}

function ProfDetails() {
    return (
        <div id={styles.Details}>
            <p>Details</p>
        </div>
    );
}

function ProfPic() {
    const url = "https://www.w3schools.com/howto/img_avatar.png";

    return (
        <div id={styles.Pic}>
            <img src={url} alt="Avatar" />
        </div>
    );
}

function Me() {
    return (
        <div id={styles.Me}>Booker</div>
    );
}


function Form() {
    return (
        <form id={styles.Form} action="/search/submit" method="post">
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
                    <dd id={styles.Uni_opt}>
                        <span>Select your desired college</span>
                        <br />
                        <input id={styles.HKU} type="checkbox" name="university" />
                        <label>HKU</label>
                        <input id={styles.CUHK} type="checkbox" name="university" />
                        <label>CUHK</label>
                        <input id={styles.UST} type="checkbox" name="university" />
                        <label>UST</label>
                    </dd>

                    <dt><label>Professor: </label></dt>
                    <dd>
                        <span>Enter the name of Prof</span>
                        <input id={styles.Prof_name} type="text" name="prof-name" />
                    </dd>

                    <button id={styles.Search_button} type="submit">Search</button>
                </dl>
            </div>
        </form>
    );
}
  
function RankingBoard() {
    const rankings = []; // replace this with actual data

    return (
        <div id={styles.Ranking_board}>
            <ul>
                <li>
                    <input type="radio" id={styles.option1} name="option" />
                    <label for="option1">Option 1</label>
                    <span>100</span>
                </li>
                <li>
                    <input type="radio" id={styles.option2} name="option" />
                    <label for="option2">Option 2</label>
                    <span>90</span>
                </li>
                <li>
                    <input type="radio" id={styles.option3} name="option" />
                    <label for="option3">Option 3</label>
                    <span>80</span>
                </li>
            </ul>
        </div>
    );
}



export default Search