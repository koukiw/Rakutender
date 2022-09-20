import { Layout, Space } from "antd";
import PageTitle from "components/atoms/Text/PageTitle";
import EventCard from "components/organisms/EventCard";
import Sidebar from "components/organisms/Sidebar";
import React, { useState } from "react";

const { Header, Content, Footer, Sider } = Layout;

const SettingPage: React.FC = () => {
  const [collapsed, setCollapsed] = useState(false);

  return (
    <Layout style={{ minHeight: "100vh" }}>
      <Sider
        collapsible
        collapsed={collapsed}
        onCollapse={(value) => setCollapsed(value)}
      >
        <Sidebar />
      </Sider>

      <Layout className="site-layout">
        <Header className="site-layout-background" style={{ padding: 15 }}>
          <PageTitle content="設定" />
        </Header>

        <Content style={{ margin: "0 16px" }}>
          <div
            className="site-layout-background"
            style={{ padding: 24, minHeight: 360 }}
          >
            設定
          </div>
        </Content>
      </Layout>
    </Layout>
  );
};

export default SettingPage;
