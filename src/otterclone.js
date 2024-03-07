import React from "react";
import CustomNavbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import { Col, Container, Row } from "react-bootstrap";
import VoiceRecorder from "./components/Record";
import ChatCard from "./components/Chat";
import Translator from "./components/Translator";

function OtterClone() {
  return (
    <div>
      <Container fluid className="h-100">
        {/* <CustomNavbar /> */}
        <Row>
          <Col xs={2} md={2}>
            <Sidebar />
          </Col>
          <Col>
            <Row className="mx-2">
              <Col xs={6} md={6} className="px-0">
                <ChatCard>
                  <VoiceRecorder />
                </ChatCard>
              </Col>
              <Col xs={6} md={6} className="px-0">
                {/* <ChatCard /> */}
              </Col>
            </Row>
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default OtterClone;
