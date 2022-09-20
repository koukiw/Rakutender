import { Typography } from "antd";
import React from "react";

const { Title } = Typography;

const EventText: React.FC<{ content: string }> = ({ content }) => (
  <Title level={5}>{content}</Title>
);

export default EventText;
