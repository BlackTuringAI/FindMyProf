import styles from '../css/Home.module.css';

import { Header, Footer } from './basic'


function Home() {
    return (
		<div className={styles.Home}>
			<Header />
			<MainContent />
			<Footer />
		</div>
    );
}

function MainContent() {
    return (
        <div id={styles.main}>
			<B0 />
			<B1 />
			<B2 />
			<B3 />
		</div>
    );
}

function B0() {
	return (
		<div id={styles.b0}>
			<h1>Find the right one<br /> Be professional</h1>
			<ul>
				<li>achievement</li>
				<li>achievement</li>
				<li>achievement</li>
				<li>achievement</li>
			</ul>
		</div>
	);
}

function B1() {
	return (
		<div id={styles.b1}>
			<h1>Video 1</h1>
			<video control='true'>
				<source src={process.env.PUBLIC_URL + "/static/video/test_video.mp4"} type="video/mp4" />
				Your browser does not support video playing.
			</video>
		</div>
	);
}

function B2() {
	return (
		<div id={styles.b2}>
			<h1>Video 2</h1>
			<video control='true'>
				<source src={process.env.PUBLIC_URL + "/static/video/test_video.mp4"} type="video/mp4" />
				Your browser does not support video playing.
			</video>
		</div>
	);
}

function B3() {
	return (
		<div id={styles.b3}>
			<h1>Wanna save time?<br />Agency to help you!</h1>
			<ul>
				<li>score <img src="https://www.w3schools.com/howto/img_avatar.png" /> name</li>
				<li>score <img src="https://www.w3schools.com/howto/img_avatar.png" /> name</li>
				<li>score <img src="https://www.w3schools.com/howto/img_avatar.png" /> name</li>
				<li>score <img src="https://www.w3schools.com/howto/img_avatar.png" /> name</li>
			</ul>
		</div>
	);
}



export default Home;
