import { Card, Layout, Space } from "antd";
import Message from "components/atoms/Chat/Message";
import PageTitle from "components/atoms/Text/PageTitle";
import Sidebar from "components/organisms/Sidebar";
import React, { useState } from "react";

const { Header, Content, Sider } = Layout;

const MainPage: React.FC = () => {
  const [collapsed, setCollapsed] = useState(false);

  return (
    <Layout style={{ minHeight: "100vh" }}>
      <Layout className="site-layout">
        <Header className="site-layout-background" style={{ padding: 15 }}>
          <PageTitle content="チャット画面" />
        </Header>
        <Content style={{ margin: "0 16px" }}>
          <div
            className="site-layout-background"
            style={{ padding: 24, minHeight: 360 }}
          >
            <Card size="small">
              <Message
                name="田中"
                message="集合何時にする？"
                image="https://joeschmoe.io/api/v1/jon"
                date="22:40"
              />
            </Card>
            <Card size="small">
              <Message
                name="伊藤"
                message="9時か10時"
                image="https://joeschmoe.io/api/v1/jia"
                date="22:43"
              />
            </Card>
            <Card size="small">
              <Message
                name="佐藤"
                message="じゃあ10時集合で"
                image="https://joeschmoe.io/api/v1/joe"
                date="22:48"
              />
            </Card>
            <Card size="small">
              <Message
                name="田中"
                message="了解"
                image="https://joeschmoe.io/api/v1/jon"
                date="22:50"
              />
            </Card>
            <Card size="small">
              <Message
                name="伊藤"
                message="寝坊するなよ"
                image="https://joeschmoe.io/api/v1/jia"
                date="22:59"
              />
            </Card>
            <Card size="small">
              <Message
                name="田中"
                message="お前もな"
                image="https://joeschmoe.io/api/v1/jon"
                date="23:02"
              />
            </Card>
          </div>
        </Content>
      </Layout>
    </Layout>
  );
};

export default MainPage;
