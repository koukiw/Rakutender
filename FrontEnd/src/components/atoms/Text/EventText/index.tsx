import { Typography } from "antd";
import React from "react";

const { Text } = Typography;

const EventText: React.FC<{ content: string }> = ({ content }) => (
  <Text style={{ fontSize: "18px" }}>{content}</Text>
);

export default EventText;
