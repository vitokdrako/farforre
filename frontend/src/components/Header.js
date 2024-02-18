import React from 'react';
import { Link } from 'react-router-dom';
import { Container, Row, Col, Image } from 'react-bootstrap';
import './Header.css'; // Задайте необхідні стилі тут
import background from './images/background.jpg';
import farforLogo from './images/farfor_logo.png';
import phoneIcon from './images/phone_icon.png';
import cartIcon from './images/cart_icon.png';
import accountIcon from './images/account_icon.png';

function Header() {
    return (
        <header style={{ backgroundImage: `url(${background})`, width: '100%', height: '800px', position: 'relative', overflow: 'hidden' }}>
            <Container fluid className="p-5">
                <Row className="mb-4 justify-content-center">
                    <Col xs={12} md={3} className="d-flex justify-content-center mb-2 mb-md-0">
                        <div className="button-container">
                            <Link to="/news">Новини</Link>
                        </div>
                    </Col>
                    <Col xs={12} md={3} className="d-flex justify-content-center mb-2 mb-md-0">
                        <div className="button-container">
                            <Link to="/about_us">Про нас</Link>
                        </div>
                    </Col>
                    <Col xs={12} md={3} className="d-flex justify-content-center mb-2 mb-md-0">
                        <div className="button-container">
                            <Link to="/gallery">Галерея</Link>
                        </div>
                    </Col>
                    <Col xs={12} md={3} className="d-flex justify-content-center">
                        <div className="button-container">
                            <Link to="/cart">Кошик</Link>
                            <Image src={cartIcon} alt="" className="img-fluid ml-2" />
                        </div>
                    </Col>
                </Row>
                <Row className="mb-4 justify-content-center">
                    <Col xs={12} md={3} className="d-flex justify-content-center">
                        <div className="social-container">
                            <Link to="/social">Соціальні мережі</Link>
                        </div>
                    </Col>
                    <Col xs={12} md={4} className="text-center">
                        <Link to="/"><Image src={farforLogo} alt="" className="img-fluid" /></Link>
                    </Col>
                    <Col xs={12} md={3} className="d-flex justify-content-center">
                        <div className="account-container">
                            <Link to="/register">Акаунт споживача</Link>
                            <Image src={accountIcon} alt="" className="img-fluid mr-2" />
                        </div>
                    </Col>
                </Row>
                <Row className="mb-4 justify-content-center">
                    <Col xs={12} md={3} className="d-flex justify-content-center">
                        <div className="button-container">
                            <Link to="rent_rules">Умови оренди</Link>
                        </div>
                    </Col>
                    <Col xs={12} md={3} className="d-flex justify-content-center">
                        <div className="button-container">
                            <Link to="/contact">
                            <Image src={phoneIcon} alt="" className="img-fluid" style={{ marginLeft: '-45px' }} />
                                Контакти
                            </Link>
                        </div>
                    </Col>

                    <Col xs={12} md={3} className="d-flex justify-content-center">
                        <div className="button-container">
                            <Link to="/search">Пошук</Link>
                        </div>
                    </Col>
                    <Col xs={12} md={3} className="d-flex justify-content-center">
                        <div className="button-container">
                            <Link to="/favorites">Збережене</Link>
                        </div>
                    </Col>
                </Row>
            </Container>
        </header>
    );
}

export default Header;
