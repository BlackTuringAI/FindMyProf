import { useState } from 'react';
import styles from '../css/About.module.css';
import { Header, Footer } from './basic'

function About() {
    return (
        <div className={styles.About}>
            <Header />
            <MainContent />
            <Footer />
        </div>
    );
}

function MainContent() {
    // const blocks = [
    //     { title: 'block 1', description: 'I am a description' },
    //     { title: 'block 2', description: 'I am another description' },
    // ];
    return (
        <div id={styles.main}>
            <Banner />
            <Section1 />
            <Section2 />
            <Section3 />
        </div>
    );
}

function Banner() {
    return (
        <div id={styles.Banner}>
            <h1>Black Turing AI - Exploring the future of industry</h1>
            <p>Find Your Road to Research</p>
        </div>
    );
}

function Section1({blocks}) {
    const [currentBlock, setCurrentBlock] = useState(0);

    const handleClick = (index) => {
        setCurrentBlock(index);
    };

    return (
        <div id={styles.Section1}>
            <nav>
                <button onClick={() => handleClick('01')}>01</button>
                <button onClick={() => handleClick('02')}>02</button>
                <button onClick={() => handleClick('03')}>03</button>
                <button onClick={() => handleClick('02')}>03</button>
                <button onClick={() => handleClick('02')}>03</button>
                <button onClick={() => handleClick('02')}>03</button>
                <button onClick={() => handleClick('02')}>03</button>
            </nav>
            {(currentBlock === '01' || currentBlock === 0) && <Sec1_blk1 />}
            {currentBlock === '02' && <Sec1_blk2 />}
            {currentBlock === '03' && <Sec1_blk3 />}
            {/* <p>Our story</p>
            <h1>Section 1</h1>
            <p>I am a description</p>
            <img src={process.env.PUBLIC_URL + "/static/img/about_01.jpg"} alt="bruh" /> */}
        </div>
    );
}

function Sec1_blk1() {
    const url = "https://www.w3schools.com/howto/img_avatar.png";
    return (
        <div id={styles.Sec1_blk1}>
            <div>
                <p>Sec1</p>
                <h1>blk1_title</h1>
                <p>I am a description. xxxxxxxxxxxxxxxxxxxxxxxxsdadasdasdasdai drfvghaielrughkdjxxxxxxxxxx sadfesvaefcawsxxxxxxxxxx</p>
            </div>
            <img src={url} alt="bruh" />
        </div>
    );
}

function Sec1_blk2() {
    return (
        <div id={styles.Sec1_blk2}>
            <div>
                <p>Sec1</p>
                <h1>blk2_title</h1>
                <p>I am a description. xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx</p>
            </div>
            <img src={process.env.PUBLIC_URL + "/static/img/about_01.jpg"} alt="bruh" />
        </div>
    );
}

function Sec1_blk3() {
    return (
        <div id={styles.Sec1_blk3}>
            <div>
                <p>Sec1</p>
                <h1>blk3_title</h1>
                <p>I am a description. xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx</p>
            </div>
            <img src={process.env.PUBLIC_URL + "/static/img/about_01.jpg"} alt="bruh" />
        </div>
    );
}


function Section2() {
    return (
        <div id={styles.Section2}>
            <p>Our mission</p>
            <h1>Section 2</h1>
            <p>I am a description</p>
            <ul>    {/* add ainimation here */}
                <li><img src={process.env.PUBLIC_URL + "/static/img/about_02_01.jpg"} alt="bruh" /></li>
                <li><img src={process.env.PUBLIC_URL + "/static/img/about_02_02.jpg"} alt="bruh" /></li>
                <li><img src={process.env.PUBLIC_URL + "/static/img/about_02_03.jpg"} alt="bruh" /></li>
                <li><img src={process.env.PUBLIC_URL + "/static/img/about_02_04.jpg"} alt="bruh" /></li>
                {/* <li><img src={process.env.PUBLIC_URL + "/static/img/about_02_05.jpg"} alt="bruh" /></li> */}
                {/* <li><img src={process.env.PUBLIC_URL + "/static/img/about_02_06.jpg"} alt="bruh" /></li> */}
            </ul>
            
        </div>
    );
}

function Section3() {
    return (
        <div id={styles.Section3}>
            <p>Our key value</p>
            <h1>Section 3</h1>
            <p>I am a description</p>
            <ul>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
            </ul>
        </div>
    );
}

export default About;
