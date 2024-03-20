import styles from '../css/News.module.css';

import { Header, Footer } from './basic'

function News() {
    return (
        <div className={styles.News}>
            <Header />
            <MainContent />
            <Footer />
        </div>
    );
}

function MainContent() {
    return (
        <div id={styles.main}>
            
        </div>
    );
}
function banner() {
    return (
        <div id={styles.banner}>
            <h1>News</h1>
        </div>
    );
}

export default News;
