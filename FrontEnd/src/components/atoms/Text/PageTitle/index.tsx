import { Typography } from "antd";
import React from "react";

const { Title } = Typography;

const PageTitle: React.FC<{ content: string }> = ({ content }) => (
  <Title level={4} style={{ color: "white" }}>
    {content}
  </Title>
);

export default PageTitle;
